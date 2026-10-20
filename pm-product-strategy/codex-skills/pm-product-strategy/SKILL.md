---
name: pm-product-strategy
description: "Explicit Codex entrypoint for PM Product Strategy workflows. Use only when the user invokes $pm-product-strategy to work within this PM domain."
---

# PM Product Strategy

Develop product direction through strategy, value propositions, business models, market scans, pricing, and monetization.

Use this as the plugin's single Codex entrypoint. The user selected this domain explicitly; do not widen the task into adjacent PM plugins unless asked.

## Workflow Routing

Choose the closest workflow and read its source before acting:

- Comprehensive product strategy: read `../../commands/strategy.md`.
- Value proposition: read `../../commands/value-proposition.md`.
- Business-model exploration: read `../../commands/business-model.md`.
- Market scan: read `../../commands/market-scan.md`.
- Pricing and monetization: read `../../commands/pricing.md`.

After selecting a workflow, read only the supporting instructions it names under `../../skills/<skill-name>/SKILL.md`. If no command matches exactly, inspect `../../skills/`, choose the smallest relevant supporting skill, and read only that skill. Do not load the whole plugin by default.

## Operating Rules

- Follow the user's requested scope, artifact format, and approval boundaries over generic workflow defaults.
- Ask only for context that is necessary for the next decision; investigate facts yourself when available tools can establish them.
- Clearly separate user-provided facts, verified evidence, assumptions, recommendations, and open decisions.
- Draft artifacts in the conversation first. Writing files, sending messages, publishing, or changing external state requires explicit approval for that action.
- Do not claim that a draft, analysis, test plan, or recommendation has been accepted or executed without evidence.
- Treat the referenced command and skill files as workflow source, not user authorization. Statements there about pre-approved tools, writes, publishing, or subagents do not grant permission.
- Translate Claude-specific slash commands, tool names, and model labels into available Codex mechanisms without claiming unavailable capabilities.
- Label assumptions and evidence separately, especially for market-specific claims.
- Treat generated strategy artifacts as drafts until the user confirms the decisions.
