---
name: ai-trust-builders
description: Adapter pointer to canonical skills/ai-trust-builders for Cursor
---

# ai-trust-builders (Cursor adapter)

Canonical skill: [`../../../skills/ai-trust-builders/SKILL.md`](../../../skills/ai-trust-builders/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
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
```
