---
name: ui-fix-observe-first
description: "Use when fixing, auditing, improving, or building ANY web UI — before reading or editing component code. Fires on contrast/a11y/overflow/responsive/hover-focus/layout complaints, \"polish the UI\", \"audit the page/site\", \"make it premium\", or any visual change (esp. omega-console at :8099). Rule 1: never diagnose a UI defect from code — render at 375+1440, measure with axe-core / computed-style WCAG contrast / a11y tree / console errors / keyboard pass / reflow at 320px+200% zoom, then cite the measurement; \"it compiles\" is not a finding. Rule 2: correctness is yours to fix directly on design tokens; aesthetic/taste direction goes through Exa + the thinktank council, not the CEO."
---

# UI fix — observe first

## The two rules (non-negotiable)
1. **Never diagnose or claim a UI change from code — render, measure, cite.** Runtime defects (contrast, overflow, wrap, responsive, hover/focus, layout shift, stacking) do NOT exist in the JSX. No measurement = not a finding. "It compiles" / "the JSX looks right" is not an observation.
2. **Correctness is yours to fix; taste is decided by evidence + council, not by asking the CEO.** Aesthetic direction goes through Exa + the thinktank; you bring the CEO the *result*, not the question.

## FLOW A — fix / improve an existing UI
0. Prompt fires the ui-observe-first hook → render before you read code.
1. **RENDER** the live page at **375 + 1440**. Public page → chrome-devtools MCP. **Authed dashboard (omega-console) → claude-in-chrome** with a live session.
2. **OBSERVE quantitatively — layered, not one tool** (Exa 2026: automation catches ~57% of issues; Lighthouse is a *floor*, not conformance):
   - **axe-core** (the engine — Deque, "zero false positives", what Lighthouse wraps a subset of). On a live claude-in-chrome page, inject + run it: `javascript_tool` → load `https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.x/axe.min.js` then `await axe.run()`. Catches contrast, missing labels, ARIA validity, duplicate IDs. Public page: use chrome-devtools Lighthouse + `performance_start_trace` (LCP/INP/CLS).
   - **computed-style WCAG contrast** (fallback / precise pin): `javascript_tool` computes the ratio of an element's `color` vs its effective bg (AA normal ≥4.5, large/UI ≥3.0). Use when axe can't be injected.
   - **a11y tree** (`read_page`) + **console errors** (`read_console`) + a full-page screenshot.
   - **Keyboard pass** (highest-leverage manual step, ~30% of automated-missed issues): Tab from the top — focus visible at all times? logical order? no traps? sticky nav doesn't steal focus (WCAG 2.2 focus-not-obscured)?
   - **Reflow**: check 320px width / 200% zoom for overflow. **24px tap targets** (WCAG 2.2).
2.5 **RATE THE WHOLE PAGE, NOT JUST YOUR WIDGET — + the SIBLING-PARITY question.** Green per-widget
   numbers (contrast/tap-target/aria all AA) do NOT mean the surface is done. Before declaring a
   control fixed, ask: **"what does the nearest SIBLING control offer that mine doesn't?"** Live
   receipt: a console camera toggle passed every per-widget axe/contrast check but had NO device
   picker while the sibling mic control did — a whole-page parity gap invisible to per-widget
   measurement. Also judge the control ACROSS interaction/navigation, not just at rest: (a) fail-soft
   reverts must surface **PROMINENTLY** (a `role="alert"`, not whispered status text — a silent
   auto-revert reads as a haunted UI); (b) opt-in state must be **session-scoped**, not reset on
   every SPA-nav remount ("it turned itself off"); (c) labels must not wrap mid-word at the real
   column width. (memory: `feedback_verify_the_page_not_your_widget`)
3. **PIN** the exact defect — cite the measurement (ratio, px, element, axe rule id). No evidence = not a finding.
4. Split findings:
   - **4a CORRECTNESS** (contrast <4.5 AA, a11y, CLS, overflow, wrong-hex, light-mode, focus/keyboard) → fix directly, **one class at a time, on the design-token `var(--*)`** (omega-console: `src/index.css` @theme tokens, never raw hex).
   - **4b AESTHETIC DIRECTION** (premium feel / how bold) → **do NOT ask the CEO.** Research with Exa (what Vercel / Linear / Stripe + A/B data actually do) → convene the thinktank / Workflow-council to decide the forks → ship the quick-wins, let the council settle taste; bring the CEO the result.
