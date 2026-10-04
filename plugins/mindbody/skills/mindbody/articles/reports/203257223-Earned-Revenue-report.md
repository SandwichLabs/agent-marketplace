---
title: Earned Revenue report
category: reports
source: https://support.mindbodyonline.com/s/article/203257223-Earned-Revenue-report?language=en_US
source_updated: 2023-12-14
---
# Earned Revenue report

Shows earned versus deferred revenue from pricing options sold, for limited, unlimited and membership options. Use it for deferred-liability and accrual-style revenue analysis; like the Outstanding Series report but not limited to limited-visit options.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/appshell/shuttle/ASP/adm/adm_rpt_earned_revenue.asp
- Menu path: **Insights > Reports > Sales > Earned Revenue**

## Steps
1. Open the report, set filters, click **Generate**.
2. Switch between **Detail view** and **Summary view**; optionally **Export to Excel**, **Tag New**/**Tag Add**/**Untag Clients**, **Save this report**, print.

## Settings & fields
- **Earned between**: start and end dates for revenue recognition.
- **Pricing options purchased at**: one location or all.
- **Sort by**: Payment Date, Expiration Date, Client Name, Earned Revenue Amount.
- **Tagged clients only**, **Service categories**.
- **Detail view**: per sale shows client (link to Account Details), payment ref #, sale date, expiration date, amount paid, duration, days used, days remaining, earned and deferred; totals for limited and unlimited sections.
- **Summary view**: sections Unlimited Visit Pricing Option, Membership Series, Limited Visit Pricing Option, Expired Series, Total; each with **Subtotal**, **Discount**, **Earned** (Subtotal minus Discount), grouped by Program (service category).
- Calculation: limited options earn by visits used; unlimited/membership by days active. Deferred = (paid / duration) x days remaining. Expired Series lists only unused sessions on options expiring in range (e.g. $100 10-session pass with 9 left shows $90).

## Gotchas
- Needs **Analysis Reports** permission; only on certain software packages.
- Earned revenue excludes sales tax.
- Membership options count as time-based even if limited: a non-membership 8-session $99 option earns about $12.37 per visit; a membership one earns about $3.30 per day active in the range.
- Unlimited liability swings with run date.
- To exclude past-dated rows with 0 remaining, sort by Expiration Date and export to Excel.
- For earned/deferred on returns, use the Outstanding Series report (Current Series Only, sort by Deferred Amount).

## Related
- [Outstanding Series report](https://support.mindbodyonline.com/s/article/203257103-Outstanding-Series-report-Outstanding-Pricing-Options-report?language=en_US)
- [Attendance with Revenue report](203257123-Attendance-with-Revenue-report.md)
- [Attendance without Revenue report](https://support.mindbodyonline.com/s/article/203256943-Attendance-No-Revenue-report?language=en_US)
- [Revenue by Class report](https://support.mindbodyonline.com/s/article/203257203-Revenue-by-Class-report?language=en_US)
- [Tagging clients](../clients/203256033-Tagging.md)
- [Exporting reports to Excel](203256023-Exporting-reports-to-Excel.md)
- [Save This Report](https://support.mindbodyonline.com/s/article/203255983-Save-This-Report?language=en_US)
- [Favorite reports](https://support.mindbodyonline.com/s/article/203256043-Favorite-reports?language=en_US)
- [Online sales by location in a datashare site](https://support.mindbodyonline.com/s/article/How-do-I-generate-a-report-for-online-sales-revenue-by-location-in-a-datashare-site?language=en_US)
- [Cross-Studio Revenue report](https://support.mindbodyonline.com/s/article/Corporate-Dashboard-Cross-regional-Transactions-Report?language=en_US)
- [Reports explained](203256053-Reports-explained.md)
