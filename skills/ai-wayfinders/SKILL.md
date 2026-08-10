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
   are fine; ones that imply cloud spend should be honest about cost class.
4. **No dark-pattern engagement** — no fake urgency, no manipulative randomize
   for retention. Randomize only to reduce blank-slate pressure.

## Seam → pattern map

| Surface | Prefer | Avoid |
|---|---|---|
| Console Chat empty | Initial CTA + Suggestions (3–5) + honest cannot-do | Endless gallery of unproven capabilities |
| Console Voice first start | Nudge for mic permission + gate mode explain | Auto-start voice without consent |
| `⌘K` / command palette | Templates for frequent owner tasks | Duplicating every nav link |
| Telegram | Rare contextual follow-ups only | Prompt galleries in-chat |
| After a tool/run completes | Follow-ups tied to *this* result | Generic "ask me anything" |
| Capability / SOUL text | Prompt Details (show constraints) | Inflated marketing bullets |

## Eight patterns (short)

1. **Initial CTA** — scaffolded composer, not a naked box.
2. **Example Gallery** — curated, actionable, prompt-visible; console-only.
3. **Suggestions** — 3–6 chips; prefer contextual over static.
4. **Templates** — madlibs for repeatable owner jobs (status, dream review).
5. **Nudges** — one tip at the moment of need (e.g. first mic deny).
6. **Follow-ups** — after a result, not during typing.
7. **Prompt Details** — show constraints/mode so power users learn the system.
8. **Randomize** — optional shuffle of safe examples; never engagement bait.

## Capability-honesty checklist

Before adding any suggestion/chip/template:

- [ ] Mechanism exists on the live flag set (both ON and OFF copy if flag-gated).
- [ ] Medium is correct (voice tip is spoken-safe).
- [ ] Cost class is acceptable as a default click (or labeled).
- [ ] Failure copy does not claim a dead camera vs. a gate miss identically
      without distinction where the product can tell them apart.

## Output format

1. **Blank-slate moment** — which surface.
2. **Patterns** — 1–3.
3. **Exact copy candidates** — chips/templates that pass the honesty checklist.
4. **Measure** — what observe-first or dogfood will verify.

## Cross-references

- `ui-fix-observe-first` — measure console UI before declaring discoverability fixed.
- `channel-adapter-pattern` — voice vs text delivery.
- `ai-trust-builders` — disclosure beside onboarding.
- `ai-governors` — don't replace confirms with friendly chips.
- `segment-a-turn-before-classifying-intent` — voice aggregation vs request.
