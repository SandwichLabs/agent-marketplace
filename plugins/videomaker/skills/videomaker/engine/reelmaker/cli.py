"""reelmaker: beat-matched promo reels from a folder of clips.

  reelmaker doctor                 set up / check everything (ffmpeg, a render browser, the kit, a smoke render)
  reelmaker ingest                 clips/ -> proxies, shots at scene cuts, thumbnails, contact sheets
  reelmaker shots [--untagged]     the shot library as a table
  reelmaker tag SHOT TAG... [--note N] [--name N]   tag shots: an id, ids joined by commas, or a pattern ("clip-*"); "exclude" keeps them out
  reelmaker catalog                the curated royalty-free tracks (reference/catalog.json)
  reelmaker fetch ID               download a catalog track into music/ with its licence note
  reelmaker analyze TRACK          tempo, bars, energy and drop candidates of a track
  reelmaker music TRACK REEL       cut the track to the reel's bar window with the drop on --drop-bar
  reelmaker check REEL             draw every 3rd frame, report errors and edit warnings
  reelmaker stills REEL            contact sheet at every cue with the Reels UI zones overlaid
  reelmaker preview REEL           fast 540p draft (preview.mp4)
  reelmaker render REEL            the final 1080x1920 reel.mp4 (Instagram encode, -14 LUFS)
  reelmaker board REEL             board.html: timeline, thumbnails, text, preview, caption
  reelmaker storyboard             rebuild kit/storyboard.html (the kit's motion storyboard)
  reelmaker pace MP4               picture changes per 10 s
  reelmaker open PATH              open a file in the default app

REEL is a folder name under reels/ (or a path). The workspace is the current folder, or --ws / $REEL_WORKSPACE.
"""
import argparse, json, os, pathlib, subprocess, sys

from .ws import Workspace, find_workspace, die, is_mac, STORYBOARD


