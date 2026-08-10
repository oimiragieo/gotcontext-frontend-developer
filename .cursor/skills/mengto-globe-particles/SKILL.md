---
name: mengto-globe-particles
description: Adapter pointer to canonical skills/mengto-globe-particles for Cursor
---

# mengto-globe-particles (Cursor adapter)

Canonical skill: [`../../../skills/mengto-globe-particles/SKILL.md`](../../../skills/mengto-globe-particles/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-globe-particles
description: Create a globe-like 3D particle visualization with a dense luminous spherical core and thinner orbital ring or flattened disc. Use when a design needs a premium planetary, orbital, synthesized data-globe effect rendered with real WebGL/Three.js particles, not generic starfields or full page layout changes.
---

# Globe Particles

## Scope
- Apply only to a globe-like 3D particle visualization.
- Do not change full page layout, copy, or unrelated motion systems.
- Use for planetary, orbital, infrastructure, or synthesized data-globe effects.
- Keep the core neutral or white-hot and derive ring/glow accents from the design's primary color.

## Visual Target
- Dense spherical core of luminous points.
- Thinner outer orbital ring or flattened disc around the sphere.
- Clear globe silhouette with tilt, depth, and layered particle density.
- Dark atmospheric background, restrained glow, clean structure, and subtle sci-fi depth.
- Premium and cinematic, not playful or noisy.

## HTML And CSS

```html
<div class="globe-particles-shell">
  <canvas class="globe-particles-canvas" data-globe-particles></canvas>
</div>
```

```css
.globe-particles-shell {
```
