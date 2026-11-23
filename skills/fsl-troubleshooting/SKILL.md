---
name: fsl-troubleshooting
description: Diagnose Field Service problems from symptoms, including no appointment slots or candidates, wrong or missing assignments, failed or partial optimization, maintenance work orders not generated, mobile sync or offline errors, stale Gantt data and permission errors. Use when something in Field Service fails or behaves unexpectedly and the cause is not yet known.
---

# Field Service troubleshooting

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-core, fsl-scheduling, fsl-maintenance, fsl-mobile, fsl-security, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Capture the exact symptom, record IDs, user, time zone, time of occurrence, org release, package version and whether enhanced scheduling applies. Reproduce it before changing anything.
2. Classify the symptom with the reference table and open the matching skill. Check the documented limits and prerequisites before suspecting custom code.
3. Narrow the cause by comparing a working and a failing record, running the same action as another persona, and reading the request or log record the feature writes.
4. Confirm the fix on the original record and on a clean one, and record the cause, evidence and any limit that was reached.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for a symptom table that points to the documented cause to check first. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
