---
name: fsl-analytics
description: Design or review Field Service reporting, including custom report types, dashboards, the Field Service Analytics app, Field Service Intelligence, optimization insights and KPIs such as first-time fix rate, utilization, travel time and SLA compliance. Use when defining field service KPIs, when numbers disagree between reports, or when sizing an analytics rollout.
---

# Field Service analytics, reporting and KPIs

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-analytics, fsl-core, fsl-scheduling. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Define each KPI with its formula, source objects and fields, time zone, and the status values that count. Record who owns the definition.
2. Choose the surface per audience among standard reports, the dispatcher console utilization views, optimization insights and CRM Analytics apps. Check licenses and permissions for each.
3. Trace data quality back to execution. Check status transitions, actual times, travel records, cannot-complete reasons and parts consumption that the KPI depends on.
4. Reconcile a sample period by hand against the dashboard, and document known gaps and refresh timing.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for the analytics apps, their permissions and the documented metric targets. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
