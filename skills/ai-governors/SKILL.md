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
| Staged fact writes / `JARVIS_WRITE_APPROVAL` | Verification + Memory + Footprints | Queue must drain; doctor depth; dedupe pending |
| Transcript dreaming accept/reject | Verification + Sample Response + Cost Estimates + Draft Mode | Never auto-apply; owner HITL only; bind approval to exact bytes |
| Action / codework confirm | Action Plan + Verification + Cost Estimates | Confirm gate ahead of fire; camera forward must not pop `pending_action` |
| Brain / Exa / OpenRouter spend | Cost Estimates (+ Draft Mode for bakeoffs) | `PRICED_LANES` + ledgers; unknown → visible not "free" |
| Console Runs / agent activity | Shared Vision + Stream of Thought + Controls | Read-only detail; stop/cancel only if real control exists |
| Recall / fact capture | Memory (+ Verification for sensitive) | Matched-core-first; secret scan before store |
| Research / web / vision observer | Citations + References | Untrusted framing; observer mode never names |
| Voice speaker gate | Controls + Verification | Gate modes off/shadow/on; partial API must not crash UI |

## Calibration (friction vs speed)

Match friction to **irreversibility × blast radius**, not to how "AI" the feature feels:

1. **High** (money, outbound message, memory write, dream apply, destructive tool) → contractual Action Plan or Verification; no silent defaults that grant the act.
2. **Medium** (long research, multi-step orchestrator run) → Shared Vision + Controls + Cost Estimates; Verification only on the commit step.
3. **Low** (search, draft reply, deterministic math) → skip Verification; optional Citations.

Prompt fatigue is a defect: a confirm on every chat turn trains the owner to click through. Prefer one strong gate on the irreversible step.

## Design checklist (before shipping a HITL surface)

- [ ] Name the irreversible effect in the confirm copy (what lands where).
- [ ] Approval is bound to **exact bytes / run id / proposal id**, not a path or intent (`#142` digest law).
- [ ] Cost or side-effect estimate is visible **before** the owner commits, when spend is non-trivial.
- [ ] Undo or compensating action is stated when the act is reversible; when not, say so.
- [ ] Failure/degrade path does not skip the gate (happy-path-only guards are inert).
- [ ] Absent evidence ≠ consent (no "missing lease means free").

## Anti-patterns (JARVIS-specific)

- Manifest line that promises a capability the confirm gate still blocks (false capability).
- Dreaming that stages then auto-applies "because the model was confident".
- Cost UI that only meters vision/TTS while the brain lane is free (`#140` class).
- Console control that looks like Stop but only navigates away.
- Replacing full speaker state with a partial `{gate_mode}` payload (UI crash).

## Output format

When recommending governors:

1. **Situation** — one sentence blast radius.
2. **Patterns** — 1–3 from the catalog, not all 13.
3. **Seam** — concrete file/flag/API in omega-jarvis / omega-console / orch.
4. **Friction call** — high/medium/low and why.
5. **Falsify next** — hand off to `falsify-a-gate-design` for wiring attack.

## Cross-references

- `falsify-a-gate-design` — gate wiring inert modes.
- `design-self-improvement-loop` — autonomy safety before flag-flip.
- `n8n-human-in-the-loop-approval` — workflow Send-and-Wait.
- `default-unknown-to-costly-and-metered` — spend visibility polarity.
- `ai-trust-builders` — disclosure/consent beside oversight.
- `ai-wayfinders` — first-run discoverability (does not replace HITL).
