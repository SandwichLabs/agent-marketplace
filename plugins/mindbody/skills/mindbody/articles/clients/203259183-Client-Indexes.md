---
title: Client indexes and client index values
category: clients
source: https://support.mindbodyonline.com/s/article/203259183-Client-Indexes?language=en_US
source_updated: 2026-06-03
---
# Client indexes and client index values

Client indexes are custom categories (Location, Age, Skill Level) each holding a list of values; a client gets one value per index. Use for segmentation, searching, mailing lists and reports.

## Where in Mindbody
- Client Indexes: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_clt_index.asp (Settings > Clients > Client Indexes)
- Client Index Values: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_clt_index_val.asp (Settings > Clients > Client Index Values)
- Modify Tagged Clients: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_taggedclts.asp (Settings > Clients > Modify Tagged Clients)
- Client Alerts: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_clt_alerts.asp

## Steps
### Create an index
1. Settings > Clients > Client Indexes; enter **Name**; set the checkboxes below; click **Add New Client Index**.

### Add values
1. Settings > Clients > Client Index Values; choose the **Index** dropdown; type a value; keep **Active?** ticked; **Add New Index Value**. Repeat per value.

### Assign to one client
1. Client Info > expand **Client Indexes** > **+Assign** (or the same via the Contact Logs screen > Client Indexes > **Assign**); pick a value per index; **Update**.

### Assign to many
1. Tag the clients first.
2. Settings > Clients > Modify Tagged Clients: **Update** = **Client Indexes**, choose **Index** and **Value**; optionally **Set for ALL Tagged Clients** (overwrites existing values); click **Update Tagged Clients**.

### Alert for missing required values
1. Ensure Client Alerting is enabled; Settings > Clients > Client Alerts > **Missing Required Fields**; pick screens in **Enable alerts**; **Update**.

## Settings & fields
- **Sort Order**: lower first; blank = alphabetical (prefix names with numbers to order them in the Business app).
- **Active**: inactive indexes drop to the bottom, not deleted.
- **Show on Course Roster** / **Edit on Course Roster**, **Show on Add Client**.
- **Show in Consumer Mode**: clients see and can change their value.
- **Required in Consumer Mode**: forced before creating a login or signing up (needs Show in Consumer Mode; branded web tools only, not the branded app).
- **Required in Business Mode**: staff must assign when adding a client (needs the Advanced - Add new Client Form).

## Gotchas
- Requires the Sales Team Management feature enabled; otherwise indexes and the Settings entries are hidden.
- Staff need the Assign Client Indexes permission.
- Required indexes are unsupported in the branded app and Mindbody app.
- Only the first 10 indexes show on the course schedule screen.

## Related
- [Client indexes and client types FAQ](203276923-About-Client-Indexes-and-Client-Types.md)
- [Client Indexes report](https://support.mindbodyonline.com/s/article/203256663-Client-Indexes-report?language=en_US)
- [Modify Tagged Clients tool](https://support.mindbodyonline.com/s/article/203259593-Modify-Tagged-Clients-tool?language=en_US)
- [Tagging clients](203256033-Tagging.md)
- [Client alerts](203259733-Client-alerts.md)
- [Client alerts FAQ](https://support.mindbodyonline.com/s/article/Client-alerts-FAQ?language=en_US)
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Client Contact Logs screen](https://support.mindbodyonline.com/s/article/215843268-Client-Contact-Logs-Screen-overview?language=en_US)
- [Looking up clients](203259203-Looking-up-clients.md)
- [Smart list: client index values](https://support.mindbodyonline.com/s/article/In-Specific-Client-Index-Value-Smart-List?language=en_US)
- [General Setup & Options: System Settings](https://support.mindbodyonline.com/s/article/General-Setup-Options-screen-System-Settings?language=en_US)
