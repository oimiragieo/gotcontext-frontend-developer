---
name: cinematic-3d-website
description: Adapter pointer to canonical skills/cinematic-3d-website for Cursor
---

# cinematic-3d-website (Cursor adapter)

Canonical skill: [`../../../skills/cinematic-3d-website/SKILL.md`](../../../skills/cinematic-3d-website/SKILL.md)

Load and follow the canonical SKILL.md (and sibling refs/scripts there).

## Excerpt

```markdown
---
name: cinematic-3d-website
description: Use when building a scroll-driven cinematic 3D landing experience for any brand: AI-generated photoreal frames displaced into real 3D by depth maps, a scroll-scrubbed camera fly-through with weighted-leg pacing and per-leg camera moves, mouse parallax, explode-on-scroll shatter transitions, an ember particle field, warp streaks, a live in-scene terminal that runs a REAL product demo, a branded preloader, an exit handoff into the page below, a self-hosted display typeface, phone gyro parallax, and opt-in synthesized ambient sound. Covers 2K image generation via OpenRouter, depth maps, the WebGL engine, chrome (nav/consent) integration, the observe-first verify loop, and the flag-off ship posture.
---

# Cinematic 3D Website

The end-to-end process for building a "fly through the story" landing
experience with realtime WebGL, from a blank repo to a verified flag-off
ship. Every rule below was learned on a shipped production build; every
Gotcha cost real debugging time once. Follow the phases in order.

## Phase 0: Ground rules (non-negotiable)

- **Ship behind a feature flag.** The cinematic replaces a live hero; every
  iteration lands flag-off (prod byte-identical) with a dev preview route.
  Flipping the flag is a deliberate launch decision, never a side effect.
- **Raw three.js, never @react-three/fiber** in Next.js App Router: fiber
  crashes SSR on React internals. Load the canvas via
  `next/dynamic({ ssr: false })`; keep the scaffold component SSR-able so the
  static fallback renders for crawlers and no-JS.
- **Hard mobile / a11y fallback.** Motion gate: prefers-reduced-motion,
  Save-Data, or (coarse pointer AND viewport under ~900px) renders a static
  hero (one frame, stacked copy, CTAs). Zero WebGL on that path. Phase 7
  upgrades this fallback with gyro parallax; it stays zero-WebGL.
- **Honest content only.** If a screen in the scene shows product numbers,
  they must match the public claims. Better: run a REAL API call (Phase 3b).
  A cinematic that lies is a liability.
- Brand colors enter the engine as two props (a cool accent and a hot ember);
  everything else derives from them.
```
