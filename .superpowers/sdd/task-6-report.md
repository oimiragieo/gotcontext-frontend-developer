# Task 6 report — Mengto description trigger pass

**Status:** complete

## What changed
- Rewrote frontmatter `description:` only on **37** skills (bodies untouched).
- Set: Step-1 weak targets in `mengto-*` + `claude-design-adaptation` + `sample-awesome-*`, plus `mengto-glass-dark-ui` for dark-glass Prefer-over disambiguation.
- Descriptions lead with `Use when` / `When asked`; dark-glass near-duplicates name clock dials vs workspace shells vs blue laser vs gradient borders vs border-gradient frames.
- Descriptions with `: ` are JSON-quoted.
- Regenerated adapters (`generate_adapters.py` ×2); no drift after second run.
- `python3 scripts/pack_quality/check_pack.py` → **OK**.

## Counts
| Metric | Value |
|--------|-------|
| Canonical descriptions rewritten | 37 |
| mengto-* | 34 (33 weak + glass-dark-ui) |
| claude-design-adaptation | 1 |
| sample-awesome-* | 2 |
| Remaining weak (target families) | 0 |
| Pack-wide remaining weak (stitch/uupm, out of scope) | 15 |
| Plan expected ~52 | Tree had 36 weak targets pre-pass; many mengto already had trigger phrasing |

## Commits
- `6604d1b` — fix: add trigger phrases to mengto skill descriptions for discoverability (148 files: 37 canonical + adapters)

## Concerns
- Plan “expected 52” overstated vs current tree (36 failing Step-1 regex before this pass). Did not rewrite already-trigger-strong mengto that trail-trigger only (“… Use when asked” at end) except glass-dark-ui for disambiguation.

---

## Follow-up — 17 trail-`Use for` → lead `Use when` (2026-08-10)

**Status:** complete

### What changed
- First pass left 17 mengto descriptions that only had trailing `Use for…` (plan regex green, brief `Use when`/`When asked` missing).
- Rewrote frontmatter `description:` only on those 17 canonical skills; quoted when containing `: `.
- Regenerated adapters (`generate_adapters.py`).
- Plan weak heuristic: **0** mengto remaining (pack-wide weak still 15 stitch/uupm, out of scope).
- `python3 scripts/pack_quality/check_pack.py` → **OK** (exit 0).

### Slugs
ambient-section-particles, build-mobile-threejs-games, build-threejs-enemy-systems, build-threejs-scroll-worlds, cinematic-gsap-lenis-motion-system, editorial-portfolio-chapters, editorial-service-booking, falling-leaves, operational-enterprise-ai, optimize-threejs-games, pointer-trail-emitter, product-proof-saas, reveal-hover-effect, scroll-progress-timeline, scroll-scrubbed-visual-sequence, scroll-scrubbed-word-reveal, staggered-word-reveal.

### Commits
- `c482617` — fix: lead 17 mengto descriptions with Use when trigger phrasing
