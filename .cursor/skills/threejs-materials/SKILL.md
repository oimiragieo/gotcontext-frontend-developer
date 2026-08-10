---
name: threejs-materials
description: Adapter pointer to canonical skills/threejs-materials for Cursor
---

# threejs-materials (Cursor adapter)

Canonical skill: [`../../../skills/threejs-materials/SKILL.md`](../../../skills/threejs-materials/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: threejs-materials
description: Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material performance.
---

# Three.js Materials

## Quick Start

```javascript
import * as THREE from "three";

// PBR material (recommended for realistic rendering)
const material = new THREE.MeshStandardMaterial({
  color: 0x00ff00,
  roughness: 0.5,
  metalness: 0.5,
});

const mesh = new THREE.Mesh(geometry, material);
```

## Material Types Overview

| Material             | Use Case                              | Lighting           |
| -------------------- | ------------------------------------- | ------------------ |
| MeshBasicMaterial    | Unlit, flat colors, wireframes        | No                 |
| MeshLambertMaterial  | Matte surfaces, performance           | Yes (diffuse only) |
| MeshPhongMaterial    | Shiny surfaces, specular highlights   | Yes                |
| MeshStandardMaterial | PBR, realistic materials              | Yes (PBR)          |
```
