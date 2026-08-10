---
name: mengto-aura-asset-images
description: Adapter pointer to canonical skills/mengto-aura-asset-images for Cursor
---

# mengto-aura-asset-images (Cursor adapter)

Canonical skill: [`../../../skills/mengto-aura-asset-images/SKILL.md`](../../../skills/mengto-aura-asset-images/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-aura-asset-images
description: "Use when you need high-quality stock-style images from Aura Assets (aura.build/assets) similar to Unsplash for design mockups and marketing: backgrounds, abstract wallpapers, architecture, portraits, and headshots. Includes a workflow for searching by tag on aura.build/assets and returns 5 real image URLs per category plus practical guidance for using different resolutions and aspect ratios."
---

# Aura Asset Images (Unsplash-style)

Aura has a big searchable asset library at:
- https://www.aura.build/assets

Use it like Unsplash: search by tag, pick 5 strong candidates, and return direct image URLs.

## How to search (fast)
1) Open: https://www.aura.build/assets
2) Use the search box or URL query:
   - `https://www.aura.build/assets?q=<tag>&order=popular`
3) Tags that work well: `background`, `abstract`, `architecture`, `portrait`, `headshot`

## URL formats (what to return)
Aura thumbnails commonly look like:

```
https://hoirqrkdgbmvpwutwuwj.supabase.co/storage/v1/object/public/assets/assets/<UUID>_800w.jpg
```

### Higher-res (recommended)
Many images support a larger variant by swapping:
- `_800w` → `_1600w`

Example:
```
