---
name: video-template
description: Design a business's reusable video kit for beat-matched promo reels, and show it as a motion storyboard artifact. The kit holds their colours, fonts and logo, the opening hook, a start card with a logo fade-in, an out card that animates their hours, location, offer and website, and the text styles and transitions. Use when someone wants to set up or change their reel template, video branding, intro or outro cards, or the standard hook, or before making their first reel with the videomaker skill. Works in a chat with code execution or on their computer.
---

# video-template

You set up a business's **video kit**: the fixed look every reel shares. You build it from their own assets, show it
moving in a storyboard, adjust it until they're happy, and save it where the videomaker skill can use it. The owner is
usually not technical: show, don't explain, and keep messages short.

A kit is a folder:

```
kit/
  brand.json        the facts and choices: colours, fonts, logo, URL, address, hours, offer, voice lines, the hook
  cards.js          how things are drawn: text styles, the start, out and lower-third cards, the grade
  fonts/            the font files (woff2)
  logo.svg|png      their logo, copied from their assets
  storyboard.html   the motion storyboard (built from the above; never edit it by hand)
```

Start from the neutral starter kit in this skill's `kit/` folder. `runtime/` holds the code that draws it (the same code
videomaker renders with), and `scripts/storyboard.py` builds the storyboard. Read `reference/kit-api.md` before changing
`cards.js`, and `reference/design.md` before choosing colours and type.

## Where the kit lives

- **On their computer (the Code tab or Claude Code):** in their reel workspace, `<workspace>/kit/`. A good default for
  the workspace is `~/Movies/Reels` (videomaker uses the same folder). Copy this skill's `kit/` there if it doesn't
  exist yet.
- **In a chat with code execution:** work in the sandbox, then give them `kit.zip` to download at the end. Tell them
  to unzip it into their reel workspace as `kit/`, or keep it for when they set up videomaker.

Never commit or publish a client's logo or footage anywhere public.

## The flow

### 1. Gather (one message, then work)

Ask for whatever you can't find yourself:

- **What kind of business it is, and what the reels are for**: read it from their site or assets ("a two-person
  software consultancy that wants inbound leads", "a bakery announcing a second shop"). Ask only if it isn't clear.
  Everything below follows from it: the starter kit's sample copy is for a gym, so don't carry its words over to
  another kind of business.
- **Their assets**: the logo (SVG, or a PNG with a transparent background, is best), and any brand guide.
- **Their website**: read it for the name, the colours (the site's theme colour and buttons), the address, the offer
  and the lines they already use about themselves (the `voice` list).
- **Hours**: ask, or read them from their booking system if another skill can (for example a Mindbody skill). Never
  guess hours.
- **The offer and the call to action**: the headline ("TRY A FREE WEEK."), a short pill ("UNLIMITED CLASSES"), the URL.

### 2. Fill in `brand.json`

Replace every starter value (the `_notes` block explains each field) and delete `"_starter": true`. Then settle two
choices with the owner, each in a sentence:

- **The hook** (`hook`): `"template"` fixes one opening line for every reel ("STRONGER / EVERY / WEEK."), which is
  consistent and on brand. `"jit"` lets each reel open with a fresh line written for its topic, which grabs attention
  better for news and events. Recommend `"jit"` unless they want one signature line. In template mode, write the line
  (`text` with `/` between stacked lines; `strike` only for a contrarian opener).
- **The start card** (`start_card`): `"bug"` (recommended) fades the logo in small over the opening footage, so the
  hook line still owns the first frame. `"full"` puts a logo card on black for the first bar, which costs the first two
  seconds of attention. `"none"` drops it.

Also set `logo_style`: `"neon"` if the logo is a neon sign or glow, otherwise `"plain"`, and `business` (the type and
the goal from step 1). `classes` holds what they sell (services, products, menu items), not only classes.

### 3. Write the sample reel for this business

The storyboard plays a 16-bar sample reel. Copy this skill's `scripts/sample-edit.json` to `kit/sample-edit.json` and
rewrite its words for this business, keeping the bars, styles and cards as they are:

- Every `text` line, the lower-third `props` and the shot ids (the stand-in footage shows them as labels, so name
  shots this business would film: `standup`, `whiteboard`, `screen_closeup` for a dev shop, not `squat`).
- Sample copy is placeholder copy: short, the right length for its style, and plainly about this kind of business and
  its goal ("SHIP/EVERY/WEEK.", "CODE REVIEWED."), but it makes no claims of fact. Real reels write their own words.
- Keep `"title"` saying it's sample copy.

`storyboard.py` uses `kit/sample-edit.json` when it's there.

### 4. Adjust the look (only if needed)

The starter `cards.js` suits most gyms and studios: bold stacked caps, one accent colour, soft dark scrims for
legibility. Change it only for what the owner asks or their brand needs (a calmer type style for a law firm or a
clinic, say) (a different headline font, rounded pills, a
lower-third shape). Keep to the kit API, keep every style inside the safe box, and test with the storyboard.

Fonts must be files in `kit/fonts/` (woff2), free to use commercially (Google Fonts' open-licence fonts are). To swap
one, download its woff2, put it in `fonts/` and update `brand.json` `fonts`.

### 5. Build and show the storyboard

```bash
python3 <this skill>/scripts/storyboard.py <kit folder>
```

It writes `<kit>/storyboard.html`, a single self-contained page that plays every component on a 16-bar sample reel at
124 BPM, with play and scrub, a click track, safe-zone overlay, a tempo switch and **Use my clip** (they can preview the
cards over one of their own videos). It lists each component with how a reel asks for it, and flags missing hours or
logo.

If you can publish HTML artifacts, publish `storyboard.html` and share the link. Otherwise open it in their browser
(`open` on a Mac). Ask them to press play, and to try **Use my clip**.

### 6. Iterate

Take feedback ("bigger hours", "logo in white", "no strike-through"), change `brand.json` or `cards.js`, rebuild, and
republish to the same artifact. Two or three rounds is normal. Look at the storyboard yourself when you can (a
screenshot of a few moments) before saying a change is done.

### 7. Save

On their computer, the kit is already in place. Tell them videomaker will use it for every reel. In chat, zip the kit
folder (without `storyboard.html` if size matters) and share `kit.zip`.

## Rules

- Only true facts: hours, prices, addresses and claims come from the owner or their own materials.
- One accent colour, with strong contrast against dark footage (design.md has the check).
- Text and cards stay inside the safe box in `brand.json` (clear of the Instagram UI).
- No strobing effects in the kit: one flash on the drop is the most a reel uses.
- Keep the kit generic in code and specific in data: business facts go in `brand.json`, never hard-coded in `cards.js`.
