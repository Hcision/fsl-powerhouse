---
name: salesforce-quality
description: Implementation audit, Salesforce Code Analyzer, regression and delivery. Use when the request or implementation touches these areas.
---

# Implementation audit, Salesforce Code Analyzer, regression and delivery

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from delivery, architecture, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Read the work item and acceptance criteria, inspect the repo and record baseline test status. Trace each acceptance criterion to implementation and test evidence.
2. Review design, newest applicable official guidance, security, performance, rollback and behavior through normal UI/API paths. Record severity and location for each confirmed finding.
3. Apply scoped fixes when requested, run targeted Apex/Jest/Flow checks and Code Analyzer where installed, then run the relevant regression suite and report exact commands and outcomes.
4. For 2GP inspect dependencies, namespace, package version, metadata coverage, install/upgrade behavior and post-deploy steps. Use only an explicitly authorized sandbox or scratch org for validation.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
