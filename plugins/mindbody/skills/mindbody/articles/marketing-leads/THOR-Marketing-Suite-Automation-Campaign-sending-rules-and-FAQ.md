---
title: Automation and campaign sending rules (Marketing Suite)
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/THOR-Marketing-Suite-Automation-Campaign-sending-rules-and-FAQ?language=en_US
source_updated: 2026-09-11
---
# Automation and campaign sending rules (Marketing Suite)

Reference for the rules, delays, and limits that govern when Marketing Suite automations and campaigns actually send. Consult when designing an automation or diagnosing why a message did not go out.

## Where in Mindbody
- Menu path: **Marketing > Marketing Suite**. Delivery tracking: Text Message History report and Email History report (inside Marketing Suite).

## Settings & fields
- **Rule order**: automation/campaign rules, then priority rules, then global rules.
- **Automation send timing**: Mindbody locations send after each data sync, up to 4 times a day; Booker locations once daily.
- **Recipients** must be eligible, match the contact list criteria, and be subscribed to the chosen channel(s). The preview list shows possible, not guaranteed, recipients.
- **Unique lists**: each automation needs its own set of contact lists; reusing lists gives an error saying the lists are already used by another automation.
- **Delays**: same-type messages (email then email) need at least 1 day apart; "Wait 0 day(s)" is not allowed. Different types (email then text) cannot have a delay between them; put an email and a text in the same step to send both together (only clients subscribed to both receive them).
- **Text messages**: sent from a trackable phone number (2-way). Clients opt in to "News and promos" by texting SUBSCRIBE; opt out with NOOFFERS (text marketing only). Opt-out footer cannot be disabled and does not count toward the **136**-character limit. No merge tags; emojis and links OK. HTTP/HTTPS links auto-shorten to 21 characters (links over 136 characters cannot); clicks on them appear in Text Message History; "www" links are neither shortened nor tracked.
- **Automation priority**: when a client qualifies for several automations, only one sends per day, chosen in alphabetical order; the other can send the next day.
- **Text limits (global)**: 50 per minute and 900 per day per phone number; 30 per client per 30 days per number; Feedback & Reviews automations send up to 20 texts per location per day, with an email fallback. You are not notified on hitting limits. Follows TCPA and CTIA guidance.
- **Campaigns, single location**: multiple campaigns can go out the same day, so a client on several lists (or the same list twice) gets multiple emails.
- **Campaigns, multi-location (datashare)**: a contact gets only one promotional email per day across locations (from whichever location syncs first), whether campaigns are shared or not. To target one location use contact list filters (visited / booked appointment / purchased) with **most recently in this location**.
- **Campaign cap**: 200K emails per day per location, resetting at 12am local time.

## Gotchas
- Accelerate 2.0 or higher is needed for campaigns; Ultimate 2.0 for automations and text marketing. SMS is not available in all countries.
- Marketing Suite messages are separate from site auto emails and do not appear in site reports or contact logs.
- A multi-step automation mixing channels with a delay can stall if the client lacks one subscription.
- The Utility Messages add-on (France, Germany, Netherlands, Spain, Switzerland) automates SMS from system events.

## Related
- [Why a campaign or automation may not send to more clients](Why-didn-t-my-campaign-or-automation-get-sent-to-more-clients-Marketing-Suite.md)
- [Marketing Suite FAQ](https://support.mindbodyonline.com/s/article/What-is-the-Marketing-suite-screen-tab?language=en_US)
- [Send times and limits](https://support.mindbodyonline.com/s/article/When-are-emails-and-texts-sent-out-Marketing-Suite?language=en_US)
- [Videos in campaigns and automations](https://support.mindbodyonline.com/s/article/Can-I-place-videos-in-campaigns-or-automations-Marketing-Suite?language=en_US)
- [Copy campaigns, automations, smart lists](https://support.mindbodyonline.com/s/article/Can-I-copy-a-campaign-Marketing-Suite?language=en_US)
- [Creating automations](Creating-automations-Frederick.md)
- [Trackable phone number](https://support.mindbodyonline.com/s/article/What-is-a-trackable-phone-number-Frederick?language=en_US)
- [Text Message History report](https://support.mindbodyonline.com/s/article/Text-Message-History-report-Marketing-Suite?language=en_US)
- [Email History report](https://support.mindbodyonline.com/s/article/Email-History-report?language=en_US)
- [Personalize with merge tags](https://support.mindbodyonline.com/s/article/How-do-I-personalize-my-campaign-and-automation-emails?language=en_US)
- [Multi-location management guide](https://support.mindbodyonline.com/s/article/How-do-I-switch-locations-Frederick?language=en_US)
- [SMS requirements by country](https://support.mindbodyonline.com/s/article/Twilio-SMS-Compliance-for-Core-Products?language=en_US)
- [Utility messages overview](https://support.mindbodyonline.com/s/article/Utility-messages-overview-and-FAQ?language=en_US)
