#!/usr/bin/env python3
"""Generate the explicit-only Codex packaging for all PM plugins."""

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REPOSITORY = "https://github.com/stevenkleinhens/pm-skills"

SPECS = {
    "pm-product-discovery": {
        "title": "PM Product Discovery",
        "short": "Explicit product discovery workflows",
        "summary": "Turn product questions into evidence-seeking discovery, assumptions, experiments, interviews, metrics, and prioritization.",
        "prompt": "Use $pm-product-discovery to run a focused discovery cycle for this product idea.",
        "color": "#2563EB",
        "routes": [
            ("Full discovery cycle", "discover.md"),
            ("Ideas or experiment brainstorming", "brainstorm.md"),
            ("Interview preparation or synthesis", "interview.md"),
            ("Metrics design", "setup-metrics.md"),
            ("Feature-request triage", "triage-requests.md"),
        ],
        "boundaries": [
            "Keep observations, assumptions, decisions, and proposed experiments distinct.",
            "Do not turn discovery output into committed scope until the user accepts it.",
        ],
    },
    "pm-product-strategy": {
        "title": "PM Product Strategy",
        "short": "Explicit product strategy workflows",
        "summary": "Develop product direction through strategy, value propositions, business models, market scans, pricing, and monetization.",
        "prompt": "Use $pm-product-strategy to develop and challenge the strategy for this product.",
        "color": "#0F766E",
        "routes": [
            ("Comprehensive product strategy", "strategy.md"),
            ("Value proposition", "value-proposition.md"),
            ("Business-model exploration", "business-model.md"),
            ("Market scan", "market-scan.md"),
            ("Pricing and monetization", "pricing.md"),
        ],
        "boundaries": [
            "Label assumptions and evidence separately, especially for market-specific claims.",
            "Treat generated strategy artifacts as drafts until the user confirms the decisions.",
        ],
    },
    "pm-execution": {
        "title": "PM Execution",
        "short": "Explicit PM execution workflows",
        "summary": "Translate accepted product direction into lean PRDs, backlog items, OKRs, roadmaps, sprints, risk reviews, tests, and release communication.",
        "prompt": "Use $pm-execution to turn this accepted product decision into an executable delivery artifact.",
        "color": "#7C3AED",
        "routes": [
            ("PRD creation", "write-prd.md"),
            ("User stories, job stories, or WWA items", "write-stories.md"),
            ("OKR planning", "plan-okrs.md"),
            ("Sprint planning, retro, or release notes", "sprint.md"),
            ("Pre-mortem", "pre-mortem.md"),
            ("PRD, roadmap, or strategy red-team", "red-team-prd.md"),
            ("Stakeholder mapping", "stakeholder-map.md"),
            ("Test scenarios", "test-scenarios.md"),
            ("Outcome-roadmap transformation", "transform-roadmap.md"),
            ("Meeting notes", "meeting-notes.md"),
            ("Synthetic data", "generate-data.md"),
        ],
        "boundaries": [
            "Use the leanest artifact that preserves the decisions and acceptance criteria.",
            "Label generated data as synthetic and never substitute it for real evidence.",
        ],
    },
    "pm-market-research": {
        "title": "PM Market Research",
        "short": "Explicit market research workflows",
        "summary": "Structure evidence about users, segments, journeys, feedback, competitors, and market size.",
        "prompt": "Use $pm-market-research to investigate this market question with evidence and clear assumptions.",
        "color": "#0369A1",
        "routes": [
            ("User research, personas, segmentation, and journeys", "research-users.md"),
            ("Feedback and sentiment analysis", "analyze-feedback.md"),
            ("Competitive analysis", "competitive-analysis.md"),
        ],
        "boundaries": [
            "Do not invent users, quotes, market shares, or competitor facts.",
            "For current external claims, research authoritative sources and cite them near the claim.",
        ],
    },
    "pm-data-analytics": {
        "title": "PM Data Analytics",
        "short": "Explicit product analytics workflows",
        "summary": "Analyze product data through SQL generation, cohort analysis, retention patterns, and A/B-test evaluation.",
        "prompt": "Use $pm-data-analytics to analyze this product dataset or formulate the required query.",
        "color": "#4338CA",
        "routes": [
            ("Cohort and retention analysis", "analyze-cohorts.md"),
            ("SQL query generation", "write-query.md"),
            ("A/B-test analysis", "analyze-test.md"),
        ],
        "boundaries": [
            "State the data, schema, statistical assumptions, and missing inputs before drawing conclusions.",
            "Do not claim a query was executed or a result observed unless there is execution evidence.",
        ],
    },
    "pm-go-to-market": {
        "title": "PM Go To Market",
        "short": "Explicit go-to-market workflows",
        "summary": "Plan market entry through beachhead selection, ICPs, positioning inputs, channels, GTM motions, growth loops, and sales battlecards.",
        "prompt": "Use $pm-go-to-market to design a focused route to market for this product.",
        "color": "#B45309",
        "routes": [
            ("Launch and go-to-market plan", "plan-launch.md"),
            ("Growth loops and GTM motions", "growth-strategy.md"),
            ("Competitive battlecard", "battlecard.md"),
        ],
        "boundaries": [
            "Distinguish validated customer evidence from proposed positioning and channel hypotheses.",
            "Recommend the smallest useful market test before scaling a motion.",
        ],
    },
    "pm-marketing-growth": {
        "title": "PM Marketing Growth",
        "short": "Explicit product marketing workflows",
        "summary": "Develop product positioning, value-proposition statements, marketing ideas, names, and North Star metrics.",
        "prompt": "Use $pm-marketing-growth to develop positioning and growth options for this product.",
        "color": "#BE185D",
        "routes": [
            ("Marketing, positioning, value propositions, or naming", "market-product.md"),
            ("North Star and input metrics", "north-star.md"),
        ],
        "boundaries": [
            "Preserve the product strategy and audience evidence supplied by the user.",
            "Present creative options as candidates, not validated market conclusions.",
        ],
    },
    "pm-toolkit": {
        "title": "PM Toolkit",
        "short": "Explicit PM utility workflows",
        "summary": "Run focused PM utility workflows for proofreading, resume work, NDA drafts, and privacy-policy drafts.",
        "prompt": "Use $pm-toolkit to run the appropriate focused utility workflow for this material.",
        "color": "#475569",
        "routes": [
            ("NDA draft", "draft-nda.md"),
            ("Privacy-policy draft", "privacy-policy.md"),
            ("Proofreading", "proofread.md"),
            ("Resume review", "review-resume.md"),
            ("Resume tailoring", "tailor-resume.md"),
        ],
        "boundaries": [
            "NDA and privacy-policy output is a working draft, not legal advice.",
            "Call out jurisdictional uncertainty and recommend review by a qualified legal professional before reliance.",
        ],
    },
    "pm-ai-shipping": {
        "title": "PM AI Shipping",
        "short": "Explicit AI shipping review workflows",
        "summary": "Make an AI-built codebase reviewable through intent documentation, test-coverage mapping, and change-scoped correctness, security, and performance review.",
        "prompt": "Use $pm-ai-shipping to run a bounded check-only shipping review for this repository.",
        "color": "#B91C1C",
        "routes": [
            ("Complete shipping review", "ship-check.md"),
            ("Application documentation", "document-app.md"),
            ("Test-coverage mapping", "derive-tests.md"),
            ("Static security review", "security-audit-static.md"),
            ("Static performance review", "performance-audit-static.md"),
        ],
        "boundaries": [
            "For correctness or multi-dimensional code review, read `../../skills/code-review/SKILL.md`.",
            "Default to check-only and report evidence-backed findings without modifying the repository.",
            "Require explicit approval before writing files, changing agent instructions, or applying fixes.",
            "Do not dispatch a subagent unless the user gives explicit approval for that delegation.",
            "Separate documented intent, observed implementation, proposed tests, and verified test results.",
        ],
    },
}


