"""Drive comp.html in headless Chromium: render frames in parallel pages, then one ffmpeg encode and mux.
Also stills (contact sheets at cue times with the safe zones drawn), a render check, and the edit's resolved plan."""
import asyncio, base64, json, math, os, pathlib, shutil, sys, time

from PIL import Image, ImageDraw

from . import tools
from .media import _font
from .server import serve

ARGS = ["--autoplay-policy=no-user-gesture-required", "--disable-background-timer-throttling", "--disable-renderer-backgrounding",
        "--mute-audio", "--force-color-profile=srgb"]


async def launch(p, ok: dict):
    b = ok.get("browser") or {}
    kw = {"headless": True, "args": ARGS}
    if b.get("channel"):
        kw["channel"] = b["channel"]
    elif b.get("executable"):
        kw["executable_path"] = b["executable"]
    return await p.chromium.launch(**kw)


async def open_page(browser, url, timeout=90000):
    page = await browser.new_page(viewport={"width": 1080, "height": 1920})
    errs = []
    page.on("pageerror", lambda e: errs.append(str(e)))
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" and "404" not in m.text else None)
    await page.goto(url, wait_until="load")
    await page.wait_for_function("window.REELR", timeout=timeout)
    failed = await page.evaluate("window.REELR.failed || null")
    if failed:
        raise SystemExit(f"the edit failed to load: {failed}")
    await page.evaluate("window.REELR.ready()")
    page._errs = errs
    return page


GRAB = "async ([i, q]) => { await window.REELR.frame(i); return window.REELR.canvas.toDataURL('image/jpeg', q).slice(23); }"
STALL = 45  # seconds one frame may take before the page is treated as stuck


class Progress:
    """A line every few seconds ("120/950 frames"), so a slow run never looks like a hung one."""
    def __init__(self, total, what="frames", every=5.0):
        self.total, self.what, self.every, self.n, self.t0 = total, what, every, 0, time.time()
        self.last = self.t0

    def tick(self):
        self.n += 1
        now = time.time()
        if now - self.last >= self.every and self.n < self.total:
            self.last = now
            print(f"  {self.n}/{self.total} {self.what}, {self.n / (now - self.t0):.0f} per s", file=sys.stderr, flush=True)


async def grab(browser, url, page, i, quality):
    """One frame as JPEG bytes. If the page stalls (a video that stops loading), reopen it and try once more, then fail
    with the frame and the media it was waiting for, never hang."""
    for attempt in (1, 2):
        try:
            return page, base64.b64decode(await asyncio.wait_for(page.evaluate(GRAB, [i, quality]), STALL))
        except asyncio.TimeoutError:
            try:
                srcs = await asyncio.wait_for(page.evaluate("i => window.REELR.need(i)", i), 5)
            except Exception:
                srcs = ["?"]
            print(f"  frame {i} stalled for {STALL} s waiting on {', '.join(srcs)}; reopening the page", file=sys.stderr, flush=True)
            try:
                await asyncio.wait_for(page.close(), 10)
            except Exception:
                pass
            if attempt == 2:
                raise SystemExit(f"rendering stalled at frame {i} waiting on {', '.join(srcs)}. "
                                 f"Run it again; if it repeats, use -j 2, or delete .engine/proxies and run ingest again.")
            page = await open_page(browser, url)


def _url(base, ws, reel_dir):
    return f"{base}/_engine/comp.html?reel={ws.rel(reel_dir)}&render"


