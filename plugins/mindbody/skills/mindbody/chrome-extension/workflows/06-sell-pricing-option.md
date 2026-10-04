---
workflow: Sell a pricing option, contract or product at checkout
safety: 🔴 Money or irreversible
---
# Sell a pricing option, contract or product at checkout

Ring up a class pack, membership/contract or retail product at **Point of Sale** (Retail) and take payment with a card on file, another payment method, or a promo code. Typical phrasings: "sell Sarah a 10-class pack", "put Marcus on the unlimited membership", "ring up a water bottle for Dana, use the card on file".

## Ask the person for
- Client name (or "walk-in" for products and gift cards only).
- Exactly what to sell: pricing option / contract name, or product and quantity. If several similarly named items exist, list them with prices and ask.
- Payment method: card on file, cash, check, Account, gift card, comp, other. If the person has not said, ask. Never invent a method.
- Promo code, if any (codes are case-insensitive).
- For contracts: start/charge date if the contract asks for one (and whether a deposit or registration fee applies).
- Card details are never typed by you. If a new card is needed, ask the person to enter it themselves on the form or terminal.

## Read first
- [Selling products](../../articles/pos-payments/203260133-Selling-products.md) — POS layout, Add Item.
- [Promo codes for contract sales](../../articles/pricing-memberships/203274253-Will-a-promotion-work-on-a-contract.md) — Contracts / Packages tab and promo field.
- [Promo Codes screen](../../articles/pricing-memberships/203258713-Promotions-Promo-Codes.md) — what a code covers and its limits.
- [Payment Methods screen](../../articles/pos-payments/203259823-Payment-Methods-screen.md) — what each button means (CC Key/Stored, Account, Comp).
- [Account payments](../../articles/pos-payments/203254193-Account-Payments-Apply-Payments.md) and [Redeeming a gift card](../../articles/pricing-memberships/204078876-Redeeming-a-gift-card.md) — if paying by account or gift card.

## Steps
1. **Open Point of Sale** — navigate to `https://clients.mindbodyonline.com/app/business/asp/adm/main_retail.asp` (contract sales: `main_retail.asp?fl=true&tabID=3`). Confirm the site and, on multi-location sites, the location.
2. **Select the client** — search by last name, pick the right person (check email/phone). If none, add them first ([playbook 02](02-add-new-client.md)).
3. **Add the item** — in the **Add Item** box on the right:
   - Pass or single session: **Services** tab; search by name or narrow with the service category dropdown.
   - Membership/autopay: **Contracts / Packages** tab, choose the contract.
   - Retail: **Products** tab (All products or Favorites), search, click the product.
   - Gift card or account credit: **Payments/Gift Cards** tab.
   Adjust quantity and price only if the person asked, then click **Add Item**. Only the contract's own price and options apply; do not edit other fields.
4. **Promo code** — if given, type it in **PROMOTION CODE** and click **Apply**; the discount must show on the ticket. If it errors, report the exact message and do not try other codes. No stacking; the code must cover the item's pricing option.
5. **Pick payment** — choose the method button the person named:
   - Card on file: **CC Key/Stored** (integrated merchant account). Confirm which card it is: client's **Client Info** > **Billing Information** shows the stored card (last digits only; do not read out more).
   - **Card Reader** (terminal): the client taps; you cannot cancel once tapped.
   - **Cash**, **Check**, **Account**, **Prepaid Gift Card** (enter ID, **Look Up**), **Comp/Guest**, **Other**. For split payments, set each amount and check Amount Remaining is $0.00.
   If the method button is missing, it may be inactive in Payment Methods; tell the person.
   Do not tick the option to store a new card on the profile unless asked: storing replaces the current card, which autopays also use.
6. 🔴 **Stop** — before the final click, `get_page_text` the ticket and show one line: client, item(s) and quantity, promo applied, grand total, payment method (and card ending digits for card on file), and for contracts the number and schedule of autopays and deposit. Wait for an explicit yes for this sale.
7. **Complete** — choose the receipt option the person wants (default: email if they ask, else no receipt), then click the **Save/Complete Sale** button (`find` it; its label varies by receipt choice). Wait for the page to refresh.

## Verify
- A sale confirmation appears; note the Sale ID.
- Client's **Purchases** screen shows the sale with the right Description, Amount Paid and Payment Method ([Client Purchases](../../articles/clients/215843338-Client-Purchases-Screen-overview.md)).
- Client's **Account Details** > **Available for Use** lists the new pass (Remaining, Expiration Date) or **Contracts** shows the contract and its **Autopays**.

## If it goes wrong
- Item missing: Services Pricing may be inactive, restricted to members, or not available at this location; do not change settings.
- Card declined or gateway error: stop, tell the person, do not retry repeatedly or try another card without being asked.
- Sold the wrong item or amount: stop. Do not void or refund on your own; that is a separate 🔴 flow ([Returns, refunds and voids](../../articles/pos-payments/203259303-Returns-Refunds-and-Voids.md)).
- Needs the Complete sales transactions at POS permission; if absent, say so.

## Variations
- Sale needed during class check-in: use **Buy** on the roster ([playbook 03](03-check-in-client-to-class.md)).
