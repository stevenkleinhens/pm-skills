# PM Skills Codex Port

This fork adapts all nine PM Skills plugins for Codex while preserving the upstream Claude- and Cursor-oriented sources.

## Repository

- Upstream: `https://github.com/phuryn/pm-skills`
- Fork: `https://github.com/stevenkleinhens/pm-skills`
- Branch: `codex/pm-skills-all-explicit`
- Upstream baseline: `v2.2.0` plus commit `07b34f64ee828df08953f505b7f747aef85ae7c6`
- Local path in Skillzone: `upstream/pm-skills`

## Decision

All nine plugins are available through Steven's fork, but Codex exposes exactly one explicit entrypoint per plugin:

- `$pm-product-discovery`
- `$pm-product-strategy`
- `$pm-execution`
- `$pm-market-research`
- `$pm-data-analytics`
- `$pm-go-to-market`
- `$pm-marketing-growth`
- `$pm-toolkit`
- `$pm-ai-shipping`

Every entrypoint has `allow_implicit_invocation: false`. Installing the marketplace does not authorize automatic PM workflow selection.

## Packaging Architecture

The repository separates source and distribution:

- the original `pm-*/commands/` and `pm-*/skills/` trees remain the upstream Claude-oriented sources
- the marketplace on this branch points to isolated packages under `codex-packages/<plugin-name>/`
- each package has one registered skill under `skills/<plugin-name>/`
- the 69 frameworks are copied as internal `references/frameworks/*/GUIDE.md` files
- the 42 workflows are copied as internal `references/workflows/*.md` files
- installable packages contain no `commands/` directory, preventing Codex from auto-migrating Claude commands into extra visible skills

The Codex manifest points only at `./skills/`. `scripts/generate_codex_port.py` regenerates the isolated packages, their manifests, entrypoints, metadata, and references from the current upstream sources.

## Operating Boundaries

- Draft artifacts in the conversation first; external writes need explicit approval.
- Keep facts, evidence, assumptions, recommendations, and decisions distinct.
- `pm-toolkit` legal documents are drafts and require qualified legal review.
- `pm-ai-shipping` defaults to check-only, cannot write or fix without explicit approval, and cannot dispatch subagents without explicit approval.
- `pm-ai-shipping` uses dedicated safe Codex workflow adapters; it does not load the conflicting operational directions from the upstream Claude commands.

## Install

Configure Steven's fork branch as the marketplace:

```bash
codex plugin marketplace add stevenkleinhens/pm-skills --ref codex/pm-skills-all-explicit
```

Install all plugins:

```bash
codex plugin add pm-product-discovery@pm-skills
codex plugin add pm-product-strategy@pm-skills
codex plugin add pm-execution@pm-skills
codex plugin add pm-market-research@pm-skills
codex plugin add pm-data-analytics@pm-skills
codex plugin add pm-go-to-market@pm-skills
codex plugin add pm-marketing-growth@pm-skills
codex plugin add pm-toolkit@pm-skills
codex plugin add pm-ai-shipping@pm-skills
```

Restart Codex Desktop after installation.

## Per-Project Control

Installed local-marketplace plugins can be enabled or disabled in a trusted project's `.codex/config.toml`:

```toml
[plugins."pm-product-discovery@pm-skills"]
enabled = true

[plugins."pm-ai-shipping@pm-skills"]
enabled = false
```

This controls availability for that project. Invocation remains explicit even when a plugin is enabled.

## Validation

Run from `upstream/pm-skills`:

```bash
python3 scripts/generate_codex_port.py
python3 -m unittest tests.test_codex_port tests.test_consistency
python3 validate_plugins.py
git diff --check
```

Validate an entrypoint with Skillzone's environment:

```bash
/Users/skleinhens/Projects/skillzone/.venv/bin/python \
  /Users/skleinhens/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  codex-packages/pm-market-research/skills/pm-market-research
```

## Rollback

Each plugin can be removed independently:

```bash
codex plugin remove pm-product-discovery@pm-skills
codex plugin remove pm-product-strategy@pm-skills
codex plugin remove pm-execution@pm-skills
codex plugin remove pm-market-research@pm-skills
codex plugin remove pm-data-analytics@pm-skills
codex plugin remove pm-go-to-market@pm-skills
codex plugin remove pm-marketing-growth@pm-skills
codex plugin remove pm-toolkit@pm-skills
codex plugin remove pm-ai-shipping@pm-skills
```

Remove the marketplace only after no installed plugin still depends on it:

```bash
codex plugin marketplace remove pm-skills
```
