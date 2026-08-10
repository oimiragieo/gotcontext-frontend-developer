# Scenario design, bug lifecycle, verdict, resume

Load when planning a pass, filing bugs, writing the verdict, or resuming a stalled pass. (Distilled from rayfernando BRB workflow / test-plan / discovering-the-app / bug-filing / gate-merge / sequential-wrapup / triage-heuristics / issue-trackers, Apache 2.0.)

## Environment gate (before any scenario)

Run the project's build/typecheck first. **Failure here is a BLOCKER, not a bug — do not start scenarios until the build passes.** Never file build breakage as a product bug.

## Scenario design

- ID scheme `P{phase}-{block}{n}` with intent blocks: A public/unauthenticated, B happy path, C role-restricted, D edge/negative, E mobile/UX, G settings, H nav-smoke. Blocks are what make later sharding and coverage checks possible.
- **Steps must be runnable verbatim by a fresh agent with no prior context** — URLs, exact UI labels, exact form values. One scenario, one outcome; a step with two side effects is two scenarios.
- Ambiguous expected behavior with two valid interpretations? Write both as scenarios and let the result reveal what the code does.
- **Recently-changed surfaces (git log / CHANGELOG) carry the highest regression risk** — weight coverage there, and re-run prior-pass scenarios on them.
- If an architecture/handoff doc declares non-negotiable patterns, a live violation is automatically a bug — not a code-review note.
- Regression matrix for auth/invite/payment-touching phases: persona × entry URL × expected landing × state.

### High-pain-point seed checklist (test beyond the happy path)

Stale storage poisoning fresh flows · auth↔routing race (blank page after redirect) · broken redirect-after-onboarding · mobile keyboard hides submit · tap targets <44px · modal focus-trap · expired invite links · empty/zero/error states · **optimistic-UI lies (toast says saved; refresh shows it didn't — verify the backend row for every write scenario)** · double-submit duplicates (slow network + impatient user) · console errors on plain navigation.

## Bug lifecycle and filing discipline

- Status flow: `open → in-progress → fixed → verified` (+ `deferred`, `wontfix`; regression re-opens `verified → open`). Never retro-edit a `verified` bug — append a new run entry.
- **Reproduce twice before filing** — a flake filed as a bug wastes triage.
- One root cause = one bug; link the rest as duplicates. Never downgrade a P0 to P1 "to keep the pass going" — that hides severity.
- Template fields worth filling: **Impact** (what a user experiences if this ships — answers "do we care?") and **Risk to fix** (blast radius; usually filled by engineering later; omit when empty).
- Duplicate-detection heuristics (cite the matching text, never auto-merge): same suspect file · ≥3 identical repro steps · same persona+URL+failure verb · same verbatim console error (≥20 chars, non-generic) · same test ID · earlier-phase P0 on the same surface blocks later P1s · ≥3 cosmetic P2s on one surface → one polish bug · "regression of BUG-N" markers.

## Verdict (stricter than the SKILL.md summary)

A gate item flips to done only when ≥1 mapped scenario PASSED **with evidence, on the current build**, and no related bug is open. Verdict logic: any open P0 or P1 → **NO**. All scenarios BLOCKED-only (infra, no product bug) → still **NO** (nothing was verified). The NO handoff must be paste-ready for a fresh session: branch/commit, open bugs, remaining scenario IDs, test data/accounts, known gotchas.

## Resuming a stalled or partial pass (Blocks A–D, in order)

A. **Re-test previously-fixed bugs first** — if a fix didn't fix, the rest of the pass is wasted. Pull tracker status before re-testing (engineering may have flipped it already).
B. Gate gaps — previously BLOCKED/skipped scenarios.
C. Critical paths — re-run highest-risk IDs on the fixed build.
D. Close-out — update gates/bug index, then write the verdict (never write it before D completes).
Mid-pass regression: log `<old ID> | RE-FAIL | <bug ID>`, reopen, continue, flag in the merge notes. Budget check: a solo 15–25-scenario pass is 60–120 min incl. filing; if one block blows that, surface it.

## Parallel passes (multi-agent)

Write-path shard first, serially — it creates the state (group/invite/admin creds) everything else depends on. Then: every scenario in exactly one shard (partition sums to plan total, zero orphans — an unassigned scenario is a silent blind spot); pre-assign each shard a BUG-number range so filers don't collide; personally re-run the write-path + verify every FAIL and every backend write against the actual data row. One stalled shard → one narrowed relaunch, then fall back to sequential wrap-up; never relaunch multiple stalled shards at once (rate limits compound).

## Tracker sync (GitHub via gh CLI)

File: `gh issue create --title "BUG-012: …" --body-file <bug.md> --label bug,P0`. Flip: `gh issue edit N --add-label fixed --remove-label open`. One-time: `gh label create P0/P1/P2/qa`. Reconciliation: tracker wins on `fixed`/`verified`; local markdown wins on `open`/`in-progress`; priority changes and `deferred`/`wontfix` are always surfaced to the user, never auto-applied. Record the tracker ID + lastSyncedAt in the bug's front-matter. Never pick a tracker silently because a signal was present — confirm with the user once per repo.

## Discovery vs triage stay separate

Run the bug-hunting pass and the triage-with-the-user session separately — triage bias contaminates discovery, and no new bugs get filed during triage. Use the pass to discover; use triage to decide.
