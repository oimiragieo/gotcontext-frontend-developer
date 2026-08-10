---
name: mengto-animation-on-scroll
description: Adapter pointer to canonical skills/mengto-animation-on-scroll for Claude Code
---

# mengto-animation-on-scroll (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-animation-on-scroll/SKILL.md`](../../../skills/mengto-animation-on-scroll/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-animation-on-scroll
description: Create an on-scroll animation trigger using IntersectionObserver with Tailwind-friendly animation classes and keyframes. Use when asked for scroll-reveal, animate-on-scroll, or sequencing element animations when they enter the viewport.
---

# Animation On Scroll Skill

## Workflow
1. Confirm animation style, timing, and whether animations should run once or repeat.
2. Provide the keyframes + JS observer snippet and the exact Tailwind class to apply.
3. Offer focused tweaks only (threshold, rootMargin, duration, delay, transform/blur values).

## Usage checklist
- Insert the JS snippet in the `<head>` after the keyframes.
- Add the animation class and `animate-on-scroll` to elements.
- Ensure your keyframes name matches the Tailwind animation reference.

## IntersectionObserver trigger
```html
<script>
  /*
    Sequence animation on scroll when visible. Requires Animation Keyframe. Usage:

    1) Insert this code in the <head> along with the Animation Keyframe code.

    2) Add to Tailwind Classes: [animation:animationIn_0.8s_ease-out_0.1s_both] animate-on-scroll
  */
  (function () {
    // Inject CSS for paused/running states
    const style = document.createElement("style");
```
