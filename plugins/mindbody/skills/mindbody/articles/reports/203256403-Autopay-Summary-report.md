---
title: Autopay Summary report
category: reports
source: https://support.mindbodyonline.com/s/article/203256403-Autopay-Summary-report?language=en_US
source_updated: 2026-09-03
---
# Autopay Summary report

Day-by-day totals of scheduled and processed autopays with projected value, used for budget forecasting and reviewing autopay revenue. Default window is the last two months plus the next two.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_sum.asp?category=Paymentprocessing
- Menu path: **Insights** > **Reports** > **Payment Processing** > **Autopay Summary**

## Steps
1. Open the report, set filters.
2. Click **Generate**.
3. Click a Scheduled Autopay Date link to open the Autopay Detail report for that day.

## Settings & fields
Filters
- **Start date**, **End date**; **Location** (online store, one location, or All locations default); **Payment method** (All default, Credit card, Account, ACH, ApplePay, GooglePay; depends on enabled methods); **Type** (All or one service category).
- Quick dates: **Calendar Months** (last completed period), **To-Date** (period start through today), **Rolling Averages** (last 365/90/30/7 days).
- **Tagged clients only**; **Include Autopays Charged at POS** (clear to show only scheduled/processed autopays).
- Buttons: **Generate**, **Tag add** (append shown clients to the tagged list), **Tag new** (replace the tagged list; does not delete clients), **Print this report**.
Result statuses
- **Not submitted - Scheduled** (not yet run, projected amount), **Not submitted - Suspended** (account on hold, deferred amount), **Submitted - Successful** (run, settled, batched), **Submitted - Declined** (uncollected), **Submitted - Pending** (not yet settled), **Total** per day. Bottom row gives total count and amount of scheduled autopays.

## Gotchas
- Needs the **Autopay Reports** permission.
- Excludes contracts that auto-renew within the range (appear after renewal) and month-to-month contracts in the forward forecast.
- Totals exclude tax; use Autopay Detail for tax amounts.
- Tag new overwrites the existing tagged clients list.
- Report availability depends on software package.

## Related
- [Autopay reports](203256393-Autopay-reports.md)
- [Autopay Detail report](203256413-Autopay-Detail-report.md)
- [Favorite reports](https://support.mindbodyonline.com/s/article/203256043-Favorite-reports?language=en_US)
- [Icons and date filters](https://support.mindbodyonline.com/s/article/203254263-Icons-and-date-filters?language=en_US)
- [Tagging](../clients/203256033-Tagging.md)
- [Printing reports](https://support.mindbodyonline.com/s/article/203256003-Printing-reports?language=en_US)
- [Reports available per package](https://support.mindbodyonline.com/s/article/207342557-Which-reports-do-I-have-access-to-Software-Levels-Full-Breakdown?language=en_US)
