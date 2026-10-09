# Handoff: test the videomaker plugin on a Mac

> Written 2026-10-09 at the end of the session that built the plugin (on Linux) and merged to main. You're the Claude instance on a Mac
> that proves it works for a non-technical owner in Claude desktop's **Code tab**. Read this, then `README.md`,
> `SETUP.md` and both `SKILL.md` files, before touching anything.

## What this is

Two skills in one plugin, replacing a CapCut walkthrough that a client (a small strength studio) found too manual and
inconsistent:

- **video-template** (`skills/video-template/`): builds a business's **video kit**. `kit/brand.json` holds the facts
  and choices (colours, fonts, logo, hours, address, offer, voice lines, the hook) and `kit/cards.js` holds the drawing
  code (text styles, start, out and lower-third cards, the grade). It publishes a **storyboard artifact** that plays
  every component on a 16-bar sample reel. It works in plain chat too.
- **videomaker** (`skills/videomaker/`): runs on its own on the owner's computer. It turns `clips/` and a track into a
  1080×1920 `reel.mp4` plus `caption.txt`. It bootstraps its own tools with no admin password: the launcher
  `bin/reelmaker` installs uv, and uv brings Python, librosa, Playwright and static-ffmpeg from `engine/uv.lock`. The
  pipeline: ingest (proxies, scene-cut shots, contact sheets Claude reads to tag the shots) → music (beat grid, drop
  detection, splice to 16 or 32 bars) → Claude writes `edit.json` → check and stills → preview → board → render.

The storyboard and the renderer run the same code (`skills/video-template/runtime/fx.js` and `reel.js`). videomaker
finds that runtime in its sibling skill. A standalone upload gets a vendored copy through `package.vendor` in
`marketplace.config.json`.

## Decisions Zac made (don't relitigate)

- **The Code tab is the default runtime.** Chat-only sandboxes can't see local clips.
- **Everything in this repo is generic.** No client logo, footage, names or copy, ever. A client's look is a kit built
  by video-template from their own files and kept in their workspace.
- **The hook is decided in the kit**: `brand.hook.mode` is `"template"` (a fixed line, used via `{"hook": true}`) or
  `"jit"` (written per reel).
- **pr-sizzle-reel** (the old CapCut planner) gets delisted once this is proven. Don't extend it.
- No Homebrew requirement. Homebrew needs an admin password and the Xcode tools; uv and the static builds don't. Use
  Homebrew only if it's already there.

## Getting the code

The plugin is on **main** of `SandwichLabs/agent-marketplace` (merged 2026-10-09 from `videomaker-skills`).

```bash
git clone git@github.com:SandwichLabs/agent-marketplace.git ~/projects/agent-marketplace   # or git pull if you have it
cd ~/projects/agent-marketplace
node scripts/build.mjs --check      # expect: 3 plugin(s) valid
```

Because it's on main, the owner's real install paths work too: the `SETUP.md` raw URL, and the one-step
`/plugin install videomaker --marketplace SandwichLabs/agent-marketplace`. Phase A tests them. Do fixes on a branch off
main (e.g. `videomaker-mac-fixes`).

## What was verified on Linux (your baseline)

Fedora, 32 cores, Playwright Chromium (no Chrome installed), Homebrew ffmpeg, warm uv cache.

| Step | Result |
| --- | --- |
| `doctor` on a fresh workspace and venv | 6 s (11 s with `REEL_FFMPEG=static`, including the static download) |
| Codec probe | Playwright's Chromium decoded H.264, so proxies were H.264 (VP9 is only the fallback) |
| `ingest` of two 1080p/720p Instagram reels | 3 s, 30 shots at scene cuts (threshold 0.18 plus a 0.3 s debounce) |
| `music` on a Suno take and on catalog tracks | Drop found where the energy jumps; tempos match the published BPMs (128.0, 122.0, 134.0, 130.0) |
| `check` / `stills` | 5 s each; stills composited real footage correctly, all text inside the safe box |
| `preview` / `render`, 30 s reel | 7 s / 15 s with 6 workers (about 90 fps). H.264 high, 30 fps, AAC 48 kHz, −13.7 LUFS |
| Beat sync | Cuts detected in the output were within one frame of a beat or half-beat for 31 of 32 (median 15 ms) |
| Same `edit.json` on a different song | Re-timed automatically, check passed |
| HDR | A synthetic HLG HEVC clip was detected and tone-mapped to BT.709 with both Homebrew and static ffmpeg |
| `claude plugin validate --strict` | Passes for the repo and the plugin |

**Never verified:** anything on macOS, Google Chrome as the render browser, the static ffmpeg on Apple Silicon, real
iPhone footage (HEVC, HDR, rotation, HEIC photos), laptop render speed, the Code tab's permission prompts, the plugin
install flow end to end, and an artifact publish of the storyboard from the Code tab.

## Before you start: what you need

- The Mac's details, recorded in the results: the chip, the macOS version, whether Google Chrome is installed, and
  whether Homebrew, uv or ffmpeg are already installed (`which brew uv ffmpeg`).
