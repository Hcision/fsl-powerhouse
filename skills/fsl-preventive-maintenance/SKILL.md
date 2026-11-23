---
name: fsl-preventive-maintenance
description: Design, debug or review Field Service preventive maintenance, including MaintenancePlan, MaintenanceAsset, MaintenanceWorkRule, recurrence patterns, generation timeframe and horizon, work order and appointment auto-generation, and custom builders, projections or simulations built on them. Use for wrong, duplicate or missing generated work orders, date drift, or high-volume generation.
---

# Maintenance plans, preventive maintenance, recurrence and volume

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-maintenance, fsl-core, apex, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Trace Maintenance Plan → Maintenance Asset and Maintenance Work Rule → work orders, line items and appointments. Verify which level owns each recurrence rule and which date acts as the generation cursor.
2. Distinguish plan generation settings, work type defaults, recurrence, generation horizon and appointment creation. Verify the target version and native behavior with representative sandbox data.
3. Build a matrix for multi-asset plans, overlapping recurrence, edits to active plans, time zones, month end, cutoff dates, duplicate prevention, retries, partial failures, locking and high-volume batches.
4. Where a custom Builder, projection or simulation exists, compare its output with operational generation for identical inputs. Treat custom limits and job cadence as project-specific until measured.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for object and field anchors, generation behavior and known traps. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
