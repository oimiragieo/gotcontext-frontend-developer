# Gotcontext Frontend Developer

Gotcontext **multi-harness** frontend craft skill pack — so agents can ship
non-slop, enterprise-grade UI/UX (product-design bar, not generic AI layout).

**~141** canonical skills · Cursor + Claude Code + GitHub Copilot adapters.

Sibling products (pointer only — not required): **gotcontext-memory**, **tensor-grep**.

## Install

| Mode | What to do |
|------|------------|
| **A. Open this repo as the workspace** | Clone and open in Cursor / Claude Code / VS Code. Harness trees are already at `.cursor/skills/`, `.claude/skills/`, `.github/`. |
| **B. Use on another site repo** | Copy (or symlink) `skills/`, `.cursor/skills/`, `.claude/skills/`, and `.github/` into that project — thin adapters need sibling `skills/`. |
| **C. User-global** | Copy full skill directories into `~/.cursor/skills/` and/or `~/.claude/skills/` (prefer full `skills/<name>/` trees, not adapters alone). |

| Harness | Path |
|---------|------|
| **Cursor** | [`.cursor/skills/`](.cursor/skills/) |
| **Claude Code** | [`.claude/skills/`](.claude/skills/) |
| **GitHub Copilot** | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) + [`.github/instructions/`](.github/instructions/) |
| **Canonical bodies** | [`skills/<name>/SKILL.md`](skills/) |

### Thin-adapter caveat

Project harness entries are **pointers + excerpts** into `skills/`. Opening only
`.cursor/skills` without `skills/` breaks relative links. Official Agent Skills
shape is still `…/skills/<name>/SKILL.md` under the harness root.

## Support matrix

| Surface | Status |
|---------|--------|
| Cursor project skills (`.cursor/skills`) | Supported |
| Claude Code project skills (`.claude/skills`) | Supported |
| Copilot repo instructions | Supported |
| Marketplace / gotcontext.com plugin listing | **Not claimed** (future) |
| Auto-inject into unrelated repos | **No** — use install modes above |

## License

See [LICENSE](LICENSE), [NOTICE.txt](NOTICE.txt), [ATTRIBUTION.md](ATTRIBUTION.md),
and [LICENSES/](LICENSES/).

## Pack meta

| Doc | Purpose |
|-----|---------|
| [AGENTS.md](AGENTS.md) | Agent entry rules |
| [CLAUDE.md](CLAUDE.md) | Claude Code contract |
| [SELECTION.md](SELECTION.md) | Include/exclude ledger |
| [ATTRIBUTION.md](ATTRIBUTION.md) | Upstream credit + SPDX |
| [VERIFICATION.md](VERIFICATION.md) | Verify notes |
| [manifest.json](manifest.json) / [provenance.json](provenance.json) | Machine ledgers |
| [CUTOVER.json](CUTOVER.json) | Factory → product cutover receipt |

## Source of truth

This repository is the **installable product**. The private factory workspace that
assembled the first cut is not published and may be retired later.
