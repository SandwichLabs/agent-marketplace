"""ffmpeg / ffprobe resolution and small run helpers.

Order: the paths recorded by `doctor` in .engine/ok.json, then PATH, then Homebrew's prefixes, then a static build
fetched by the static-ffmpeg package (no admin password, no Homebrew needed).
"""
import json, os, pathlib, shutil, subprocess

_cache = {}


def _from_ok():
    root = os.environ.get("REEL_WORKSPACE") or os.getcwd()
    ok = pathlib.Path(root) / ".engine" / "ok.json"
    if ok.exists():
        try:
            d = json.loads(ok.read_text())
            if d.get("ffmpeg") and pathlib.Path(d["ffmpeg"]).exists():
                return d["ffmpeg"], d["ffprobe"]
        except Exception:
            pass
    return None


def find(fetch=False):
    """-> (ffmpeg, ffprobe) or None. fetch=True downloads a static build if nothing else is found."""
    if "ff" in _cache:
        return _cache["ff"]
    force = os.environ.get("REEL_FFMPEG")  # "static" = always the static build (to test a machine without one)
    if force == "static":
        from static_ffmpeg import run
        _cache["ff"] = run.get_or_fetch_platform_executables_else_raise()
        return _cache["ff"]
    hit = _from_ok()
    if not hit:
        ff, fp = shutil.which("ffmpeg"), shutil.which("ffprobe")
        if ff and fp:
            hit = ff, fp
    if not hit:
        for prefix in ("/opt/homebrew/bin", "/usr/local/bin", "/home/linuxbrew/.linuxbrew/bin"):
            ff, fp = pathlib.Path(prefix, "ffmpeg"), pathlib.Path(prefix, "ffprobe")
            if ff.exists() and fp.exists():
                hit = str(ff), str(fp)
                break
    if not hit and fetch:
        from static_ffmpeg import run  # downloads once into the package's own folder
        hit = run.get_or_fetch_platform_executables_else_raise()
    if hit:
        _cache["ff"] = hit
    return hit


def ffmpeg():
    hit = find(fetch=True)
    return hit[0]


def ffprobe():
    hit = find(fetch=True)
    return hit[1]


def run(args, **kw):
    kw.setdefault("check", True)
    return subprocess.run(args, **kw)


def ff(*args, quiet=True, **kw):
    base = [ffmpeg(), "-y", "-hide_banner"] + (["-loglevel", "error"] if quiet else [])
    return run(base + [str(a) for a in args], **kw)


def probe(path) -> dict:
    out = run([ffprobe(), "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(path)],
              capture_output=True, text=True).stdout
    return json.loads(out)


def video_info(path) -> dict:
    """duration, display width/height (rotation applied), fps, has_audio."""
    d = probe(path)
    v = next((s for s in d["streams"] if s["codec_type"] == "video"), None)
    if not v:
        return {}
    w, h = int(v.get("width", 0)), int(v.get("height", 0))
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(float(sd["rotation"]))
    rot = int(v.get("tags", {}).get("rotate", rot) or rot)
    if abs(rot) % 180 == 90:
        w, h = h, w
    num, den = (v.get("avg_frame_rate") or v.get("r_frame_rate") or "30/1").split("/")
    fps = float(num) / float(den) if float(den) else 30.0
    dur = float(v.get("duration") or d["format"].get("duration") or 0)
    hdr = v.get("color_transfer") in ("arib-std-b67", "smpte2084")  # HLG (iPhone default) or PQ
    return {"w": w, "h": h, "fps": round(fps, 3), "dur": round(dur, 3), "codec": v.get("codec_name"), "hdr": hdr,
            "audio": any(s["codec_type"] == "audio" for s in d["streams"])}


def encoders() -> str:
    return run([ffmpeg(), "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