async def _frames(ws, reel_dir, frames_dir, step=1, quality=0.92, jobs=None, t_from=0.0, t_to=None, progress=True):
    from playwright.async_api import async_playwright
    ok = ws.ok()
    srv, base = serve(ws.root)
    url = _url(base, ws, reel_dir)
    jobs = jobs or ok.get("jobs") or max(2, min(6, (os.cpu_count() or 4) // 2))
    async with async_playwright() as p:
        browser = await launch(p, ok)
        probe = await open_page(browser, url)
        fps, duration = await probe.evaluate("[window.REELR.fps, window.REELR.duration]")
        await probe.close()
        i0, i1 = round(t_from * fps), round(min(t_to or duration, duration) * fps)
        idx = list(range(i0, i1, step))
        shutil.rmtree(frames_dir, ignore_errors=True)
        frames_dir.mkdir(parents=True)
        per = math.ceil(len(idx) / jobs)
        t0, errs, prog = time.time(), [], Progress(len(idx), every=5.0 if progress else 15.0)

        async def worker(chunk):
            if not chunk:
                return
            page = await open_page(browser, url)
            for i in chunk:
                page, data = await grab(browser, url, page, i, quality)
                (frames_dir / f"{(i - i0) // step:05d}.jpg").write_bytes(data)
                prog.tick()
            errs.extend(page._errs)
            await page.close()

        await asyncio.gather(*(worker(idx[k * per:(k + 1) * per]) for k in range(jobs)))
        await browser.close()
    srv.shutdown()
    if progress:
        print(f"  {len(idx)} frames in {time.time() - t0:.0f} s ({len(idx) / max(0.1, time.time() - t0):.0f} fps)", file=sys.stderr)
    return fps, errs


def render(ws, reel_dir: pathlib.Path, preview=False, jobs=None, t_from=0.0, t_to=None, music=True) -> pathlib.Path:
    frames = reel_dir / ".frames"
    step = 2 if preview else 1
    fps, errs = asyncio.run(_frames(ws, reel_dir, frames, step=step, quality=0.8 if preview else 0.93, jobs=jobs, t_from=t_from, t_to=t_to))
    for e in errs:
        print(f"[page] {e}", file=sys.stderr)
    out = reel_dir / ("preview.mp4" if preview else "reel.mp4")
    rate = fps / step
    args = ["-framerate", f"{rate}", "-i", frames / "%05d.jpg"]
    wav = reel_dir / "track.wav"
    if music and wav.exists():
        args += ["-ss", f"{t_from}", "-i", wav, "-map", "0:v", "-map", "1:a", "-shortest"]
    if preview:
        args += ["-vf", "scale=540:960", "-c:v", "libx264", "-preset", "veryfast", "-crf", "28", "-maxrate", "900k", "-bufsize", "1800k",
                 "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k"]
    else:  # Instagram-friendly: H.264 high, 30 fps, 2 s GOP, AAC 48 kHz, loudness -14 LUFS, faststart
        args += ["-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", f"{fps}", "-g", f"{int(fps * 2)}"]
        if music and wav.exists():
            args += ["-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k"]
    tools.ff(*args, "-movflags", "+faststart", out)
    shutil.rmtree(frames, ignore_errors=True)
    print(f"{out} ({out.stat().st_size / 1e6:.1f} MB)")
    return out


async def _plan(ws, reel_dir):
    from playwright.async_api import async_playwright
    srv, base = serve(ws.root)
    async with async_playwright() as p:
        browser = await launch(p, ws.ok())
        page = await open_page(browser, _url(base, ws, reel_dir))
        plan = await page.evaluate("window.REELR.plan()")
        plan["errors"] = page._errs + await page.evaluate("window.REELR.errors")
        await browser.close()
    srv.shutdown()
    return plan


def plan(ws, reel_dir):
    return asyncio.run(_plan(ws, reel_dir))


async def _stills(ws, reel_dir, times, out_dir):
    from playwright.async_api import async_playwright
    srv, base = serve(ws.root)
    async with async_playwright() as p:
        browser = await launch(p, ws.ok())
        page = await open_page(browser, _url(base, ws, reel_dir))
        fps = await page.evaluate("window.REELR.fps")
        paths, prog = [], Progress(len(times), "stills")
        for k, t in enumerate(times):
            page, data = await grab(browser, _url(base, ws, reel_dir), page, round(t * fps), 0.9)
            pth = out_dir / f"still-{k:02d}.jpg"
            pth.write_bytes(data)
            paths.append(pth)
            prog.tick()
        await browser.close()
    srv.shutdown()
    return paths


def stills(ws, reel_dir, at=None, safe=True, cols=6) -> pathlib.Path:
    """A contact sheet of frames at the cue times (or at=[seconds]), each labelled, with the Reels UI zones overlaid."""
    if at:
        cues = [{"t": t, "label": f"{t:.2f}s"} for t in at]
    else:
        cues = plan(ws, reel_dir)["cues"]
    tmp = reel_dir / ".stills"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir()
    paths = asyncio.run(_stills(ws, reel_dir, [c["t"] for c in cues], tmp))
    tw, th, lab = 270, 480, 40
    rows = math.ceil(len(paths) / cols)
    sheet = Image.new("RGB", (cols * (tw + 8) + 8, rows * (th + lab + 8) + 8), (24, 24, 26))
    d, f = ImageDraw.Draw(sheet), _font(14)
    sx, sy = tw / 1080, th / 1920
    for k, (pth, c) in enumerate(zip(paths, cues)):
        x, y = 8 + (k % cols) * (tw + 8), 8 + (k // cols) * (th + lab + 8)
        im = Image.open(pth).convert("RGB").resize((tw, th))
        if safe:
            ov = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
            od = ImageDraw.Draw(ov)
            for box in ((0, 0, 1080, 220), (0, 1500, 1080, 1920), (930, 640, 1080, 1500)):
                od.rectangle([box[0] * sx, box[1] * sy, box[2] * sx, box[3] * sy], fill=(255, 60, 120, 70))
            im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
        sheet.paste(im, (x, y))
        d.text((x + 2, y + th + 4), f"{c['t']:.2f}s", fill=(240, 236, 230), font=f)
        d.text((x + 2, y + th + 21), c["label"][:34], fill=(160, 155, 148), font=f)
    out = reel_dir / "stills.jpg"
    sheet.save(out, quality=85)
    shutil.rmtree(tmp, ignore_errors=True)
    print(out)
    return out


def check(ws, reel_dir, every=3) -> int:
    """Draw every Nth frame (no encode) and report page errors and edit warnings. Exit code 1 on errors."""
    pl = plan(ws, reel_dir)
    fps, errs = asyncio.run(_frames(ws, reel_dir, reel_dir / ".check", step=every, quality=0.3, progress=False))
    shutil.rmtree(reel_dir / ".check", ignore_errors=True)
    errs = pl["errors"] + errs
    print(f"{pl['bars']} bars, {pl['duration']:.2f} s at {pl['bpm']:.1f} BPM; {len(pl['cuts'])} cuts, {len(pl['lines'])} text lines, {len(pl['cards'])} cards")
    holds = [c["t1"] - c["t0"] for c in pl["cuts"]]
    if holds:
        print(f"cuts: shortest {min(holds):.2f} s, longest {max(holds):.2f} s, first cut at {pl['cuts'][1]['t0'] if len(pl['cuts']) > 1 else 0:.2f} s")
    for w in pl["warnings"]:
        print(f"warning: {w}")
    for l in pl["lines"]:
        n = len(l["text"].replace("/", " ").split())
        if n > 6:
            print(f"warning: \"{l['text']}\" has {n} words; keep on-screen lines to about five")
        if l["b1"] - l["b0"] < 1:
            print(f"warning: \"{l['text']}\" is on screen for less than a beat")
    for e in errs:
        print(f"error: {e}")
    print("check passed" if not errs else f"check failed: {len(errs)} error(s)")
    return 1 if errs else 0


def pace(mp4: pathlib.Path):
    """Full-frame picture changes (ffmpeg scene score), as in the newsroom pace check."""
    import re, subprocess
    r = subprocess.run([tools.ffmpeg(), "-hide_banner", "-i", str(mp4), "-an", "-vf", "fps=10,select='gt(scene,0.15)',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    ts = [float(x) for x in re.findall(r"pts_time:([0-9.]+)", r.stderr)]
    dur = tools.video_info(mp4)["dur"]
    gaps = [b - a for a, b in zip([0.0] + ts, ts + [dur])]
    print(f"{len(ts)} picture changes in {dur:.1f} s = {10 * len(ts) / max(dur, 0.1):.1f} per 10 s; first at {ts[0] if ts else dur:.2f} s; "
          f"longest hold {max(gaps):.2f} s")
