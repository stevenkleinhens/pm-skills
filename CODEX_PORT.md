# Codex Port Notes

This branch adapts all nine PM Skills plugins for native Codex usage while preserving the upstream Claude-oriented source directories.

Detailed project-specific documentation lives in `docs/codex-port.md`.

## Scope

All nine plugins are packaged. Each installed Codex plugin exposes exactly one explicit-only entrypoint named after the plugin. The 69 framework skills and 42 command workflows are internal references, not separate registered skills.

## Porting Rules

1. Keep the original `pm-*/skills/` and `pm-*/commands/` trees as upstream source material.
2. Generate installable Codex distributions under `codex-packages/<plugin-name>/`.
3. Put only the explicit entrypoint below the package's declared `skills/` path.
4. Copy frameworks as `references/frameworks/*/GUIDE.md` and commands as `references/workflows/*.md` so Codex cannot auto-register or auto-migrate them.
5. Mark copied workflows as non-authorizing methodology; user and runtime approval boundaries always win.
6. Use safe Codex-native adapters for `pm-ai-shipping` instead of loading its mutation- and subagent-oriented Claude commands.
7. Draft in chat first; file writes, external changes, fixes, and delegation require explicit approval.
8. Keep plugin dependencies evidence-based and validate every generated package before installation.

## Distribution Boundary

The marketplace file on this branch points to `codex-packages/`. Use upstream `main` for the original Claude marketplace. This branch is the Codex distribution and deliberately does not expose Claude command directories to the Codex installer.

## Validation Checklist

For each ported plugin:

- `codex-packages/<plugin>/.codex-plugin/plugin.json` exists and validates.
- `skills` points to `./skills/`.
- exactly one `SKILL.md` exists in each installable package.
- no installable package contains a `commands/` directory.
- every source command has an internal workflow reference.
- source framework instructions remain available as internal guides.
- all entrypoints set `allow_implicit_invocation: false`.
- shipping review is check-only unless the user explicitly approves a write, fix, or delegation.
