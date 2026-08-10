---
name: mengto-shaders-cursor-ripples
description: Adapter pointer to canonical skills/mengto-shaders-cursor-ripples for Claude Code
---

# mengto-shaders-cursor-ripples (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-shaders-cursor-ripples/SKILL.md`](../../../skills/mengto-shaders-cursor-ripples/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-shaders-cursor-ripples
description: Add cursor-following fluid WebGPU distortion over an existing image with the Shaders library's ImageTexture and CursorRipples components. Use when a hero, gallery, or media panel needs a water-ripple mouse effect; when replacing a drifting CSS spotlight or flashlight reveal; or when a prompt says to borrow only the shader interaction from a Shaders.com reference while preserving the current brand, image, copy, and layout.
---

# Shaders Cursor Ripples

## Core Contract

1. Preserve the existing page, content, and semantic image.
2. Install `shaders` and import from the active framework subpath.
3. Render the source image through one `Shader` canvas.
4. Place `CursorRipples` after `ImageTexture` so it post-processes that image.
5. Keep `toneMapping="aces"` on the root.
6. Let Shaders track the cursor. Remove custom spotlight coordinates, radial masks, duplicated reveal images, and pointer animation loops.
7. Keep one real image beneath the canvas as the accessible loading and WebGPU fallback.
8. Disable the shader for reduced motion and unsupported WebGPU.
9. Lazy-load the shader code so the library does not inflate the initial page bundle.

When the user asks for only the shader effect, do not copy a reference's ribbon, blob, glow, typography, layout, copy, colors, or identity. Do not substitute the Shaders `Water` component: `CursorRipples` is the interactive image-displacement effect.

## Inspect Before Editing

- Find the real media wrapper, image URL, crop, overlays, z-index, and existing motion.
- Confirm the wrapper has a non-zero rendered width and height.
- Search for old reveal code such as `data-reveal-hover`, `mask-image: radial-gradient`, duplicated images, `requestAnimationFrame`, and manual pointer listeners.
- Preserve unrelated parallax or entrance motion unless it conflicts with the shader canvas.
- Check the installed `shaders` version and current framework API when the package may have changed.

## Install
```
