import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("monitor", ROOT / "scripts/monitor_sources.py")
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)


class RepoTest(unittest.TestCase):
    def test_manifests_and_catalog(self):
        metadata, market = [
            json.loads((ROOT / ".claude-plugin" / file).read_text())
            for file in ("plugin.json", "marketplace.json")
        ]
        self.assertEqual(metadata["name"], market["plugins"][0]["name"])
        self.assertEqual(ROOT, (ROOT / market["plugins"][0]["source"]).resolve())
        sources = json.loads((ROOT / "knowledge/sources.json").read_text())
        self.assertEqual(len(sources), len({source["id"] for source in sources}))
        self.assertTrue(all(monitor.official(source["url"]) for source in sources))
        self.assertTrue(any(source["id"] == "fsl-release" and source["monitor"] for source in sources))

    def test_frontmatter_and_agent_skill_references(self):
        skills = {path.parent.name: path for path in ROOT.glob("skills/*/SKILL.md")}
        agents = {path.stem: path for path in ROOT.glob("agents/*.md")}
        self.assertGreaterEqual(len(skills), 13)
        self.assertGreaterEqual(len(agents), 11)
        for name, path in list(skills.items()) + list(agents.items()):
            content = path.read_text()
            frontmatter = re.match(r"^---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n", content)
            self.assertIsNotNone(frontmatter, path)
            self.assertEqual(name, frontmatter[1])
            self.assertLessEqual(len(content.splitlines()), 500)
        for path in agents.values():
            listed = re.search(r"playbooks from (.+?)\. Use", path.read_text())
            self.assertIsNotNone(listed, path)
            self.assertTrue(set(listed[1].split(", ")).issubset(skills), path)

    def test_fingerprint_ignores_scripts_and_detects_text_changes(self):
        body = "<main>" + "Field Service scheduling documentation " * 12 + "</main>"
        self.assertEqual(monitor.fingerprint(body), monitor.fingerprint(body + "<script>x</script>"))
        self.assertNotEqual(monitor.fingerprint(body), monitor.fingerprint(body + "<p>Updated</p>"))
        with self.assertRaises(ValueError):
            monitor.fingerprint("<p>Unavailable</p>")

    def test_monitor_host_validation(self):
        self.assertTrue(monitor.official("https://help.salesforce.com/path"))
        for url in ("http://help.salesforce.com", "https://help.salesforce.com.example.org",
                    "https://help.salesforce.com@example.org"):
            self.assertFalse(monitor.official(url))


if __name__ == "__main__":
    unittest.main()
