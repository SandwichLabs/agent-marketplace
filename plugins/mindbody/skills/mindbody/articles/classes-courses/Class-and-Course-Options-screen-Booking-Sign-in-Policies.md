---
title: Class and Course Options screen: Booking & Sign-in Policies
category: classes-courses
source: https://support.mindbodyonline.com/s/article/Class-and-Course-Options-screen-Booking-Sign-in-Policies?language=en_US
source_updated: 2026-09-21
---
# Class and Course Options screen: Booking & Sign-in Policies

Reference for every setting in the Booking & Sign-in Policies section of Class and Course Options: unpaid booking rules, schedule/cancellation windows, waitlists, sign-in behavior, no-show handling, and sign-in screen display. Look here when class booking or check-in behaves unexpectedly.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_res.asp
- Menu path: **Settings > Services > Class and Course Options > Booking & Sign-in Policies**

## Steps
1. Open Class and Course Options, expand **Booking & Sign-in Policies**.
2. Change settings, then click **Update** (unsaved changes are lost).
(Tip: browser find on the setting name expands the matching section.)

## Settings & fields
**Scheduling restrictions**
- **Client Unpaid Scheduling Restrictions**: who may book unpaid when a class allows unpaid online signups: Allow All Clients / Members Only / Clients with AutoPays Only / Members or Clients with AutoPays Only. Member options need the memberships flagged in Membership settings. AutoPay options reveal "Limit unpaid bookings to client's contract allowance."

**Schedule Window Type** (when future dates open for booking)
- **Rolling**: fixed number of bookable days; one new day opens daily at **Schedule Release Time**. Reveals the Schedule Windows table. **Class time-based booking** opens booking 15 min before the computed time (unavailable if Scheduling Hours is Custom in General Setup).
- **Monthly**: next whole month opens on **Day of Month Scheduling Opens For Next Month** (1-28) at release time; clients can never book two months ahead.
- **Weekly**: opens on **Day of Weekly Schedule Release**, covering through 11:59pm the following same weekday.
- Rolling/Monthly/Weekly work with membership "Days before scheduling window" and "Allow Early Access Booking". Branded apps: use Member Day of Month Scheduling Restrictions in Membership Options.
- **Schedule Windows** (Rolling only, one row per service category): **Starts** = days ahead clients can book; **Closes** = minutes before class that booking stops. Both default 0 (no limit).

**Cancellation Windows** (row per service category)
- **When**: minutes before class a client can cancel without penalty (outside = early cancel, inside = late cancel). Default 0 = cancel any time.
- **Enable Cancellations In Consumer Mode**: allows online cancelling; otherwise clients must contact you.

**Default Schedule Lengths**
- **Classes** / **Courses**: days new schedules run by default; end date can always be changed.

**Waitlists**
- **Enable Waitlists**: turns the feature on but capacity must still be set per class. Classes auto-promote by join order outside the cancellation window; courses require applying payment and clicking **Enroll** on the roster. With unpaid signups on, clients may waitlist without a pricing option.
- **Late Cancellation Window Automation**: choose Start "First to Claim" Automation (SMS to all waitlisted, first reply wins) or Continue Auto-add Automation.
- **Waitlist Lock Window**: minutes before start when clients go straight to the roster instead of waitlist. Online, clients cannot book or waitlist and are told to contact you; staff bookings are added directly to the roster.
- **Number of Overlapping Waitlist Allowed**: Unlimited or 1-5.
- **Enforce settings of "Client Unpaid Scheduling Restrictions" for the Waitlist**: on = payment status checked before promotion; off = unpaid visits can be promoted and staff reconcile payment.
- **Allow Clients to Waitlist Classes/Courses that overlap existing reservations**.

**Booking behavior**
- **Count all Pre-registrations as web sign-ups**: staff-added pre-registrations count against online capacity.
- **Duplicate/Overlapping Client Reservations/Sign-Ins**: **Enable - Business Mode** / **Enable - Consumer Mode**; same client can book a class twice or overlapping classes (name appears per booking). Not supported in branded app or Mindbody app or CartV2 branded web tools; Messenger[ai] ignores the setting. When off, a "Registered!" link appears on classes the client already booked.
- **Use Class Levels**, **Use Class Testing** (staff-only tests/progress notes), **Use Leaders/Followers** (online capacity split evenly; role required online; no limit in business mode).
- **Require All Prerequisites Client Types**: on = client needs every prerequisite client type; off = any one suffices.

