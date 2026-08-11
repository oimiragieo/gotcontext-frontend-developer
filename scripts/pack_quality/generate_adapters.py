#!/usr/bin/env python3
"""Generate pointer-only harness adapters from skills/ inventory."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"


def skill_slugs() -> list[str]:
    return sorted(p.parent.name for p in SKILLS.glob("*/SKILL.md"))


def canonical_description(slug: str) -> str:
    """Read the canonical skill's frontmatter description (routing depends on it)."""
    text = (SKILLS / slug / "SKILL.md").read_text(encoding="utf-8")
    end = text.find("\n---", 3)
    fm = text[3:end]
    try:
        data = yaml.safe_load(fm)
        if isinstance(data, dict) and data.get("description") is not None:
            return str(data["description"]).strip()
    except yaml.YAMLError:
        # Canonical may ship unquoted ": " in description (e.g. cinematic-3d-website).
        # Adapter still needs the verbatim scalar; Task 4 may fix canonical YAML later.
        pass
    for line in fm.splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    raise KeyError(f"description missing: {slug}")


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def adapter(slug: str, harness: str) -> str:
    # json.dumps gives a YAML-safe double-quoted scalar — several canonical
    # descriptions contain ": " (e.g. cinematic-3d-website), which is what
    # broke strict YAML parsing in the first place. Never emit it unquoted.
    desc = json.dumps(canonical_description(slug))
    return (
        f"---\n"
        f"name: {slug}\n"
        f"description: {desc}\n"
        f"---\n\n"
        f"# {slug} ({harness} adapter)\n\n"
        f"Canonical skill: [`../../../skills/{slug}/SKILL.md`](../../../skills/{slug}/SKILL.md)\n\n"
        f"Load and follow the canonical SKILL.md (and sibling refs/scripts there).\n"
    )


def github_instructions(slug: str) -> str:
    # Broad applyTo so Copilot can attach pack guidance; tune later if noisy.
    desc = json.dumps(canonical_description(slug))
    return (
        f"---\n"
        f"description: {desc}\n"
        f"applyTo: \"**/*\"\n"
        f"---\n\n"
        f"# {slug}\n\n"
        f"Apply the canonical skill: "
        f"[`../../skills/{slug}/SKILL.md`](../../skills/{slug}/SKILL.md)\n"
    )


def main() -> None:
    slugs = skill_slugs()
    for slug in slugs:
        write(ROOT / ".claude" / "skills" / slug / "SKILL.md", adapter(slug, "Claude Code"))
        write(ROOT / ".cursor" / "skills" / slug / "SKILL.md", adapter(slug, "Cursor"))
        write(
            ROOT / ".github" / "instructions" / f"{slug}.instructions.md",
            github_instructions(slug),
        )
    print(f"generated adapters for {len(slugs)} skills")


if __name__ == "__main__":
    main()
