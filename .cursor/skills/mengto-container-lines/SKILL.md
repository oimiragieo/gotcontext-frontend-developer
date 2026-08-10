---
name: mengto-container-lines
description: Adapter pointer to canonical skills/mengto-container-lines for Cursor
---

# mengto-container-lines (Cursor adapter)

Canonical skill: [`../../../skills/mengto-container-lines/SKILL.md`](../../../skills/mengto-container-lines/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-container-lines
description: Add vertical container-size guide lines with mini corner squares for precise, structured web layouts. Use when asked for container lines, measured layout guides, vertical boundary lines, editorial grid markers, or small corner-square frame details.
---

# Container Lines

## Use When
- A page needs subtle vertical guides that reveal the content container width.
- A hero, section, or product page feels too loose and needs structural tension.
- The design calls for mini corner squares, measured edges, or quiet technical framing.

## Rules
1. Draw lines at the left and right edges of the main content container.
2. Keep lines thin: `1px` with low opacity.
3. Add mini squares at container corners or section intersections.
4. Keep the line system consistent across sections; do not change width per section.
5. Place lines behind content but above the page background.
6. Disable pointer events so the guides never block UI.

## Base Tokens

```css
:root {
  --container-max: 1120px;
  --container-pad: clamp(20px, 4vw, 48px);
  --line-color: rgba(24, 24, 27, 0.14);
  --line-strong: rgba(24, 24, 27, 0.28);
  --corner-size: 6px;
}
```
