# APIs and integration reference

Anchors read from the Field Service Developer Guide on 2026-11-23. Several guide pages omit URIs and minimum versions, so confirm them in the REST reference before coding.

## Field Service REST resources

| Resource | Purpose | Since |
| --- | --- | --- |
| Field Service Flow | Information about field service flows | API 42.0 |
| Field Service Mobile Settings | The user's mobile app settings | API 42.0 |
| Service Report Template | One or more report templates | API 40.0 |
| Appointment Bundling | Create, update and unbundle bundles, remove members, start automatic bundling | Not stated |

## Standard actions

Called with `POST /services/data/vXX.X/actions/standard/<name>` and a JSON body holding an `inputs` array.

| Action | Inputs | Notes |
| --- | --- | --- |
| `generateWorkOrders` | `recordId` of the maintenance plan | Success returns 201 |
| `createServiceReport` | `entityId`, `templateId`, `signatures` | API 41.0 and later for several signatures. API 40.0 allows one |
| `scheduleServiceAppointment` | `serviceAppointmentId`, `schedulingPolicyId` | API 62.0 and later. Check `isSuccess` and `errors` in the response |

- `entityId` is a work order, work order line item or service report. `templateId` comes from a query on `ServiceReportLayout`.
- Each signature needs `data` (base64), `contentType` and `signatureType`. Types must differ from each other and match the template in kind and number.
- A guest user running under a future method cannot create the content document, so cannot create the report.
- The guide also lists these invocable actions: Convert Time Zone, Get Current Time, Get Service Appointment Time Slots, Get Field Service Object Field, Get Agent Context, Create Engagement Topic and Get Engagement Topics.

The documented Apex samples call these endpoints with the running user's session ID and need remote site settings. Review that pattern against the org's security standards before reusing it.

## Metadata API

The guide lists `FieldServiceSettings`, `Flow` with Field Service action types, `Skill` and `TimeSheetTemplate`. It does not state which managed package configuration is deployable, so inventory scheduling policies, work rules, objectives and package settings separately and confirm how each one moves between orgs.

## Managed package triggers

The package ships triggers on Assigned Resource, Operating Hours, Resource Absence, Scheduling Policy, Service Appointment, Service Resource, Service Resource Capacity, Service Territory, Service Territory Member, Time Dependency, Time Slot, Work Order and others. A pinned appointment rejects changes to its scheduled times. Bulk loads and integrations share a transaction with this logic.

## Data model diagrams

The guide groups the objects into core data model, inventory management, preventive maintenance, product service campaign, warranty management and pricing.

## Sources

- [Field Service API](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-rest.html)
- [Invocable Actions](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-actions-parent.html)
- [Schedule Service Appointment action](https://developer.salesforce.com/docs/service/field-service-dev/guide/actions-obj-scheduleserviceappointment.html)
- [Generate Work Orders with Apex](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-wo.html)
- [Create a Service Report with Apex](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-sr.html)
- [Metadata API](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-metadata.html)
- [Managed package triggers](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-custom-triggers.html)
- [Data Objects](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-soap.html)
