---
name: mengto-nested-container-frames
description: "Use when implementing a container-in-container layout with an outer centered frame (vertical boundary lines, corner markers) and inset inner containers with their own backgrounds and rounded frames. Prefer this over mengto-nested-container-clean-agency when the technique is structural nested frames, not a full agency visual system."
---

# Nested Container Frames Skill

## Use When
- A layout needs a container-in-container system with visible outer bounds, inset inner frames, and layered page structure.

## Workflow
1. Define an outer centered container that controls the global page width.
2. Add visible vertical boundary lines and small corner markers to establish the frame.
3. Place inner containers inset from the outer edges using consistent padding.
4. Give each inner level its own background, border, radius, and spacing rhythm.
5. Use the frame hierarchy to separate hero, feature, proof, and CTA modules without adding heavy cards.

## Guardrails
- Do not nest cards inside cards until the layout feels boxed in.
- Do not let frame lines overpower content readability.
