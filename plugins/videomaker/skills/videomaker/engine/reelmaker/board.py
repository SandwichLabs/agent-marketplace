"""board.html: one self-contained page per reel, to publish as an artifact or open locally. The bar grid with the
track's energy and the sections, a thumbnail per cut, every on-screen line, the preview video and the caption."""
import base64, html, json, pathlib

from .render import plan as get_plan

CSS = """
:root { --bg:#F5F3EF; --panel:#FFFFFF; --fg:#1B1A18; --muted:#6E6860; --line:#DEDAD3; --accent:%(accent)s; --accent-ink:#1B1A18;
  --display:'Space Grotesk', system-ui, sans-serif; --body:'DM Sans', system-ui, sans-serif; --mono:'Space Mono', ui-monospace, Menlo, monospace; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#0F0F11; --panel:#17171A; --fg:#EEECE8; --muted:#A09A93; --line:#2B2A2E; color-scheme:dark } }
:root[data-theme="dark"] { --bg:#0F0F11; --panel:#17171A; --fg:#EEECE8; --muted:#A09A93; --line:#2B2A2E; color-scheme:dark }
body { background:var(--bg); color:var(--fg); font:15px/1.55 var(--body); }
.wrap { max-width:1120px; margin:0 auto; padding-inline:16px; padding-block:28px 64px; display:flex; flex-direction:column; gap:28px; }
h1 { font:700 clamp(1.8rem,5vw,2.6rem)/1.05 var(--display); margin:0; text-transform:uppercase; text-wrap:balance; }
h2 { font:700 .75rem var(--mono); letter-spacing:.1em; text-transform:uppercase; color:var(--muted); margin:0; }
.meta { color:var(--muted); font:13px var(--mono); font-variant-numeric:tabular-nums; }
.top { display:grid; grid-template-columns:minmax(0,300px) minmax(0,1fr); gap:28px; align-items:start; }
@media (max-width:760px) { .top { grid-template-columns:minmax(0,1fr); } }
video { width:100%%; max-width:300px; aspect-ratio:9/16; background:#000; border-radius:8px; display:block; }
.noprev { aspect-ratio:9/16; max-width:300px; border:1px dashed var(--line); border-radius:8px; display:grid; place-items:center; color:var(--muted); font:13px var(--mono); text-align:center; padding:16px; }
.col { display:flex; flex-direction:column; gap:14px; min-width:0; }
.cap { background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 16px; white-space:pre-wrap; font-size:.95rem; max-width:62ch; }
button { background:var(--accent); color:var(--accent-ink); border:0; border-radius:6px; padding:8px 14px; font:700 12px var(--mono); letter-spacing:.04em; cursor:pointer; align-self:flex-start; }
button:focus-visible { outline:2px solid var(--fg); outline-offset:2px; }
.warn { border-left:3px solid var(--accent); padding:4px 12px; font-size:.92rem; }
.scroll { overflow-x:auto; border:1px solid var(--line); border-radius:8px; background:var(--panel); }
.tl { position:relative; min-width:%(minw)dpx; padding:10px 10px 12px; }
.row { position:relative; height:%(rowh)dpx; margin-bottom:6px; }
.bar { position:absolute; top:0; bottom:0; border-left:1px solid var(--line); font:10px var(--mono); color:var(--muted); padding-left:3px; }
.en { position:absolute; bottom:0; background:color-mix(in srgb, var(--accent) 55%%, transparent); border-radius:2px 2px 0 0; }
.sec { position:absolute; top:0; height:22px; border-radius:4px; background:color-mix(in srgb, var(--fg) 8%%, transparent); font:700 10px var(--mono); text-transform:uppercase; letter-spacing:.06em; padding:4px 6px; overflow:hidden; white-space:nowrap; }
.drop { position:absolute; top:-4px; bottom:-4px; width:2px; background:var(--accent); }
.cut { position:absolute; top:0; height:100%%; overflow:hidden; border-radius:3px; border:1px solid var(--bg); background:#222; }
.cut img { width:100%%; height:100%%; object-fit:cover; display:block; }
.cut span { position:absolute; left:0; right:0; bottom:0; font:9px var(--mono); color:#fff; background:rgba(0,0,0,.55); padding:1px 3px; white-space:nowrap; overflow:hidden; }
.txt { position:absolute; top:0; height:100%%; border-radius:4px; background:color-mix(in srgb, var(--accent) 22%%, var(--panel)); font:11px/1.25 var(--body); padding:4px 6px; overflow:hidden; border:1px solid var(--line); }
.card { background:color-mix(in srgb, var(--fg) 14%%, var(--panel)); font-family:var(--mono); text-transform:uppercase; }
table { border-collapse:collapse; width:100%%; font-size:.92rem; }
td, th { text-align:left; padding:7px 10px; border-bottom:1px solid var(--line); vertical-align:top; }
th { font:700 11px var(--mono); color:var(--muted); text-transform:uppercase; letter-spacing:.06em; }
td.n { font:12px var(--mono); color:var(--muted); white-space:nowrap; font-variant-numeric:tabular-nums; }
"""


def bb(b):  # 0-based beat -> "bar:beat"
    return f"{int(b // 4) + 1}:{b % 4 + 1:g}"


