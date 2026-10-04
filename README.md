# Sandwich Labs agent marketplace

Skills and plugins from [Sandwich Labs](https://sandwichlabs.dev) for small businesses that run their operations with
an AI agent. One repo, installable from Claude first, and from Codex, ChatGPT and any app that takes an uploaded skill.

| Plugin | What it does | Skills |
| --- | --- | --- |
| [**mindbody**](plugins/mindbody) | Run a studio's Mindbody business site from your agent, in your own Chrome: schedules, rosters, bookings, client status, sales, attendance, reports. Asks before anything that moves money. | `mindbody` |
| [**pr-sizzle-reel**](plugins/pr-sizzle-reel) | Plan a beat-matched Instagram reel for The PR Method: a script in the studio's voice, a cut sheet timed to a song from your library, and a CapCut walkthrough. | `pr-sizzle-reel` |

## Install

### Claude desktop and claude.ai (easiest)

Paste the plugin's install prompt into a new chat (each plugin's `SETUP.md` starts with its own). For Mindbody:

> Use the skill-creator skill to install the Mindbody skill by following
> https://raw.githubusercontent.com/SandwichLabs/agent-marketplace/main/plugins/mindbody/SETUP.md. Walk me through
> anything I need to click, one step at a time.

Claude fetches the skill, checks and packages it, and hands you a file with a **Save skill** button, then helps with
anything else the plugin needs (for Mindbody, connecting Claude in Chrome). Each plugin's `SETUP.md` is written for
Claude to follow.

By hand: download the skill from the [latest release](https://github.com/SandwichLabs/agent-marketplace/releases/latest)
(`mindbody.skill`), then **Customize → Skills → + → Upload a skill**. Needs **Settings → Capabilities → Code execution and
file creation**.

### Claude Code and Cowork

```
/plugin marketplace add SandwichLabs/agent-marketplace
/plugin install mindbody@sandwichlabs
```

### Codex

```
codex plugin marketplace add SandwichLabs/agent-marketplace
```

Then install **mindbody** from the Sandwich Labs marketplace in `/plugins`. ChatGPT reads the same catalog
(`.agents/plugins/marketplace.json`) from a local checkout; otherwise upload `mindbody.zip` from the latest release under
Plugins → Skills.

### Everything else (Gemini, Copilot, Cursor, other agents)

Every plugin is an [Agent Plugins](https://agent-plugins.org) package and every skill follows the
[Agent Skills](https://agentskills.io/specification) format. Upload `<skill>.zip` from the latest release where the app
takes a skill upload, or point the agent at the plugin folder (`plugins/<name>/`).

What each platform supports, and why the repo looks like this: [docs/platforms.md](docs/platforms.md).

## Layout

```
marketplace.config.json            ← the catalog: plugin order, categories, Codex policy        (edit)
plugins/<name>/
  plugin.json                      ← Agent Plugins 1.1.0 manifest, the plugin's metadata          (edit)
  skills/<skill>/SKILL.md …        ← the skills                                                  (edit)
  SETUP.md                         ← install instructions written for Claude desktop             (edit)
  .claude-plugin/plugin.json       ← generated: Claude manifest
  .codex-plugin/plugin.json        ← generated: Codex manifest (legacy location)
.claude-plugin/marketplace.json    ← generated: Claude catalog
.agents/plugins/marketplace.json   ← generated: Codex / ChatGPT catalog
scripts/build.mjs                  ← validates, regenerates the manifests, packages dist/<skill>.skill|.zip
```

## Adding or changing a plugin

1. Create `plugins/<name>/plugin.json` (copy `plugins/mindbody/plugin.json`; `name` must match the folder) and put
   skills under `plugins/<name>/skills/<skill>/SKILL.md`.
2. List it in `marketplace.config.json`.
3. Write `plugins/<name>/SETUP.md` for Claude desktop users (copy the Mindbody one and change the specifics).
4. Bump `version` in `plugin.json` when you change a plugin: marketplaces offer updates by version.
5. Run `node scripts/build.mjs`, then `claude plugin validate . --strict`, and commit the generated files. CI runs
   `node scripts/build.mjs --check` and fails if they're stale.
6. Release: push a tag `vYYYY.MM.DD` (or any `v*`) and the release workflow attaches every `dist/<skill>.skill` and
   `.zip`. The `releases/latest/download/<skill>.skill` links in each `SETUP.md` always point at the newest.

Each skill is checked like skill-creator's validator does (kebab-case `name` matching its folder, a `description` of at
most 1024 characters with no angle brackets, standard frontmatter keys only, one `SKILL.md`), plus every relative link
in its Markdown.

---

Not affiliated with the vendors whose software these plugins operate. Trademarks belong to their owners.
