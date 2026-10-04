---
title: Notifications (email and text message) settings screen
category: settings-navigation
source: https://support.mindbodyonline.com/s/article/203254073-Auto-emails-text-message-descriptions?language=en_US
source_updated: 2026-08-24
---
# Notifications (email and text message) settings screen

Reference catalog of every system-generated notification on the Notifications screen: what triggers it, timing, and quirks. Use when deciding which notifications to enable or when a client says they did or did not get a message. Enabling steps are in the setup article.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/settings/notifications
- Menu path: **Settings** > **Communications & Marketing** > **Notifications**

## Settings & fields
General rules
- Clients must be opted in and have valid contact info. Opt-in category by group: Account Updates = account management; Client Schedule = reminders and schedule changes; Promotional = news and promos; Operations and Staff Facing = no client opt-in (Operations are mandatory, email only; Promotional email only).
- Email only goes out if a **Business reply to email** is set on the notification.
- Switching site language does not translate emails you edited manually, only default text.
- Booking notifications for desktop bookings also fire for Mindbody app, branded app, branded web tools bookings.
- Per-email checkboxes: **Always Send/Default On?**, **Use in business mode?**, **Copy Instructor** (CC/BCC), **Send email only to members** (birthday, anniversary).
- Replace phrases cited: <APPTINFOBOOK>, <APPTINFO>, <MULTIPLECANCELLEDAPPOINTMENTSINFO>, <OLDAPPTDETAILS>, <CLIENTFORMS>, <VISITTYPE>, <PASSWORDLINK>, <MBLINK> vs <STUDIOURL>. Lists of appointments in SMS can increase SMS volume/cost.

### Account Updates
- **AutoPay Purchase Confirmation**: immediate on each autopay charge (contract or scheduled on Account Details); not sent for fee autopays (no-show, late cancel, suspension); sent if declined then charged to house account. No staff copy.
- **Contract (BUSINESS MODE)**: immediate when a contract is sold in POS or Business app; change <STUDIOURL> to <MBLINK> so clients agree on the Mindbody site; digital agreement needs the **Contract Confirmation** client alert.
- **Contract / AutoPay Credit Card Expiring**: nightly; based on Credit Card Expiration client alert threshold; only if card expires before next autopay; incompatible with "Run autopay when the pricing options run out".
- **Contract Date Update Notification (Presales)**: immediate when presale contract start date edited.
- **Contract Reminder**: immediate when **Email Contract Reminder** clicked in client's Account Details > Contracts.
- **Contract Renewal Notification**: nightly, N days ahead, only for fixed-interval contracts (not pay-per-run-out, not paid-in-full). Choose contracts in "Enable the following Contracts" dropdown. If a contract is deactivated first, emails keep sending; disable it in the dropdown before deactivating (or reactivate, disable, redeactivate).
- **Contract Unsuspended**: nightly, N days before suspension ends.
- **Invoice Email**: immediate when an invoice is created and emailed; enabled by default and must stay on to send invoices.
- **New Client / Welcome (BUSINESS MODE)**: immediate on new profile via business site Client Directory (email only; not from Business app; with Family Accounts or Consumer Identity only via Client Directory add).
- **New Client / Welcome (CONSUMER MODE)**: immediate on consumer-site or Registration widget signup or branded web Cart booking; includes password-setup link; not from Prospect widget, Mindbody app bookings, or branded apps requiring Mindbody account.
- **Order Shipped Notification**: immediate when an online order is marked "Fulfilled" in Manage Online Orders report.

### Client Schedule (staff can usually be copied)
- **Advanced Course Confirmations** and **(Payment Plan)**, **Course Confirmations** and **(Payment Plan)**: immediate on enrollment; on business site tick **Email Client Confirmation** on Enroll Client. Payment-plan email lists total, deposit, balance; no down payment shows "Paid in Full". Sent only once enrollment completes.
- **Appointment Booking Confirmation (Single / Recurring / Waitlist)**: immediate; Single sends one itinerary per day; business site sends only if **Always Send/Default On?** or the "Send a confirmation" box is ticked at booking; Waitlist triggers when booking from Appointment Waitlist screen; masked staff names show as generic (Staff/Therapist); Business app needs "Ability to view all clients" permission; staff not copied if client booked in Mindbody app and isn't opted in to email.
- **Appointment Cancellation (Early / Late)**: immediate; early/late set by cancellation window on Appointment Options; staff-made cancellations only send if **Use in business mode?** is on; prompt appears only if Default On is off.
- **Appointment Change Notification**: immediate on changing time, staff, service, or length (sidebar or Modify Appointment); "Send Change Notification" boxes default checked; needs client Reminders and schedule changes opt-in; not from Business app; same-day multi-reschedules grouped.
- **Appointment Reminder**: nightly, N days ahead; one reminder per appointment, not resent after edits; optional auto-confirm; booking after the last reminder window (2pm-8pm) still gets a reminder that evening; may also live in Retention Marketing Dashboard; clients may opt in to SMS by texting START (Retention Marketing Dashboard businesses).
- **Appointment Request Confirmation (Single / Recurring)**, **Appointment Request Denial**, **Appointment Request Notification**: immediate; confirmation also covers adding from waitlist; enable all three together; denial not sent if client cancels the request first; staff copy by email only.
- **Class & Event Cancellation (Early / Late)**: immediate; from Class Sign In; instructors can be copied, substitutes cannot; business-mode send depends on **Always Send/Default On?** and **Use in business mode?** combos (both on = auto; only business mode = prompt; only default-on = nothing sent).
- **Class/Event Cancellation (service not scheduled any more)**: immediate when a class/course is cancelled from the schedule gear icon with send option; once per client for blocks; substitute instructors not emailed.
- **Course Waitlist Notification**: immediate on adding to course waitlist; no staff copy; promotion to roster sends Course Confirmation; class waitlist uses the next item.
- **No Show Notification Emails**: nightly; classes by Late Check-In Window option; appointments need payment applied, time passed, not checked out.
- **Reservation Added from Waitlist Notification**: immediate; may be in Retention Marketing Dashboard.
- **Reservation Confirmations (Single / Recurring)**: immediate; on business site use **Adv. Register** with "Email client confirmation"; not from Business app; branded-app reservations by one client for another do send, consumer-site ones do not.
- **Reservation Reminder**: nightly, morning of the chosen day; courses remind per date; no staff copy.
- **Teacher Sub Notification**: immediate after a temporary substitution in Make Schedule Change or Business app; goes to registered clients, original and sub teachers or a business copy address; no staff copy.

