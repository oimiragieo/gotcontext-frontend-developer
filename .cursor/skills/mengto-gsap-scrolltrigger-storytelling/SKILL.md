---
name: mengto-gsap-scrolltrigger-storytelling
description: Adapter pointer to canonical skills/mengto-gsap-scrolltrigger-storytelling for Cursor
---

# mengto-gsap-scrolltrigger-storytelling (Cursor adapter)

Canonical skill: [`../../../skills/mengto-gsap-scrolltrigger-storytelling/SKILL.md`](../../../skills/mengto-gsap-scrolltrigger-storytelling/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-gsap-scrolltrigger-storytelling
description: "Build cinematic sticky product storytelling with GSAP ScrollTrigger, progressive UI reveals, scroll-synced animation, smooth interpolation, and immersive section transitions."
---

# GSAP ScrollTrigger Storytelling Skill

## Use When
- Build cinematic sticky product storytelling with GSAP ScrollTrigger, progressive UI reveals, scroll-synced animation, smooth interpolation, and immersive section transitions.

## Workflow

## Scope
- Apply this when the page should feel like a scroll-driven product story rather than a static marketing layout.
- Use GSAP ScrollTrigger as the main choreography layer for sticky sections, progressive interface reveals, pinned scenes, scrubbed timelines, and immersive transitions between sections.
- Preserve the actual product narrative and interface clarity. The motion should amplify comprehension, not hide basic content behind theatrical effects.

## Experience target
- Create sticky product storytelling where each scroll segment reveals a new product state, feature layer, data view, device frame, or workflow step.
- Use scroll-synced animation so copy, UI panels, screenshots, overlays, and background atmosphere move together as one authored sequence.
- Build progressive UI reveals: draw in frames, fade in controls, slide panels into place, count values up, highlight regions, and swap states as the user advances.
- Keep the overall mood cinematic, premium, and immersive with controlled pacing, clean staging, depth, and transitions that feel intentional.

## Implementation guidance
- Use GSAP timelines with ScrollTrigger `scrub` for the main scroll narrative and regular tweens only for supporting entrance or hover motion.
- Pin long-form story sections with `pin: true` and map each scene to explicit timeline labels so the sequence is easy to tune.
- Prefer transform and opacity animation over layout-affecting properties. Use `will-change` sparingly on animated elements that actually need it.
- Use `gsap.context()` in React components and clean it up on unmount so ScrollTriggers are killed correctly.
- Refresh ScrollTrigger after images, fonts, or async content load if those assets affect section height or pinned offsets.
- Use `matchMedia()` or equivalent breakpoints so desktop sticky choreography can simplify gracefully on smaller screens.
```
