---
name: claude-design
description: Adapter pointer to canonical skills/claude-design for Claude Code
---

# claude-design (Claude Code adapter)

Canonical skill: [`../../../skills/claude-design/SKILL.md`](../../../skills/claude-design/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: claude-design
description: "Use when generating, prototyping, or iterating on UI designs (prototypes, wireframes, slide decks, landing/dashboard mockups) with Anthropic's Claude Design tool at claude.ai/design — particularly when you want a design system applied automatically and a clean handoff into Claude Code for implementation."
---

# Claude Design — UI generation with prompt + design-system + Claude Code handoff

## Overview

Claude Design (claude.ai/design, Anthropic Labs, launched 2026-04-17, powered by Opus 4.8) is a chat-driven visual canvas. You describe what you want in plain English; Claude generates a working design on the right pane; you iterate via chat or by clicking individual elements to leave inline comments. **A major 2026-06-17 overhaul** repositioned it from a flashy demo into a design-system *compliance layer* with a bidirectional Claude Code round-trip + a fix for its token-burning problem. The standout features for engineering teams:

1. **Org-wide design system (import from GitHub repo / local codebase / design files / raw uploads)** — bring one or several design systems in ONCE; Claude builds with your real components, **checks its output against the system, and auto-corrects before you see it**. A new admin role can approve ONE standard system + lock edits (enterprise brand control).
2. **Bidirectional Claude Code round-trip (the 2026-06-17 headline)** — from a Claude Code terminal: **`/design-sync`** imports your local codebase's design system INTO Claude Design (so prototypes start from real components, not approximations); **`/design`** creates/edits/syncs design projects without leaving the terminal. When a design is ready it hands off to Claude Code, which picks up exactly where you left off — no screenshot, no rebuild. *(This Claude Code environment exposes a `DesignSync` tool for this.)*
3. **Multi-output export + connectors** — standalone HTML, PDF, PPTX, .zip, org-scoped share link (view/comment/edit), or push to a connected app: **Adobe, Base44, Canva, Gamma, Lovable, Miro, Replit, Vercel, Wix** (more added over time).

Available on **Pro / Max / Team / Enterprise**. NOT on Free. Usage now **shares your subscription pool with chat / Cowork / Code** (see Pricing). Still beta — treat as exploratory tooling, not a system of record (no audit logs yet).

## When to use

- Generate a prototype / wireframe / high-fidelity mock from a verbal spec before you commit any engineering
- Build a pitch deck, investor slides, or sales one-pager that needs to look on-brand
- Produce dashboard/landing mockups using your real component library — then hand off to Claude Code with full context
- Explore 3-5 visual directions in parallel for a design crit without burning eng time
- Generate marketing assets (emails, banners, social posts) that match brand

## When NOT to use

- **Cloning a specific reference UI screenshot/URL** → use `aura-screenshot-clone` skill (aura.build Pro is the project's asset source-of-truth)
- **Greenfield high-fi UI from natural language via Google Stitch MCP** → use `stitch-mcp-design` (remote MCP + optional google-labs-code/stitch-skills)
- **Translating an existing Figma file into code** → use `figma:figma-implement-design`
```
