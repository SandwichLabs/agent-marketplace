---
title: How to run a transaction on the WisePOS E terminal (Mindbody Payments, All Regions)
category: pos-payments
source: https://support.mindbodyonline.com/s/article/Running-a-transaction-on-your-WisePOS-E-terminal-Mindbody-Payments?language=en_US
source_updated: 2026-09-28
---
# How to run a transaction on the WisePOS E terminal (Mindbody Payments, All Regions)

How to take card payments on an already-paired WisePOS E terminal from Point of Sale or Appointment Checkout, including tips, split payments, and cancelling.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/main_retail.asp?fl=true&tabID=3 (Point of Sale)
- Direct link: https://clients.mindbodyonline.com/app/business/mainappointments/index (Appointment Schedule)
- Menu path: **Point of Sale** or **Appointments** in the left navigation.

## Steps
### From Point of Sale
1. Search for a client or start a walk-in sale.
2. With multiple locations, select the location where the terminal is registered before adding items.
3. Under Add Items, pick items and click **Add Item**.
4. Select a payment method, then click **Card Reader**; the items appear on the terminal.
5. With several terminals, choose one from **Select Reader**.
6. If prompted, tick the box to store the card on the client profile; click **Next**.
7. After payment, choose a receipt: email (editable, prefilled), customer copy, gift receipt, or invoice.
8. Click **Complete Sale**.

### From Appointment Checkout
1. Click the appointment; choose the location if needed; optionally pick the staff member credited with sale and tip.
2. Select **Checkout** from the action menu, then **Card Reader**.
3. Optionally pick the terminal and tick the store-card box.

### Tip and finish
1. Client sees the tip screen on the terminal, then final total with an Edit tip button, then taps, inserts, or swipes.
2. Choose receipt type and click **Complete Purchase**; wait for the screen to refresh before starting another ticket.

### Split payment
1. Add the item, choose the first method (e.g. **Cash** or **CC (Key/Stored)**) and set its amount; Amount Remaining updates.
2. Click **Card Reader** last for the remainder.

### Stop or edit a payment in progress
- Click **X** at top right to clear the terminal prompt. If no X and nothing tapped yet, refresh and restart the terminal.

## Settings & fields
- Tip prompt appears only if tipping is enabled and at least one staff member earns tips; defaults 18%, 20%, 25%, custom, or skip. Only the owner via Support can change defaults.
- Accepted: magstripe, EMV chip, Australian EFTPOS with brand logo, prepaid cards, contactless/NFC (including Apple/Google Pay; Tap to Pay on iPhone needs iOS 18.0.1+).

## Gotchas
- Terminal joins only password-protected Wi-Fi. WisePOS E is supported but no longer sold in US, Canada, UK, select EU.
- Once a card is tapped/inserted/swiped, you cannot cancel or void; let it finish and refund. Closing the browser mid-payment leaves a pending card charge that drops in 5-7 business days.
- Split payments: one card must be keyed/stored and the terminal must be last; two different cards on the terminal not allowed.
- Recurring-payment contracts: NFC wallets, Interac, and brandless EFTPOS cannot be stored for future payments (can pay in full); a physical card tapped can be stored.
- Storing a card replaces the client's existing saved card. The terminal cannot save a card without a sale; mobile wallets cannot be saved.
- **CC (Swipe)** does not work with the terminal (button disabled); use a USB swiper.
- Business gift cards are not accepted on the terminal; use USB swiper or enter ID manually.
- Tips missing: Appointment Checkout Review may be on; restart and tick **Add Product(s) or Tip in Retail**. Tip is split evenly across services by default, excludes products, and uses discounted totals.
- Walk-in sales sell only products and gift cards.
- ⚠️ Irreversible / financial — confirm with the user first (card charge).

## Related
- [Activating a WisePOS E terminal](https://support.mindbodyonline.com/s/article/Activating-a-WisePOS-E-terminal-Mindbody-Payments?language=en_US)
- [WisePOS E best practices and troubleshooting](https://support.mindbodyonline.com/s/article/How-to-troubleshoot-and-apply-best-practices-when-using-the-WisePOS-E-terminal-Mindbody-Payments-All-Regions?language=en_US)
- [Stripe Reader S710 transactions](https://support.mindbodyonline.com/s/article/How-to-run-a-transaction-on-your-Stripe-Reader-S710-Mindbody-Payments-All-Regions?language=en_US)
- [Point of Sale](https://support.mindbodyonline.com/s/article/203258753-Retail-Point-of-Sale?language=en_US)
- [Appointment Checkout](../appointments/Appointment-Checkout.md)
- [Tips](203258723-Tips.md)
- [Transactions report](https://support.mindbodyonline.com/s/article/Transactions-report-for-MINDBODY-Payments?language=en_US)
- [Mindbody Payments FAQ](https://support.mindbodyonline.com/s/article/MINDBODY-Payments-account-FAQ-US-Beta?language=en_US)
- [Walk-in sales](https://support.mindbodyonline.com/s/article/How-to-sell-edit-and-manage-print-email-and-return-walk-in-sales?language=en_US)
- [Update client billing info](../clients/203257913-How-do-I-update-my-clients-billing-information.md)
