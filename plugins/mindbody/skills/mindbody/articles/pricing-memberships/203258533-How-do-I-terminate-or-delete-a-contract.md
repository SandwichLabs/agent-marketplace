---
title: How to terminate or delete a contract
category: pricing-memberships
source: https://support.mindbodyonline.com/s/article/203258533-How-do-I-terminate-or-delete-a-contract?language=en_US
source_updated: 2026-07-01
---
# How to terminate or delete a contract

How to end a client's contract (terminate), undo a termination, or remove a contract entirely (delete), plus timing rules that avoid surprise charges.

## Where in Mindbody
- Menu path: client profile > Account Details > Contracts > three-dot Actions menu

## Steps
### Terminate
1. Open the client's **Account Details** (use **Show all dates** if the contract is hidden).
2. Three-dot menu on the contract > **Terminate**.
3. Enter the termination date, choose a termination code (defined on the Contract Options screen), add a reason under **Comments**.
4. Click **Terminate** (bottom right).

### Undo a termination
1. Account Details > three-dot menu > **Terminated from [date]**.
2. Click **Cancel Termination**. Contract and remaining autopays are reinstated (missed autopays are not pushed out).

### Find who deleted a contract
1. Tag the client.
2. Run the Autopay Detail report with **Tagged clients only**, Start Date today, End Date two or more months ahead, Status **Deleted**, then **Generate**.

## Gotchas
- Required Clients permissions: Delete client contracts, Terminate client contracts, Auto-renew and suspend client contracts.
- Termination removes autopays on/after the termination date and active pricing options from that contract. Pricing options expire one day before the termination date.
- Best timing: terminate the day before the next autopay so it does not run. Terminating earlier cuts off access; extend the current pricing option if the client should keep access.
- An autopay that runs between entering the termination and its date leaves that pricing option with its original expiry.
- Cancel Termination is disabled (grayed) once the contract end date has passed; resell instead.
- Termination date carries across auto-renewals; if the final payment already ran and the contract renewed, terminate both contracts.
- Terminating a suspended contract deletes the suspension.
- Declined autopays scheduled before termination may still be retried if resubmission is enabled; delete them on the Autopay Schedule screen first.
- Manually added autopays are not removed; check the Autopay Schedule afterward.
- Month-to-month contracts cannot be suspended; terminate and resell.
- ⚠️ Irreversible / financial — confirm with the user first: terminating a contract (access removed, autopays deleted) and especially deleting one (cannot be undone; purchased items need separate return/void). Delete only contracts sold in error.

## Related
- [Suspending, terminating, deleting overview](An-overview-of-suspending-terminating-and-deleting-contracts.md)
- [Suspend a contract](203258563-How-do-I-suspend-pause-freeze-a-contract.md)
- [Contracts FAQ](https://support.mindbodyonline.com/s/article/203274453-Facts-About-Contracts-Options-Settings-Changes-Modifications-and-More?language=en_US)
- [Cancel or delete an autopay](https://support.mindbodyonline.com/s/article/203259533-How-to-cancel-or-delete-an-autopay?language=en_US)
- [Contract Options screen](https://support.mindbodyonline.com/s/article/203259763-Contract-Options-screen?language=en_US)
- [Extend a customer's pricing option](https://support.mindbodyonline.com/s/article/203276103-How-do-I-extend-a-customer-s-pricing-option?language=en_US)
- [Resubmit declined autopay days](https://support.mindbodyonline.com/s/article/204064406-How-do-I-change-the-number-of-days-to-resubmit-a-declined-autopay?language=en_US)
- [Autopay Detail report](../reports/203256413-Autopay-Detail-report.md)
- [Autopay Schedule screen](206026137-Autopay-Schedule-screen.md)
- [Tagging clients](../clients/203256033-Tagging.md)
- [Manage active and inactive client profiles](../clients/203257863-How-do-I-delete-deactivate-a-client.md)
