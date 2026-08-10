---
name: mengto-masked-reveal
description: Adapter pointer to canonical skills/mengto-masked-reveal for Claude Code
---

# mengto-masked-reveal (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-masked-reveal/SKILL.md`](../../../skills/mengto-masked-reveal/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-masked-reveal
description: Create masked staggered word reveals on scroll with GSAP ScrollTrigger. Use when headings, hero copy, section titles, or editorial text should reveal word-by-word through an overflow mask as they enter the viewport.
---

# Masked Reveal

## Use When
- A headline or short text block needs a premium reveal on scroll.
- Words should rise through an invisible mask with a staggered sequence.
- The project already uses GSAP or needs ScrollTrigger-based motion.

## Motion Defaults
- Trigger: start when the text top reaches `82%` of the viewport.
- Duration: `0.7s` to `0.9s`.
- Stagger: `0.025s` to `0.045s` per word.
- Offset: `yPercent: 110` to `0`.
- Ease: `power3.out` or `expo.out`.
- Replay: reveal once by default.

## HTML

```html
<h1 class="masked-reveal" data-masked-reveal>
  Design systems that feel alive from the first scroll.
</h1>
```

## CSS Mask

```
