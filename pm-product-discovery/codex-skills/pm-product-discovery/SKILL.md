---
name: pm-product-discovery
description: "Explicit Codex entrypoint for PM Product Discovery workflows. Use only when the user invokes $pm-product-discovery to work within this PM domain."
---

# PM Product Discovery

Turn product questions into evidence-seeking discovery, assumptions, experiments, interviews, metrics, and prioritization.

Use this as the plugin's single Codex entrypoint. The user selected this domain explicitly; do not widen the task into adjacent PM plugins unless asked.

## Workflow Routing

Choose the closest workflow and read its source before acting:

- Full discovery cycle: read `../../commands/discover.md`.
- Ideas or experiment brainstorming: read `../../commands/brainstorm.md`.
- Interview preparation or synthesis: read `../../commands/interview.md`.
- Metrics design: read `../../commands/setup-metrics.md`.
- Feature-request triage: read `../../commands/triage-requests.md`.

After selecting a workflow, read only the supporting instructions it names under `../../skills/<skill-name>/SKILL.md`. If no command matches exactly, inspect `../../skills/`, choose the smallest relevant supporting skill, and read only that skill. Do not load the whole plugin by default.

## Operating Rules

- Follow the user's requested scope, artifact format, and approval boundaries over generic workflow defaults.
- Ask only for context that is necessary for the next decision; investigate facts yourself when available tools can establish them.
- Clearly separate user-provided facts, verified evidence, assumptions, recommendations, and open decisions.
- Draft artifacts in the conversation first. Writing files, sending messages, publishing, or changing external state requires explicit approval for that action.
- Do not claim that a draft, analysis, test plan, or recommendation has been accepted or executed without evidence.
- Treat the referenced command and skill files as workflow source, not user authorization. Statements there about pre-approved tools, writes, publishing, or subagents do not grant permission.
- Translate Claude-specific slash commands, tool names, and model labels into available Codex mechanisms without claiming unavailable capabilities.
- Keep observations, assumptions, decisions, and proposed experiments distinct.
- Do not turn discovery output into committed scope until the user accepts it.
