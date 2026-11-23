# Inventory reference

Anchors read from Salesforce Help on 2026-11-23.

## Objects and what each one does

| Object | Role |
| --- | --- |
| `Location` | A warehouse, site, van or plant where stock is kept or used |
| `ProductItem` | Stock of one product at one location. A product kept in two places has two product items |
| `ProductItemTransaction` | The record of a change to a product item |
| `ProductRequired` | A part needed for the job, set on a work type, work order or line item |
| `ProductRequest` and line items | An order for parts, with need-by date, destination location and shipment type. Can relate to a work order, line item, case or account |
| `ProductTransfer` | Movement of stock between locations |
| `ProductConsumed` | Stock used on a work order or line item, which leaves inventory |
| `ReturnOrder` and line items | Customer returns, repairs, or unused van stock going back |

## Rules to check

- **Serial numbers.** A product item that carries a serial number must have a quantity on hand of 1. Serialized inventory uses one product item per unit.
- **Transfers.** Create one product transfer per product request line item so each part has its own status. Marking a transfer received needs Edit on product items.
- **Consumption.** A product consumed names the product item the part came from. Creating one needs Edit on work orders and Read on product items.
- **Returns.** Return orders can relate to product requests, cases, accounts, orders and work orders. Salesforce advises against linking them to product transfers, to keep processing short.

## Sources

- [Set Up Your Field Service Inventory](https://help.salesforce.com/s/articleView?id=service.fs_set_up_parts.htm&language=en_US&type=5)
- [Product Item and Inventory Fields](https://help.salesforce.com/s/articleView?language=en_US&id=fs_parts_fields.htm&type=0)
- [Transfer Inventory](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_create_product_transfers.htm&type=5)
- [Track Inventory Consumption](https://help.salesforce.com/s/articleView?language=en_US&id=sf.fs_create_products_consumed.htm&type=5)
- [Manage Serialized Inventory V2](https://help.salesforce.com/s/articleView?language=en_US&id=service.fs_learn_serialized_products.htm&type=5)
- [Guidelines for Tracking Customer Returns](https://help.salesforce.com/s/articleView?id=fs_return_order_settings.htm&language=en_US&type=5)
