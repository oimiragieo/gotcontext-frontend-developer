---
name: mengto-threejs
description: Adapter pointer to canonical skills/mengto-threejs for Cursor
---

# mengto-threejs (Cursor adapter)

Canonical skill: [`../../../skills/mengto-threejs/SKILL.md`](../../../skills/mengto-threejs/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-threejs
description: Use when building or debugging interactive 3D scenes on the web with Three.js (scene/camera/renderer, lights/materials, GLTF loading, controls, performance). Helpful for designers shipping 3D UI moments.
---

# Three.js — WebGL 3D Scenes Skill

## When to use
- Real 3D: product spins, interactive hero scenes, shaders/material effects, 3D data viz
- You need full control beyond “background effects”
- You can budget time for asset pipeline + performance tuning

## Core mental model
- Create:
  - `Scene` (root graph)
  - `Camera` (Perspective/Orthographic)
  - `Renderer` (`WebGLRenderer`)
  - `Mesh` = `Geometry` + `Material`
  - Lights (if using non-unlit materials)
- Render loop:
  - `requestAnimationFrame(animate)`
  - Update time-based animations, controls, mixers, then `renderer.render(scene, camera)`

## Key APIs/patterns
- Setup:
  - `const renderer = new THREE.WebGLRenderer({ canvas, antialias, alpha })`
  - `renderer.setSize(width, height, false)`
  - `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`
- Camera:
  - `camera.aspect = width / height; camera.updateProjectionMatrix()`
```
