---
title: New consumer cart v2 and checkout experience (branded web tools)
category: online-booking
source: https://support.mindbodyonline.com/s/article/Consumer-cart-v2-branded-web-tools?language=en_US
source_updated: 2026-09-11
---
# New consumer cart v2 and checkout experience (branded web tools)

How the v2 checkout behaves for bookings made through the Appointment widget v2 and Schedule widget v2, plus Pricing widget and Buy Now links. Explains which Mindbody settings pick the booking/payment workflow.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_appt.asp (Appointment Options)
- Menu path: **Settings > Services > Appointment Options**; **Settings > General > General Setup & Options > Online Store Settings**; Class and Course Options (unpaid scheduling)

## Requirements (automatic upgrade)
- Appointment widget v2 (appointments) and/or Schedule widget v2 (classes).
- **Online Retail Store** enabled in Online Store Settings.
- For book-now-pay-now classes: at least one eligible pricing option sellable online, or checkout can fail.
- Only services booked through v2 widgets use cart v2.

## Settings & fields
### Appointment workflow (Appointment Options)
- **Book now, pay later**: Allow Client Booked Appointments checked, Require Client Payment for Booked Appointments unchecked.
- **Request to book**: both unchecked; business reviews and confirms.
- **Book now, pay now**: both checked.
- Click **Update** to save.
- Multi-service booking works in any workflow: staff/add-ons/time set per service; double booking same staff and time is blocked; removing a service removes its add-ons and any pricing option no longer used; contracts cannot be bought in multi-service flow (adding a contract hides Add another service). Eligible pricing options apply automatically; if payment is required and none exist, the client is prompted to buy one.

### Class workflow
- **Pay later**: set Client Unpaid Scheduling Restrictions (Class and Course Options) and unpaid signup settings on the class (Edit Scheduled Class/Event); memberships can be opted in. A card is requested only when payment, late-cancel or no-show fees apply.
- **Pay now**: unpaid online signups off for the class, or the client fails the unpaid rules. $0 class with no fees: no card requested.
- Supports pricing options, intro offers, passes, packages, contracts, promo/gift cards, waivers, cancellation policy, cross-regional booking, Pick-a-Spot, family accounts, waitlists.

### Other features
- Subscriptions: transactional opt-ins covered by privacy policy; marketing opt-in (email/text at confirm, SMS or WhatsApp post-booking) shown only to clients not already subscribed.
- **Pricing widget**: separate pricing page; sells pricing options, contracts, gift cards; can replace or complement Buy Now links.
- **Buy Now links**: existing links route to cart v2 automatically, open checkout in a pop-up; passes show service notes/dates/payment methods; contracts show terms, signature, promo codes, pre-sale (over 96 weeks is shown as month-to-month); gift cards take recipient/sender, image, send date (default next day).

## Gotchas
- Not supported: packages via Buy Now, course (enrollment) booking, multi-class/course bookings and add-ons, client alerts at class checkout (use late-cancel/no-show fees to capture a card), "thank you" redirect for class bookings (use GA4 and Meta Pixel), family purchasing via Buy Now, multi-item purchase, default Registration widget settings (new accounts enter email, names, password, country, email opt-in; first-time existing sign-ins are asked for gender, birthdate, address, plus any required fields).
- Clients can add to cart before login but must log in to book; ineligible clients (e.g. scheduling suspension) see an error after login.
- Cancellation policy text comes from General Setup & Options or the No-Show/Late Cancel Fees screen.
- Estimated appointment cost shown is the lowest available price.
- Features depend on software package; Support cannot edit website code.

## Related
- [New Schedule widget v2](New-Schedule-Widget-setup-and-options-branded-web-tools.md)
- [New Appointment widget v2](https://support.mindbodyonline.com/s/article/Appointment-widget-branded-web-tools?language=en_US)
- [Pricing widget setup and options](https://support.mindbodyonline.com/s/article/Pricing-widget-setup-and-options-branded-web-widgets?language=en_US)
- [Links and buttons in branded web tools FAQ](https://support.mindbodyonline.com/s/article/Creating-links-with-branded-web-tools?language=en_US)
- [Sell contracts](https://support.mindbodyonline.com/s/article/Can-I-sell-contracts-through-branded-web-tools?language=en_US)
- [Consumer cart errors](https://support.mindbodyonline.com/s/article/Consumer-Cart-is-not-properly-loading-branded-web-tools-formerly-HealCode?language=en_US)
- [Using the consumer cart as a client](https://support.mindbodyonline.com/s/article/Using-the-consumer-cart-as-a-client-branded-web-tools-formerly-HealCode?language=en_US)
- [Automate No-Show/Late Cancel Fees](How-to-automate-No-Show-and-Late-Cancel-Fees.md)
- [Appointment Options screen](../appointments/203259913-Appointment-Options-screen.md)
- [Class and Course Options screen](../classes-courses/203259633-Class-enrollment-options-screen.md)
- [Branded web tools FAQ](https://support.mindbodyonline.com/s/article/Frequently-asked-questions-about-widgets?language=en_US)
