# videomaker on a Mac: test results (2026-10-09)

Machine: Apple M5 (10 cores, 24 GB), macOS 26.6.2 (25G83), Chrome yes (154.0.8037.99), Homebrew yes
(`/opt/homebrew/bin/brew`, with uv and ffmpeg from Homebrew), network <tbd>. iCloud Drive is on (Desktop & Documents
sync to be confirmed in Phase F).

| Phase | Result | Time | Notes |
| --- | --- | --- | --- |
| setup | pass | | `git clone` + `node scripts/build.mjs --check`: 3 plugin(s) valid. Branch `videomaker-mac-fixes`. |
| A install | pass (after fix) | | One-step `/plugin install videomaker --marketplace …` failed: the marketplace had to be added first. Worked: `/plugin marketplace add SandwichLabs/agent-marketplace`, then `/plugin install videomaker@sandwichlabs`. User scope. Cache: `~/.claude/plugins/cache/sandwichlabs/videomaker/0.1.0` (commit 9cc5491). Both skills listed in the session. |
| B doctor (bare) | | | |
| C video-template | | | |
| D first reel | pass with workaround | | Agent run in `~/Reels` (data consultancy kit, Mixkit stock footage + catalog track): finished 31.7 s reel, 1080×1920, 13.6 cuts/10 s. Renders hung until `-j 1` (bug 4). Agent's report: `~/Reels/FEEDBACK.md`. After the fix: render 950 frames in 9 s (~100 fps, 5–8 workers), ~30 s wall; check 5–6 s; preview 7 s; stills 3 s. |
| E changes | | | |
| F edge cases | | | |

## Bugs found (and fixed on the branch?)

1. **Install command (A).** The one-step `--marketplace` form doesn't work on a fresh install. Fixed: SETUP.md and
   README.md now give the two commands as the default path.
2. **Bare bootstrap can't be simulated on a Homebrew Mac (B).** The launcher prepends `/opt/homebrew/bin` to PATH, so
   Homebrew's uv is always found. Not a bug for owners; it means the uv-install path needs a fresh user account to test.

3. **Storyboard showed gym copy for a dev shop (C).** `storyboard.py` always played the starter's gym sample reel
   ("STRONGER EVERY WEEK", squat/sled shot labels), whatever the business. Fixed: video-template now starts by working
   out the kind of business and the goal of its reels (from the site, or by asking), stores it in `brand.json`
   `business`, and writes `kit/sample-edit.json` with placeholder copy and shot names that suit that business.
   `storyboard.py` uses the kit's sample reel when there is one and warns when a finished kit falls back to the gym one.

4. **P0: renders hung on macOS (D).** Reproduced: about 1 in 4 `check` runs hung forever. Cause: `media.js` waited for
   `loadeddata` whenever a video's `readyState` was below 2, but it drops back to 1 while a seek fetches unbuffered data
   and `loadeddata` fires once per load. Fixed (3d12a61): 0 stalls in 25 checks; render output SSIM 0.997 vs the `-j 1`
   reel. Hardening in the same commit: ENOBUFS-safe resumable sends and 4 MB range spans in `server.py`, a per-frame
   45 s watchdog (reopen once, then fail naming the media), progress every 5 s, server tracebacks to `.engine/server.log`.
5. **`reelmaker tag` one shot per call.** Now takes comma lists and patterns (477db38).
6. **No contrast checker.** `storyboard.py` now prints accent/bg contrast and warns below 4.5:1 (477db38).
7. **Docs assume a gym; catalog and reelmaker path hard to find; board too big to publish.** Fixed in the docs pass.

Open from FEEDBACK.md (not yet done): stock-footage path, font download helper, `check` warnings for tiny fitted text
and thin/accent text over bright footage, smaller proxies, a lighter board, `music` hint when the window's first bars
are flat. Note: the feedback agent says the one-step `--marketplace` install worked; Zac's own run needed the
marketplace added first (the marketplace may already have been added by then).

## Owner-experience notes (confusing moments, unnecessary questions, too many prompts)

## Visual check of reel.mp4 (HDR, rotation, sync, text, audio)

## Recommendation: ready for the client? What must change first?

Merged as 0.2.0 on 2026-10-09. Zac ran a fresh install end to end and signed it off as the first version. Deferred by Zac: stock-footage path, font helper,
extra `check` warnings, smaller proxies, lighter board (the client has his own footage). Still unverified on a Mac:
real iPhone footage (HEVC/HDR, rotation, HEIC, 60 fps/4K), the bare-machine bootstrap (Phase B), and Phase E/F.
