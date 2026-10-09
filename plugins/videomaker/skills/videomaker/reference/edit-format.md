# edit.json: the reel, as data

A reel is `reels/<name>/edit.json` plus `beats.json` (written by `reelmaker music`). You write only `edit.json`. The
renderer reads it, the measured beat grid times everything, and the kit draws the type and cards. Never type seconds:
every position is a musical count.

## Positions and lengths

- **Positions are 1-based musician counts, written as strings.** `"9"` is the downbeat of bar 9. `"9:3"` is bar 9,
  beat 3. `"9:3.5"` is the "and" after beat 3. `"end"` is the end of the track.
- **Lengths (`len`) are in beats.** One bar is 4 beats.
- **Sections take `bars: [first, last]`, inclusive.** `[9, 12]` covers bars 9, 10, 11 and 12.

At 124 BPM, a beat is 0.484 s and a bar is 1.935 s. A 16-bar reel runs about 31 s, and 32 bars about 62 s.

## Top level

```json
{
  "title": "Free week: spring",
  "fps": 30,
  "sections": [ … ],
  "text": [ … ],
  "cards": [ … ]
}
```

## sections: the footage

Sections must tile the reel from bar 1 to the last bar with no gaps. Each one lays cuts across its bars.

| Key | Meaning |
| --- | --- |
| `name` | A label (`hook`, `build`, `breakdown`, `lift`, `drop`, `proof`, `offer`). Shows on the board. |
| `bars` | `[first, last]`, inclusive. |
| `shots` | Shot ids from the library (`reelmaker shots`), or a shot's `name`. They're used in order and cycled when the section needs more cuts than shots. A shot can also be an object: `{"id": "ddh-04", "in": 0.5, "speed": 0.5}`. |
| `cut` | How often to cut. A number is beats per cut: `1` cuts on every beat, `2` every other beat, `0.5` on every half beat. `"hold"` gives each listed shot an equal share of the section. An array accelerates: `[2, 1, 0.5]` splits the section into three equal parts that cut every 2 beats, then every beat, then every half beat. |
| `speed` | Playback speed (`0.5` is half-speed slow motion). Shots shorter than their cut are slowed down to fit, never frozen. |
| `push` | A slow zoom-in across each cut (`0.03` by default, `0.08` to `0.1` for slow, deliberate shots). |
| `punch` | A zoom pulse on every beat (`0.02` to `0.04` in fast sections, otherwise leave it out). |
| `zoom` | The base zoom (`1.04` by default). |
| `duotone` | `true`, or `0`–`1`: a freeze-frame look in the kit's dark and accent colours. Use it for a proof or quiet moment. |
| `hit` | One-shot effects on the section's first downbeat: `true` (flash, shake and colour split together), or an object of `flash`, `shake`, `rgb`, `burst` and `glitch`. **Use it once, on the drop.** At most two flashes in a reel. |

The in-point within a shot is picked deterministically, so the same edit always renders the same frames. Set `in`
(seconds into the shot) only when a particular moment matters, such as the lockout of a lift or a chart appearing.

## text: what's on screen

```json
{ "at": "3", "len": 4, "style": "slam", "text": "MOVE WELL.", "every": 2 }
```

