---
name: tui-observe-first
description: Adapter pointer to canonical skills/tui-observe-first for Claude Code
---

# tui-observe-first (Claude Code adapter)

Canonical skill: [`../../../skills/tui-observe-first/SKILL.md`](../../../skills/tui-observe-first/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: tui-observe-first
description: Use when building, fixing, polishing, or comparing any terminal UI — ratatui/crossterm REPLs, agent CLI chrome (hydron, claude-code-like TUIs) — or when a TUI shows a frozen spinner/dead keys during turns, duplicated responses, stale cells bleeding through, flicker, a resume wedged on API 400 tool_use-without-tool_result, or when you need screenshots of a TUI on Windows / a side-by-side vs Claude Code, codex, or droid.
---

# TUI observe-first

## Overview

A TUI is judged **rendered in a real terminal**, never from its source. Render
it, screenshot it, compare it against the best CLIs at the **same terminal
grid**, and cite a screenshot for every finding and every fix. The terminal
sibling of `ui-fix-observe-first`; proven by the 2026-07-20 hydron redesign
(11 screenshot-cited findings → all closed; 4 load-bearing bugs found only by
rendering, zero by reading code).

## The comparative loop

1. **Reference set**: spawn the CLIs you must beat (claude, droid, codex) AND
   your TUI in omega-vision tmux sessions, attached in Chrome — one rendering
   stack, one viewport. Reuse the SAME browser tab for every capture; the PTY
   grid follows the tab viewport, so a new/resized tab = an unfair comparison
   (a docked DevTools once shrank the viewport to 389px silently).
2. **Capture the same CUJ moments for each**: welcome screen, empty composer,
   slash palette, streaming/working state, tool receipts, permission/question
   dialog, error, interrupt, quit.
3. **Teardown**: every finding cites a screenshot ID. No screenshot = not a
   finding. Rank by impact; fix ONE issue-class at a time.
4. **Re-render after every rebuild** and verify the fix AND no regressions.
   Then dogfood the real flows end-to-end (real turns, real tool calls, real
```
