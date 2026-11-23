---
name: fsl-security-licensing
description: Review or set up Field Service access, including permission set licenses, the managed package permission sets per persona, custom permissions, sharing for work orders, service appointments, resources and territories, user territories and contractor or community access. Use when a user cannot see the Gantt, book, be scheduled or open the mobile app, or before changing org-wide defaults.
---

# Field Service licenses, permission sets and record access

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-security, fsl-core, fsl-workforce, architecture. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Build a persona matrix for admin, dispatcher, call center agent, technician, contractor and customer. Record user license, permission set licenses, permission sets and custom permissions for each.
2. Review org-wide defaults and sharing for the core Field Service objects, user territories and any custom sharing. Confirm that dispatchers keep read and write access to the appointments they manage.
3. Check that every scheduled resource holds the license the engine requires, that inactive or unlicensed users are not on the Gantt, and that community users have the right site license.
4. Test each persona end to end with synthetic records, including a user who should be denied. Re-run after package upgrades, because permission sets can need a refresh.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for the license and permission set names and what each one unlocks. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
