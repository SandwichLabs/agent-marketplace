---
title: Scheduling increments (active business hours for services)
category: appointments
source: https://support.mindbodyonline.com/s/article/203253593-Scheduling-increments-Active-Appointment-Times-active-business-hours-for-services?language=en_US
source_updated: 2026-06-23
---
# Scheduling increments (active business hours for services)

Defines which clock times classes, appointments, courses and rooms can be scheduled/booked. The selected times populate start/end dropdowns across the site. Sometimes labeled Active Session Times or Active Appointment Times. If a time is missing from a dropdown or clients see no slots, check here first.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_times.asp (Scheduling Increments)
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_appt.asp (Appointment Options)
- Menu path: **Settings > Services > Scheduling Increments**; **Settings > Services > Appointment Options > Appointment System Policies**

## Steps
### Set increments
1. Open **Settings > Services > Scheduling Increments**.
2. Pick a view from the dropdown (top left); the entries are your navigation tabs, not individual services.
3. Tick boxes for the times (both start AND end times, e.g. 6:15am and 6:45am for a 6:15-6:45 class). Grid is hourly rows by 5-minute columns.
4. Click **Update**.

### Bold times
- Click a ticked (blue) box again to turn it gray = bold time (only effective if bold-time restriction is on in Appointment Options).

### Appointment schedule display/booking intervals
1. **Settings > Services > Appointment Options**, expand **Appointment System Policies**.
2. In Additional Settings choose **Block Size on First Load** (schedule row increments) and **Schedule Booking Snapping Interval** (booking interval).
3. Click **Update**.

## Settings & fields
- Room Schedule shows in the dropdown only if Resource Scheduling is enabled.
- Bold times: when restriction is enabled, clients can book only at bold times.
- Block Size / Snapping Interval change appearance only, not active times or staff availability.

## Gotchas
- Needs staff permissions **Active Session Times (Scheduling Increments) screen** and **Appointment Options screen**.
- This screen does NOT control staff availability (set separately).
- Unticked times are unavailable to both staff and clients; a slot only appears to clients if at least one staff member is available.
- Client booking times follow Client Views/Custom Views: increments come from the Custom View(s) the service category belongs to; multiple views combine their increments (union); with none set, the Appointments Default View is used. Consumer site shows an error "No available appointment times were found in your search range." if the selected tab has no increments.
- To force specific times for a service: give its category its own Custom View with its own increments, and remove it from other views; group services sharing the same times.
- Branded app: disable "Enable MB tabs for appointments" to prevent clients from picking a mismatched tab.
- Widget changes may take extra time to show after refreshing widget data.

## Related
- [Scheduling staff appointment availability](203254013-Appointments-Scheduling-staff-appointment-availability.md)
- [Appointment Options screen](203259913-Appointment-Options-screen.md)
- [Client View Settings / Tab Management](../online-booking/203259793-Tab-Management-screen.md)
- [Missing start/end times troubleshooting](https://support.mindbodyonline.com/s/article/203267853-Why-can-I-not-choose-a-start-time-and-end-time-when-scheduling-a-class-or-adding-appointment-availability-Scheduling-Increments-Active-Session-Times?language=en_US)
- [Restrict client appointments to bold times](https://support.mindbodyonline.com/s/article/205735258-Restrict-client-booked-appointments-to-bold-times?language=en_US)
- [Appointment booking troubleshooting](https://support.mindbodyonline.com/s/article/215813658-troubleshooting-appointment-booking-for-consumer-mode?language=en_US)
- [Class setup, scheduling and pricing](../classes-courses/203254153-Classes-setup-scheduling-and-pricing.md)
- [Edit navigation menu](../settings-navigation/How-to-edit-the-navigation-menu-on-my-site.md)
- [Appointment widget](https://support.mindbodyonline.com/s/article/Appointment-widget-branded-web-tools?language=en_US)
- [Branded app settings](https://support.mindbodyonline.com/s/article/204949317-How-do-I-change-the-App-Settings-MINDBODY-Engage?language=en_US)
