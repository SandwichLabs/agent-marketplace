---
title: Staff Permissions - Appointments
category: staff
source: https://support.mindbodyonline.com/s/article/Staff-Permissions-Appointment-Permissions?language=en_US
source_updated: 2025-10-06
---
# Staff Permissions - Appointments

Reference for the Appointments checkboxes in a permission group: what each allows on the Appointment Schedule and which other permissions must also be enabled. Use it to diagnose why a staff login cannot view, book, change, cancel or check out appointments.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_staff.asp
- Menu path: **Settings > Staff > Staff Permissions**, then choose the permission group.

## Settings & fields
(Prereqs shown after "needs"; "View Appointment Schedule" means View entire appointment schedule.)
- **View entire appointment schedule**: see all clients/appointments/staff on the Appointment Schedule. Does not open appointment details. No prereqs.
- **View own info/appointment schedule**: access own schedule, Schedule at a Glance report, other appointment displays. The Settings permission "Staff member availability" overrides it.
- **Edit own info/appointment schedule**: edit own schedule, book own future appointments, add/edit unavailability (Staff > Appointment Setup). Needs View own info.
- **View appointment details**: open an individual appointment. Needs either view-schedule permission.
- **Manage appointment requests**: accept/deny online booking requests (envelope icon in the schedule sidebar). Needs View entire schedule.
- **Book appointments for all staff**: single/recurring bookings for other staff. Needs View entire schedule and Ability to view all clients.
- **Book appointments in the past**: needs Book for all staff, View entire schedule, view all clients.
- **Modify appointments**: change type, instructor, client, start time, confirmed/arrived status, formula notes. Needs View entire schedule, View appointment details, view all clients.
- **Use any appointment type as add-on**, **Override length of scheduled appointments**, **Apply payment**: each needs View entire schedule, View appointment details, Modify appointments, view all clients.
- **Edit default appointment lengths**: Services & Products appointment type screen and Classic Setup > Appointment types. Needs Session Type/Class Type.
- **Edit appointment length per staff** and **Edit appointment prep and finish times**: Staff Appointment Setup (prep/finish also the Edit appointment type screen). Both need Staff Pay Rates.
- **Cancel appointments**: also lets staff manage the branded mobile app. Needs a view-schedule permission plus View appointment details, Modify appointments, view all clients; cancelling after start time also needs Override Cancellation Policy.
- **Apply payment**: charges a client without checkout, e.g. a no-show or late cancel.
- **Check out appointments**: collect payment and mark present. Needs a view-schedule permission plus View appointment details, Modify appointments, Complete sales transactions at POS, view all clients.
- **Override appointment type rules**: adds an "Override Appointment (Session) Type Rules" checkbox on Modify Appointment so any pricing option in the service category can pay. Only for sites using appointment types; prereqs as Modify.
- **Customize appointment schedule colors**: color key by status, service category or appointment type, plus available-time, line and background colors (sidebar color section). No prereqs.
- **View Progress/SOAP Notes**: via schedule action menu or client Info > Progress/SOAP Notes History. No prereqs.
- **Add/Edit Progress/SOAP Notes**: needs View Progress/SOAP Notes.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first: granting Apply payment, Check out, or Cancel appointments lets staff charge cards or cancel bookings.
- Nearly all booking/modify permissions silently fail without Ability to view all clients.
- Features depend on software package.

## Related
- [Staff Permissions - Settings](Staff-Permissions-Settings.md)
- [Staff Permissions - Clients](Staff-Permissions-Client-Permissions.md)
- [Staff Permissions - Analytics](https://support.mindbodyonline.com/s/article/Staff-Permissions-Analytics?language=en_US)
- [Staff Permissions - Reports](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reports?language=en_US)
- [Staff Permissions - Classes & Courses](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reservation-Permissions?language=en_US)
- [Staff permissions explained](203253743-Staff-permissions-explained.md)
- [Appointment Schedule screen overview](../appointments/203258883-Appointments-Appointment-schedule.md)
- [Appointment Checkout options and features](../appointments/Appointment-Checkout.md)
- [Appointments screen overview](../appointments/203254043-Appointments-Appointment-types.md)
