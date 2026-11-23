# Preventive maintenance reference

Anchors read from official Salesforce documentation on 2026-11-23. They are starting points. Confirm each one against the target org's API version before relying on it.

## Objects

| Object | Role | Notes |
| --- | --- | --- |
| `MaintenancePlan` | Schedule for one or more assets | Field Service must be enabled |
| `MaintenanceAsset` | Asset covered by a plan | Holds its own `NextSuggestedMaintenanceDate` |
| `MaintenanceWorkRule` | Recurrence for a plan or an asset | API 49.0 and later |

A work rule points to a plan through `ParentMaintenancePlan` (API 51.0 and later) or to a maintenance asset through `ParentMaintenanceRecord`. Both lookups are nillable. `RecurrencePattern` holds an RRULE string. `Type` is Calendar-based (default) or Criteria-based (API 52.0 and later), and a criteria-based rule uses `RecordsetFilterCriteria`. A boolean added in API 55.0 turns on the floating work order adjustment. Its API name was not readable on the page, so describe the object before using it.

## MaintenancePlan generation fields

| Field | Meaning |
| --- | --- |
| `NextSuggestedMaintenanceDate` | Suggested service date of the first work order in the next batch. UI label: Date of the first work order in the next batch. Not the creation date |
| `GenerationTimeframe` + `GenerationTimeframeType` | How far ahead one batch reaches (Days, Weeks, Months, Years). Required |
| `GenerationHorizon` | Whole number of days before `NextSuggestedMaintenanceDate` at which an automatic batch is generated |
| `DoesAutoGenerateWorkOrders` | Generates batches automatically and blocks the manual Generate Work Orders action |
| `DoesGenerateUponCompletion` | With auto-generation, holds the next batch until the last generated work order is completed |
| `MaintenanceWindowStartDays` / `MaintenanceWindowEndDays` | Drive Earliest Start Permitted and Due Date on generated service appointments. Blank means both use the suggested maintenance date |
| `WorkOrderGenerationMethod` | One work order per asset, or one work order line item per asset |
| `SvcApptGenerationMethod` | One appointment per work order, or one per line item. Required with the line-item method |
| `WorkOrderGenerationStatus` | Read-only: NotStarted, InProgress, Completed, Unsuccessful |

## Behavior to check first

- **Cursor location.** When the plan has maintenance assets, the date advances on each asset after a batch and stays unchanged on the plan. Without assets, it advances on the plan. Read the cursor from the level that owns it.
- **Completion gating.** A work order counts as completed in status categories Cannot Complete, Canceled, Completed and Closed. Generation is per asset, so one late work order staggers that asset against the others.
- **One batch at a time.** A plan with `WorkOrderGenerationStatus` InProgress cannot start another batch. Custom jobs that trigger generation need to check the status and handle Unsuccessful.
- **Generation methods are fixed once records exist.** Changing them means deleting and regenerating the work orders, or recreating the plan.
- **Plan-level frequency is legacy.** The object reference for API 63.0 states that `Frequency` and `FrequencyType` began phased retirement in Summer '22 and directs migration to maintenance work rules. Treat any code that reads or writes these fields as a defect lead and confirm their state in the target release.
- **Batch volume.** One generation creates at most 2,600 work orders per maintenance plan, and a plan holds at most 25,000 maintenance work rules. Estimate assets × rules × occurrences inside the generation timeframe, and shorten the timeframe or split the plan when the estimate approaches the limit.
- **Generation from code.** The standard action `generateWorkOrders` takes the maintenance plan ID as `recordId` and returns 201 on success.

## Sources

- [MaintenancePlan](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_maintenanceplan.htm)
- [MaintenancePlan, API 63.0](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_maintenanceplan.htm)
- [Field Service Limits and Limitations](https://help.salesforce.com/s/articleView?id=service.fs_limits.htm&language=en_US&type=5)
- [Generate Work Orders with Apex](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-wo.html)
- [MaintenanceWorkRule](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_maintenanceworkrule.htm)
