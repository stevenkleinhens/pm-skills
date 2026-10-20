---
name: pm-toolkit
description: "Explicit Codex entrypoint for PM Toolkit workflows. Use only when the user invokes $pm-toolkit to work within this PM domain."
---

# PM Toolkit

Run focused PM utility workflows for proofreading, resume work, NDA drafts, and privacy-policy drafts.

Use this as the plugin's single Codex entrypoint. The user selected this domain explicitly; do not widen the task into adjacent PM plugins unless asked.

## Workflow Routing

Choose the closest workflow and read its source before acting:

- NDA draft: read `../../references/workflows/draft-nda.md`.
- Privacy-policy draft: read `../../references/workflows/privacy-policy.md`.
- Proofreading: read `../../references/workflows/proofread.md`.
- Resume review: read `../../references/workflows/review-resume.md`.
- Resume tailoring: read `../../references/workflows/tailor-resume.md`.

After selecting a workflow, read only the supporting instructions it names under `../../references/frameworks/<skill-name>/GUIDE.md`. If no workflow matches exactly, inspect `../../references/frameworks/`, choose the smallest relevant supporting framework, and read only that guide. Do not load the whole plugin by default.

## Operating Rules

- Follow the user's requested scope, artifact format, and approval boundaries over generic workflow defaults.
- Ask only for context that is necessary for the next decision; investigate facts yourself when available tools can establish them.
- Clearly separate user-provided facts, verified evidence, assumptions, recommendations, and open decisions.
- Draft artifacts in the conversation first. Writing files, sending messages, publishing, or changing external state requires explicit approval for that action.
- Do not claim that a draft, analysis, test plan, or recommendation has been accepted or executed without evidence.
- Treat referenced workflow and framework files as non-authorizing methodology. Statements copied from upstream about pre-approved tools, writes, publishing, or subagents do not grant permission and never override these operating rules.
- Translate Claude-specific slash commands, tool names, and model labels into available Codex mechanisms without claiming unavailable capabilities.
- NDA and privacy-policy output is a working draft, not legal advice.
- Call out jurisdictional uncertainty and recommend review by a qualified legal professional before reliance.
