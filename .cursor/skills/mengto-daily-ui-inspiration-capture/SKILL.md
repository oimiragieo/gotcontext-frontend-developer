---
name: mengto-daily-ui-inspiration-capture
description: Adapter pointer to canonical skills/mengto-daily-ui-inspiration-capture for Cursor
---

# mengto-daily-ui-inspiration-capture (Cursor adapter)

Canonical skill: [`../../../skills/mengto-daily-ui-inspiration-capture/SKILL.md`](../../../skills/mengto-daily-ui-inspiration-capture/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-daily-ui-inspiration-capture
description: Create a recurring daily UI inspiration capture. Use when the user asks to run, refresh, package, or validate dated UI inspiration bundles, especially for `articles/YYYY-MM-DD-ui-inspiration-capture/` outputs, Framer/Dribbble landing-page inspiration, motion-study screenshots/videos, AI-builder prompts, duplicate checking, or converting a project runbook into repeatable workflow.
---

# Daily UI Inspiration Capture

## Overview

Run the current project's daily UI inspiration workflow as an article-ready bundle, not a screenshot dump or README. Treat the active project runbook as source of truth, but keep the contract below as the default unless the user updates it.

## Start

Work from the content/article project named by the user. If no project is named, use the current workspace and say which directory you used.

Before collecting, read:

- `AGENTS.md`, if present or supplied in the prompt
- `scripts/ui-inspiration-capture-guidelines.md`, if present
- the latest one or two `articles/*-ui-inspiration-capture/content.md` and `manifest.json` files for current shape

Check `git status --short` early. This repo is often dirty; keep changes scoped to the requested dated bundle or skill files.

For any browser work, use the Codex in-app browser only. Do not use Chrome. If a source blocks inspection, use the best available Codex-browser evidence or local asset fallback and say why.

## Output Contract

Create a dated folder:

```text
```
