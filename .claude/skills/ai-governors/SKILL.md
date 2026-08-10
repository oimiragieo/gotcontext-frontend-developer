---
name: ai-governors
description: Adapter pointer to canonical skills/ai-governors for Claude Code
---

# ai-governors (Claude Code adapter)

Canonical skill: [`../../../skills/ai-governors/SKILL.md`](../../../skills/ai-governors/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: ai-governors
description: "Use when designing or auditing JARVIS/console human-in-the-loop — write-approval, dreaming accept/reject, action confirm, spend caps, Runs detail, memory capture, or any AI action with irreversible blast radius. Trigger on confirmation UX, undo, cost-before-act, show-the-plan, citations, or 'keep the owner in control'."
---

# AI Governors — JARVIS HITL product UX

Governors are **product patterns** that keep the owner in control while JARVIS
acts. Mechanism skills (`falsify-a-gate-design`, `design-self-improvement-loop`,
`transcript-dream-hitl`) answer "is the gate sound?". This skill answers "which
oversight *shape* should the surface expose?".

Pattern catalog (names + definitions): [references/patterns.md](references/patterns.md).
Adapted from tommyjepsen/awesome-ux-skills `ai-governors` for this ecosystem.

## When to use

- Designing or reviewing: write-approval queue, dreaming proposals, action
  confirm, voice speaker gate, console Admin flags, cost/spend UI, Runs/agent
  activity, memory capture chips.
- Phrases like: confirm before act, undo, show cost, action plan, cite sources,
  draft then commit, pause the agent.
- **Not** for: wiring a deny-list so it cannot be inert (`falsify-a-gate-design`),
  untrusted prompt framing (`gate-untrusted-content-into-prompts`), or n8n
  Send-and-Wait plumbing (`n8n-human-in-the-loop-approval`).

## JARVIS seam → pattern map

| Seam | Prefer | Hard rules already in tree |
|---|---|---|
```
