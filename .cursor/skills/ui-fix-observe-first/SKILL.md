---
name: ui-fix-observe-first
description: Adapter pointer to canonical skills/ui-fix-observe-first for Cursor
---

# ui-fix-observe-first (Cursor adapter)

Canonical skill: [`../../../skills/ui-fix-observe-first/SKILL.md`](../../../skills/ui-fix-observe-first/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: ui-fix-observe-first
description: >-
  Use when fixing, auditing, improving, or building any web UI — before reading
  or editing component code. Fires on contrast/a11y/overflow/responsive/hover-
  focus/layout complaints, polish, audit, or any visual change. Never diagnose a
  UI defect from code alone: render at real viewports, measure (axe / contrast /
  a11y tree / console / keyboard / reflow), then cite the measurement.
---

# UI fix — observe first

## Rules

1. **Never diagnose a UI change from code alone — render, measure, cite.**
   Runtime defects (contrast, overflow, wrap, responsive, hover/focus, layout
   shift, stacking) do not exist in the JSX. No measurement = not a finding.
2. **Fix correctness directly; settle taste with evidence.** Prefer competitive
   pattern research (Vercel / Linear / Stripe and similar) over asking the user
   to invent aesthetic direction mid-fix.

## Flow A — fix / improve an existing UI

1. **RENDER** the live page at the layout’s target widths (typically **375 + 1440**).
   Public pages → browser / DevTools MCP. Authed apps → a session that can see
   the real UI (logged-in browser automation when needed).
2. **OBSERVE** with layered tools (automation alone misses a large share of issues;
   Lighthouse is a floor, not conformance):
   - **axe-core** for contrast, labels, ARIA, duplicate IDs.
   - **Computed-style WCAG contrast** when axe cannot run (AA normal ≥4.5,
```
