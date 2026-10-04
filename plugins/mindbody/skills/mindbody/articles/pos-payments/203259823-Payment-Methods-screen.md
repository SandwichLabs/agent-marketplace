---
title: Payment Methods screen
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203259823-Payment-Methods-screen?language=en_US
source_updated: 2025-05-28
---
# Payment Methods screen

Where a studio adds, renames, activates/deactivates, and configures the payment-method buttons shown at the Point of Sale. Needed when a checkout button is missing, a custom tender (e.g. Trade) is wanted, or refund behavior must be restricted.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/appshell/shuttle/asp/adm/adm_tlbx_paymeth.asp
- Menu path: **Settings** > **Retail** > **Payment Methods** (or type "Payment Methods" in the top search bar)

## Steps
### Add a payment method
1. Open the screen; in the "Add New" section type the new method's name.
2. Tick the settings you want (see below).
3. Click **Add**. It appears in the list at the bottom.

### Edit existing methods
1. Change the name or tick/untick checkboxes in the list.
2. Click **Update** at the bottom to save.

## Settings & fields
- **Payment Method**: name shown on the POS button; most can be renamed without changing behavior (do not rename the Credit no-auth methods).
- **Reserved**: marks hardcoded methods with limited editing; "Third Party" ones come from third-party payer client profiles.
- **Active?**: if unchecked, no POS button.
- **CashEQ?**: check if the method is a real cash equivalent (card, check). Uncheck for things like trade/other so Sales reports reflect it properly.
- **Allow $0?**: method offered even when sale total is zero (e.g. 100% discount).
- **Allow>$0?**: method usable when total is above zero.
- **Allow Refund?**: controls which methods can receive refunds (e.g. allow only business credit).
- **PayNotes?**: adds a note box at payment (check number, trade info). Not available for merchant-account card payments. Shows on receipts, not visible to clients on consumer site, findable via Manage Sales.
- **PayNotes Label**: title for that note box, shown greyed at POS.
- Greyed-out checkboxes cannot be changed.

### Default methods
- **Cash**, **Check**.
- **Credit (AMEX)**, **Credit (Visa/MC)**, **Credit (Discover)**, **Credit (ATM)**: no-auth records for use with an external card processor, only for bookkeeping.
- **Comp/Guest**: free service/product.
- **Other**: catch-all alternative tender.
- **Account**: charge to client's account balance.
- **Prepaid Gift Card**, **Rewards Program** (points-to-cash rate set in General Setup & Options), **Room Charge** (needs Rooms and Resources; shows in sales reports Notes column under "Misc (Room Charge)"), **Staff Charge** (appears once professional products is enabled), **Third Party Payers**, **Trade**: appear only when the related feature is enabled.
- With an integrated Mindbody merchant account, POS also shows **CC Key/Stored**, **CC Swiped** (USB swiper), and **ACH** (if ACH service used). These are not listed on this screen and cannot be edited individually. Merchant integration is confirmed by a "Mindbody - Merchant Account Live" email and **Reports** > **Payment Processing**.

## Gotchas
- Requires staff permission "Set up payment methods" (Settings).
- Some features depend on software package.
- Adding/removing methods here does not affect ability to accept credit cards. Studios not taking cards can deactivate the four Credit no-auth methods to clean up POS.
- Deactivating a method removes it as a report filter and may hinder sorting of past sales.
- Keyed card entry usually costs more in fees than swiping.
- Apple Pay and similar alternatives for Mindbody Payments are enabled in the Payments Portal, not here.

## Related
- [Why-isn-t-this-feature-available](../settings-navigation/Why-isn-t-this-feature-available.md)
- [Staff-Permissions-Settings](../staff/Staff-Permissions-Settings.md)
- [203255403-Adding-or-removing-no-auth-credit-card-payment-methods](https://support.mindbodyonline.com/s/article/203255403-Adding-or-removing-no-auth-credit-card-payment-methods?language=en_US)
- [204363803-How-do-I-disable-a-payment-option](https://support.mindbodyonline.com/s/article/204363803-How-do-I-disable-a-payment-option?language=en_US)
- [203258783-How-to-manage-clients-purchasing-on-account](https://support.mindbodyonline.com/s/article/203258783-How-to-manage-clients-purchasing-on-account?language=en_US)
- [203258793-Third-party-Payers](https://support.mindbodyonline.com/s/article/203258793-Third-party-Payers?language=en_US)
- [227078488-How-to-set-up-work-trades-for-exchange-of-services](https://support.mindbodyonline.com/s/article/227078488-How-to-set-up-work-trades-for-exchange-of-services?language=en_US)
- [203259783-General-setup-options-explained](../settings-navigation/203259783-General-setup-options-explained.md)
- [How-to-enable-alternative-payment-methods-like-Apple-Pay-in-the-Payments-portal-Mindbody-Payments-All-Regions](https://support.mindbodyonline.com/s/article/How-to-enable-alternative-payment-methods-like-Apple-Pay-in-the-Payments-portal-Mindbody-Payments-All-Regions?language=en_US)
