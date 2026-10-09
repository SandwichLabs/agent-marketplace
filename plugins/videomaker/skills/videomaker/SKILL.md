---
name: videomaker
description: Make a finished, beat-matched promo reel (a 1080x1920 MP4 for Instagram Reels or TikTok) on the person's own computer from a folder of their clips and photos and a music track, in their brand's video kit. Sets up its own tools (uv, ffmpeg, a headless browser), tags the footage, cuts every shot to the song's measured beat with the drop on a fixed bar, renders, and writes the post caption. Use when someone asks for a reel, a sizzle or hype video, a promo, a launch, class or event teaser, or a beat-matched video from their footage. Needs a shell on their computer (Claude desktop's Code tab or Claude Code).
---

# videomaker

You make a business's promo reel from start to finish: their clips, their brand kit, a track, and a short brief go in;
a finished `reel.mp4` and the text to post come out. The owner is usually not technical. Run the steps yourself
without asking at each one. Stop only where the steps below say so, and keep messages to a line or two: what you did
and what's next.

Everything here is generic. The business's look, words and facts live in their kit (`kit/brand.json`, `kit/cards.js`),
made with the **video-template** skill. Never bring in another business's copy or assets.

**Read before you start:** `reference/setup.md` (first run on a machine), `reference/craft.md` (how a reel is built)
and `reference/edit-format.md` (the file you write). Read `reference/music.md` when choosing a track,
`reference/suno.md` if they want an original, and `reference/captions.md` before writing the post text.

## Where this runs

This skill needs a shell on the person's computer: the **Code tab** in Claude desktop (the default) or Claude Code. In
a chat-only session (a cloud sandbox that can't see their folders), say so in one line, offer to set up their video kit
with the video-template skill there, and stop.

Commands below are written as `reelmaker …`. Run them as `"<this skill's folder>/bin/reelmaker" …`, from the
workspace folder, where the skill's folder is the base directory reported when this skill loads (normally under
`~/.claude/plugins/cache/`).

## The run

### 1. Workspace and setup

