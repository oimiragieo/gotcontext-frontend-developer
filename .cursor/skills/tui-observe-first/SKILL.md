---
name: tui-observe-first
description: Adapter pointer to canonical skills/tui-observe-first for Cursor
---

# tui-observe-first (Cursor adapter)

Canonical skill: [`../../../skills/tui-observe-first/SKILL.md`](../../../skills/tui-observe-first/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: tui-observe-first
description: >-
  Use when building, fixing, polishing, or comparing any terminal UI —
  ratatui/crossterm REPLs, agent CLI chrome — or when a TUI shows a frozen
  spinner, dead keys, duplicated responses, stale cells, flicker, resume
  failures on dangling tool_use, or when you need side-by-side screenshots
  against reference CLIs.
---

# TUI observe-first

A TUI is judged **rendered in a real terminal**, never from its source. Render
it, screenshot it, compare it against strong CLIs at the **same terminal grid**,
and cite a screenshot for every finding and fix. Terminal sibling of
`ui-fix-observe-first`.

## The comparative loop

1. **Reference set**: spawn the CLIs you must beat (e.g. claude, codex, droid)
   and your TUI in the **same** rendering stack and viewport. Reuse the same
   browser/PTY tab for every capture — a resized tab makes an unfair comparison.
2. **Capture the same CUJ moments**: welcome, empty composer, slash palette,
   streaming/working, tool receipts, permission dialog, error, interrupt, quit.
3. **Teardown**: every finding cites a screenshot. No screenshot = not a finding.
   Rank by impact; fix one issue-class at a time.
4. **Re-render after every rebuild**, then dogfood real turns (tools, interrupts).
   Many worst bugs only appear live.

## What a strong agent TUI usually has
```
