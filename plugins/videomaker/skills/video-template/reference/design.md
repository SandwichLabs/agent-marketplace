# Designing a kit

The kit plays over real gym footage on a phone, for under a second per line. Legibility and one strong idea beat
detail.

## Colour

- **One accent.** Take it from the logo or the website's buttons. It marks the landing word of a line, strike-throughs,
  the offer pill and the drop. Everything else is `ink` (near-white) on dark footage.
- **Check the accent against dark footage.** It needs a contrast ratio of at least 4.5:1 against `bg`. Mid-saturation
  oranges, yellows, limes, cyans and pinks usually pass. Deep blues, purples and reds usually fail: lighten them, or use
  them for the pill background with `bg` text on top.
- `bg` is the brand's darkest neutral. Pure black is fine; a slightly warm or cool black that matches the brand is
  better.
- `grade.wash` tints the footage toward the accent (0.15–0.3). Lower it for brands whose accent is cold or very
  saturated, and set it to 0 if the footage already looks on brand.

## Type

- **Display**: a bold grotesque or condensed face that holds up in all caps at 150–300 px. The starter's Space Grotesk
  works. Bebas Neue, Anton, Archivo (Black or Expanded), Barlow Condensed, Oswald and Unbounded are good open-licence
  alternatives, depending on the brand's character.
- **Body**: a plain sans for the caption style (DM Sans, Inter, Manrope).
- **Mono**: for tags, the URL and the hours (Space Mono, JetBrains Mono, IBM Plex Mono).
- If the brand guide names a font, use it only if its licence allows video use and you have the woff2 file.
- Download from Google Fonts or Fontsource as woff2. A variable font file covers every weight.

## The logo

- SVG first, then a PNG of at least 1000 px with a transparent background. A logo on a white box looks pasted on: ask
  for a transparent or light-on-dark version.
- `logo_style: "neon"` adds a flicker-on and a glow; use it only when the logo is a neon sign or glows on the site.

## Copy

- Collect 5–10 lines the business already uses (site headline, signage, taglines) into `voice`. Reels use these and
  the owner's own words, nothing invented.
- On-screen lines are five words or fewer. Rewrite long taglines into short stacked versions with the owner's okay
  ("Small classes and real coaching, so you get stronger every week." becomes "STRONGER / EVERY / WEEK." then
  "SMALL CLASSES. / REAL COACHING.").

## The hook

- **Template** (one fixed line): consistent and on brand. Pick their strongest short claim. It suits a business that
  posts often, where the line works like a signature.
- **JIT** (written per reel): better for events, launches and offers, where the news is the hook.
- Either way, the hook is on screen from frame 0 over footage. The start card is a small logo fade over it, not a
  title card.