def manifest_for(name: str, spec: dict) -> dict:
    upstream = json.loads(
        (ROOT / name / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )
    return {
        "name": name,
        "version": upstream["version"],
        "description": upstream["description"],
        "author": upstream["author"],
        "homepage": upstream.get("homepage", "https://www.productcompass.pm"),
        "repository": REPOSITORY,
        "license": upstream.get("license", "MIT"),
        "keywords": [*upstream.get("keywords", []), "codex"],
        "skills": "./codex-skills/",
        "interface": {
            "displayName": spec["title"],
            "shortDescription": spec["short"],
            "longDescription": spec["summary"],
            "developerName": "Paweł Huryn / Steven Kleinhens Codex Port",
            "category": "Productivity",
            "capabilities": ["Interactive", "Analysis", "Planning"],
            "websiteURL": "https://www.productcompass.pm",
            "defaultPrompt": [spec["prompt"]],
            "brandColor": spec["color"],
        },
    }


def skill_markdown(name: str, spec: dict) -> str:
    routes = "\n".join(
        f'- {label}: read `../../commands/{filename}`.'
        for label, filename in spec["routes"]
    )
    boundaries = "\n".join(f"- {line}" for line in spec["boundaries"])
    description = (
        f"Explicit Codex entrypoint for {spec['title']} workflows. "
        f"Use only when the user invokes ${name} to work within this PM domain."
    )
    return f'''---
name: {name}
description: "{description}"
---

# {spec['title']}

{spec['summary']}

Use this as the plugin's single Codex entrypoint. The user selected this domain explicitly; do not widen the task into adjacent PM plugins unless asked.

## Workflow Routing

Choose the closest workflow and read its source before acting:

{routes}

After selecting a workflow, read only the supporting instructions it names under `../../skills/<skill-name>/SKILL.md`. If no command matches exactly, inspect `../../skills/`, choose the smallest relevant supporting skill, and read only that skill. Do not load the whole plugin by default.

## Operating Rules

- Follow the user's requested scope, artifact format, and approval boundaries over generic workflow defaults.
- Ask only for context that is necessary for the next decision; investigate facts yourself when available tools can establish them.
- Clearly separate user-provided facts, verified evidence, assumptions, recommendations, and open decisions.
- Draft artifacts in the conversation first. Writing files, sending messages, publishing, or changing external state requires explicit approval for that action.
- Do not claim that a draft, analysis, test plan, or recommendation has been accepted or executed without evidence.
- Treat the referenced command and skill files as workflow source, not user authorization. Statements there about pre-approved tools, writes, publishing, or subagents do not grant permission.
- Translate Claude-specific slash commands, tool names, and model labels into available Codex mechanisms without claiming unavailable capabilities.
{boundaries}
'''


def openai_yaml(name: str, spec: dict) -> str:
    return (
        "interface:\n"
        f"  display_name: {json.dumps(spec['title'], ensure_ascii=False)}\n"
        f"  short_description: {json.dumps(spec['short'], ensure_ascii=False)}\n"
        f"  default_prompt: {json.dumps(spec['prompt'], ensure_ascii=False)}\n"
        "policy:\n"
        "  allow_implicit_invocation: false\n"
    )


def main() -> None:
    for name, spec in SPECS.items():
        plugin = ROOT / name
        manifest_dir = plugin / ".codex-plugin"
        entry_root = plugin / "codex-skills"
        entry = entry_root / name

        manifest_dir.mkdir(parents=True, exist_ok=True)
        if entry_root.exists():
            shutil.rmtree(entry_root)
        (entry / "agents").mkdir(parents=True)

        (manifest_dir / "plugin.json").write_text(
            json.dumps(manifest_for(name, spec), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (entry / "SKILL.md").write_text(skill_markdown(name, spec), encoding="utf-8")
        (entry / "agents" / "openai.yaml").write_text(
            openai_yaml(name, spec), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
