# Field notes: what the screens actually look like

The playbooks are built from Mindbody's support articles, which describe fields and menus but often not exact button labels or layouts. This page is where agents record what they actually observed on the live site, so later sessions don't rediscover it. **Add a dated bullet whenever reality differs from a playbook or fills one of the gaps below.** Keep entries short and factual; never record client data, card details or credentials here.

Format: `- YYYY-MM-DD · <playbook or screen> · <what you saw / what worked>`

## Open questions from the docs (fill these in when you see them)

**Point of sale (playbook 06)**
- Exact label of the final button that completes a sale, and what receipt options appear after.
- How the stored card is selected at checkout (docs mention **CC Key/Stored**), and where the card's last four digits are shown to confirm the right card.
- Which fields a contract sale asks for at POS (start date, first payment, registration fee).

**Check-in and booking (03, 04, 05)**
- ~~Where the **Signed In** checkbox sits~~ → roster column 12, `name=optMissed<visitId>`; whether ticking it saves immediately is still unverified.
- What prompt appears when signing in a client who has no valid pass (unpaid vs. go to sale).
- Whether there is an explicit no-show control, or no-shows are only "not signed in" after class time.
- Whether a late cancel creates a fee by itself or only via the **Charge Fees** tab. (Roster column 13 is **Late Cancel**, `name=optCancel<visitId>`.)

**Appointments (07, 10)**
- Layout of the appointment checkout payment step.
- Label of the slot menu on the appointment schedule grid; where the availability form's day/time controls sit.

**Staff (11)**
- Label of the add-staff button (docs say both "+Add Staff" and "Add New Staff").
- Layout of the Class / Hourly / Commission pay rate screens.

**Contracts and billing (13, 14)**
- Where the termination code list appears on the Terminate form; how to unsuspend.
- Which of the two promo code screens the site uses (`/ASP/adm/adm_tlbx_promotion.asp` vs `/app/services-products/promo-codes`).

**Reports and closeout (16, 17)**
- Names of the bill/coin count fields on Daily Closeout; whether **Preview Close Amounts** is side-effect free.
- Report generate button label per report ("Generate" vs "Go!"); where exports land (assumed Chrome's Downloads folder).

## Observations

- 2026-10-04 · all classic screens · Open `/classic/...` and `/ASP/adm/...` URLs directly; the `/app/business/classic/...` shell wraps them in an iframe, drops URL parameters and can render blank.
- 2026-10-04 · new-style pages (`/app/clients/...`) · 10-20 s to load on the sandbox; prefer classic equivalents when one exists (e.g. contact logs).
- 2026-10-04 · Claude in Chrome · JS results containing URL query strings, or text like `a=b/c`, are blocked (`[BLOCKED: Cookie/query string data]`); return parsed values and replace `/` in dates.
- 2026-10-04 · class roster search (`#consumerSearchQueryInput`) · needs a real click in the centre of the box before typing; results need a real click (JS `.click()` ignored).
- 2026-10-04 · booking (W1) · clients who owe money trigger an "Outstanding account balance" pop-up with card fields after the booking is saved; dismiss with **Ignore** (`#BtnIgnore<n>`), never enter card data.
- 2026-10-04 · booking a full class · client went straight to the waitlist with no prompt (sandbox).
- 2026-10-04 · cancel (W2) · ✕ opens in-page dialog `#autoGenLightBox` titled "Early/Late cancel this visit?"; not a native confirm. Cancelling in a full class auto-promoted the first waitlisted client.
- 2026-10-04 · contact log (W3) · note field is TinyMCE; setting the textarea saves an empty note.
- 2026-10-04 · Account Details · Client Home showed "Non-Member" for a client whose Memberships grid had an Active contract; trust Account Details.
- 2026-10-04 · reports · Sales, Attendance, First Visit, Last Visit use `#reportForm` + `#button-generate` ("Go!") and render `table.result-table`.
