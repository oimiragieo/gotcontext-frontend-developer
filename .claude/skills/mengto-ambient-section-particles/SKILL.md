---
name: mengto-ambient-section-particles
description: Adapter pointer to canonical skills/mengto-ambient-section-particles for Claude Code
---

# mengto-ambient-section-particles (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-ambient-section-particles/SKILL.md`](../../../skills/mengto-ambient-section-particles/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-ambient-section-particles
description: Add a restrained particle atmosphere inside one section with configurable shapes, density, gravity, wind, sway, rotation, recycling or settling, pointer disturbance, visibility pausing, responsive limits, and reduced-motion fallbacks. Use for petals, leaves, snow, sparks, confetti, dots, paper, icons, or brand fragments that support a section's mood without obscuring content.
---

# Ambient Section Particles

Build particles as a bounded atmosphere layer, not as a page-wide screensaver. Keep the content primary and stop work when the effect cannot be seen.

## Choose the renderer

- Use canvas for roughly 40 or more small particles, frequent motion, pointer forces, or simple procedural shapes.
- Use DOM or inline SVG for a small count of branded fragments that need individual styling or semantic labels.
- Use WebGL only for thousands of particles, depth, shaders, or real 3D behavior. Cap device pixel ratio and provide a static fallback.

Start with the least expensive renderer that preserves the desired shape language.

## Define one configuration

```js
const particles = {
  count: 54,
  gravity: 7,
  wind: -3,
  sway: 16,
  speed: [8, 18],
  size: [4, 12],
  opacity: [0.18, 0.62],
  rotation: [-0.8, 0.8],
  mode: "recycle",
```
