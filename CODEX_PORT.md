# Codex Port Notes

This branch adapts PM Skills for native Codex plugin usage while preserving the upstream Claude-oriented structure.

Detailed project-specific documentation lives in `docs/codex-port.md`.

## Scope

Initial test scope:

- `pm-product-discovery`
- `pm-product-strategy`
- `pm-execution`

Do not port the remaining plugins until one of the initial three has a validated workflow that requires them.

## Porting Rules

1. Keep upstream files intact unless a Codex-specific change is necessary.
2. Add `.codex-plugin/plugin.json` beside existing `.claude-plugin/plugin.json`; do not remove Claude metadata.
3. Preserve existing `skills/*/SKILL.md` files as the source PM frameworks.
4. Convert high-value `commands/*.md` workflows into Codex-loadable workflow skills.
5. Treat slash commands as natural-language triggers in Codex. Do not rely on `/command` invocation.
6. Convert "save as markdown" instructions into a guarded behavior: draft in chat first, write files only after explicit user approval.
7. Keep plugin dependencies evidence-based. Add another plugin only when a workflow directly requires a missing skill, not for optional next-step suggestions.
8. Validate each plugin before installing or recommending normal use.

## Dependency Baseline

The first dependency pass found no declared cross-plugin dependencies in the manifests for `pm-product-discovery`, `pm-product-strategy`, or `pm-execution`.

Observed cross-plugin references are optional next-step suggestions, for example discovery output can lead to PRDs or user stories in `pm-execution`. That is covered by the initial three-plugin test scope.

## Validation Checklist

For each ported plugin:

- `.codex-plugin/plugin.json` exists and validates.
- `skills` points to `./skills/`.
- Existing skills keep valid frontmatter.
- Command workflows that matter in Codex have a corresponding workflow skill.
- Workflow skills reference command files for detailed steps instead of duplicating large command bodies.
- Any file writes require explicit user approval.
