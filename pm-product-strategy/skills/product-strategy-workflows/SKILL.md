---
name: product-strategy-workflows
description: Run Codex-native product strategy workflows adapted from pm-product-strategy commands. Use when the user asks for product strategy, value proposition, business model, market scan, pricing strategy, monetization, SWOT, PESTLE, Porter's Five Forces, or Ansoff analysis without relying on Claude slash commands.
---

# Product Strategy Workflows

Use this skill as the Codex entrypoint for the workflows originally stored in `commands/`.

Codex does not expose Claude-style slash commands. Treat user requests such as "create a product strategy", "write a value proposition", "map the business model", "run a market scan", or "design pricing" as natural-language workflow triggers.

## Workflow Routing

Choose the closest workflow:

- Comprehensive product strategy: read `../../commands/strategy.md`.
- Value proposition design: read `../../commands/value-proposition.md`.
- Business model exploration: read `../../commands/business-model.md`.
- Market scan: read `../../commands/market-scan.md`.
- Pricing and monetization strategy: read `../../commands/pricing.md`.

Read the referenced command file before running the workflow. Then apply the named supporting skills from this plugin as needed.

## Codex Adaptation Rules

- Ask only for missing context needed for the next decision or analysis step.
- Preserve the original workflow's framework choices, but explain tradeoffs briefly when selecting one.
- Treat generated strategy artifacts as drafts until the user confirms them.
- When a command says to save a markdown file, draft the content in chat first and ask for explicit approval before writing files.
- If evidence is stale or market-specific, say what is an inference and ask before using web research unless the user requested current research.
- Do not use slash-command syntax in the final answer unless the user is explicitly asking about Claude usage.

## Expected Outputs

For product strategy, produce a strategy canvas covering vision, segments, costs, value propositions, trade-offs, metrics, growth engine, capabilities, and defensibility.

For value propositions, produce the six-part JTBD-framed template: who, why, what before, how, what after, and alternatives.

For business models, produce the selected canvas or comparison with assumptions, risks, and validation questions.

For market scans, synthesize SWOT, PESTLE, Porter's Five Forces, and Ansoff insights into strategic implications.

For pricing, produce pricing model options, willingness-to-pay assumptions, risks, experiments, and a recommended next test.

