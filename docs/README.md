# Docs

- [README.md](../README.md) — install, support surface, short skill router
- [AGENTS.md](../AGENTS.md) — agent rules · skill router · design-path matrix
- [ATTRIBUTION.md](../ATTRIBUTION.md) — licenses
- [mcp.stitch.example.json](mcp.stitch.example.json) — Stitch MCP template (no secrets)

`docs/superpowers/` is **local-only** SDD scratch (plans, briefs, reports). Omit it from release PRs; do not stage or commit it on merge tips.

## Stitch MCP setup

1. Get an API key from **Google Stitch / AI Studio settings** (see Google AI Studio / Stitch project settings — no secrets in this repo).
2. Copy `mcp.stitch.example.json` and replace `REPLACE_WITH_STITCH_API_KEY_FROM_SETTINGS` with your key in a private MCP config (never commit the real key).
3. **Claude Code:** register the same Stitch MCP server via Claude Code MCP config pointing at the same URL/headers shape as the example.
4. **Cursor / other hosts:** add an equivalent MCP server entry using the same remote URL and `X-Goog-Api-Key` header.
