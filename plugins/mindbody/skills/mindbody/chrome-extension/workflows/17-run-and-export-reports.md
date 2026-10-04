---
workflow: Run and export reports and build a client contact list
safety: 🟢 Read-only (exporting or copying client lists only when the person asks)
---
# Run and export reports and build a client contact list

Run Sales, Attendance with Revenue, Payroll, Autopay and Retention reports for a date range, read the results, export to Excel, and, when asked, build a mailing or email list. Typical phrasings: "what were September sales?", "run payroll for the last two weeks", "how many new clients came back?", "export the autopay forecast", "get me an email list of active clients".

## Ask the person for
- **Which report** and the **date range** (the reports have different defaults, so always set dates explicitly). Also location if the site has several.
- **Output**: just a summary in chat, or an Excel export too.
- **For a client list**: Email, Mailing or Sales list; which clients (active, birthdays, first visit dates and so on); and opt-in status (for marketing, only clients subscribed to news and promos). Only build or export a list if the person clearly asked, and say what the export contains.

## Read first
- [Reports explained](../../articles/reports/203256053-Reports-explained.md) — how reports are organized
- [How to export reports to Microsoft Excel](../../articles/reports/203256023-Exporting-reports-to-Excel.md) — export icon and permissions
- [Sales report](../../articles/reports/203257193-Sales-Report.md) and [Attendance with Revenue](../../articles/reports/203257123-Attendance-with-Revenue-report.md)
- [Payroll report](../../articles/reports/203256603-Payroll-report.md)
- [Autopay Summary](../../articles/reports/203256403-Autopay-Summary-report.md) and [Autopay Detail](../../articles/reports/203256413-Autopay-Detail-report.md)
- [Retention report](../../articles/reports/203256863-Retention-report.md)
- [Mailing Lists report](../../articles/reports/203256833-Mailing-Lists.md) and [Export client email or mailing addresses](../../articles/reports/205027717-Export-client-email-or-mailing-addresses.md)

## Steps
1. **Set up the browser** — see [the general guide](../README.md). Open a new tab, confirm the site name.
2. **Open the report** — navigate to its direct link (or Insights > Reports and search the name):
   - Sales: https://clients.mindbodyonline.com/app/business/Report/Sales/Sales?category=Sales
   - Attendance with Revenue: https://clients.mindbodyonline.com/app/business/AttendanceReport
   - Payroll: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_ipay_new.asp
   - Autopay Summary: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_sum.asp?category=Paymentprocessing; Autopay Detail: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_det.asp
   - Retention: https://clients.mindbodyonline.com/app/business/asp/adm/adm_rpt_retention.asp?category=Clients
3. **Set the filters** — `read_page` (interactive) for refs, then `form_input` on legacy form fields. Set start/end dates (or Quick Dates), then report-specific choices: *Sales* View (summary or detail), Accounting Basis (accrual or cash), Autopays include/exclude; *Attendance with Revenue* View, Exclude no-shows; *Payroll* View (All staff - Summary or Detail) and note the default range is the last two weeks; *Autopay* Status and Payment method (Summary defaults to two months back and forward); *Retention* initial-visit range, service category, **Within N days**, Summary or Detail. Say out loud which accounting basis or view you used.
4. **Generate** — click **Go!** (or **Generate** for Payroll, Autopay, Retention). If nothing happens there were no records in the range. Wait about 2 seconds.
5. **Read it** — `get_page_text` and summarize the key totals and anything unusual. Quote numbers exactly as shown; values in parentheses are returns or deductions. Payroll shows only the first 80,000 visits; narrow the range if the data seems cut. For long tables, filter further instead of paging through screenshots.
6. **Export if asked** — find the **Export to Excel** icon (`find` "Export to Excel button") and click it. A file downloads in Chrome; tell the person it went to their Downloads folder (you cannot open it). No icon means that report cannot be exported. Needs the Export report information permission. Payroll and client-detail exports contain personal or pay data; mention that.
7. **Build a client contact list (only when asked)** — open https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_mailer.asp. Choose the list type (**Email**, **Mailing** or **Sales**), the **List clients** option (for example **Currently active**), **Client's Opt-in status** (choose a subscribed status for marketing use), **Clients Only / Prospects Only** if shown, and **Sort by**. Click **Generate**, then report the count. Use **Export to Excel**, or copy the addresses from the box (capped at 10,000). Do not paste client details into other sites. Never press **Tag New**, which replaces the existing tagged list.
8. **Close up** — close the tab you opened.

## Verify
- Confirm the dates and filters shown at the top of the result match what was asked (read them back from the page text).
- Sanity check: totals line up with the summary view, and the Sales cash-basis total should match Daily Closeout for the same location and range.
- Tell the person the exact range, view, basis, the headline numbers, and where any export was saved.

## If it goes wrong
- Report missing or blocked: permission or software package (each article lists the Reports permission, e.g. Autopay Reports, Marketing Reports, Analysis Reports).
- Retention instructor missing from the **With** menu: widen the dates, click **Generate**, reopen the menu.
- Export blank on Windows: disable Excel Protected View. Browser extensions can freeze exports.
- Autopay reports omit contracts auto-renewing in range and show only the next month-to-month autopay; say so when forecasting.
- Mailing list includes clients without emails when opt-in is "All Clients".

## Variations
- Client Directory list (under 1,000 clients, no export button): [How to create and export a list using the Client Directory](../../articles/reports/203259313-All-client-search.md).
- Active-client list: [Mailing list of all active clients](../../articles/reports/How-to-create-a-mailing-list-of-all-active-clients.md).
- Retention Management (TRP) export: [Retention Management report](../../articles/reports/203256853-Retention-Management-report.md); emailing it sends personal data outside Mindbody, so confirm first.
- Unpaid visits and cash drawer: see [playbook 16](16-end-of-day-closeout.md).
