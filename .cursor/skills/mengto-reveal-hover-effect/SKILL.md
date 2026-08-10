---
name: mengto-reveal-hover-effect
description: Adapter pointer to canonical skills/mengto-reveal-hover-effect for Cursor
---

# mengto-reveal-hover-effect (Cursor adapter)

Canonical skill: [`../../../skills/mengto-reveal-hover-effect/SKILL.md`](../../../skills/mengto-reveal-hover-effect/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-reveal-hover-effect
description: Build cursor-following spotlight reveals that expose a second aligned image through a soft radial mask. Use for hover-to-color, before-and-after, x-ray, material, texture, product-detail, and illustrated hero effects where a desaturated or embossed base image should remain visible while another treatment follows an eased pointer.
---

# Reveal Hover Effect

## Core Contract

1. Prepare two images with identical dimensions, composition, crop, and focal point.
2. Keep the base image fully visible.
3. Stack the reveal image directly above it.
4. Apply a feathered radial `mask-image` to the reveal image.
5. Track pointer coordinates in the component's local coordinate space.
6. Ease the rendered position toward the raw pointer with `requestAnimationFrame`.
7. Collapse the mask on pointer exit; never leave a stale spotlight behind.

Default to CSS masks instead of generating a canvas data URL every frame. The CSS version preserves the same look with less allocation and simpler cleanup.

## Motion Defaults

- Desktop spotlight radius: `260px`.
- Compact spotlight radius: `140px` to `220px`.
- Pointer easing: `0.1`.
- Radius easing: `0.14`.
- Mask stops:
  - `0%`: alpha `1`
  - `40%`: alpha `1`
  - `60%`: alpha `0.75`
  - `75%`: alpha `0.4`
```
