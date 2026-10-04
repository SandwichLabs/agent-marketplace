---
title: Cash Drawer report
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203257163-Cash-Drawer-report?language=en_US
source_updated: 2026-09-29
---
# Cash Drawer report

Breaks sales down by payment method, by date or by employee, so the register can be counted and balanced at end of shift or day. Usually paired with the Daily Closeout report.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/Report/Sales/CashDrawer
- Menu path: **Insights > Reports > Sales > Cash Drawer** (also under the **Administrative** filter on the Sales reports screen)

## Steps
1. Open the report.
2. Set **Start date** and **End date** (and optionally times).
3. Pick the **View**: **By Date** (ignores who rang the sale) or **By Employee** (grouped by date, then employee).
4. Optionally choose payment methods under "Display individual summaries for the following payment methods".
5. Click **Go!**.

## Settings & fields
- **Start time** / **End time**, **Quick Dates**, **Show tagged clients only**.
- **Location**: multi-select, includes online store; default All Locations.
- **Entered By**: per-employee view; requires each employee to use their own login for every sale.
- **Cash register**: only appears with multiple cash drawers set up.
- Individual summaries: each selected payment method gets its own Total Sales and Grand Total columns; unselected ones fall into Other.
- Buttons: **Go!**, **Print this report**, **Export to Excel**, **Export to PDF**, **Save this report**, **Tag add**, **Tag new**, **Untag clients**.
- Result columns: Client (link to Client Info), Sale ID (link to Manage Sales), Location, Notes/Check # (notes only if the payment method has Pay Notes enabled), Payment Amount.
- Totals: Total Sales per date, Grand Total at the bottom, Total column far right. Credit includes keyed, swiped and no-auth. Other includes custom methods (Trade, Room Charge) and ACH.
- Cash-balancing rows: Total Received, Tips, In Drawer (Total Received plus Tips), Paid Out (tips paid out).

## Gotchas
- Needs one of: Cash Drawer - Run for current date, or Cash Drawer - Run for date range. Availability depends on software package.
- Tips need the **Tips** setting on General Setup & Options. **Tips Included in Cash Drawer & Payroll** enabled puts tips in the In Drawer total; disabled shows them as Paid Out and excludes them.
- Autopays are not shown; use the Autopay Detail report.
- Payment methods without "Cash EQ" selected on the Payment Methods screen do not appear.
- No results on **Go!** means no sales in that range.
- Checkbox and radio choices are remembered per login.
- The Constant Contact button was retired June 1, 2020.

## Related
- [Daily Closeout report](203257183-Daily-Closeout-report.md)
- [Cash drawer troubleshooting FAQ](https://support.mindbodyonline.com/s/article/213570018-Cash-Drawer-questions-and-troubleshooting?language=en_US)
- [How do I close out the cash drawer for different staff members/shifts](215682927-How-do-I-close-out-the-cash-drawer-for-different-staff-members-shifts.md)
- [Electronic Cash Drawer - WASP (PC)](https://support.mindbodyonline.com/s/article/203254673-Electronic-Cash-Drawer-WASP-PC?language=en_US)
- [Electronic Cash Drawer - WASP (Mac)](https://support.mindbodyonline.com/s/article/203254733-Electronic-Cash-Drawer-WASP-Mac?language=en_US)
- [How do I set up multiple cash drawers](https://support.mindbodyonline.com/s/article/203274233-How-do-I-set-up-multiple-cash-drawers?language=en_US)
- [Payment Methods screen](203259823-Payment-Methods-screen.md)
- [Autopay Detail report](../reports/203256413-Autopay-Detail-report.md)
