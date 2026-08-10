---
name: mengto-tailwindcss
description: Adapter pointer to canonical skills/mengto-tailwindcss for Claude Code
---

# mengto-tailwindcss (Claude Code adapter)

Canonical skill: [`../../../skills/mengto-tailwindcss/SKILL.md`](../../../skills/mengto-tailwindcss/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: mengto-tailwindcss
description: Use when designing/implementing UI with Tailwind CSS (layout, typography, responsive, theming, component patterns). Includes quick recipes and conventions for clean, consistent web design.
---

# Tailwind CSS — Utility-first Styling Skill

## When to use
- Rapid UI building with consistent spacing/typography scales
- Design systems where composition beats bespoke CSS
- Component-driven apps (React/Vue/Svelte), marketing pages, prototypes → production

## Key concepts & patterns
- Utilities compose in HTML/JSX: `class="flex gap-4 p-6 bg-zinc-950 text-white"`
- Responsive variants: `sm: md: lg: xl:` etc.
- State variants: `hover:`, `focus:`, `active:`, `disabled:`, `group-hover:`, `peer-checked:`
- Arbitrary values (use sparingly): `w-[42rem]`, `bg-[#0b1220]`, `translate-y-[3px]`
- Dark mode patterns: `dark:` with class-based strategy
- Extracting repeated patterns:
  - Prefer components (JSX/Vue components) first
  - Then `@apply` for small reusable patterns (avoid overuse)
- Build pipeline:
  - Tailwind scans “content” files for class names and generates CSS (zero-runtime)

## Common pitfalls
- Classes not generated in production
  - Ensure content paths include all templates/components.
  - Avoid building class names dynamically (e.g. `"text-" + color`) unless safelisted.
- Overusing `@apply` and losing the utility-first benefits
- Conflicting styles due to class order assumptions
```
