---
name: mengto-dither-background
description: Adapter pointer to canonical skills/mengto-dither-background for Cursor
---

# mengto-dither-background (Cursor adapter)

Canonical skill: [`../../../skills/mengto-dither-background/SKILL.md`](../../../skills/mengto-dither-background/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-dither-background
description: Create a dark monochrome procedural background with enlarged square pixels and visible Bayer-style ordered dithering. Use when a page needs an atmospheric near-black dither field, broad organic waves or cloud masses, and restrained gray-white highlights behind framed UI, hero content, or data overlays.
---

# Dither Background

## Use When
- A dark interface needs an atmospheric monochrome background layer.
- The visual should show enlarged square pixels and visible ordered dithering.
- The design calls for organic waves, cloud-like masses, or procedural depth without colorful gradients.
- The background should support framed UI, hero content, or data overlays.

## Visual Target
- Near-black base with charcoal midtones, soft gray buildup, and occasional white highlights.
- Clearly visible square pixel cells, not tiny film grain.
- 4x4 Bayer-style dither pattern or equivalent ordered thresholding.
- Broad organic waves or cloud-like masses, not random TV noise.
- Vignetted edges so the brighter mass sits centrally or off-axis.

## HTML And CSS

```html
<canvas class="dither-background" data-dither-background></canvas>
```

```css
.dither-background {
  position: fixed;
  inset: 0;
```
