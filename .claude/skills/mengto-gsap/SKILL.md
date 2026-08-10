---
name: mengto-gsap
description: Adapter pointer to canonical skills/mengto-gsap for Claude Code
---

# mengto-gsap (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-gsap/SKILL.md`](../../../skills/mengto-gsap/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-gsap
description: Use when you need to add or debug professional web animations with GSAP (timelines, ScrollTrigger, stagger, transforms) in HTML/CSS/JS/React. Includes patterns for smooth motion, performance, and common pitfalls.
---

# GSAP (GreenSock) — Web Animation Skill

## When to use
- High-quality UI/motion design: entrances, micro-interactions, page transitions
- Timeline-based sequences (vs. scattered CSS transitions)
- Scroll-driven storytelling (with ScrollTrigger)
- Complex easing, staggering, orchestration across many elements

## Key concepts & APIs
- Tweens:
  - `gsap.to(targets, vars)`
  - `gsap.from(targets, vars)`
  - `gsap.fromTo(targets, fromVars, toVars)`
- Timelines:
  - `const tl = gsap.timeline({ defaults, repeat, yoyo, paused })`
  - Chain: `tl.to(...).from(...).addLabel('x').add(() => ...)`
  - Position parameter: absolute `1.2`, relative `"+=0.5"`, overlap `"-=0.3"`, label `"intro"`
- Eases: `ease: "power2.out"`, `"expo.inOut"`, `"elastic.out(1, 0.3)"`
- Staggers: `stagger: 0.05` or `{ each, from: "start|center|end|random", grid }`
- Performance-friendly properties:
  - Prefer transforms (`x`, `y`, `scale`, `rotation`) and opacity (`autoAlpha`)
- ScrollTrigger (plugin):
  - `gsap.registerPlugin(ScrollTrigger)`
  - Inline: `gsap.to(".box", { scrollTrigger: ".box", x: 500 })`
  - Advanced: `scrollTrigger: { trigger, start, end, scrub, pin, snap, markers }`
```
