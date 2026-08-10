---
name: mengto-beam-glow-states
description: Adapter pointer to canonical skills/mengto-beam-glow-states for Claude Code
---

# mengto-beam-glow-states (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-beam-glow-states/SKILL.md`](../../../skills/mengto-beam-glow-states/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-beam-glow-states
description: Create React loading, processing, selected, current, focus, and pressed states with the border-beam package's animated edge glow. Use when a card, button, input, tab, option, task panel, or agent surface needs a restrained traveling or breathing beam; includes installation, imports, prop selection, state wiring, reduced motion, accessibility, and performance and layout guardrails.
---

# Beam Glow States

Use the beam as a decorative state accent. Keep the state understandable through text, shape, contrast, and the correct semantic attribute when the animation is absent.

The API below was verified against `border-beam` 1.3.0. Recheck the official README and exported types when the installed version changes.

## Install and import

Install the same package with the repository's package manager:

```bash
npm install border-beam
pnpm add border-beam
yarn add border-beam
bun add border-beam
```

The package requires React and React DOM 18 or newer. It ships ESM, CommonJS, and TypeScript declarations. It injects component-scoped styles, so do not import a separate CSS file.

Prefer the named import:

```tsx
import { BorderBeam } from "border-beam";
import type {
  BorderBeamProps,
```
