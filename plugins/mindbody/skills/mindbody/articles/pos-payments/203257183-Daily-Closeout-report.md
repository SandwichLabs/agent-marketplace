---
title: Daily Closeout report
category: pos-payments
source: https://support.mindbodyonline.com/s/article/203257183-Daily-Closeout-report?language=en_US
source_updated: 2026-09-14
---
# Daily Closeout report

Compares the cash you physically count in the register with what Mindbody recorded at the Point of Sale, then locks that day's sales data ("closes out"). Meant to be run daily; also shows past closed data.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_dailycloseout.asp
- Menu path: **Insights > Reports**, search "Daily Closeout" or go to **Sales > Daily Closeout**

## Steps
### First-time setup
1. Void any test sales first.
2. Click **Close Data**.
3. Do not enter dollar amounts; click **Preview Close Amounts**.
4. Enter the starting cash in **Amount to keep in drawer**.
5. Click **Close Out**. A message confirms the data is closed. This one closeout absorbs all past sales as the baseline.

### Daily
1. Click **Close Data**.
2. Count the register and enter the total dollar value (not quantity) for each bill and coin.
3. Click **Preview Close Amounts**.
4. Compare **Total cash expected in drawer** with **Actual cash counted in drawer**.
5. Enter what stays in the register in **Amount to keep in drawer**; set the rest aside for deposit. If tips are paid out daily, take those out now.
6. If there is no discrepancy, click **Close Out**.
7. To recount, edit the amounts at the top and click **Preview Close Amounts** again.

## Settings & fields
- **Start date/End date**, **Location** (close or view by location).
- **Use Date Range** (all data between dates) vs **Use Closed Data** (one specific closeout).
- **Closed by**: staff member logged in at closeout.
- **All staff members/Owner** filter.
- **Include Subcategories**: primary and secondary revenue categories (contract fees appear in a "fees" section).
- **Include Prepaid Gift Card Sales**.
- **View Closed Data** / **Close Data**, **Export to PDF**, **Save this Report**, **Print this Report**.
- Closed-data sections: Sales by Payment Type (cash-equivalent total matches the Sales report on cash basis for same location/range); Sales by Category (quantity sold and returned; counts visits by the pricing option's service category; a Service Program Performance section appears for date ranges); Merchant Account Processing (Approved and Settled, keyed and swiped; not for accounting, use payment processing reports and bank statements).
- Terms: Sales since last close, Sales tax since last close, Starting cash in drawer (previous keep amount), Cash sales, Cash tips/Tips paid out/Other tips, Total cash expected in drawer, Actual cash counted in drawer, Over/short amount, Amount to keep in drawer, Check sales, Actual check amount; other payment methods get their own sections.

## Gotchas
- ⚠️ Irreversible: after **Close Out** for a date or range nothing can be modified. Reopening a closed day requires contacting Mindbody support. Confirm with the user first.
- Needs the Daily Closeout permission (Reports). Availability depends on software package.
- Online sales are not included.
- Totals cannot be split by cash drawer; use the Cash Drawer report per register.
- A sale already closed out is not closed again if its date is later edited.
- Tips: **Tips Included in Cash Drawer & Payroll** (General Setup & Options, Retail Settings) enabled puts tips in Payroll and Cash Drawer reports; disabled moves them to Cash Drawer and Closeout (suits daily payout).
- With no-auth and merchant account both enabled, transactions are listed under the card brand chosen at sale.
- Deactivated service categories do not appear.
- Coin names can be changed via the Words and Phrases screen.

## Related
- [Daily Closeout report FAQ](https://support.mindbodyonline.com/s/article/203273603-Questions-about-the-Daily-Closeout?language=en_US)
- [How the Daily Closeout report balances the cash drawer](203256313-What-report-will-help-me-balance-out-my-cash-drawer-at-the-end-of-the-day.md)
- [Cash Drawer report](203257163-Cash-Drawer-report.md)
- [Words and Phrases screen](https://support.mindbodyonline.com/s/article/203259813-Words-and-Phrases-screen?language=en_US)
- [General setup options explained](../settings-navigation/203259783-General-setup-options-explained.md)
