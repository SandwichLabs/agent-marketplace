---
title: How to set up your sales pipeline (Lead Management)
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/Setting-up-your-sales-pipeline?language=en_US
source_updated: 2026-09-15
---
# How to set up your sales pipeline (Lead Management)

Configure the Lead Management settings: automatic lead capture, AI/ML lead scoring, which purchases convert a lead to Won, pay-for-another conversion, and notifications.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/lead-management
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/main_retail.asp?fl=true&tabID=3 (Point of Sale)
- Menu path: **Marketing > Lead Management** > **Settings** (gear), or **Quick-Start Guide**.

## Steps
### Open settings
1. Go to Lead Management and click the **Settings** gear. Each criteria option has an on/off toggle; click **Save** after changes.

### Track Leads
1. Toggle **Track Leads**; Save. New leads land in the New Lead column and trigger an email notice.

### AI/ML-based Lead Score
1. Toggle it. Cards then show Likely to convert, May convert, or Not Likely to convert. Open a card and hover the insights blurb to see scoring factors.

### My Lead Conversion Criteria
1. Toggle it on, pick pricing options, contracts, or memberships from the dropdowns; click X beside an item to remove.

### Convert via client relationships (pay for another)
1. Point of Sale > select the paying client > **Pay for another client**.
2. Select the recipient (must have an assigned relationship with the payer).
3. Under **Add item**, add the service/product and complete the purchase.
4. The recipient's lead moves to Won; the Lead Management dashboard shows a pop-up on next visit. The payer's Purchases screen shows a symbol with the recipient's name on hover under "Payment Ref #".

### Notification Settings
1. Click **+Add another email** for each address to be told about new leads.
2. Under Staff Assignment Notifications toggle: email on lead assignment, SMS on lead assignment, email on follow-up task creation. Click **Save**.

## Settings & fields
- **Track Leads**: enabled by default; auto-adds a lead when a new profile is created (business or consumer site). A new client who buys at creation still counts as a lead. Disabled: no new leads can be added, existing ones retained.
- **Lead score inputs**: past contracts, first purchase amount, spending in last 3 months, days since last visit, visits in last 3 months, days since last purchase. Recomputed daily; only Trial Started and Trial Completed stages; default pipeline only; excludes gift card, service exchange, and account-adjustment purchases; counts only visits after a purchase.
- **Lead conversion criteria**: enabled by default but nothing is selected until you choose items. Default behavior is converting on any purchase only when criteria are not constraining; with criteria on, only selected items convert. Memberships granted by a pricing option must be listed; items in a selected contract require the contract itself.

## Gotchas
- Permissions: Sales Team Management > Ability to work the leads from Sales Pipeline; Sales Pipeline setting (needed to edit).
- Prospects created before Lead Management was on do not appear as leads; convert them manually.
- If conversion criteria are off or empty, no purchase moves a lead to Won; an intro offer with the trigger enabled moves it to Trial Started instead.
- Contracts chosen as conversion criteria are hidden from other stage-trigger dropdowns.
- Packages cannot be conversion criteria even if they contain a selected pricing option.
- A prospect who reaches Won has the prospect flag cleared on Client Info (not retroactive).
- Lead score is not recalculated until the next day after a card move.
- SMS notifications are unavailable in some countries; only email shows there.
- Package-dependent features.

## Related
- [Automated lead progression (default pipeline)](https://support.mindbodyonline.com/s/article/How-to-set-up-automated-lead-progression-on-the-Sales-Pipeline?language=en_US)
- [Triggers on the Configurable Sales Pipeline](https://support.mindbodyonline.com/s/article/How-to-set-up-triggers-on-the-Configurable-Sales-Pipeline?language=en_US)
- [Automated lead distribution](Automated-lead-distribution-Sales-Pipeline.md)
- [Managing leads](https://support.mindbodyonline.com/s/article/Managing-leads-in-the-Sales-Pipeline?language=en_US)
- [Sales pipeline dashboard overview](Sales-Pipeline-Dashboard.md)
- [Change an existing client into a lead](https://support.mindbodyonline.com/s/article/How-do-I-change-an-existing-client-into-a-lead-Sales-Pipeline-dashboard?language=en_US)
- [Assigning client relationships](../clients/203259383-Assigning-Client-Relationships.md)
- [Lead Management FAQ](Getting-started-with-Lead-Management-FAQ.md)
- [SMS requirements by country](https://support.mindbodyonline.com/s/article/Twilio-SMS-Compliance-for-Core-Products?language=en_US)
- [Utility messages overview](https://support.mindbodyonline.com/s/article/Utility-messages-overview-and-FAQ?language=en_US)
- [Sales Team Management permissions](https://support.mindbodyonline.com/s/article/Staff-Permissions-Sales-Team-Management?language=en_US)
- [Why isn't this feature available](../settings-navigation/Why-isn-t-this-feature-available.md)
