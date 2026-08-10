---
name: mengto-staggered-word-reveal
description: Adapter pointer to canonical skills/mengto-staggered-word-reveal for Claude Code
---

# mengto-staggered-word-reveal (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-staggered-word-reveal/SKILL.md`](../../../skills/mengto-staggered-word-reveal/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-staggered-word-reveal
description: Create subtle editorial word-by-word text reveal animations where each word fades and rises into place once it enters the viewport. Use for premium portfolio headlines, hero copy, section intros, and short marketing text that needs a cinematic staggered reveal with IntersectionObserver or in-view detection.
---

# Staggered Word Reveal

## Use When
- A short headline, intro, or pull quote should reveal word by word.
- The motion should feel editorial, premium, and restrained.
- The reveal should trigger only once when the text enters the viewport.
- The project does not need heavy GSAP SplitText behavior.

## Motion Defaults
- Initial state: `opacity: 0`, `transform: translateY(20px)`.
- Final state: `opacity: 1`, `transform: translateY(0)`.
- Duration: `0.8s`.
- Ease: `cubic-bezier(0.16, 1, 0.3, 1)`.
- Stagger: `0.06s` to `0.08s` per word. Default to `0.07s`.
- Trigger: start around `20%` visible, with a slight lower viewport bias.
- Replay: once only.

## HTML

```html
<h1 class="word-reveal" data-word-reveal>
  Build interfaces that feel calm, cinematic, and alive.
</h1>
```

```
