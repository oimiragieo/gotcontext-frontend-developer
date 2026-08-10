---
name: mengto-progressive-blur
description: Adapter pointer to canonical skills/mengto-progressive-blur for Claude Code
---

# mengto-progressive-blur (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-progressive-blur/SKILL.md`](../../../skills/mengto-progressive-blur/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-progressive-blur
description: Create a layered CSS progressive blur (top or bottom) using multiple backdrop-filter masks for depth and softness. Use when asked for “progressive blur”, “gradient blur overlay”, or stepped blur masks that fade from an edge of the viewport.
---

# Progressive Blur Skill

## Workflow
1. Confirm placement (top or bottom), height, and z-index relative to UI.
2. Provide the matching snippet and a short usage checklist.
3. Offer only targeted tweaks (height, blur steps, direction, opacity stops).

## Usage checklist
- Insert the HTML inside `<body>`.
- Keep the `.gradient-blur` element near the top of the DOM.
- Ensure the background behind it exists (backdrop-filter blurs what is behind).
- Adjust `z-index` to sit above content but below modals.

## Top blur (from top)
```html
<div class="gradient-blur">
  <div></div><div></div><div></div><div></div><div></div><div></div>
</div>
<style>
  .gradient-blur {
    position: fixed;
    z-index: 5;
    inset: 0 0 auto 0;
    height: 12%;
    pointer-events: none;
```
