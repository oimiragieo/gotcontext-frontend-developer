---
name: ai-wayfinders
description: Adapter pointer to canonical skills/ai-wayfinders for Claude Code
---

# ai-wayfinders (Claude Code adapter)

Canonical skill: [`../../../skills/ai-wayfinders/SKILL.md`](../../../skills/ai-wayfinders/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: ai-wayfinders
description: >-
  Use when designing AI product first-run or blank-slate UX — chat empty state,
  example prompts, capability discovery, templates, nudges, or follow-ups.
  Trigger on "users don't know what to ask", onboarding, suggestion chips, or
  discoverability.
---

# AI Wayfinders — discoverability UX

Wayfinders reduce blank-slate anxiety and teach **what the product can actually
do** without over-claiming.

Pattern catalog: [references/patterns.md](references/patterns.md).
Adapted from tommyjepsen/awesome-ux-skills `ai-wayfinders`.

## When to use

- Chat empty state, composer placeholders, suggestion chips, command palette,
  capability help, first voice session.
- Fixing "I didn't know it could X" or "it claimed Y and can't".
- **Not** for: visual craft (`ui-fix-observe-first`), HITL confirms
  (`ai-governors`), or privacy disclosure (`ai-trust-builders`).

## Constraints

1. **Wayfinders must track real capabilities and flags.** A chip that offers a
   blocked or missing feature is a product bug.
2. **Voice / spoken** — few short suggestions; no dense galleries.
```
