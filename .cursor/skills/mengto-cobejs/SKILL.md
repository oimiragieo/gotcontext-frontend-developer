---
name: mengto-cobejs
description: Adapter pointer to canonical skills/mengto-cobejs for Cursor
---

# mengto-cobejs (Cursor adapter)

Canonical skill: [`../../../skills/mengto-cobejs/SKILL.md`](../../../skills/mengto-cobejs/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-cobejs
description: Use when adding a lightweight interactive globe with cobe (canvas setup, markers, interaction, performance, integration with React/Next.js).
---

# cobe.js — Lightweight WebGL Globe Skill

## When to use
- A “spinning globe” / location markers in hero or about pages
- You want a small, focused globe lib (not full three.js)
- Decorative + interactive (markers, rotation) with minimal setup

## Key APIs/patterns
- Core:
  - `import createGlobe from "cobe"`
  - `const globe = createGlobe(canvas, { ...options, onRender(state) { ... } })`
- Important options (common):
  - `devicePixelRatio`, `width`, `height`
  - `phi`, `theta` (rotation angles)
  - `scale`, `dark`, `diffuse`
  - `baseColor`, `markerColor`, `glowColor`
  - `markers: [{ location: [lat, lon], size, color? }]`
- Lifecycle:
  - `globe.toggle()` pauses RAF
  - `globe.destroy()` removes instance

## Common pitfalls
- Canvas sizing mismatch
  - Set CSS size AND set canvas `width/height` scaled for DPR.
- Not updating on resize
```
