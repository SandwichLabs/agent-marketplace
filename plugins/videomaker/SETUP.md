# Install videomaker (instructions for Claude)

> **For people:** this page is written for Claude. Open the **Code** tab in the Claude desktop app, choose (or create)
> the folder for your videos, paste this in, and Claude takes it from here:
>
> *Install the videomaker plugin by following
> https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/videomaker/SETUP.md. Walk me through
> anything I need to click, one step at a time.*

## Your job, Claude

The person wants the **videomaker** plugin: two skills that make beat-matched promo reels from their own clips.
**video-template** designs their brand's video kit, and **videomaker** renders reels with it on their computer. Get it
installed, set up a workspace, run the setup check, and hand off to the video-template skill.

They're usually a business owner, not a developer. One step per message, plain words, and wait for "done" or what
they see before moving on. Never say it's installed until you've seen it work.

## Step 1: check where you are

You need a shell on their computer: the **Code tab** in Claude desktop, or Claude Code in a terminal. Check with
`uname -s && pwd`.

- If you have no shell (a chat with only a cloud sandbox), tell them: "Making videos needs the Code tab in the Claude
  desktop app. Open it, pick a folder for your videos, and paste the same message there." You can still offer to start
  their video kit here with the video-template skill.

## Step 2: add the marketplace and install

Ask them to type these into the prompt, one at a time, waiting for each to finish (you can't run slash commands for
them):

```
/plugin marketplace add SandwichLabs/agent-marketplace
```

```
/plugin install videomaker@sandwichlabs
```

If their Claude asks, they should choose to install it for their user. Then confirm it's there: the skills
**videomaker** and **video-template** should be available (after `/reload-plugins`, or in a new session if not).

If the `/plugin` commands aren't available in their app, fall back to `claude plugin marketplace add
SandwichLabs/agent-marketplace` and `claude plugin install videomaker@sandwichlabs` in the shell, or download the
repository (`https://codeload.github.com/SandwichLabs/agent-marketplace/zip/refs/heads/main`) and work from
`plugins/videomaker/skills/` directly for this session.

## Step 3: the workspace

Use the folder they opened if it's meant for videos; otherwise suggest `~/Movies/Reels`. Avoid Desktop and Documents if
iCloud syncs them (the video cache is large). Then:

1. Find the installed skill folder (the plugin cache, e.g. `~/.claude/plugins/…/videomaker/skills/videomaker`).
2. Run `"<skill folder>/bin/reelmaker" init` from the workspace.
3. Ask them to drag their clips and photos into `clips/`, and any music they own into `music/` (or tell you where
   they are, and copy them in).

## Step 4: set up the tools

Tell them first: "Next I'll install the video tools into your user folder: no password, about two minutes, and you
may see a few permission prompts." Then run `"<skill folder>/bin/reelmaker" doctor`.

It installs uv, Python and its libraries, finds or downloads ffmpeg, finds Google Chrome or downloads a browser,
copies the starter kit and renders a one-second test. If it fails, follow the table at the end of the videomaker
skill's `reference/setup.md`.

## Step 5: make it theirs

Hand off to the **video-template** skill to build their kit from their logo and website. When the storyboard looks
right to them, suggest a first reel: "Make a 30-second reel for <their offer>."

## If something goes wrong

| What they see | What to do |
| --- | --- |
| `/plugin` isn't recognized | Update the Claude desktop app. Or use the `claude plugin …` shell commands from Step 2. |
| Permission prompts for every command | Normal the first time. They can allow `reelmaker` commands for this folder. |
| `doctor` can't download something | Check the internet connection and run it again. See `reference/setup.md`. |
| No browser works | Install Google Chrome from google.com/chrome, then run `doctor` again. |
