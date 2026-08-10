---
name: mengto-liquid-metal-border
description: Adapter pointer to canonical skills/mengto-liquid-metal-border for Claude Code
---

# mengto-liquid-metal-border (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-liquid-metal-border/SKILL.md`](../../../skills/mengto-liquid-metal-border/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-liquid-metal-border
description: Add and tune animated liquid-metal WebGL borders with the React `metal-fx` package. Use when buttons, icon controls, chips, tabs, cards, or selected surfaces need a metallic active, selected, hover, focus, or premium border; when implementing the MetalFx component from metal.jakubantalik.com; or when troubleshooting its presets, themes, strength, glow, reflections, sizing, radius, animation, accessibility, SSR, or performance.
---

# Liquid Metal Border

## Core Contract

1. Use `metal-fx` in React 18 or newer.
2. Wrap exactly one real host element such as a `button`, `a`, `div`, or `article`.
3. Keep the host semantic and interactive. `MetalFx` is visual framing, not the control.
4. Reserve the animated border for active, selected, focused, hovered, or primary surfaces. Do not put it around every control.
5. Keep a static CSS border or focus outline as the fallback. WebGL decoration must never carry essential state by itself.
6. Pause non-active instances and reduced-motion experiences.
7. Test light and dark modes independently. Reflections intentionally render only in dark mode.

## Inspect Before Editing

- Confirm the project uses React and has `react` and `react-dom` version 18 or newer.
- Find the real control, its dimensions, radius, background, border, outline, shadow, active-state source, and theme source.
- Decide whether the metal should be always visible or driven by `active`, `selected`, hover, or focus state.
- Check whether the project has a manual theme toggle. Use that state instead of `theme="auto"` when it does not follow the OS.
- Identify nearby elements that genuinely benefit from reflected light. Do not add reflections by default.
- Check the installed `metal-fx` version before relying on the prop surface below.

## Install and Import

Install with the project's package manager:

```
