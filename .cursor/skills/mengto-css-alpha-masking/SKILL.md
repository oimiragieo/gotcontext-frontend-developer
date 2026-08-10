---
name: mengto-css-alpha-masking
description: Adapter pointer to canonical skills/mengto-css-alpha-masking for Cursor
---

# mengto-css-alpha-masking (Cursor adapter)

Canonical skill: [`../../../skills/mengto-css-alpha-masking/SKILL.md`](../../../skills/mengto-css-alpha-masking/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-css-alpha-masking
description: Apply CSS alpha masking with linear-gradient for horizontal or vertical edge fades (mask-image and -webkit-mask-image). Use when asked for alpha masks, fade edges, or CSS mask gradients.
---

# CSS Alpha Masking Skill

## Workflow
1. Confirm direction (horizontal or vertical) and fade stop percentages.
2. Provide the inline CSS snippet and any needed class usage.
3. Offer small tweaks only (direction, stop positions, colors).

## Usage checklist
- Apply the mask styles directly on the element or in a CSS class.
- Always include both `mask-image` and `-webkit-mask-image` for Safari.
- Ensure the element has visible content; masks reveal/hide alpha only.

## Horizontal (left/right) fade
```css
/* Add this inline CSS to any element */
mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
-webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
```

## Vertical (top/bottom) fade
```css
/* Add this inline CSS to any element */
mask-image: linear-gradient(to bottom, transparent, black 15%, black 85%, transparent);
-webkit-mask-image: linear-gradient(to bottom, transparent, black 15%, black 85%, transparent);
```
```
