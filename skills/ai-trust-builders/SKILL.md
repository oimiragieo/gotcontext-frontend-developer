---
name: ai-trust-builders
description: "Use when designing JARVIS/console trust, privacy, or honesty UX — OpenRouter/cloud disclosure, voice/mic consent, transcript retention, memory ownership, AI labeling, caveats, or audit footprints. Trigger on 'disclose cloud', 'recording consent', 'what did we send', watermark, incognito, or data-ownership settings."
---

# AI Trust Builders — JARVIS honesty & privacy UX

Trust builders make the system **legible**: what is AI, what left the machine,
what was retained, and how to refuse. Complementary to governors (control of
*actions*) and untrusted framing (control of *prompt injection*).

Pattern catalog: [references/patterns.md](references/patterns.md).
Adapted from tommyjepsen/awesome-ux-skills `ai-trust-builders`.

## When to use

- Cloud cutover, dreaming on OpenRouter, voice enrollment, webcam, transcript
  manifests, recall blocks, console Settings/Admin privacy copy.
- Auditing whether a feature is honest about where data goes.
- **Not** for: scanner/framing implementation (`gate-untrusted-content-into-prompts`),
  cost metering polarity (`default-unknown-to-costly-and-metered`), or HITL
  confirm shapes (`ai-governors`).

## JARVIS seam → pattern map

| Seam | Prefer | Notes |
|---|---|---|
| `JARVIS_BRAIN=openrouter:*` / failover | Disclosure + Caveat + Footprints | Persona + recall leave the box on failover (`JARVIS_CLOUD_FAILOVER`) — say so |
| Transcript dreaming (`LOCAL_ONLY=0`) | Disclosure + Consent + Data Ownership + Footprints | Transcripts to OpenRouter is a privacy event, not a doc footnote |
| Voice mic / speaker enroll / WebRTC | Consent (+ Disclosure) | Recording indicator; gate mode is Control (governors), consent is Trust |
| Webcam / vision-via-brain | Consent + Disclosure + Caveat | Observer mode; no silent always-on claim |
| Memory / facts.db / dream apply | Data Ownership + Footprints + Caveat | Owner can see/delete; dreaming sources labeled |
| Capability manifest / SOUL | Disclosure (honest cannot-do) | False capability line = user-visible bug |
| Console Chat / History | Footprints + Caveat | Show model/provider when non-obvious; History unavailable must say why |
| Generated images / cards | Watermark / attribution where user-facing | Don't pretend human-authored |

## Seven patterns (short)

1. **Caveat** — decision-time "may be wrong", specific when possible; never the only safety net.
2. **Consent** — opt-in for record/enroll/train; separate recording vs training vs sharing.
3. **Data Ownership** — retention vs training toggles; default privacy-protective; say if you never train.
4. **Disclosure** — label AI actor and cloud vs local; verb labels ("Summarized with AI").
5. **Footprints** — inspectable trail of what was sent/stored/applied (run id, proposal id, provider).
6. **Incognito / memory-off** — session without durable write when stakes are high.
7. **Watermark** — mark AI-generated media/artifacts when mixed with human content.

## Honesty rules (repo laws, product form)

- A **false capability line** is a bug — manifest must match mechanism and flags.
- **Merged ≠ live** — disclosure about a new cloud path is inert until deployed.
- **Degrade path** must not drop disclosure (blocked research that still speaks hostile titles).
- Caveats habituate; pair with Footprints/Citations for anything the owner might act on.
- Consent buried in `.env` comments is not consent UX — surface it where the act starts.

## Design checklist

- [ ] Owner can answer: local or cloud? retained? used for dreaming/training?
- [ ] Voice/camera active state is perceptible without reading logs.
- [ ] Dreaming / cloud paths name the provider class (not only "AI").
- [ ] Unavailable/degraded search shows notice, not an empty success.
- [ ] Settings expose ownership controls or an explicit "we don't train on you".

## Output format

1. **Trust risk** — what could be misunderstood.
2. **Patterns** — 1–3.
3. **Surface** — exact UI/copy/flag.
4. **Pair with** — governor if an irreversible act is involved.

## Cross-references

- `ai-governors` — oversight of acts.
- `gate-untrusted-content-into-prompts` — data-plane injection.
- `ai-wayfinders` — onboarding without over-claiming.
- `health-signal-consumer-contract` — honest health signals to operators.
