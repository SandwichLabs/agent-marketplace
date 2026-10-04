# Install the PR Method reel skill (instructions for Claude)

> **For people:** this page is written for Claude. Paste this into a new chat in the Claude desktop app and Claude
> takes it from here:
>
> *Use the skill-creator skill to install the PR Method reel skill by following
> https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/pr-sizzle-reel/SETUP.md. Walk me through
> anything I need to click, one step at a time.*

## Your job, Claude

The person you're talking to (usually Phil, owner of The PR Method Fitness) wants the **pr-sizzle-reel** skill in their
Claude. With it, Claude plans a beat-matched Instagram reel with them: a script in the studio's voice, a cut sheet timed
to a song from their own library, and a CapCut walkthrough.

You'll use the **skill-creator** skill to check the skill and package it as a `.skill` file. When you share that file in
the chat, it shows a **Save skill** button. **You can't press it for them**: installing is always their click. So:

1. get the skill files into your sandbox;
2. check and package them with skill-creator, and share the `.skill` file;
3. walk them through saving it;
4. confirm it works.

Keep every message short: one step, then wait for "done" or what they see. They're a coach, not a developer: avoid
jargon. Claude's settings move between versions; if what they describe doesn't match, work from what they see. Never say
it's installed until they've confirmed it's in their skills list.

## Step 1: check two things

Ask them to confirm both. You can't see their settings.

1. **They're in the Claude desktop app** (claude.ai in a browser works too), on any plan.
2. **Code execution is on:** **Settings → Capabilities → "Code execution and file creation"**. Skills need it.
   - On a **Team or Enterprise** plan, an admin has to allow skills (**Organization settings → Plugins & skills**).

## Step 2: get the skill

The skill is the folder `plugins/pr-sizzle-reel/skills/pr-sizzle-reel/` in Sandwich Labs' public agent marketplace,
**https://github.com/SandwichLabs/agent-marketplace**: five small Markdown files (`SKILL.md`, `brand.md`, `music.md`,
`examples.md`, `capcut.md`). Each release also attaches it pre-packaged as `pr-sizzle-reel.skill`.

In your sandbox, use the first of these that works:

1. **Download the packaged release** and unpack it:
   ```bash
   mkdir -p /tmp/pr && cd /tmp/pr
   curl -fsSL -o pr-sizzle-reel.skill https://github.com/SandwichLabs/agent-marketplace/releases/latest/download/pr-sizzle-reel.skill
   unzip -q pr-sizzle-reel.skill && ls pr-sizzle-reel/SKILL.md
   ```
2. **Or download the repository** and take the folder:
   ```bash
   mkdir -p /tmp/pr && cd /tmp/pr
   curl -fsSL -o repo.zip https://codeload.github.com/SandwichLabs/agent-marketplace/zip/refs/heads/main
   unzip -q repo.zip && mv agent-marketplace-main/plugins/pr-sizzle-reel/skills/pr-sizzle-reel ./pr-sizzle-reel
   ```
3. **Or fetch the five files** from
   `https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/pr-sizzle-reel/skills/pr-sizzle-reel/<file>`
   into a folder named exactly `pr-sizzle-reel`.
4. **No internet in your sandbox?** Ask them to download
   https://github.com/SandwichLabs/agent-marketplace/releases/latest/download/pr-sizzle-reel.skill and attach it here.

## Step 3: check and package it with skill-creator

You're installing a finished skill, so skip skill-creator's interview, test and eval steps and only:

1. **Validate:** run skill-creator's `scripts/quick_validate.py` on `/tmp/pr/pr-sizzle-reel`.
2. **Package:** `python -m scripts.package_skill /tmp/pr/pr-sizzle-reel /tmp/pr/out` from skill-creator's folder.
3. **Share** `/tmp/pr/out/pr-sizzle-reel.skill` with them as a file in the chat.

If skill-creator isn't available, share the downloaded `pr-sizzle-reel.skill` as it is: it's already packaged.

## Step 4: walk them through saving it

1. Click **Save skill** on the file card.
   - **No button?** Download the file, then **Customize → Skills → + → Upload a skill** and pick it (rename to
     `pr-sizzle-reel.zip` if it insists on a zip).
2. Check **pr-sizzle-reel** appears under **Customize → Skills** with its switch **on**. If they had an older copy, the
   new one replaces it.

## Step 5: check it works

Ask them to start a **new chat** and type: **"Let's make a 30-second reel for the free week."**

It's working if Claude asks four questions: what the reel is for, how long, which song from their library, and which
clips they have. Tell them that, then you're done. They'll need their music library and CapCut when they make one.

## If something goes wrong

| What they see | What to do |
| --- | --- |
| No **Skills** under Customize | Update the Claude app; check code execution is on (Step 1). On Team/Enterprise, ask the admin. |
| Upload error: folder name doesn't match | The archive must open to `pr-sizzle-reel/SKILL.md`. Re-package (Step 3). |
| It uploaded, but a new chat doesn't use it | Check the switch is on, then start a **new** chat; open chats don't pick up new skills. |
| They want to change something (a new offer, a new class) | Ask Sandwich Labs to update `brand.md` in the marketplace, then paste the install prompt again. Or edit their copy: Customize → Skills → pr-sizzle-reel. |

**Can't install right now?** Offer to run the workflow from the files in this chat: read
`.../plugins/pr-sizzle-reel/skills/pr-sizzle-reel/SKILL.md` from the raw URL above and follow it exactly. It works for
one reel; installing makes it permanent.