### Operations
- **Appointment Confirmation (Manual)**: **Send Email Confirmation** link in appointment sidebar or Modify Appointment; appointment turns from green to light purple.
- **AutoPay Failed Notification**: immediate; pair with **Autopay Failed** alert; not sent for ACH/Direct Debit declines (they become negative balances, see Account Balances report) unless bad account details; not sent for manual autopay runs; one email per declined contract item; repeats daily when resubmit is on.
- **Client Forms Notification**: **Send Client Forms** on client's Documents screen.
- **Client Schedule (Manual)**: **Email Schedule** on client Schedule screen; first 15 services only.
- **Forgot Login Information**: consumer site password reset; cannot be disabled.
- **Gift Card Delivery Email**: PDF to recipient and copy to purchaser; cannot be disabled.
- **Purchase Receipt (BUSINESS MODE)**: tick **Send Email Receipt** in POS (or set Business Mode Always Send); Business app adds signature.
- **Purchase Receipt (CONSUMER MODE)**: cannot be disabled.
- **Live Stream Class Link**: 30 minutes before class (or 3 minutes after booking if within 30); not shown or editable on screen; links auto-created around midnight, same-day classes need manual link creation; clients need an email.

### Promotional
- **Appointment Follow-up**: nightly, N days after (must be 1 or more; 0 blocks sending), per service category.
- **Birthday Email**: nightly, N days before; members-only option skips suspended memberships.
- **Client Closed** (immediate when POS sells to a prospect) and **Close Follow-up** (nightly, N days after close; Prospects feature).
- **First Visit Anniversary**: nightly; not retroactive for anniversaries before enabling; members-only option.
- **First Visit Email (Appointment / Reservation)**: nightly, once per client.
- **Open Ticket Quote**: **Email Ticket** in POS; needs Open Tickets enabled in General Setup & Options; visible to owner or Rep 1 staff.
- **Series Notification - Time Running Out** and **- Visits Remaining Low**: nightly; Accelerate/Ultimate only; thresholds set per pricing option; skipped for repurchasers and clients with future autopays.

### Staff Facing
- **Contact Log Follow-up Notification**: nightly; needs Sales Team Management.
- **New Lead Generated**: immediate to the **Business copy email** when a prospect is added.
- **Teacher Sub Reminder Email**: nightly, N days before; from Make a Schedule Change teacher substitution, not Quick Teacher Substitution; needs staff email.

## Gotchas
- Missing reply-to email means nothing sends.
- Deactivating a contract without first disabling its renewal email keeps emails flowing.
- Some features depend on software package.

## Related
- [Setting up auto emails and texts](203254063-Setting-up-Auto-Emails-and-Texts.md)
- [Replace phrases](205778938-Replace-phrases.md)
- [Notifications vs Marketing Suite](https://support.mindbodyonline.com/s/article/Auto-emails-vs-the-Marketing-Suite?language=en_US)
- [Client email/text subscriptions](https://support.mindbodyonline.com/s/article/How-to-opt-in-to-receive-auto-emails-reminders-and-notifications?language=en_US)
- [Emails/texts to staff](https://support.mindbodyonline.com/s/article/207199957-How-do-I-send-include-cc-auto-emails-and-text-messages-to-my-staff-members?language=en_US)
- [Clients not receiving SMS](https://support.mindbodyonline.com/s/article/Why-is-my-client-not-receiving-SMS-text-messages?language=en_US)
- [Client alerts](../clients/203259733-Client-alerts.md)
- [Cancellation windows](../online-booking/203257723-How-do-I-set-up-cancellation-windows.md)
