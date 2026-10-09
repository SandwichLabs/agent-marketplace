# Craft: how a reel is built

Every reel has one big moment, **the drop**, and everything builds to it. `reelmaker music` puts the song's drop on
the bar you choose (bar 9 of 16, or bar 17 of 32, by default). The structure below counts from there. If the track's
shape is different (a drop with no breakdown before it, or a long build), move the parts to fit the song; the drop
bar stays fixed.

## The shapes

**30 seconds = 16 bars** (`--bars 16 --drop-bar 9`)

| Part | Bars | Cutting | On screen |
| --- | --- | --- | --- |
| Hook | 1–2 | `hold`, 2 strong shots, half speed, `push` 0.08 | The hook line from frame 0, plus the `start` card |
| Build | 3–4 | every beat, `punch` 0.03 | `slam` lines, one word per 1–2 beats |
| Breakdown | 5–6 | `hold`, calm shots, `speed` 0.4 | `quiet` (when the music drops back) |
| Lift | 7–8 | `[2, 1]` or `[1, 0.5]`, accelerating | A `label` or two, then the `shout` over bar 8, ending exactly on the drop |
| **Drop** | 9–12 | every beat, `punch` 0.04, `hit: true` | `stack` from beat 2 of the drop, then a `caption` or `label`s |
| Offer | 13–16 | `hold`, the best wide or group shots | The `outro` card |

**60 seconds = 32 bars** (`--bars 32 --drop-bar 17`)

| Part | Bars | Cutting | On screen |
| --- | --- | --- | --- |
| Hook | 1–4 | `hold`, then every 2 beats | Hook line, the `start` card, then a `stack` answer |
| Build 1 | 5–8 | every beat | `slam` lines |
| Proof 1 | 9–12 | every 2 beats | `label`s (classes, services, products), 2 beats each |
| Breakdown | 13–14 | `hold`, slow | `quiet` |
| Lift | 15–16 | `[2, 1, 0.5]` | `shout` over bar 16 |
| **Drop** | 17–24 | every beat, the fastest cutting, `hit: true` | `stack`, then `label`s |
| Proof 2 | 25–28 | every 2 beats, maybe `duotone` | A `stack` of what customers get, or a `caption` |
| Offer | 29–32 | `hold` | The `outro` card |

The breakdown only works if the music actually drops back there. Check the energy column `reelmaker music` prints:
if bars 5–8 of the reel aren't quieter, skip `quiet`, keep cutting, and put a `stack` there instead. If the first
bars of the music window are flat too (no build to speak of), skip the breakdown and cut slower (every 2 beats) until
the lift.

## The hook

The first frame is the hook. There's no logo intro, no fade-in and no black frame: the reel opens on footage with
the line already on screen, because that's all most people see before they scroll. The `start` card only adds a small
logo over it.

- **Kit hook (`brand.json` `hook.mode` is `"template"`).** Use it as is: `{"hook": true}` as the first text line.
  Don't rewrite it.
- **Fresh hook (`hook.mode` is `"jit"`).** Write one for this reel's topic, 2–4 words per line, 2–4 lines, readable
  with the sound off. What works:
  - **Contrarian**, struck through, then answered: `BIG GYMS / CROWDED / CLASSES.` with `strike: 2`, then a
    `stack`: `SMALL GROUPS. / REAL COACHING.` (or `SPREADSHEETS / EVERYWHERE.`, then `ONE / DASHBOARD.`). Only
    when it's the business's own position.
  - **The promise**: `STRONGER / EVERY / WEEK.` or `MESSY DATA. / CLEAR / ANSWERS.`
  - **The news**: `NEW CLASS / SATURDAYS / 9AM.` or `NOW BAKING / ON SUNDAYS.`
  - **Direct to the viewer**: `YOUR FIRST / CLASS IS / FREE.` or `YOUR FIRST / CALL IS / ON US.`

  Build it from the brief and the kit's `voice` lines. Never invent a claim, a number or a result.

## Picking shots

- Read the contact sheets (`.engine/sheets/`) and tag every shot before writing the edit. Useful tags: what it is
  (`squat`, `group` and `coach` at a gym; `screen_closeup`, `whiteboard`, `team_wide` at a consultancy; `storefront`,
  `product`, `counter` at a shop or bakery), its energy (`power`, `calm`), and anything special (`wall` or `sign` for the
  business's own signage, `wide`).
- Tag `exclude` on shots with burned-in text or titles, blurry or dark frames, screens or mirrors with readable
  text (a screen close-up is fine when nothing on it is readable or private), and anyone who looks uncomfortable. Ask the owner if you're unsure whether someone has agreed to be in ads.
- **Hook**: the two most striking shots, ideally a person mid-action, close (a lift, hands at work, a pen on a
  whiteboard).
- **Build and drop**: variety. Don't repeat a shot within 8 cuts, alternate close and wide, and alternate people.
- **Breakdown**: calm shots (a slow rep, a conversation, a product turning in the light).
- **Drop downbeat**: the single most powerful shot.
- **Offer**: the room. Group or team shots, the business's own signage or storefront, smiles. Start it on a wide or
  empty shot so the out card's logo doesn't land on a face.
- Photos work as shots too. They get the same slow push.

## Words

- **Five words or fewer per line**, and each line stays at least one beat (two beats for `label` names).
- One text layer at a time.
- Only what the business says about itself: its `voice` lines in `brand.json`, its `classes` (what it sells) and
  offer, and the owner's own words in the brief. No invented stats, results, testimonials or prices.
- If the track has vocals, don't put different words on screen while someone sings. Instrumentals are easier.

## Safety and polish

- **No strobing.** At most one flash hit per reel, on the drop, and never more than three flashes a second
  (photosensitivity).
- Text stays inside the kit's safe box (the Reels UI covers the top, the bottom and the lower right). `stills` draws
  those zones; check them.
- The first cut lands within 2 s. Aim for about 8–14 picture changes per 10 s (`reelmaker pace`), slower in the
  breakdown and offer.
