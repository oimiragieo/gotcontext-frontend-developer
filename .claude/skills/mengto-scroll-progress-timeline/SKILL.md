---
name: mengto-scroll-progress-timeline
description: Adapter pointer to canonical skills/mengto-scroll-progress-timeline for Claude Code
---

# mengto-scroll-progress-timeline (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-scroll-progress-timeline/SKILL.md`](../../../skills/mengto-scroll-progress-timeline/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-scroll-progress-timeline
description: Turn any ordered process into a data-driven vertical or horizontal scroll story with a base line, progress fill, active step states, responsive collapse, semantic fallback, and reduced-motion behavior. Use for onboarding, checkout, roadmaps, recipes, case studies, service processes, histories, or narratives where progress through the sequence should become visible while scrolling.
---

# Scroll Progress Timeline

Use one progress line to connect ordered information. The sequence must remain complete, readable, and navigable before animation is added.

## Model the steps

Keep the content data-driven:

```js
const steps = [
  { id: "brief", number: "01", title: "Set the direction", body: "..." },
  { id: "build", number: "02", title: "Make the system", body: "..." },
  { id: "ship", number: "03", title: "Release and learn", body: "..." }
];
```

Render it as an ordered list with real headings. The line, dots, media, and active state enhance that structure; they do not replace it.

## Build the line

1. Render a quiet base line behind every point.
2. Place one progress line on top with `transform-origin: top` for vertical or `left` for horizontal.
3. Measure the first and last point centers, not arbitrary section edges.
4. Normalize scroll position between those centers.
5. Apply `scaleY(progress)` or `scaleX(progress)` so updates stay on the compositor.
```
