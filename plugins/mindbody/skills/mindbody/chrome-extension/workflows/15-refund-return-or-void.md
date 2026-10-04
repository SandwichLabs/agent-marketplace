---
workflow: Return, refund or void a sale
safety: 🔴 Money or irreversible
---
# Return, refund or void a sale

Reverse a purchase: a full return with refund, a single-item (line-item) or partial return, a return with no refund, or a void. Typical phrasings: "refund Jen's 10-class pack", "void that sale I just rang up", "give Marcus his money back for the water bottle", "return it to account credit". Voiding and card refunds cannot be reversed, so every commit needs its own explicit yes.

## Ask the person for
- **Client name**, the **item or sale** (date, amount, Sale ID if they have it) and the **reason** (required by Mindbody; for a chargeback, the notice number).
- **Scope**: whole sale, one line item, or part (e.g. unused sessions only).
- **Refund method** wanted: original card, ACH, account credit, cash or check, or no refund. If they just say "refund it", explain the options and ask.
- Is this a **chargeback**? If the bank has already pulled the money, never refund to the card (see Variations).

## Read first
- [Returns, refunds, and voids](../../articles/pos-payments/203259303-Returns-Refunds-and-Voids.md) — core flow and rules
- [How to process line-item returns](../../articles/pos-payments/Line-item-returns.md) — one item of a ticket
- [Partial sale returns](../../articles/pos-payments/203280743-Partial-Sale-Returns.md) — refund the unused part of a pack
- [Why can't I void a sale](../../articles/pos-payments/203258313-Why-can-t-I-void-a-sale.md) — blockers
- [Record a chargeback](../../articles/pos-payments/203274893-Should-I-process-a-return-to-the-credit-card-if-a-customer-files-a-Chargeback.md) — no card refund
- [Undo a return](../../articles/pos-payments/209565108-How-do-I-undo-or-void-a-return-refund.md) — fixing a mistake

## Steps
1. **Set up the browser** — see [the general guide](../README.md). Confirm the site.
2. **Find the sale (🟢)** — search the client (Find a client at the top), open **Purchases**, `get_page_text`, and locate the item. Confirm with the person which row. Note whether it shows "Unsettled transaction" and which payment method it used.
3. **Choose void vs return** — Void removes the sale entirely and is only available if the sale shows "0 in use" and, for cards, before settlement (often same day). Sites with auto capture (Mindbody Payments, TSYS) have no void, only refunds. Anything else is a return. Tell the person which applies and why.
4. **Open Manage Sales** — click the **Sale ID** or **Return/Void** in the Actions column (`find` it by description).
5. **If visits use the pricing option** — a sale tied to class or appointment visits shows an **# in use** link (red "In Use"). Open it, then click **Make All Unpaid** or **Early** per visit, or **Reassign** to another pricing option, and return to Manage Sales. Early-cancelling appointments changes the schedule, so list what you will cancel to the person first.
6. **Void path** — 🔴 Stop: show client, item, amount, payment method and "this permanently removes the sale and cannot be undone", and wait for an explicit yes. Warn about Chrome's confirm box. Click **Void**, then **Yes, Void This Sale**.
7. **Return path** — click **Return All** (whole transaction) or **Return this item** (one line). Enter the reason. For products, tick **Add items back into inventory?** only if stock should return. For a partial quantity on one line, untick the inventory box and edit the amount to quantity x unit price in the next step.
8. **Refund method** — click **Choose Refund Method** to refund, or **Return without a Refund** to keep the money (item removed, no refund shown). Select the Refund method and amount; tick **Use additional refund method?** to split, e.g. unused value to the original method and used value to Account. Card refunds go only to the original card; if it is expired or closed, use account credit, cash, check or gift card. You cannot refund more than the original amount, and only one refund per purchase is allowed.
9. 🔴 Stop: summarize client, item(s), reason, refund method(s) and amounts (card type and last four if shown), and that any refund makes the pricing option inactive and voids related commission. Wait for an explicit yes, then click **Save No Receipt** or **Save Print Receipt**. A different second action (another item) needs its own yes.

## Verify
- Purchases shows the sale as **Returned** (red) or gone (voided); a returned sale with a card type was refunded to that card, $0 with no payment method means no refund.
- For pricing options, Account Details lists the option under Inactive; for partial returns, finish the reassign steps in the partial returns article.
- Report amount, method and timing (card refunds show for the client in about 5-10 business days; original processing fees are not returned).

## If it goes wrong
- No Void or Refund button: missing permission (Void/edit past sales, Issue sale refunds, Issue sale refunds to credit cards). Tell the person; do not change permissions yourself.
- Void unavailable: already settled, already returned (undo the return first), or auto capture; refund instead.
- Only one line-item return or partial per card/ACH transaction: plan the amount carefully before saving.
- ACH: void quickly if offered; otherwise wait at least 7 days to refund.
- Refund declined may go back to the business account without notice; tell the person to watch the processor portal.

## Variations
- **Chargeback**: do not refund the card. Create a **Chargeback** payment method once (Settings > Payment Methods; tick Active, CashEQ, Allow Refund), then Return All with Refund Method 1 set to Chargeback. Page: [record a chargeback](../../articles/pos-payments/203274893-Should-I-process-a-return-to-the-credit-card-if-a-customer-files-a-Chargeback.md); fees: [Mindbody Payments chargebacks](../../articles/pos-payments/MINDBODY-Payments-chargebacks-US-Beta.md).
- **Undo a return** made by mistake: Manage Sales on the return sale > **Void** (not possible for card returns).
- **Mindbody Payments rules by method** (windows, waits): [Refund and void guidelines](../../articles/pos-payments/Refund-void-guidelines-for-MINDBODY-Payments-US-Beta.md).
