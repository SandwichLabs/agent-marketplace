---
title: Autopay Detail report
category: reports
source: https://support.mindbodyonline.com/s/article/203256413-Autopay-Detail-report?language=en_US
source_updated: 2026-06-24
---
# Autopay Detail report

Per-transaction list of scheduled and processed autopays (default: today's), plus the place to manually run or delete scheduled autopays. Use for expected income snapshots and autopay status checks.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_det.asp
- Menu path: **Insights** > **Reports** > **Payment Processing** > **Autopay Detail**

## Steps
### Run the report
1. Open the report, choose filters, click **Generate**.

### Run or delete scheduled autopays
1. Generate the report.
2. Tick the checkbox for each transaction (**Check all | Uncheck all** helps).
3. Click **Run All Checked Transactions Now** or **Remove (Delete) Checked Transactions** at the bottom.
4. Click **OK** to confirm.

## Settings & fields
Filters
- **Start date**, **End date**, **Location** (All default; online store available), **Payment method** (All, Credit, Account).
- **Status**: All, **Scheduled**, **Declined** (counted in total), **Successful** (also shown for declined cards converted to negative balances if "Convert Declined Credit Card Autopays to Negative Account Balances after X Days" is on), **Deleted** (removed from schedule/report or contract terminated; deleted declined ones do not appear here), **Suspended** (excluded from the bottom total). Result-only statuses: **Submitted** (red; did not fully run, contact Merchant Support) and **Pending** (not settled).
- **Include autopays charged at POS** (clear to hide first-payment POS charges), **Only account autopays** (scheduled from Account Balances report), **Only Auto-renewing** (catch contracts before they renew and adjust terms/fees), **Tagged clients only**.
Result columns
- Date, Client, Phone #, Studio, Item, **Contract Associated** (Yes = in a contract; No = manually scheduled), Billing Information, Amount, Status.
- **Rows**: 500 default, selectable 100 or 1000 (not remembered); Previous/Next paging.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first: **Run All Checked Transactions Now** charges clients immediately; deletions remove scheduled payments. Deleting a month-to-month autopay removes ALL pending autopays on that client's account; to remove just one, use the client's Account Details autopay schedule.
- Needs the **Autopay Reports** permission.
- Includes inactive clients who still have autopays; omits dates after a contract's auto-renew (rerun after renewal); month-to-month contracts show only the next autopay.
- Ignores returns and refunds (a payment returned later still shows successful).
- Autopays for the same client, location, date and payment method are combined into one transaction to cut fees, displayed as one sale with line items.
- Some features depend on software package.

## Related
- [Autopay reports](203256393-Autopay-reports.md)
- [Autopay Summary report](203256403-Autopay-Summary-report.md)
- [Cancel or delete an autopay](https://support.mindbodyonline.com/s/article/203259533-How-to-cancel-or-delete-an-autopay?language=en_US)
- [Change autopay payment method](https://support.mindbodyonline.com/s/article/213812718-How-do-I-change-the-payment-method-of-a-client-s-autopay?language=en_US)
- [Add autopay schedule from Account Details](https://support.mindbodyonline.com/s/article/203894218-How-do-I-add-a-new-autopay-schedule-from-the-Account-Details-screen?language=en_US)
- [Terminate or delete a contract](../pricing-memberships/203258533-How-do-I-terminate-or-delete-a-contract.md)
- [General setup options explained](../settings-navigation/203259783-General-setup-options-explained.md)
