# Trust-builder patterns (catalog)

Source adapted from tommyjepsen/awesome-ux-skills `ai-trust-builders`.
Use with [SKILL.md](../SKILL.md) for product seam mapping.

| # | Pattern | One-liner |
|---|---|---|
| 1 | **Caveat** | Decision-time reminder that AI can be wrong; specific > blanket. |
| 2 | **Consent** | Opt-in before record/analyze/train; separate those decisions. |
| 3 | **Data Ownership** | Retention vs training controls; privacy-protective defaults. |
| 4 | **Disclosure** | Label AI actor and cloud vs local; use verbs ("Summarized with…"). |
| 5 | **Footprints** | Inspectable trail of sends/stores/applies. |
| 6 | **Incognito** | Session without durable memory/write. |
| 7 | **Watermark** | Mark AI-generated media/artifacts in mixed surfaces. |

## Pairings

- Disclosure + Footprints (cloud brain / dreaming / failover)
- Consent + Disclosure (voice, camera, enrollment)
- Data Ownership + Incognito (sensitive work sessions)
- Caveat + Citations (research answers the owner might act on)

## Pitfalls

- Caveat-only safety (habituated, ignored).
- Consent in ToS / `.env` comments only.
- Training and retention collapsed into one toggle.
- Empty success when the real state is unavailable/degraded.
