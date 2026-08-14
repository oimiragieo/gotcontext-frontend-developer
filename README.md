# Gotcontext Frontend Developer

Multi-harness UI/UX agent skill pack for Cursor, Claude Code, and GitHub Copilot.

**156** skills under `skills/<name>/SKILL.md`. Sibling products (optional): gotcontext-memory, tensor-grep.

## Install

| Mode | Action |
|------|--------|
| **A. This repo as workspace** | Open the repo in Cursor / Claude Code / VS Code. |
| **B. Into another project** | Copy or symlink `skills/`, `.cursor/skills/`, `.claude/skills/`, and `.github/`. |
| **C. User-global** | Copy full `skills/<name>/` trees into `~/.cursor/skills/` and/or `~/.claude/skills/`. |

| Harness | Path |
|---------|------|
| Cursor | [`.cursor/skills/`](.cursor/skills/) |
| Claude Code | [`.claude/skills/`](.claude/skills/) |
| Copilot | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) · [`.github/instructions/`](.github/instructions/) |
| Canonical | [`skills/`](skills/) |

Harness adapters are thin pointers into `skills/`. Keep both trees together.

## Stitch

Google Stitch MCP + pack skills: start at `stitch-mcp-design` (~**400 credits/day**). Phases: [`skills/STITCH_PHASES.json`](skills/STITCH_PHASES.json). MCP example (no secrets): [`docs/mcp.stitch.example.json`](docs/mcp.stitch.example.json).

Other design paths: Aura clone → `aura-screenshot-clone`; Figma → Figma MCP; Claude Design → `claude-design`.

## Skill router

| Prefix | Reach first |
|--------|-------------|
| craft (no prefix) | `stitch-mcp-design`, `frontend-audit`, `impeccable`, `cinematic-3d-website`, `claude-design`, `aura-screenshot-clone` |
| `mengto-*` | Match visual brief |
| `uupm-*` | `uupm-ui-ux-pro-max` |
| `threejs-*` | Prefer over stale r128 CSV pins |
| `stitch-*` | After `stitch-mcp-design` · [`STITCH_PHASES.json`](skills/STITCH_PHASES.json) |
| `sample-*` / `mkt-*` / `ai-*` | Pattern, CRO, or AI-UX concerns |

Full design-path matrix and intent shortcuts: [AGENTS.md](AGENTS.md) § Skill router.

## License

[LICENSE](LICENSE) · [NOTICE.txt](NOTICE.txt) · [ATTRIBUTION.md](ATTRIBUTION.md) · [LICENSES/](LICENSES/)

## Agent entry

[AGENTS.md](AGENTS.md) · [CLAUDE.md](CLAUDE.md) · `manifest.json` / `provenance.json`

Pack freshness (GSAP / Three.js / Motion CWV): [AGENTS.md](AGENTS.md) § Pack errata.
