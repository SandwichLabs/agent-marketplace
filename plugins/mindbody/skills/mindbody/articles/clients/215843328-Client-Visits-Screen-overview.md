---
title: Client Visits screen
category: clients
source: https://support.mindbodyonline.com/s/article/215843328-Client-Visits-Screen-overview?language=en_US
source_updated: 2025-10-03
---
# Client Visits screen

Shows a client's past (and optionally future) visits with status, payment and who booked, plus login, appointment and cancellation views. Use it to check attendance, find who made a booking, or trace which pricing option paid.

## Where in Mindbody
- Menu path: **Find a client** > select client > **Visits** on the client management submenu.

## Steps
1. Open the client and click **Visits**.
2. Choose **Show All Dates** or **Select date range** (extend into the future to see booked visits).
3. Optional: narrow with the **All Visit Types** service-category filter.
4. Switch views with links above the date range: **Logins**, **Appointments**, **Cancellations**.
5. Click a class/event description to open its sign-in sheet, an appointment description to open it on the schedule, or a pricing option link to see everything it paid for.
6. Export with the XLS icon / **Export** > Download as CSV (bottom right).

## Settings & fields
Visits view columns: Date, Day, Time, Description, Teacher, Studio, Resource, Status, Pricing Options, Created by, Totals.
- **Status** values: Signed-in; Absent (missed, or booked today and not started, or past appointment not checked out); Completed (appointment checked out); Late Cancel (cancelled inside the window); Reserved (future); No-Show (past/same-day appointment with payment applied but not completed). If an appointment was marked Arrived on the schedule, Visits shows No-Show, Visits - Appointments shows Arrived, and the No-Show report omits it.
- **Pricing Options**: shows the paying option or "Unpaid (Service Category Name)"; an icon marks shared or other-client pricing options.
- **Created by**: username who booked, with timestamp; "From waitlist" for automatic waitlist adds; the staff name for manual waitlist adds; API integration name for ClassPass/Groupon and similar.
- Totals: Total visits counts Late Cancel and Absent; Total hours excludes them.
- Logins view: Name, Studio, Date/Time, Total Logins (consumer-site logins only).
- Appointments view: Date, Time, Teacher, Studio, Description, Type Purchased, Status, Booked online, Payment Ref#, Notes, totals.
- Cancellations view: Date/Time of cancellation, Conf #, Canceled by, Date, Time, Type, Studio, Teacher, Method (Late Cancel or Early Cancel), Total cancellations.
- **More** menu: set Visits as the default client landing screen; manage duplicate clients (Merge Duplicate Clients tool).

## Gotchas
- Default date range is configurable up to 60 months (General Setup & Options, Client Management); totals only cover the displayed range.
- Needed permissions: View client visit history, View client account/purchase history, View entire appointment schedule, Entry logs (Reports), Ability to view all clients.

## Related
- [Client lookup landing page](https://support.mindbodyonline.com/s/article/203259413-Client-lookup-landing-page?language=en_US)
- [Default date range for client screens](https://support.mindbodyonline.com/s/article/212830497-Can-I-set-Show-All-Dates-as-the-default-date-range-for-viewing-client-history?language=en_US)
- [Print a client's visit history](https://support.mindbodyonline.com/s/article/216308557-How-to-print-out-a-client-s-visit-history?language=en_US)
- [Client visit history for a year or longer](https://support.mindbodyonline.com/s/article/214630358-How-can-I-get-a-list-of-a-client-s-visit-history-for-the-past-year-or-longer?language=en_US)
- [Merge Duplicate Clients tool](203259603-Merge-Duplicate-Clients-tool.md)
- [Cancellations report](https://support.mindbodyonline.com/s/article/203256893-Cancellations-report?language=en_US)
- [Cancellation windows](../online-booking/203257723-How-do-I-set-up-cancellation-windows.md)
- [What counts as a no-show](https://support.mindbodyonline.com/s/article/206629617-What-Determines-If-An-Appointment-Is-Considered-A-No-Show?language=en_US)
- [Appointments missing from Visits](https://support.mindbodyonline.com/s/article/Why-can-t-I-see-all-of-the-clients-appointments-from-the-Visits-page?language=en_US)
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Client Account Details screen](215843418-Client-Account-Details-Screen-overview.md)
