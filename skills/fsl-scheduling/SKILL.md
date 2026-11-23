---
name: fsl-scheduling
description: Field Service scheduling, booking, dispatch and optimization. Use when the request or implementation touches these areas.
---

# Field Service scheduling, booking, dispatch and optimization

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from fsl-scheduling, fsl-core, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Confirm engine generation, optimization mode, scheduling policy, staffing model, time zone, travel assumptions, territory membership, availability, calendars and capacity.
2. Trace eligibility rules separately from scored objectives. Evaluate resource absences, overtime, work windows, shifts, crews, dependencies, emergency work, travel and dispatcher overrides.
3. For appointment booking, trace availability lookup, displayed slots, booking, rescheduling, cancellation and confirmation. Verify the actual API contract, arrival window semantics, reassignment and concurrent requests.
4. Build a same-data scenario matrix across booking, dispatcher console and optimization. Include DST, boundaries, travel, absences, sparse availability, conflicting constraints and no-slot behavior.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
