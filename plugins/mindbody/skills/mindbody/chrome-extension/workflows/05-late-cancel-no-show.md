---
workflow: Late cancel, early cancel or no-show a class booking
safety: 🔴 Money or irreversible (only when charging fees; cancelling alone is 🟡)
---
# Late cancel, early cancel or no-show a class booking

Cancel a client's class reservation (early cancel, no penalty; late cancel, session kept), mark a no-show, and only if asked charge the late-cancel or no-show fee. Typical phrasings: "Dana can't make tonight's 6pm, cancel her", "late cancel Marcus from this morning's class", "mark the no-shows from 9am", "charge the no-show fees for last week".

## Ask the person for
- Client name, class name, date and time.
- Which outcome they want: early cancel (no penalty), late cancel (penalty applies), or no-show. If they do not say, check the cancellation window and propose one; do not guess. The window is "minutes before class" per service category in Class and Course Options > Booking & Sign-in Policies ([Cancellation windows](../../articles/online-booking/203257723-How-do-I-set-up-cancellation-windows.md)); cancelling inside it is late.
- Whether fees should be charged. Never charge by default.

## Read first
- [Early cancellations, late cancellations and no-shows (classes)](../../articles/online-booking/Classes-Early-cancellations-late-cancellations-and-no-shows.md) — the three roster actions.
- [Class Sign In screen](../../articles/classes-courses/203259423-Classes-Class-Sign-in-screen.md) — X icon, Late Cancel and Signed In checkboxes.
- [No-Show/Late Cancel Fees](../../articles/online-booking/How-to-automate-No-Show-and-Late-Cancel-Fees.md) — Manage Fees and Charge Fees tabs.
- [No-Shows report](../../articles/reports/203256753-No-Shows-report.md) — listing missed visits.

## Steps
1. **Open the class roster** — navigate to `https://clients.mindbodyonline.com/app/business/classic/admmainclass?fl=true`, go to the class's date, `find` "Sign In link for <time> <class>" and click it. Confirm the date and time; `get_page_text` and locate the client's row and **Payment Type**.
2. **Decide the outcome and say it** (🟡) — one line, e.g. "Late cancelling Dana Cole from Tue 6pm Spin; her 10-class pass will lose a session." Proceed if the person already asked for this specific action.
3. **Early cancel** — click the red **X** left of the client's name. They leave the roster; the session used goes back to their pass. After class start this needs the Override cancel policy permission.
4. **Late cancel** — tick the **Late Cancel** checkbox at the far right of the row. The name stays on the roster, the spot opens up (waitlist may fire), and the session stays used. With no prepaid pass the visit stays unpaid.
5. **No-show** — leave the client on the roster and make sure **Signed In** is unticked after class (untick if auto sign-in ticked it). Do not tick Late Cancel. They show as Absent on Visits and count in the No-Shows report. If the site has "Deduct no-shows from client's pricing option" on, a session is deducted; read the result rather than assuming.
6. **Check effects** — re-read the roster, then open the client's **Visits** and confirm the status (Late Cancel, Absent, or no entry for an early cancel).
7. **Fees (only if asked)** — go to `https://clients.mindbodyonline.com/app/business/noshowlatecancel` (Settings > Clients > No-Show/Late Cancel Fees). Check **Manage Fees** has fees set for the category (read only). Open **Charge Fees**, set the period (up to 90 days) and filters, and `get_page_text` the Member Details table: Name, Date and Time, Pricing Option, Fees, Fee Type. Tick or untick the Fee Type checkbox per row so only the intended client and fee are selected.
8. 🔴 **Stop** — show: client name(s), class/date, fee type, fee amount, and that each checked row schedules an autopay that runs the next day (clients without stored billing info are debited to their account balance, possibly going negative). Wait for an explicit yes in chat for these exact rows. Only then click **Charge Fees**.

## Verify
- Roster shows the intended state; Visits status matches.
- After charging fees: **Autopay Detail** report shows the next-day scheduled fees (see [Autopay Detail report](../../articles/reports/203256413-Autopay-Detail-report.md)); on the client's **Account Details** > **Autopays** the charge is listed.
- Tell the person the charge runs next day and may fail or go to balance.

## If it goes wrong
- No X or Late Cancel control: staff lacks Cancel reservations (or Override cancel policy); tell the person.
- Clicked the wrong box: re-tick/untick the same control and re-verify. Do not use Charge Fees to fix it.
- Charged in error: stop and report; reversing is a separate 🔴 flow ([Returns, refunds and voids](../../articles/pos-payments/203259303-Returns-Refunds-and-Voids.md)).

## Variations
- Cancel from the client side: client's **Account Details** > pricing option three-dot > **Show Visits** gives per-visit **Early Cancel**, **Late Cancel**, **Make Unpaid** (late cancel there is financial, so treat it as 🔴).
- Review no-shows without changing anything (🟢): **No-Shows** report, `https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_noshows.asp?category=Clients`.
