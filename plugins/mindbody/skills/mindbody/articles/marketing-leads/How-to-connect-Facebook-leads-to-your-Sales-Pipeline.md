---
title: How to track Meta (Facebook and Instagram) leads in the sales pipeline (Lead Management)
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/How-to-connect-Facebook-leads-to-your-Sales-Pipeline?language=en_US
source_updated: 2026-09-29
---
# How to track Meta (Facebook and Instagram) leads in the sales pipeline (Lead Management)

Connect a studio's Meta account so Facebook/Instagram Instant-form leads land in the Mindbody Sales Pipeline. Three parts: build the form in Ads Manager, connect in Mindbody, grant CRM lead access in Meta.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/lead-management
- Menu path: **Marketing > Lead Management** > Settings gear > **Third Party Lead Channels**
- Meta side: Facebook Ads Manager; Facebook Business settings > **Integrations > Leads Access**

## Steps
### 1. Create the lead form (Facebook Ads Manager)
1. Campaigns screen > **+ Create** (or open an existing campaign); objective **Leads**; choose **Manual leads campaign** > **Continue**.
2. Name campaign and ad set; Conversion Location = **Instant forms**; set **Budget & Schedule**; name the ad; optionally pick an Instagram account in **Identity**.
3. In Destination click **Create Form**. Name it clearly (the form name shows on the lead card).
4. Under Questions > **Prefill questions** add First name, Last name, Email, Phone number. Other fields do not flow into Mindbody.
5. Optional: Privacy Policy custom disclaimer and consent checkboxes; form language under **Settings > Form Configuration**.
6. **Create form**, then **Publish**. Meta review can take up to 24 hours.

### 2. Connect Mindbody to Facebook
1. **Marketing > Lead Management**, open the pipeline, click the **Settings gear**.
2. In **Third Party Lead Channels** click **Connect**, sign in to Facebook, pick the businesses/pages, review permissions, **Save**.

### 3. Assign lead access
1. Facebook Business settings > **Integrations > Leads Access** > **CRMs** tab > **Assign CRMs**.
2. Select **MINDBODY - Lead Management** > **Assign**.

### Add pages / choose forms
1. Settings gear > Third Party Lead Channels > **+ Add page** > **Edit previous settings**; pick business and pages; **Save**.
2. Default is **All published forms**; click it, choose **Select specific form**, tick forms, **Save**. To go back: form name > **Back** > **All published forms**.

### Disconnect a page
1. Settings gear > Third Party Lead Channels > click **X** by the page name.

## Settings & fields
Form field names must be the system names regardless of display language, with no trailing spaces: first_name, last_name, full_name, phone_number, email. Consent fields: transactional_email, transactional_text, transactional_email_and_text, promotional_email, promotional_text, promotional_email_and_text, transactional_and_promotional_email, transactional_and_promotional_text, transactional_and_promotional_email_and_text. Marketing consent maps to the News and Promo subscription preference.

## Gotchas
- Form needs first name, last name, email, phone. A full_name of one word leaves last name empty and the lead is not created. Do not rename default field names or leads fail.
- Leads arrive about a minute late; refresh. Channel is "Facebook Lead Ad" (card shows form name) or "Instagram".
- Changing Facebook password or de-authorizing the app breaks the connection; a banner ("There's an error linking Facebook page(s) or account... Please reconnect.") appears and the page shows red in Settings. Banner reappears on refresh until fixed.
- A page already connected to another studio cannot be linked; if another studio holds a form-level connection you cannot revert to all forms until it is removed there. Archived forms mark the page inactive; no forms shows "No forms found."
- Deleting the app from the Meta CRM tab or not assigning it stops lead delivery.
- Disable third-party ad automation (e.g. Leadsbridge); it can break setup.
- Ad spend is with Meta, not Mindbody. Mindbody stores only Page ID, User ID and access token. Branded web widgets on Facebook or a "Book Now" button are alternatives without ads.
- Package dependent.

## Related
- [Create, manage, and delete leads](https://support.mindbodyonline.com/s/article/Managing-leads-in-the-Sales-Pipeline?language=en_US)
- [Automated lead distribution](Automated-lead-distribution-Sales-Pipeline.md)
- [Change existing clients into leads](https://support.mindbodyonline.com/s/article/How-do-I-change-an-existing-client-into-a-lead-Sales-Pipeline-dashboard?language=en_US)
- [Automated lead channel mapping](https://support.mindbodyonline.com/s/article/Automated-lead-channel-mapping-on-the-Sales-Pipeline-overview?language=en_US)
- [Lead channels overview](https://support.mindbodyonline.com/s/article/Lead-Channels-Sales-Pipeline?language=en_US)
- [Consent options for communication preferences](https://support.mindbodyonline.com/s/article/Consent-options-for-Communication-Preferences-Sales-Pipeline?language=en_US)
- [Branded web widgets on Facebook FAQ](https://support.mindbodyonline.com/s/article/How-to-install-and-customize-your-HealCode-widgets-on-Facebook?language=en_US)
- [Bookings through the Facebook app FAQ](https://support.mindbodyonline.com/s/article/Manage-bookings-on-Facebook-FAQ?language=en_US)
- [Best practices for Facebook (branded web tools)](https://support.mindbodyonline.com/s/article/7-Best-practices-for-Facebook-branded-web-tools-formerly-HealCodeS?language=en_US)
