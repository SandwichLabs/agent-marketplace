---
title: General Setup & Options screen: Client Management
category: clients
source: https://support.mindbodyonline.com/s/article/General-Setup-Options-screen-Client-Management?language=en_US
source_updated: 2026-09-28
---
# General Setup & Options screen: Client Management

Reference for every toggle in the Client Management section of General Setup & Options. Many client features (alerts, documents, prospects, suspensions, negative balances) only appear after a setting here is turned on.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_setup.asp
- Menu path: Settings > General > General Setup and Options > expand **Client Management** (Expand All / Collapse All at top right; click **Update** to save before leaving).
- Visible settings depend on package and on other settings (turning one off can hide dependents).

## Settings & fields
Account balance and purchasing:
- **Account Purchases - Allow All Clients**: on = anyone may charge to account; off = only clients individually granted in the Member status section of Client Info. Does not allow negative balances by itself.
- **Account Purchases - Allow All Clients in Consumer Mode**: online store may use account credit; needs the setting above or individual permission.
- **Allow Client Negative Balances**: purchases on account without funds (business site).
- **Allow Client Negative Balances in AutoPays**: debt only from autopays.
- **Allow Client Negative Balances in Consumer Mode**: only in countries without credit card processing.
- **Apply Client Account Payments by Location**: balances are per location instead of combined.
- **Automatically Reconcile Unpaids**: after a cancellation the freed session pays the next unpaid visit; an earlier new booking can turn the oldest paid visit into unpaid.

Lookup and display:
- **Auto Select Client** (single match opens Client Info), **Lookup Clients - Search All Clients** (include inactive), **Lookup Clients by All Locations** (needs "View all locations in Client Lookup" permission), **Client History Windows - Default** (months, up to 60; affects Account Details, Purchases, Contact Logs, Visits, and how far ahead Schedule shows), **Purchase History - Default** (detailed vs summary), **Schedule Display** (Weekly/Monthly client schedule), **Show Membership Summary in Client Home**, **Show contract name in Sign In instead of membership pricing option name**, **Add New Client - Default City**, **Address Line 2 Field for Individuals**, **User Defined Search Field for Clients** and **User Defined Field in Schedules** (label "Company", renamable in Words and Phrases), **Enable second client photo (After photo)**.

Features unlocked:
- **Children's Program Features** (emergency contact, age filters), **Client Alerting** (shows Client Alerts in Settings), **Client Document Uploads** with **Allow Clients to View Their Documents in Consumer Mode** (View checkbox preselected on new uploads), **Allow Clients to Upload Documents**, **Default Permissions for Client Documents in Consumer Mode** (Delete requires View), **ID Cards** (swipe/scan sign-in), **Insurance Fields**, **Use Costume Management**, **Use Client Measurements**, **Covid-19 Vaccine Verification**, **Allow Individuals to be Prospects**, **Add New Client - Default to Prospect** (both need Sales Team Management), **Ignore/Hide Close Dates**.
- **Contract Suspension Fees** (adds Suspension fee field) plus **Revenue Category** for those fees.
- **Scheduling Suspensions**: lets staff block consumer-site booking per client; auto-applies to clients whose contracts get suspended (not retroactive); suspended names show red on Class Sign In; separate from contract suspension.
- **Membership Sharing** and **Pricing Option Sharing**: enable the shared relationship types.
- **Pricing Option Activation Dates - Enforce** (honor activation dates vs expiry only), **- Update Automatically** (defaults the "Update Activation Date to First Visit Date" box), **- Autopays** (**Activate on Success Date** default, or **Activate on Schedule Date** even if declined; success-date plus unpaid scheduling can leave an unreconciled gap).
- **Set up Automatic Deactivation of Clients** (see the active/inactive profiles article).
- Invoices: **Show Credit Card Option**, **Show AutoPay Option**, **Show Pricing Option Receipt Notes**; **Account Balance Statement - Show Purchase Activity**.
- Integrations: **Constant Contact Integration** (removed June 2020), **Namaste Light Integration**.
- Sign-up: **Family Sign Up Experience** (prominent Add Family button; not on all sites), **Create Minimal User Profile** (default on; name and email only at first), **Suppress Consumer Identity Emails** (stops "Finish creating your Mindbody account" and "Add [business] to your Mindbody account" emails; Consumer Identity sites only).

## Gotchas
- Ignore/Hide Close Dates on = no automatic close date; staff close manually via Edit name. Turning it off means an existing purchaser without a close date gets one only after a second purchase.
- Negative-balance settings stack: you usually need the Allow All Clients (or per-client permission) setting plus the negative balance setting. ⚠️ Irreversible / financial — confirm with the user first: enabling negative balances or changing autopay activation dates changes how money and sessions are granted.
- Always click **Update** or changes are lost.

## Related
- [General Setup & Options: Directory](../settings-navigation/203259783-General-setup-options-explained.md)
- [General Setup & Options: System Settings](https://support.mindbodyonline.com/s/article/General-Setup-Options-screen-System-Settings?language=en_US)
- [General Setup & Options: Consumer Mode Settings](../online-booking/General-Setup-Options-screen-Consumer-Mode-Settings.md)
- [General Setup & Options: Retail Settings](https://support.mindbodyonline.com/s/article/General-Setup-Options-screen-Retail-Settings?language=en_US)
- [Client alerts](203259733-Client-alerts.md)
- [Client Documents screen](215843448-Client-documents-screen-overview.md)
- [Family accounts FAQ](Family-accounts-FAQ.md)
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Manage active and inactive client profiles](203257863-How-do-I-delete-deactivate-a-client.md)
- [Suspend a contract](../pricing-memberships/203258563-How-do-I-suspend-pause-freeze-a-contract.md)
- [Sharing pricing options and memberships](https://support.mindbodyonline.com/s/article/203259213-Sharing-pricing-options-memberships?language=en_US)
