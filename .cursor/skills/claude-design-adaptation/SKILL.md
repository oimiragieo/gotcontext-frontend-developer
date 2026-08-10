---
name: claude-design-adaptation
description: Adapter pointer to canonical skills/claude-design-adaptation for Cursor
---

# claude-design-adaptation (Cursor adapter)

Canonical skill: [`../../../skills/claude-design-adaptation/SKILL.md`](../../../skills/claude-design-adaptation/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: claude-design-adaptation
description: Use AFTER a Claude-Design export exists and BEFORE the render-verify step — the discipline for adapting an export into a production page with real data, honest empty states, and existing tokens/components (never shipping mock numbers).
---

# Claude-Design Adaptation

## When to use
- After receiving a Claude-Design export zip and before writing any production JSX.
- When a design audit finds mock data, invented metrics, or inline-styled clone components in a shipped page.
- NOT during the design generation phase — invoke `claude-design` first to produce the export, then this skill to adapt it.
- Pairs with `claude-design` (produces the export this skill adapts). (Prior refs to `gc-brand-voice`/`ui-rater`/`web-creation-checklist` were dead — removed 2026-07-14.)

## P1: Study the zip before touching code

Open `manifest.json`, `tokens/`, and `design.html` before writing a line. Identify:
- Token names that collide with or duplicate `aura.css var(--*)` — map them, don't add new variables.
- Existing components in `apps/web/src/components/` that cover the same pattern under a different name.
- Which sections belong on the EXISTING route vs an implied new route that doesn't exist yet.

Adapt the layout concepts. Never copy the JSX.

## P2: Never ship export numbers

Grep the export for fake-data tells before wiring any data: `John Doe`, `Lorem ipsum`, `example.com`, round-thousands (`1,000+`, `10,347`), fabricated testimonials, invented logo clouds. Every visible number in production must map to a real DB query or be omitted. If the backend doesn't emit a metric, the UI doesn't show it. If the value is zero for a new user, show the zero state — not the mock.

## P3: Design honest empty states

The export shows the happy path with N items. Production users see the empty path first. Before merging, implement all four variants:
- **New user** — zero data, onboarding CTA
```
