#!/usr/bin/env python3
"""Check a skill folder the way skill-creator's quick_validate.py does, plus every relative Markdown link.

Usage: scripts/validate.py skills/mindbody
"""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ALLOWED = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def main(root):
    root = Path(root)
    errors = []
    skill_mds = list(root.rglob("SKILL.md"))
    if skill_mds != [root / "SKILL.md"]:
        errors.append(f"expected exactly one SKILL.md at the root, found {[str(p) for p in skill_mds]}")
    fm = frontmatter((root / "SKILL.md").read_text()) if (root / "SKILL.md").exists() else None
    if fm is None:
        errors.append("SKILL.md has no YAML frontmatter")
    else:
        extra = set(fm) - ALLOWED
        if extra:
            errors.append(f"unexpected frontmatter keys: {sorted(extra)}")
        name, desc = fm.get("name", ""), fm.get("description", "")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"name must be kebab-case, at most 64 characters: {name!r}")
        if name != root.name:
            errors.append(f"name {name!r} must match the folder name {root.name!r}")
        if not desc or len(desc) > 1024 or "<" in desc or ">" in desc:
            errors.append(f"description must be 1-1024 characters with no angle brackets (has {len(desc)})")

    link = re.compile(r"\]\(([^)\s]+)\)")
    broken = 0
    for md in root.rglob("*.md"):
        for target in link.findall(md.read_text()):
            if re.match(r"^[a-z]+:|^#", target):
                continue
            path = unquote(target.split("#", 1)[0])
            if path and not (md.parent / path).exists():
                broken += 1
                if broken <= 20:
                    errors.append(f"broken link in {md.relative_to(root)}: {target}")
    if broken > 20:
        errors.append(f"... and {broken - 20} more broken links")

    files = sum(1 for p in root.rglob("*") if p.is_file())
    if errors:
        print("\n".join("✗ " + e for e in errors))
        sys.exit(1)
    print(f"✓ {root}: valid ({files} files, name={fm['name']}, description {len(fm['description'])} chars, links ok)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "skills/mindbody")