**Sign-in behavior**
- **Automatically Sign In Future Reservations**: marks clients present at booking. Only use if you do not track attendance or pay teachers per head.
- **Sign In Window**: (when auto sign-in is off) default marks a client signed in if they register under 2 hours before class; adjustable 0-360 min in 5-min steps.
- **Sign In - Late Check-In Window**: 0-360 min after start that preregistered clients can still sign in; after that they become no-shows. **Sign In All** signs the client into all their classes that day.
- **Sign In / Self Sign-In - Look Ahead Window**: minutes the check-in screens look ahead to auto-sign-in a preregistration.
- **Self Sign-In** options: Allow Signing in without Pre-Registration; Allow Signing in Unpaid; Automatically Sign Clients in (only when one class is in the look-ahead window and no other reservations that day); Show Account Balance; Alert Staff to Member Issues (red flash and chime for inactive member or balance owed, including "Pays for" relationships).
- **Sign In - Allow Signing in Unpaid** (Client Check In screen); **Sign In - Change background color**: Never / By Sign In Status (green prepaid, yellow not signed up no balance, red balance or non-member) / By Membership Status; **Flag/Prompt Non-Members** (pop-up asks to continue); **Flag/Prompt Suspended Clients** (needs Scheduling Suspensions in General Setup).

**No-shows and pay**
- **Pay Teachers for No-Shows**: Yes/No.
- **Deduct no-shows from client's pricing option**: Yes/No. Unpaid signups are marked unpaid and must be charged in Point of Sale.

**Sign-in screen display and printing**
- **Class Sign In Sort Order** (Sign In Time or Last name); **Show Client Phone Numbers** and **Show Client IDs** (instructors see only their own classes); **Show Account Balances**; **Alert Clients w/Negative Account Balances** (reminder only, does not block); **Client Alerts Time Window** (All or 1-12 hrs before class); **Enable Registering Tagged Clients**; **Show pricing option details**; **Sign In Receipt - Show Account Balance**; **Sign In Sheet (Print) - Show Yellow Alert** (on prints medical/staff alerts too); **Print Class Sign In Receipts** and **Non Preregistered Client Alert** (each: click it, pick **Studio**, tick the checkbox, **Save**).
- **Assistant1** / **Assistant2**: enable second/third staff slots for classes and courses; paid by Pay Rate 1 by default.
- **Show Client Visit Milestones** (sign-in and Schedule at a Glance) and **Visit counts (milestones)** sub-options: show counts, count class sign-ins, completed appointments, course sign-ins, arrivals.

## Gotchas
- Needs the **Class & Events Options Screen** staff permission (Settings).
- Waitlist enable alone creates no waitlist; capacity is per class.
- Some options only exist when a related feature is enabled (Scheduling Suspensions, Pick-a-Spot, Leaders/Followers, etc.).
- Auto sign-in breaks per-head teacher pay and attendance tracking.
- Changing windows affects what clients can see/book online immediately.

## Related
- [Class and Course Options screen: Directory](203259633-Class-enrollment-options-screen.md)
- [Class Schedule Appearance & Options](Class-and-Course-Options-screen-Class-Schedule-Appearance-Options.md)
- [Course Schedule Appearance & Options](https://support.mindbodyonline.com/s/article/Class-and-Course-Options-screen-Course-Schedule-Appearance-Options?language=en_US)
- [Unpaid online signups](215842797-Unpaid-Online-Signups-for-Classes-and-Enrollments-How-does-it-work.md)
- [Schedule windows setup](204244713-How-can-I-set-up-how-far-in-advance-my-clients-can-schedule-classes-or-workshops.md)
- [Cancellation windows](../online-booking/203257723-How-do-I-set-up-cancellation-windows.md)
- [Waitlists](203253503-Waitlists.md)
- [Prerequisites](204798418-What-are-prerequisites.md)
- [Class assistants](203253513-Class-Assistants-setup-and-scheduling.md)
- [Class and course pay rates](../staff/203253623-Class-and-enrollment-pay-rates.md)
- [Visit Milestones](https://support.mindbodyonline.com/s/article/What-is-Visit-Milestones-on-Class-Sign-in-screen?language=en_US)
- [Early/late cancellations and no-shows](../online-booking/Classes-Early-cancellations-late-cancellations-and-no-shows.md)
