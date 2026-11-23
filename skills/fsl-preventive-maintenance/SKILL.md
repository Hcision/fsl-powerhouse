---
name: fsl-preventive-maintenance
description: Maintenance plans, preventive maintenance, recurrence and volume. Use when the request or implementation touches these areas.
---

# Maintenance plans, preventive maintenance, recurrence and volume

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from fsl-maintenance, fsl-core, apex, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Trace Maintenance Plan → Maintenance Asset and Maintenance Work Rule → work orders, line items and appointments. Verify which level owns each recurrence rule and which date acts as the generation cursor.
2. Distinguish plan generation settings, work type defaults, recurrence, generation horizon and appointment creation. Verify the target version and native behavior with representative sandbox data.
3. Build a matrix for multi-asset plans, overlapping recurrence, edits to active plans, time zones, month end, cutoff dates, duplicate prevention, retries, partial failures, locking and high-volume batches.
4. Where a custom Builder, projection or simulation exists, compare its output with operational generation for identical inputs. Treat custom limits and job cadence as project-specific until measured.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
