---
title: Account payments, purchasing on account, and the account payment method
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203254193-Account-Payments-Apply-Payments?language=en_US
source_updated: 2026-09-29
---
# Account payments, purchasing on account, and the account payment method

Covers the house-account feature: selling account credit in advance, letting clients run a tab (negative balance) and pay it off, and where to track balances. Needed when setting this up or selling/applying credit at POS.

## Where in Mindbody
- Payment Methods: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_paymeth.asp (**Settings** > **Retail** > **Payment Methods**)
- General Setup & Options: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_setup.asp (**Settings** > **General** > **General Setup and Options**)
- Account Payments: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_credits_ae.asp?cardType=account (**Settings** > **Pricing** > **Account Payments**)

## Steps
### Enable the account payment method
1. Payment Methods: tick **Active?** beside **Account**, click **Update**.

### Allow purchases on account
1. General Setup and Options > expand **Client Management** > tick **Account Purchases - Allow All Clients** > **Update**. (Allows paying with account credit; does not by itself decide whether balances may go negative.)

### Create an account payment
1. Account Payments > **Add New**, fill fields below, save.

### Use at Point of Sale
- Purchase on account: add item to ticket, choose payment method **Account**, complete sale.
- Sell credit: see the sell/give credit article.
- Pay off debt: **Receive payment** appears at checkout when a client owes money; allocate to specific past account purchases.
- Assignable gift cards can be redeemed as account credit (package-dependent).

## Settings & fields
- **Description** (shows in POS and receipts), **Barcode**, **Selling price**, **Credit amount** (set both to $0.00 for custom-amount sales; fix them for a specific purpose such as a course payment plan).
- **Force price and credit fields to match in Business Mode**: unchecked lets you sell $50 credit for $40 at POS. Consumer site always matches. Locked after the first sale.
- **Allow clients to choose the amount**: consumer-site custom amounts; locked after the first sale.
- **Sell online**: needs integrated merchant account processing.
- **Members only**: restrict to selected memberships (Ctrl/Cmd-click for multiples); Accelerate and Ultimate only.

## Gotchas
- Permissions: **Set up payment methods**; **Manage account credits, gift cards, contracts, and packages**.
- Clients cannot buy account payments or pay owed balances in Mindbody mobile apps.
- Negative balances: consider client alerts for thresholds.
- Tracking: client **Account Details** > GIFT/Debit section; **Account Balances report** (statements, bulk autopays, reconciling); **Sales by Product report** lists account payments.
- Consumer-site balance viewing, use, and payoff are separate help articles (pay-off link can be generated for clients).
- Some features depend on software package.

## Related
- [Payment Methods screen](203259823-Payment-Methods-screen.md)
- [Settings for clients purchasing on account](https://support.mindbodyonline.com/s/article/203258783-How-to-manage-clients-purchasing-on-account?language=en_US)
- [Using account payments and account method](https://support.mindbodyonline.com/s/article/What-is-the-account-payment-method-and-why-would-I-use-it?language=en_US)
- [Sell/give account credit](https://support.mindbodyonline.com/s/article/Putting-Credit-on-Client-Account?language=en_US)
- [Receiving payments on negative balances](https://support.mindbodyonline.com/s/article/203254233-Receiving-payments-on-negative-account-balances?language=en_US)
- [Account Balances report](https://support.mindbodyonline.com/s/article/203256673-Account-Balances-report?language=en_US)
- [Client Account Details screen](../clients/215843418-Client-Account-Details-Screen-overview.md)
- [Report for account payments](https://support.mindbodyonline.com/s/article/212880878-How-do-I-pull-a-report-of-only-Account-Payments-Payment-on-Account-report?language=en_US)
- [Restrict account purchases](https://support.mindbodyonline.com/s/article/216080627-Why-was-my-client-able-to-make-a-purchase-to-Account?language=en_US)
- [Partial refunds of account payments](https://support.mindbodyonline.com/s/article/Partial-Refunds-of-Account-Payments?language=en_US)
- [Redeeming gift cards](../pricing-memberships/204078876-Redeeming-a-gift-card.md)
- [Point of Sale](https://support.mindbodyonline.com/s/article/203258753-Retail-Point-of-Sale?language=en_US)
- [Client alerts](../clients/203259733-Client-alerts.md)
