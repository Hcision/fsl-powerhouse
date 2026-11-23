---
name: fsl-scheduling
description: Configure, debug or review Field Service scheduling, including scheduling policies, work rules and service objectives, appointment booking and arrival windows, dispatcher console and Gantt, optimization (including Enhanced Scheduling and Optimization), travel, crews, absences and capacity. Use when appointments get no slots or the wrong resource or time, or when calling scheduling Apex or REST APIs.
---

# Field Service scheduling, booking, dispatch and optimization

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-scheduling, fsl-core, release. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Confirm engine generation, optimization mode, scheduling policy, staffing model, time zone, travel assumptions, territory membership, availability, calendars and capacity.
2. Trace eligibility rules separately from scored objectives. Evaluate resource absences, overtime, work windows, shifts, crews, dependencies, emergency work, travel and dispatcher overrides.
3. For appointment booking, trace availability lookup, displayed slots, booking, rescheduling, cancellation and confirmation. Verify the actual API contract, arrival window semantics, reassignment and concurrent requests.
4. Build a same-data scenario matrix across booking, dispatcher console and optimization. Include DST, boundaries, travel, absences, sparse availability, conflicting constraints and no-slot behavior.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for FSL Apex entry points, the booking sequence and ESO differences. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
