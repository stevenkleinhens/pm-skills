---
name: product-discovery-workflows
description: Run Codex-native product discovery workflows adapted from pm-product-discovery commands. Use when the user asks to run discovery, brainstorm product ideas or experiments, prepare or summarize interviews, set up product metrics, or triage feature requests without relying on Claude slash commands.
---

# Product Discovery Workflows

Use this skill as the Codex entrypoint for the workflows originally stored in `commands/`.

Codex does not expose Claude-style slash commands. Treat user requests such as "run discovery", "brainstorm experiments", "prepare an interview", "set up metrics", or "triage feature requests" as natural-language workflow triggers.

## Workflow Routing

Choose the closest workflow:

- Full product discovery cycle: read `../../commands/discover.md`.
- Product ideas or experiment brainstorming: read `../../commands/brainstorm.md`.
- Customer interview prep or transcript synthesis: read `../../commands/interview.md`.
- Metrics dashboard setup: read `../../commands/setup-metrics.md`.
- Feature-request triage: read `../../commands/triage-requests.md`.

Read the referenced command file before running the workflow. Then apply the named supporting skills from this plugin as needed.

## Codex Adaptation Rules

- Ask only for missing context that is required for the next step.
- Keep checkpoint questions from the original workflow, but ask them one at a time.
- When a command says to save a markdown file, draft the content in chat first and ask for explicit approval before writing files.
- If the workflow suggests a next step from another plugin, present it as optional unless that plugin is installed and relevant.
- Prefer concrete tables, assumptions, experiment specs, and decision points over broad explanation.
- Do not use slash-command syntax in the final answer unless the user is explicitly asking about Claude usage.

## Expected Outputs

For full discovery, produce a discovery plan with:

- discovery question
- product stage
- ideas explored
- selected ideas
- critical assumptions
- validation experiments
- experiment details
- timeline
- decision framework

For brainstorming, produce a short list of ideas or experiments grouped by perspective, then ask which ones to carry forward.

For interviews, produce either an interview script or a structured transcript summary, depending on the user's input.

For metrics, produce a North Star metric, input metrics, health metrics, data sources, alerts, and implementation notes.

For feature triage, cluster requests by theme, analyze segments and underlying needs, prioritize the backlog, and identify the recommended next actions.

