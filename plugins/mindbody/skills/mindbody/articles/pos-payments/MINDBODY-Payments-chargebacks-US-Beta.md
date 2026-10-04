---
title: Chargeback fees (Mindbody Payments, All Regions)
category: pos-payments
source: https://support.mindbodyonline.com/s/article/MINDBODY-Payments-chargebacks-US-Beta?language=en_US
source_updated: 2026-08-26
---
# Chargeback fees (Mindbody Payments, All Regions)

Reference for the fee Mindbody Payments charges per dispute (chargeback), by country and payment type, and how each type shows up in the software. Use when a failed or disputed payment appears.

## Where in Mindbody
- Disputes tool (Mindbody Payments); Transactions report; Payouts report; client Account Details and Purchases screens; Account Balances report.

## Settings & fields
### Credit card fee per dispute
- US $15; Canada 25 CAD; UK 25 GBP; Australia 25 AUD; New Zealand 30 NZD; Switzerland 25 CHF; EU 20 EUR (currently charged at 10 EUR, see SEPA below); Denmark 150 DKK; Norway 200 kr; Sweden 290 SEK; Poland 100 PLN; Romania 100 RON; Bulgaria 40 BGN; Czech Republic 525 Kc; Hungary 7200 Ft; Malaysia 90 RM; Mexico 150 MXN; UAE 80 AED.

### Bank account methods
- **ACH (US)**: no fee. Clients usually have 60 days. Covers client disputes and bank returns (insufficient funds, bad account details). Money goes back to the account holder with no recourse. Shows as negative balance, caution icon on Account Details (hover for reason), "Returned (Failed)" in Transactions report, refund in Payouts report. No need to contact Mindbody; monitor with Account Balances report, then collect or terminate related contracts.
- **Bacs Direct Debit (UK)**: 25 GBP. Disputes allowed at any time; no recourse.
- **BECS Direct Debit (AU, NZ)**: 25 AUD / 30 NZD. Clients typically up to seven years; no recourse.
- **PADs (Canada)**: 25 CAD. Up to about 90 days depending on bank; no recourse.
- **SEPA and credit card (EU)**: 10 EUR flat for every dispute, since Mindbody cannot yet tell bank rejections from client chargebacks. Window about eight weeks to 13 months. Cannot be challenged or reversed. Shows as negative balance, FAILED on Account Details, "FAILED SEPA" with Account payment method on Purchases, declined/returned in Transactions, "Chargeback" in Payouts. Follow up with client, delete related contracts if needed, and process a returned check to create a balance owed if the system has not.
- For ACH/Bacs/BECS/PADs/SEPA, recover money by working with the client and recharging if appropriate.

### Alternative payment methods
- **Klarna**: 20 EUR; 180-day dispute window; Klarna handles fraud/non-repayment itself; Mindbody notifies about other dispute types.
- **TWINT (Switzerland)**: 25 CHF; Mindbody notifies and helps respond.
- **iDEAL | Wero (Netherlands), Bancontact (Belgium), FPX (Malaysia), PayNow (Singapore)**: no fee; payments cannot be reversed, so no dispute monitoring needed. For PayNow, still work with clients who ask for a refund.

## Gotchas
- Disputes from Marketing Suite transactions trigger email notices; respond promptly with requested info.
- A card chargeback won in the Disputes tool shows status "Won"; funds and the fee come back with the next deposit.
- ⚠️ Irreversible / financial — confirm with the user first before terminating contracts or recharging clients.

## Related
- [Mindbody Payments chargebacks quick guide](https://support.mindbodyonline.com/s/article/Mindbody-Payments-chargebacks-quick-guide?language=en_US)
- [Disputes tool](https://support.mindbodyonline.com/s/article/The-Mindbody-Payments-Disputes-tool?language=en_US)
- [Evaluate and challenge disputes](https://support.mindbodyonline.com/s/article/How-to-evaluate-and-challenge-disputes-Mindbody-Payments?language=en_US)
- [Processing rates overview](https://support.mindbodyonline.com/s/article/What-are-my-MINDBODY-Payments-processing-rates-US-Beta?language=en_US)
- [Chargebacks FAQ](https://support.mindbodyonline.com/s/article/203255573-Chargebacks-FAQ?language=en_US)
- [Mindbody Payments FAQ](https://support.mindbodyonline.com/s/article/MINDBODY-Payments-account-FAQ-US-Beta?language=en_US)
- [Transactions report](https://support.mindbodyonline.com/s/article/Transactions-report-for-MINDBODY-Payments?language=en_US)
- [Payouts report](https://support.mindbodyonline.com/s/article/Payouts-report-US-only?language=en_US)
- [Account Balances report](https://support.mindbodyonline.com/s/article/203256673-Account-Balances-report?language=en_US)
- [Terminate or delete a contract](../pricing-memberships/203258533-How-do-I-terminate-or-delete-a-contract.md)
- [Bounced checks](https://support.mindbodyonline.com/s/article/203259253-Bounced-checks?language=en_US)
- [Klarna FAQ](https://support.mindbodyonline.com/s/article/Klarna-FAQ-Mindbody-Payments-All-Regions?language=en_US)
