import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import monitor_sources as monitor  # noqa: E402
import search_docs  # noqa: E402

FRONTMATTER = re.compile(r"^---\n(.+?)\n---\n", re.S)
NUMBERS = {"eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16}


def frontmatter(path):
    """Parse the flat subset of YAML used here: scalars and one-level lists."""
    block = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    assert block, f"Missing frontmatter in {path}"
    fields, key = {}, None
    for line in block[1].splitlines():
        if line.startswith("  - "):
            fields[key].append(line[4:].strip())
        else:
            key, _, value = line.partition(": ")
            key = key.rstrip(":")
            fields[key] = value.strip() if value else []
    return fields


class RepoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        cls.sources = json.loads((ROOT / "knowledge/sources.json").read_text(encoding="utf-8"))
        cls.skills = {path.parent.name: path for path in ROOT.glob("skills/*/SKILL.md")}
        cls.agents = {path.stem: path for path in ROOT.glob("agents/*.md")}

    def test_manifests_and_catalog(self):
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(self.plugin["name"], market["plugins"][0]["name"])
        self.assertEqual(ROOT, (ROOT / market["plugins"][0]["source"]).resolve())
        self.assertEqual(len(self.sources), len({source["id"] for source in self.sources}))
        self.assertEqual(len(self.sources), len({source["url"] for source in self.sources}))
        for source in self.sources:
            self.assertEqual({"topic", "id", "title", "url", "monitor"}, set(source), source)
            self.assertIsInstance(source["monitor"], bool, source)
            self.assertTrue(monitor.official(source["url"]), source)
        self.assertTrue(any(source["id"] == "fsl-release" and source["monitor"] for source in self.sources))

    def test_frontmatter(self):
        self.assertGreaterEqual(len(self.skills), 13)
        self.assertGreaterEqual(len(self.agents), 11)
        for name, path in list(self.skills.items()) + list(self.agents.items()):
            fields = frontmatter(path)
            self.assertEqual(name, fields["name"], path)
            description = fields["description"]
            self.assertIn("Use ", description, f"{path}: say when to use it")
            self.assertNotIn(": ", description, f"{path}: unquoted colon breaks YAML")
            self.assertLessEqual(len(description), 1024, path)
            self.assertLessEqual(len(path.read_text(encoding="utf-8").splitlines()), 500)

    def test_agents_preload_existing_skills(self):
        prefix = self.plugin["name"] + ":"
        for path in self.agents.values():
            fields = frontmatter(path)
            self.assertTrue(fields.get("skills"), path)
            for skill in fields["skills"]:
                self.assertTrue(skill.startswith(prefix), f"{path}: {skill}")
                self.assertIn(skill[len(prefix):], self.skills, path)
            read_only = "Read-only" in fields["description"]
            self.assertEqual(read_only, "disallowedTools" in fields, f"{path}: reviewers must not edit")

    def test_knowledge_references_resolve(self):
        topics = {source["topic"] for source in self.sources}
        ids = {source["id"] for source in self.sources}
        for path in list(self.skills.values()) + list(self.agents.values()):
            content = path.read_text(encoding="utf-8")
            self.assertNotIn("../", content, f"{path}: use ${{CLAUDE_PLUGIN_ROOT}}")
            for target in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+\.\w+)", content):
                self.assertTrue((ROOT / target).is_file(), f"{path}: {target}")
            for target in re.findall(r"\$\{CLAUDE_SKILL_DIR\}/([\w./-]+\.\w+)", content):
                self.assertTrue((path.parent / target).is_file(), f"{path}: {target}")
            listed = re.search(r"topics needed among ([a-z, -]+)\.", content)
            if listed:
                self.assertLessEqual(set(listed[1].split(", ")), topics, path)
        protocol = (ROOT / "knowledge/research-protocol.md").read_text(encoding="utf-8")
        rows = [line.split("|")[2] for line in protocol.splitlines() if line.startswith("| ")][2:]
        self.assertTrue(rows)
        for row in rows:
            self.assertLessEqual(set(row.strip().split(", ")), ids, row)

    def test_readme_counts(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
        for label, items in (("specialists", self.agents), ("task-specific playbooks", self.skills)):
            word = re.search(rf"(\w+) {label}", readme)
            self.assertIsNotNone(word, label)
            self.assertEqual(NUMBERS[word[1]], len(items), label)

    def test_sections_ignore_headings_inside_code_fences(self):
        markdown = "intro\n# Setup\ntext\n```sh\n# not a heading\nrun\n```\n## Next\nmore"
        self.assertEqual(["Overview", "Setup", "Next"], [heading for heading, _ in search_docs.sections(markdown)])

    def test_fingerprint_ignores_scripts_and_detects_text_changes(self):
        body = "<main>" + "Field Service scheduling documentation " * 12 + "</main>"
        self.assertEqual(monitor.fingerprint(body), monitor.fingerprint(body + "<script>x</script>"))
        self.assertNotEqual(monitor.fingerprint(body), monitor.fingerprint(body + "<p>Updated</p>"))
        with self.assertRaises(ValueError):
            monitor.fingerprint("<p>Unavailable</p>")

    def test_probe_renders_pages_that_are_only_a_script_shell(self):
        url = "https://help.salesforce.com/s/articleView?id=x"
        shell = lambda _: "<body><p>Loading</p><script>app()</script></body>"  # noqa: E731
        article = "Field Service release notes " * 20
        digest = monitor.probe(url, renderer=lambda _: article, download=shell)
        self.assertEqual("rendered:" + monitor.text_fingerprint(article), digest)
        with self.assertRaisesRegex(monitor.ThinPage, "sf-docs"):
            monitor.probe(url, download=shell)
        with self.assertRaises(monitor.ThinPage):
            monitor.probe(url, renderer=lambda _: "Loading", download=shell)
        static = "<main>" + "Apex Developer Guide " * 20 + "</main>"
        self.assertEqual(monitor.fingerprint(static),
                         monitor.probe(url, renderer=self.fail, download=lambda _: static))

    def test_monitor_host_validation(self):
        self.assertTrue(monitor.official("https://help.salesforce.com/path"))
        for url in ("http://help.salesforce.com", "https://help.salesforce.com.example.org",
                    "https://help.salesforce.com@example.org"):
            self.assertFalse(monitor.official(url))


if __name__ == "__main__":
    unittest.main()
