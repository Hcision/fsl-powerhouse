# Agentforce in Field Service reference

Anchors read from Salesforce Help and the Field Service Developer Guide on 2026-11-23. This area changes every release. Only the items below were confirmed on official pages. Treat anything else as unverified until its setup page is read.

## Confirmed

- The product is now named Agentforce Field Service and Operations.
- **Agent in the mobile app.** Once enabled for the org, the agent is available in the Field Service mobile app. Using text and images, mobile workers can ask it to find and summarize records, generate a post-work summary and gather information.
- **Standard actions an agent or flow can call:** Get Service Appointment Time Slots, Schedule Service Appointment (API 62.0 and later), Get Field Service Object Field, Get Agent Context, Create Engagement Topic, Get Engagement Topics, Convert Time Zone and Get Current Time.

## To verify per org

The user context an agent's actions run in and whether it holds the permission sets that scheduling requires. License and edition, which agent templates are available, data residency, and whether a capability is generally available or in preview for the org's release.

## Sources

- [Field Service Mobile App](https://help.salesforce.com/s/articleView?id=service.mfs_overview.htm&language=en_US)
- [Set Up Field Service Basics](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_set_up.htm&type=5)
- [Invocable Actions](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-actions-parent.html)
- [Schedule Service Appointment action](https://developer.salesforce.com/docs/service/field-service-dev/guide/actions-obj-scheduleserviceappointment.html)
