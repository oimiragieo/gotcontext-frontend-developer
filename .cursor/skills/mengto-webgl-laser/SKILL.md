---
name: mengto-webgl-laser
description: Adapter pointer to canonical skills/mengto-webgl-laser for Cursor
---

# mengto-webgl-laser (Cursor adapter)

Canonical skill: [`../../../skills/mengto-webgl-laser/SKILL.md`](../../../skills/mengto-webgl-laser/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-webgl-laser
description: Create a fixed full-screen WebGL laser background effect with a thin white-hot vertical core, restrained brand-colored halo, and soft smoky fog around the beam. Use only for laser background effects, not full page layout, copy, generic hero scenes, particles, or unrelated motion systems.
---

# WebGL Laser

## Scope
- Apply only to the laser background effect.
- Use a fixed full-screen canvas behind the DOM.
- Set `pointer-events: none` on the canvas.
- Keep page content in a higher stacking context.
- Match the halo and smoke to the page's primary or strongest accent color.

## Visual Target
- Thin vertical beam: crisp white-hot inner core, narrow colored halo.
- Atmospheric smoke: soft cloudy breakup concentrated around the beam.
- Dark cinematic field: restrained, brand-colored, and readable behind content.
- Slow pulse: glow breathes gently; no aggressive flicker or color cycling.
- Light blade feel: narrow and precise, never a thick neon pillar.

## Layering

```html
<canvas class="laser-canvas" data-webgl-laser></canvas>
<main class="page-content">
  ...
</main>
```

```
