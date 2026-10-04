---
workflow: Set staff availability and scheduling increments
safety: 🟡 Changes data
---
# Set staff availability and scheduling increments

Give a staff member bookable appointment hours, change them, add unavailability (lunch, vacation), or fix missing time options. Typical phrasings: "Marcus works Tue/Thu 9-5 starting Monday", "block Lisa out next week", "I can't book 15-minute slots".

## Ask the person for
- Staff member, location, service categories they offer.
- Days, start/end times, and start date; ongoing or ending on a date.
- Available vs unavailable (and reason, if unavailable).
- For increments: which view/service and which times are missing.

## Read first
- [Scheduling staff appointment availability](../../articles/appointments/203254013-Appointments-Scheduling-staff-appointment-availability.md)
- [Edit appointment availability](../../articles/appointments/203259013-Appointments-Changing-a-staff-member-s-availability.md)
- [Scheduling increments](../../articles/appointments/203253593-Scheduling-increments-Active-Appointment-Times-active-business-hours-for-services.md)
- [Let staff edit only their own availability](../../articles/appointments/203270073-How-do-I-allow-my-staff-to-edit-their-OWN-appointment-availability-only.md)

## Steps
1. **Check the staff member is an instructor** — navigate to https://clients.mindbodyonline.com/app/staff, click the person, and confirm **Instructor/Therapist (for appointments)** is ticked under Settings. If not, tick it and **Save** (tell the person).
2. **Open availability** — on **Staff**, click the three-dot menu beside the name > **Manage Schedules** (or open the profile > **Appointment Availability**).
3. **Add availability** — click **+ Add New Schedule**. Set **Show staff as** to **Available**, answer "What services does [staff] offer at this time?", choose **Studio**, **Date Range** (**Ongoing** or **Custom**; Custom defaults to two weeks out), **Days**, **Time**, and **Privacy** (default **Allow clients to see schedule**). Click **Add**, or **Save and Add Next**.
4. **Add unavailability** — same form, **Show staff as: Unavailable**, with a **Reason** and dates. Note it applies to all locations on multi-location sites. Over an existing appointment you get a Scheduling Conflict warning; the appointment stays.
5. **Change hours going forward** — click the existing block, set its end date to the day before the change, **Save**; then create a new schedule from the change date. For edits to a single block, click it, change dropdowns, **Save**; choose one day or multiple days if prompted.
6. **Fix a missing time (increments)** — navigate to https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_times.asp (**Settings > Services > Scheduling Increments**). Pick the view top left, tick both start and end times needed, click **Update**. This changes which times exist for everyone on that view; state that before saving.
7. **Schedule display only** — in **Settings > Services > Appointment Options > Appointment System Policies** you may change **Block Size on First Load** and **Schedule Booking Snapping Interval**, then **Update**. These change appearance only.
8. 🟡 Deleting a block (trash icon) is destructive; only do it when asked, and say booked appointments will stay but need moving.

## Verify
- Open https://clients.mindbodyonline.com/app/business/mainappointments/index, pick the staff member's **Week** view, and screenshot that the expected blocks appear.
- For increments, confirm the time now appears in the booking sidebar dropdown.

## If it goes wrong
- "This schedule conflicts with another existing schedule": an ongoing schedule or a class the person teaches overlaps; end it the day before or work around it.
- "Please input a valid date": switch Ongoing to Custom with a near end date.
- Staff member missing from the schedule: no availability left; they reappear after availability is added.
- Needs **Staff member availability** permission; do not edit permissions yourself.
- Service category absent from the form: it must be on a consumer-site view (tab).
- Bi-weekly patterns are not direct; add every week then unavailability for skipped weeks.

## Variations
- Staff edit only their own availability: permission-group change in [that article](../../articles/appointments/203270073-How-do-I-allow-my-staff-to-edit-their-OWN-appointment-availability-only.md) (affects the whole group; ask first).
- Quick edit from the Appointment Schedule: click an empty slot and choose edit day, weekly schedule or unavailable.
