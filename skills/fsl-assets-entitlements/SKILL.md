---
name: fsl-assets-entitlements
description: Design or review Field Service asset and coverage management, including Asset hierarchies and relationships, asset warranties and warranty terms, entitlements and milestones, service contracts and contract line items, product service campaigns and asset history. Use when coverage is not applied to a work order, SLA milestones misfire, or installed-base data is being modeled or migrated.
---

# Field Service assets, warranties, entitlements and contracts

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-core, fsl-maintenance, service, architecture. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Map the installed base, including asset hierarchy, location, account and replacement or upgrade relationships. Identify which record carries warranty and coverage dates.
2. Trace coverage from service contract and contract line item to entitlement, milestone and work order. Establish which automation selects the entitlement and which business hours and time zone drive the milestones.
3. Review warranty terms by product or product family, product service campaigns and their work orders or return orders, and how maintenance plans reference assets and contracts.
4. Test expired and overlapping coverage, asset transfer between accounts, milestone pause and restart, and work orders created from each channel.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
