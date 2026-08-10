# TOOLING appendix (not routable design skills)

Thinktank (2026-08-08): browser MCP helpers stay **out of** `skills/` routing.

## Browser / observation dependencies

- `use-claude-in-chrome` — authenticated Chrome via claude-in-chrome MCP
- `use-chrome-devtools-mcp` — CDP / a11y-tree driven Chrome

Install those from the internal Claude skills library when running
`ui-fix-observe-first`, `frontend-audit`, or `real-user-qa`.

## Unresolved cross-references in imported AI trio

The JARVIS-adapted `ai-governors` / `ai-trust-builders` / `ai-wayfinders`
skills may mention sibling internal skills such as
`gate-untrusted-content-into-prompts` or n8n HITL helpers.
Those are **not** bundled in this portable pack; treat mentions as
optional ecosystem links, not pack dependencies.
