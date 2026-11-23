---
name: fsl-workforce-territories
description: Design or review the Field Service workforce model, including ServiceResource, ServiceCrew, skills, ServiceTerritory hierarchies and ServiceTerritoryMember types, operating hours and time slots, shifts, resource absences, capacity-based resources and contractors. Use when resources are missing from the Gantt, availability looks wrong, or territories, crews or shifts are being set up or restructured.
---

# Field Service workforce, territories and availability

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-workforce, fsl-core, fsl-scheduling, fsl-security. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Inventory service resources by type, user link, active flag, license and location. Map each to its primary, secondary and relocation memberships with their date ranges and operating hours.
2. Trace availability from territory operating hours through member-level hours, time slots, shifts and absences. State which layer wins for the date in question and in which time zone.
3. Check territory design against the sizing guidelines, the hierarchy, polygon or address assignment and the work rules that read membership. Review crews, skill levels and expiry, and capacity-based or contractor resources against their restrictions.
4. Test membership changes mid-day, overlapping secondary memberships, relocation periods, shifts crossing midnight or DST, and resources deactivated with future appointments.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for membership types, shift and capacity restrictions and territory sizing guidance. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
