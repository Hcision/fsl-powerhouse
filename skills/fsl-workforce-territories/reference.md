# Workforce and territory reference

Anchors read from Salesforce Help on 2026-11-23.

## Service resources

- A user can have one service resource. Resource type is technician, dispatcher or crew. The picklist also shows Asset, which cannot be saved.
- An inactive resource cannot be assigned to appointments and cannot use the mobile app.
- A location, such as a van or warehouse, can be linked to one service resource only.

## Territory membership types

| Type | Rule |
| --- | --- |
| Primary | One per resource. Usually where the resource works most often |
| Secondary | Several allowed, and their dates can overlap |
| Relocation | A temporary move |

- The Match Territory work rule keeps appointments with primary or relocation members of the appointment's territory.
- Members use the territory's operating hours unless their own membership record names different hours.
- A territory that has service appointments cannot be deleted.

## Shifts

- A shift needs a territory and a resource assigned to it, and must sit fully inside a primary territory membership of that resource.
- Without Enhanced Scheduling and Optimization, shifts on secondary territories are ignored by resource schedule optimization. Use shifts without a territory, or time slots.

## Capacity-based resources and contractors

- Mark a resource capacity-based when it works a set number of hours or appointments per period. Contractors usually are.
- Capacity-based resources cannot take appointments with scheduling dependencies, cannot be relocated or given a secondary territory, are not supported by resource schedule optimization, and show no utilization on the Gantt.
- Contractors reach Salesforce through Experience Cloud with community licenses. Contractor and Contractor Plus licenses exist per user and login-based.

## Work capacity

Turn on "Allow defining work capacity limits" in Field Service Settings. The feature adds Work Capacity Limits, Usages and Availabilities, whose tabs must be visible to the profile.

## Sources

- [Create Service Resources](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_create_resources.htm&type=5)
- [Guidelines for Creating Service Territories](https://help.salesforce.com/s/articleView?language=en_US&id=fs_territory_guidelines.htm&type=0)
- [Guidelines for Shift Availability](https://help.salesforce.com/s/articleView?id=fs_shifts_guidelines.htm&language=en_US&type=5)
- [Define Capacity-Based Resources](https://help.salesforce.com/s/articleView?language=en_US&id=service.fs_define_resource_capacity.htm&type=5)
- [Guidelines for Setting Up Contractors](https://help.salesforce.com/s/articleView?language=en_US&id=service.fs_setting_up_contractors.htm&type=5)
- [Set Up Work Capacity](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_work_capacity_setup.htm&type=5)
- [Field Service Limits and Limitations](https://help.salesforce.com/s/articleView?id=service.fs_limits.htm&language=en_US&type=5)
