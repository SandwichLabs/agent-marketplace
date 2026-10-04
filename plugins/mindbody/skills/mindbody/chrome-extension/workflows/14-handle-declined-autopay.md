---
workflow: Handle a declined autopay
safety: 🔴 Money or irreversible
---
# Handle a declined autopay

Find autopays that were declined, get the client's card updated, and re-run the failed charge. Typical phrasings: "which autopays declined this week?", "Sam's membership payment failed, fix it", "retry the declined autopays after he updates his card".

**Card details are never typed by you.** The person (or the client, in front of them) enters card number, expiry and any bank details directly into the Billing Information fields. You open the screen, tell them when to type, wait, and continue after they say it is done.

## Ask the person for
- The **client name**, or a date range if they want a list of all declines (default: the last 7 days).
- Whether the client has **a new card** ready, or whether you should only report and not fix.
- Confirmation that the person can enter the card details themselves. If not, stop after the report.

## Read first
- [Steps when an autopay is declined](../../articles/pricing-memberships/210310898-What-do-I-do-when-my-client-s-autopay-gets-declined.md) — the main sequence
- [Re-run a failed autopay with a new card](../../articles/pricing-memberships/204196313-How-do-I-re-run-a-failed-autopay-with-a-new-card.md) — two paths, converted or not
- [Update a client's billing information](../../articles/clients/203257913-How-do-I-update-my-clients-billing-information.md) — the card fields
- [Autopay Detail report](../../articles/reports/203256413-Autopay-Detail-report.md) — finding declines
- [Autopay Schedule screen](../../articles/pricing-memberships/206026137-Autopay-Schedule-screen.md) — running it
- [Autopay reports](../../articles/reports/203256393-Autopay-reports.md) — resubmit window

## Steps
1. **Set up the browser** — see [the general guide](../README.md). Confirm the site name.
2. **Find declines (🟢)** — navigate to https://clients.mindbodyonline.com/app/business/ASP/adm/adm_eft_det.asp (Insights > Reports > Payment Processing > Autopay Detail). Set **Start date** and **End date**, set **Status** to **Declined**, leave Location as All, then **Generate**. Needs the Autopay Reports permission. Read the table with `get_page_text` (Date, Client, Item, Billing Information, Amount, Status). Note a "Submitted" status separately: those need Mindbody Merchant Support, not a retry.
3. **Report and choose** — list the declines to the person and ask which client to fix. Mention Mindbody auto-resubmits declines for up to 7 days by default, so a retry may already be queued.
4. **Open the client's billing** — search the client, click **Client Info**, expand **Billing Information**. Use `read_page` to look at what is stored, but only read the card type, last digits and expiry shown; do not repeat full numbers anywhere.
5. **Hand over for card entry** — tell the person: "Please enter the new card details in Billing Information yourself (CC Number, CC Expiration, name and address) and tell me when done." Wait. Do not use `form_input` or `computer` type on card or bank fields. The person (or you, with their go-ahead) then clicks **Save**; if a name-mismatch alert appears, click **OK** only after the person confirms. Warn them it replaces the card currently on file, which later autopays will also use.
6. **Work out which case applies** — check Account Details for a negative balance from the failed autopay. Converted to negative balance: use Point of Sale > **Receive Payments** (step 8). Not converted: use the Autopay Schedule (step 7).
7. **Not converted: re-run the autopay** — Account Details > **Autopay Schedule**. On the failed row set **Payment method** to **Credit card**, tick the checkbox at the far right of that row. 🔴 Stop: show client, autopay date, amount, and the card type and last four digits now on file, and wait for an explicit yes. Then click **Run All Checked Transactions Now**. Needs the "Run autopays" permission. Only tick the one row.
8. **Converted: take the payment** — Point of Sale, search the client, click **Receive Payments**, **Continue**, and choose the credit card as **Payment Method**. 🔴 Stop with the same summary and amount owed; wait for yes before completing the sale. If the card must be keyed in at checkout, hand that field to the person.
9. **Alternative start** — you can instead tick the declined row in Autopay Detail and use **Run All Checked Transactions Now** (also 🔴, click **OK** on the confirm; warn about the native dialog per the guide).

## Verify
- Autopay Schedule or Autopay History for the client shows the transaction as accepted/successful, or the negative balance is cleared on Account Details.
- Re-run Autopay Detail for that client with Status Declined to confirm it is no longer listed. Report the result; if declined again, stop and tell the person to contact the client (decline codes are in the processor references).

## If it goes wrong
- Declined again: do not retry repeatedly; each run is a new charge attempt.
- Autopay Schedule not available or missing permissions: report which one (Run autopays, View AutoPay schedule, Edit client billing information).
- Contract paused after a decline: a declined autopay not converted to a negative balance pauses the contract until run successfully.
- Client is being terminated: delete queued declined autopays first, see [Terminate or delete a contract](../../articles/pricing-memberships/203258533-How-do-I-terminate-or-delete-a-contract.md).
- Failed ACH autopays automatically convert to the account (debit) payment method.

## Variations
- Only list declines: stop after step 3 (🟢).
- Cards about to expire: Autopay CC Expirations report, see [Autopay reports](../../articles/reports/203256393-Autopay-reports.md).
- Run an autopay with a different payment method on the row: use the **Payment Method** dropdown on the Autopay Schedule, confirm with 🔴 stop.