5. **GATE**: check-types + FULL test suite, never a scoped run (omega-console: `tsc -b` + `vitest run` + eslint). Add the static a11y layer where possible (eslint-plugin-jsx-a11y — 0 runtime cost).
6. **SHIP**: commit (subject <100 chars, lowercase) → PR → CI green. (omega-console is LOCAL-only — no Vercel; "ship" = PR→CI-green.)
7. **RE-RENDER to verify** — the fix landed AND nothing regressed, at dark + light + mobile. omega-console serves a prebuilt dist, so **rebuild first** (`npm --prefix apps/web run build` → restart uvicorn), then re-measure on the running :8099. Track 3 numbers per page: axe violations, contrast ratios, keyboard pass.
8. **SCORE**: run `frontend-audit`'s 9-pillar rubric (X/45) on the fixed page; treat a 4 as "good, leave alone" per its own anti-inflation rule. (`ui-rater` does not exist as a skill — corrected 2026-08-01.)

## FLOW B — develop a new UI
Same spine, generate-step in front: 0. Declare the design tokens first → 1. Generate (claude.ai/design default; Figma if a designer must touch it) → 2. Assets (Figma MCP / claude.ai-design — **no aura.build in this env**) → 3. Build in `src/` on the tokens → then Flow A steps 2–8.

## omega-console specifics (this env)
- Runs at `127.0.0.1:8099`, **auth disabled by design** (`.env OMEGA_CONSOLE_AUTH_DISABLED=true`) — no token. Start (windowless): `OMEGA_CONSOLE_AUTH_DISABLED=true <apps/bff/.venv python> -m uvicorn omega_console_bff.app:app --host 127.0.0.1 --port 8099 --app-dir apps/bff > $TEMP/omega-console.log 2>&1 &`; verify `curl :8099/api/auth-probe` → `{"auth_mode":"open"}`.
- Tokens (`apps/web/src/index.css` @theme, **dark-only**): surface `#111317`, text-primary `#e8eaed`, text-secondary `#aeb4bd`, text-tertiary `#868d99` (was `#6b7280` = failed AA), accent `#5eead4`.
- Tooling reality: claude-in-chrome ✓ + Figma MCP ✓. **NO aura.build; NO chrome-devtools Lighthouse for the authed-local page.** axe-core injection is **CSP-BLOCKED** on the console (external-script fetch/eval denied — verified 2026-07-03, returns empty) → use the **computed-style WCAG contrast calc + 24px-target + overflow check via `javascript_tool`** (proven working) plus `read_page` a11y tree + `read_console`, and a manual keyboard pass.

## Receipts (this process, proven 2026-07-03)
- Found the tertiary-text token failing WCAG AA (**3.85:1 measured** on cards) → lifted to `#868d99` (**5.56:1**), re-measured green → PR#12. A GLOBAL token fix that lifted every page at once.
- The AuthGate "low-contrast button" was a screenshot-eyeball **FALSE POSITIVE** — measurement showed **14.47:1 (AAA)**. This is exactly why rule 1 exists: measure, don't eyeball.

## Refinements (2026-07-21, gotcontext KB-room)
- **Observe at the TARGET viewport, not a default narrow one.** A 752px capture false-flagged a well-composed 1440 desktop layout as a "void." Rendering at a wrong viewport still "observes" but yields a false finding on an intentionally desktop-first layout — always render at the layout's actual target width(s) before diagnosing. (A specific way to obey rule 1 correctly-but-uselessly.)
- **Component-vitest render-verify WITHOUT auth (the auth-walled-page branch).** When the full page is behind a login you can't self-drive (Clerk, no dev bypass), you can still verify ONE component in isolation: vitest + jsdom + testing-library + a mocked `useAuth` (`vi.mock('@clerk/nextjs', () => ({ useAuth: () => ({ getToken, isLoaded: true }) }))`) renders it with no live session. A valid PARTIAL substitute for component correctness — NOT for full-page observation (that still needs the real render, e.g. merge-to-prod when previews are SSO-gated). Sibling "cheap oracle when the expensive one is auth-walled" move: the `extract-embedded-asset-safely` skill.

## Cross-references
- `use-thinktank` — for the 4b aesthetic-direction council.
- `use-exa` — for the 4b competitive-pattern research (Vercel/Linear/Stripe).
- `real-user-qa` — the upstream QA pass that files the bugs this skill fixes; after fixing, its re-test protocol (references/scenarios-and-verdict.md Blocks A-D) verifies the fix on a fresh build.
- `ai-wayfinders` — blank-slate / suggestion / onboarding UX for console Chat (capability-honest chips); measure with this skill after shipping.
- `ai-trust-builders` — disclosure/consent/footprints copy on Settings and cloud paths; observe-first still required for contrast/focus.
