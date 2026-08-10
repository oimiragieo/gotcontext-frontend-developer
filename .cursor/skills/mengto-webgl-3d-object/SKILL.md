---
name: mengto-webgl-3d-object
description: Adapter pointer to canonical skills/mengto-webgl-3d-object for Cursor
---

# mengto-webgl-3d-object (Cursor adapter)

Canonical skill: [`../../../skills/mengto-webgl-3d-object/SKILL.md`](../../../skills/mengto-webgl-3d-object/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-webgl-3d-object
description: Create a real 3D WebGL object with geometric mesh depth, physically based material, directional and ambient lighting, perspective camera, subtle rotation, and floating motion. Use when a page needs a faceted 3D hero object or product-like visual with real lighting instead of CSS transform tricks.
---

# WebGL 3D Object

## Use When
- A hero, feature block, or product moment needs one strong 3D object.
- The visual should show real geometry, lighting, highlights, and edges.
- A faceted mesh should float or rotate subtly inside a web layout.
- CSS transforms, SVG illusions, or flat gradients are not enough.

## Rules
1. Use real 3D geometry: `IcosahedronGeometry`, `DodecahedronGeometry`, `BoxGeometry`, custom `BufferGeometry`, or a glTF mesh.
2. Use a perspective camera so the object has depth and scale.
3. Use PBR material: `MeshStandardMaterial` or `MeshPhysicalMaterial`.
4. Tune `metalness`, `roughness`, and `emissive` to match the brand mood.
5. Light the object with at least one directional light plus ambient or hemisphere fill.
6. Animate transforms only: subtle rotation, bobbing, or parallax.
7. Handle resize and dispose geometry/material/renderer on teardown.

## HTML And CSS

```html
<div class="webgl-object-shell">
  <canvas class="webgl-object-canvas" data-webgl-3d-object></canvas>
</div>
```

```