def need_setup(ws):
    ok = ws.ok()
    if not ok:
        die("not set up in this folder yet: run `reelmaker doctor` first")
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(prog="reelmaker", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ws", help="workspace folder (default: current folder)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("doctor"); s.add_argument("--quick", action="store_true", help="trust a previous successful check")
    sub.add_parser("init")
    s = sub.add_parser("ingest"); s.add_argument("--only", nargs="*", help="file names to (re)ingest")
    s = sub.add_parser("shots"); s.add_argument("--untagged", action="store_true"); s.add_argument("--json", action="store_true")
    s = sub.add_parser("tag"); s.add_argument("shot", help="a shot id, several joined by commas, or a pattern like 'clip-name-*'"); s.add_argument("tags", nargs="*"); s.add_argument("--note"); s.add_argument("--name"); s.add_argument("--replace", action="store_true")
    sub.add_parser("catalog")
    s = sub.add_parser("fetch"); s.add_argument("id")
    s = sub.add_parser("analyze"); s.add_argument("track"); s.add_argument("--bpm", type=float, default=124)
    s = sub.add_parser("music"); s.add_argument("track"); s.add_argument("reel")
    s.add_argument("--bars", type=int, default=16, help="reel length in bars (16 ≈ 30 s at 124 BPM)")
    s.add_argument("--drop-bar", type=int, default=9, help="reel bar the drop lands on (1-based)")
    s.add_argument("--drop-at", type=float, help="seconds into the song where the drop is (overrides detection)")
    s.add_argument("--start-bar", type=int, help="song bar to start on (0-based, from `analyze`)")
    s.add_argument("--ending", choices=["fade", "song"], default="fade", help="fade out, or end on the song's own last bars")
    s.add_argument("--bpm", type=float, default=124)
    for name in ("check", "preview", "render", "board"):
        s = sub.add_parser(name); s.add_argument("reel")
        if name == "render":
            s.add_argument("--from", dest="t_from", type=float, default=0.0); s.add_argument("--to", dest="t_to", type=float)
            s.add_argument("--no-music", action="store_true", help="silent video (the music is added later in the app)")
        if name in ("render", "preview"):
            s.add_argument("-j", "--jobs", type=int)
        if name == "board":
            s.add_argument("--title")
    s = sub.add_parser("stills"); s.add_argument("reel"); s.add_argument("--at", help="comma-separated seconds"); s.add_argument("--no-safe", action="store_true")
    sub.add_parser("storyboard")
    s = sub.add_parser("pace"); s.add_argument("mp4")
    s = sub.add_parser("open"); s.add_argument("path")
    a = ap.parse_args(argv)
    ws = find_workspace(a.ws)
    os.environ["REEL_WORKSPACE"] = str(ws.root)

    if a.cmd == "init":
        ws.init(); print(f"workspace ready: {ws.root}")
    elif a.cmd == "doctor":
        from .doctor import doctor
        doctor(ws, quick=a.quick)
    elif a.cmd == "ingest":
        ok = need_setup(ws)
        from .media import ingest
        ingest(ws, ok["proxy"], only=a.only)
    elif a.cmd == "shots":
        lib = ws.library()
        rows = [(k, v) for k, v in lib["shots"].items() if not a.untagged or not v.get("tags")]
        if a.json:
            print(json.dumps(dict(rows), indent=1)); return
        for k, v in rows:
            print(f"{k:28s} {v['b'] - v['a']:5.1f}s  {(v.get('name') or ''):14s} {' '.join(v.get('tags', [])):28s} {v.get('note', '')}")
        print(f"{len(rows)} shots")
    elif a.cmd == "tag":
        import fnmatch
        lib = ws.library()
        ids = []
        for pat in filter(None, a.shot.split(",")):
            hit = fnmatch.filter(lib["shots"], pat)
            if not hit:
                die(f"no shot {pat}")
            ids += [i for i in sorted(hit) if i not in ids]
        if a.name is not None and len(ids) > 1:
            die("--name is for one shot")
        for sid in ids:
            s = lib["shots"][sid]
            s["tags"] = a.tags if a.replace else sorted(set(s.get("tags", [])) | set(a.tags))
            if a.note is not None: s["note"] = a.note
            if a.name is not None: s["name"] = a.name
            print(f"{sid}: {' '.join(s['tags'])} {s.get('note', '')}")
        ws.save_library(lib)
    elif a.cmd == "catalog":
        from .catalog import listing
        listing()
    elif a.cmd == "fetch":
        from .catalog import fetch
        fetch(ws, a.id)
    elif a.cmd == "analyze":
        from .music import analyze, table
        print(table(analyze(pathlib.Path(a.track), a.bpm)))
    elif a.cmd == "music":
        from .music import make_track
        make_track(a.track, ws.reel(a.reel), bars=a.bars, drop_bar=a.drop_bar, drop_at=a.drop_at, start_bar=a.start_bar, ending=a.ending, bpm_hint=a.bpm)
    elif a.cmd == "check":
        need_setup(ws)
        from .render import check
        sys.exit(check(ws, ws.reel(a.reel)))
    elif a.cmd == "stills":
        need_setup(ws)
        from .render import stills
        stills(ws, ws.reel(a.reel), at=[float(x) for x in a.at.split(",")] if a.at else None, safe=not a.no_safe)
    elif a.cmd in ("preview", "render"):
        need_setup(ws)
        from .render import render
        render(ws, ws.reel(a.reel), preview=a.cmd == "preview", jobs=a.jobs, **({"t_from": a.t_from, "t_to": a.t_to, "music": not a.no_music} if a.cmd == "render" else {}))
    elif a.cmd == "board":
        need_setup(ws)
        from .board import build
        build(ws, ws.reel(a.reel), title=a.title)
    elif a.cmd == "storyboard":
        subprocess.run([sys.executable, str(STORYBOARD / "storyboard.py"), str(ws.kit)], check=True)
    elif a.cmd == "pace":
        from .render import pace
        pace(pathlib.Path(a.mp4))
    elif a.cmd == "open":
        subprocess.run(["open" if is_mac() else "xdg-open", a.path])


if __name__ == "__main__":
    main()
