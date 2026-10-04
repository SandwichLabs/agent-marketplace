---
workflow: Book a client into a future class
safety: 🟡 Changes data
---
# Book a client into a future class

Reserve a client into a class on a later date, set up a recurring reservation with Adv. Register, or mass-register a group of tagged clients. Typical phrasings: "book Priya into Thursday's 7am", "put Tom in every Tuesday spin through December", "register the whole team for Saturday".

## Ask the person for
- Client name (or the tagged group / client type for a mass booking).
- Class name, date and time (and instructor if ambiguous).
- For recurring: frequency, days of week, start and end date (max span is one year or the class end date, whichever is sooner).
- Payment: use their existing pass (**Make a recurring reservation**) or register unpaid (**Register as unpaid**). If they need a pass sold, hand off to [playbook 06](06-sell-pricing-option.md).

## Read first
- [Class Sign In screen](../../articles/classes-courses/203259423-Classes-Class-Sign-in-screen.md) — registering from the roster.
- [Adv Register / recurring reservations](../../articles/classes-courses/203257783-How-do-I-make-a-recurring-class-reservation.md) — fields and limits.
- [Mass register clients](../../articles/classes-courses/203268113-Classes-How-can-I-mass-register-multiple-clients-into-a-class-or-event.md) — Register Tagged Clients.
- [Tagging](../../articles/clients/203256033-Tagging.md) — Tag new vs Tag add.

## Steps
1. **Open the Class Schedule** — navigate to `https://clients.mindbodyonline.com/app/business/classic/admmainclass?fl=true`. Use the calendar icon or the **Day / Week** arrows to reach the target date. Use filters (service category, class type, instructor) if needed.
2. **Open the class** — `find` "Sign In link for <time> <class>" on that date and click it. Confirm the date, time and class name at the top of the roster, and the registered/capacity count.
3. **Pick the path**:
   - **Single reservation**: click **Search for client**, search by last name, select the client. Note this quick path sends no confirmation email.
   - **Recurring**: click **Adv. Register**, search and select the client, then set **Make this reservation every**, **Select days**, **Start date** and **End date**. Multi-day recurrence (such as Mon/Wed/Fri) only works if "Bundle classes to allow for multi-day recurring reservations" is on in Class and Course Options; if the option is missing, say so rather than changing settings.
   - **Mass register**: first make the tag list (see below), then on the roster click **Register Tagged Clients**; the number in brackets is how many are tagged.
4. **Mass-register preparation** — if **Register Tagged Clients** is missing, the site setting "Class Sign In - Enable Registering Tagged Clients" is off (Settings > Services > Class and Course Options > Booking & Sign-in Policies). Ask before changing it. To build the list: Client Directory (`https://clients.mindbodyonline.com/app/business/asp/adm/adm_clt_lkup.asp`), filter (for example by client type), click **Tag new** (replaces any earlier list) and **OK**. Needs the Tag clients permission.
5. **State what will be booked** — one line: client(s), class, date(s), paid vs unpaid. For a mass or recurring booking list the number of sessions or clients.
6. **Commit** — for recurring, click **Make a recurring reservation** (pays from their pass) or **Register as unpaid** (leaves unpaid visits; the person must have said so). For a single booking, complete the pop-ups: if the client has no valid pass you will be offered unpaid or sale paths; do not choose unpaid without the person's instruction.
7. **Full class** — if the class is full, offer **No, waitlist instead** (see [Waitlists](../../articles/classes-courses/203253503-Waitlists.md)). The Adv. Register button is hidden for full rosters and free classes.

## Verify
- Re-read the roster (`get_page_text`): the client appears, with the expected Payment Type.
- Open the client's profile > **Schedule** (and **Visits** with a future date range) to confirm every recurring date shows as Reserved ([Client Visits](../../articles/clients/215843328-Client-Visits-Screen-overview.md)).
- For mass registration, compare the roster count with the tag count.

## If it goes wrong
- No class on that date: the date may be beyond the schedule window or the class may not exist; check the schedule, do not create classes here.
- Mass option unavailable: tagged clients exceed capacity; raise capacity (a class edit, ask first) or add individually. Courses with a payment plan attached need enrolling one at a time.

## Variations
- Cancel or move a booking: playbook 05 and the [Class Sign In screen](../../articles/classes-courses/203259423-Classes-Class-Sign-in-screen.md) (red **X**).
- Courses/enrollments: same Register Tagged Clients flow from the course roster, one date at a time ([Mass register](../../articles/classes-courses/203268113-Classes-How-can-I-mass-register-multiple-clients-into-a-class-or-event.md)).
