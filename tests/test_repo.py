import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OFFICIAL_HOSTS = {
    "resources.docs.salesforce.com", "help.salesforce.com", "developer.salesforce.com", "architect.salesforce.com",
    "issues.salesforce.com", "trailhead.salesforce.com",
}
FRONTMATTER = re.compile(r"^---\n(.+?)\n---\n", re.S)


def official(url):
    parts = urlsplit(url)
    return parts.scheme == "https" and parts.netloc in OFFICIAL_HOSTS


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
            self.assertEqual({"topic", "id", "title", "url"}, set(source), source)
            self.assertTrue(official(source["url"]), source)

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
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        counts = {"agents": len(self.agents), "skills": len(self.skills)}
        for path in ("README.md", "assets/banner.svg"):
            content = (ROOT / path).read_text(encoding="utf-8")
            for label, expected in counts.items():
                shown = {int(n) for n in re.findall(rf"(\d+) {label}\b", content)}
                shown |= {int(n) for n in re.findall(rf"badge/{label}-(\d+)-", content)}
                self.assertEqual({expected}, shown, f"{path}: {label}")
        for name in list(self.agents) + list(self.skills):
            self.assertIn(f"`{name}`", readme, f"README does not list {name}")

    def test_field_service_topic_map_and_references(self):
        topic_map = (ROOT / "knowledge/fsl-topic-map.md").read_text(encoding="utf-8")
        for name, path in self.skills.items():
            reference = path.parent / "reference.md"
            if name.startswith("fsl-"):
                expected = "Yes" if reference.is_file() else "Not yet"
                row = re.search(rf"\| `{name}` \|.*\| ({expected}) \|", topic_map)
                self.assertIsNotNone(row, f"topic map row for {name} should end with {expected}")
            if reference.is_file():
                content = reference.read_text(encoding="utf-8")
                self.assertRegex(content, r"on 20\d\d-\d\d-\d\d", f"{reference}: state when it was read")
                self.assertIn("reference.md", path.read_text(encoding="utf-8"), f"{path} does not point to its reference")
                for url in re.findall(r"\]\((https?://[^)\s]+)\)", content):
                    self.assertTrue(official(url), f"{reference}: {url}")

    def test_official_host_validation(self):
        self.assertTrue(official("https://help.salesforce.com/path"))
        for url in ("http://help.salesforce.com", "https://help.salesforce.com.example.org",
                    "https://help.salesforce.com@example.org"):
            self.assertFalse(official(url))


if __name__ == "__main__":
    unittest.main()
