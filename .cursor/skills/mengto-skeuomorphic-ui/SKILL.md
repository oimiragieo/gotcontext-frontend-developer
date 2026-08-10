---
name: mengto-skeuomorphic-ui
description: Adapter pointer to canonical skills/mengto-skeuomorphic-ui for Cursor
---

# mengto-skeuomorphic-ui (Cursor adapter)

Canonical skill: [`../../../skills/mengto-skeuomorphic-ui/SKILL.md`](../../../skills/mengto-skeuomorphic-ui/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-skeuomorphic-ui
description: Create skeuomorphic web UI surfaces with layered gradients, stacked inner and outer shadows, reflective gradient borders, micro texture, and embossed text or icon details. Use when asked for pressed, carved, tactile, realistic, soft-plastic, soft-metal, or premium physical interface styling.
---

# Skeuomorphic UI

## Use When
- A card, button, switch, dial, input, toolbar, or control should feel tactile.
- A flat surface needs physical depth without becoming glossy or cartoonish.
- The design calls for pressed, carved, raised, soft-plastic, soft-metal, or premium hardware-like UI.

## Surface Recipe
1. Start with a rounded shape and a soft vertical gradient: lighter top, darker bottom.
2. Add a 1px gradient-border wrapper to simulate a reflective edge.
3. Stack outer shadows for elevation and inset shadows for carved depth.
4. Add a fine top-edge highlight and a darker lower edge.
5. Use text shadows and icon shadows sparingly for an embossed feel.
6. Add micro-details only when scale supports it: dots, grain, seams, or tiny specular marks.
7. Keep transitions smooth and short: `160ms` to `240ms`.

## Base Tokens
Tune these per brand and theme.

```css
:root {
  --sk-bg-top: #f8fafc;
  --sk-bg-mid: #e9eef5;
  --sk-bg-bottom: #cfd7e4;
  --sk-edge-top: rgba(255, 255, 255, 0.82);
```
