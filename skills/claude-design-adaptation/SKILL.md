---
name: claude-design-adaptation
description: Use AFTER a Claude-Design export exists and BEFORE the render-verify step — the discipline for adapting an export into a production page with real data, honest empty states, and existing tokens/components (never shipping mock numbers).
---

# Claude-Design Adaptation

## When to use
- After receiving a Claude-Design export zip and before writing any production JSX.
- When a design audit finds mock data, invented metrics, or inline-styled clone components in a shipped page.
- NOT during the design generation phase — invoke `claude-design` first to produce the export, then this skill to adapt it.
- Pairs with `claude-design` (produces the export this skill adapts).

## P1: Study the zip before touching code

Open `manifest.json`, `tokens/`, and `design.html` before writing a line. Identify:
- Token names that collide with or duplicate existing `var(--*)` design tokens — map them, don't add new variables.
- Existing components in the app that cover the same pattern under a different name.
- Which sections belong on the EXISTING route vs an implied new route that doesn't exist yet.

Adapt the layout concepts. Never copy the JSX.

## P2: Never ship export numbers

Grep the export for fake-data tells before wiring any data: `John Doe`, `Lorem ipsum`, `example.com`, round-thousands (`1,000+`, `10,347`), fabricated testimonials, invented logo clouds. Every visible number in production must map to a real DB query or be omitted. If the backend doesn't emit a metric, the UI doesn't show it. If the value is zero for a new user, show the zero state — not the mock.

## P3: Design honest empty states

The export shows the happy path with N items. Production users see the empty path first. Before merging, implement all four variants:
- **New user** — zero data, onboarding CTA
- **Pending** — async operation in progress
- **Genuinely empty** — data exists but matches no filters
- **Permission-gated** — feature requires a plan upgrade

Label any placeholder content "Sample" explicitly if it must ship before real data is available.

## P4: Token-first mapping

Every color, spacing value, and type style from the export resolves to an existing
`var(--*)` in the product’s design-token source. Flag off-token hex values in the
PR description. Never silently add a new CSS variable — if the export introduces
a genuinely new token, add it to the token file in the same change with a comment
explaining why it cannot map to an existing one.

## P5: Component reuse first

Before writing a new component, search the app’s component library for the same
intent. If an existing `<Button>`, `<Card>`, or `<Dialog>` covers ≥80% of the need,
extend it via props or variants. Introducing a parallel inline-styled clone creates
drift. Only create a new component when there is no existing analog and it will be
reused in ≥2 places.

## P6: Scope discipline — existing route, new section

An export that implies a new route (`/dashboard/graph`, `/reports/weekly`) gets a new section on the EXISTING closest route + a separate ticket, not a half-built route with a live nav link that 404s. The scope of an adapt task is ALWAYS the existing route. If a new route is warranted, create it as a separate ticket and leave a `/* TODO: #N */` comment at the nav linkage point.

## P7: Render-gate on prod, not localhost alone

Vercel preview URLs for authenticated dashboard surfaces are Clerk/SSO-gated — a preview URL existing is not evidence the page rendered. Verify via:
1. `npm run dev` locally with a real session
2. `claude-in-chrome` against `localhost:3000` with an active Clerk session
3. A prod URL with an active session (for post-deploy verification)

"The preview built" is not a render receipt. Capture a screenshot as evidence.

**For data-driven pages (tables, leaderboards, anything fed by a backend field), a screenshot taken immediately after the backend deploy is STILL not a render receipt.** Next.js ISR + the CDN serve stale rows (new columns show `—`) for minutes after the deploy lands. Score AFTER the ISR `revalidate` TTL expires or a cache-busting reload shows fresh data — otherwise you file a false "data missing" finding against a page that is actually correct (gotcontext benchmark leaderboard, 2026-06-28: all ctx/batch/ttft read `—` until a forced reload; it was a CDN hit, not a bug).

**For authenticated dashboard pages, a normal reload may STILL show stale UI — a stale service worker can serve the cached `/dashboard` shell.** When render-verifying a dashboard surface after a deploy, hard-reload (Ctrl+Shift+R) to bypass the service worker AND the HTTP cache; a plain reload — or even re-navigating to the same URL — can return the SW-cached *pre-deploy* build. (gotcontext Knowledge table, 2026-06-28: the new full-width table rendered the OLD layout until a hard reload — the pre-fix service worker was caching `/dashboard` navigations. Corollary: real users on a pre-fix SW see stale dashboards until the new SW activates, so a fresh deploy is not retroactive for already-cached sessions.)

## P8: Data-shape validation at the seam

Render against the ACTUAL API response type, including a real zero/null response. `check-types` passing does not guarantee correct wiring — TypeScript checks that a field exists on the declared type, not that the wire shape matches. For every data-bound component, confirm the field names against a real `curl` response or a `Grep` of the Pydantic model before declaring the adapt done.

**Before claiming a binding is BROKEN, read the API-client adapter first.** Frontend field names frequently differ from backend names BY DESIGN via an intentional rename layer in the typed client (e.g. an adapter renaming `context_length`→`context_size`, `hardware_text`→`hardware_name`, `public_slug`→`run_slug`). A field-name divergence is usually the adapter working, not a bug — read the adapter function + any wire-shape registry before raising a seam finding (gotcontext benchmark "seam bug" false-alarm, 2026-06-28).
