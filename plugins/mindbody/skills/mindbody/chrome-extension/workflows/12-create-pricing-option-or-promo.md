---
workflow: Create a pricing option, autopay contract or promo code
safety: 🟡 Changes data
---
# Create a pricing option, autopay contract or promo code

Set up something new for clients to buy: a single-visit, multi-visit or unlimited pricing option (optionally an intro offer), an autopay contract, or a promo code. Typical phrasings: "add a 10-class pack to Yoga", "create a $49 intro month for new clients", "make a monthly unlimited membership contract", "set up a 20% off code for October". Nothing here charges anyone, but the new item becomes sellable (and possibly visible online), so state exactly what you will create before saving.

## Ask the person for
- **Which kind**: pricing option, contract (autopay), or promo code (or a combination, e.g. an intro option plus a code).
- **Pricing option**: name, number of sessions (limited number, Unlimited, or Membership), service category it pays for, revenue category, "Expires after" (number plus Days/Months), price, online price (if sold online), sales tax, activation date mode (sale date, first visit, custom date).
- **Intro offer?** Yes for new clients only, or new and existing clients (each client can buy once).
- **Contract**: name, items and prices, number of autopays or month-to-month, billing day, what happens after the last payment, whether to sell online.
- **Promo code**: code text (or let Mindbody generate it), percent or amount, what it applies to, start/end dates, max uses per client, staff-only or online too, and for contracts how many autopays it discounts.
- If any required field is missing, ask; do not guess prices, expirations or session counts.

## Read first
- [How to add pricing options overview](../../articles/pricing-memberships/203253823-Pricing-options-memberships.md) — where options can be created
- [Pricing Options on the Settings screen](../../articles/pricing-memberships/213024177-Pricing-Options-screen.md) — every field
- [How to create an intro offer](../../articles/pricing-memberships/203257543-How-do-I-create-an-introductory-special.md) — eligibility rules
- [How to add and set up a contract](../../articles/pricing-memberships/203253843-Setting-up-contracts.md) — autopay options
- [Promo Codes screen](../../articles/pricing-memberships/203258713-Promotions-Promo-Codes.md) — code fields
- [Promo codes for contract sales](../../articles/pricing-memberships/203274253-Will-a-promotion-work-on-a-contract.md) — discounting autopays

## Steps
1. **Set up the browser** — follow [the general guide](../README.md) (load tools, `tabs_context_mcp`, new tab). Confirm the site name in the header.
2. **Pricing option: open the screen** — navigate to https://clients.mindbodyonline.com/app/services-products/pricing (Services & Products > Pricing) and `find` "Add pricing option". For all fields, including scheduling restrictions, use the classic screen instead: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_series.asp (Settings > Pricing > Pricing Options), then **+Add New**. The classic screen exists only on Accelerate/Ultimate; if missing, use the Pricing screen. If it redirects home, use the menu path.
3. **Fill the pricing option** — use `read_page` (interactive) to get refs, then `form_input` or clicks. Minimum: name, number of sessions (Limited / Unlimited / Membership), service category, revenue category, Expires after, price, activation date. Appointment categories add an **Appointment type** to assign. Single visit = 1 session; unlimited = Unlimited sessions with an expiry matching the period. Leave **Sell online** unticked unless asked; a blank **Online price** means $0, so set it deliberately.
4. **Intro offer** — in the intro field choose **Yes, for new clients only** or **Yes, for new and existing clients** (classic screen: Advanced Settings > **Introductory offer**). Tick **Promote in Mindbody app** only if asked (a $0 promoted offer carries a fee, see the article).
5. **Save the option** — state the summary (name, sessions, price, expiry, category), then click **Add**. Check for a validation message.
6. **Contract: open and name it** — navigate to https://clients.mindbodyonline.com/app/services-products/contracts, click **+Add a Contract**, fill "What would you like to call this contract?".
7. **Contract items** — in Pick Contract Items add the pricing option(s) (search, set **One-time item**, **Price**, **Quantity**, then **Assign**), or **+ Add a new item** to create one inline (quantity can only be set after the first save, then edit it from Contract Items).
8. **Contract options** — set intro offer, **Run autopay** (On a set schedule is the recommended default), number of autopays (max 99) or Month-to-Month, **When will clients be charged?**, **What happens after N payments?**, **Sell online**. 🔴 Stop before touching "Apply this setup change to ongoing autopays?" or any free-first/last-autopay option on an existing contract: that cannot be undone, so show the effect and wait for an explicit yes. Then click **Add** (top right).
9. **Promo code** — navigate to https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_promotion.asp (Settings > Pricing > Promo Codes), click **+Add New**. Fill Promotion name, Promotion code (or **Generate**), Discount type and amount, Max uses per client, dates, and Define promotional items. Leaving items blank discounts the whole purchase, so narrow it if the person named a target.
10. **Promo on a contract** — choose the pricing option inside the contract (not the contract name) as the item, tick **Apply discount on autopays** and enter how many autopays to discount (cannot exceed the contract's count; month-to-month covers only the first two). Click **Add**.

## Verify
- Reopen the list (Pricing, Contracts or Promo Codes) and confirm the new row with the right price, expiry and Active status; use `get_page_text`.
- Optionally open Point of Sale for a test client view (do not complete a sale) to confirm the item appears; the person should confirm it is not visible online if it should not be.

## If it goes wrong
- Option not showing in POS or online: check Sell online, Online price, restrictions and that it is not Discontinued.
- Permissions missing (pricing options, promotions, contracts): tell the person which permission is needed.
- Custom activation date is unavailable inside a contract; use sale date or first visit.
- Promo code error "Invalid Promocode. Exceeding discount autopay count": lower the autopay number.
- Pricing options cannot be deleted, only discontinued; if the person wants one removed, say so.

## Variations
- Copy an existing option: [How to duplicate a pricing option](../../articles/pricing-memberships/How-to-duplicate-a-pricing-option.md).
- Choose activation behavior: [Activation date options](../../articles/pricing-memberships/203257593-What-are-the-differences-between-the-different-pricing-option-activation-dates.md).
- Deactivate a promo code: open it and clear **Active**, per the Promo Codes screen page.
- Memberships benefits: [Membership Setup screen](../../articles/pricing-memberships/203259703-Membership-Setup-screen.md).
