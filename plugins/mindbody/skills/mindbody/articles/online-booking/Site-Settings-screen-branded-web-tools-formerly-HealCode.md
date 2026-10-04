---
title: Site Settings screen (branded web tools)
category: online-booking
source: https://support.mindbodyonline.com/s/article/Site-Settings-screen-branded-web-tools-formerly-HealCode?language=en_US
source_updated: 2026-01-28
---
# Site Settings screen (branded web tools)

The site-wide options in the Branded Web Manager that affect all widgets: branding colors, default registration widget, locations, currency/language, booking and payment behavior, tracking IDs, hotwords, MailChimp. Needed when widgets show stale data, send clients to the wrong checkout, or need tracking.

## Where in Mindbody
- Direct link: https://brandedweb.mindbodyonline.com/users/sign_in
- Menu path: Branded Web Manager > **Site Settings** (top menu). Requires a Branded Web Manager user account.

## Settings & fields
- **Refresh all Mindbody data**: manual sync of Mindbody site data into the widgets; use after changes in the business software.
- **Who powers your website?**: pick the website builder (WordPress, Squarespace, Weebly...); "Custom/other" if not listed.
- **Branding**: Primary Color (buttons), Secondary Color (links), Widget background color (only the newest Schedule widget on new widgets). Hex or color box.
- **Account Registration**: choose the default Registration widget used when clients create an account through the consumer cart.
- **Locations**: enable/disable locations; a disabled one disappears from widget creation/editing.
- **Region**: currency symbol and default language (applies to consumer cart/widgets).
- **Users**: the owner account can add logins so staff can create/edit/delete widgets.
- **Booking and E-Commerce**:
  - **Enable Booking**: on = clients book in widgets; off = redirected to the Mindbody consumer site. Must be on for Post-Booking Redirect, analytics and Facebook settings. Honored by Schedule widget v2.
  - **Post-Booking Redirect**: thank-you page on the studio's site after booking/purchase (usable for Google Analytics tracking).
  - **Google analytic number**: legacy Universal Analytics IDs no longer work (unsupported since July 1, 2023); migrate to GA4.
  - **GA4 Measurement ID**: enter the GA4 ID.
  - **Facebook Pixel ID**: Meta Pixel for the cart.
  - **Enable Payments Through Widgets**: off = payments completed in the Mindbody online store.
  - **Mindbody Settings**: read-only mirror of whether billing info is required and whether appointments can be booked or requested; managed in Mindbody, refresh to update.
- **Hotwords**: renamed terms from Words and Phrases (e.g. instructor to teacher); click Refresh all Mindbody data to pull them. Only V1 widgets use hotwords; V2 widgets do not.
- **MailChimp**: Prospect and Registration widgets add signups to MailChimp once configured; **Get Lists from MailChimp** refreshes lists, **Disconnect MailChimp** removes the integration.

## Gotchas
- Features depend on software package.
- Changing Enable Booking or Enable Payments reroutes clients to the consumer site; confirm with the user before toggling on a live site.

## Related
- [How to set up branded web tools](Intro-to-branded-web-tools.md)
- [Branded web tools FAQ](https://support.mindbodyonline.com/s/article/Frequently-asked-questions-about-widgets?language=en_US)
- [Best practices (branded web widgets)](https://support.mindbodyonline.com/s/article/Best-practices-for-widgets-branded-web-tools-formerly-HealCode?language=en_US)
- [How to create a new widget](How-to-create-a-new-widget.md)
- [How to add widgets to your website](https://support.mindbodyonline.com/s/article/How-to-put-branded-web-tool-widgets-on-your-site?language=en_US)
- [Manage user logins](https://support.mindbodyonline.com/s/article/Can-I-add-staff-member-logins-to-my-branded-web-tools-account?language=en_US)
- [Missing or outdated widget information](https://support.mindbodyonline.com/s/article/Missing-info-and-how-updating-works-for-widgets-branded-web-tools?language=en_US)
- [Consumer cart overview](https://support.mindbodyonline.com/s/article/What-is-the-Consumer-Cart-branded-web-tools-formerly-HealCode?language=en_US)
- [Consumer cart v2](Consumer-cart-v2-branded-web-tools.md)
- [Words and Phrases screen](https://support.mindbodyonline.com/s/article/203259813-Words-and-Phrases-screen?language=en_US)
- [Sites and locations FAQ](https://support.mindbodyonline.com/s/article/How-do-I-add-a-new-location-branded-web-tools?language=en_US)
