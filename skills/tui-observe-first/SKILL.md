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
   interrupts) — 4 of hydron's worst bugs only appeared in live turns.

## What a best-in-class agent TUI has

| Element | Shape (learned from claude + droid) |
|---|---|
| Welcome header | Logo glyph + name/version bold, model · permission-mode, cwd · session — 3-4 lines, scrolls away |
| Bottom bar | Two-sided: mode pill + key hints left; model · session · $cost · ctx% right |
| Working line | Spinner + verb + elapsed + `(esc to interrupt)` + queued count, above the input |
| Turn receipt | One whimsy-dim line per turn (`✦ Fused in 6s`) |
| Tool receipts | `⎿` connector, green ✓ / red ✗ / spinner while running; collapsed summaries, never raw output |
| Text rendering | Markdown-lite: bold, accent inline code, tinted fenced blocks with hidden ``` fences |
| Palette | Alphabetical on bare `/`, ranked on query; `❯` selected row; aliases dim |
| Dialogs | Rounded accent border, `❯` selection + numeric quick keys + y/n, dim hint row |
| Input | Accent `❯`, dim italic placeholder, thin rules — never status text inside the input line |
| Flow | Type-to-queue while running; Esc interrupts (never quits); Ctrl+C arms quit (2nd press ≤2s) |

## Render-loop laws (violations found live, not in review)

Freeze triage from symptom alone: **keyboard dead too ⇒ lock contention in
the render loop; keys work but spinner/elapsed frozen ⇒ a turn started
without stamping its start time.**

- **Never await a shared engine/session lock in the render loop.** The turn
  task holds it for the whole turn → spinner, timer, AND keyboard freeze until
  the turn ends. Clone inner `Arc` handles out (e.g. an ask-bridge) and poll
  with `try_lock`. (hydron: `run_loop`, `crates/hydron-repl/src/tui.rs`.)
- **Every new-turn path goes through one `begin_turn()`** that stamps the
  start time. A path that sets `status = Running` directly renders a frozen
  0s spinner forever — hydron's autopoll branch shipped exactly this.
  (hydron: `ReplApp::begin_turn`, `crates/hydron-repl/src/app.rs`.)
- **A turn has TWO independent completion signals** — the task/join handle
  and the unbounded event channel — and they race. Drain the channel before
  finalizing, or leftover stream deltas arriving after the receipt line start
  a duplicate response block. (hydron: tail-drain before `finish_assistant`
  in `run_loop`.)
- **`Clear` the full frame before drawing.** ratatui `Paragraph`/`Block` set
  styles, not symbols — pre-launch pane content bleeds through empty cells.
- **Set the terminal cursor explicitly** (`set_cursor_position`) from the
  edit-cursor column; browser PTYs show no caret otherwise.
- **Repair histories at session load**: for each dangling `tool_use` id
  (kill mid-tool ⇒ every resume 400s otherwise) insert a synthetic
  `is_error:true` tool_result saying no result was recorded — merged into an
  existing partial-result user turn when one exists, else as a new user turn.
  In hydron: `repair_dangling_tool_use` in
  `crates/hydron-session/src/lib.rs`, applied inside both load choke points
  (`SessionStore::load_messages`, `load_messages_from_path`) so every resume
  surface (CLI `--continue`/`--resume`, REPL `/resume`) self-heals.
- **TestBackend-test every layout/keyboard change** (buffer_text scan +
  cursor position asserts) — but treat those as gates, not proof; only the
  rendered screenshot proves a visual claim.

## Windows rendering mechanics (hydron ⇄ omega-vision)

Cheap first look: `cargo run -p hydron` in Windows Terminal — fastest smoke
test, but NOT the comparison rig (different font/grid/renderer than the
browser-attached PTY the references run in).

First-class path: `cd omega-vision/orchestrator && npm run hydron:build`
(Linux binary via rust bookworm image = container-glibc parity), then
`POST :8090/sessions {"profile":"hydron"}` and `npm run hydron:dogfood` for
the scripted regression. Raw loop when no profile fits (any repo/binary):

```bash
MSYS_NO_PATHCONV=1 docker run --rm -v "C:/dev/projects/<repo>:/src" \
  -v <name>-cargo-registry:/usr/local/cargo/registry -v <name>-target:/target \
  -w /src -e CARGO_TARGET_DIR=/target rust:1-bookworm \
  bash -c "cargo build --release -p <bin> && cp /target/release/<bin> /src/<bin>-linux"
# spawn profile "basic", run the binary from the /projects mount, screenshot
# the attach page (localhost:8090/?termid=…) via claude-in-chrome
```

Traps that cost real time:
- WSL-built binaries can need a NEWER glibc than the container (`ldd
  --version` of the distro ≠ what rustc links) — build in the matching
  bookworm image; musl needs `musl-tools` you may not have.
- omega-vision `POST /sessions/:id/input {"text":…}` **auto-submits** unless
  `"submit":false`; MCP `send_keys` takes an **array** (`{"keys":["Enter"]}`)
  and the HTTP MCP endpoint needs `Accept: application/json, text/event-stream`.
- The container has no `pkill` — kill via `/proc` scan of `readlink
  /proc/$pid/exe`.
- `GET :8090/scrollback?termid=…` is ground truth when a screenshot looks
  stale; the profile `ready_regex`
  (`omega-vision/orchestrator/capabilities/<profile>.yaml`) must match what
  the CURRENT UI prints — a redesign silently broke hydron's
  `'Hydron REPL'` regex and timed out every `wait_for_ready` spawn.
- Cargo package ≠ directory name: `cargo test -p hydron_repl` (underscore),
  directory `crates/hydron-repl`.
- `cargo test | tail` eats the exit code — capture to a file, check `$?`.
- **The browser attach page swallows keys** (Escape, sometimes Ctrl-chords):
  a "keyboard bug" observed through Chrome typing is a RIG ARTIFACT until
  reproduced against the raw PTY (`send_keys` MCP with `{"keys":["Escape"]}`
  + scrollback read). Receipt 2026-07-21: "Escape doesn't clear the slash
  composer" was about to be fixed in code that was already correct — the
  PTY reproduction showed the composer clearing perfectly. Keyboard findings
  need a PTY-level repro before any code change.

## Common mistakes

| Mistake | Reality |
|---|---|
| "It compiles / tests pass, ship it" | 4 of hydron's worst TUI bugs had green tests. Render + dogfood live turns. |
| Diagnosing look/flow from the source | Freeze, bleed-through, grid width, and timing bugs do not exist in code. |
| Comparing screenshots from different tabs/sizes | PTY grid follows the viewport; same tab, same size, every capture. |
| Restyling without a reference set | "Better" is relative — capture claude/droid first, then rank gaps. |
| Blaming your change for a failing host test | Baseline it on clean HEAD first (hermetic-test trap: tests that ingest operator-real state false-fail locally). |

## Cross-references

- `ui-fix-observe-first` — the web sibling (render → measure → cite → fix).
- `use-omega-vision` — session substrate, HTTP/MCP surface details.
- Hydron receipts: `Docs/05-ui/cli-tui.md` §6/§12, memory
  `project_tui_redesign_2026_07`, commits `00aa8cb`/`e5bd9d3`.
