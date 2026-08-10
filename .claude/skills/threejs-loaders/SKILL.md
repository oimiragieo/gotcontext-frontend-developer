---
name: threejs-loaders
description: Adapter pointer to canonical skills/threejs-loaders for Claude Code
---

# threejs-loaders (Claude Code adapter)

Canonical skill: [`../../../skills/threejs-loaders/SKILL.md`](../../../skills/threejs-loaders/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: threejs-loaders
description: Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress.
---

# Three.js Loaders

## Quick Start

```javascript
import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

// Load GLTF model
const loader = new GLTFLoader();
loader.load("model.glb", (gltf) => {
  scene.add(gltf.scene);
});

// Load texture
const textureLoader = new THREE.TextureLoader();
const texture = textureLoader.load("texture.jpg");
```

## LoadingManager

Coordinate multiple loaders and track progress.

```javascript
const manager = new THREE.LoadingManager();
```
