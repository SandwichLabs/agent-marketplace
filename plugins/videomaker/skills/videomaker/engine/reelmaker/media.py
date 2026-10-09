"""Ingest: every clip and photo in clips/ -> a seek-friendly proxy, shots split at scene cuts, a thumbnail per shot,
and contact sheets Claude reads to tag the shots. Results go in .engine/library.json and are cached by size+mtime."""
import json, math, pathlib, re, shutil, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

from . import tools
from .ws import IMAGE_EXT, VIDEO_EXT, is_mac

MIN_SHOT, MAX_SHOT, SCENE = 0.5, 6.0, 0.18


def slug(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "clip"


def proxy_args(codec: str):
    # short GOP (a keyframe every 6 frames) so the renderer's frame-exact seeks decode almost nothing
    if codec == "vp9":
        return ["-c:v", "libvpx-vp9", "-crf", "30", "-b:v", "0", "-g", "6", "-row-mt", "1", "-deadline", "good", "-cpu-used", "5"]
    return ["-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-g", "6", "-bf", "0", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]


def make_proxy(src: pathlib.Path, dst: pathlib.Path, info: dict, codec: str):
    short = min(info["w"], info["h"]) or 1080
    target = min(1080, short)
    vf = f"scale='if(gt(iw,ih),-2,{target})':'if(gt(iw,ih),{target},-2)'"
    if info.get("fps", 30) > 60.5:
        vf += ",fps=60"
    if info.get("hdr"):
        # iPhones record HDR (HLG) by default; without tone-mapping the SDR proxy looks washed out
        tm = "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,"
        try:
            tools.ff("-i", src, "-an", "-vf", tm + vf, *proxy_args(codec), "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", dst)
            return
        except subprocess.CalledProcessError:
            print(f"  warning: this ffmpeg can't tone-map HDR (no zscale); {src.name} may look washed out", file=sys.stderr)
    tools.ff("-i", src, "-an", "-vf", vf, *proxy_args(codec), dst)


def scene_cuts(path: pathlib.Path, debounce=0.3) -> list:
    """Hard cuts score 0.18-0.45 on ffmpeg's scene metric and are followed by a few frames of 0.08-0.17 echoes, so:
    threshold, then keep only the strongest hit inside each debounce window."""
    r = subprocess.run([tools.ffmpeg(), "-hide_banner", "-i", str(path), "-an", "-filter:v",
                        f"select='gt(scene,{SCENE})',metadata=print:key=lavfi.scene_score", "-f", "null", "-"], capture_output=True, text=True)
    hits = [(float(t), float(s)) for t, s in re.findall(r"pts_time:([0-9.]+)\s*\n.*?lavfi\.scene_score=([0-9.]+)", r.stderr)]
    cuts = []
    for t, s in hits:
        if cuts and t - cuts[-1][0] < debounce:
            if s > cuts[-1][1]:
                cuts[-1] = (t, s)
            continue
        cuts.append((t, s))
    return [t for t, _ in cuts]


def split_shots(dur: float, cuts: list, fps: float) -> list:
    pad = 2 / max(fps, 24)                                  # trim two frames inside each detected cut
    bounds = [0.0] + [c for c in cuts if 0.2 < c < dur - 0.2] + [dur]
    shots = []
    for a, b in zip(bounds, bounds[1:]):
        a2, b2 = a + (pad if a > 0 else 0), b - (pad if b < dur else 0.04)
        if b2 - a2 < MIN_SHOT:
            continue
        n = max(1, math.ceil((b2 - a2) / MAX_SHOT)) if b2 - a2 > MAX_SHOT * 1.5 else 1
        step = (b2 - a2) / n
        shots += [(round(a2 + k * step, 3), round(a2 + (k + 1) * step, 3)) for k in range(n)]
    return shots


def thumb(src: pathlib.Path, t: float, dst: pathlib.Path, w=216, h=384):
    tools.ff("-ss", f"{t:.3f}", "-i", src, "-frames:v", "1", "-vf",
             f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}", "-q:v", "4", dst)


def heic_to_jpg(src: pathlib.Path, dst: pathlib.Path) -> bool:
    if is_mac() and shutil.which("sips"):
        return subprocess.run(["sips", "-s", "format", "jpeg", str(src), "--out", str(dst)], capture_output=True).returncode == 0
    try:
        tools.ff("-i", src, dst)
        return True
    except subprocess.CalledProcessError:
        return False


def _font(size):
    for f in ("/System/Library/Fonts/SFNSMono.ttf", "/System/Library/Fonts/Menlo.ttc", "/usr/share/fonts/dejavu-sans-mono-fonts/DejaVuSansMono.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            continue
    return ImageFont.load_default()


def contact_sheets(ws, lib: dict, per=24, cols=6):
    """Pages of thumbnails labelled with shot id and length; returns the sheet paths."""
    for old in ws.sheets.glob("sheet-*.jpg"):
        old.unlink()
    ids = [i for i in lib["shots"] if (ws.thumbs / f"{i}.jpg").exists()]
    out, f = [], _font(15)
    tw, th, lab = 216, 384, 44
    for page in range(math.ceil(len(ids) / per)):
        chunk = ids[page * per:(page + 1) * per]
        rows = math.ceil(len(chunk) / cols)
        sheet = Image.new("RGB", (cols * (tw + 8) + 8, rows * (th + lab + 8) + 8), (24, 24, 26))
        d = ImageDraw.Draw(sheet)
        for k, i in enumerate(chunk):
            x, y = 8 + (k % cols) * (tw + 8), 8 + (k // cols) * (th + lab + 8)
            sheet.paste(Image.open(ws.thumbs / f"{i}.jpg").convert("RGB"), (x, y))
            s = lib["shots"][i]
            d.text((x + 2, y + th + 4), i, fill=(240, 236, 230), font=f)
            d.text((x + 2, y + th + 23), f"{s['b'] - s['a']:.1f}s  {' '.join(s.get('tags', []))[:20]}", fill=(160, 155, 148), font=f)
        p = ws.sheets / f"sheet-{page + 1:02d}.jpg"
        sheet.save(p, quality=82)
        out.append(p)
    return out


def ingest(ws, codec: str, only=None):
    ws.init()
    lib = ws.library()
    by_file = {s["file"]: k for k, s in lib["sources"].items()}
    files = sorted(p for p in ws.clips.rglob("*") if p.is_file() and p.suffix.lower() in VIDEO_EXT | IMAGE_EXT and not p.name.startswith("."))
    if only:
        files = [p for p in files if p.name in only]
    if not files:
        print(f"no clips found in {ws.clips} (videos: {', '.join(sorted(VIDEO_EXT))}; photos: {', '.join(sorted(IMAGE_EXT))})")
        return lib
    seen, new = set(), 0
    for n, p in enumerate(files, 1):
        rel = ws.rel(p)
        st = p.stat()
        sig = f"{st.st_size}:{int(st.st_mtime)}"
        key = by_file.get(rel)
        if key and lib["sources"][key].get("sig") == sig and (lib["sources"][key]["kind"] == "image" or ((ws.root / lib["sources"][key]["proxy"]).exists() and lib["sources"][key].get("codec") == codec)):
            seen.add(key)
            continue
        if not key:
            base, key, k = slug(p.stem), slug(p.stem), 2
            while key in lib["sources"]:
                key, k = f"{base}-{k}", k + 1
        # drop this source's old shots
        for sid in [s for s, v in lib["shots"].items() if v["src"] == key]:
            del lib["shots"][sid]
        print(f"[{n}/{len(files)}] {rel}", flush=True)
        if p.suffix.lower() in IMAGE_EXT:
            use = p
            if p.suffix.lower() == ".heic":
                use = ws.proxies / f"{key}.jpg"
                if not heic_to_jpg(p, use):
                    print(f"  skipped: can't convert {p.name} (HEIC); export it as JPEG", file=sys.stderr)
                    continue
            with Image.open(use) as im:
                im = ImageOps.exif_transpose(im)
                w, h = im.size
                ImageOps.fit(im.convert("RGB"), (216, 384)).save(ws.thumbs / f"{key}-01.jpg", quality=85)
            lib["sources"][key] = {"file": rel, "kind": "image", "url": ws.rel(use), "w": w, "h": h, "sig": sig}
            lib["shots"][f"{key}-01"] = {"src": key, "a": 0.0, "b": 8.0, "tags": [], "note": "", "name": None, "kind": "image"}
        else:
            info = tools.video_info(p)
            if not info or info["dur"] < MIN_SHOT:
                print("  skipped: no video stream or too short", file=sys.stderr)
                continue
            ext = "webm" if codec == "vp9" else "mp4"
            prox = ws.proxies / f"{key}.{ext}"
            make_proxy(p, prox, info, codec)
            pinfo = tools.video_info(prox)
            cuts = scene_cuts(prox)
            shots = split_shots(pinfo["dur"], cuts, pinfo["fps"])
            lib["sources"][key] = {"file": rel, "kind": "video", "proxy": ws.rel(prox), "url": ws.rel(prox), "w": pinfo["w"], "h": pinfo["h"],
                                   "fps": pinfo["fps"], "dur": pinfo["dur"], "sig": sig, "codec": codec}
            for k, (a, b) in enumerate(shots, 1):
                sid = f"{key}-{k:02d}"
                lib["shots"][sid] = {"src": key, "a": a, "b": b, "tags": [], "note": "", "name": None}
                thumb(prox, (a + b) / 2, ws.thumbs / f"{sid}.jpg")
            print(f"  {pinfo['w']}x{pinfo['h']} {pinfo['dur']:.1f}s{' (HDR, tone-mapped)' if info.get('hdr') else ''} -> {len(shots)} shots", flush=True)
        seen.add(key)
        new += 1
        ws.save_library(lib)
    # sources whose files are gone
    if not only:
        for key in [k for k in lib["sources"] if k not in seen]:
            for sid in [s for s, v in lib["shots"].items() if v["src"] == key]:
                del lib["shots"][sid]
            del lib["sources"][key]
    ws.save_library(lib)
    sheets = contact_sheets(ws, lib)
    untagged = sum(1 for s in lib["shots"].values() if not s.get("tags"))
    print(f"\n{len(lib['sources'])} sources, {len(lib['shots'])} shots ({new} sources new or changed, {untagged} shots untagged)")
    print("contact sheets:\n  " + "\n  ".join(ws.rel(p) for p in sheets))
    return lib
