#!/usr/bin/env node
/**
 * One source, every vendor's manifest.
 *
 *   marketplace.config.json + plugins/<name>/plugin.json (Agent Plugins 1.1.0)
 *     → .claude-plugin/marketplace.json            Claude Code / Cowork catalog
 *     → .agents/plugins/marketplace.json           Codex / ChatGPT catalog
 *     → plugins/<name>/.claude-plugin/plugin.json  Claude plugin manifest
 *     → plugins/<name>/.codex-plugin/plugin.json   Codex legacy manifest (newer Codex reads plugin.json directly)
 *     → dist/<skill>.skill, dist/<skill>.zip       upload packages for apps without a catalog (claude.ai, ChatGPT, Gemini)
 *
 * Usage:
 *   node scripts/build.mjs           validate, write manifests, package skills
 *   node scripts/build.mjs --check   validate and fail if any generated manifest is stale (CI)
 *
 * No dependencies: Node 20+, python3 (skill validation) and zip.
 */
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";

const root = resolve(dirname(new URL(import.meta.url).pathname), "..");
const check = process.argv.includes("--check");
const errors = [];
const stale = [];

const AP_SCHEMA = "https://agent-plugins.org/schemas/1.1.0/plugin.schema.json";
const AP_FIELDS = new Set(["$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"]);
const NAME = /^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$/;
const POLICY_INSTALL = new Set(["NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"]);
const POLICY_AUTH = new Set(["ON_INSTALL", "ON_USE"]);

const readJSON = (p) => JSON.parse(readFileSync(join(root, p), "utf8"));
const json = (v) => `${JSON.stringify(v, null, 2)}\n`;
const pick = (o, keys) => Object.fromEntries(keys.filter((k) => o[k] !== undefined).map((k) => [k, o[k]]));

function emit(path, value) {
	const text = json(value);
	const abs = join(root, path);
	const current = existsSync(abs) ? readFileSync(abs, "utf8") : null;
	if (current === text) return;
	if (check) return stale.push(path);
	mkdirSync(dirname(abs), { recursive: true });
	writeFileSync(abs, text);
	console.log(`wrote ${path}`);
}

/** Agent Plugins 1.1.0 §5: a closed manifest schema; anything else is fatal for the plugin. */
function validateManifest(dir, m) {
	const where = `plugins/${dir}/plugin.json`;
	for (const k of Object.keys(m)) if (!AP_FIELDS.has(k)) errors.push(`${where}: unknown top-level field "${k}" (put client data under extensions)`);
	if (m.$schema !== AP_SCHEMA) errors.push(`${where}: $schema must be ${AP_SCHEMA}`);
	if (typeof m.name !== "string" || m.name.length > 64 || !NAME.test(m.name)) errors.push(`${where}: invalid name ${JSON.stringify(m.name)}`);
	if (m.name !== dir) errors.push(`${where}: name "${m.name}" must match its folder "${dir}"`);
	for (const k of ["version", "description", "homepage", "repository", "license"]) {
		if (m[k] !== undefined && typeof m[k] !== "string") errors.push(`${where}: ${k} must be a string`);
	}
	if (m.keywords !== undefined && !(Array.isArray(m.keywords) && m.keywords.every((k) => typeof k === "string"))) errors.push(`${where}: keywords must be strings`);
	if (m.author !== undefined) {
		const bad = typeof m.author !== "object" || Object.keys(m.author).some((k) => !["name", "email", "url"].includes(k));
		if (bad) errors.push(`${where}: author may only have name, email, url`);
	}
	if (m.extensions !== undefined && (typeof m.extensions !== "object" || Array.isArray(m.extensions))) errors.push(`${where}: extensions must be an object`);
	if (!m.version) errors.push(`${where}: set a version (marketplaces use it to offer updates)`);
	if (!m.description) errors.push(`${where}: set a description (catalogs show it)`);
}

function skillsOf(dir) {
	const base = join(root, "plugins", dir, "skills");
	if (!existsSync(base)) return [];
	return readdirSync(base).filter((s) => existsSync(join(base, s, "SKILL.md")) && statSync(join(base, s)).isDirectory());
}

// ---------------------------------------------------------------------------------------------------------------

const config = readJSON("marketplace.config.json");
if (!NAME.test(config.name)) errors.push(`marketplace.config.json: invalid marketplace name ${config.name}`);

