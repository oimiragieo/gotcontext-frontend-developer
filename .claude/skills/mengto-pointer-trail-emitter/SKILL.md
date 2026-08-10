---
name: mengto-pointer-trail-emitter
description: Adapter pointer to canonical skills/mengto-pointer-trail-emitter for Claude Code
---

# mengto-pointer-trail-emitter (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-pointer-trail-emitter/SKILL.md`](../../../skills/mengto-pointer-trail-emitter/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-pointer-trail-emitter
description: Build a cursor trail whose spacing stays constant at any hand speed, by emitting motes per unit of distance travelled rather than on a timer, so a flick draws the same continuous ribbon as a crawl instead of breaking into scattered dots. Covers sub-segment placement, the ring-buffer ordering trap, the idle breath a distance emitter needs, anchoring the trail to the screen in a 3-D scene, scaling scatter against the plane it hangs on, coasting instead of stopping dead, touch and reduced-motion fallbacks, and why moving the emitter to a DOM overlay to raise its z-index costs more than it buys. Use for cursor wisps, pointer sparks, embers, magic trails, comet tails, plankton, dust, or any mote trail that must stay legible however fast the hand moves.
---

# Pointer Trail Emitter

Build the emitter yourself when the trail's density has to respond to how fast the hand is moving.

Reach for `add-shader-cursor-trail` or `shaders-cursor-ripples` when you want the packaged WebGPU looks from the Shaders library. Reach for `reveal-hover-effect` when the cursor exposes a second image through a mask. Reach for `ambient-section-particles` when motes fill a section and the pointer only disturbs them. Reach for this when the pointer *lays* them.

Extracted from a dark WebGL night scene where the trail had to stay readable over type and never pull attention from the set behind it.

## Emit by distance, not by time

This is the whole mechanism. Accumulate the distance the emitter has moved and spend it in fixed steps:

```js
E.acc += moved;
let guard = 0;
while (E.acc >= STEP && guard++ < 14) {
  E.acc -= STEP;
  spawn(/* … */);
}
```

Spacing along the path is then `STEP`, whatever the hand is doing, so the trail reads as one continuous ribbon at a crawl and at a flick alike.

Tie emission to a timer instead and spacing becomes proportional to speed — the pointer covers `speed × interval` between spawns. **A flick breaks the line into scattered dots, and a resting hand piles every mote on one spot.** That is the failure this prevents, and it is worth building the toggle to see it once.

```
