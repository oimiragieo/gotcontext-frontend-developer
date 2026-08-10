---
name: mengto-corner-diagonals
description: Adapter pointer to canonical skills/mengto-corner-diagonals for Cursor
---

# mengto-corner-diagonals (Cursor adapter)

Canonical skill: [`../../../skills/mengto-corner-diagonals/SKILL.md`](../../../skills/mengto-corner-diagonals/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-corner-diagonals
description: Apply diagonal-cut corners and chamfered edges to buttons, cards, panels, and container shells. Use when a design needs precise geometric framing, sci-fi UI surfaces, clipped-corner controls, or engineered sharp containers instead of rounded pills or plain rectangles.
---

# Corner Diagonals

## Scope
- Apply only to buttons, cards, panels, and container shells.
- Use when surfaces need diagonal-cut corners or chamfered edges.
- Keep the hit area readable and usable even when the visual shape is clipped.
- Reuse the same corner logic across surfaces so it feels like a system.

## Visual Target
- Diagonal cuts should feel engineered, sharp, and intentional.
- Cuts stay subtle and proportional to the component size.
- One or more corners can be chamfered, but the silhouette should still read quickly.
- Use diagonal corners as a repeated structural motif, not a one-off trick.

## Cut Tokens

```css
:root {
  --corner-cut-sm: 8px;
  --corner-cut-md: 14px;
  --corner-cut-lg: 24px;
  --corner-line: rgba(255, 255, 255, 0.18);
  --corner-line-strong: rgba(255, 255, 255, 0.34);
  --corner-fill: rgba(10, 14, 24, 0.82);
  --corner-accent: #8b5cf6;
```