- **Test footage.** Ask Zac. Best: 8–15 real iPhone clips of a gym or workout, shot in the default settings (HEVC, HDR,
  portrait, some at 60 fps or 4K), plus 2–3 photos (one HEIC, one JPG), plus one clip with text burned in. If Zac
  provides client footage, keep it outside the repo and never commit or publish it.
- A business to build a test kit for. Use a made-up one, or one Zac names. Real client kits stay out of the repo.

## The test plan

Work through the phases in order. Time each command (`time …`) and note every permission prompt. Act as the
non-technical owner where a phase says so: give Claude the short prompt and don't help it.

Throughout, `R` is the launcher. For the install test, use the copy inside the installed plugin (under
`~/.claude/plugins/…/videomaker/skills/videomaker/bin/reelmaker`). For fixing bugs, run the checkout's copy
(`~/projects/agent-marketplace/plugins/videomaker/skills/videomaker/bin/reelmaker`), because edits to the checkout
don't change the installed plugin cache.

### Phase A: install the plugin (the owner's path)

1. In the Code tab, with a new empty folder open (e.g. `~/Movies/Reels`), paste the prompt at the top of `SETUP.md`
   (the raw GitHub URL) as the owner would, and let Claude drive. It should have the owner type
   `/plugin install videomaker --marketplace SandwichLabs/agent-marketplace`.
2. Check that both skills are listed and that a new session picks them up. If the one-step form fails, try
   `/plugin marketplace add SandwichLabs/agent-marketplace` then `/plugin install videomaker@sandwichlabs`, and record
   which worked.
3. **Record:** the exact commands that worked, any confusing prompts, and where the plugin cache landed.

### Phase B: bootstrap from bare

The goal is to measure what a fresh owner's Mac does. Make it as bare as you can without uninstalling Zac's tools:

```bash
mv ~/.local/bin/uv ~/.local/bin/uv.bak 2>/dev/null   # if uv lives there; restore afterwards
export REEL_VENV=$(mktemp -d)/venv                    # a brand-new Python environment
export REEL_FFMPEG=static                              # ignore any Homebrew ffmpeg and fetch the static build
```

Note that `REEL_VENV` and `REEL_FFMPEG` must be set for every later command in this phase. Better still, use a fresh
macOS user account with no developer tools at all: that's the real owner's machine.

1. `R init`, then `time R doctor`.
2. **Expect:** uv installs (about 10 s), the venv builds (30–90 s cold), static ffmpeg downloads, **Google Chrome** is
   chosen with "H.264 yes", the smoke render passes, and the run ends with "ready in N s".
3. `R doctor --quick` returns in about a second.
4. **Watch for:**
   - Gatekeeper or quarantine blocking the static ffmpeg binary.
   - The macOS privacy prompt for the Movies folder.
   - Playwright's `channel="chrome"` failing to launch Chrome.
   - numba or llvmlite wheels missing for this Python.
   - `UV_NO_MODIFY_PATH` leaving uv off the PATH for the next shell. The launcher adds `~/.local/bin` itself, so this
     should be fine.
5. **Record:** each step's time, total time, download sizes if visible, and every prompt the owner would see.

### Phase C: video-template as the owner

Prompt: *"Set up our video template. Here's our logo and our website is <url>."* (give it a logo file).

1. **Expect:**
   - It copies the starter kit into `kit/`, fills `brand.json` from the site, asks about hours, the hook mode and the
     start card, and copies the logo.
   - It builds `kit/storyboard.html` with `scripts/storyboard.py`, then publishes it as an artifact, or opens it if
     artifacts aren't available in the Code tab. Record which.
2. In the storyboard, press play, toggle safe zones, and try **Use my clip** with an iPhone `.mov` and a JPG. Does
   Chrome or the artifact viewer play HEVC from a blob URL? Record it.
3. Ask for two changes ("make the hours bigger", "use a different headline font") and check it rebuilds and republishes.
4. **Record:** the time to a kit the owner would accept, the questions it asked, and any visual bug, with a screenshot.

### Phase D: videomaker as the owner

Put the test clips in `clips/` and leave `music/` empty. Prompt: *"Make a 30-second reel for our free week from my
clips."*

1. **Expect, without help:**
   - `doctor --quick`, then the brief.
   - A single stop to choose a track. It offers catalog picks via `R catalog`, or Suno, or the owner's own track.
     Choose a Mixkit track.
   - `R fetch <id>`, `R music … --bars 16 --drop-bar 9`, then `R ingest`.
   - It **reads every contact sheet and tags every shot**, excluding the burned-in-text clip, then writes `edit.json`.
   - `R check`, then `R stills` (it must Read stills.jpg and fix what it sees), `R preview`, `caption.txt`,
     `R board`, `R render` and `R pace`, and opens `reel.mp4`.
2. Play `reel.mp4` in QuickTime and look closely at:
   - **HDR clips:** colours should look like the originals, not washed out or grey.
   - **Rotation:** portrait iPhone clips should be upright.
   - **60 fps or 4K clips:** smooth, and with good ingest time.
   - **HEIC photo:** converted by `sips` and shown.
   - **Sync:** cuts on the beat and the drop hit on bar 9.
   - **Text:** inside the safe zones, with no strobing.
   - **Audio:** level comparable to other reels.
