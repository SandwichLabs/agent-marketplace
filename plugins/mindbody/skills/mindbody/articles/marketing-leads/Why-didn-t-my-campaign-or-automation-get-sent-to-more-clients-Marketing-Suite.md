---
title: Reasons a campaign or automation may not send to more clients (Marketing Suite)
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/Why-didn-t-my-campaign-or-automation-get-sent-to-more-clients-Marketing-Suite?language=en_US
source_updated: 2026-09-25
---
# Reasons a campaign or automation may not send to more clients (Marketing Suite)

Troubleshooting checklist for when fewer clients receive a campaign or automation than expected. Work through the causes below.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/marketingsuite (and /marketingsuite/index)
- Menu path: **Marketing > Marketing Suite**; Contact Lists > **Manage**; Discount Settings via **Manage** beside Feedback and reviews or Referrals (Booker: **Marketing > Open more tools**).

## Steps
### Check true number of subscribed contacts
1. Marketing Suite > **Manage** beside Contact Lists (Booker: **Marketing > Contact Lists**).
2. In System Lists, open **Marketing Email Subscribed**.

### Check who an automation reaches
1. Open the automation, **Settings > Who it's sent to**, click the linked contact list to see eligibility and email/text subscription status.

### Check the Require a Recent Visit setting
1. Open Discount Settings and review **Require a Recent Visit** (when on, nobody who has not visited in two years gets messages).

## Gotchas (likely causes)
- **Opt-in**: only clients opted in to marketing email/"News and promos" are messaged; most opt out by default. A client may be opted in within Marketing Suite yet lack the News and Promos checkbox on the site profile.
- **Duplicate emails**: if several profiles share an email, only the first profile synced is linked to the Marketing Suite contact.
- **Dynamic eligibility**: contacts leave a list the moment they stop qualifying; in a drip, delayed messages are dropped if the client is removed after message one.
- **Send to / Do not send to**: ALL-lists means the client must be on every list; ANY-lists means at least one; any Do-not-send list excludes them.
- **Enroll (#) clients who already meet these criteria**: if cleared, only contacts added later receive it; existing qualifiers will not get it again unless they leave and re-qualify.
- **Count mismatch** vs list size: unsubscribed, already received a Smart Marketing/campaign message that day, or invalid email. Check the Performance report and the Browse Contacts screen.
- **One automation message per calendar day** per client. A campaign can follow an automation the same day, but not the reverse; multiple campaigns per day are fine.
- **Timing**: campaigns send at the chosen time (15-minute increments) in the Business Profile time zone; automations and Smart Marketing cannot be scheduled. Mindbody syncs about 4x daily (changes show within 2-6 hours); Booker once daily; a new automation may take up to 24 hours.
- **Multi-location (datashare)**: one promotional email per client per day across locations.
- **Smart Marketing** sends only to a targeted subset and not again for a couple of weeks.
- **Inactive/deleted pricing option** attached as an offer stops the automation and its SMS, and blocks reactivation until fixed.
- **Run Campaigns** toggled off on the Marketing Suite Dashboard stops automations and Smart Marketing (scheduled campaigns still go). If absent, Smart Marketing is not on.
- **Footer and unsubscribe** must remain in an automation or it cannot be tested or sent.
- **Canada**: campaigns go only to clients with a visit in the past 24 months (anti-spam law), even if All Contacts is chosen.
- Global limits: 50 texts/min and 900/day per number, 30 per contact per 30 days, 200,000 campaign emails per day per location (resets 12am local).
- Not applicable to Attentive SMS & Email.

## Related
- [Automation and campaign sending rules](THOR-Marketing-Suite-Automation-Campaign-sending-rules-and-FAQ.md)
- [Reasons clients may not appear](https://support.mindbodyonline.com/s/article/Why-aren-t-all-of-my-email-addresses-syncing-to-the-Marketing-Suite?language=en_US)
- [Manually subscribe and unsubscribe clients](https://support.mindbodyonline.com/s/article/How-to-Manually-Subscribe-and-Unsubscribe-Customers-in-Marketing-Suite?language=en_US)
- [Marketing Suite FAQ](https://support.mindbodyonline.com/s/article/What-is-the-Marketing-suite-screen-tab?language=en_US)
- [Why an auto email may not send](https://support.mindbodyonline.com/s/article/What-would-cause-some-auto-emails-to-send-while-others-do-not?language=en_US)
- [Text message marketing](https://support.mindbodyonline.com/s/article/Enabling-text-message-opt-ins-Frederick?language=en_US)
- [Discount settings](https://support.mindbodyonline.com/s/article/Adjusting-your-discount-settings-Frederick?language=en_US)
- [Creating automations](Creating-automations-Frederick.md)
- [Performance reports](Automation-reporting-Marketing-Suite.md)
- [Browse Contacts screen](https://support.mindbodyonline.com/s/article/Browse-Contacts-screen-Marketing-Suite?language=en_US)
- [Smart Marketing overview](https://support.mindbodyonline.com/s/article/Smart-Marketing-Marketing-Suite?language=en_US)
- [Marketing Suite Dashboard](https://support.mindbodyonline.com/s/article/Understanding-your-Dashboard-Frederick?language=en_US)
- [Business Profile](https://support.mindbodyonline.com/s/article/Filling-out-your-business-profile-Frederick?language=en_US)
- [Multi-location guide](https://support.mindbodyonline.com/s/article/How-do-I-switch-locations-Frederick?language=en_US)
- [Canada's Anti-Spam Legislation](https://support.mindbodyonline.com/s/article/Canada-s-Anti-Spam-Legislation?language=en_US)
- [Anti-spam law compliance](https://support.mindbodyonline.com/s/article/Does-the-Marketing-Suite-comply-with-anti-spam-laws?language=en_US)
- [Adding offers to campaigns](https://support.mindbodyonline.com/s/article/Adding-offers-to-campaigns?language=en_US)
- [Why isn't this feature available](../settings-navigation/Why-isn-t-this-feature-available.md)
