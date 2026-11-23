---
name: salesforce-release-watch
description: Assess Salesforce seasonal releases, monthly changes, Field Service package and mobile patch notes, and Release Updates for their impact on an org or codebase. Use when asked what changed, whether a release or enforcement affects a feature, or to plan sandbox preview testing.
---

# Salesforce releases, monthly changes, patch notes and release updates

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among release, fsl-core, delivery. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Open the current official release notes, change log, Field Service notes (including app and package patch links) and Release Updates. Verify preview versus GA and target org release, API, package, app and licensing.
2. Trace announcements to specific files, settings, integrations and personas. Record rollout dates, enforcement dates, feature settings, prerequisites, known issues and evidence URLs.
3. Use a sandbox validation plan with risk, owner, acceptance evidence and rollback.
4. Document exact checked date and items that could not be independently verified.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
