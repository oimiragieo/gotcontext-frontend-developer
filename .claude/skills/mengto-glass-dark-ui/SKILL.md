---
name: mengto-glass-dark-ui
description: Adapter pointer to canonical skills/mengto-glass-dark-ui for Claude Code
---

# mengto-glass-dark-ui (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-glass-dark-ui/SKILL.md`](../../../skills/mengto-glass-dark-ui/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-glass-dark-ui
description: Build dark-mode glassmorphism interfaces with readable contrast, frosted surfaces, and gradient borders using a pseudo-element mask. Use when asked for glass cards, frosted dark hero sections, blur panels, or dark UI systems with gradient/glow borders.
---

# Glass Dark UI Skill

## Workflow
1. Confirm environment (`HTML/CSS`, Tailwind, or React) and target surface (`hero`, `dashboard`, `modal`, `card`).
2. Define dark UI tokens first (background, glass fill, border glow, primary text, muted text).
3. Build frosted panels with `backdrop-filter`, transparent dark fill, and subtle inner highlight.
4. Apply the masked gradient border (`.border-gradient::before`) to key surfaces.
5. Add restrained depth (shadow + glow) and clear hover/focus states.
6. Validate contrast and mobile behavior before finalizing.

## Base Tokens
Use these as defaults and tune per brand.

```css
:root {
  --bg-0: #020617;
  --bg-1: #0b1220;
  --glass-fill: rgba(15, 23, 42, 0.45);
  --glass-fill-strong: rgba(15, 23, 42, 0.62);
  --text-main: #e2e8f0;
  --text-muted: #94a3b8;
  --accent: #60a5fa;
}
```

```
