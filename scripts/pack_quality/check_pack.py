#!/usr/bin/env python3
"""Pack quality gates for gotcontext-frontend-developer."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
CLAUDE = ROOT / ".claude" / "skills"
CURSOR = ROOT / ".cursor" / "skills"
GH_INSTR = ROOT / ".github" / "instructions"
MANIFEST = ROOT / "manifest.json"
STALE_COPILOT = ROOT / ".github" / "copilot" / "instructions"

# Migration remaps for short upstream / sibling names → in-pack slugs.
# After Task 4, callers should require real dirs only (empty this table).
SKILL_LINK_REMAP: dict[str, str] = {
    "ui-ux-pro-max": "uupm-ui-ux-pro-max",
    "brand": "uupm-brand",
    "design": "uupm-design",
    "design-system": "uupm-design-system",
    "banner-design": "uupm-banner-design",
    "ui-styling": "uupm-ui-styling",
    "extract-static-html": "stitch-extract-static-html",
    "extract-design-md": "stitch-extract-design-md",
    "upload-to-stitch": "stitch-upload-to-stitch",
    "design-md": "stitch-design-md",
    "code-to-design": "stitch-code-to-design",
    "mcp-design": "stitch-mcp-design",
    "manage-design-system": "stitch-manage-design-system",
    "shadcn-ui": "stitch-shadcn-ui",
    "react-components": "stitch-react-components",
    "react-native": "stitch-react-native",
    "remotion": "stitch-remotion",
}

# Skill-shaped markdown links: ../<slug>/… or skills/<slug>/…
REL_LINK_RE = re.compile(
    r"\[[^\]]*\]\("
    r"(?P<href>"
    r"\.\./(?P<rel>[A-Za-z0-9_-]+)/(?:[^)\s]*)?"
    r"|skills/(?P<abs>[A-Za-z0-9_-]+)/(?:[^)\s]*)?"
    r")"
    r"\)"
)
FENCE_RE = re.compile(r"^```", re.MULTILINE)

_failures: list[str] = []


def skill_slugs() -> list[str]:
    return sorted(
        p.parent.name
        for p in SKILLS.glob("*/SKILL.md")
        if p.is_file()
    )


def record(check: str, msg: str) -> None:
    line = f"CHECK {check} FAIL: {msg}"
    print(line)
    _failures.append(line)


def parse_frontmatter(text: str, path: Path, check: str) -> dict | None:
    if yaml is None:
        record(check, "PyYAML required: pip install pyyaml")
        return None
    if not text.startswith("---"):
        record(check, f"missing frontmatter: {path.relative_to(ROOT)}")
        return None
    end = text.find("\n---", 3)
    if end < 0:
        record(check, f"unclosed frontmatter: {path.relative_to(ROOT)}")
        return None
    try:
        data = yaml.safe_load(text[3:end])
    except Exception as e:  # noqa: BLE001
        record(check, f"YAML parse {path.relative_to(ROOT)}: {e}")
        return None
    if not isinstance(data, dict):
        record(check, f"frontmatter not a mapping: {path.relative_to(ROOT)}")
        return None
    return data


def check_yaml_frontmatter() -> None:
    name = "yaml_frontmatter"
    if yaml is None:
        record(name, "PyYAML required: pip install pyyaml")
        return
    for p in SKILLS.glob("*/SKILL.md"):
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---"):
            record(name, f"missing frontmatter: {p.relative_to(ROOT)}")
            continue
        end = text.find("\n---", 3)
        if end < 0:
            record(name, f"unclosed frontmatter: {p.relative_to(ROOT)}")
            continue
        try:
            data = yaml.safe_load(text[3:end])
        except Exception as e:  # noqa: BLE001
            record(name, f"YAML parse {p.relative_to(ROOT)}: {e}")
            continue
        if not isinstance(data, dict) or "name" not in data or "description" not in data:
            record(name, f"name/description required: {p.relative_to(ROOT)}")


def check_no_excerpts() -> None:
    name = "no_excerpts"
    bad: list[str] = []
    for base in (CLAUDE, CURSOR):
        for p in base.glob("*/SKILL.md"):
            text = p.read_text(encoding="utf-8")
            if "## Excerpt" in text:
                bad.append(str(p.relative_to(ROOT)))
    if bad:
        record(name, f"adapter excerpts present ({len(bad)}), e.g. {bad[0]}")


def check_forbidden_paths() -> None:
    name = "forbidden_paths"
    # Path-narrow patterns: real-user-qa/SKILL.md:29 legitimately mentions
    # "chrome-devtools MCP" in prose — only the dead script path is forbidden.
    patterns = [
        re.compile(r"CLAUDE_PLUGIN_ROOT.*/ui-ux-pro-max/"),
        re.compile(r"chrome-devtools/scripts/screenshot\.js"),
        re.compile(r"\.\./extract-static-html/"),
    ]
    bad: list[str] = []
    # rglob ALL text files under skills/ — the dangling refs live in
    # references/ (uupm-design/references/social-photos-design.md) and
    # data/ CSVs too, not just SKILL.md.
    for p in SKILLS.rglob("*"):
        if p.suffix.lower() not in {".md", ".csv", ".json", ".txt"} or not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for pat in patterns:
            if pat.search(text):
                bad.append(f"{p.relative_to(ROOT)} matches {pat.pattern}")
    if bad:
        record(name, "; ".join(bad[:5]) + (f" (+{len(bad) - 5} more)" if len(bad) > 5 else ""))


def check_fence_balance() -> None:
    name = "fence_balance"
    bad: list[str] = []
    for base in (CLAUDE, CURSOR):
        for p in base.glob("*/SKILL.md"):
            text = p.read_text(encoding="utf-8")
            count = len(FENCE_RE.findall(text))
            if count % 2 == 1:
                bad.append(f"{p.relative_to(ROOT)} odd fence count={count}")
            elif count != 0:
                # Pointer-only adapters should have 0 code fences.
                bad.append(f"{p.relative_to(ROOT)} fence count={count} (want 0)")
    if bad:
        record(name, "; ".join(bad[:5]) + (f" (+{len(bad) - 5} more)" if len(bad) > 5 else ""))


def check_manifest_sync() -> None:
    name = "manifest_sync"
    if not MANIFEST.is_file():
        record(name, "manifest.json missing")
        return
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    included = data.get("included") or []
    manifest_slugs = {item["slug"] for item in included if isinstance(item, dict) and "slug" in item}
    disk = set(skill_slugs())
    missing = sorted(disk - manifest_slugs)
    orphan = sorted(manifest_slugs - disk)
    if missing:
        record(name, f"on disk not in manifest: {missing[:8]}")
    if orphan:
        record(name, f"in manifest not on disk: {orphan[:8]}")
    # After Task 3, uupm-core must be absent. Document expected-fail until removal.
    if "uupm-core" in disk or "uupm-core" in manifest_slugs:
        record(name, "uupm-core present (expected until Task 3 removal)")


def check_adapter_sync() -> None:
    name = "adapter_sync"
    missing: list[str] = []
    for slug in skill_slugs():
        claude = CLAUDE / slug / "SKILL.md"
        cursor = CURSOR / slug / "SKILL.md"
        gh = GH_INSTR / f"{slug}.instructions.md"
        if not claude.is_file():
            missing.append(f".claude/skills/{slug}/SKILL.md")
        if not cursor.is_file():
            missing.append(f".cursor/skills/{slug}/SKILL.md")
        if not gh.is_file():
            missing.append(f".github/instructions/{slug}.instructions.md")
    if missing:
        record(name, f"missing adapters ({len(missing)}), e.g. {missing[0]}")


def check_apply_to() -> None:
    name = "apply_to"
    bad: list[str] = []
    if not GH_INSTR.is_dir():
        record(name, ".github/instructions/ missing")
        return
    for p in sorted(GH_INSTR.glob("*.instructions.md")):
        text = p.read_text(encoding="utf-8")
        data = parse_frontmatter(text, p, name)
        if data is None:
            continue
        if "applyTo" not in data:
            bad.append(str(p.relative_to(ROOT)))
    if bad:
        record(name, f"missing applyTo ({len(bad)}), e.g. {bad[0]}")


def check_adapter_descriptions() -> None:
    name = "adapter_descriptions"
    if yaml is None:
        record(name, "PyYAML required: pip install pyyaml")
        return
    bad: list[str] = []
    for slug in skill_slugs():
        canonical = SKILLS / slug / "SKILL.md"
        canon_text = canonical.read_text(encoding="utf-8")
        if not canon_text.startswith("---"):
            continue
        end = canon_text.find("\n---", 3)
        if end < 0:
            continue
        try:
            canon_data = yaml.safe_load(canon_text[3:end])
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(canon_data, dict) or "description" not in canon_data:
            continue
        expected = canon_data["description"]
        for base, label in ((CLAUDE, ".claude"), (CURSOR, ".cursor")):
            adapter = base / slug / "SKILL.md"
            if not adapter.is_file():
                continue
            text = adapter.read_text(encoding="utf-8")
            data = parse_frontmatter(text, adapter, name)
            if data is None:
                continue
            got = data.get("description")
            if got != expected:
                bad.append(f"{label}/skills/{slug}/SKILL.md")
    if bad:
        record(
            name,
            f"description mismatch ({len(bad)}), e.g. {bad[0]}",
        )


def _resolve_skill_slug(slug: str) -> Path | None:
    target = SKILLS / slug
    if target.is_dir() and (target / "SKILL.md").is_file():
        return target
    remapped = SKILL_LINK_REMAP.get(slug)
    if remapped:
        mapped = SKILLS / remapped
        if mapped.is_dir() and (mapped / "SKILL.md").is_file():
            return mapped
    return None


def check_relative_skill_links() -> None:
    name = "relative_skill_links"
    bad: list[str] = []
    for p in SKILLS.rglob("*.md"):
        if not p.is_file():
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in REL_LINK_RE.finditer(text):
            slug = m.group("rel") or m.group("abs")
            href = m.group("href")
            if slug is None:
                continue
            # In-skill relative paths (e.g. resources/../examples/) that exist on disk
            # are not skill-to-skill links — skip them.
            if m.group("rel") is not None:
                local = (p.parent / ".." / slug).resolve()
                try:
                    local.relative_to(SKILLS.resolve())
                except ValueError:
                    local = None  # type: ignore[assignment]
                if local is not None and local.exists():
                    continue
            if _resolve_skill_slug(slug) is None:
                bad.append(f"{p.relative_to(ROOT)} -> {href}")
    if bad:
        record(name, "; ".join(bad[:5]) + (f" (+{len(bad) - 5} more)" if len(bad) > 5 else ""))


def check_no_stale_copilot_tree() -> None:
    name = "no_stale_copilot_tree"
    if STALE_COPILOT.exists():
        record(name, f"{STALE_COPILOT.relative_to(ROOT)} exists (delete; keep README index only)")


def main() -> None:
    global _failures
    _failures = []
    check_yaml_frontmatter()
    check_no_excerpts()
    check_forbidden_paths()
    check_fence_balance()
    check_manifest_sync()
    check_adapter_sync()
    check_apply_to()
    check_adapter_descriptions()
    check_relative_skill_links()
    check_no_stale_copilot_tree()
    if _failures:
        print(f"FAILED: {len(_failures)} check(s)", file=sys.stderr)
        raise SystemExit(1)
    print("OK: pack quality checks passed")


if __name__ == "__main__":
    main()
