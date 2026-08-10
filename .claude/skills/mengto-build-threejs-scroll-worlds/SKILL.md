---
name: mengto-build-threejs-scroll-worlds
description: Adapter pointer to canonical skills/mengto-build-threejs-scroll-worlds for Claude Code
---

# mengto-build-threejs-scroll-worlds (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-build-threejs-scroll-worlds/SKILL.md`](../../../skills/mengto-build-threejs-scroll-worlds/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-build-threejs-scroll-worlds
description: Build rich, scroll-controlled real-time Three.js experiences as one persistent 3D world whose camera, lighting, atmosphere, materials, objects, DOM story, and interactions evolve across authored chapters. Use for 3D scrollytelling, scroll-driven WebGL worlds, camera journeys, interactive portfolios, product stories, exhibitions, explainers, game or film microsites, spatial narratives, and multi-scene websites where native scroll should travel through one continuous place. Not limited to landing pages.
---

# Build Three.js Scroll Worlds

Build one detailed real-time world and use native document scroll as its deterministic conductor. Keep the renderer, scene graph, and spatial continuity alive while camera composition, light, fog, animation, copy, and interaction focus move through authored chapters.

The mechanism is **one persistent Three.js world + one normalized reversible scroll state**. If removing either makes the experience collapse into stacked sections, this skill applies.

The exact [Kage demo](demo/index.html) proves the quality bar; it is staging, not a mandatory subject or layout. Use its detailed anatomy only when the requested direction benefits from it: [references/kage-anatomy.md](references/kage-anatomy.md).

## Route the request correctly

- Use `threejs` for a single interactive scene with no scroll-authored journey.
- Use `scroll-world-storytelling` when deciding between real-time 3D, pre-rendered video, and DOM-first storytelling.
- Use `scroll-scrubbed-visual-sequence` for a video or image sequence whose time is scrubbed by scroll.
- Use `cinematic-scroll-storytelling` for DOM-first GSAP/Lenis choreography.
- Use this skill when objects must remain truly spatial and interactive while scroll moves through several compositions in one live WebGL world.

Do not disguise a video as Three.js. The public [oso95/scroll-world](https://github.com/oso95/scroll-world) project, reviewed at commit `71cc36d`, is a strong reference for intake, scene ledgers, budget gates, mobile-specific composition, config-driven playback, and seam QA, but its renderer is a pre-generated video chain. This skill adopts those structural strengths while retaining real geometry, materials, lighting, raycasting, and camera control.

## Read the build references

Before implementing a new world, read:

- [references/world-bible.md](references/world-bible.md) for intake, art direction, scene, material, texture, and interaction ledgers;
- [references/realtime-architecture.md](references/realtime-architecture.md) for the scene graph, conductor, camera, loading, interaction, and lifecycle patterns;
- [references/quality-and-qa.md](references/quality-and-qa.md) before optimization and final verification.
```
