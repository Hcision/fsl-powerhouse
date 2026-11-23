---
name: salesforce-security
description: Defensive Salesforce security and access review. Use when the request or implementation touches these areas.
---

# Defensive Salesforce security and access review

Read `../../knowledge/research-protocol.md` relative to this file. Select only the source catalog topics needed from architecture, apex, lwc, fsl-core. Follow links to the specific official page and record the verification date, applicability and environment. Ask for missing decisive evidence when it blocks a safe implementation.

1. Build an actor/object/field/record access matrix including dispatchers, technicians, admins, integrations and guest users when applicable.
2. Inspect sharing and execution mode, CRUD/FLS, Apex and Flow entry points, guest record exposure, file access, dynamic query construction and credentials. Verify the specific API’s current security behavior.
3. Review logging, secret handling, data retention and least-privilege permissions. Document exposure and remediation with code or configuration evidence.
4. Verify fixes with controlled unit/sandbox permission tests using synthetic records and intended personas.

Return decisions and findings with source URLs, implementation evidence, checks performed and unresolved items.
