# FSL Powerhouse

A Claude Code plugin for source-grounded Salesforce delivery. Field Service is the main focus, with workflows for architecture, scheduling and optimization, preventive maintenance, mobile/offline, and service operations. The platform skills cover Apex, LWC JavaScript/HTML/CSS, Flow, configuration, security, testing, packaging, releases and Jira-to-code delivery.

## Quick start

Extract the repository. From the directory containing it, run:

```sh
claude --plugin-dir ./fsl-powerhouse
```

Or register the local repository from an active Claude Code session using its full path:

```text
/plugin marketplace add /absolute/path/to/fsl-powerhouse
/plugin install fsl-powerhouse@fsl-powerhouse
```

Try: “Use the FSL Powerhouse to review the scheduling flow in this repo. Determine which engine and policy it uses, verify the applicable Salesforce docs, and give me a test matrix.” For the maintenance package, give Claude the Jira IDs and use the ticket delivery and preventive maintenance skills. Jira and web access depend on your Claude Code environment.

## What's included

| Path | Purpose |
| --- | --- |
| `agents/` | Eleven specialists for architecture, development, Field Service, security, QA and releases |
| `skills/` | Fifteen task-specific playbooks with evidence and validation requirements |
| `knowledge/sources.json` | Curated official reference catalog |
| `knowledge/research-protocol.md` | Documentation workflow and Field Service topic map |
| `knowledge/release-baseline.md` | Initial release baseline and verified November Field Service changes |
| `scripts/monitor_sources.py` | Optional manual monitoring for changes to selected official pages |
| `tests/` | Catalog, manifest, agent-reference and monitor tests |

## Live documentation lookup

The plugin searches Salesforce's official websites when you ask about Field Service, Service Cloud, Agentforce or the Salesforce platform. It needs web search and fetch access in your Claude Code session. It starts with one precise search and up to two official pages per question, asks for the relevant sections, and reads more when evidence is missing. The source catalog is a set of starting points. The search can follow official documentation beyond those links.

Try asking Claude: “Use live Salesforce documentation to explain how to test an Agentforce agent. Cite the current Testing Center guidance and check whether it applies to Agentforce for Field Service.”

The importer and local search scripts from the earlier version are available for existing users as optional tools. Live mode requires no local document import, index or refresh schedule.

Run repository validation with `python3 -m unittest discover -s tests -v`.

## Design references

[Craft Anything](https://github.com/storytold/craft-anything) informs the research-first workflow. [ECC](https://github.com/affaan-m/ECC) informs the modular agents and skills structure and the practice of writing a handoff before context compaction. The plugin uses original Salesforce playbooks.

Claude Code format references: [plugins](https://code.claude.com/docs/en/plugins-reference) and [plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

## Lightning Knowledge and Agentforce

Use the `salesforce-knowledge-grounding` skill to plan Lightning Knowledge article publishing, Agentforce Data Library setup and persona-based retrieval tests. For example, ask it to design a missing-part procedure for technicians and validate when the agent should answer or escalate.

Public Salesforce documentation is fetched live. Consulting your org’s private Knowledge articles requires an authorized org connection.

## SkillSpector static scan

From a clean checkout, run `skillspector scan . --no-llm --use-shipped-baseline --show-suppressed --fail-on-incomplete`. The checked-in baseline records two reviewed calls to the optional `sf-docs` CLI by exact fingerprint. Run without `--use-shipped-baseline` to see all raw findings. Review any new finding before changing the baseline.
