# Field Service topic map

Every Field Service area and the skill that covers it. A skill is a playbook of what to check. A reference is a file of facts read from official Salesforce pages, with the date and the links.

| Area | Skill | Covers | Verified reference |
| --- | --- | --- | --- |
| Product model, layers, limits | `fsl-architecture` | Core versus managed package versus mobile, prerequisites, documented limits, work order and appointment lifecycle | Yes |
| Workforce and territories | `fsl-workforce-territories` | Resources, crews, skills, territory membership, operating hours, shifts, absences, capacity, contractors | Yes |
| Scheduling and optimization | `fsl-scheduling` | Policies, work rules, objectives, booking, FSL Apex, optimization, complex work, bundling, enhanced engine | Yes |
| Dispatcher console | `fsl-dispatch-console` | Gantt, lists and filters, map, utilization, custom actions, custom permissions | Yes |
| Preventive maintenance | `fsl-preventive-maintenance` | Maintenance plans, assets, work rules, recurrence, generation and limits | Yes |
| Mobile and offline | `fsl-mobile-offline` | Mobile app, LWC offline, priming, deep linking, service documents, sync | Yes |
| Service execution | `fsl-operations` | Work plans and steps, service reports, Document Builder, closure | Yes |
| Inventory and parts | `fsl-inventory` | Locations, product items, requests, transfers, consumption, returns, serialized stock | Yes |
| Assets and coverage | `fsl-assets-entitlements` | Asset hierarchy, warranties, entitlements, milestones, service contracts, product service campaigns | Not yet |
| Customer engagement | `fsl-customer-engagement` | Appointment Assistant, real-time location, self-service scheduling, messaging, Visual Remote Assistant | Yes |
| Licenses and access | `fsl-security-licensing` | Permission set licenses, persona permission sets, sharing, user territories, contractor access | Yes |
| APIs, integration, data, deployment | `fsl-integration-data` | REST resources, standard actions, FSL Apex, managed triggers, data loads, moving configuration | Yes |
| Analytics and KPIs | `fsl-analytics` | Report types, dashboards, optimization insights, Field Service Analytics and Intelligence | Yes |
| Agentforce and AI | `fsl-agentforce-ai` | Agent in the mobile app, agent-callable actions, grounding and testing | Yes |
| Troubleshooting | `fsl-troubleshooting` | Symptom table that points to the documented cause and the right skill | Yes |

## How to read the last column

"Yes" means the skill ships a `reference.md` whose statements were read on an official page. It does not mean the area is fully documented there. "Not yet" means the playbook works from live documentation only.

## Related platform skills

Field Service work usually also needs `apex-engineering`, `lwc-engineering`, `flow-configuration`, `salesforce-security`, `salesforce-quality` and `salesforce-release-watch`.
