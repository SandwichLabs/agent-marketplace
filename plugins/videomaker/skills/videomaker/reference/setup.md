# Setup: what the launcher and `doctor` do

The skill runs on the person's own computer, in a folder of their clips. It installs everything it needs into their
user account, with no admin password, and checks it all with one command.

## Where it runs

- **Claude desktop's Code tab (the default), or Claude Code in a terminal.** These have a shell on the computer, so
  the skill can read the clips folder, install tools and render.
- **Cowork** should also work (a sandboxed computer with the chosen folder), as long as it has internet for the first
  setup. It renders with Playwright's Chromium instead of the person's Chrome.
- **A chat with code execution only** runs in a cloud sandbox that can't see the person's folders. Don't try to render
  there. Offer the video-template skill (it works in chat) and say that making the video needs the Code tab.

## The workspace

One folder per business, chosen with the person. A good default is `~/Movies/Reels`. Avoid folders synced to iCloud
or Dropbox (Desktop and Documents often are), because the proxies take gigabytes. The folder holds:

```
clips/     their videos and photos, any format the phone or camera produced
music/     tracks: theirs, downloaded catalog tracks (each with its licence), Suno exports
kit/       the video kit (brand.json, cards.js, fonts, logo, storyboard.html)
reels/     one folder per reel: edit.json, beats.json, track.wav, preview.mp4, reel.mp4, caption.txt, board.html
.engine/   the cache: proxies, thumbnails, contact sheets, library.json, ok.json (safe to delete; ingest rebuilds it)
```

Open the workspace folder in the Code tab, or `cd` into it, so it's the current folder. Every `reelmaker` command
works on the current folder (or `--ws <folder>`).

## The launcher: `bin/reelmaker`

Run it by its full path inside this skill's folder, e.g. `"<skill folder>/bin/reelmaker" doctor`. On first use it:

1. **Installs uv** if it's missing (`curl -LsSf https://astral.sh/uv/install.sh | sh`, about 10 s, into
   `~/.local/bin`).
2. **Creates the Python environment** from the engine's lockfile on the first `uv run`: Python 3.12 (uv downloads it),
   numpy, librosa, Pillow, Playwright, static-ffmpeg. That's 30–90 s on a normal connection, once. The environment
   lives in `~/Library/Caches/reelmaker/venv` on a Mac, never in the workspace.

## `reelmaker doctor`

| Step | What happens | First time |
| --- | --- | --- |
| ffmpeg | Uses one on the PATH or from Homebrew. Otherwise it downloads a static build through static-ffmpeg. Checks for the H.264 encoder. | 0–30 s |
| Browser | Tries Google Chrome first (most Macs have it), then Playwright's Chromium, downloading it if needed (about 100–170 MB). It decodes a test clip in each browser to learn which proxy codec works (H.264, or VP9 as the fallback). | 0–60 s |
| Kit | If `kit/` doesn't exist yet, copies the neutral starter kit. | instant |
| Smoke render | Renders one second of a test reel and checks the file. | 5–10 s |

It writes `.engine/ok.json`. After that, `reelmaker doctor --quick` returns in about a second. Run the full `doctor`
again after an OS or Chrome update if renders start failing.

## Permission prompts

The Code tab asks before running commands. Tell the person in one line what's about to happen ("This installs the
video tools into your user folder. No password needed, about two minutes the first time.") so the prompts aren't a
surprise. If they'd like fewer prompts, they can allow the `reelmaker` commands for this folder.

## When something goes wrong

| What you see | What to do |
| --- | --- |
| `curl: command not found` or no internet | The first setup needs internet. Try again on a working connection. |
| ffmpeg download fails | If they have Homebrew: `brew install ffmpeg`. Otherwise retry `doctor`; the static build comes from GitHub. |
| `no browser could decode a test clip` | Install Google Chrome (google.com/chrome), then run `doctor` again. |
| `codec not supported by this browser` during a render | Proxies were made for another browser. Delete `.engine/proxies` and run `ingest` again. |
| Renders are slow | Close other apps. `-j 2` uses fewer workers on a small laptop. A 30 s reel takes 1–3 minutes on most laptops. |
| `the edit failed to load` | `reelmaker check <reel>` names the problem (usually a typo in edit.json). |
| Disk is filling up | `.engine/proxies` is the big folder. Delete it and re-ingest only what's needed. |
