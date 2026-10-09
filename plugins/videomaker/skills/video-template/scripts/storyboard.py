#!/usr/bin/env python3
"""Build the kit storyboard: one self-contained HTML page (an artifact, or open it locally) that plays every
component of a video kit on a 16-bar sample reel. Inlines the runtime (fx.js, reel.js), the kit's cards.js,
brand.json, fonts and logo, so what plays is exactly what the renderer draws.

  python3 storyboard.py [KIT_DIR] [-o KIT_DIR/storyboard.html] [--edit KIT_DIR/sample-edit.json] [--title "Video Kit"]

Standard library only: runs in Claude's chat sandbox as well as on a laptop.
"""
import argparse, base64, json, mimetypes, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
SKILL = HERE.parent


def data_uri(path: pathlib.Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or ("font/woff2" if path.suffix == ".woff2" else "application/octet-stream")
    if path.suffix == ".woff2":
        mime = "font/woff2"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def js_literal(obj) -> str:
    # JSON is valid JS; escape "</" so no string can close the inline <script>
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


def contrast(a: str, b: str) -> float:
    """WCAG contrast ratio of two #rrggbb colours."""
    def lum(h):
        c = [int(h.lstrip("#")[k:k + 2], 16) / 255 for k in (0, 2, 4)]
        c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kit", nargs="?", default=str(SKILL / "kit"))
    ap.add_argument("-o", "--out")
    ap.add_argument("--edit", help="sample reel (default: KIT_DIR/sample-edit.json, else the starter's)")
    ap.add_argument("--title", default="Video Kit")
    a = ap.parse_args()

    kit = pathlib.Path(a.kit).resolve()
    rt = next(p for p in (SKILL / "runtime", HERE.parent / "runtime") if p.exists())
    brand = json.loads((kit / "brand.json").read_text())
    # the kit's own sample reel carries copy for this business; the starter's is a generic gym
    ep = pathlib.Path(a.edit) if a.edit else next(p for p in (kit / "sample-edit.json", HERE / "sample-edit.json") if p.exists())
    if not a.edit and ep.parent == HERE and not brand.get("_starter"):
        print("warning: no kit/sample-edit.json; the storyboard shows the starter's gym copy", file=sys.stderr)
    edit = json.loads(ep.read_text())

    c = brand["colors"]
    r = contrast(c["accent"], c["bg"])
    print(f"accent {c['accent']} on bg {c['bg']}: contrast {r:.2f}:1" +
          ("" if r >= 4.5 else " (below 4.5: lighten the accent, see design.md)"), file=sys.stderr)
    faces = []
    for role, f in brand["fonts"].items():
        p = kit / f["file"]
        if not p.exists():
            sys.exit(f"font for {role} not found: {p}")
        faces.append(f"@font-face{{font-family:'{f['family']}';src:url({data_uri(p)}) format('woff2');"
                     f"font-weight:{f.get('weights', '400')};font-display:block}}")
    logo = "null"
    if brand.get("logo"):
        lp = kit / brand["logo"]
        if lp.exists():
            logo = js_literal(data_uri(lp))
        else:
            print(f"warning: logo {lp} not found; the storyboard uses the wordmark", file=sys.stderr)

    scripts = {name: (src.read_text().replace("</script", "<\\/script")) for name, src in
               {"FX": rt / "fx.js", "REEL": rt / "reel.js", "CARDS": kit / "cards.js"}.items()}
    html = (HERE / "storyboard.template.html").read_text()
    subs = {
        "__TITLE__": a.title, "__BRAND__": brand.get("name", ""), "__ACCENT__": brand["colors"]["accent"],
        "__FONTFACES__": "\n".join(faces), "__FX__": scripts["FX"], "__REEL__": scripts["REEL"], "__CARDS__": scripts["CARDS"],
        "__BRAND_JSON__": js_literal(brand), "__EDIT_JSON__": js_literal(edit), "__LOGO_URI__": logo,
    }
    # replace placeholders in one pass so inlined code can't be re-substituted
    import re
    html = re.sub("|".join(map(re.escape, subs)), lambda m: subs[m.group(0)], html)
    out = pathlib.Path(a.out) if a.out else kit / "storyboard.html"
    out.write_text(html)
    print(f"{out} ({out.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
