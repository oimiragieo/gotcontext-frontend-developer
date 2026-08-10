# Gotcontext Frontend Developer — AGENTS

Installable gotcontext frontend craft pack for Cursor / Claude Code / Copilot.

## Rules

1. Prefer canonical `skills/<slug>/SKILL.md` over adapter excerpts.
1. Do not rewrite skill bodies casually — ship craft, don't invent slop.
1. This repo is the **product source of truth**.
1. Sibling pointers only: gotcontext-memory, tensor-grep (no install dependency).
1. Respect [ATTRIBUTION.md](ATTRIBUTION.md) / [LICENSES/](LICENSES/) — do not treat
   all skill bodies as gotcontext MIT.

## Install reminder

Thin adapters under `.cursor/skills` and `.claude/skills` point at `skills/`.
Keep those trees together (see README install modes).

## Verify (maintainers)

From a checkout of this repo (paths relative to your machine):

```bash
# Requires the private factory tooling while it still exists:
#   PYTHONPATH=<factory>/scripts python verify_folder_maps.py \
#     --repos '' --no-include-pack --pack <this-repo> \
#     --check-links --check-adapters
```

Product-local checks without factory tooling: open the repo in your harness and
confirm skills discover under `.cursor/skills` / `.claude/skills` /
`.github/instructions`.
