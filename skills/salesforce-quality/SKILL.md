---
name: salesforce-quality
description: Audit a Salesforce implementation before merge or release, including acceptance-criteria traceability, Apex, Jest and Flow test runs, Salesforce Code Analyzer, regression scope and 2GP packaging readiness. Use for code review, pre-deployment checks or when asked whether a change is ready to ship.
---

# Implementation audit, Salesforce Code Analyzer, regression and delivery

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among delivery, architecture, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Read the work item and acceptance criteria, inspect the repo and record baseline test status. Trace each acceptance criterion to implementation and test evidence.
2. Review design, newest applicable official guidance, security, performance, rollback and behavior through normal UI/API paths. Record severity and location for each confirmed finding.
3. Apply scoped fixes when requested, run targeted Apex/Jest/Flow checks and Code Analyzer where installed, then run the relevant regression suite and report exact commands and outcomes.
4. For 2GP inspect dependencies, namespace, package version, metadata coverage, install/upgrade behavior and post-deploy steps. Use only an explicitly authorized sandbox or scratch org for validation.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
