---
name: mengto-optimize-web-animations
description: Adapter pointer to canonical skills/mengto-optimize-web-animations for Cursor
---

# mengto-optimize-web-animations (Cursor adapter)

Canonical skill: [`../../../skills/mengto-optimize-web-animations/SKILL.md`](../../../skills/mengto-optimize-web-animations/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-optimize-web-animations
description: Profile, audit, and optimize frontend page performance with emphasis on animation work, memory-leak risks, long-session slowdowns, CSS animations, canvas/WebGL requestAnimationFrame loops, marquees, skeletons, GSAP/Three/Matter effects, timers, listeners, and observers. Use when the user asks to make animations performant, pause offscreen animations, look for memory leaks, profile pages that slow the computer over time, fix janky scrolling, reduce CPU/GPU use, or repeat the "only play in view" optimization on React/Vite/Next/frontend pages using Codex Browser.
---

# Optimize Web Animations

## Core Rule

Measure the real page before editing. The goal is not to remove motion; it is to make offscreen work stop, visible motion resume correctly, and route/unmount cleanup release long-lived resources.

Use Codex Browser when available, especially for localhost pages. Do not use Chrome unless the user explicitly asks for it.

## Workflow

1. Inspect repo context.
   - Read `AGENTS.md` or local instructions.
   - Run `git status --short` early.
   - Find page components, animation hooks, CSS keyframes, `requestAnimationFrame`, `setInterval`, `setTimeout`, canvas/WebGL/physics components, media elements, GSAP timelines/tweens, and existing visibility utilities.
   - Search effect cleanup for event listeners, observers, RAF loops, intervals, timers, external scripts, media streams, WebGL textures/materials/geometries/renderers, and async work that can complete after unmount.
   - If the worktree is dirty, plan narrow staging from the start.

2. Capture a baseline in the browser.
   - Open the exact route the user named.
   - Profile at top, mid-page, footer/lower content, and one mobile viewport when layout could differ.
   - Count CSS animations by computed `animationName`, `animationPlayState`, and visibility. Include `::before` and `::after`.
   - Inspect canvases/WebGL elements separately; CSS profiling does not prove RAF loops have stopped.
   - Record which animation names are running offscreen and the DOM owners responsible.
   - For memory/leak asks, also record element/canvas/image/iframe counts, exposed JS heap metrics when available, an idle sample after 10-30 seconds, and a short route-cycle sample. If heap APIs return `null` or the Browser sandbox blocks monkey-patching, say so and rely on stable observable counts plus source audit.
   - Keep stress tests bounded. A Browser tab crash during profiling is evidence of overload, but do not over-attribute the cause unless reproduced by a minimal test.
```
