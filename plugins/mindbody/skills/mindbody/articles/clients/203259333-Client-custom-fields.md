---
title: Custom fields on the Client Info screen
category: clients
source: https://support.mindbodyonline.com/s/article/203259333-Client-custom-fields?language=en_US
source_updated: 2026-03-06
---
# Custom fields on the Client Info screen

Lets a studio add unlimited extra date, number or text fields to client profiles and search by them. Use when the studio needs to store data (due date, coupon code) that standard fields do not cover.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_clt_customfields.asp
- Menu path: Settings > Clients > Client Profile Custom Fields
- Search at: https://clients.mindbodyonline.com/app/business/asp/adm/adm_clt_lkup.asp (Clients)

## Steps
### Create
1. Open Client Profile Custom Fields.
2. Type the name under Add a New Custom Field.
3. Pick **Select a field type**: **Date** (DD/MM/YYYY), **Number** (numbers only), **Text** (also accepts alphanumeric codes such as coupon codes).
4. Leave **Active** ticked, click **Add New Custom Field**.

### Deactivate
1. Untick **Active** on the field, click **Update**.

### Fill in for a client
1. Open the client's Client Info; expand **Other Custom Fields** (number/text) or **Custom Date Fields**; enter values; **Save**.

### Search by custom field
1. Client Directory: date fields appear in **Filters** (start and end date); text/number fields appear in the **Search client by** dropdown, then enter the exact value; **Search**.

## Gotchas
- Package-dependent; supported on the business site and branded web tools, not in the Mindbody Business app.
- Not shown on the consumer site or in the business-site new-profile form; clients cannot edit them; cannot be made required.
- Search needs an exact match, and results list names only (the value is not displayed). Custom field data cannot be exported directly; workaround: **Tag new** the search results, then run Mailing Lists for tagged clients only.
- If a field is used in the Registration widget, hide it there before deactivating, otherwise it keeps showing.

## Related
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Client required fields](202988236-Client-required-fields.md)
- [Looking up clients](203259203-Looking-up-clients.md)
- [Tagging clients FAQ](203256033-Tagging.md)
- [Mailing Lists report](../reports/203256833-Mailing-Lists.md)
- [Export client email or mailing addresses](../reports/205027717-Export-client-email-or-mailing-addresses.md)
- [Exporting reports to Excel](../reports/203256023-Exporting-reports-to-Excel.md)
- [Registration widget setup](https://support.mindbodyonline.com/s/article/Configuring-your-Registration-Widget-Required-Fields-Custom-Fields-Client-Indexes-and-Referral-Types-Branded-web-healcode?language=en_US)
- [Mindbody account section on Client Info](https://support.mindbodyonline.com/s/article/MINDBODY-Account-on-the-Client-Info-screen?language=en_US)
