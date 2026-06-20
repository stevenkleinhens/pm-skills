---
name: execution-workflows
description: Run Codex-native execution workflows adapted from pm-execution commands. Use when the user asks for a PRD, user stories, job stories, WWA backlog items, OKRs, sprint planning, retrospectives, release notes, roadmap transformation, stakeholder map, pre-mortem, red-team review, meeting notes, test scenarios, or dummy data without relying on Claude slash commands.
---

# Execution Workflows

Use this skill as the Codex entrypoint for the workflows originally stored in `commands/`.

Codex does not expose Claude-style slash commands. Treat user requests such as "write a PRD", "break this into stories", "plan OKRs", "run a pre-mortem", "red-team this PRD", "plan a sprint", "summarize these meeting notes", "generate test scenarios", or "create dummy data" as natural-language workflow triggers.

## Workflow Routing

Choose the closest workflow:

- PRD creation: read `../../commands/write-prd.md`.
- Backlog item creation: read `../../commands/write-stories.md`.
- OKR planning: read `../../commands/plan-okrs.md`.
- Sprint planning, retro, or release notes: read `../../commands/sprint.md`.
- Pre-mortem: read `../../commands/pre-mortem.md`.
- PRD, roadmap, or strategy red-team: read `../../commands/red-team-prd.md`.
- Stakeholder mapping: read `../../commands/stakeholder-map.md`.
- Test scenario generation: read `../../commands/test-scenarios.md`.
- Outcome-roadmap transformation: read `../../commands/transform-roadmap.md`.
- Meeting notes: read `../../commands/meeting-notes.md`.
- Dummy data generation: read `../../commands/generate-data.md`.

Read the referenced command file before running the workflow. Then apply the named supporting skills from this plugin as needed.

## Codex Adaptation Rules

- Ask only for missing context needed for the next step.
- Preserve checkpoints and format choices from the original workflow, but ask one question at a time.
- Treat generated PRDs, OKRs, stories, roadmaps, and risk reviews as drafts until the user confirms them.
- When a command says to save markdown, CSV, JSON, SQL, Python, or other files, draft the content in chat first and ask for explicit approval before writing files.
- For dummy data, avoid real personal data and label generated data clearly as synthetic.
- For red-team and pre-mortem work, separate real blockers from speculative risks and recommend the cheapest validation step.
- Do not use slash-command syntax in the final answer unless the user is explicitly asking about Claude usage.

## Expected Outputs

For PRDs, produce the original eight-section PRD structure with assumptions, open questions, scope, and release planning.

For stories, produce the requested format: user stories, job stories, or WWA items with acceptance criteria and dependency notes.

For OKRs, produce focused objectives with measurable key results and confidence/risk notes.

For sprint workflows, produce sprint plans, retro themes, or release notes depending on the user's intent.

For risk workflows, produce ranked failure modes, mitigations, cheap tests, and kill criteria.

For testing, produce executable test scenarios with setup, steps, expected results, and environment notes.

For dummy data, produce the schema, generation approach, sample rows, and only write files after approval.

