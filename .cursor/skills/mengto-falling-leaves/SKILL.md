---
name: mengto-falling-leaves
description: Adapter pointer to canonical skills/mengto-falling-leaves for Cursor
---

# mengto-falling-leaves (Cursor adapter)

Canonical skill: [`../../../skills/mengto-falling-leaves/SKILL.md`](../../../skills/mengto-falling-leaves/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-falling-leaves
description: Build falling leaves that read as leaves, with each one tumbling on its own axis so it presents a face, thins to an edge, and opens out again, and with its sideways slip driven by that same tumble. Covers the 2-D canvas build and the instanced-3-D variant, where leaves are recycled from, density-versus-count maths, depth layering, colour under a tone-mapped composite, reduced motion, and visibility pausing. Use for autumn maple, sakura petals, blossom, ash, snowfall shapes, or any drifting foliage where a generic particle field reads as confetti.
---

# Falling Leaves

Make the falling thing read as a leaf. Reach for `ambient-section-particles` when you want a bounded atmosphere of generic motes. Reach for this when the shape has to be recognisable.

## Build the tumble first

Turn each leaf about its own long axis so it shows its face, thins to nothing edge-on, then opens out on the other side. That instant of near-disappearance is what the eye reads as "leaf". A sprite that only spins in the picture plane reads as confetti, a coin, or a paper scrap, however good the artwork is.

On 2-D canvas the tumble is a horizontal scale that crosses zero:

```js
ctx.save();
ctx.translate(l.x, l.y);
ctx.rotate(l.roll);              // long axis drifting in-plane
ctx.scale(Math.cos(l.spin), 1);  // the tumble: cos crosses 0, edge-on
ctx.globalAlpha = l.alpha;
ctx.drawImage(sprite, -w / 2, -h / 2, w, h);
ctx.restore();
```

Drive two axes, not one. `roll` turns the leaf within the picture plane; `spin` turns it through the plane. Give each its own rate per leaf, or the motion reads as mechanical however you ease it.

In 3-D, instance **quads**, never point sprites. A point sprite always faces the camera and can never turn away, so it can never go edge-on. That single constraint decides the whole implementation.

## Couple the slip to the tumble
```
