---
name: fsl-architecture
description: Design or review an end-to-end Salesforce Field Service (FSL) solution covering WorkOrder, WorkOrderLineItem, ServiceAppointment, WorkType, ServiceTerritory, ServiceResource, skills, shifts and operating hours, and the boundary between core, the Field Service managed package, the scheduling engine, the mobile app and custom code. Use for Field Service data-model, lifecycle, licensing or configure-versus-build decisions.
---

# Field Service architecture and end-to-end configuration

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-core, architecture, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Map work orders, line items, appointments, work types, assets, locations, service territories, resource memberships, shifts/operating hours, skills and assigned resources. Identify ownership, sharing and routing boundaries.
2. Walk intake → work planning → booking → dispatch → mobile execution → service report → closure. Review work plans and steps, entitlements, assets, inventory, warranties, crews, maps, reporting and customer communications where relevant.
3. Identify which behavior comes from Salesforce core, the Field Service managed package, the scheduling engine, the mobile app, or custom automation. Verify availability and distinguish Field Service scheduling from Salesforce Scheduler.
4. Compare native configuration, Flow and custom implementation. Record decision triggers, package and licensing assumptions, migration of existing records, monitoring and fallback.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for product layers, prerequisites and documented limits. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
