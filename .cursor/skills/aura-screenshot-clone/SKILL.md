---
name: aura-screenshot-clone
description: Adapter pointer to canonical skills/aura-screenshot-clone for Cursor
---

# aura-screenshot-clone (Cursor adapter)

Canonical skill: [`../../../skills/aura-screenshot-clone/SKILL.md`](../../../skills/aura-screenshot-clone/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: aura-screenshot-clone
description: "Use when the user wants to clone or adapt a UI pattern from any website into gotcontext.ai, or asks to \"build something like X\", \"make our nav look like Y\", or \"clone that component\". Requires an aura.build Pro subscription. Aura's clone is now NATIVE — paste a URL or drag a screenshot into aura.build and it generates React/Tailwind directly; the Anima/Chrome-extension flow is only a fallback for login-gated pages Aura can't fetch server-side."
---

# Aura Screenshot-to-Component Pipeline

## Overview

Full pipeline for cloning any web UI pattern into a gotcontext.ai React/Next.js component: paste a URL or drag a screenshot into aura.build → it generates React/Tailwind directly → adapt in Claude Code. The user points at a reference; you handle everything else.

> **Clone primitive (updated 2026-06-06, per `docs/audits/2026-06-06-ui-ux-design-pipeline-playbook.md` gap #3):** Aura's clone is **NATIVE** — paste a URL or drag in a screenshot and Aura converts it to React-mode components in-app. No Chrome browser extension is required for the core flow. The Anima/Chrome-extension path is only a **fallback for login-gated pages** Aura can't fetch server-side (use the screenshot-upload path below). Figma export (Phase 3) is optional/downstream for design review only.

**Core principle:** Never write layout from scratch when you can URL-import / screenshot → convert → adapt. AI vision at ~90% in one shot; you spend effort only on the 10% that makes it uniquely gotcontext.ai.

> This is one branch of the broader design-to-code router (**Path 1C**). Sibling paths:
> - **1A** Claude Design → `claude-design`
> - **1B** Figma SoT → Figma MCP / `figma-design-to-code`
> - **1C** Clone reference URL/screenshot → **this skill** (`aura-screenshot-clone`)
> - **1D** Google Stitch MCP (NL → high-fi screens → code) → `stitch-mcp-design`
>
> Use Stitch when you are **authoring** a new UI in Stitch, not when cloning an existing live site (Aura).

---

## Decision gate — which input path to use

Before anything else, pick the **input path** to aura. Two options, order of preference:

1. **URL import (preferred)** — aura fetches and screenshots the reference itself. Skip manual screenshots entirely. **Fails on sites that block server-side fetches** (Cloudflare, anti-bot WAFs, login-walled content). Known to fail: `artificialanalysis.ai`, `openrouter.ai`, many high-traffic SaaS comparison sites. Known to work: most marketing pages (Anthropic, Vercel, Stripe, GitHub pricing), Wikipedia, blog posts.
```
