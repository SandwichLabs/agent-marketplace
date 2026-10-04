---
title: How to set up and manage client alerts
category: clients
source: https://support.mindbodyonline.com/s/article/203259733-Client-alerts?language=en_US
source_updated: 2026-09-24
---
# How to set up and manage client alerts

Client alerts are pop-ups shown when staff open a client (or when clients use the consumer site) to flag account issues such as failed autopays, missing waivers or low sessions. They do not change site functionality.

## Where in Mindbody
- General Setup & Options: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_setup.asp (Settings > General > General Setup and Options)
- Client Alerts: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_clt_alerts.asp (Settings > Clients > Client Alerts)

## Steps
### Turn the feature on
1. Settings > General Setup and Options > expand **Client Management**.
2. Tick **Client Alerting**, click **Update**.

### Configure an alert
1. Settings > Clients > Client Alerts.
2. Pick an alert type from the dropdown.
3. In **Enable alerts**, select the screens where it should appear (multi-select; varies by alert and by business vs consumer site).
4. Set the alert options, then **Update**.

## Settings & fields
- **Erase Alert button** (Staff and Yellow alerts): lets staff clear the alert from the pop-up.
- **Force Resolution** (Contract Confirmation on consumer site; Missing Billing Information on both): removes Ignore. If off, staff can tick "Do not alert me for this client again".
- **Reason to Ignore field** (Staff/Yellow): ignored alerts return at next login.
- **Reason to Sign In field** (Account Balance Threshold, Arrivals in Threshold): staff pick Reject or Sign In and give a reason.
- **Write contact log**: every alert can log who responded and what they chose (view in client's Contact Logs by Alert Type).
- **Threshold**: days, sessions, hours, months or amount, depending on alert.

Alert types (location in parentheses: B = business site, C = consumer site):
- Account Balance Threshold (B, C), ACH Failed / Account Credit Notification (B, C), Arrivals in Threshold (B), Autopay Failed (B, C; saves card entered when resubmitting from the pop-up), Client Status (B, C; shows Declined/Active/Expired/Suspended/Terminated), Contract Confirmation (consumer only in practice; earliest contract first, one at a time; re-prompts on auto-renew), Credit Card Expiration (B, C; months threshold), Failed Auto Email (B, C), Followup Due (B), Liability Waiver (B, C), Low Session Alert (B, C), Missing Billing Information (B, C, branded app, branded web cart v1), Missing Required Fields (B, C), No Arrivals in Threshold (B), No Current Membership Or Pricing Option (B), No Visits in Threshold (B), Scheduling Suspended (B), Staff (Red) Alert (B), Unpaid Sessions Alert (B), Waitlist Confirmed (B, C), Yellow Alert (B).

## Gotchas
- Staff need General Setup & Options (Settings) and Set up client alerts (Clients) permissions.
- Not supported in the Mindbody app or web; the branded app only supports Missing Billing Information with Force Resolution - Consumer Mode.
- Low Session Alert threshold is set on the pricing option (must be above zero) and activates 24 hours after saving.
- Followup Due excludes today (threshold 5 on May 23 fires May 28).
- Unpaid Sessions Alert ignores clients whose only unpaid bookings are in the future.
- Liability Waiver: selecting all screens on the consumer site forces acceptance before booking or buying.
- Dashboard business alerts are different features (failed autopays, expiring cards, expiring intro offers).

## Related
- [Client alerts FAQ](https://support.mindbodyonline.com/s/article/Client-alerts-FAQ?language=en_US)
- [Screen locations for client alerts](https://support.mindbodyonline.com/s/article/227314068-What-screen-locations-can-the-Client-Alerts-be-displayed-on?language=en_US)
- [Yellow and red alerts on the client profile](https://support.mindbodyonline.com/s/article/205650228-What-do-the-yellow-and-red-alerts-on-the-client-profile-mean?language=en_US)
- [Liability waiver](203259873-Liability-waiver.md)
- [Client required fields](202988236-Client-required-fields.md)
- [Client Indexes](203259183-Client-Indexes.md)
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Client Contact Logs screen](https://support.mindbodyonline.com/s/article/215843268-Client-Contact-Logs-Screen-overview?language=en_US)
- [Scheduling suspensions after failed autopay](https://support.mindbodyonline.com/s/article/203276553-How-can-I-stop-a-client-from-booking-if-their-autopay-has-failed-Scheduling-Suspensions?language=en_US)
- [Pricing Options on the Settings screen](../pricing-memberships/213024177-Pricing-Options-screen.md)
- [Failed autopays dashboard alert](https://support.mindbodyonline.com/s/article/What-does-the-Alerts-on-my-dashboard-mean?language=en_US)
