---
name: threejs-textures
description: Adapter pointer to canonical skills/threejs-textures for Claude Code
---

# threejs-textures (Claude Code adapter)

Canonical skill: [`../../../skills/threejs-textures/SKILL.md`](../../../skills/threejs-textures/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: threejs-textures
description: Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimization.
---

# Three.js Textures

## Quick Start

```javascript
import * as THREE from "three";

// Load texture
const loader = new THREE.TextureLoader();
const texture = loader.load("texture.jpg");

// Apply to material
const material = new THREE.MeshStandardMaterial({
  map: texture,
});
```

## Texture Loading

### Basic Loading

```javascript
const loader = new THREE.TextureLoader();

// Async with callbacks
```
