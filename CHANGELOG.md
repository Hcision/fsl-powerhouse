# Changelog

## 0.3.0

- A skill for every Field Service area: workforce and territories, dispatcher console, inventory, assets and coverage, customer engagement, licenses and access, APIs and integration, analytics, Agentforce and troubleshooting, next to the existing architecture, scheduling, maintenance, mobile and operations skills.
- Fourteen reference files of facts read from official Salesforce pages, including documented limits.
- `knowledge/fsl-topic-map.md` lists every area, its skill and whether it has a verified reference.
- Two new read-only agents: `field-service-troubleshooter` and `field-service-operations-reviewer`.
- Ticket delivery no longer assumes Jira. It works from any connected tracker or from pasted ticket text.
- Source catalog grows from 39 to 95 official entries.
- Contribution guide, issue and pull request templates.

## 0.2.0

- Plugin paths use `${CLAUDE_PLUGIN_ROOT}`. Agents preload their skills. Reviewers are read-only.
- Verified references for scheduling and preventive maintenance.
- Scripts that depended on unavailable tools are removed. MIT license added.

## 0.1.0

- Initial release.
