---
title: Returns, refunds, and voids
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203259303-Returns-Refunds-and-Voids?language=en_US
source_updated: 2026-08-07
---
# Returns, refunds, and voids

Explains the difference between returning, refunding and voiding a sale, and the steps for each. Use when reversing a purchase made in person or online.

## Where in Mindbody
- Menu path: client **Purchases** screen (via client profile), then **Return/Void** in the Actions column or the **Sale ID** link, which opens Manage Sales.

## Steps
### Return a sale
1. Open the client's Purchases screen and find the item.
2. Click the **Sale ID** or **Return/Void**.
3. Click **Return All** (whole transaction) or **Return this item** (one item).
4. Enter the required reason.
5. Click **Choose Refund Method** to refund, or **Return without a Refund** to just remove the item.
6. Choose the refund method, enter the amount, optionally tick **Use additional refund method?** to split.
7. Click **Save No Receipt** or **Save Print Receipt**.

### Void a sale
1. Open Purchases, click **Sale ID** or **Return/Void**.
2. On Manage Sales, if it shows "0 in use", click **Void**.
3. If visits use the pricing option: click the **# in use** link, click **Early** per visit or **Reassign** to another pricing option, return to Manage Sales and click **Void**.
4. Confirm with **Yes, Void This Sale**.

## Settings & fields
- Refund targets: original credit card (final), ACH to checking/debit, account credit (good for exchanges), cash or check (can cut processing fees; hand it to the client).
- Statuses: **Returned** (red on Purchases); a returned sale showing a card type was refunded to that card; $0 with no payment method means returned without refund.
- Return without a refund removes the item without reporting; undo it by clicking the line item and **Void**.
- Return date records processing time; it cannot schedule a future return.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first. Refunds (especially to credit cards) and voids cannot be reversed.
- Permissions: Issue sale refunds; Issue sale refunds to credit cards (without it, only account-credit refunds).
- Sites with auto capture have no void, only refunds. TSYS and Mindbody Payments cannot void credit card sales. Without auto capture, contact the payment processor directly for out-of-hours help.
- Cannot refund more than the original amount; no bulk refunds; only one refund per purchase (no partial now, rest tomorrow).
- Multiple quantities of one item cannot be partly returned; return all and re-ring the quantity at Point of Sale.
- Any refund makes the pricing option inactive. Visits tied to a returned pricing option stay attached as paid; make them unpaid or early cancel and reassign first.
- Returns or voids of commissioned sales void the commission.
- Credit card voids only work before settlement (often same day). Voids may cost less than refunds; original processing fees are never returned.
- ACH: use Void as soon as possible if offered; otherwise wait at least 7 days before refunding to avoid losing money if the payment fails.
- Card refunds only go to the original card. If it is expired, closed or invalid, refund via account credit, cash, check or gift card; declined refunds may return to your business account without any software notice, so watch the bank/processor portal.
- Easy upgrades before settlement void the original sale; confirm whether a 24-hour wait applies.
- Refund timing varies by processor (TSYS, Mindbody Payments, Elavon US, Elavon Canada/Bluefin, Paysafe, Ezidebit).

## Related
- [Why can't I void a sale](203258313-Why-can-t-I-void-a-sale.md)
- [Client Purchases screen overview](../clients/215843338-Client-Purchases-Screen-overview.md)
- [Partial Sale Returns](203280743-Partial-Sale-Returns.md)
- [Line-item returns](Line-item-returns.md)
- [Returns report](https://support.mindbodyonline.com/s/article/203257083-Returns-report?language=en_US)
- [Refunds FAQ](https://support.mindbodyonline.com/s/article/214108797-Why-do-I-keep-getting-an-error-when-trying-to-issue-a-refund?language=en_US)
- [How do I refund a credit card transaction](https://support.mindbodyonline.com/s/article/209061677-How-do-I-refund-a-credit-card-transaction-TSYS?language=en_US)
- [How do I exchange a product or service](https://support.mindbodyonline.com/s/article/222673608-How-do-I-exchange-a-product-or-service?language=en_US)
- [Reassigning payments overview](https://support.mindbodyonline.com/s/article/Reassigning-Payments-overview?language=en_US)
- [Make a client's visit unpaid](https://support.mindbodyonline.com/s/article/223204108-How-do-I-make-a-client-s-visit-unpaid?language=en_US)
- [Auto capture vs SmartBatching vs manual batching](https://support.mindbodyonline.com/s/article/205625567-Smart-Batching-Vs-Manually-Batching?language=en_US)
- [Payment Processing reports](https://support.mindbodyonline.com/s/article/203256443-Payment-Processing-reports?language=en_US)
