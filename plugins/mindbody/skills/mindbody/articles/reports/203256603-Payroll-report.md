---
title: Payroll report
category: reports
source: https://support.mindbodyonline.com/s/article/203256603-Payroll-report?language=en_US
source_updated: 2026-09-24
---
# Payroll report

Shows what each staff member earned from classes, courses, appointments, hourly pay, tips and commissions, minus assistant and professional-product deductions. Use it when preparing staff pay or auditing a paycheck.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/ASP/adm/adm_rpt_ipay_new.asp
- Menu path: **Insights > Reports > Staff > Payroll**

## Steps
1. Open the report (link or menu above).
2. Pick a **View** and set the other filters, including start and end dates.
3. Click **Generate**.
4. Optionally use **Export to Excel**, **Export to PDF**, **Save this report** or **Print this report**.

## Settings & fields
- **View**: All staff members - Detail (default; per-service rows with pay rate, revenue, earnings, back bar charges); All staff members - Summary (per-staff totals); All staff members - Summary by Pay Rate; Paycheck Pickup (printable sign-off list of staff names); or a single staff member (detail).
- **Pay rates**: filter by a class/course pay rate. Appointment pay rates cannot be filtered.
- **Locations**, **Service categories** (Ctrl/Cmd-click for multiple), **Start date**, **End date**.
- **Hide client payment info**: for class/course instructors on percentage rates, hides revenue, revenue per session and per-client earnings.
- **Include inactive staff members**: adds deactivated staff; they then also appear in the View dropdown.
- **One staff member per page**: page break per staff for PDF export; not available in Summary view.
- **Show comp details**: breaks out comped visits by pricing option with client names and counts; no-shows and late cancels count as comps here.
- Quick dates: **Calendar Months**, **To-Date**, **Rolling Averages**.
- Key result columns: # Staff paid, # Staff unpaid (comps where staff got no pay, not the same as free pricing options), Base Pay, Assistant Pay, Bonus Pay, Earnings, Rev. per Session (appointments with percentage pay only: price divided by sessions, then the percentage applied), Hourly Pay, Tips, Commissions, Professional Products Charge, Net Earnings, Grand total.
- Detail view contents vary: flat/incremental/per-head class rates show client/comp counts and a roster link; percentage rates show pricing option and client names.
- A diamond icon marks a No Registrations Rate applied to a class (in Base Pay for flat rates, Earnings for percentage rates).
- Assistants show an Assistant icon by the class name; their earnings sit in Base Pay/Earnings. If the teacher pays the assistant, the assistant is hidden and a deduction appears in the instructor's Assistant Pay column.
- "Edit Class Pay Rates" / "Edit Appointment Pay Rates" links jump to the staff pay-rate screens. Changing a class's rate also requires assigning the new rate to the class.

## Gotchas
- Staff need a Reports permission: Payroll Report/Payroll Export/Tips/Assistant/Commission reports, either All Staff or "own only".
- Pay rates (class/course, appointment, hourly) must already be set up.
- Default date range is the last two weeks and cannot be changed as a default; edit the dates before generating.
- Only the first 80,000 visits are shown; narrow dates, staff or services if data seems missing.
- Tips only appear if **Tips Included in Cash Drawer & Payroll** is enabled in General Setup and Options.
- Deductions and negatives show in parentheses. Rounding is banker's rounding.
- Partial refunds reduce the tip proportionally: refund / (sale + tip) x tip. Example: $150 sale + $30 tip, $40 refund gives a $6.67 deduction.
- Add-ons booked with a primary appointment are not counted in # Services; standalone add-ons are.
- Class names link to the sign-in sheet, where attendance can be corrected.
- Availability depends on software package.
- For deeper detail use the Assistants, Time Clock, Tips or Commission reports.

## Related
- [Payroll Report Troubleshooting and FAQ](https://support.mindbodyonline.com/s/article/203257443-Payroll-Report-Troubleshooting-and-FAQ?language=en_US)
- [How to fix comps on the Payroll Report](https://support.mindbodyonline.com/s/article/207149227-How-to-fix-comps-on-the-Payroll-Report?language=en_US)
- [Tips](../pos-payments/203258723-Tips.md)
- [Commissions](https://support.mindbodyonline.com/s/article/207033637-Commissions?language=en_US)
- [Class and enrollment pay rates](../staff/203253623-Class-and-enrollment-pay-rates.md)
- [Hourly Pay Rates](https://support.mindbodyonline.com/s/article/203253723-Hourly-Pay-Rates?language=en_US)
- [How to set up appointment pay rates](https://support.mindbodyonline.com/s/article/206911487-How-to-set-up-appointment-pay-rates?language=en_US)
- [Professional products](https://support.mindbodyonline.com/s/article/203260073-Professional-products?language=en_US)
