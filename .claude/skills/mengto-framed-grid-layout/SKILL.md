---
name: mengto-framed-grid-layout
description: Adapter pointer to canonical skills/mengto-framed-grid-layout for Claude Code
---

# mengto-framed-grid-layout (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-framed-grid-layout/SKILL.md`](../../../skills/mengto-framed-grid-layout/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-framed-grid-layout
description: Create minimal framed grid layouts with thin visible boundary lines, L-shaped corner brackets, subtle diagonal line texture, and strict section alignment. Use when asked for clean, neutral, precise, structured, editorial, technical, or guide-border web layouts.
---

# Framed Grid Layout

## Use When
- A page needs a clean technical structure with visible section boundaries.
- Content should feel precise, organized, editorial, or system-like.
- The design calls for thin guide borders, L-shaped corner brackets, and consistent framed boxes.

## Layout Rules
1. Define the parent grid first; make every section snap to the same columns and rows.
2. Use one border color, one corner bracket color, and one spacing scale across the page.
3. Keep frames rectangular and precise. Avoid floating cards, soft blobs, and uneven margins.
4. Use thin lines: `1px` borders, low-contrast dividers, and subtle bracket marks.
5. Add diagonal background texture at very low opacity; it should read only as surface tension.
6. Align section padding, headings, controls, and media edges to the same grid rhythm.
7. Separate sections with consistent gaps, not random whitespace.

## Base Tokens
Use neutral colors and tune contrast per theme.

```css
:root {
  --fg-bg: #f7f7f4;
  --fg-surface: rgba(255, 255, 255, 0.62);
  --fg-line: rgba(24, 24, 27, 0.14);
  --fg-line-strong: rgba(24, 24, 27, 0.34);
```