| Key | Meaning |
| --- | --- |
| `at` | Where it starts (position string). |
| `len` | How long it stays, in beats (default 4). |
| `style` | A kit text style; see the table below. |
| `text` | The words. `/` breaks a line in stacked styles: `"STRONGER/EVERY/WEEK."` |
| `every` | Beats between words (`slam`, `shout`) or lines (`stack`, `quiet`). |
| `strike` | `hook` only: the beat (counted from the line's start) where an accent strike-through begins, running across each line half a beat apart. For contrarian openers ("BIG GYMS / CROWDED / CLASSES." struck out, then the answer). |
| `accent` | `true` colours a `label` in the accent. For `hook`, `"last"` or a line index colours that line. |
| `tag` | `label` only: the small mono word above the name (`"CLASS"`, `"SERVICE"`, `"NEW"`; none by default). |
| `hook` | `true`: use the kit's fixed opening line from `brand.json` (`hook.text`, `hook.style`, `hook.strike`). Any other key you set overrides it, for example `{"hook": true, "len": 8}`. |

Text styles in the starter kit (a business's kit may add or restyle them; `kit/storyboard.html` shows them all):

| Style | Use for | Words |
| --- | --- | --- |
| `hook` | The opening statement, on screen from frame 0 when it starts at bar 1 | 2–4 short lines |
| `slam` | One word per beat, each slams in; the last word in the accent | 2–3 words, `every` 1–2 |
| `stack` | Two or three short lines rising a beat apart | under 5 words |
| `quiet` | The breakdown: thin, slow, one line per bar | 2 short lines, `every` 4 |
| `label` | What they sell (classes, services, products, menu items): a big name, optional tag | 1–3 words, 2 beats each |
| `shout` | The lift into the drop. Words fall in on the beat and shatter when the line ends, so end it exactly on the drop downbeat | 2–4 words over one bar |
| `caption` | One supporting sentence, low in the frame | up to about 8 words |

Keep one text layer on screen at a time: start the next line where the last one ends.

## cards: the kit's set pieces

```json
{ "card": "outro", "at": "13", "len": 16 }
```

| Card | What it does | Default length |
| --- | --- | --- |
| `start` | The logo fades in small over the hook footage and leaves by the end of its bar (or a full logo card, if the kit's `start_card` is `"full"`; nothing if `"none"`). Put it at `"1"`. | 4 beats |
| `outro` | Darkens the footage. The logo strikes, then the offer, the pill, the URL, the hours (one row per beat) and the address come in. Put it on the last 3–4 bars. | 12 beats |
| `lower` | A lower-third. `props: {"title": "Tempo Strength", "tag": "New class"}` or `{"title": "Data audits", "tag": "New service"}` | 8 beats |

`props` overrides any `brand.json` value for that card, for example
`{"card": "outro", "at": "13", "len": 16, "props": {"offer": {"headline": "SPRING SALE.", "pill": "20% OFF"}}}`.

## A complete 16-bar example

For a gym; the shot ids are whatever you tagged (a consultancy's might be `whiteboard-02` or `screen_closeup-05`).

```json
{
  "title": "Free week",
  "sections": [
    {"name": "hook", "bars": [1, 2], "cut": "hold", "shots": ["squat-01", "rdl-03"], "speed": 0.5, "push": 0.08},
    {"name": "build", "bars": [3, 4], "cut": 1, "shots": ["dl-07", "stepup-13", "rower-06", "trx-10"], "punch": 0.03},
    {"name": "breakdown", "bars": [5, 6], "cut": "hold", "shots": ["stretch-03", "plank-14"], "speed": 0.4, "push": 0.1},
    {"name": "lift", "bars": [7, 8], "cut": [2, 1], "shots": ["lunge-05", "older-08", "box-12", "squat-09"], "punch": 0.02},
    {"name": "drop", "bars": [9, 12], "cut": 1, "shots": ["swing-04", "group-17", "dl-07", "medball-04", "rower-06", "kb-11"], "punch": 0.04, "hit": true},
    {"name": "offer", "bars": [13, 16], "cut": "hold", "shots": ["group-17", "swing-04"], "speed": 0.5, "push": 0.08}
  ],
  "text": [
    {"at": "1", "len": 6, "style": "hook", "text": "STRONGER/EVERY/WEEK."},
    {"at": "3", "len": 4, "style": "slam", "text": "MOVE WELL.", "every": 2},
    {"at": "4", "len": 4, "style": "slam", "text": "LIFT STRONG.", "every": 2},
    {"at": "5", "len": 8, "style": "quiet", "text": "NO EGO./NO PRESSURE.", "every": 4},
    {"at": "7", "len": 4, "style": "label", "text": "STRENGTH", "tag": "CLASS"},
    {"at": "8", "len": 4, "style": "shout", "text": "ONE MORE REP!"},
    {"at": "9:2", "len": 7, "style": "stack", "text": "REAL/STRENGTH."},
    {"at": "11", "len": 8, "style": "caption", "text": "Small classes. Real coaching, every session."}
  ],
  "cards": [
    {"card": "start", "at": "1", "len": 4},
    {"card": "outro", "at": "13", "len": 16}
  ]
}
```

`reelmaker check <reel>` reports unknown shots, unknown styles, lines that are too long or too short, and any page
error. Run it after every change.
