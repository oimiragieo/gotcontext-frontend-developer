---
name: mengto-scroll-scrubbed-visual-sequence
description: Adapter pointer to canonical skills/mengto-scroll-scrubbed-visual-sequence for Cursor
---

# mengto-scroll-scrubbed-visual-sequence (Cursor adapter)

Canonical skill: [`../../../skills/mengto-scroll-scrubbed-visual-sequence/SKILL.md`](../../../skills/mengto-scroll-scrubbed-visual-sequence/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-scroll-scrubbed-visual-sequence
description: Build reversible scroll-controlled visual transformations with a pinned or sticky stage, normalized progress, and video, image-sequence, canvas, SVG, or DOM renderers. Use for hero transformations, product assembly, interface state walkthroughs, object rotation, diagrams, or photo sequences that must move forward and backward with native scrolling.
---

# Scroll-Scrubbed Visual Sequence

Turn one visual transformation into a responsive scroll instrument. Keep the page usable without motion and keep the renderer replaceable.

## Define the sequence

Write the visual states before coding:

```js
const sequence = {
  scrollVh: 280,
  frameCount: 96,
  fit: "contain",
  posterFrame: 0,
  reducedMotionFrame: 95,
  copyStops: [0, 0.42, 0.78]
};
```

Use one normalized value for every renderer:

```js
const progress = Math.min(1, Math.max(0,
  (viewportTop - sectionTop) / (sectionHeight - viewportHeight)
));
```
