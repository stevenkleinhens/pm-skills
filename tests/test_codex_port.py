"""Codex-specific packaging and explicit-invocation invariants."""

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
PACKAGES = ROOT / "codex-packages"
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
            path = PACKAGES / name / ".codex-plugin" / "plugin.json"
            self.assertTrue(path.is_file(), f"missing {path}")
            manifest = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["name"], name)
            self.assertEqual(manifest["version"], version)
            self.assertEqual(manifest["skills"], "./skills/")

    def test_marketplace_installs_isolated_codex_packages(self):
        marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
        sources = {plugin["name"]: plugin["source"] for plugin in marketplace["plugins"]}
        for name in PLUGINS:
            self.assertEqual(sources[name], f"./codex-packages/{name}")

    def test_each_plugin_exposes_exactly_one_codex_entrypoint(self):
        for name in PLUGINS:
            root = PACKAGES / name / "skills"
            entries = sorted(p.name for p in root.iterdir() if p.is_dir())
            self.assertEqual(entries, [name])
            skill = root / name / "SKILL.md"
            self.assertEqual(frontmatter(skill)["name"], name)

    def test_packages_cannot_trigger_legacy_command_migration(self):
        for name in PLUGINS:
            package = PACKAGES / name
            self.assertFalse((package / "commands").exists())
            registered = sorted(package.rglob("SKILL.md"))
            self.assertEqual(registered, [package / "skills" / name / "SKILL.md"])
            self.assertTrue((package / "LICENSE").is_file())
            self.assertIn("Paweł Huryn", (package / "UPSTREAM.md").read_text())

    def test_original_plugin_sources_keep_their_commands_and_frameworks(self):
        for name in PLUGINS:
            self.assertTrue(any((ROOT / name / "commands").glob("*.md")))
            self.assertTrue(any((ROOT / name / "skills").glob("*/SKILL.md")))
            self.assertFalse((ROOT / name / ".codex-plugin").exists())
            self.assertFalse((ROOT / name / "codex-skills").exists())

    def test_legacy_registered_workflow_wrappers_are_removed(self):
        for path in LEGACY_CODEX_WRAPPERS:
            self.assertFalse(path.exists(), f"legacy wrapper remains: {path}")


class TestExplicitInvocation(unittest.TestCase):
    def test_every_entrypoint_is_explicit_only(self):
        for name in PLUGINS:
            metadata = (
                PACKAGES
                / name
                / "skills"
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
                PACKAGES / name / "skills" / name / "SKILL.md"
            ).read_text(encoding="utf-8")
            commands = sorted((ROOT / name / "commands").glob("*.md"))
            self.assertTrue(commands, f"no commands found for {name}")
            for command in commands:
                reference = f"../../references/workflows/{command.name}"
                self.assertIn(reference, body, f"{name} does not route {command.name}")
                self.assertTrue(
                    (PACKAGES / name / "references" / "workflows" / command.name).is_file()
                )
            self.assertIn("../../references/frameworks/", body)

    def test_source_workflows_do_not_expand_authority(self):
        for name in PLUGINS:
            body = (
                PACKAGES / name / "skills" / name / "SKILL.md"
            ).read_text(encoding="utf-8")
            self.assertIn("do not grant permission", body)
            self.assertIn("Claude-specific", body)

    def test_copied_workflows_are_explicitly_non_authorizing(self):
        for name in PLUGINS[:-1]:
            for path in (PACKAGES / name / "references" / "workflows").glob("*.md"):
                body = path.read_text(encoding="utf-8")
                self.assertIn("non-authorizing methodology", body)
                self.assertIn("do not execute its operational directions directly", body)


class TestSafetyBoundaries(unittest.TestCase):
    def test_ai_shipping_defaults_to_check_only(self):
        path = (
            PACKAGES
            / "pm-ai-shipping"
            / "skills"
            / "pm-ai-shipping"
            / "SKILL.md"
        )
        text = path.read_text(encoding="utf-8").lower()
        self.assertIn("check-only", text)
        self.assertIn("explicit approval", text)
        self.assertIn("subagent", text)
        self.assertIn("../../references/frameworks/code-review/guide.md", text)

    def test_ai_shipping_uses_safe_codex_workflows_not_raw_commands(self):
        root = PACKAGES / "pm-ai-shipping" / "references" / "workflows"
        ship_check = (root / "ship-check.md").read_text(encoding="utf-8").lower()
        self.assertIn("check-only", ship_check)
        self.assertIn("explicitly approves delegation", ship_check)
        self.assertNotIn("pre-approved", ship_check)
        self.assertNotIn("run `/", ship_check)
        for path in root.glob("*.md"):
            body = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("parallel subagents", body)
            self.assertNotIn("reports are always written", body)

    def test_legal_drafts_require_review(self):
        path = (
            PACKAGES / "pm-toolkit" / "skills" / "pm-toolkit" / "SKILL.md"
        )
        text = path.read_text(encoding="utf-8").lower()
        self.assertIn("legal advice", text)
        self.assertIn("qualified", text)


if __name__ == "__main__":
    unittest.main()
