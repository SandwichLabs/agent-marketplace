---
title: Commonly used smart lists (Marketing Suite)
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/Smart-Lists-Most-Commonly-Used-Guide?language=en_US
source_updated: 2026-08-28
---
# Commonly used smart lists (Marketing Suite)

Cookbook of ready-made smart list recipes (filter combinations) for common audiences. Use it to pick the filters when building a smart list to feed a campaign or automation.

## Where in Mindbody
- Menu path: **Marketing > Marketing Suite** > smart lists (creation steps are in the Creating Smart Lists article).

## Settings & fields
Recipes, grouped by filter type (wording paraphrased):

### Contact Field filters
- Upcoming birthdays: **Birth Date is within** N days.
- No birth date: **Birth Date is blank**.
- Prospects by stage: **Is Prospect is Yes** and **Prospect Stage Name is** a stage.
- Client index set (any value): index field (e.g. Age Range) **is not blank**; specific value: index field **is** value.
- Leads by stage / channel / rep: **Lead Stage is**, **Lead Channel is**, **Lead Sales Rep is**.

### Interaction History filters
- Visited a service category: Contacts who **have booked appointment** with **service category name is** X.
- Booked a class/appointment: **have booked appointment** with **service name is** X.
- Specific course: **have purchased** with **description is** course name and **have visited** with **class name is** X (course must have met at least once).
- Visited a staff member: **have visited** with **calendar name is** staff name.
- First-time bookers: have booked with **start at** after 7 days ago and have not booked with start at before 7 days ago.
- Completed first visit: have visited, **minimum occurrences** 1 and **maximum occurrences** 1, **status** any of Signed-In, Completed.
- Leads never visited: have not visited and **contact created** occurred within N days.
- At least one visit (or future booking): have booked with start at before 0 days ago.
- Milestone visit: have visited with status Signed-In/Completed, min and max occurrences both N.
- First visit with a given pricing option: have visited with **product id** and **first occurred within** N days.
- Not booked recently: have not booked with start at after N days ago. No recent visit: have not visited, **occurred within** N days.
- Visited on an active pricing option: pricing option name, maximum occurrences, start at, status.
- Active contract: have purchased with **contract is Yes** and last occurred within N days.
- No contract: have not purchased with description any of named contracts.
- Recent intro offer: have purchased with **product external id** and first occurred within N days. Intro offer but no visit: purchased intro offer and have not booked.
- Purchased specific option(s): have purchased with description any of (multiple allowed). Purchased but never visited: purchased plus have not visited. Purchased and visited at least N: purchased plus visited with min occurrences. Not purchased: have not purchased with product external id.
- Cross-sell: purchased a drop-in (product external id) and have not purchased a given contract.
- No recent purchase: have not purchased, occurred within N days.
- Opened a campaign recently: **have opened email**, **source type is Campaign**, last occurred within N days.
- Clicked a URL: **have clicked link** with **url is** address.

### Contact List filter
- Not in an existing list: Contacts who are **not in** a chosen list (e.g. not in "Visited in the last day").

## Gotchas
- Needs permission **View and manage the Marketing tab**; features depend on package.
- When filtering by pricing option, prefer **Product External ID** over name.
- Recipes can be duplicated and edited; adjust numbers to fit your business.

## Related
- [Creating smart lists](Creating-Smart-Lists-Frederick.md)
- [Setting up campaigns](Setting-up-Campaigns-Frederick.md)
- [Creating automations](Creating-automations-Frederick.md)
- [Contact field filters](https://support.mindbodyonline.com/s/article/Contact-Field-Filters-Marketing-Suite?language=en_US)
- [Interaction History filters](https://support.mindbodyonline.com/s/article/Interaction-History-Filter?language=en_US)
- [Contact list filters](https://support.mindbodyonline.com/s/article/Contact-List-Filter-Marketing-Suite?language=en_US)
- [Operators for smart lists](https://support.mindbodyonline.com/s/article/Marketing-Suite-Operators-for-Smart-Lists?language=en_US)
- [Copy campaigns, automations, smart lists](https://support.mindbodyonline.com/s/article/Can-I-copy-a-campaign-Marketing-Suite?language=en_US)
- [System lists](https://support.mindbodyonline.com/s/article/Understanding-system-lists-Marketing-Suite?language=en_US)
- [Prospect Stages](https://support.mindbodyonline.com/s/article/206176457-Prospect-Stages?language=en_US)
- [Why isn't this feature available](../settings-navigation/Why-isn-t-this-feature-available.md)
