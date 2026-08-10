---
name: mengto-unicorn-studio
description: Adapter pointer to canonical skills/mengto-unicorn-studio for Cursor
---

# mengto-unicorn-studio (Cursor adapter)

Canonical skill: [`../../../skills/mengto-unicorn-studio/SKILL.md`](../../../skills/mengto-unicorn-studio/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-unicorn-studio
description: Use when embedding and customizing Unicorn Studio interactive animations on the web (embed, responsive sizing, performance, layering with UI, fallbacks).
---

# Unicorn Studio — No-code WebGL Scenes (Embed/SDK) Skill

## When to use
- Designers want custom WebGL visuals without hand-coding shaders/three.js
- You need “designed” effects layered with text/images/video, with built-in interactivity
- Site builders: Framer, Webflow, Wix, Figma Sites, etc.

## What it is
- A scene editor (layers + effects + events) that exports:
  - Embed via Unicorn Studio SDK (small JS library)
  - Or JSON/code export for faster/self-hosted loading (plan-dependent)

## Key embed patterns
- Load SDK (can be in `<head>` or footer depending on above-the-fold):
  - UMD from jsDelivr (versioned)
  - Call `UnicornStudio.init()` once DOM is ready
- Add attributes to a container element:
  - `data-us-project="PROJECT_ID"`
  - Optional performance/behavior params:
    - `data-us-scale` (render scale)
    - `data-us-dpi` (resolution multiplier)
    - `data-us-fps` (cap FPS)
    - `data-us-lazyload="true"`
    - `data-us-production="true"`
  - Optional JSON source:
```
