# Install the Mindbody skill (instructions for Claude)

> **For people:** this page is written for Claude. Paste this into a new chat in the Claude desktop app and Claude
> takes it from here:
>
> *Use the skill-creator skill to install the Mindbody skill by following
> https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/mindbody/SETUP.md. Walk me through anything I need to click,
> one step at a time.*

## Your job, Claude

The person you're talking to runs or works at a studio that uses **Mindbody**, and wants the **mindbody** skill in their
Claude. With it, Claude can work in their Mindbody business site through the Claude in Chrome extension: today's
schedule and rosters, booking and cancelling, membership and balance checks, notes, sales, attendance and top members,
and more.

You'll use the **skill-creator** skill to check the skill and package it as a `.skill` file. When you share that file in
the chat, it shows a **Save skill** button. **You can't press it for them**: installing is always the person's click. So
your job is to:

1. get the skill files into your sandbox;
2. check and package them with skill-creator, and share the `.skill` file;
3. walk them through saving it, and through connecting Claude in Chrome if they haven't;
4. confirm it works.

Keep every message short: one step, then wait for them to say "done" or tell you what they see. They're running a
studio, not writing software, so avoid jargon. Claude's settings move between versions: if what they describe doesn't
match these steps, work from what they see.

Never say it's installed until they've confirmed it appears in their skills list.

## Step 1: check two things

Ask them to confirm both. You can't see their settings.

1. **They're in the Claude desktop app** (claude.ai in a browser works too), on any plan.
2. **Code execution is on:** **Settings → Capabilities → "Code execution and file creation"**. Skills need it.
   - On a **Team or Enterprise** plan, an admin has to allow skills (**Organization settings → Plugins & skills**). If
     they can't change it, stop and tell them who to ask.

## Step 2: get the skill

The skill is the folder `plugins/mindbody/skills/mindbody/` in Sandwich Labs' public agent marketplace,
**https://github.com/SandwichLabs/agent-marketplace**: a `SKILL.md` plus a wiki of a few hundred small Markdown files.
Each release also attaches it pre-packaged as `mindbody.skill` (a zip that opens to `mindbody/SKILL.md`).

In your sandbox, try these in order and use the first that works:

1. **Download the packaged release** and unpack it:
   ```bash
   mkdir -p /tmp/mb && cd /tmp/mb
   curl -fsSL -o mindbody.skill https://github.com/SandwichLabs/agent-marketplace/releases/latest/download/mindbody.skill
   unzip -q mindbody.skill && ls mindbody/SKILL.md
   ```
2. **Or download the repository** and take the folder:
   ```bash
   mkdir -p /tmp/mb && cd /tmp/mb
   curl -fsSL -o repo.zip https://codeload.github.com/SandwichLabs/agent-marketplace/zip/refs/heads/main
   unzip -q repo.zip && mv agent-marketplace-main/plugins/mindbody/skills/mindbody ./mindbody && ls mindbody/SKILL.md
   ```
3. **No internet in your sandbox?** Ask them to download
   https://github.com/SandwichLabs/agent-marketplace/releases/latest/download/mindbody.skill and attach it to this chat.
   Unzip what they attach the same way. If you can't take attachments either, skip to **Plan B** at the end.

## Step 3: check and package it with skill-creator

Use the **skill-creator** skill. You're installing a finished skill, not writing one, so skip its interview, test and
eval steps and only:

1. **Validate** the folder: run skill-creator's `scripts/quick_validate.py` on `/tmp/mb/mindbody`, or check by hand
   that `SKILL.md` has frontmatter with `name: mindbody` and a `description` under 1024 characters. Tell the person it
   checked out.
2. **Package** it: `python -m scripts.package_skill /tmp/mb/mindbody /tmp/mb/out` from skill-creator's folder. That
   writes `/tmp/mb/out/mindbody.skill`.
3. **Share** `mindbody.skill` with them as a file in the chat.

If skill-creator isn't available, share the `mindbody.skill` you downloaded in Step 2 (option 1) as it is: it's already
packaged.

## Step 4: walk them through saving it

One step per message:

1. Click **Save skill** on the `mindbody.skill` file card.
   - **No Save skill button?** Ask them to download the file instead, then open **Customize → Skills**, click **+**,
     choose **Upload a skill**, and pick `mindbody.skill`. If it insists on a `.zip`, the same file renamed to
     `mindbody.zip` works.
2. Check **mindbody** now appears under **Customize → Skills** and its switch is **on**.

## Step 5: connect Claude in Chrome

The skill does its work in their own Chrome, where they're already signed in to Mindbody. Ask whether they use the
**Claude in Chrome** extension with this Claude app.

- **Not yet:** have them install **Claude in Chrome** from the Chrome Web Store (search "Claude in Chrome"), sign in
  with the same Claude account, and allow it when Claude asks to connect. Claude's in-app instructions for Chrome are
  the reference; keep it to one step per message.
- **Already connected:** move on.

They should also be **signed in to Mindbody** (`clients.mindbodyonline.com`) in that Chrome. Claude never types their
Mindbody password.

## Step 6: check it works

Ask them to start a **new chat** and type: **"What's on the class schedule today in Mindbody?"**

It's working if Claude uses the mindbody skill, opens Mindbody in Chrome (Chrome may ask once to allow
`clients.mindbodyonline.com`), and comes back with today's classes and booked/capacity counts. Tell them that, give them
two or three things to try next ("who's new in tonight's 6pm?", "is Sam Smith's membership active?", "who were our top
members last month?"), and you're done.

## If something goes wrong

| What they see | What to do |
| --- | --- |
| No **Skills** under Customize | Update the Claude app and check code execution is on (Step 1). On Team/Enterprise, ask the admin. |
| Upload error: folder name or structure | The archive must open to `mindbody/SKILL.md`. Re-package with skill-creator (Step 3). |
| Upload error: too large or not a zip | They probably picked an unzipped folder or a different file. Give them a fresh `mindbody.skill`. |
| A new chat doesn't use the skill | Check the switch in Customize → Skills, then start a **new** chat: open chats don't pick up new skills. Mentioning "Mindbody" in the request helps. |
| Claude says it has no browser tools | Claude in Chrome isn't connected to this app (Step 5). |
| Mindbody shows a login page | They sign in themselves in Chrome, then ask again. |
| They want the latest version later | Paste the same prompt again. Saving a skill with the same name replaces the old one. |

## Plan B: use it without installing

If installing isn't possible right now, offer to work from the files directly in this chat: read
https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/mindbody/skills/mindbody/SKILL.md and follow it as if it were
installed, fetching the files it points to from the same place
(`.../main/plugins/mindbody/skills/mindbody/chrome-extension/recipes/README.md` and so on). It works for this conversation; installing
makes it permanent.
