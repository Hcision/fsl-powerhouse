---
name: fsl-customer-engagement
description: Configure or review customer-facing Field Service features, including Appointment Assistant real-time location and self-service scheduling, Experience Cloud booking pages, customer notifications and messaging, and Visual Remote Assistant. Use when customers cannot book, reschedule or track a technician, or when a guest-facing booking flow is being built or audited.
---

# Field Service customer engagement and self-service

Read `${CLAUDE_PLUGIN_ROOT}/knowledge/research-protocol.md`. From `${CLAUDE_PLUGIN_ROOT}/knowledge/sources.json`, select only the topics needed among fsl-customer, fsl-scheduling, fsl-security, fsl-mobile. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Confirm which add-on packages and licenses are installed and assigned, the Experience Cloud site and guest or authenticated access model, and the messaging channel used.
2. Trace the booking journey through identity verification, work type selection, slot lookup, booking, reschedule, cancel and confirmation. Identify the flow, scheduling policy and operating hours behind each step.
3. For real-time location, check geolocation collection settings, when sharing starts and stops, the messaging components and the data a customer link exposes.
4. Test as a guest and as an authenticated customer. Include expired links, repeated code requests, no available slots, concurrent bookings of the same slot and status transitions that trigger messages.

Before searching, read `${CLAUDE_SKILL_DIR}/reference.md` for Appointment Assistant prerequisites, settings and known conflicts. Re-verify any anchor that a decision depends on.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
