# Mobile and offline reference

Anchors read from the Field Service Developer Guide and Salesforce Help on 2026-11-23. Read the Mobile and Offline Developer Guide first, as the Field Service guide asks.

## Lightning web components in the app

- LWCs are opened from the Actions menu as quick actions and can work offline.
- Test on an iOS Simulator or Android Emulator with a virtual device build of the app. Debug with browser developer tools.
- Automatic Offline Mode can be turned on and tuned.

## Considerations to check first

- A global quick action shows on any page with the Actions menu but does not receive the current record ID.
- Community license users can hit a missing record error when opening a service appointment.
- Task objects cannot be primed. A briefcase that includes them shows an error, and the other objects still prime.
- Appointment Assistant can conflict with LWC Offline and cause missing URLs.
- On iOS, component changes load only after a full quit and relaunch.

## Deep linking

- A predefined URI scheme opens the app from email, a website or another app. Links can target tabs, flows and actions, and can pass data to an LWC.
- A user who is not logged in is sent to login and must tap the link again afterwards.
- A link to an action shows a confirmation dialog unless the URL is configured with a security key.

## Service documents

LWCs for Document Builder need print styling, so a component built for the mobile app has to be rebuilt for a document template.

## Sources

- [Lightning Web Components in the Field Service Mobile App](https://developer.salesforce.com/docs/service/field-service-dev/guide/sfs-gs.html)
- [Considerations for LWC Offline](https://developer.salesforce.com/docs/service/field-service-dev/guide/sfs-gs-lwc-considerations.html)
- [Configure Offline Mode](https://developer.salesforce.com/docs/service/field-service-dev/guide/sfs-gs-lwc-fs-offline.html)
- [Deep Linking](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-mobile-deep-linking.html)
- [LWCs for Service Documents](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-mobile-document-builder.html)
- [Mobile and Offline Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.mobile_offline.meta/mobile_offline/intro.htm)
