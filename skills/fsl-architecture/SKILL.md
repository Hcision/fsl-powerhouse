---
name: fsl-architecture
description: Field Service architecture and end-to-end configuration. Use when the request or implementation touches these areas.
---

# Field Service architecture and end-to-end configuration

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from fsl-core, architecture, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Map work orders, line items, appointments, work types, assets, locations, service territories, resource memberships, shifts/operating hours, skills and assigned resources. Identify ownership, sharing and routing boundaries.
2. Walk intake → work planning → booking → dispatch → mobile execution → service report → closure. Review work plans and steps, entitlements, assets, inventory, warranties, crews, maps, reporting and customer communications where relevant.
3. Identify which behavior comes from Salesforce core, the Field Service managed package, the scheduling engine, the mobile app, or custom automation. Verify availability and distinguish Field Service scheduling from Salesforce Scheduler.
4. Compare native configuration, Flow and custom implementation. Record decision triggers, package and licensing assumptions, migration of existing records, monitoring and fallback.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
