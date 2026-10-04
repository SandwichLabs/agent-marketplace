---
title: Staff Permissions - Clients
category: staff
source: https://support.mindbodyonline.com/s/article/Staff-Permissions-Client-Permissions?language=en_US
source_updated: 2026-09-28
---
# Staff Permissions - Clients

Reference for the Clients checkboxes in a permission group: what each unlocks and its prerequisites. Use it when a staff login cannot see or edit client data, billing, autopays, contracts, documents or forms.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_staff.asp
- Menu path: **Settings > Staff Permissions** (or **Staff > Staff Permissions**), then pick the group.

## Settings & fields
"Base" = **Ability to view all clients** (lives under Sales Team Management); nearly everything below needs it.

### Client info
- **Add Client**: create clients from client search, Advanced Add New Client, Appointments, POS, class Sign In. No prereqs.
- **View client info**: all Client Info screens, Locker report, Documents link on appointments. Needs base.
- **Edit client info**: edit those screens and assign relationships. Needs base + View.
- **Edit client master list**: cross-regional (franchise) sites only; hidden otherwise.
- **Assign client indexes**: needs base, View, Edit.
- **Manage client suspensions**: set suspension start/end (Member Status); suspended clients cannot book online. Needs base, View, Edit, purchase history.
- **View client visit history**: Visits screen and Show Visits; Business app also needs View Client Info there and View entire appointment schedule.
- **View client schedule**: Schedule button/print; Business app needs View entire appointment schedule.
- **Administer client logins**: create client logins; needs base, View, Edit.
- **View client billing information**: last four digits, billing address, expiry; also allows card charges in the Business app. **Edit client billing information** needs it. Without either, staff can still save billing info at POS.

### Account, series, payments
- **View client account/purchase history**: Account Details and Purchases, receipts, PDFs (invoice PDFs also need Void/edit past sales and Account Balances & Invoices).
- **Edit client's series (duration/reassign payment)**: change pricing option duration; Reassign Payment under Show Visits; turning it off removes the "change" option on class sign-in. Needs base, View, Edit, purchase history.
- **Edit client's series count and session numbers**: same prereqs.
- **Override service category rules when reassigning payments**: move a visit to an unrelated purchase. Same prereqs.
- **Unassign client gift cards**: needs base, purchase history, Gift Card report permission.
- **Override cancel policy**: cancel past the window without a late fee (policies at Settings > More > Appointment Options / Class and Course Options). Needs all cancellation permissions.
- **Launch Sign-In Screen**: sign in class clients, mark appointments arrived; walk-ins also need Make reservations and View reservations.

### Autopay
- **View AutoPay schedule and history**: Autopay Schedule/History screens and Autopay Detail report. Needs base, View, Edit, purchase history.
- **Edit autopay details**: amount, location, payment method, contact. Needs base, View, purchase history. Sub-options: **Edit autopay schedule dates**, **Add New Autopays**, **Delete Existing Autopays** (no prereqs). Running autopays is under Payment Processing permissions.

### Contracts
- **Delete client contracts**: also removes associated autopay schedules.
- **Terminate client contracts**: keeps the autopay schedules.
- **Release contract deposits**.
- **Auto-renew and suspend contracts**: toggle auto-renew and handle suspensions.
- All four need base and purchase history.

### Documents and forms
- **View client documents**, **Add new client documents**, **Delete client documents**: need the Client Documents Upload feature on General Setup & Options (else the permission is hidden) and base; add/delete need View.
- **View/re-send forms**: needs Manage client forms (Settings). **Print/Download client forms**, **Delete client forms**, **Fill out client forms from profile** need View/re-send forms.

### Setup screens (no prereqs)
- **Required fields** (Settings > More > Required Fields): fields needed for consumer logins.
- **Set up client alerts** (alerts show to all staff once enabled).
- **Set up client types and client indexes**: also Courses roster indexes, Profile Custom Fields, Contract Options, Prospect Stages.
- **Set up referral types** (cannot assign referrals), **Set up relationship types** (cannot assign), **Set up client genders** (custom genders).
- **Access Messenger**: shows Messenger icon in top nav; staff without it can still log in to Messenger directly.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first: granting delete/terminate contract, autopay delete/add, unassign gift card, billing edits, or override cancel policy.
- Missing Ability to view all clients is the most common cause of a silently non-working client permission.
- Features depend on software package.

## Related
- [Staff Permissions - Settings](Staff-Permissions-Settings.md)
- [Staff Permissions - Appointments](Staff-Permissions-Appointment-Permissions.md)
- [Staff Permissions - Reports](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reports?language=en_US)
- [Staff Permissions - Classes & Courses](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reservation-Permissions?language=en_US)
- [Staff Permissions - Marketing](https://support.mindbodyonline.com/s/article/Staff-Permissions-Marketing?language=en_US)
- [Staff Permissions - Sales Team Management](https://support.mindbodyonline.com/s/article/Staff-Permissions-Sales-Team-Management?language=en_US)
- [Staff Permissions - Payment Processing](https://support.mindbodyonline.com/s/article/Staff-Permissions-Payment-Processing?language=en_US)
- [Staff permissions explained](203253743-Staff-permissions-explained.md)
