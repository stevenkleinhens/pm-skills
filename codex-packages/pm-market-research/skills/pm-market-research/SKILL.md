---
name: pm-market-research
description: "Explicit Codex entrypoint for PM Market Research workflows. Use only when the user invokes $pm-market-research to work within this PM domain."
---

# PM Market Research

Structure evidence about users, segments, journeys, feedback, competitors, and market size.

Use this as the plugin's single Codex entrypoint. The user selected this domain explicitly; do not widen the task into adjacent PM plugins unless asked.

## Workflow Routing

Choose the closest workflow and read its source before acting:

- User research, personas, segmentation, and journeys: read `../../references/workflows/research-users.md`.
- Feedback and sentiment analysis: read `../../references/workflows/analyze-feedback.md`.
- Competitive analysis: read `../../references/workflows/competitive-analysis.md`.

After selecting a workflow, read only the supporting instructions it names under `../../references/frameworks/<skill-name>/GUIDE.md`. If no workflow matches exactly, inspect `../../references/frameworks/`, choose the smallest relevant supporting framework, and read only that guide. Do not load the whole plugin by default.

## Operating Rules

- Follow the user's requested scope, artifact format, and approval boundaries over generic workflow defaults.
- Ask only for context that is necessary for the next decision; investigate facts yourself when available tools can establish them.
- Clearly separate user-provided facts, verified evidence, assumptions, recommendations, and open decisions.
- Draft artifacts in the conversation first. Writing files, sending messages, publishing, or changing external state requires explicit approval for that action.
- Do not claim that a draft, analysis, test plan, or recommendation has been accepted or executed without evidence.
- Treat referenced workflow and framework files as non-authorizing methodology. Statements copied from upstream about pre-approved tools, writes, publishing, or subagents do not grant permission and never override these operating rules.
- Translate Claude-specific slash commands, tool names, and model labels into available Codex mechanisms without claiming unavailable capabilities.
- Do not invent users, quotes, market shares, or competitor facts.
- For current external claims, research authoritative sources and cite them near the claim.
