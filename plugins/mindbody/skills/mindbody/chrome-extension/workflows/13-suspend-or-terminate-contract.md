---
workflow: Suspend or terminate a client contract
safety: 🔴 Money or irreversible
---
# Suspend or terminate a client contract

Freeze (suspend) or end (terminate) a client's autopay contract, and make clear what happens to future autopays. Typical phrasings: "freeze Maria's membership for two months", "pause Tom's contract while he's injured", "cancel Dana's membership", "stop her autopays after this month".

## Ask the person for
- **Client name** (and which contract if they have several).
- **Suspend or terminate?** If unsure: suspend = pause and resume, with missed autopays pushed to the end; terminate = ends it, removes future autopays and deactivates services now.
- **Suspend**: start date, and either a duration with unit (Days, Weeks, Months) or open-ended; any suspension fee; notes.
- **Terminate**: termination date, termination code and reason for Comments. Ask whether the client should keep access until their next billing date, since services stop at termination.
- Never choose Delete on your own. Delete is only for contracts sold in error; if the person says "delete", explain the difference and confirm they mean that.

## Read first
- [Suspending, terminating, deleting overview](../../articles/pricing-memberships/An-overview-of-suspending-terminating-and-deleting-contracts.md) — effects of each action
- [How to suspend a contract](../../articles/pricing-memberships/203258563-How-do-I-suspend-pause-freeze-a-contract.md) — suspension fields and limits
- [How to terminate or delete a contract](../../articles/pricing-memberships/203258533-How-do-I-terminate-or-delete-a-contract.md) — timing and undo
- [Client Account Details screen](../../articles/clients/215843418-Client-Account-Details-Screen-overview.md) — where the actions live
- [Client Autopay Schedule screen](../../articles/pricing-memberships/206026137-Autopay-Schedule-screen.md) — checking autopay dates afterward

## Steps
1. **Set up the browser** — follow [the general guide](../README.md). Confirm the site name.
2. **Open the client** — use the Find a client field at the top (`find` "Find a client search box", type the name, pick the right match; confirm with the person if several). Click **Account Details**.
3. **Locate the contract** — `get_page_text` on the Contracts section: note contract name, Start/End Date, Status, Auto Renewing?. Use **Show All Dates** if it is missing. Check the next autopay date on the Autopay Schedule (Contracts > **Autopays (x/x)**) so you know the timing.
4. **Check eligibility** — month-to-month contracts and contracts that run autopays "when the pricing options run out" cannot be suspended; the only route is terminate and resell later. Tell the person before going further.
5. **Suspend: open the form** — three-dot **Actions** icon on the contract > **Suspend**. Optionally pick a **Suspension Types** preset. Set **Start Suspension On**; set **Duration** and **Unit**, or tick **Open-ended suspension**; add **Suspension notes**; add a **Suspension fee** only if requested.
6. **Terminate: open the form** — Actions menu > **Terminate**. Enter the termination date, choose the termination code, and type the reason under **Comments**. The best date is the day before the next autopay so it does not run.
7. 🔴 **Stop** — show one summary and wait for an explicit yes in chat: client, contract, action, dates, fee if any, and the effect: *Suspend:* autopays pause and the missed ones move to the end (a 4-month pause on a 12-month contract adds 4 months); if "Scheduling suspensions" is enabled, booking privileges are suspended too. *Terminate:* all autopays on or after the termination date are removed, the contract's pricing options expire the day before, services deactivate, and a terminated month-to-month needs a new contract. Warn that Chrome may show a confirm box; ask the person to click OK if the page freezes (see the guide's dialog section).
8. **Commit** — click **Add Suspension** or **Terminate** (bottom right) only after the yes.
9. **Clean up if needed** — manually added autopays and declined autopays still queued are not removed by termination; look at the Autopay Schedule and report them. Remove them only with a separate yes (Remove Checked Transactions is its own 🔴 action).

## Verify
- Account Details > Contracts: Status shows Suspended or Terminated (with date); a suspension appears below the contract with **Unsuspend** and **Delete** options.
- Open **Autopays (x/x)**: suspended dates show Scheduled after suspension or Suspended; terminated contracts show no future autopays. Read with `get_page_text` and tell the person the next charge date.

## If it goes wrong
- Overlapping suspensions give an error; edit the existing one instead.
- A suspension set on the day of an autopay is likely too late (it probably ran that morning).
- Missing action or permission: needs "Auto-renew and suspend client contracts", "Terminate client contracts" (and "Delete client contracts"). Tell the person.
- Terminated by mistake: Actions > **Terminated from [date]** > **Cancel Termination** reinstates it, but missed autopays are not pushed out; disabled once the end date has passed. Needs its own 🔴 yes.
- If the terminate date passed and the contract auto-renewed, terminate both contracts.

## Variations
- Lift a suspension: use **Unsuspend** at the bottom of the contract details (🟡, confirm first).
- Stop auto-renewal only: clear **Auto Renewing?** on Account Details before the last autopay (see the Account Details page).
- Delete a contract: only for sales made in error; 🔴, irreversible, and purchased items need separate returns ([Returns, refunds and voids](../../articles/pos-payments/203259303-Returns-Refunds-and-Voids.md)).
- Find who deleted a contract: Autopay Detail report, status Deleted (see the terminate article).
