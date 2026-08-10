---
name: mengto-css-border-gradient
description: Adapter pointer to canonical skills/mengto-css-border-gradient for Claude Code
---

# mengto-css-border-gradient (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-css-border-gradient/SKILL.md`](../../../skills/mengto-css-border-gradient/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-css-border-gradient
description: Apply subtle gradient-border treatments for premium web surfaces. Use when cards, pricing panels, nav bars, modals, buttons, or hero surfaces need a refined edge highlight without a loud glow.
---

# Border Gradients

## Use When
- A surface needs a more premium edge than a flat `border`.
- Dark glass, pricing, hero, modal, or feature-card UI feels too plain.
- A hover or focus state needs a quiet brand accent.

## Defaults
- Width: `1px`; use `2px` only for large hero cards or active states.
- Radius: inherit the parent radius.
- Angle: `135deg` or `160deg`.
- Stops: neutral highlight, one brand accent, neutral fade.
- Opacity: keep most stops below `0.4`; subtle beats shiny.

## Simple CSS Pattern
Use this when the surface has a solid or translucent fill.

```css
.gradient-border {
  --surface: rgba(10, 14, 24, 0.72);
  --border-a: rgba(255, 255, 255, 0.34);
  --border-b: rgba(125, 92, 255, 0.36);
  --border-c: rgba(255, 255, 255, 0.08);

  border: 1px solid transparent;
```
