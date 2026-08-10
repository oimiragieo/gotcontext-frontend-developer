---
name: mengto-build-threejs-enemy-systems
description: Adapter pointer to canonical skills/mengto-build-threejs-enemy-systems for Claude Code
---

# mengto-build-threejs-enemy-systems (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-build-threejs-enemy-systems/SKILL.md`](../../../skills/mengto-build-threejs-enemy-systems/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-build-threejs-enemy-systems
description: Build or refactor reusable, data-driven enemy archetype and moveset systems for Three.js action games. Use for enemy content schemas, model and rig conventions, combat move timing and contact contracts, runtime state boundaries, placeholder fallbacks, deterministic fixtures, or production playthrough validation.
---

# Build Three.js Enemy Systems

Make each enemy a portable authored definition consumed by shared runtime systems. Keep AI choice, combat resolution, rendering, and feedback as separate consumers of the same stable contract.

## Separate content from runtime state

- Put stable IDs, role/tags, base stats, presentation spec, move IDs, AI hints, feedback hook IDs, rewards, and variant data in immutable authored definitions.
- Put instance ID, transform, health/posture, target, current move and phase clock, cooldowns, statuses, pathing, visibility, and LOD state in runtime instances.
- Reference definitions by ID. Reject duplicate IDs, missing references, invalid ranges, or impossible timing during content validation.
- Never mutate authored definitions, store live timers in content, or duplicate the combat clock across AI, animation, and rendering.

## Normalize presentation contracts

Define these fields before integrating a model:

- source or factory ID, provenance, coordinate system, forward axis, and meters-per-unit;
- root pivot at ground contact, normalized scale, facing offset, and visual height;
- simple movement collider plus named hurtboxes, independent of render geometry;
- stable sockets for contact origins, weapons, projectiles, VFX, audio, UI markers, and targeting;
- rig and semantic clip map for idle, locomotion, moves, reactions, and death;
- LOD tiers with hysteresis, animation/update policy, and unchanged gameplay colliders.

Normalize at the asset boundary. Do not scatter scale fixes, pivot offsets, raw clip names, or compensating rotations through gameplay code.

## Define moves as data
```
