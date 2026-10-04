---
workflow: Book, reschedule, move, cancel and check out an appointment
safety: 🔴 Money or irreversible
---
# Book, reschedule, move, cancel and check out an appointment

Put a client on a staff member's appointment book, then change it, cancel it, or take payment. Typical phrasings: "book Dana for a 60-minute PT session Thursday at 5 with Marcus", "move Sam's 3pm to Friday", "late cancel Priya's appointment", "check out Lee's session".

## Ask the person for
- Client name, appointment type (service), staff member, date and start time. If the client is new, use the add-client workflow first.
- For changes: which existing appointment, and the new date/time or new staff member.
- For cancellations: early or late cancel. If unsure, ask; late cancel deducts a session or fee.
- For checkout: which pricing option or payment method. Never type card numbers; if a card must be entered, ask the person to do it.

## Read first
- [How to book appointments](../../articles/appointments/206615788-How-do-I-book-an-appointment.md) — booking sidebar, Book vs Book & Buy.
- [How to reschedule appointments](../../articles/appointments/Rescheduling-Appointments-From-the-Sidebar-using-the-Reschedule-function-action.md) — sidebar, drag, Reschedule action.
- [Move an appointment to another staff member](../../articles/appointments/222455187-I-need-to-change-which-staff-member-took-an-appointment-How-do-I-move-the-appointment-to-another-staff-member-s-schedule-Modifying-Appointments.md)
- [How to manage appointment cancellation](../../articles/appointments/203258403-How-do-I-early-cancel-late-cancel-or-reschedule-appointments.md)
- [Appointment Checkout](../../articles/appointments/Appointment-Checkout.md)

## Steps
### A. Book (🟡)
1. **Open the schedule** — navigate to https://clients.mindbodyonline.com/app/business/mainappointments/index (menu: **Appointments**). Confirm the site name. Pick the date; use **Day** view for several staff.
2. **Find the slot** — screenshot the grid; available times are solid, unavailable gray. Click the open block in the right staff member's column. No open block means the staff member lacks availability (see workflow 10); stop and tell the person.
3. **Pick the client** — in the left sidebar, search and select the client (read_page to confirm the name).
4. **Choose the service** — click **Service** and pick the appointment type. Check start/end time.
5. **Choose how to finish** — **Book** (pay later), **Book & Buy** (opens checkout, 🔴) or **Book & Apply** (uses a pricing option, deducts a session, 🔴). Tick **Send Confirmation** only if the person wants an email. Default to **Book**.

### B. Reschedule (🟡)
1. Click the appointment. Same day or staff change: edit in the sidebar and **Save**, or drag the block and click **OK**.
2. Different week or location: choose **Reschedule** in the action menu, drag the appointment from the sidebar to the new slot, then **Save**.
3. Only unpaid appointments can be modified. If payment is applied, early cancel and rebook (the cancel is 🔴, see D).

### C. Move to another staff member (🟡)
1. Click the appointment > **Modify** > **Change Instructor**, click the new staff name, then **Update and Close** (top right). Alternatively drag onto the other staff column and click **Save** in "Move appointment" (note whether **Send Change Notification** is pre-checked).

### D. Cancel (🔴)
1. Click the appointment. State which kind: **Early Cancel** (no penalty) or **Late Cancel** (session deducted or fee; the option appears only after payment applied or checkout).
2. 🔴 Stop: show client, appointment, early/late, and any session or fee consequence, and wait for an explicit yes.
3. Choose **Early Cancel**/**Late Cancel**; if the client has other same-day appointments pick **Cancel this appointment**; click **Complete Early Cancellation** or **Complete Late Cancellation**. Warn the person a confirm box may appear.

### E. Check out (🔴)
1. Click the appointment > **Checkout**. Under Unpaid, **Select pricing**, then **Add to cart**.
2. Review the cart (tips, promos, discounts only if asked), click **Checkout**, pick the payment method.
3. 🔴 Stop: show client, items, total, payment method (card ending), and wait for an explicit yes. Then **Complete Sale**; optionally **Email receipt**, then **Done**.

## Verify
- Re-open the day; the block shows under the right staff, time and client (read_page or screenshot).
- Cancelled: check **Insights > Reports > Clients > Cancellations**. Checked out: appointment status is Completed and the client's Purchases screen shows the sale.

## If it goes wrong
- "This staff member is not available for this type of appointment": staff lacks availability or the type assignment; fix that first.
- Move fails: the receiving staff member must be assigned to that type and open at that time.
- Late Cancel missing: payment not yet applied; ask the person whether to apply payment first.
- Early cancel after the cancel window needs the Override cancel policy permission; report, do not work around.
- Checked-out appointments cannot be edited or moved. Saved cards need the Run stored credit cards permission.

## Variations
- Several or recurring bookings: see [booking](../../articles/appointments/206615788-How-do-I-book-an-appointment.md).
- Cancel a whole recurring series: appointment > **Modify** > **Cancel Recurring Appointment** (🔴).
- Charge a no-show fee: see [automate fees](../../articles/online-booking/How-to-automate-No-Show-and-Late-Cancel-Fees.md); manual charges are 🔴.
