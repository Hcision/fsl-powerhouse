---
name: fsl-inventory
description: Design or review Field Service inventory, including Location, ProductItem, ProductItemTransaction, ProductRequired, ProductRequest, ProductTransfer, ProductConsumed, ReturnOrder, shipments, van stock and serialized products. Use when stock quantities drift, parts are missing on site, or when integrating inventory with an ERP or warehouse system.
---

# Field Service inventory and parts

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-inventory, fsl-core, fsl-mobile, fsl-apis. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Map locations, including vans and warehouses, to product items and owners. Establish the system of record for stock and how quantity on hand is adjusted.
2. Walk the part lifecycle from product required through request, transfer, receipt, consumption and return. Identify which record changes quantity at each step and which user permission each step needs.
3. For serialized stock, check one product item per serial and the transfer flow. For integrations, check idempotency, ordering, partial receipts and reconciliation between systems.
4. Test over-consumption, transfers in transit, returns of unused parts, mobile entry while offline and concurrent updates to the same product item.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for the inventory objects, who changes quantity and the permissions each step needs. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
