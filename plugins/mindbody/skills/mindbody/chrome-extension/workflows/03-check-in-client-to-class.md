---
workflow: Check a client in to a class
safety: 🟡 Changes data
---
# Check a client in to a class

Sign a client into today's class from the Class Schedule and its Class Sign In roster: register walk-ins, use their existing pass, handle a full class (waitlist), and handle clients with nothing to pay with. Typical phrasings: "check Sarah in to 6pm spin", "sign Marcus into the 9am yoga", "she just walked in, put her in the next class".

## Ask the person for
- Client name (plus email or phone if the name is common).
- Which class: name and start time today (and instructor if two classes share a time). If vague, open the schedule, list the candidates and ask.
- If the client has no usable pass: whether to sell one (hand off to playbook 06), register them unpaid, or leave them off. Do not choose for the person.

## Read first
- [Class Sign In screen](../../articles/classes-courses/203259423-Classes-Class-Sign-in-screen.md) — every roster control, Payment Type column, Change, Buy, X.
- [Class Schedule screen overview](../../articles/classes-courses/217438617-Class-schedule-overview.md) — finding the class and Sign In link.
- [Waitlists](../../articles/classes-courses/203253503-Waitlists.md) — the full-class pop-up and promoting from the waitlist.
- [Unpaid reservations permission](../../articles/classes-courses/203281533-How-to-I-allow-my-staff-members-to-sign-clients-up-for-classes-as-unpaid-Unpaid-reservations.md) — why a booking may be blocked.

## Steps
1. **Open the schedule** — navigate to `https://clients.mindbodyonline.com/app/business/classic/admmainclass` (or **Classes** in the left nav). Make sure the view is today (**Today** button) and the location filter is right.
2. **Find the class** — `find` "Sign In link for <time> <class name>". Note the registered/capacity count shown with it (e.g. 7/15). Click **Sign In** to open the roster.
3. **Check whether the client is already booked** — `get_page_text` and look for the name. If present, go to step 6.
4. **Register the client** — click **Search for client**, type the last name, and select the person. If there is no match, search again by email or phone before choosing **Add new client** (see playbook 02). Note that this quick path does not send the Reservation Confirmed email.
5. **Class full** — if a "class is full" pop-up appears, tell the person and ask whether to waitlist. If yes, click **No, waitlist instead**. Do not override capacity unless the person asks and the screen offers it. Later, a waitlisted client is promoted with **Add to class** beside their name in the waitlist section (needs the Make reservations permission; a session is deducted on promotion).
6. **Check payment** — in the client's roster row read **Payment Type**, **Expiration Date** and **Remaining**:
   - Shows a pricing option name: their pass will pay. If a different active pass should be used, click **Change** and choose it (Change works even if the option is not set for that service category).
   - Shows "Unpaid [category]" and the person wants a sale: use **Buy** (opens Point of Sale) and follow [playbook 06](06-sell-pricing-option.md); return here afterwards.
   - Shows "Unpaid" and the person wants them in anyway: confirm that this leaves an unpaid visit to reconcile later; it requires the **Make unpaid reservations** permission.
7. **Check alerts and waiver** — look for a red liability waiver icon on the row (click it only to email a signature request, with the person's OK), any red/yellow alert, and a red negative **Balance** if shown. Report them.
8. **Sign in** — tick the **Signed In** checkbox in the client's row (`find` it by the row's name; verify the checkbox state after clicking). Clients registered by staff after class start, or under the Sign In Window, may already be signed in.

## Verify
- Re-read the roster with `get_page_text`: the client is listed, **Signed In** is ticked, Payment Type is as intended, and the **Signed in** and **Total Count** tiles went up by one.
- For a waitlist add, the client shows in the waitlist section, not the roster.

## If it goes wrong
- No Sign In or register ability: staff lacks View/Make reservations; tell the person.
- Cannot register because the client has no valid pass: either sell one (playbook 06), or needs **Make unpaid reservations**.
- Checked into the wrong class: untick **Signed In**; use the red **X** (early cancel) only if the person wants the booking removed, since it returns the session to the pass.

## Variations
- Sign in someone already pre-registered: steps 1-3 then 6-8.
- Future class: playbook 04.
