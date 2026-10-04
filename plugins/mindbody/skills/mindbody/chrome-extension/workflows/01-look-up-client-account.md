---
workflow: Look up a client account
safety: 🟢 Read-only
---
# Look up a client account

Find a client and review their profile: active passes and contracts, sessions remaining, balance, visit history, alerts and waiver status. Typical phrasings: "does Sarah Lee still have classes left?", "pull up Marcus's account", "is Dana's waiver signed?"

## Ask the person for
- The client's name (first and last). Email, phone or client ID helps if the name is common; if they give only a first name, ask for more.
- What they want to know (passes, balance, visits, waiver, all of it). If unclear, review everything below and report what is relevant.

## Read first
- [Looking up clients](../../articles/clients/203259203-Looking-up-clients.md) — quick search vs Client Directory, search quirks.
- [Client Info screen overview](../../articles/clients/Client-Info-screen-overview.md) — alerts, waiver, membership summary, sessions remaining.
- [Client Account Details screen](../../articles/clients/215843418-Client-Account-Details-Screen-overview.md) — pricing options, contracts, balances.
- [Client Visits screen](../../articles/clients/215843328-Client-Visits-Screen-overview.md) — visit history and statuses.
- [Client alerts](../../articles/clients/203259733-Client-alerts.md) — what yellow/red alerts mean.

## Steps
1. **Confirm the site** — per the [general guide](../README.md), check the site name in the header matches the business the person means.
2. **Search** — find "Find a client field at top of page", click it and type the last name (or first name) only. Full names containing a space or hyphen can return nothing. Pick the match from the autofill list.
3. **Handle several matches** — if more than one person matches, use `get_page_text` to list them and compare email/phone with what the person gave. If still ambiguous, ask which one. Fallback: navigate to the Client Directory (`https://clients.mindbodyonline.com/app/business/asp/adm/adm_clt_lkup.asp`), choose the "Search client by" field (e.g. Email address or Phone #), enter the term, click **Search**. If the client is not found, open **Filters** and switch the status to All clients, since inactive clients are hidden by default.
4. **Client Info** — click the client's name, then **Client Info** in the client submenu. `get_page_text` and note: the **Alerts** module (yellow Client Alert and red Staff Alert text), the left-column **Liability waiver** status (complete, incomplete or expired), Membership summary (status, current membership, **Sessions Remaining**), and next/last visit.
5. **Account Details** — click **Account Details**. Click **Show all Dates** if the window looks short. Read each section with `get_page_text`: **Available for Use** (active pricing options with Remaining, Scheduled, Expiration Date), **Contracts** (Status, Start/End Date, Autopays), **Unpaid Visits** (# Owed), **GIFT/Debit Account** (Current Balance; negative shows red), and **Autopays** if relevant. The **Inactive** section holds used-up or expired options; mention it only if asked.
6. **Visits** — click **Visits**, choose **Show All Dates** (or a date range), and read the table: Date, Description, Status (Signed-in, Late Cancel, Reserved, Absent, etc.) and Pricing Options column. Future bookings appear only if the range extends forward.
7. **Report** — give a short summary: active options with remaining visits and expiry, contract status, balance, unpaid visits, recent and upcoming visits, alerts verbatim, waiver status. Do not click Edit, Return/Void, Suspend, Terminate or any three-dot action.

## Verify
- The name, email or ID on Client Info matches the person's description.
- The date range was widened before you concluded "no visits" or "no balance".

## If it goes wrong
- Search returns nothing: try last name only, then email or phone in the Client Directory; check inactive clients via Filters.
- A profile with no ID assigned does not appear in any search; tell the person rather than creating a new one.
- Sections missing (for example no GIFT/Debit Account): widen the date range; otherwise the staff login may lack permissions. Say what you could not see.
- Remaining counts look stale after an expiry: the **Recalculate** button on Account Details refreshes it, but it changes data (🟡), so ask first.
- Alert pop-up on opening a client: read it, report it, and dismiss it only with the person's OK.

## Variations
- Purchase history or receipts only: use **Purchases** ([Client Purchases screen](../../articles/clients/215843338-Client-Purchases-Screen-overview.md)).
- Find all clients with an unsigned waiver or a current contract: Client Directory **Filters** ([Looking up clients](../../articles/clients/203259203-Looking-up-clients.md)).
- Reactivate or edit what you found: that is a 🟡 change; see [Client profile FAQ](../../articles/clients/203273113-Questions-about-the-client-profile.md).
