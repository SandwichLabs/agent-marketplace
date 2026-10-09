"""The curated track catalog: list it, and fetch one track on demand into music/ with a licence note beside it."""
import json, pathlib, sys, time, urllib.request

from .ws import ENGINE

CATALOG = ENGINE.parent / "reference" / "catalog.json"


def load() -> list:
    return json.loads(CATALOG.read_text())["tracks"]


def listing():
    for t in load():
        fits = "30/60 s" if t["drop_60s"] else "30 s"
        credit = "credit needed" if t["credit"] else "no credit"
        print(f"{t['id']:32s} {t['bpm']:5.1f} BPM  {t['title']} — {t['artist']} · {t['genre']}, {t['feel']} · {fits} · {t['source']}, {credit}")


def fetch(ws, track_id: str) -> pathlib.Path:
    t = next((x for x in load() if x["id"] == track_id), None)
    if not t:
        sys.exit(f"no catalog track {track_id!r}; see `reelmaker catalog`")
    ws.music.mkdir(parents=True, exist_ok=True)
    out = ws.music / f"{t['id']}.mp3"
    if not out.exists():
        req = urllib.request.Request(t["url"], headers={"User-Agent": "Mozilla/5.0 (reelmaker)"})
        with urllib.request.urlopen(req, timeout=60) as r, open(out, "wb") as f:
            f.write(r.read())
    note = [f"{t['title']} — {t['artist']}", f"Source: {t['source']} ({t['url']})", f"Licence: {t['license']} ({t['license_url']})",
            f"Fetched: {time.strftime('%Y-%m-%d')}"]
    note += ["", "Credit (put this in the post caption):", t["credit"]] if t["credit"] else ["", "No credit required."]
    (ws.music / f"{t['id']}.license.txt").write_text("\n".join(note) + "\n")
    print(f"{ws.rel(out)} ({out.stat().st_size / 1e6:.1f} MB) and {t['id']}.license.txt")
    if t["credit"]:
        print("this track needs a credit line in the caption (it's in the licence note)")
    return out
