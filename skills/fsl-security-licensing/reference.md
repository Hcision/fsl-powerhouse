# Licenses and access reference

Anchors read from Salesforce Help on 2026-11-23. License packaging changes, so confirm names in the org's Company Information before advising.

## Licenses

- Every user needs the Field Service Standard user permission to reach field service objects. Field Service user licenses include it.
- Field Service includes three permission set licenses related to the managed package and mobile app. The pages read name Field Service Dispatcher, Field Service Mobile and Field Service Scheduling.
- The Scheduling license is what lets a user appear on the Gantt and be scheduled by the engine and optimizer.
- Dispatcher and technician licenses do not cover call center work, case management or sales tasks.

## Permission sets by persona

The managed package creates its permission sets from Field Service Settings, Getting Started, Permission Sets. Guided Setup checks they are current and reports missing permissions.

| Persona | Needs |
| --- | --- |
| Dispatcher | Field Service Dispatcher permissions and the Dispatcher license |
| Call center rep | Field Service Call Center Rep permission set |
| Technician | Field Service Mobile license, Field Service Resource license and Resource permissions |
| Community dispatcher | Partner Community license with the Community Dispatcher permission sets |
| Contractor | Customer Community Plus or Partner Community license, plus a Field Service permission set |

Scheduling through Apex needs one of the Field Service Admin, Dispatcher, Call Center or Self-Service permission sets.

## Record access

- By default the core objects are widely visible. Most orgs set Work Order, Work Order Line Item, Service Appointment, Service Resource and Service Territory to Private.
- With custom sharing, a dispatcher needs read and write access, not read-only, to the appointments in their territories in order to edit schedules.

## Sources

- [Field Service Permission Set Licenses](https://help.salesforce.com/s/articleView?language=en_US&id=service.fs_perm_set_licenses.htm&type=5)
- [Assign Field Service Permissions](https://help.salesforce.com/s/articleView?id=pfs_set_profiles_perms.htm&language=en_US&type=5)
- [Limit Access to Field Service Records](https://help.salesforce.com/s/articleView?id=sf.fs_sharing.htm&language=en_US&type=5)
- [Give Contractors Access to the Mobile App](https://help.salesforce.com/s/articleView?language=en_US&id=service.fs_contractor_access.htm&type=5)
- [Key Concepts and Glossary](https://help.salesforce.com/s/articleView?id=service.fs_key_concepts.htm&language=en_US&type=5)
- [AppointmentBookingService](https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-appointmentbookingservice.html)
