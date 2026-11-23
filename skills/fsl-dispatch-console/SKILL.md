---
name: fsl-dispatch-console
description: Configure, extend or review the Field Service dispatcher console, including the Gantt, appointment list and filters, map, utilization views, bulk and custom actions, custom permissions, palettes and live updates. Use when dispatchers report missing appointments, slow or stale Gantt views or blocked actions, or when adding a custom Gantt action.
---

# Field Service dispatcher console and Gantt

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-dispatch, fsl-scheduling, fsl-security, fsl-apis. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Identify the console in use and its hosting surface, the dispatcher's permission sets, custom permissions and user territories, and the loaded territories and horizon.
2. Trace what feeds each view. Check appointment list filters and field sets, Gantt filters and palettes, utilization settings, and whether live updates are enabled and readable for the user.
3. For custom actions, review the Apex interface or Visualforce contract, bulk behavior, sharing mode, returned messages and error paths. Confirm where the action is registered and who can run it.
4. Test with a dispatcher persona on realistic volume. Include bulk schedule and dispatch, drag and drop, pinned appointments, cross-territory views and the refresh behavior after background changes.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for the custom action contract, temporary appointment lists and console settings. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
