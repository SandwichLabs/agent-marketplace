# Platforms: what each one reads, and why this repo looks the way it does

*Updated 2026-10-04. Builds on Sandwich Labs' "executable documentation" research (2026-10-03): ship instructions and
skills to the agent people already run, instead of shipping software.*

## The three layers

| Layer | Standard? | What we use |
| --- | --- | --- |
| **Skill** (`SKILL.md` + files) | Yes: [Agent Skills](https://agentskills.io/specification), read by nearly every agent | `plugins/<name>/skills/<skill>/` |
| **Plugin** (skills + MCP + metadata) | Yes, since 2026: [Agent Plugins 1.1.0](https://agent-plugins.org), steered by Amazon, Cursor, Microsoft, OpenAI and Vercel. Root `plugin.json`, fixed `skills/` and `mcp.json` locations, client data under `extensions.<reverse-domain>` | `plugins/<name>/plugin.json` is the source of truth |
| **Marketplace** (a catalog of plugins) | **No.** Each vendor has its own file, all "a git repo with a JSON catalog" | Generated per vendor from `marketplace.config.json` |

Since there's still no open catalog format, `scripts/build.mjs` writes each vendor's file from one config, the way the
research suggested. Agent Plugins removed the need for one per-vendor *plugin* manifest (OpenAI reads the root
`plugin.json`), but Claude still reads `.claude-plugin/plugin.json`, and older Codex reads `.codex-plugin/plugin.json`, so
those are generated too.

## Per platform

| Platform | How people install | What it reads here | Runtime for the skill | Tested |
| --- | --- | --- | --- | --- |
| **Claude Code, Cowork** | `/plugin marketplace add SandwichLabs/agent-marketplace` → `/plugin install <name>@sandwichlabs` | `.claude-plugin/marketplace.json`, `plugins/<name>/.claude-plugin/plugin.json`, `skills/` | Full shell; scripts run | ✅ `claude plugin validate . --strict` passes; added, installed and enabled from a local checkout with Claude Code 2.1.289 (skill discovered, ~210 tokens idle, ~1.6k loaded) |
| **Claude desktop, claude.ai** | Paste the plugin's install prompt: Claude follows `SETUP.md`, packages with skill-creator, user clicks **Save skill**. Or upload `<skill>.skill` under Customize → Skills | `SETUP.md`, the release asset, or the repo zip | Sandbox with code execution; Chrome via Claude in Chrome | ⚠️ download paths and skill-creator packaging verified; the Save-skill click and a live run not yet |
| **Codex** | `codex plugin marketplace add SandwichLabs/agent-marketplace`, then install from `/plugins` | `.agents/plugins/marketplace.json` (`source: local`, `policy`, `category`), root `plugin.json` or `.codex-plugin/plugin.json` | Full local shell | ⚠️ written to OpenAI's [plugin docs](https://developers.openai.com/plugins/build/plugins); not run (no Codex CLI here) |
| **ChatGPT** | Reads the same repo or personal catalog from a local checkout; public listing needs OpenAI's submission portal. Or upload `<skill>.zip` (Plugins → Skills) | `.agents/plugins/marketplace.json`, or the zip | Cloud computer + browser (Dots) | ❌ not tested |
| **Gemini (Spark, chat), Antigravity** | Upload a folder or zip with `SKILL.md` at its root (Spark: up to 100 MB). No third-party catalog found | `<skill>.zip` | Workspace-oriented; scripts may not run | ❌ not tested |
| **Copilot, Cursor, other agents** | Point at `plugins/<name>/` or upload the zip, depending on the client | `plugin.json` (Agent Plugins) and `skills/` | Usually a local shell | ❌ not tested |

## Rules that keep skills portable

- **Spec-only frontmatter** in `SKILL.md`: `name`, `description` (and optionally `license`, `compatibility`,
  `metadata`). Vendor fields like `allowed-tools` aren't portable.
- **Don't hard-code one vendor's tool names.** Describe the capability ("the Claude in Chrome tools: `navigate`,
  `javascript_tool`…") and say what to do when it's missing. The Mindbody skill needs a browser-control extension, so it
  says so up front.
- **Packages open to `<skill>/SKILL.md`.** That's what skill-creator's `package_skill.py`, Claude's skill upload and the
  Agent Plugins `skills/` discovery all expect.
- **Versions matter.** Catalogs offer updates by the plugin's `version`; bump it whenever a plugin changes.

## Sources

- Agent Plugins specification 1.1.0 and schemas: https://agent-plugins.org, https://github.com/agentplugins/agent-plugins-spec
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- OpenAI plugins (Codex, ChatGPT): https://developers.openai.com/plugins/build/plugins
- Agent Skills specification: https://agentskills.io/specification
