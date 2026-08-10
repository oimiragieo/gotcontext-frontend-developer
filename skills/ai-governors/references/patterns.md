# Governor patterns (catalog)

Source adapted from tommyjepsen/awesome-ux-skills `ai-governors`.
Use with [SKILL.md](../SKILL.md) for JARVIS seam mapping.

| # | Pattern | One-liner |
|---|---|---|
| 1 | **Action Plan** | Show intended steps before commit (advisory vs contractual). |
| 2 | **Branches** | Parallel explorations with trail back to origin. |
| 3 | **Citations** | Tie claims to exact source passages. |
| 4 | **Controls** | Stop / pause / queue in-flight work; same place every time. |
| 5 | **Cost Estimates** | Show spend drivers before and during generation. |
| 6 | **Draft Mode** | Cheap preview before full-cost run; never silent downgrade. |
| 7 | **Memory** | Cross-session retention with visible add/edit/delete/off. |
| 8 | **References** | Organized source set beside inline citations. |
| 9 | **Sample Response** | Preview one row/result before bulk apply. |
| 10 | **Shared Vision** | Let the owner see what the agent is doing live. |
| 11 | **Stream of Thought** | Progress/fidelity against the plan during execution. |
| 12 | **Variations** | Multiple candidates before commit. |
| 13 | **Verification** | Required human approval before irreversible harm. |

## Pairings that pay off here

- Action Plan → Verification (dream apply, outbound, destructive tools)
- Draft Mode → Cost Estimates (model bakeoffs, image/TTS)
- Sample Response → Verification (bulk memory / dream batches)
- Shared Vision → Controls (orchestrator runs, console agent activity)
- Memory → Verification (sensitive fact capture)
- Citations + References (research / web / transcripts)

## Verification worth the friction

Use when failure risks: reputation, money, security, lost work, costly cleanup.
Skip for: search, draft-only replies, deterministic low-stakes lanes.
