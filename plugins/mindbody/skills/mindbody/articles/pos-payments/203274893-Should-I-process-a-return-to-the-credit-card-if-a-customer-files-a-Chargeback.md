---
title: How to record a client chargeback in your software without processing a return to credit card
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203274893-Should-I-process-a-return-to-the-credit-card-if-a-customer-files-a-Chargeback?language=en_US
source_updated: 2024-11-22
---
# How to record a client chargeback in your software without processing a return to credit card

When a client disputes a charge with their bank, the processor has already pulled the money back, so the card must NOT be refunded again. Instead, record the sale as returned to a custom "Chargeback" payment method so books and the client's access reflect reality.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_paymeth.asp
- Menu path: **Settings** > **Payment Methods**; then client **Purchases** screen > **Return/Void**

## Steps
### 1. Create a Chargeback payment method (one-time)
1. Open **Payment Methods** and check that "Chargeback" is not already listed.
2. In "Add New", type **Chargeback** and tick **Active?**, **CashEQ?**, and **Allow Refund?**.
3. Click **Add**.

### 2. Return the sale to Chargeback
1. Find the client who filed the chargeback. If the notice lacks a name, match the last four digits of the card on the notice to a client.
2. Open the client's **Purchases** screen and click **Return/Void** next to the sale.
3. On Manage Sales choose **Return All**.
4. Enter a reason (e.g. the chargeback notice number).
5. Click **Choose Refund Method**.
6. Set Refund Method 1 to **Chargeback**.
7. Click either **Save** button.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first. Never refund to the client's credit card for a chargeback; do not pick any option resembling the card.
- If the sale was already refunded to the card (partly or fully), this cannot be fixed afterward.
- Avoid ticking "Allow $0" / "Allow>$0" on Chargeback, or it becomes selectable at POS, which is almost never wanted.
- CashEQ keeps cash-based reports accurate; Allow Refund is required for step 2.

## Related
- [203255573-Chargebacks-FAQ](https://support.mindbodyonline.com/s/article/203255573-Chargebacks-FAQ?language=en_US)
- [208710727-How-do-you-look-up-a-member-by-the-last-4-of-their-credit-card-or-account-number](https://support.mindbodyonline.com/s/article/208710727-How-do-you-look-up-a-member-by-the-last-4-of-their-credit-card-or-account-number?language=en_US)
- [203259823-Payment-Methods-screen](203259823-Payment-Methods-screen.md)
- [210812917-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-TSYS](https://support.mindbodyonline.com/s/article/210812917-How-do-I-complete-a-partial-refund-of-a-credit-card-transaction-TSYS?language=en_US)
- [220433667-I-accidentally-sold-the-wrong-item-to-a-client-How-do-I-return-it-and-buy-the-correct-item-without-charging-their-credit-a-second-time](https://support.mindbodyonline.com/s/article/220433667-I-accidentally-sold-the-wrong-item-to-a-client-How-do-I-return-it-and-buy-the-correct-item-without-charging-their-credit-a-second-time?language=en_US)
