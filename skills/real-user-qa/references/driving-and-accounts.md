# Driving the app + test accounts

Tactical layer for the QA pass. Load when actually driving a browser or provisioning test identities. (Distilled from rayfernando BRB browser-playbook / session-hygiene / test-accounts, Apache 2.0.)

## Drive like a real human (don't trip the defenses)

- **Attach to the user's real, already-signed-in Chrome instead of a fresh automated profile.** A WebDriver-launched browser is exactly what bot defenses (Cloudflare Turnstile, hCaptcha, "anomaly detected" on auth) are built to catch — and it starts logged out, so every scenario re-fights auth. chrome-devtools MCP: `--autoConnect` (Chrome 144+, via `chrome://inspect/#remote-debugging`) or `--browser-url=http://127.0.0.1:9222` with a dedicated `--user-data-dir` for sandboxed setups.
- **Security caveat:** while the remote-debugging port is open, any local process can drive that browser with the real session. Don't browse sensitive sites in it; close the port when the pass ends.
- **Universal flow per scenario:** navigate → snapshot → act on fresh refs → wait_for → capture evidence.
- **Fresh-ref discipline:** always re-snapshot after navigation, click, or form submit — refs go stale. "Element has pointer-events: none" or "ref not found" almost always means a stale snapshot (or a form mid-"Saving…" — wait ~3s and re-snapshot), not an app bug.
- **Recovery protocol when the browser tool itself misbehaves:** retry once on the same tab → once on a fresh tab → if it still fails, stop and report the tooling blocker. Don't loop.
- **Responsive spot-checks:** tap targets ≥44×44px; focus an input near the page bottom to confirm it stays visible above the on-screen keyboard; submit reachable without scrolling.

## Session hygiene (numbers that matter)

- Fresh storage per fresh-user scenario; **capture storage state as evidence BEFORE clearing it** (a stale sessionStorage value is often the repro).
- **Full reset between role changes** — switching member → admin means sign-out + fresh tab, not just clicking "sign out".
- **Cooldowns:** ~30s between sign-ups (Clerk dev keys); Auth0 "anomaly detected"/429 → 60s + dashboard reset; local Supabase/Firebase emulators are unlimited. **On a rate limit: mark the scenario BLOCKED and stop — retry-spam grows the limit.**
- Stale-state diagnostics: new signup lands somewhere unexpected → suspect a stale invite/redirect value in storage. If hygiene is perfect and behavior still depends on unpredictable prior state, that itself is a P1.

## Test accounts and fixtures

Email pattern: `<persona>+<tag>+run<MMDD>[-<shard>]@example.com` — `example.com` is IANA-reserved, never delivers. Never reuse a failed run's address; bump the tag.

| Provider | Fixture |
|---|---|
| Clerk (test mode) | email `*+clerk_test+<tag>@example.com`; OTP always `424242`; phone `+1 (XXX) 555-0100`–`0199` |
| Supabase local | seed via `seed.sql`; mail lands in Inbucket at `localhost:54324` |
| Firebase emulator | Auth Emulator UI at `localhost:9099` |
| Stripe test | `4242 4242 4242 4242` success · `4000 0027 6000 3184` 3DS · `4000 0000 0000 0002` decline |
| Twilio test | magic number `+15005550006` always succeeds |

Never commit passwords or tokens; keep them in a gitignored `.env.test` or vault. Run reports record the email pattern + role, never the password. If no test account is documented and no local emulator exists, ask the user before guessing.
