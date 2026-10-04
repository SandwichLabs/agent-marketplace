---
title: How to represent a staff member's pay if they are paid a flat weekly or monthly salary
category: staff
source: https://support.mindbodyonline.com/s/article/203270083-I-have-a-teacher-that-gets-paid-a-flat-weekly-monthly-salary-can-I-represent-that-in-the-system?language=en_US
source_updated: 2025-10-14
---
# How to represent a staff member's pay if they are paid a flat weekly or monthly salary

Mindbody has no native salary feature. Two workarounds make a salary show up on the Payroll report: a time-clock rate with manual punches, or a dummy zero-capacity "salary" class.

## Where in Mindbody
- Direct links: https://clients.mindbodyonline.com/app/staff ; https://clients.mindbodyonline.com/app/business/classdescription/list (Class & Course Management); https://clients.mindbodyonline.com/app/business/classic/admmainclass?fl=true (Class Schedule)
- Menu path: **Staff**; **Settings > Classic Setup > Class & Course Management**; **Classes**

## Steps
### Option A: salary as a time clock rate (only if the person has no hourly rate)
1. **Staff** > select the person > **Class Pay Rates** (shortcut bar).
2. Scroll to **Hourly Pay rates**; enter the salary amount in one of the tasks (create a new task if needed).
3. Manually enter a time clock punch every week/month (owner/managers with permission can use the Time Clock menu: Clock Others In/Out, View/Edit Time Clock).
4. The Payroll report then shows the salary.

### Option B: weekly/monthly salary class
1. **Staff** > person > **Class Pay Rates**; on any free **Class** pay rate set the **No Registration** amount to the salary figure; **Save**.
2. **Settings > Classic Setup > Class & Course Management** > **Add New**; create a class named "Weekly Salary" or "Monthly Salary" under any program/class type.
3. Click **Schedule this class**.
4. Set when: start/end times are irrelevant but required. Weekly: **Recurring class**, a day, end date far in the future. Monthly: **Single class**, one day; repeat as a new schedule every month.
5. Pick the staff member and the pay rate set up; no room needed.
6. Set all capacity fields (total, waitlist, online) to 0; click **Schedule Class**.
7. Hide it: **Classes** > click the salary class > uncheck **Show to public** > **Save**. Repeat for each instance.
8. The Payroll report shows the salary.

## Gotchas
- Option A needs manual punches each period or nothing is recorded.
- The hidden class still appears on the business-side schedule.
- Show to public must be unchecked per schedule instance.
- Monthly salary needs a new schedule every month.
- ⚠️ Financial — pay data feeds payroll; confirm with the user first.

## Related
- [Time Clock Tasks](https://support.mindbodyonline.com/s/article/203269913-Can-I-set-different-rates-for-different-tasks-on-the-time-clock?language=en_US)
- [How to manage time clock entries](How-to-manage-time-clock-entries.md)
- [How to clock in and clock out](https://support.mindbodyonline.com/s/article/How-to-clock-in-and-clock-out?language=en_US)
- [Class and course pay rates](203253623-Class-and-enrollment-pay-rates.md)
- [Flat fee for semi-private appointments](https://support.mindbodyonline.com/s/article/203275593-How-Can-a-Staff-Member-Get-Paid-a-Single-Flat-Fee-for-a-Semi-Private-Appointment-with-More-than-One-Client-Scheduled?language=en_US)
