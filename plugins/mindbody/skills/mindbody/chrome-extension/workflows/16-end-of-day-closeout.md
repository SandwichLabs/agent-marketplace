---
workflow: End-of-day closeout and cash drawer reconciliation
safety: 🟢 Read-only (🔴 only if the person asks you to click Close Out)
---
# End-of-day closeout and cash drawer reconciliation

Run the Cash Drawer and Daily Closeout reports, compare what Mindbody recorded with the physical drawer, and review unpaid visits. Typical phrasings: "do the end of day", "does the drawer balance?", "run closeout for today", "what's still unpaid from today's classes?".

You prepare the numbers; a person counts the cash. Do not make up counts. The default outcome is a reconciliation summary. Clicking **Close Out** locks the day's data and cannot be undone without Mindbody support, so it is a separate, explicitly requested step.

## Ask the person for
- **Date** (default today) and **location** if the site has several.
- The **counted cash**: total dollar value of each bill and coin in the drawer, from the person. If they have not counted, ask them to; stop there.
- **Starting cash** or **amount to keep in drawer** for tomorrow.
- Whether tips are paid out daily, and whether several staff or registers shared the drawer (then run the Cash Drawer report per shift).
- Whether they want the day **closed** after balancing.

## Read first
- [Daily Closeout report](../../articles/pos-payments/203257183-Daily-Closeout-report.md) — fields and close behavior
- [Cash Drawer report](../../articles/pos-payments/203257163-Cash-Drawer-report.md) — per date or per employee
- [How the Daily Closeout report balances the drawer](../../articles/pos-payments/203256313-What-report-will-help-me-balance-out-my-cash-drawer-at-the-end-of-the-day.md) — overview
- [Closing out drawers for different staff or shifts](../../articles/pos-payments/215682927-How-do-I-close-out-the-cash-drawer-for-different-staff-members-shifts.md) — shift routine
- [Unpaid Visits report](../../articles/reports/203256703-Unpaid-Visits-report.md) — what is still owed
- [Reconcile unpaid appointments](../../articles/reports/How-to-use-reports-to-reconcile-unpaid-appointments.md) — clearing them

## Steps
1. **Set up the browser** — see [the general guide](../README.md). Confirm the site name.
2. **Run the Cash Drawer report** — navigate to https://clients.mindbodyonline.com/app/business/Report/Sales/CashDrawer (Insights > Reports > Sales > Cash Drawer). Set **Start date** and **End date** (and times for a shift), **Location**, and **View**: **By Date**, or **By Employee** with **Entered By** when each person uses their own login. Optionally pick payment methods for individual summaries. Click **Go!** and read it with `get_page_text`. Note Total Received, Tips, In Drawer and Paid Out. Autopays do not appear here.
3. **Open Daily Closeout** — navigate to https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_dailycloseout.asp. Pick **Location**, and use **Use Date Range** for the day. Read cash sales, **Total cash expected in drawer**, check totals, and each payment-type section with `get_page_text`. Online sales are not included.
4. **Preview with the counted cash (does not commit)** — only if the person gave counts: click **Close Data**, enter dollar values for each bill and coin (the person's numbers, as stated), enter **Amount to keep in drawer**, then click **Preview Close Amounts**. Compare **Total cash expected in drawer** with **Actual cash counted in drawer** and report the over/short amount. To recount, edit amounts and preview again. Stop here unless asked to close.
5. **Investigate differences** — compare the Cash Drawer report by sale (Sale ID links open Manage Sales) for wrong payment type, wrong amount, missing sales, tips paid out, or voided test sales. Do not alter sales without a separate request (returns and voids are in [playbook 15](15-refund-return-or-void.md)).
6. **Review unpaid visits** — navigate to https://clients.mindbodyonline.com/app/business/Unpaidvisitsreport?category=Clients. Set **Start date/End date** (or **Select all dates**), tick **Include future unpaids** if wanted, choose **View** Summary or Detail, click **Go!**, and `get_page_text`. Summarize counts per client and service category. Do not use Tag new, which replaces the tagged list.
7. 🔴 **Close the day, only if asked** — Stop: show date, location, expected vs counted cash, over/short, amount kept in the drawer, and "after Close Out nothing for this range can be modified; reopening needs Mindbody support". Wait for an explicit yes. Then click **Close Out** and confirm the success message.

## Verify
- The preview shows no unexplained over/short, or the person accepts the stated discrepancy.
- After a close, **View Closed Data** (**Use Closed Data**) lists the closeout with the **Closed by** name and date.
- Give the person a short summary: cash expected, counted, over/short, check totals, unpaid visit count.

## If it goes wrong
- Reports missing or blocked: needs the Daily Closeout and Cash Drawer permissions and the right software package; tell the person.
- Cash Drawer shows no results: no sales in range, or the payment method lacks "Cash EQ" on Payment Methods.
- First-ever closeout: it absorbs all past sales as a baseline; void test sales first and enter no amounts, only the starting cash in **Amount to keep in drawer** (see the report page). Treat that Close Out as 🔴 too.
- Tips mismatch: the setting **Tips Included in Cash Drawer & Payroll** changes whether tips count in the drawer.
- Cannot split totals by drawer in Daily Closeout; use Cash Drawer per register.

## Variations
- Shift handoff only: run Cash Drawer **By Employee** per shift and skip Daily Closeout.
- Look at past closed days: **View Closed Data** on Daily Closeout.
- Save or export: **Export to PDF** or **Save this Report** on either report.
