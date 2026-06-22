# PM Skills Codex Port

This fork adapts the PM Skills marketplace for Codex while preserving the upstream Claude-oriented structure.

## Repository

- Upstream: `https://github.com/phuryn/pm-skills`
- Fork: `https://github.com/stevenkleinhens/pm-skills`
- Branch: `codex-port/plugins-1-3`
- Local path in Skillzone: `upstream/pm-skills`

## Decision

Use a fork, not a vendor copy.

Rationale:

- The repo is a full marketplace with 9 plugins, 68+ skills, and 42 command workflows.
- We want to keep upstream structure and potentially pull upstream updates.
- Codex adaptation touches plugin manifests and command-to-skill workflow behavior.
- Reviewable commits and a branch are useful for ongoing port work.

Initial test scope:

- `pm-product-discovery`
- `pm-product-strategy`
- `pm-execution`

The other plugins remain uninstalled until a workflow directly requires them.

## Codex Changes

Added Codex plugin manifests:

- `pm-product-discovery/.codex-plugin/plugin.json`
- `pm-product-strategy/.codex-plugin/plugin.json`
- `pm-execution/.codex-plugin/plugin.json`

Added Codex workflow skills:

- `pm-product-discovery/skills/product-discovery-workflows/SKILL.md`
- `pm-product-strategy/skills/product-strategy-workflows/SKILL.md`
- `pm-execution/skills/execution-workflows/SKILL.md`

These workflow skills convert Claude slash-command workflows into natural-language Codex triggers.

## Porting Rules

- Preserve upstream files unless a Codex-specific change is necessary.
- Keep `.claude-plugin` metadata.
- Add `.codex-plugin/plugin.json` beside Claude metadata.
- Treat `commands/*.md` as workflow source docs.
- Add workflow skills that read command files and route to supporting skills.
- Draft generated files in chat first; write files only after explicit approval.
- Add dependent plugins only when a workflow actually requires a missing skill.

## Install

The installed marketplace currently points at Steven's fork branch:

```bash
codex plugin marketplace add stevenkleinhens/pm-skills --ref codex-port/plugins-1-3
```

Installed plugins:

```bash
codex plugin add pm-product-discovery@pm-skills
codex plugin add pm-product-strategy@pm-skills
codex plugin add pm-execution@pm-skills
```

Rollback:

```bash
codex plugin remove pm-product-discovery
codex plugin remove pm-product-strategy
codex plugin remove pm-execution
codex plugin marketplace remove pm-skills
```

## Validation

Run from Skillzone root:

```bash
.venv/bin/python /Users/skleinhens/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py upstream/pm-skills/pm-product-discovery
.venv/bin/python /Users/skleinhens/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py upstream/pm-skills/pm-product-strategy
.venv/bin/python /Users/skleinhens/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py upstream/pm-skills/pm-execution

.venv/bin/python /Users/skleinhens/.codex/skills/.system/skill-creator/scripts/quick_validate.py upstream/pm-skills/pm-product-discovery/skills/product-discovery-workflows
.venv/bin/python /Users/skleinhens/.codex/skills/.system/skill-creator/scripts/quick_validate.py upstream/pm-skills/pm-product-strategy/skills/product-strategy-workflows
.venv/bin/python /Users/skleinhens/.codex/skills/.system/skill-creator/scripts/quick_validate.py upstream/pm-skills/pm-execution/skills/execution-workflows
```

Run from `upstream/pm-skills`:

```bash
python3 validate_plugins.py
```

Last known result:

```text
ALL CHECKS PASSED
```

## Smoke Test

A fresh ephemeral Codex run successfully used:

- `pm-product-discovery:product-discovery-workflows`
- `pm-product-strategy:product-strategy-workflows`
- `pm-execution:execution-workflows`

Test shape:

- Product Discovery: ideas, assumptions, risk prioritization, experiment
- Product Strategy: value proposition, strategic tradeoffs
- Execution: mini PRD, user stories, pre-mortem risk

No files were written.

Known note: Codex reported that skill descriptions were shortened to fit the skills context budget. This is not an installation failure, but if trigger quality suffers, reduce installed plugin scope or shorten descriptions.

