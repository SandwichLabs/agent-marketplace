---
title: Most frequently used Mindbody reports
category: reports
source: https://support.mindbodyonline.com/s/article/203814246-Top-Reports-requested-by-MINDBODY-clients?language=en_US
source_updated: 2026-02-18
---
# Most frequently used Mindbody reports

Digest of eight popular reports: what each is for, where it lives, and its filters. Use to pick the right report or find its URL.

## Where in Mindbody
- General path: **Insights** > **Reports**, then search the report name in "Search reports" and press Enter, or use the category path below.
- Direct links:
  - Daily Closeout: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_dailycloseout.asp (Sales > Daily Closeout)
  - Last Visit: https://clients.mindbodyonline.com/app/business/LastVisitReport (Clients > Last Visit)
  - Sales: https://clients.mindbodyonline.com/app/business/Report/Sales/Sales?category=Sales (Sales > Sales)
  - Payroll: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_ipay_new.asp (Staff > Payroll)
  - Cancellations: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_tlbx_advcanc_rest.asp (Clients > Cancellations)
  - Attendance with Revenue: https://clients.mindbodyonline.com/app/business/AttendanceReport (Sales > Attendance with Revenue)
  - Autopay Detail: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_det.asp (Payment Processing > Autopay Detail)
  - Retention: https://clients.mindbodyonline.com/app/business/asp/adm/adm_rpt_retention.asp (Clients > Retention)

## Reports
### Daily Closeout
Compares POS-recorded cash for a day/range against the actual cash counted; if they match, close the data and bank it. Mismatches mean wrong collection, wrong payment type chosen, or missing money.
- **Include Subcategories** checkbox shows primary and secondary revenue categories.
- **View Close Data**: lists previously closed days. **Close Data**: starts closing (asks for cash currently in register).
- ⚠️ Irreversible: a closed range cannot be adjusted.

### Last Visit
Shows clients' most recent visits; complements Retention and No-Return reports. Filters: **List Clients Whose Last Visit Was On/Before**, **Who Took (number) or More Sessions**, **Between** / **And** date window, **Sales Rep**, **All Locations**, **Sort By** (Client Name or # of visits), **Include Inactive Clients**.

### Sales
Lists every sale, with breakdowns by employee, category, and location. Defaults to accrual basis first time, then remembers the last basis used. Cash basis adds a Deposits section at the bottom (account payments and assignable gift cards: original price and remaining balance). Prepaid gift card purchases appear in the non-deposits section.

### Payroll
Staff earnings from class/appointment pay rates, including assistant pay (the Assistants report gives assistant-only detail). Filters: **View** (staff), **Service Categories (Programs)**, **Pay Rates**, **Start Date**, **End Date**, **Locations**, **Include Inactive Instructors**, **One Teacher Per Page?** (tick it, click **Generate**, then the print icon), **Show Comp Details** (lists comped clients/visits per pricing option; a comp = visit on a pricing option where "Does teacher get paid for this client?" is No).

### Cancellations
Lists cancelled appointments, courses, and classes, who cancelled, and allows restoring the booking (undo). Filters: **Start Date**, **End Date**, **Studios**, **All Teachers**, **All** / **All Late Cancels** (client still charged) / **All Early Cancels** (not charged), **View All** (consumer-site vs business-site cancels), **Restore** (group vs individual cancels), **Sort By** (original appointment date or cancellation date), **Client's All** / **Client Selected**.

### Attendance with Revenue
Gross revenue per visit (e.g. $45 5-visit pass gives $9 per visit). Handy for debugging Payroll (checking if a pricing option does not pay the teacher). Filters: **[No Revenue]** (switches to the Attendance without Revenue report), **Start Date**, **End Date**, **Used at** (defaults to main location), **Purchased by** (defaults to all locations), **Staff member** (only staff with activity in range are listed), **Start Time**, weekday checkboxes (all on by default), **Visit service category**, **Payment Service Category** (Ctrl/Cmd for multi-select), **Payment Method** (one at a time), **View** (class, staff member, date, service category, class type, roll sheet, or summary).

### Autopay Detail
Snapshot of scheduled autopays (default: today's). Columns include date, client, phone, location, item, card info, amount, status. The **Run Checked Now** button at the bottom can run autopays. Shown by scheduled date even if settled later; ignores returns/refunds afterward; unsettled ones show as pending. Not a sales report.

### Retention
Share of clients with an initial visit in a period who return. Filters: **Initial Visit To** (location), **Initial Visit between** (default: one-month window starting three months back; **Quick Date** available), **Service Category** (then pricing option), **With** (initial-visit instructor; only staff with initial visits in range appear), **Client Returned to** (location), **Within "X" days**, **With** (Any Instructor / The Same Instructor), **Repeat Clients Based on** (Any/Same Instructor x Any/Same Location combos), **View** (Detail with names or Summary with percentages only).

## Gotchas
- Report availability depends on software package and staff permissions (Staff Permissions - Reports).
- Reports can be exported to Excel.

## Related
- [203256053-Reports-explained](203256053-Reports-explained.md)
- [203257183-Daily-Closeout-report](../pos-payments/203257183-Daily-Closeout-report.md)
- [203256823-Last-Visit-report](203256823-Last-Visit-report.md)
- [203256013-Accrual-vs-cash-accounting](https://support.mindbodyonline.com/s/article/203256013-Accrual-vs-cash-accounting?language=en_US)
- [203256603-Payroll-report](203256603-Payroll-report.md)
- [203256513-Assistants-report](https://support.mindbodyonline.com/s/article/203256513-Assistants-report?language=en_US)
- [203256893-Cancellations-report](https://support.mindbodyonline.com/s/article/203256893-Cancellations-report?language=en_US)
- [203257123-Attendance-with-Revenue-report](203257123-Attendance-with-Revenue-report.md)
- [203256943-Attendance-No-Revenue-report](https://support.mindbodyonline.com/s/article/203256943-Attendance-No-Revenue-report?language=en_US)
- [203256413-Autopay-Detail-report](203256413-Autopay-Detail-report.md)
- [203256863-Retention-report](203256863-Retention-report.md)
- [203253563-Adding-service-categories](../pricing-memberships/203253563-Adding-service-categories.md)
- [Staff-Permissions-Reports](https://support.mindbodyonline.com/s/article/Staff-Permissions-Reports?language=en_US)
- [203256023-Exporting-reports-to-Excel](203256023-Exporting-reports-to-Excel.md)
- [207342557-Which-reports-do-I-have-access-to-Software-Levels-Full-Breakdown](https://support.mindbodyonline.com/s/article/207342557-Which-reports-do-I-have-access-to-Software-Levels-Full-Breakdown?language=en_US)
- [204416573-Common-Reports-used-for-business-data-backup](https://support.mindbodyonline.com/s/article/204416573-Common-Reports-used-for-business-data-backup?language=en_US)
