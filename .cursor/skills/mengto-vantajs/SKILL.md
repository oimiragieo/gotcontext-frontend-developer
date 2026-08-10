---
name: mengto-vantajs
description: Adapter pointer to canonical skills/mengto-vantajs for Cursor
---

# mengto-vantajs (Cursor adapter)

Canonical skill: [`../../../skills/mengto-vantajs/SKILL.md`](../../../skills/mengto-vantajs/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-vantajs
description: Use when adding animated WebGL background effects with Vanta.js (setup, parameters, resizing, performance, integration in React/Next.js).
---

# Vanta.js — Animated WebGL Backgrounds Skill

## When to use
- Decorative animated backgrounds behind hero sections
- You want “wow” quickly without building a full three.js scene
- Lightweight integration into static sites or React/Vue

## How it works
- Vanta injects a canvas into a container element and renders an effect (many use three.js).
- Typical usage: include `three.min.js` (or provide THREE) + one Vanta effect bundle.

## Key APIs/patterns
- Init:
  - `const effect = VANTA.WAVES({ el: "#hero", ...options })`
- Update after init:
  - `effect.setOptions({ color: 0xff88cc })`
- Resize:
  - `effect.resize()` (if container size changes)
- Cleanup:
  - `effect.destroy()` (important in SPAs)

## Common pitfalls
- Container has no size → nothing visible
  - Ensure the target element has explicit width/height (or is laid out).
- Multiple WebGL canvases on one page → GPU load
```
