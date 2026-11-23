# Scheduling Apex reference

Anchors read from the Field Service Developer Guide on 2026-11-23. Enhanced Scheduling and Optimization (ESO) changes several behaviors, so establish first whether the org and territory use it.

## FSL namespace entry points

| Class | Use |
| --- | --- |
| `FSL.AppointmentBookingService` | `getSlots` returns graded slots for one appointment. `getABSlots` covers a chain of related appointments |
| `FSL.ScheduleService` | `schedule`, `scheduleExtended`, `scheduleHere`, `getAppointmentInsights` |
| `FSL.GradeSlotsService` | Evaluates every candidate slot, as the Candidates action does |
| `FSL.OAAS` | `optimize`, `reshuffle`, `resourceDayOptimization` |
| `FSL.ScheduleJobsApi` | Territory configuration of Enhanced Optimization scheduled jobs |
| `FSL.PolygonUtils` | Service territory from latitude and longitude |
| `FSL.RecurringAppointmentsManager` | Slots for recurring appointment patterns |

## Booking sequence

1. The work order and the service appointment must exist before `getSlots` is called.
2. Pass the time zone of the service territory. Slots come back in that zone. The `TimeZone` on the operating hours record passed for slot intervals is ignored.
3. `getSlots` ignores the work type's Exact Appointment setting. Query the work type and pass the value when it must be honored.
4. Write the chosen slot to `ArrivalWindowStartTime` and `ArrivalWindowEndTime` in UTC. The documented sample shifts by a fixed offset and does not handle daylight saving changes, so test dates on both sides of a DST switch.
5. Call `FSL.ScheduleService.schedule` to place the appointment inside the window.

## Constraints

- **Permissions.** The running user needs one of the managed package permission sets Field Service Admin, Dispatcher, Call Center or Self-Service. A platform event trigger runs as Automated Process unless a user is configured, and that user cannot schedule.
- **One appointment per call.** `schedule` handles a single appointment. For volume, use a batch class with a batch size of one.
- **DML before the call.** The guide recommends no earlier DML in the same transaction.
- **Callouts.** With ESO, every scheduling call makes a callout. Without ESO, a callout can occur for street-level or point-to-point travel that is not cached.
- **Chains.** `scheduleExtended` and `getABSlots` are synchronous with ESO, always all-or-none, for up to five appointments. Without ESO they are asynchronous, results arrive on `MstCompletedChannel` through the Streaming API, and behavior is reliable for two appointments only.
- **`scheduleHere` requires ESO.** Call `getAppointmentCandidates` first. The start must fall inside its horizon, 10 days by default and 30 at most.
- **Optimization.** `OAAS` methods return the ID of an optimization request record to poll. `optimize` runs in-day optimization when the policy's in-day flag is set. `maxOptRuntime` defaults to 30 seconds and excludes queue time. Without ESO, calling `OAAS` from a batch `start` or `execute` method or from a future method throws an exception.
- **Managed triggers.** The package ships triggers on Service Appointment, Assigned Resource, Service Resource, Service Territory Member, Resource Absence, Work Order and other scheduling objects. A pinned appointment rejects changes to its scheduled times. Custom automation on these objects shares their transaction, so test it with the package logic active.

## Policy and engine rules

- A scheduling policy needs at least one database work rule to narrow candidates during Appointment Booking and Get Candidates. Salesforce recommends filtering to about 20 candidates.
- Match Territory keeps appointments with primary or relocation members of the appointment's territory.
- With Enhanced Scheduling and Optimization enabled per territory, every appointment and resource territory in one optimization request, bulk schedule or batch update must use the same engine. Appointments in enabled territories can go only to resources whose primary territory is also enabled.
- Complex work: a chain that spans territories needs all of them in the optimization request. Without Enhanced Scheduling and Optimization, Same Resource dependencies need a single territory membership per resource. Pinned appointments are not counted in a request.
- Scheduled jobs count against the 100 concurrently scheduled Apex jobs. A job recurring every 15 minutes counts as four.
- Resource schedule optimization is not supported for capacity-based resources.
- The standard action `scheduleServiceAppointment` (API 62.0 and later) schedules one appointment under a policy without Apex. Appointment bundling has its own REST APIs.

## Documentation inconsistencies seen

- `getAppointmentInsights`: the signature lists the policy ID first, while the parameter list and example pass the appointment ID first. Confirm the order in the org.
- `resourceDayOptimization`, third overload: the signature uses `Set<String>` where the parameter description says `Set<Id>`.
- `getABSlots`: the usage text mentions two appointments, and the ESO note allows five.

## Sources

- [FSL Apex namespace](https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-namespace-fsl.html)
- [AppointmentBookingService](https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-appointmentbookingservice.html)
- [ScheduleService](https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-scheduleservice.html)
- [OAAS](https://developer.salesforce.com/docs/service/field-service-dev/guide/apex-class-fsl-oaas.html)
- [Create and Manage Work Rules](https://help.salesforce.com/s/articleView?language=en_US&id=sf.pfs_optimization_theory_work_rules.htm&type=5)
- [Limitations for Enhanced Optimization per Territory](https://help.salesforce.com/s/articleView?id=pfs_enhanced_optimization_per_territory_limitations.htm&language=en_US&type=5)
- [Considerations for Complex Work](https://help.salesforce.com/s/articleView?id=pfs_complex_work_considerations.htm&language=en_US&type=0)
- [Limits for Enhanced Scheduling and Optimization](https://help.salesforce.com/s/articleView?language=en_US&id=service.pfs_enhanced_available_limits.htm&type=5)
- [Managed package triggers](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-custom-triggers.html)
