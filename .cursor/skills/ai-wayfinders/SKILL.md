---
name: ai-wayfinders
description: Adapter pointer to canonical skills/ai-wayfinders for Cursor
---

# ai-wayfinders (Cursor adapter)

Canonical skill: [`../../../skills/ai-wayfinders/SKILL.md`](../../../skills/ai-wayfinders/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: ai-wayfinders
description: "Use when designing JARVIS/console first-run or blank-slate UX — Chat empty state, example prompts, capability discovery, templates, nudges, or follow-ups. Trigger on 'users don't know what to ask', onboarding, suggestion chips, or discoverability — especially omega-console Chat/Voice."
---

# AI Wayfinders — JARVIS discoverability UX

Wayfinders reduce blank-slate anxiety and teach **what JARVIS can actually do**
without lying. Primary home: **omega-console** Chat/Voice and Settings. Telegram
and phone need lighter forms (no gallery clutter on a lifeline channel).

Pattern catalog: [references/patterns.md](references/patterns.md).
Adapted from tommyjepsen/awesome-ux-skills `ai-wayfinders`.

## When to use

- Console Chat empty state, composer placeholders, suggestion chips, command
  palette (`⌘K`), capability help, first voice session.
- Fixing "I didn't know it could X" or "it claimed Y and can't".
- **Not** for: visual craft polish (`ui-fix-observe-first`), HITL confirms
  (`ai-governors`), or privacy disclosure (`ai-trust-builders`).

## JARVIS constraints (non-negotiable)

1. **Wayfinders must track the capability manifest and flags.** A chip that
   offers webcam-on-demand when the reflex still intercepts is a false
   capability line — a product bug, not a nice-to-have.
2. **Voice/spoken** — few short suggestions; no markdown galleries; channel
   adapter (`channel-adapter-pattern`) owns delivery shape.
3. **Deterministic lanes** — suggestions that always hit `deterministic_override`
```
