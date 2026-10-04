---
title: Refund and void guidelines (Mindbody Payments, All Regions)
category: pos-payments
source: https://support.mindbodyonline.com/s/article/Refund-void-guidelines-for-MINDBODY-Payments-US-Beta?language=en_US
source_updated: 2026-08-04
---
# Refund and void guidelines (Mindbody Payments, All Regions)

Rules for refunding card, bank-account, and alternative-payment sales processed through Mindbody Payments: what is supported, timing, and windows. Consult before issuing any refund.

## Where in Mindbody
- Menu path: client Purchases screen > Sale ID or Return/Void > refund flow (see Returns, Refunds and Voids article). Refunds also work in the Mindbody business app.

## Steps
### Interac card refund (Canada), after reaching the refund-method step
1. Choose **Issue refund to credit card** in the Refund method dropdown.
2. If asked, pick the reader that took the original payment (wrong reader gives an error; restart the refund).
3. Wait until the reader is ready, then insert the card.
4. On the reader choose checking or savings, then enter the PIN.
5. When both the site and reader confirm, remove the card and choose a receipt option.

### Interac partial refund
1. **Choose Refund Method > Issue refund to credit card** first (required for the split).
2. Set the refund amount to what goes to the card.
3. Tick **Use additional refund method?**, pick a second method, and adjust amounts so both total the original purchase.
4. Run the Interac steps above.

## Settings & fields
- **No voids**: Mindbody Payments offers refunds only. A refund reverses a settled transaction; refunds must go through the original merchant account/site.
- **Credit card**: full, line-item (once), and partial (once) refunds supported; no time limit but older cards may have changed details. Refund goes only to the original card; if that fails, refund to cash, check, or account.
- **Interac**: card must be physically present (else refund to cash/check/account). Full supported; line item not; partial only as a full refund split with another method. Identify Interac sales: card refund prompts card insertion; Transactions report Paid With shows Dipped; Payouts report fee is 0.15 CAD; Purchases screen shows "Visa/MC".
- **ACH (US)**: after settlement only (early attempt errors, try later); within 180 days; full, line-item, partial (each once).
- **PAD (Canada)**: wait 5-8 days after sale; within 180 days; same refund types.
- **SEPA (EU)**: wait 3-5 days; within 180 days; same.
- **Bacs Direct Debit (UK)**: wait 3-6 days; within 180 days; same.
- **BECS Direct Debit (AU, NZ)**: wait 3-6 days; within 90 days; takes at least 10 business days to settle; same types.
- **iDEAL | Wero (NL)**: refund immediately; full and partial (once); no line item.
- **Alternative methods** (Klarna, Apple Pay, Bancontact, TWINT, FPX, PayNow): only to original method or to account; no cash or split. Refund to account is instant and anytime. To original method: 180 days (FPX 60, PayNow 90), full and partial, 5-7 days (FPX up to 7 business days). Klarna partial refunds reduce the outstanding balance, and surplus is returned or the rest spread across remaining installments.

## Gotchas
- ⚠️ Irreversible / financial — confirm with the user first.
- Early refunds on bank debits can pay the account holder while the original payment later declines.
- Cardholders see funds in 5-10 business days.
- No refund fee, but original processing fees are not returned.
- Refunds come out of the pending payout; if larger than the balance, payouts pause until covered.

## Related
- [Returns, Refunds and Voids](203259303-Returns-Refunds-and-Voids.md)
- [Errors when issuing a refund](https://support.mindbodyonline.com/s/article/214108797-Why-do-I-keep-getting-an-error-when-trying-to-issue-a-refund?language=en_US)
- [Chargeback fees](MINDBODY-Payments-chargebacks-US-Beta.md)
- [Decline codes](https://support.mindbodyonline.com/s/article/MINDBODY-Payments-decline-codes-US-Beta?language=en_US)
- [Deposit times](https://support.mindbodyonline.com/s/article/Payout-reconciliation-and-deposit-times-for-MINDBODY-Payments-US-Beta?language=en_US)
- [Processing rates](https://support.mindbodyonline.com/s/article/What-are-my-MINDBODY-Payments-processing-rates-US-Beta?language=en_US)
- [Missing deposits](https://support.mindbodyonline.com/s/article/Why-am-I-not-receiving-my-MINDBODY-Payments-deposits-US-Beta?language=en_US)
- [Mindbody Payments FAQ](https://support.mindbodyonline.com/s/article/MINDBODY-Payments-account-FAQ-US-Beta?language=en_US)
- [Klarna FAQ](https://support.mindbodyonline.com/s/article/Klarna-FAQ-Mindbody-Payments-All-Regions?language=en_US)
- [Apple Pay FAQ](https://support.mindbodyonline.com/s/article/Apple-Pay-FAQ?language=en_US)
- [Transactions report](https://support.mindbodyonline.com/s/article/Transactions-report-for-MINDBODY-Payments?language=en_US)
- [Payouts report](https://support.mindbodyonline.com/s/article/Payouts-report-US-only?language=en_US)
