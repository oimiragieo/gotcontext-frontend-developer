---
name: ai-governors
description: Adapter pointer to canonical skills/ai-governors for Cursor
---

# ai-governors (Cursor adapter)

Canonical skill: [`../../../skills/ai-governors/SKILL.md`](../../../skills/ai-governors/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: ai-governors
description: >-
  Use when designing or auditing AI product human-in-the-loop — write approval,
  proposal accept/reject, action confirm, spend caps, run detail, memory
  capture, or any AI action with irreversible blast radius. Trigger on
  confirmation UX, undo, cost-before-act, show-the-plan, citations, or keeping
  the owner in control.
---

# AI Governors — HITL product UX

Governors are **product patterns** that keep the owner in control while the
agent acts. Mechanism skills answer "is the gate sound?". This skill answers
"which oversight *shape* should the surface expose?".

Pattern catalog: [references/patterns.md](references/patterns.md).
Adapted from tommyjepsen/awesome-ux-skills `ai-governors`.

## When to use

- Write-approval queues, staged proposals, action confirm, spend UI, agent
  activity / runs, memory capture, voice speaker gates.
- Phrases like: confirm before act, undo, show cost, action plan, cite sources,
  draft then commit, pause the agent.
- **Not** for: low-level gate wiring audits, untrusted prompt framing, or
  workflow Send-and-Wait plumbing in isolation.

## Seam → pattern map

```
