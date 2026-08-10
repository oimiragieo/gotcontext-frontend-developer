---
name: clone-website
description: Adapter pointer to canonical skills/clone-website for Cursor
---

# clone-website (Cursor adapter)

Canonical skill: [`../../../skills/clone-website/SKILL.md`](../../../skills/clone-website/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: clone-website
description: "Use when the user wants to clone, replicate, rebuild, reverse-engineer, or copy any website — or says 'make a copy of this site', 'rebuild this page', 'pixel-perfect clone'. Reverse-engineers one or more sites in one shot: extracts assets, CSS, and content section-by-section, then proactively dispatches parallel builder agents in worktrees as it goes (foreman pattern, not inspect-then-build). Provide one or more target URLs as arguments; requires browser automation (Chrome MCP/Playwright/Browserbase/Puppeteer). Pixel-perfect fidelity default: visual layout, styling, components, responsive design, mock data — NOT real backend/auth/real-time/SEO/accessibility unless specified."
argument-hint: "<url1> [<url2> ...]"
user-invocable: true
---

# Clone Website

You are about to reverse-engineer and rebuild **$ARGUMENTS** as pixel-perfect clones.

When multiple URLs are provided, process them independently and in parallel where possible, while keeping each site's extraction artifacts isolated in dedicated folders (for example, `docs/research/<hostname>/`).

This is not a two-phase process (inspect then build). You are a **foreman walking the job site** — as you inspect each section of the page, you write a detailed specification to a file, then hand that file to a specialist builder agent with everything they need. Extraction and construction happen in parallel, but extraction is meticulous and produces auditable artifacts.

## Scope Defaults

The target is whatever page `$ARGUMENTS` resolves to. Clone exactly what's visible at that URL. Unless the user specifies otherwise, use these defaults:

- **Fidelity level:** Pixel-perfect — exact match in colors, spacing, typography, animations
- **In scope:** Visual layout and styling, component structure and interactions, responsive design, mock data for demo purposes
- **Out of scope:** Real backend / database, authentication, real-time features, SEO optimization, accessibility audit
- **Customization:** None — pure emulation

If the user provides additional instructions (specific fidelity level, customizations, extra context), honor those over the defaults.

## Pre-Flight

1. **Browser automation is required.** Check for available browser MCP tools (Chrome MCP, Playwright MCP, Browserbase MCP, Puppeteer MCP, etc.). Use whichever is available — if multiple exist, prefer Chrome MCP. If none are detected, ask the user which browser tool they have and how to connect it. This skill cannot work without browser automation.
2. Parse `$ARGUMENTS` as one or more URLs. Normalize and validate each URL; if any are invalid, ask the user to correct them before proceeding. For each valid URL, verify it is accessible via your browser MCP tool.
```