def uri(path: pathlib.Path, mime: str) -> str:
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def build(ws, reel_dir: pathlib.Path, title=None) -> pathlib.Path:
    p = get_plan(ws, reel_dir)
    brand = json.loads((ws.kit / "brand.json").read_text())
    edit = json.loads((reel_dir / "edit.json").read_text())
    beats = json.loads((reel_dir / "beats.json").read_text())
    nbar = p["bars"]
    px = max(56, min(90, 1040 // max(nbar, 1)))  # pixels per bar
    W = nbar * px
    xb = lambda b: b / 4 * px  # beat -> x

    rows = []
    # bar ticks + energy
    en = beats.get("energy") or []
    ticks = "".join(f'<div class="bar" style="left:{i * px}px;width:{px}px">{i + 1}</div>' for i in range(nbar))
    bars_e = "".join(f'<div class="en" style="left:{i * px + 4}px;width:{px - 8}px;height:{max(2, int(e * 46))}px"></div>' for i, e in enumerate(en[:nbar]))
    drop = beats.get("drop_bar") or next((s.get("bars", [0])[0] for s in edit.get("sections", []) if s.get("hit")), None)
    dm = f'<div class="drop" style="left:{(drop - 1) * px}px" title="drop"></div>' if drop else ""
    rows.append(f'<div class="row" style="height:52px">{ticks}{bars_e}{dm}</div>')
    rows.append('<div class="row" style="height:24px">' + "".join(
        f'<div class="sec" style="left:{xb(s["b0"]) + 1}px;width:{xb(s["b1"]) - xb(s["b0"]) - 2}px">{html.escape(s["name"] or "")}</div>' for s in p["sections"]) + "</div>")
    cut_html = []
    for c in p["cuts"]:
        b1 = next((d["b"] for d in p["cuts"] if d["b"] > c["b"]), nbar * 4)
        th = ws.thumbs / f"{c['id']}.jpg"
        img = f'<img alt="" src="{uri(th, "image/jpeg")}">' if th.exists() else ""
        cut_html.append(f'<div class="cut" style="left:{xb(c["b"])}px;width:{max(3, xb(b1) - xb(c["b"]))}px" title="{html.escape(c["id"])} · {bb(c["b"])}">{img}<span>{html.escape(c["id"])}</span></div>')
    rows.append(f'<div class="row" style="height:96px">{"".join(cut_html)}</div>')
    rows.append('<div class="row" style="height:44px">' + "".join(
        f'<div class="txt" style="left:{xb(l["b0"])}px;width:{max(20, xb(l["b1"]) - xb(l["b0"]) - 2)}px" title="{html.escape(l["text"])}">{html.escape(l["text"])}</div>' for l in p["lines"]) + "</div>")
    rows.append('<div class="row" style="height:28px">' + "".join(
        f'<div class="txt card" style="left:{xb(c["b0"])}px;width:{max(20, xb(c["b1"]) - xb(c["b0"]) - 2)}px">{html.escape(c["card"])} card</div>' for c in p["cards"]) + "</div>")

    prev = reel_dir / "preview.mp4"
    if prev.exists() and prev.stat().st_size < 12e6:
        video = f'<video controls playsinline preload="metadata" src="{uri(prev, "video/mp4")}"></video>'
    else:
        video = '<div class="noprev">No preview yet.<br>Run <code>reelmaker preview</code>, then rebuild this page.</div>'
    capf = reel_dir / "caption.txt"
    caption = capf.read_text().strip() if capf.exists() else ""
    cap_html = (f'<div class="cap" id="cap">{html.escape(caption)}</div><button type="button" id="copy">Copy caption</button>' if caption
                else '<p class="meta">No caption.txt yet.</p>')
    warn = "".join(f'<p class="warn">{html.escape(w)}</p>' for w in p["warnings"] + p.get("errors", []))
    lines_tbl = "".join(f'<tr><td class="n">{bb(l["b0"])}</td><td class="n">{l["t0"]:.2f}s</td><td class="n">{html.escape(l["style"])}</td><td>{html.escape(l["text"])}</td></tr>' for l in p["lines"])
    name = title or edit.get("title") or reel_dir.name
    dur = p["duration"]
    css = CSS % {"accent": brand["colors"]["accent"], "minw": W + 20, "rowh": 40}
    page = f"""<title>{html.escape(name)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600&family=Space+Grotesk:wght@700&family=Space+Mono:wght@400;700&display=swap">
<style>{css}</style>
<div class="wrap">
  <div class="col">
    <h2>{html.escape(brand.get("name", ""))} · reel</h2>
    <h1>{html.escape(name)}</h1>
    <p class="meta">{dur:.1f} s · {nbar} bars at {p["bpm"]:.0f} BPM · {len(p["cuts"])} cuts · {len(p["lines"])} lines{f" · drop at bar {drop}" if drop else ""}</p>
    {warn}
  </div>
  <div class="top">
    <div>{video}</div>
    <div class="col"><h2>Post text</h2>{cap_html}</div>
  </div>
  <div class="col">
    <h2>Timeline</h2>
    <p class="meta">Bars across; the track's energy per bar, the sections, a thumbnail per cut, the on-screen lines and the cards.</p>
    <div class="scroll"><div class="tl">{"".join(rows)}</div></div>
  </div>
  <div class="col">
    <h2>On-screen text</h2>
    <div class="scroll"><table><thead><tr><th>Bar</th><th>Time</th><th>Style</th><th>Text</th></tr></thead><tbody>{lines_tbl}</tbody></table></div>
  </div>
</div>
<script>
const b = document.getElementById('copy');
if (b) b.onclick = () => {{
  const t = document.getElementById('cap').textContent;
  const sel = () => {{ const r = document.createRange(); r.selectNodeContents(document.getElementById('cap')); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected: press Cmd+C'; }};
  try {{ navigator.clipboard.writeText(t).then(() => b.textContent = 'Copied', sel); }} catch (e) {{ sel(); }}
}};
</script>
"""
    out = reel_dir / "board.html"
    out.write_text(page)
    print(f"{out} ({out.stat().st_size / 1e6:.1f} MB)")
    return out
