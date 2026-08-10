---
name: mengto-matterjs
description: Adapter pointer to canonical skills/mengto-matterjs for Cursor
---

# mengto-matterjs (Cursor adapter)

Canonical skill: [`../../../skills/mengto-matterjs/SKILL.md`](../../../skills/mengto-matterjs/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-matterjs
description: Use when implementing 2D physics interactions with Matter.js, including Engine/World setup, Render/Runner configuration, adding bodies and constraints, and scroll/interaction-friendly canvas scenes.
---

# Matter.js Skill

## Workflow
1. Confirm environment (plain HTML, React, or canvas-only) and rendering approach (Matter.Render for debug vs custom renderer).
2. Provide a minimal Engine/World/Render/Runner setup and add bodies.
3. Add interactions (mouse constraint) or constraints only if requested.
4. Share cleanup steps for SPA or teardown scenarios.

## Minimal setup
```html
<script>
  const { Engine, Render, Runner, Bodies, Composite } = Matter;

  const engine = Engine.create();

  const render = Render.create({
    element: document.body,
    engine: engine,
    options: {
      width: 800,
      height: 600,
      wireframes: false
    }
  });

```
