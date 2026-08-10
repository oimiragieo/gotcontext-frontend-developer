# Verification notes — Gotcontext Frontend Developer

Public tree after Thinktank APPROVE_WITH_AMENDMENTS (license hold-back + cleanup).

## Pre-publish gates

- Awesome-ux skills **held back** (no upstream LICENSE) — see `LICENSES/HELD_BACK.md`
- Upstream MIT/Apache texts carried under `LICENSES/upstream/`
- Host absolute paths scrubbed from AGENTS/README
- `.ruff_cache` removed
- Secrets scan: no live API key assignments (env var *names* in docs OK)

## Maintainer verify (optional factory tooling)

```bash
PYTHONPATH=<ui-repos>/scripts python verify_folder_maps.py \
  --repos '' --no-include-pack \
  --pack <path-to-this-repo> \
  --check-links --check-adapters
```