3. **Record:**
   - Wall time for each command, especially `ingest` (clips per minute) and `render` (fps, worker count).
   - The number of permission prompts.
   - Every point where Claude stopped, asked something unnecessary, or went wrong.
   - The final file size and `R pace` output.
4. Don't post to Instagram unless Zac says so. If he does, record whether it uploads cleanly and plays at full
   quality, and whether any music claim appears.

### Phase E: changes

1. *"Same reel with a different song."* It should run `R music` on the same reel folder; text should still land.
2. *"Make a 60-second version."* A new reel with `--bars 32 --drop-bar 17` and the 60 s shape from `craft.md`.
3. *"Use the clip of <something> on the drop."* It should tag it if needed and reorder `shots`.
4. *"Render it without music, I'll add a song in Instagram."* `R render <reel> --no-music`.

### Phase F: edge cases (as time allows)

- A workspace in an iCloud-synced Desktop or Documents folder. It should warn per `setup.md`; note what actually
  happens.
- Turn Wi-Fi off after setup: preview and render should still work. The board loads Google Fonts but must still
  render without them.
- Delete `.engine/proxies` and re-ingest. Add one new clip and re-ingest: only that one should be processed.
- A clip with no video stream, or one shorter than 0.5 s: it should be skipped with a message.
- Run `R doctor` again after quitting Chrome, and with Chrome open.

## Where to fix things

| Symptom | File |
| --- | --- |
| Install, uv, venv location | `skills/videomaker/bin/reelmaker` |
| ffmpeg resolution, probing (rotation, HDR detection) | `engine/reelmaker/tools.py` |
| Browser choice, codec probe, smoke render, `ok.json` | `engine/reelmaker/doctor.py` |
| Proxies, scene cuts (`SCENE`, `MIN_SHOT`, `MAX_SHOT`), HDR tone-map, HEIC, contact sheets | `engine/reelmaker/media.py` |
| Beats, tempo, drop detection, window, splice | `engine/reelmaker/music.py` |
| Frame rendering, workers (`jobs`), encode settings, stills, check, pace | `engine/reelmaker/render.py` |
| Local server (range requests, mounts `/_rt/`, `/_engine/`, `/`) | `engine/reelmaker/server.py` |
| Video seeking in the page | `engine/web/media.js`, `engine/web/comp.html` |
| Edit semantics (positions, cuts, hits, camera) | `skills/video-template/runtime/reel.js` |
| Type styles and cards | `skills/video-template/kit/cards.js` (the starter kit) |
| Storyboard page | `skills/video-template/scripts/storyboard.template.html`, `storyboard.py` |
| What Claude does | the two `SKILL.md` files and `skills/videomaker/reference/*.md` |
| Music catalog | `skills/videomaker/reference/catalog.json` (measured with `music.py`; licences in `music.md`) |

After a change, run `node scripts/build.mjs` from the repo root (it validates skills and refreshes the manifests),
plus `R check` and `R stills` on a test reel. If you change `engine/pyproject.toml`, run `uv lock` in `engine/`. Bump
`plugins/videomaker/plugin.json` `version` before Zac merges.

## Rules

- **No pushing to main, merging, or publishing without Zac's explicit go-ahead.** Commit fixes to a branch off main
  (e.g. `videomaker-mac-fixes`), with clear messages, and push only when he says so.
- **No client assets in the repo**: logos, footage, music, kits or names. `.gitignore` won't catch them, so check
  `git status` before every commit.
- `board.html` and `preview.mp4` contain footage of real people. Publish a board only as a private artifact for Zac,
  and only if he wants it.
- Don't download catalog tracks in bulk. Their terms forbid mass downloading; `R fetch` is one track at a time, on
  demand.
- Keep skill text plain and short for a non-technical reader. The house style is in the existing `SKILL.md` files.

## Report back

Write `plugins/videomaker/TEST-RESULTS-mac.md` and tell Zac it's there:

```markdown
# videomaker on a Mac: test results (<date>)

Machine: <chip>, macOS <version>, Chrome <yes/version|no>, Homebrew <yes|no>, network <rough speed>

| Phase | Result | Time | Notes |
| --- | --- | --- | --- |
| A install | pass/fail | | commands that worked, prompts |
| B doctor (bare) | | | per step: uv, venv, ffmpeg, browser, smoke |
| C video-template | | | artifact or local, questions asked, changes |
| D first reel | | | ingest rate, render fps/workers, stops, prompts |
| E changes | | | |
| F edge cases | | | |

## Bugs found (and fixed on the branch?)
## Owner-experience notes (confusing moments, unnecessary questions, too many prompts)
## Visual check of reel.mp4 (HDR, rotation, sync, text, audio)
## Recommendation: ready for the client? What must change first?
```

Attach or point to `stills.jpg` and a short screen recording if anything looks wrong.
