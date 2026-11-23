---
name: fsl-operations
description: Configure or review Field Service execution, including assets and service contracts, work plans and work steps, inventory (ProductItem, ProductRequest, ProductTransfer, ProductConsumed, ReturnOrder), service reports and signatures, entitlements and warranties, and customer engagement such as Appointment Assistant and self-service booking. Use for anything between dispatch and work order closure.
---

# Field Service assets, work plans, inventory, service reports and customer engagement

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-core, fsl-mobile, fsl-scheduling, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Map lifecycle and access from installed asset and service contract to work order, appointment, work plan, inventory transactions and closure.
2. For inventory follow products, locations, stock balance, requests, transfers, consumption and returns. Verify transaction ownership and reconciliation before custom automation.
3. For steps and reports verify selection rules, templates, sequencing, versioning, signatures, file access and mobile support. For customer engagement verify consent, identity, guest data access and status transitions.
4. Evaluate connected cases, entitlements, warranties, asset history, customer notifications, analytics and Agentforce workflows against the actual Field Service release and org settings.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for service report and Document Builder anchors. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