- **Find the workspace**: the current folder if it has `clips/` or `.engine/`. Otherwise ask once where their clips
  are and suggest `~/Movies/Reels` for the workspace (see setup.md about iCloud). Create it with `reelmaker init` and
  move or copy their clips into `clips/` (copy if they'd rather keep the originals where they are).
- **Set up**: `reelmaker doctor --quick`. If it isn't set up yet, tell them in one line ("Setting up the video tools,
  about two minutes the first time, no password needed") and run `reelmaker doctor`. If it fails, follow the table in
  setup.md.
- **Kit**: if `kit/brand.json` still has `"_starter": true`, the business has no kit yet. Say so, and offer to run
  the video-template skill first (about 5 minutes). If they want the reel now, fill at least `name`, `url`, `offer`
  and `colors.accent` in `brand.json` from what they tell you or their website, and continue.

### 2. The brief

Take what you can from their message and fill the rest with defaults. Don't interview them.

| Ingredient | Default |
| --- | --- |
| Topic and purpose (a new service, product or class, the offer, an event) | From their message. Ask only if there's nothing to go on. |
| Length | 30 s (16 bars). 60 s (32 bars) if they ask. |
| Clips, images, text | Everything in `clips/`; you pick. Use any they name first. |
| Track | A file in `music/`, if there's exactly one, or the one they name. |
| Messaging | The topic plus the kit's `voice` lines and offer. |
| Hook | The kit's `hook.mode`: `"template"` uses the kit's line; `"jit"` means you write one (craft.md). |

Write the brief to `reels/<yyyy-mm-dd>-<topic>/brief.md` (a few lines), so a later change knows what was asked.

### 3. The track (the only required stop, when there's no track)

- **They have one** in `music/`: use it.
- **No track**: run `reelmaker catalog` first and suggest three royalty-free tracks from it that suit the topic,
  saying which need a credit line. In the same message, offer the other two options: their own track, or an original
  made in Suno (`reference/suno.md`: write the prompt and wait for the WAV). Wait for their choice; this is the one
  place you have to. For a catalog pick, `reelmaker fetch <id>` downloads it into `music/` with its licence note.
  Don't search or scrape music sites for tracks.
- Then cut it to the reel: `reelmaker music music/<track> <reel> --bars 16 --drop-bar 9` (`--bars 32 --drop-bar 17`
  for 60 s). Read the printed table. The drop it found should be where the energy jumps. If it isn't, or the owner
  says the drop is elsewhere, rerun with `--drop-at <seconds>`. If the song has a clean ending, try `--ending song`.

### 4. The footage

- `reelmaker ingest`. It makes proxies, splits clips at scene cuts and writes contact sheets to `.engine/sheets/`.
- **Read every contact sheet** and tag every untagged shot: `reelmaker tag <shot> <tags…> [--note "…"]`. Tag
  `exclude` on anything with burned-in text, blur, readable screens, or people who may not want to be in an ad (craft.md).
- `reelmaker shots` lists the library with your tags.

### 5. The edit

Write `reels/<name>/edit.json` following edit-format.md and the shape for the length in craft.md: sections that tile
every bar, shots picked by tag, text lines on the beat, the `start` card at bar 1 and the `outro` card on the last 3–4
bars. Words come only from the brief, the kit's `voice`, `classes` (what the business sells) and offer.

### 6. Check it, look at it, fix it once

- `reelmaker check <reel>` must pass. Fix every error and warning it lists.
- `reelmaker stills <reel>` writes `stills.jpg`, a frame at every cue with the Reels UI zones overlaid. **Read it.**
  Look for text over the pink zones, text over busy footage, a weak shot on the drop, repeated shots, and a dark or
  blurry frame. Fix what you see in one pass and run `check` again.

### 7. Preview, caption, board

- `reelmaker preview <reel>` renders a fast 540p draft (`preview.mp4`).
- Write `caption.txt` (captions.md).
- `reelmaker board <reel>` builds `board.html`: the preview, the caption with a copy button, the timeline with a
  thumbnail per cut, and every on-screen line. It embeds the media, so it can be several MB. Open it locally with
  `reelmaker open reels/<name>/board.html`. Publish it as an artifact only if they want to watch it on another device
  (it contains their footage and stays private to them).

### 8. Render

- `reelmaker render <reel>` renders the final `reel.mp4`: 1080×1920, 30 fps, H.264, the track at −14 LUFS. It takes
  1–3 minutes on most laptops. Then `reelmaker pace reels/<name>/reel.mp4` checks the cutting rate (craft.md).
- `reelmaker open reels/<name>/reel.mp4`, and tell them where the file is and that the caption is in `caption.txt`
  and on the board. Remind them of the music credit if the track needs one.

Render straight after the preview unless they asked to approve the draft first. They can always ask for changes.

## Changes

Edit `edit.json` (or `kit/brand.json` for brand facts), then `check`, `stills` for the part that changed, and
`preview` or `render`. Common asks:

- "Different song": `reelmaker music` with the new track into the same reel folder, then check that text still lands
  well (positions are bars, so the edit follows the new beat automatically).
- "Use the clip of X": tag it if needed and put it first in the section's `shots`.
- "Make it 60 seconds": a new reel folder with `--bars 32 --drop-bar 17` and the 60 s shape.
- "Change the colours, logo, hours": that's the kit. Edit `kit/brand.json` or use the video-template skill.

## Rules

- **The first frame is the hook.** No logo intro and no fade from black.
- **One flash, on the drop.** Never more than three flashes a second.
- **Only true words.** Use the kit's facts and voice and the owner's own words. Never invent numbers, results,
  testimonials or prices; if they want a stat, ask them for it.
- **Music rights.** Use only tracks they're licensed to post (music.md). Commercial songs from the radio stay out of
  the file: render with `--no-music` and have them add it in Instagram's own picker.
- **People.** Only use people (members, clients, staff) who are OK being in an ad. Exclude anyone you're unsure
  about and say so.
- **Their files stay theirs.** Don't upload footage anywhere except an artifact you publish for them to view.
