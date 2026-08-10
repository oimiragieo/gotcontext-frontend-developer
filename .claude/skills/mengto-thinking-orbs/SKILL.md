---
name: mengto-thinking-orbs
description: Adapter pointer to canonical skills/mengto-thinking-orbs for Claude Code
---

# mengto-thinking-orbs (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-thinking-orbs/SKILL.md`](../../../skills/mengto-thinking-orbs/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-thinking-orbs
description: Add accessible animated AI loading and agent-status indicators with the React thinking-orbs library. Use when a chat, copilot, voice, search, generation, or tool-running interface needs a semantic working, searching, solving, listening, composing, or shaping state; when replacing a generic spinner with an AI activity orb; or when implementing the library's size, theme, speed, pause, reduced-motion, and canvas behavior.
---

# Thinking Orbs

## Core Contract

1. Use `thinking-orbs` in React 18+ interfaces that need indeterminate AI activity feedback.
2. Map the real product lifecycle to one of the six shipped states.
3. Use only the tuned `20` or `64` pixel size. Do not stretch one preset into another.
4. Keep `theme="auto"` unless the surrounding surface has a known fixed theme.
5. Pair the orb with concise visible status text when the activity matters to the user.
6. Override `aria-label` with a task-specific label, or hide the orb from assistive technology when adjacent live text already announces the same state.
7. Use `paused` to freeze the current frame. Do not simulate pause with `speed={0}`.
8. Treat the orb as indeterminate feedback, never as a progress percentage or completion signal.

The package renders monochrome dots on a transparent 2D canvas. It does not expose custom colors, arbitrary sizes, or determinate progress.

## Install

Inspect the project package manager, then install:

```bash
npm install thinking-orbs
```

The package declares `react` and `react-dom` version 18 or newer as peer dependencies. Import the component and exported types from the package root:

```