const onDisk = readdirSync(join(root, "plugins")).filter((d) => existsSync(join(root, "plugins", d, "plugin.json")));
const listed = config.plugins.map((p) => p.name);
for (const d of onDisk) if (!listed.includes(d)) errors.push(`plugins/${d} has a plugin.json but is not listed in marketplace.config.json`);

const plugins = [];
for (const entry of config.plugins) {
	const dir = entry.name;
	if (!existsSync(join(root, "plugins", dir, "plugin.json"))) {
		errors.push(`marketplace.config.json lists "${dir}" but plugins/${dir}/plugin.json is missing`);
		continue;
	}
	const m = readJSON(`plugins/${dir}/plugin.json`);
	validateManifest(dir, m);
	if (entry.policy) {
		if (!POLICY_INSTALL.has(entry.policy.installation)) errors.push(`${dir}: policy.installation must be one of ${[...POLICY_INSTALL]}`);
		if (!POLICY_AUTH.has(entry.policy.authentication)) errors.push(`${dir}: policy.authentication must be one of ${[...POLICY_AUTH]}`);
	}
	const skills = skillsOf(dir);
	for (const s of skills) {
		const r = spawnSync("python3", [join(root, "scripts/validate_skill.py"), join(root, "plugins", dir, "skills", s)], { encoding: "utf8" });
		if (r.status !== 0) errors.push(`plugins/${dir}/skills/${s}: ${(r.stdout + r.stderr).trim()}`);
		else console.log(r.stdout.trim());
	}
	plugins.push({ dir, entry, m, skills });
}

if (errors.length) {
	console.error(errors.map((e) => `✗ ${e}`).join("\n"));
	process.exit(1);
}

// Claude: plugin manifests. Skills are discovered from skills/, so the manifest is metadata only.
const meta = ["name", "version", "description", "author", "homepage", "repository", "license", "keywords"];
for (const { dir, m } of plugins) {
	emit(`plugins/${dir}/.claude-plugin/plugin.json`, pick(m, meta));
	const ui = m.extensions?.["com.openai"]?.interface;
	emit(`plugins/${dir}/.codex-plugin/plugin.json`, { ...pick(m, meta), skills: "./skills/", ...(ui ? { interface: ui } : {}) });
}

// Claude catalog.
emit(".claude-plugin/marketplace.json", {
	name: config.name,
	description: config.description,
	owner: config.owner,
	plugins: plugins.map(({ dir, entry, m }) => ({
		...pick(m, ["name", "description", "version", "author", "homepage", "repository", "license", "keywords"]),
		source: `./plugins/${dir}`,
		...(entry.category ? { category: entry.category.toLowerCase() } : {}),
	})),
});

// Codex / ChatGPT catalog.
emit(".agents/plugins/marketplace.json", {
	name: config.name,
	interface: { displayName: config.displayName },
	plugins: plugins.map(({ dir, entry }) => ({
		name: dir,
		source: { source: "local", path: `./plugins/${dir}` },
		...(entry.policy ? { policy: entry.policy } : {}),
		...(entry.category ? { category: entry.category } : {}),
	})),
});

if (check) {
	if (stale.length) {
		console.error(`✗ generated files are out of date; run node scripts/build.mjs and commit:\n  ${stale.join("\n  ")}`);
		process.exit(1);
	}
	console.log(`✓ ${plugins.length} plugin(s) valid, generated manifests up to date`);
	process.exit(0);
}

// Upload packages: a zip that opens to <skill>/SKILL.md, the layout skill-creator's package_skill.py produces.
const dist = join(root, "dist");
rmSync(dist, { recursive: true, force: true });
mkdirSync(dist);
for (const { dir, skills } of plugins) {
	for (const s of skills) {
		const out = join(dist, `${s}.skill`);
		const r = spawnSync("zip", ["-qrX", out, s, "-x", "*.DS_Store", "*/__pycache__/*"], { cwd: join(root, "plugins", dir, "skills"), stdio: "inherit" });
		if (r.status !== 0) process.exit(r.status ?? 1);
		writeFileSync(join(dist, `${s}.zip`), readFileSync(out));
		console.log(`packaged ${relative(root, out)} and ${s}.zip (${Math.round(statSync(out).size / 1024)} KB)`);
	}
}
