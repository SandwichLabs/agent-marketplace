"""Setup check: find or fetch ffmpeg, find a browser that can render, learn which proxy codec it decodes, seed the
kit, run a one-second smoke render, and record it all in .engine/ok.json. Idempotent; safe to run any time."""
import asyncio, json, os, pathlib, platform, shutil, subprocess, sys, time

from . import tools
from .ws import STARTER_KIT, RUNTIME, is_mac

PROBE = """async (urls) => {
  const out = {};
  for (const [name, url] of Object.entries(urls)) {
    try {
      const v = document.createElement('video'); v.muted = true; v.src = url;
      await new Promise((res, rej) => { v.onloadeddata = res; v.onerror = () => rej(new Error('decode')); setTimeout(() => rej(new Error('timeout')), 8000); });
      await new Promise(res => { v.onseeked = res; v.currentTime = 1.0; });
      const c = document.createElement('canvas'); c.width = 64; c.height = 64; const x = c.getContext('2d');
      x.drawImage(v, 0, 0, 64, 64); const d = x.getImageData(0, 0, 64, 64).data;
      let s = 0; for (let i = 0; i < d.length; i += 4) s += d[i] + d[i + 1] + d[i + 2];
      out[name] = s > 64 * 64 * 30;
    } catch (e) { out[name] = false; }
  }
  return out;
}"""


def step(msg):
    print(f"• {msg}", flush=True)


def _make_test_clips(dir_: pathlib.Path):
    dir_.mkdir(parents=True, exist_ok=True)
    src = ["-f", "lavfi", "-i", "testsrc2=size=360x640:rate=30:duration=2"]
    clips = {}
    if not (dir_ / "h264.mp4").exists():
        tools.ff(*src, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-g", "6", dir_ / "h264.mp4")
    clips["h264"] = dir_ / "h264.mp4"
    try:
        if not (dir_ / "vp9.webm").exists():
            tools.ff(*src, "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "40", "-g", "6", "-deadline", "realtime", dir_ / "vp9.webm")
        clips["vp9"] = dir_ / "vp9.webm"
    except subprocess.CalledProcessError:
        pass
    return clips


async def _try_browser(cand, ws, clips):
    from playwright.async_api import async_playwright
    from .render import ARGS
    from .server import serve
    srv, base = serve(ws.root)
    try:
        async with async_playwright() as p:
            kw = {"headless": True, "args": ARGS}
            if cand.get("channel"):
                kw["channel"] = cand["channel"]
            b = await p.chromium.launch(**kw)
            page = await b.new_page()
            await page.goto(f"{base}/_rt/fx.js")
            res = await page.evaluate(PROBE, {k: f"{base}/{ws.rel(v)}" for k, v in clips.items()})
            ver = b.version
            await b.close()
            return {"ok": True, "codecs": res, "version": ver}
    except Exception as e:
        return {"ok": False, "error": str(e).splitlines()[0][:200]}
    finally:
        srv.shutdown()


def _install_chromium():
    step("downloading Chromium for rendering (one time, about 100–170 MB)…")
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)


def doctor(ws, quick=False) -> dict:
    t0 = time.time()
    ws.init()
    ok = ws.ok()
    if quick and ok.get("version") == 1 and ok.get("ffmpeg") and pathlib.Path(ok["ffmpeg"]).exists():
        print(f"ready (checked {ok.get('checked')}): {ok['browser_name']}, {ok['proxy']} proxies, {ok['jobs']} render workers")
        return ok
    if not RUNTIME.exists():
        raise SystemExit(f"the video-template skill's runtime isn't next to this skill ({RUNTIME}); install the whole videomaker plugin")

    step("ffmpeg")
    hit = tools.find(fetch=False)
    how = "found"
    if not hit:
        print("  not installed; fetching a static build (no admin password needed)…", flush=True)
        hit = tools.find(fetch=True)
        how = "downloaded"
    ff, fp = hit
    enc = tools.encoders()
    if "libx264" not in enc:
        raise SystemExit(f"{ff} has no libx264 encoder; install a full ffmpeg build")
    print(f"  {how}: {ff}")

    step("test clips")
    clips = _make_test_clips(ws.engine / "selftest")

    step("browser")
    cands = [("Google Chrome", {"channel": "chrome"}), ("Chromium (Playwright)", {})]
    chosen = None
    for name, cand in cands:
        r = asyncio.run(_try_browser(cand, ws, clips))
        err = r.get("error", "")
        if not r["ok"] and not cand and ("Executable doesn't exist" in err or "playwright install" in err):
            _install_chromium()
            r = asyncio.run(_try_browser(cand, ws, clips))
        if not r["ok"]:
            print(f"  {name}: not available ({r['error']})")
            continue
        codecs = r["codecs"]
        print(f"  {name} {r['version']}: H.264 {'yes' if codecs.get('h264') else 'no'}, VP9 {'yes' if codecs.get('vp9') else 'no'}")
        if codecs.get("h264"):
            chosen = (name, cand, "h264"); break
        if codecs.get("vp9") and not chosen:
            chosen = (name, cand, "vp9")
    if not chosen:
        raise SystemExit("no browser could decode a test clip; install Google Chrome and run doctor again")
    name, cand, codec = chosen
    if codec == "vp9" and "libvpx-vp9" not in enc:
        raise SystemExit("the render browser needs VP9 proxies but this ffmpeg has no libvpx-vp9; install Google Chrome (H.264) or a full ffmpeg")

    if not (ws.kit / "brand.json").exists():
        step("kit: none in this folder yet; copying the neutral starter kit (run the video-template skill to make it yours)")
        shutil.copytree(STARTER_KIT, ws.kit, dirs_exist_ok=True)

    cpus = os.cpu_count() or 4
    ok = {"version": 1, "ffmpeg": ff, "ffprobe": fp, "browser": cand, "browser_name": name, "proxy": codec,
          "jobs": max(2, min(6, cpus // 2)), "platform": f"{platform.system()} {platform.machine()}",
          "checked": time.strftime("%Y-%m-%d %H:%M")}
    ws.ok_path.write_text(json.dumps(ok, indent=1))

    step("smoke render (1 s)")
    _smoke(ws)
    ok["setup_seconds"] = round(time.time() - t0, 1)
    ws.ok_path.write_text(json.dumps(ok, indent=1))
    print(f"\nready in {ok['setup_seconds']} s: {name}, {codec} proxies, {ok['jobs']} render workers → {ws.rel(ws.ok_path)}")
    return ok


def _smoke(ws):
    from .render import render
    d = ws.engine / "selftest" / "reel"
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    bpm, bars = 120, 1
    spb = 60 / bpm
    (d / "beats.json").write_text(json.dumps({"track": "track.m4a", "bpm": bpm, "beats": [i * spb for i in range(bars * 4)], "duration": bars * 4 * spb}))
    (d / "edit.json").write_text(json.dumps({"sections": [{"name": "test", "bars": [1, 1], "cut": 2, "shots": ["selftest"]}],
                                             "text": [{"at": "1", "len": 4, "style": "stack", "text": "SETUP/CHECK."}]}))
    tools.ff("-f", "lavfi", "-i", f"sine=frequency=880:duration={bars * 4 * spb}", "-ar", "48000", d / "track.wav")
    os.environ.setdefault("REEL_WORKSPACE", str(ws.root))
    out = render(ws, d, preview=False, t_to=1.0)
    info = tools.video_info(out)
    if not info or info["dur"] < 0.9:
        raise SystemExit(f"smoke render produced a bad file: {out}")
    shutil.rmtree(d, ignore_errors=True)
