---
name: uupm-banner-design
description: Adapter pointer to canonical skills/uupm-banner-design for Claude Code
---

# uupm-banner-design (Claude Code adapter)

Canonical skill: [`../../../skills/uupm-banner-design/SKILL.md`](../../../skills/uupm-banner-design/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: uupm-banner-design
description: "Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with AI-generated visuals. Actions: design, create, generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero, print. Styles: minimalist, gradient, bold typography, photo-based, illustrated, geometric, retro, glassmorphism, 3D, neon, duotone, editorial, collage. Uses ui-ux-pro-max, frontend-design, ai-artist, ai-multimodal skills."
argument-hint: "[platform] [style] [dimensions]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---

# Banner Design - Multi-Format Creative Banner System

Design banners across social, ads, web, and print formats. Generates multiple art direction options per request with AI-powered visual elements. This skill handles banner design only. Does NOT handle video editing, full website design, or print production.

## When to Activate

- User requests banner, cover, or header design
- Social media cover/header creation
- Ad banner or display ad design
- Website hero section visual design
- Event/print banner design
- Creative asset generation for campaigns

## Prerequisites

**Python:** This skill uses Python scripts. On Windows, use `python` instead of `python3` (e.g., `python scripts/search.py` instead of `python3 scripts/search.py`).

## Workflow

### Step 1: Gather Requirements (AskUserQuestion)
```
