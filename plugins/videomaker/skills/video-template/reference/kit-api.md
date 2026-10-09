# Kit API 1

A kit is data (`brand.json`) plus drawing code (`cards.js`) on a fixed runtime (`runtime/fx.js`, `runtime/reel.js`).
The same three files run in the storyboard and in the videomaker renderer, frame by frame on a 1080×1920 canvas, so
anything that works in the storyboard renders identically.

## brand.json

| Field | Type | Used by |
| --- | --- | --- |
| `kit_api` | `1` | The runtime's compatibility check. |
| `name`, `short` | text | The wordmark fallback (`short`, in caps) when there's no logo. |
| `colors` | `bg`, `ink`, `ink2`, `accent`, `hot`, `cream` as hex | `bg` = the darkest tone (scrims, pills' ink); `ink` = main text; `ink2` = secondary text; `accent` = the one accent; `cream` = flash colour. |
| `fonts` | `display`, `body`, `mono`: `{family, file, weights}` | `file` is relative to the kit. `weights` is a CSS weight or range ("300 700"). |
| `logo`, `logo_style` | file name or `null`; `"plain"` or `"neon"` | Start and out cards. |
| `url`, `instagram` | text | Out card (URL), captions. |
| `address` | `{line, city}` | Out card lower-third. |
| `hours` | list of `{days, time}` (up to 4 rows show) | Out card; skipped while empty. |
| `offer` | `{headline, pill}` | Out card. |
| `classes`, `voice` | lists of text | What videomaker may put on screen. |
| `hook` | `{mode: "template"\|"jit", style, text, strike}` | How reels open (see the videomaker edit format). |
| `start_card` | `"bug"`, `"full"` or `"none"` | The start card. |
| `safe` | `{l, r, top, bot}` in canvas pixels | The text box clear of the Reels UI. Keep the default unless a platform needs a tighter one. |
| `grade` | `{wash, contrast, saturate, brightness, vignette, grain}` | The footage look: `wash` is a soft-light accent tint (0–0.35). |

## cards.js

A classic script (no `import`/`export`) that sets `globalThis.KIT`. `fx.js` loads first, so it can use `FX`.

```js
globalThis.KIT = {
  api: 1,
  setup({ brand, logo }) { … },        // once, before the first frame; set this.filter here
  filter: 'contrast(1.08) …',          // CSS filter for drawing footage
  grade(L, k) { … },                   // tint the shot layer (after the footage is drawn)
  post(ctx, k) { … },                  // over the footage, under the type (vignette)
  finish(ctx, k) { … },                // over everything, after the camera (grain)
  text: { hook, slam, stack, quiet, label, shout, caption },   // (ctx, line, k)
  cards: { start: {beats, draw}, outro: {beats, draw}, lower: {beats, draw} },  // draw(ctx, k, props)
  catalog: [['hook', 'what it is'], …],   // the storyboard's list, in order
};
```

**A text style** is `function (ctx, line, k)`, called on every frame while the line is on screen. It draws its own
entrance and exit (fade by `line.t1`). Set `fn.tail = seconds` to keep drawing after the line ends, as `shout` does
for its shatter.

- `line`: `text`, `lines` (split on `/`), `words`, `t0`/`t1` (seconds), `b0`/`b1` (beat indices), `beats` (the time of
  each word given `every`), plus any extra keys from the edit (`strike`, `accent`, `tag`, `every`, …).
- `k`: `t` (seconds), `i` (frame), `g` (the beat grid: `g.beat(n)`, `g.index(t)`, `g.pulse(t, decay)`, `g.spb`),
  `bi` (the current beat index), `SAFE`, `CW` (safe width), `C` (colours), `brand`, `logo`, `duration`.

**A card** is `{ beats, draw(ctx, k, props) }`. `beats` is its default length. `k` adds `s` (seconds into the card)
and `card` (`t0`, `t1`, `b0`, `b1`). `props` is `brand.json` merged with the edit's `props` for that card.

The runtime saves and restores the context around every style and card, composites the frame through the camera
(shake), and adds the edit's hits (flash, colour split, burst).

## fx.js helpers (FX)

`W`, `H`, `T` (theme tokens), `clamp`, `lerp`, `prog(t, a, b)`, `ease.{out3,in3,inOut3,out5,expo,back}`, `hash(a, b)`
(deterministic noise), `spring(dt, amp, freq, damp)`, `Grid`, `layer`, `buf(name)`, `clear(canvas)`,
`cover(ctx, src, {zoom,x,y})`, `font(ctx, size, {family, weight})`, `tracked(ctx, str, x, y, track)`,
`fit(ctx, str, width, opts, max)`, `letters(ctx, str, x, y, t, t0, opts)` (per-letter rise-in),
`slam(ctx, draw, t, t0, cx, cy)`, `shadowed`, `noShadow`, `pill(ctx, text, cx, cy, t, t0, opts)`,
`scrim(ctx, y0, y1, a)`, `vignette`, `flash`, `grain`, `duotone`, `leak`, `glitch`, `rgbSplit`, `burst`.

## Rules for kit code

- **Deterministic.** No `Math.random`, `Date` or `performance.now`: use `hash` and `k.t`, so a frame renders the same
  every time and the parallel renderer's chunks match.
- **Stateless per frame.** Draw everything from `k.t` and the line; don't keep animation state between calls.
- **Inside `SAFE`.** Use `SAFE.l` as the left edge and `CW` as the width; keep text between `SAFE.top` and `SAFE.bot`.
- **Facts from `props`/`brand`.** Never hard-code a business's words in `cards.js`.
- After any change, rebuild the storyboard and scrub through every component.
