# Service execution reference

Anchors read from the Field Service Developer Guide and Salesforce Help on 2026-11-23.

## Service reports

- A report can be created in code with the standard action `createServiceReport`, from a work order, a work order line item or an existing service report, using a template found by querying `ServiceReportLayout`.
- API 41.0 and later accept several signatures. Each needs a different signature type, and the types and their number must match the template.
- The Service Report Template REST resource returns the templates (API 40.0 and later).

## Document Builder

- Document Builder creates service document templates and can host custom LWCs, which need print styling.
- Users need the Field Service Dispatcher or Field Service Mobile permission set license to be assigned Document Builder.

## Related skills

Parts are in `fsl-inventory`, coverage in `fsl-assets-entitlements`, and customer messaging in `fsl-customer-engagement`.

## Sources

- [Create a Service Report with Apex](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-code-samples-sr.html)
- [Field Service API](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-rest.html)
- [LWCs for Service Documents](https://developer.salesforce.com/docs/service/field-service-dev/guide/fsl-dev-mobile-document-builder.html)
- [Assign Document Builder](https://help.salesforce.com/s/articleView?id=fs_document_builder_perm_sets.htm&language=en_US&type=5)
