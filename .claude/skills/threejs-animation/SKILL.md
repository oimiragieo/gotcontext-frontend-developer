---
name: threejs-animation
description: Adapter pointer to canonical skills/threejs-animation for Claude Code
---

# threejs-animation (Claude Code adapter)

Canonical skill: [`../../../skills/threejs-animation/SKILL.md`](../../../skills/threejs-animation/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: threejs-animation
description: Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or blending animations.
---

# Three.js Animation

## Quick Start

```javascript
import * as THREE from "three";

// Simple procedural animation
const clock = new THREE.Clock();

function animate() {
  const delta = clock.getDelta();
  const elapsed = clock.getElapsedTime();

  mesh.rotation.y += delta;
  mesh.position.y = Math.sin(elapsed) * 0.5;

  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();
```

## Animation System Overview

```
