---
title: How to process split refunds for partial sale returns
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203280743-Partial-Sale-Returns?language=en_US
source_updated: 2025-12-10
---
# How to process split refunds for partial sale returns

Procedure for refunding the unused portion of a pricing option/package (e.g. 10-pack with 4 used) while still crediting the sessions already used so staff pay is correct. Three stages: return, re-sell used sessions to account credit, reassign visits.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/main_retail.asp?fl=true&tabID=3 (Point of Sale, Services tab)
- Menu path: client **Purchases** screen > **Return/Void**; **Point of Sale**; client **Account Details** screen

## Terms
- Return = give back the item; refund = money going back; partial refund = only some money; split refund = money across several payment methods; return with no refund = business keeps the money.

## Steps
### Step 1: Return the pricing option
1. Look up the client, open **Purchases**.
2. Click the **Sale ID** or **Return/Void** on the sale.
3. On Manage Sales click **Return All**.
4. On Return / Issue Refund, enter a reason.
5. Click **Choose Refund Method** and pick Refund method 1 (original payment, cash, check, etc.).
6. Tick **Use additional refund method?**; set **Refund method 2** to **Account**.
7. Edit the amounts manually: method 1 = value of unused sessions, Account = value of used sessions.
8. Click **Save No Receipt** or **Save Print Receipt**.

### Step 2: Sell a replacement pricing option for used sessions
1. Open **Point of Sale**, select the client.
2. Click **Services** and choose a single-session pass.
3. Set session count/quantity to the number of sessions already used.
4. Set the activation date to the date of the first visit made on the returned option.
5. Set the price to equal the account credit just created.
6. Click **Add Item**, choose **Account** as payment, click **Save No Receipt**.

### Step 3: Reassign visits
1. Open the client's **Account Details** screen.
2. In the Actions column of the returned (now inactive) pricing option, click the 3-dot menu > **Show Visits**.
3. On the oldest visit, use the **Reassign Payment** menu to select the new pricing option; click **OK** on the alert.
4. Repeat until all visits are reassigned.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first. Credit card refunds cannot be undone.
- Only one refund per transaction; after a partial refund, no further refund on that ticket.
- Returning the pricing option makes it inactive.
- Refund tax uses the original sale's tax rate.
- If refunding less than the full price, still put enough into Account to pay for the replacement option in Step 2.
- A partial return differs from a line-item return (single item from a multi-item sale).
- Processor-specific partial card refund rules exist for TSYS, Elavon US, Elavon Canada, and Paysafe.

## Related
- [203259303-Returns-Refunds-and-Voids](203259303-Returns-Refunds-and-Voids.md)
- [Line-item-returns](Line-item-returns.md)
- [How-do-I-issue-a-partial-refund-for-product-transaction-with-a-quantity-of-more-than-1-on-one-line-item](https://support.mindbodyonline.com/s/article/How-do-I-issue-a-partial-refund-for-product-transaction-with-a-quantity-of-more-than-1-on-one-line-item?language=en_US)
- [Partial-Refunds-of-Account-Payments](https://support.mindbodyonline.com/s/article/Partial-Refunds-of-Account-Payments?language=en_US)
- [203259203-Looking-up-clients](../clients/203259203-Looking-up-clients.md)
- [215843338-Client-Purchases-Screen-overview](../clients/215843338-Client-Purchases-Screen-overview.md)
- [215843418-Client-Account-Details-Screen-overview](../clients/215843418-Client-Account-Details-Screen-overview.md)
- [210812917-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-TSYS](https://support.mindbodyonline.com/s/article/210812917-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-TSYS?language=en_US)
- [210105838-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-Elavon-US](https://support.mindbodyonline.com/s/article/210105838-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-Elavon-US?language=en_US)
- [210106588-How-do-I-complete-a-partial-refund-a-credit-card-transaction-Elavon-Canada](https://support.mindbodyonline.com/s/article/210106588-How-do-I-complete-a-partial-refund-a-credit-card-transaction-Elavon-Canada?language=en_US)
- [210815487-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-Paysafe-Payments](https://support.mindbodyonline.com/s/article/210815487-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-Paysafe-Payments?language=en_US)
