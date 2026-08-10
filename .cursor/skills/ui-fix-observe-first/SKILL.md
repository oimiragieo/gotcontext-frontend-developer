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
description: "Use when fixing, auditing, improving, or building ANY web UI — before reading or editing component code. Fires on contrast/a11y/overflow/responsive/hover-focus/layout complaints, \"polish the UI\", \"audit the page/site\", \"make it premium\", or any visual change (esp. omega-console at :8099). Rule 1: never diagnose a UI defect from code — render at 375+1440, measure with axe-core / computed-style WCAG contrast / a11y tree / console errors / keyboard pass / reflow at 320px+200% zoom, then cite the measurement; \"it compiles\" is not a finding. Rule 2: correctness is yours to fix directly on design tokens; aesthetic/taste direction goes through Exa + the thinktank council, not the CEO."
---

# UI fix — observe first

## The two rules (non-negotiable)
1. **Never diagnose or claim a UI change from code — render, measure, cite.** Runtime defects (contrast, overflow, wrap, responsive, hover/focus, layout shift, stacking) do NOT exist in the JSX. No measurement = not a finding. "It compiles" / "the JSX looks right" is not an observation.
2. **Correctness is yours to fix; taste is decided by evidence + council, not by asking the CEO.** Aesthetic direction goes through Exa + the thinktank; you bring the CEO the *result*, not the question.

## FLOW A — fix / improve an existing UI
0. Prompt fires the ui-observe-first hook → render before you read code.
1. **RENDER** the live page at **375 + 1440**. Public page → chrome-devtools MCP. **Authed dashboard (omega-console) → claude-in-chrome** with a live session.
2. **OBSERVE quantitatively — layered, not one tool** (Exa 2026: automation catches ~57% of issues; Lighthouse is a *floor*, not conformance):
   - **axe-core** (the engine — Deque, "zero false positives", what Lighthouse wraps a subset of). On a live claude-in-chrome page, inject + run it: `javascript_tool` → load `https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.x/axe.min.js` then `await axe.run()`. Catches contrast, missing labels, ARIA validity, duplicate IDs. Public page: use chrome-devtools Lighthouse + `performance_start_trace` (LCP/INP/CLS).
   - **computed-style WCAG contrast** (fallback / precise pin): `javascript_tool` computes the ratio of an element's `color` vs its effective bg (AA normal ≥4.5, large/UI ≥3.0). Use when axe can't be injected.
   - **a11y tree** (`read_page`) + **console errors** (`read_console`) + a full-page screenshot.
   - **Keyboard pass** (highest-leverage manual step, ~30% of automated-missed issues): Tab from the top — focus visible at all times? logical order? no traps? sticky nav doesn't steal focus (WCAG 2.2 focus-not-obscured)?
   - **Reflow**: check 320px width / 200% zoom for overflow. **24px tap targets** (WCAG 2.2).
2.5 **RATE THE WHOLE PAGE, NOT JUST YOUR WIDGET — + the SIBLING-PARITY question.** Green per-widget
   numbers (contrast/tap-target/aria all AA) do NOT mean the surface is done. Before declaring a
   control fixed, ask: **"what does the nearest SIBLING control offer that mine doesn't?"** Live
   receipt: a console camera toggle passed every per-widget axe/contrast check but had NO device
   picker while the sibling mic control did — a whole-page parity gap invisible to per-widget
   measurement. Also judge the control ACROSS interaction/navigation, not just at rest: (a) fail-soft
   reverts must surface **PROMINENTLY** (a `role="alert"`, not whispered status text — a silent
   auto-revert reads as a haunted UI); (b) opt-in state must be **session-scoped**, not reset on
   every SPA-nav remount ("it turned itself off"); (c) labels must not wrap mid-word at the real
   column width. (memory: `feedback_verify_the_page_not_your_widget`)
```
