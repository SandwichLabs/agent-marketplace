---
title: Lead Management FAQ
category: marketing-leads
source: https://support.mindbodyonline.com/s/article/Getting-started-with-Lead-Management-FAQ?language=en_US
source_updated: 2026-08-05
---
# Lead Management FAQ

Q&A on the Sales Pipeline dashboard and Sales Funnel Analytics: how leads are captured, staged, converted, assigned and reported. Use it to troubleshoot why a lead is missing, not converting, or not assignable.

## Where in Mindbody
- Direct link (Lead Management): https://clients.mindbodyonline.com/app/lead-management
- Direct link (Staff Permissions): https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_staff.asp
- Direct link (Prospect Stages): https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_prospect_stages.asp
- Direct link (General Setup & Options): https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_ss_setup.asp
- Menu path: **Marketing > Lead Management**; **Settings > Staff > Staff Permissions**; **Settings > Clients > Prospect Stage**

## Steps
### Grant sales pipeline permissions
1. **Settings > Staff > Staff Permissions**, pick the permission group, expand **Sales Team Management**.
2. Tick **Ability to work the leads from Sales Pipeline** (open pipeline, work cards, read-only Settings). Optionally add **Sales Pipeline setting** (full Settings access); it requires the first one enabled.
3. For reports tick **Access to sales funnel analytics**. Click **Update**. Franchise: enterprise dashboard > **Configuration > Permissions** > **View Sales Funnel analytics**.

### Turn off lead capture / auto distribution
1. Click the **Engine** icon (top right) > **Settings** tab > toggle **Track Leads** off.
2. Or **Lead Distribution** tab > toggle **Automated Lead Distribution** off to assign manually.

### Lead card not showing / force re-sync
1. Ensure the client has an email (any placeholder works), **Prospect** is ticked and prospect stage is **New Lead**.
2. If already ticked: clear **Prospect**, **Save**, tick again, **Save**.

### Second opportunity card for same client
1. Client Info > **Edit name**, clear **Prospect**, **Save**, tick **Prospect**, choose **New Lead** in **Prospect stage**, **Save**. Give each card a different goal (same goal twice on one lead is not allowed).

### Assign a sales rep to a lead
1. Open the card > **Account Details** tab > **Assigned to** dropdown. Missing staff are not set as sales reps in their staff profile (Sales settings; follow-up assignment also needs **Can be assigned followups**).

### Fix POS error when checking out a lead
1. General Setup & Options > **Retail Settings** > tick **Require Sales Rep in POS** > **Update**.

### Enterprise banner "Reach out to your onboarding specialist..."
1. Enterprise dashboard > **Sales Funnel Analytics > Lead Management Settings** (top right) and pick the template site in the dropdown. Template must be Ultimate or higher.

## Settings & fields
- Default stages: **New Leads**, **Contact Made**, **Trial Started**, **Trial Completed**, **Won** (automatic when conversion criteria met), **Abandoned**. Dashboard shows up to 50 cards per stage, scroll the column for more; circle number = total cards.
- Included free in Ultimate 2.0 and Ultimate Plus; Mindbody only (not Booker).
- Default pipeline: stage names/descriptions editable, stages cannot be added/removed. Only a configurable pipeline allows that.
- Lead sources: clients created in business site, Mindbody app/web, consumer site, Business app, branded app/web tools, Messenger[ai].
- Lead Score Insights ("Not likely to convert") appears only in Trial Started/Trial Completed.
- Total Visits on a card: Jan 2000 through today plus 5 months, excluding early and late cancels.
- Overall Conversion Rate = new leads vs eventually won; Conversion Rate by Stage = stage-to-stage movement only. Skipped stages count as passed through with 0 days spent.

## Gotchas
- Cards move manually (drag and drop) unless automated lead progression/triggers are set up. A card with no purchase or visit collapses when moved to Contact Made.
- Won conversion needs the pricing option, membership or contract selected in **Lead Conversion Criteria**. Packages are not valid criteria (select their pricing options). A pricing option granting a membership needs the membership listed too; items inside a contract need the contract selected. Pricing options set to "Only allow clients to purchase this in a contract or package?" = Yes will not appear in the list; change to No.
- Turning **Track Leads** off stops new leads; existing cards stay. Turning back on is not retroactive for clients created in the gap.
- Existing prospect stages are not pipeline stages; only the auto-created **New Lead** stage feeds the pipeline. If the Prospect box is missing, enable "Allow Individuals to be Prospects" in General Setup & Options > Client Management.
- Bulk-moving leads to a configurable pipeline is possible per source stage, but destination-stage triggers do not fire for that move.
- Family accounts: parents and children each become leads. Shared pricing option/membership relationships: only the purchaser counts; the other may show "does not meet criteria". Pay-for-another-client sales can convert the related lead.
- Deleting an opportunity card means re-adding the client as a lead manually. Abandoned leads can be re-marked as new lead in Client Info.
- Several notification emails can be added in pipeline Notification Settings.

## Related
- [Sales pipeline dashboard overview](Sales-Pipeline-Dashboard.md)
- [How to set up your sales pipeline](Setting-up-your-sales-pipeline.md)
- [Lead channels overview](https://support.mindbodyonline.com/s/article/Lead-Channels-Sales-Pipeline?language=en_US)
- [Automated lead distribution](Automated-lead-distribution-Sales-Pipeline.md)
- [Track Meta leads](How-to-connect-Facebook-leads-to-your-Sales-Pipeline.md)
- [Create, manage, and delete leads](https://support.mindbodyonline.com/s/article/Managing-leads-in-the-Sales-Pipeline?language=en_US)
- [Create and assign a follow-up task](https://support.mindbodyonline.com/s/article/How-to-create-and-assign-a-follow-up-task-Sales-Pipeline-dashboard?language=en_US)
- [Change existing clients into leads](https://support.mindbodyonline.com/s/article/How-do-I-change-an-existing-client-into-a-lead-Sales-Pipeline-dashboard?language=en_US)
- [Customizing stage names and descriptions](https://support.mindbodyonline.com/s/article/Customizing-stage-names-and-descriptions-Sales-Pipeline?language=en_US)
- [Sales Funnel Analytics report](https://support.mindbodyonline.com/s/article/Sales-Funnel-Analytics-report?language=en_US)
- [Enterprise Sales Funnel Analytics report](https://support.mindbodyonline.com/s/article/Enterprise-Sales-Funnel-Analytics-report?language=en_US)
- [Sales Team Management](https://support.mindbodyonline.com/s/article/203253693-Sales-Team-Management?language=en_US)
- [Prospect Stages](https://support.mindbodyonline.com/s/article/206176457-Prospect-Stages?language=en_US)
- [Family accounts FAQ](../clients/Family-accounts-FAQ.md)
