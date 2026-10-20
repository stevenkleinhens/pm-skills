"""Codex-specific packaging and explicit-invocation invariants."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PLUGINS = (
    "pm-product-discovery",
    "pm-product-strategy",
    "pm-execution",
    "pm-market-research",
    "pm-data-analytics",
    "pm-go-to-market",
    "pm-marketing-growth",
    "pm-toolkit",
    "pm-ai-shipping",
)
LEGACY_CODEX_WRAPPERS = (
    ROOT
    / "pm-product-discovery"
    / "skills"
    / "product-discovery-workflows",
    ROOT
    / "pm-product-strategy"
    / "skills"
    / "product-strategy-workflows",
    ROOT / "pm-execution" / "skills" / "execution-workflows",
)


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError(f"missing frontmatter: {path}")
    result = {}
    for line in match.group(1).splitlines():
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


class TestCodexPluginPackaging(unittest.TestCase):
    def test_all_plugins_have_codex_manifests_at_marketplace_version(self):
        version = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["version"]
        for name in PLUGINS:
            path = ROOT / name / ".codex-plugin" / "plugin.json"
            self.assertTrue(path.is_file(), f"missing {path}")
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["name"], name)
            self.assertEqual(manifest["version"], version)
            self.assertEqual(manifest["skills"], "./codex-skills/")

    def test_each_plugin_exposes_exactly_one_codex_entrypoint(self):
        for name in PLUGINS:
            root = ROOT / name / "codex-skills"
            entries = sorted(p.name for p in root.iterdir() if p.is_dir())
            self.assertEqual(entries, [name])
            skill = root / name / "SKILL.md"
            self.assertEqual(frontmatter(skill)["name"], name)

    def test_legacy_registered_workflow_wrappers_are_removed(self):
        for path in LEGACY_CODEX_WRAPPERS:
            self.assertFalse(path.exists(), f"legacy wrapper remains: {path}")


class TestExplicitInvocation(unittest.TestCase):
    def test_every_entrypoint_is_explicit_only(self):
        for name in PLUGINS:
            metadata = (
                ROOT
                / name
                / "codex-skills"
                / name
                / "agents"
                / "openai.yaml"
            ).read_text(encoding="utf-8")
            self.assertIn("allow_implicit_invocation: false", metadata)
            self.assertIn(f"${name}", metadata)
            short = re.search(r'^  short_description: "([^"]+)"$', metadata, re.M)
            self.assertIsNotNone(short, f"missing short_description for {name}")
            self.assertGreaterEqual(len(short.group(1)), 25)
            self.assertLessEqual(len(short.group(1)), 64)

    def test_each_command_is_routed_by_its_plugin_entrypoint(self):
        for name in PLUGINS:
            body = (
                ROOT / name / "codex-skills" / name / "SKILL.md"
            ).read_text(encoding="utf-8")
            commands = sorted((ROOT / name / "commands").glob("*.md"))
            self.assertTrue(commands, f"no commands found for {name}")
            for command in commands:
                reference = f"../../commands/{command.name}"
                self.assertIn(reference, body, f"{name} does not route {command.name}")
            self.assertIn("../../skills/", body)

    def test_source_workflows_do_not_expand_authority(self):
        for name in PLUGINS:
            body = (
                ROOT / name / "codex-skills" / name / "SKILL.md"
            ).read_text(encoding="utf-8")
            self.assertIn("do not grant permission", body)
            self.assertIn("Claude-specific", body)


class TestSafetyBoundaries(unittest.TestCase):
    def test_ai_shipping_defaults_to_check_only(self):
        path = (
            ROOT
            / "pm-ai-shipping"
            / "codex-skills"
            / "pm-ai-shipping"
            / "SKILL.md"
        )
        text = path.read_text(encoding="utf-8").lower()
        self.assertIn("check-only", text)
        self.assertIn("explicit approval", text)
        self.assertIn("subagent", text)
        self.assertIn("../../skills/code-review/skill.md", text)

    def test_legal_drafts_require_review(self):
        path = (
            ROOT / "pm-toolkit" / "codex-skills" / "pm-toolkit" / "SKILL.md"
        )
        text = path.read_text(encoding="utf-8").lower()
        self.assertIn("legal advice", text)
        self.assertIn("qualified", text)


if __name__ == "__main__":
    unittest.main()
