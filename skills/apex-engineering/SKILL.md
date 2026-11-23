---
name: apex-engineering
description: Apex, SOQL, async processing, integrations and automated tests. Use when the request or implementation touches these areas.
---

# Apex, SOQL, async processing, integrations and automated tests

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from apex, platform, architecture, delivery. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Trace transaction boundaries, entry points, sharing and user permissions. Model query, DML, CPU, heap and callout budgets with realistic record counts.
2. Review trigger bulkification, recursion and re-entry, collection use, query selectivity, error handling, locking and retry idempotency. Select asynchronous primitives using current documented semantics.
3. Verify user-context data access, field and object permissions and bulk partial-success behavior. For cross-system work, check named credentials, retries, idempotency, ordering and monitoring.
4. Assert outcomes for single and bulk operations, access failures, empty and legacy data, errors and retries. Use mock callouts and deterministic fixtures where relevant.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
