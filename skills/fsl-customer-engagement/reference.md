# Customer engagement reference

Anchors read from Salesforce Help and the Field Service Developer Guide on 2026-11-23.

## Appointment Assistant

- It needs its own managed package and permission set license, on top of Field Service. Each mobile worker who shares a location needs the Appointment Assistant license.
- **Real-Time Location** gives the customer temporary live tracking while the worker travels, with SMS notifications as the worker approaches.
- It relies on Field Service Mobile Settings: "Collect service resource geolocation history" must be on, with update frequencies set for foreground and background.
- Notifications are Messaging components whose text carries a URL placeholder to the Experience Builder site.
- A Real-Time Location component can be added to the service appointment page so back-office users see the same ETA and map as the customer.

## Self-Service Scheduling

- Customers can book, reschedule, cancel and confirm. The feature is added to an Experience Builder site and driven by flows.
- The new-appointment flow has components for authentication by email or mobile phone, with a resend delay, and for work types, operating hours and scheduling policy.

## Known conflict

Appointment Assistant can conflict with LWC Offline in the mobile app and cause missing URLs. Check the linked known issue before combining them.

## Sources

- [Set Up Appointment Assistant](https://help.salesforce.com/s/articleView?id=sf.mfs_appointment_assistant_parent.htm&language=en_US&type=5)
- [Set Up Real-Time Location](https://help.salesforce.com/s/articleView?id=mfs_appointment_assistant_set_up_parent.htm&language=en_US&type=5)
- [Geolocation Settings for Real-Time Location](https://help.salesforce.com/s/articleView?id=mfs_appointment_assistant_geolocation.htm&type=5&language=en_US)
- [Self-Service Scheduling for New Appointments](https://help.salesforce.com/s/articleView?id=service.mfs_appointment_assistant_sss_new_appointments.htm&language=en_US&type=5)
- [Considerations for LWC Offline](https://developer.salesforce.com/docs/service/field-service-dev/guide/sfs-gs-lwc-considerations.html)
