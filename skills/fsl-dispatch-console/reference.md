# Dispatcher console reference

Anchors read from the Field Service Developer Guide and Salesforce Help on 2026-11-23. Help now calls the managed package console the Classic Dispatch Console.

## Custom Gantt actions

An action calls a global Apex class or a Visualforce page. The Apex class implements one interface from the `FSL` namespace. Each `action` method is global, ends with a `Map<String, Object>` parameter that must be present, and returns a String. A non-empty return value is shown as a Gantt notification.

| Interface | Method parameters before the map |
| --- | --- |
| `FSL.CustomGanttServiceAppointmentAction` | `List<Id> serviceAppointmentsIds, Datetime start, Datetime end` |
| `FSL.CustomGanttServiceResourceAction` | `Id resourceId, Id stmId, Datetime start, Datetime end` |
| `FSL.CustomGanttResourceAbsenceAction` | `Id absenceId, String absenceType, Datetime start, Datetime end` |

- The appointment action can receive many IDs. Check the list size.
- The absence type is `na` or `break`. Start and end are the dates currently shown on the Gantt.
- A Visualforce action receives the same values as GET parameters and closes its lightbox with `parent.postMessage('closeLightbox','*')`.
- Visualforce pages that belong to a managed package cannot be opened by a custom action.

## Temporary appointment lists

Publishing the platform event `FSL__CreateFilterEvent__e` creates an appointment list for the publishing user.

- Requires the custom permission Create Temporary Service Appointment List.
- Fields: `FSL__ServiceApptIds__c` (JSON array of IDs), `FSL__FilterName__c`, optional `FSL__Description__c`, `FSL__FilterCategory__c` set to `GENERAL`, and `FSL__LoadFilterImmediately__c`.
- A list holds up to 300 appointments, is visible only to its creator, and disappears on console refresh.
- Subscribing to the channel consumes Change Data Capture allocations.
- The list is static unless Enhanced Live Updates is on and the user can read every field in the appointment field sets.

## Permissions and views

- Managed package custom permissions control console actions and views, such as bulk dispatch, optimize, schedule and dragging on the Gantt. Add them to the Field Service Admin, Dispatcher or Community Dispatcher permission sets.
- Using the console in an Experience Cloud site needs a Partner Community license and the Field Service Dispatcher permission set license.
- Utilization compares scheduled hours with operating hours and is calculated only for resources that are not capacity-based. Thresholds are set under Field Service Settings, Dispatcher Console UI, Gantt Configurations.
- The emergency wizard shows at most 25 candidates and uses the resource's last known location while it is still valid.

## Sources

- [Dispatcher Console Custom Actions](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-dispatcher.html)
- [Create Service Appointment Lists](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-sal.html)
- [Set Custom Permissions](https://help.salesforce.com/s/articleView?id=sf.pfs_custom_permissions.htm&language=en_US&type=5)
- [View Resource Utilization](https://help.salesforce.com/s/articleView?language=en_US&id=service.pfs_view_availability.htm&type=5)
- [Schedule Emergency Appointments](https://help.salesforce.com/s/articleView?id=sf.pfs_emergency.htm&language=en_US&type=5)
- [Dispatch Console in an Experience Builder Site](https://help.salesforce.com/s/articleView?language=en_US&id=sf.pfs_dispatcher_console_community.htm&type=5)
