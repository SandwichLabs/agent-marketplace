---
title: Pricing option activation date options
category: pricing-memberships
source: https://support.mindbodyonline.com/s/article/203257593-What-are-the-differences-between-the-different-pricing-option-activation-dates?language=en_US
source_updated: 2026-07-10
---
# Pricing option activation date options

Explains the three activation date modes for pricing options (sale date, first visit, custom date) and how each behaves. Needed when a pass seems to expire early, roll over, or be usable too soon.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_setup.asp (General Setup & Options)
- Menu path: **Settings > General > General Setup and Options > Client Management**
- Edit activation dates in **Services & Products** pricing or the **Pricing Options** settings screen (custom date only here).

## Steps
### Enable activation date enforcement
1. Open General Setup & Options, expand **Client Management**.
2. Tick **Pricing Option Activation Dates - Enforce**, click **Update**.
(Activation dates are optional; without them only expiration date decides eligibility.)

## Settings & fields
- **On the sale date**: activation = purchase day; duration sets expiry (bought May 1 with 7 days expires May 7). Only visits inside the active range are reconciled.
- **On the date of the client's first visit after purchase**: the first time this specific pass is used for a visit (not the client's first visit ever). Shows the sale date until redeemed. If it hits expiry unused, dates roll forward by one duration repeatedly until a visit is attached. If the first visit is cancelled and no other is booked, it expires on the original date and goes inactive; if several visits are booked, activation moves to the next visit. **Recalculate** on Account Details resets an unactivated option to the sale date (it may then expire/inactivate if the duration is too short).
- **On a custom date**: chosen date (Pricing Options screen only), useful for seasonal offers and exact expiry dates. Needs **Pricing Option Activation Dates - Enforce** to block use before that date.

## Gotchas
- Custom date is unavailable once the option is in a contract or package ("Cannot choose a specific date...").
- Selling or reactivating an option whose custom date puts it already past expiry makes it expire immediately; Recalculate moves it to Inactive. Older ones auto-discontinue after nightly scripts run.
- To change activation for future sales, edit the pricing option; to make it retroactive tick "Update for past sales".
- Per-client changes, expiring unused first-visit options and extending duration have separate articles.

## Related
- [Pricing Options on the Settings screen](213024177-Pricing-Options-screen.md)
- [Pricing options & memberships](203253823-Pricing-options-memberships.md)
- [Edit a pricing option activation date](https://support.mindbodyonline.com/s/article/203257893-How-do-I-edit-a-pricing-option-activation-date?language=en_US)
- [Adjust a first-visit activation date](https://support.mindbodyonline.com/s/article/203268693-How-do-I-adjust-a-pricing-option-that-activates-on-the-date-of-client-s-first-visit-to-cover-a-visit-before-its-activation-date?language=en_US)
- [Expire an unused first-visit pricing option](https://support.mindbodyonline.com/s/article/How-do-I-expire-terminate-an-unused-pricing-option-that-activates-on-date-of-first-visit?language=en_US)
- [Pricing option that expires on an exact date](https://support.mindbodyonline.com/s/article/214741337-How-to-create-a-pricing-option-that-will-expire-on-an-exact-date?language=en_US)
- [Make changes to a client's pricing option](https://support.mindbodyonline.com/s/article/How-do-I-make-changes-to-a-client-s-pricing-option?language=en_US)
- [Why a pricing option discontinued itself](https://support.mindbodyonline.com/s/article/203276523-Why-did-a-pricing-option-discontinue-itself-automatically?language=en_US)
- [Why activation date cannot be edited at POS](https://support.mindbodyonline.com/s/article/210213308-Why-can-t-I-edit-the-activation-date-of-a-pricing-option-at-the-Retail-POS?language=en_US)
- [Offset activation dates for contracts](https://support.mindbodyonline.com/s/article/Offset-Activation?language=en_US)
- [Customers using an option before it begins](https://support.mindbodyonline.com/s/article/203281913-Why-can-customers-use-this-Pricing-Option-to-pay-for-sessions-before-it-is-set-to-begin?language=en_US)
- [General Setup & Options directory](../settings-navigation/203259783-General-setup-options-explained.md)
- [Client Account Details screen](../clients/215843418-Client-Account-Details-Screen-overview.md)
