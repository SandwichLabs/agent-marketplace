---
workflow: Add a new client
safety: 🟡 Changes data
---
# Add a new client

Create a client profile after checking that the person is not already in the system, and make sure the liability waiver is handled. Typical phrasings: "add Jordan Kim as a new client", "set up a profile for the walk-in at the desk".

## Ask the person for
- First and last name (required). If missing, ask.
- Email and mobile number (needed for duplicate checks, receipts and reminders; ask for them even if the site does not require them).
- Any fields this site requires (see step 4), plus optional extras the person wants: birthday, gender, address, referral type, client ID.
- Whether to send the New Client Welcome email, and the client's communication preferences. Default is email only; do not opt anyone in to text marketing on their behalf.

## Read first
- [Adding clients](../../articles/clients/Adding-Editing-Clients-Mindbody-Experience.md) — the five places to create a profile and field meanings.
- [Client required fields](../../articles/clients/202988236-Client-required-fields.md) — what the form will insist on.
- [Looking up clients](../../articles/clients/203259203-Looking-up-clients.md) — duplicate search tips.
- [Locate Duplicate Clients tool](../../articles/clients/203259613-Locate-Duplicate-Clients-tool.md) — fuzzy duplicate check.
- [Liability waiver](../../articles/clients/203259873-Liability-waiver.md) — statuses and how staff mark or email it.

## Steps
1. **Search for duplicates (🟢)** — find "Find a client field at top of page" and search by last name, then by email, then by phone digits only (no symbols). Full names with spaces or hyphens return nothing, so search one name part at a time. Also try a nickname or formal/short variant (David/Dave). For an exhaustive check, navigate to `https://clients.mindbodyonline.com/app/business/asp/adm/adm_clt_lkup.asp`, open **Filters**, set status to All clients (inactive profiles are hidden by default) and search.
2. **Decide** — if a likely match exists, show the person the name, email and phone and ask whether it is the same person. If yes, stop: use that profile (reactivate via **Activate** on Client Info if it is inactive; see [Client profile FAQ](../../articles/clients/203273113-Questions-about-the-client-profile.md)). Only continue when no match exists or the person confirms it is someone new. Optionally mention the Locate Duplicate Clients tool (Settings > Clients) for a character-based sweep.
3. **Open the form** — click the **Find a client** field, then **+Add New Client**. (Alternatively **Clients** in the left nav, then **Add New Client**, which has extra fields such as Company, Middle name and Send welcome email.)
4. **Fill the form** — use `read_page` with `filter: interactive` to get refs, then `form_input`. Required fields carry an asterisk (*); first and last name are always required, and the site may require more. Marking any one address part required makes the whole address required. If **Mobile number** is filled, choose **Mobile provider** (needed for texting). Custom dropdowns: click, then choose the option.
5. **State what you will create** — one line: "Creating profile for <name>, <email>, <mobile>." Then click **Add New Client** at the bottom of the form (**Add Client** in the search-bar or Point of Sale versions).
6. **Open Client Info** — you land on the new profile; click **Client Info** if needed.
7. **Handle the waiver** — in the left column and in **Additional information**, read the liability waiver status. Options, in order of preference:
   - Client signs themselves: click **Email liability waiver to client**, or have them sign at the desk/business app (signature is captured and uploaded).
   - Client has signed on paper in front of staff: only with the person's explicit say-so, use **Mark complete** (sidebar) or **Mark Liability Waiver complete** (Additional information). Do not mark it complete on your own assumption.
   - If the waiver is not required at this business or no waiver exists, report that.

## Verify
- Search the new client by last name from **Find a client**: the profile appears (a profile with no ID does not appear in searches).
- Client Info shows the entered name, email and phone, and the waiver status you set or sent.

## If it goes wrong
- Form refuses to save: read the red messages; a required field (including whole address) is missing. Ask the person for it rather than inventing data.
- No **Add Client** option: staff login lacks the Add Client permission; tell the person.
- Wrong profile created: do not delete; deactivation or merging are separate approved tasks ([Merge Duplicate Clients](../../articles/clients/203259603-Merge-Duplicate-Clients-tool.md) is irreversible, so ask first).

## Variations
- Add from Class Sign In (Search for client > Add new client) so the person lands on the roster: see [Adding clients](../../articles/clients/Adding-Editing-Clients-Mindbody-Experience.md) and playbook 03.
- Family members: **Add Family Member** creates ordinary separate profiles, not a Family Account ([Family accounts FAQ](../../articles/clients/Family-accounts-FAQ.md)).
