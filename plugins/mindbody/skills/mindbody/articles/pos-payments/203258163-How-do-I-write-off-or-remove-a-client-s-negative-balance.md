---
title: How to write off or remove negative account balances
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203258163-How-do-I-write-off-or-remove-a-client-s-negative-balance?language=en_US
source_updated: 2026-09-25
---
# How to write off or remove negative account balances

Clears a client's negative account balance without collecting money, either by voiding the original sale or by recording a debt write-off at the Point of Sale. If the client actually pays, use Receive Payments or account credit instead.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/main_retail.asp (Point of Sale)
- Menu path: **Point of Sale**; payment method setup is on the **Payment Methods** settings screen

## Steps
### Option A: void the sale
1. Follow the void steps in the Returns, Refunds, and Voids article. Possible only if the item has no associated visits/usage and a single payment method was used.
2. Both the purchase and the negative balance disappear. Re-ring the sale correctly if needed.

### Option B: write off (do in order)
1. Create a payment method: open the Payment Methods screen, name it clearly in **Payment Method** (e.g. Debt write-off), tick **Active?**, **Allow $0?**, **Allow>$0?**. Optionally add a **PayNotes Label** and tick **PayNotes?** to prompt for a reason. Finish adding as usual.
2. Create an account payment item: follow the "sell and give account credit" article and enter **Payment on account** as the Description (name); leave other settings.
3. At **Point of Sale**, select the client.
4. Under Add Items click **Payments/Gift Cards** and choose the write-off account payment.
5. Pick one:
   - Option 1 (visible in sales reports): enter the negative balance amount in both Price and Credit, then apply a 100% discount so it is not counted as revenue.
   - Option 2 (hidden from reports): enter $0 in Price and the balance amount in Credit.
6. Click **Add Item**. Grand total and amount remaining show $0.00.
7. Select the write-off payment method and complete the transaction.

### Report on write-offs
- Run the Sales report or Sales by Category report with **Payment Method** set to the write-off method and **Accounting Basis** set to Accrual & cash combined. Export to Excel to sum the Subtotal column.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first. Voiding permanently removes the transaction; a write-off forgives the debt.
- Zeroing a negative balance leaves the original sale counted as revenue.
- Daily Closeout and Sales reports may disagree if: the account payment was not discounted 100%; tips are excluded from Sales totals (General Setup & Options) while Closeout includes them; sales were backdated after closing and Closed Data was used instead of Date Range; or account credit sold at $0 price with credit above $0 (needs Accrual & cash combined in the Sales report).
- If a void is blocked, see the "Reasons you may not be able to void a sale" article.

## Related
- [Returns, Refunds, and Voids](203259303-Returns-Refunds-and-Voids.md)
- [Why can't I void a sale](203258313-Why-can-t-I-void-a-sale.md)
- [Receiving payments on negative account balances](https://support.mindbodyonline.com/s/article/203254233-Receiving-payments-on-negative-account-balances?language=en_US)
- [How to sell and give account credit to a client](https://support.mindbodyonline.com/s/article/Putting-Credit-on-Client-Account?language=en_US)
- [Payment Methods screen](203259823-Payment-Methods-screen.md)
- [Account Balances report](https://support.mindbodyonline.com/s/article/203256673-Account-Balances-report?language=en_US)
- [Convert declined autopays to a negative account balance](https://support.mindbodyonline.com/s/article/221392248-How-can-I-convert-Declined-AutoPays-to-a-negative-account-balance-for-better-tracking?language=en_US)
- [Let clients pay negative balances online](https://support.mindbodyonline.com/s/article/203270843-How-can-I-get-my-clients-to-pay-their-negative-account-balance-online-themselves?language=en_US)
- [Daily Closeout report](203257183-Daily-Closeout-report.md)
- [Sales report](../reports/203257193-Sales-Report.md)
