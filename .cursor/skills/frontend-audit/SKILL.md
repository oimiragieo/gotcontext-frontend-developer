---
name: frontend-audit
description: Adapter pointer to canonical skills/frontend-audit for Cursor
---

# frontend-audit (Cursor adapter)

Canonical skill: [`../../../skills/frontend-audit/SKILL.md`](../../../skills/frontend-audit/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: frontend-audit
description: "Use when the user asks to audit, review, critique, or \"make sure it looks right\" on a deployed web page, component, or Figma mockup — or when they mention visual issues, CRO, conversion rate, design consistency, accessibility, \"feels off\", \"looks bad\", \"make it pop\", \"looks like AI slop\". Triggers on keywords like \"audit the page\", \"review the design\", \"what's wrong with this UI\", \"CRO audit\", \"a11y check\", \"visual hierarchy\", \"typography check\", \"does this look right\". Activation also recommended after any significant frontend change on gotcontext.ai before calling the work done."
---

# Frontend Audit Skill

Run a systematic, opinionated audit of a web page or component before calling frontend work done. Produces a scored report and hands off to **aura-screenshot-clone** when fixes need to be pulled from reference sites.

This skill operationalises the research consensus from 2026 design-audit frameworks (Apexure, ConvertCart, Red Rattler, Nielsen Norman, WCAG 2.2). It runs in ~10 minutes per page and produces a prioritised punch list, not a wall of findings.

## When to use

Invoke when:
- User says "audit", "review", "check", "make sure it looks right", "critique this page"
- User mentions visual issues: "feels off", "looks bad", "looks like mad science", "cluttered", "looks like AI slop"
- User mentions CRO, conversion, accessibility, a11y, WCAG, mobile, visual hierarchy, typography, spacing, whitespace
- **Proactively** after shipping any frontend change on gotcontext.ai. A one-pass audit on the live URL before saying "done" catches issues that CI can't.

## When NOT to use

- Pure code review (logic, state, security) — that's `code-review` / `pr-review-toolkit:code-reviewer`.
- Designing from scratch with no reference — use `frontend-design:frontend-design` or `brainstorming`.
- Cloning a reference pattern — use **aura-screenshot-clone** directly. This skill hands off TO that one when fixes are needed.

## Inputs (pick one)

1. **Live URL** — preferred. Use `mcp__claude-in-chrome__navigate` + `computer action=screenshot` at 1440×900 desktop + 375×812 mobile.
2. **Local dev server** — `npm run dev` then navigate the browser to `http://localhost:3000/...`.
3. **Screenshot(s) attached by user** — skip the browser phase, go directly to the scoring.
```
