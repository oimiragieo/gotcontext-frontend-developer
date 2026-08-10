---
name: mengto-scroll-scrubbed-word-reveal
description: Adapter pointer to canonical skills/mengto-scroll-scrubbed-word-reveal for Claude Code
---

# mengto-scroll-scrubbed-word-reveal (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-scroll-scrubbed-word-reveal/SKILL.md`](../../../skills/mengto-scroll-scrubbed-word-reveal/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-scroll-scrubbed-word-reveal
description: Reveal marked-up text word by word as scroll progress advances, while preserving semantic inline links, emphasis, responsive line wrapping, and reduced-motion readability. Use for headlines, quotes, manifestos, product statements, onboarding messages, or editorial passages where scrolling should pace comprehension rather than simulate typing.
---

# Scroll-Scrubbed Word Reveal

Make reading progress visible without replacing real text, breaking inline markup, or depending on a fixed line count.

## Prepare the text

1. Keep one untouched accessible text source in the DOM.
2. Walk text nodes with `TreeWalker`; do not flatten the container with `textContent` or `innerHTML`.
3. Skip `script`, `style`, form controls, and elements marked with `[data-no-split]`.
4. Replace only non-whitespace tokens with spans and preserve whitespace nodes exactly.
5. Mark generated spans `aria-hidden="true"` only when an equivalent unsplit accessible copy remains available.

Preferred structure:

```html
<p class="reveal" data-reveal>
  Motion should <em>explain</em> the next state, not decorate it.
</p>
```

Avoid line-based splitting. Browser line wraps must remain free to change with container width, language, zoom, and font loading.

## Map scroll to words

Use section progress as the single source of truth:
```
