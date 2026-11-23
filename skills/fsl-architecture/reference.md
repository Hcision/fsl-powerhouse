# Field Service product boundaries and limits

Anchors read from Salesforce Help on 2026-11-23. Limits change between releases, so confirm each number on the linked page before a design depends on it.

## Naming and layers

- Salesforce now calls the product **Agentforce Field Service and Operations**. Documentation and Setup still use "Field Service" in many places, so search for both names.
- **Core features** arrive when Field Service is enabled in Setup under Field Service Settings (needs Customize Application). They are standard objects such as work orders and service appointments.
- **The managed package** adds Guided Setup, the dispatcher console, the scheduling tools and optimizer, and custom objects. It is installed after enabling Field Service.
- **The mobile app** is the third layer. Appointment Assistant, Visual Remote Assistant and Workforce Scheduling are separate extensions.
- Core features, managed package and mobile app are available in Enterprise, Unlimited and Developer Editions.

## Managed package prerequisites

- Chatter must be enabled. From Spring '26 it is off by default in new orgs.
- The install asks to approve third-party access. That approval is what lets street-level routing and optimization run.

## General limits

| Limit | Value |
| --- | --- |
| Service resources per user | 1 |
| Service territories in one hierarchy | 10,000 |
| Work orders in one hierarchy | 10,000 |
| Work order line items in one hierarchy | 10,000 |
| Maintenance work rules per maintenance plan | 25,000 |
| Work orders generated at once per maintenance plan | 2,600 |

## Scheduling and optimization limits

| Limit | Value |
| --- | --- |
| Optimization requests per hour per org | 3,600 |
| Skills per service resource | 100, or 250 with Enhanced Scheduling and Optimization |
| Service appointments per resource per day | 200. A bundle counts as one |
| Service appointments optimized per rolling 24 hours | 50,000, higher with Enhanced Scheduling and Optimization depending on licenses |

## Territory sizing guidance

Salesforce suggests staying within 50 service resources per territory, 1,000 service appointments per day per territory, and 20 qualified resources per appointment. Without Enhanced Scheduling and Optimization, scheduling and optimization work only in territories that have at least one primary member.

## Sources

- [Field Service Limits and Limitations](https://help.salesforce.com/s/articleView?id=service.fs_limits.htm&language=en_US&type=5)
- [Guidelines for Creating Service Territories](https://help.salesforce.com/s/articleView?language=en_US&id=fs_territory_guidelines.htm&type=0)
- [Set Up Field Service Basics](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_set_up.htm&type=5)
- [Install the Field Service Managed Package](https://help.salesforce.com/s/articleView?language=en_US&id=pfs_intro.htm)
- [Field Service Objects](https://help.salesforce.com/s/articleView?id=fs_standard_objects.htm&language=en_US)
