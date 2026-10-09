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
import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, statSync, writeFileSync } from "node:fs";
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
// claude.ai's Save skill refuses a zip of more than 200 entries, so folders the config lists under package.bundle
// are merged into one Markdown file each (staged in dist/.stage; the plugin keeps its folders).
const MAX_ENTRIES = 200;
const dist = join(root, "dist");
const stage = join(dist, ".stage");
rmSync(dist, { recursive: true, force: true });
mkdirSync(stage, { recursive: true });
for (const { dir, entry, skills } of plugins) {
	for (const s of skills) {
		cpSync(join(root, "plugins", dir, "skills", s), join(stage, s), { recursive: true });
		// package.vendor: { "<skill>": { "<path in package>": "<path relative to the skill>" } } copies files a
		// standalone upload needs from elsewhere in the plugin (e.g. a sibling skill's runtime)
		for (const [to, from] of Object.entries(entry.package?.vendor?.[s] ?? {})) {
			cpSync(join(root, "plugins", dir, "skills", s, from), join(stage, s, to), { recursive: true, filter: (p) => !p.endsWith(".pyc") && !p.includes("__pycache__") });
		}
		bundle(join(stage, s), entry.package?.bundle ?? []);
		const entries = walk(join(stage, s)).length + 1;
		if (entries > MAX_ENTRIES) {
			console.error(`✗ ${s}: ${entries} zip entries, over claude.ai's ${MAX_ENTRIES}; add its biggest folders to package.bundle in marketplace.config.json`);
			process.exit(1);
		}
		const out = join(dist, `${s}.skill`);
		const r = spawnSync("zip", ["-qrX", out, s, "-x", "*.DS_Store", "*/__pycache__/*", "*/.venv/*"], { cwd: stage, stdio: "inherit" });
		if (r.status !== 0) process.exit(r.status ?? 1);
		writeFileSync(join(dist, `${s}.zip`), readFileSync(out));
		console.log(`packaged ${relative(root, out)} and ${s}.zip (${entries} entries, ${Math.round(statSync(out).size / 1024)} KB)`);
	}
}
rmSync(stage, { recursive: true, force: true });

/** Every file and folder under dir, as absolute paths. */
function walk(dir) {
	return readdirSync(dir, { withFileTypes: true }).flatMap((d) => {
		const p = join(dir, d.name);
		return d.isDirectory() ? [p, ...walk(p)] : [p];
	});
}

/**
 * Merge each folder matching the globs ("articles/*": every folder in articles/) into <folder>.md: its index.md
 * first, then each page under an anchor named after its file. Relative links anywhere in the skill that pointed into
 * a merged folder are rewritten to <folder>.md#<page>.
 */
function bundle(skillDir, globs) {
	const folders = globs.flatMap((g) => {
		if (!g.endsWith("/*")) return [join(skillDir, g)];
		const base = join(skillDir, g.slice(0, -2));
		return existsSync(base) ? readdirSync(base, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => join(base, d.name)) : [];
	});
	if (!folders.length) return;
	const moved = new Map(); // old absolute path of a page → [new file, anchor or ""]
	for (const f of folders) {
		for (const p of readdirSync(f)) {
			if (!p.endsWith(".md") || statSync(join(f, p)).isDirectory()) throw new Error(`${relative(skillDir, f)}/${p}: only Markdown pages can be bundled`);
			moved.set(join(f, p), [`${f}.md`, p === "index.md" ? "" : p.slice(0, -3)]);
		}
	}
	const linkTo = (fromFile, target) => relative(dirname(fromFile), target);
	const rewrite = (text, oldFile, newFile) =>
		text.replace(/\]\(([^)\s#]+\.md)(#[^)\s]*)?\)/g, (m, href, frag) => {
			if (/^[a-z]+:/i.test(href)) return m;
			const hit = moved.get(resolve(dirname(oldFile), href));
			if (hit) return `](${linkTo(newFile, hit[0])}${hit[1] ? `#${hit[1]}` : frag ?? ""})`;
			if (oldFile === newFile) return m;
			return `](${linkTo(newFile, resolve(dirname(oldFile), href))}${frag ?? ""})`;
		});
	// Files that stay put: rewrite links into the merged folders.
	for (const p of walk(skillDir)) {
		if (!p.endsWith(".md") || moved.has(p) || statSync(p).isDirectory()) continue;
		const text = readFileSync(p, "utf8");
		const next = rewrite(text, p, p);
		if (next !== text) writeFileSync(p, next);
	}
	// The merged folders: each page's front matter becomes a source line under its anchor.
	for (const f of folders) {
		const pages = readdirSync(f).sort((a, b) => (a === "index.md" ? -1 : b === "index.md" ? 1 : a.localeCompare(b)));
		const out = `${f}.md`;
		const parts = pages.map((p) => {
			const old = join(f, p);
			let text = rewrite(readFileSync(old, "utf8"), old, out);
			const fm = text.match(/^---\n([\s\S]*?)\n---\n/);
			if (fm) {
				const field = (k) => fm[1].match(new RegExp(`^${k}:\\s*(.+)$`, "m"))?.[1].trim();
				text = text.slice(fm[0].length);
				const src = field("source");
				if (src) text = text.replace(/^(# .*\n)/, `$1\nSource: ${src}${field("source_updated") ? ` (updated ${field("source_updated")})` : ""}\n`);
			}
			return p === "index.md" ? text.trim() : `<a id="${p.slice(0, -3)}"></a>\n\n${text.trim()}`;
		});
		const note = `<!-- Bundled from ${relative(skillDir, f)}/ (${pages.length} pages) so the upload stays under ${MAX_ENTRIES} files. Each page starts at an <a id> anchor named after its original file. -->`;
		writeFileSync(out, `${note}\n\n${parts.join("\n\n---\n\n")}\n`);
		rmSync(f, { recursive: true });
	}
}
