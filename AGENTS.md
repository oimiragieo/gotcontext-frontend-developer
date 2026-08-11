# Gotcontext Frontend Developer — AGENTS

## Rules

1. Load canonical `skills/<slug>/SKILL.md`, not adapter excerpts alone.
2. Do not casually rewrite upstream skill bodies.
3. Respect [ATTRIBUTION.md](ATTRIBUTION.md) and [LICENSES/](LICENSES/).
4. Sibling products (memory, tensor-grep) are optional pointers only.

## Stitch

Start with **`stitch-mcp-design`** (~400 credits/day). Then phase skills in
[`skills/STITCH_PHASES.json`](skills/STITCH_PHASES.json). Do not use Stitch
generate tools for Aura URL-clones or Figma-SoT work.

Same slugs exist under `.cursor/skills/`, `.claude/skills/`, and
`.github/instructions/`.

## Skill router

| Prefix | Purpose | When to reach first |
|--------|---------|---------------------|
| *(none)* craft | Flagship flows | `stitch-mcp-design`, `frontend-audit`, `impeccable`, `cinematic-3d-website`, `claude-design`, `aura-screenshot-clone` |
| `mengto-*` | Style/motion/layout presets (majority of pack) | Match visual brief; see intent shortcuts |
| `uupm-*` | Design intelligence / brand / slides | `uupm-ui-ux-pro-max` for search-driven systems |
| `threejs-*` | Three.js teaching modules | Prefer over stale r128 pins in older CSV rows |
| `stitch-*` | Stitch MCP phases | After `stitch-mcp-design`; see `skills/STITCH_PHASES.json` |
| `sample-*` | Pattern libraries (a11y, DS, interaction) | When implementing those concerns |
| `mkt-*` | Marketing/CRO copy surfaces | Paywalls, signup, popups, etc. |
| `ai-*` | AI product UX archetypes | Governors / trust / wayfinders |

### Design path matrix

| Situation | Path |
|-----------|------|
| Greenfield UI via Google Stitch MCP | `stitch-mcp-design` (~400 credits/day) |
| Clone from live URL screenshots | `aura-screenshot-clone` (no Pro → Phase 2.5 rebuild) |
| Figma is source of truth | Figma MCP (`figma:figma-design-to-code`) — not Stitch generate |
| Claude Design adaptation | `claude-design` / `claude-design-adaptation` |

Do **not** use Stitch generate tools for Aura URL-clones or Figma-SoT work.

### Intent shortcuts

| User ask | Start skill |
|----------|-------------|
| Landing page | `mengto-landing-page` |
| Awwwards-level motion site | `mengto-build-awwwards-quality-sites` |
| Frontend/UI audit | `frontend-audit` |
| Design system from brief | `uupm-ui-ux-pro-max` |
| Cinematic 3D brand experience | `cinematic-3d-website` |
