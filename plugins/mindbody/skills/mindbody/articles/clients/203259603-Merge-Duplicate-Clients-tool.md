---
title: Merge Duplicate Clients tool
category: clients
source: https://support.mindbodyonline.com/s/article/203259603-Merge-Duplicate-Clients-tool?language=en_US
source_updated: 2026-08-10
---
# Merge Duplicate Clients tool

Combines two client profiles into one, carrying over purchases, visits, billing and other history from the profile being removed into the one being kept.

## Where in Mindbody
- Direct link: https://clients.mindbodyonline.com/app/business/asp/adm/adm_tlbx_mergeclients.asp
- Menu path: Settings > Clients > **Merge Duplicate Clients**
- Also reachable from the **More** menu on Client Info.

## Steps
1. Search for the profile to keep (last name, first name or phone; choose **RSSID** in **Lookup client by** to search by client ID).
2. Click that client; it appears under KEEP on the left.
3. Search for and click the duplicate; it appears under REMOVE on the right.
4. Optionally click **Switch Client 1 with Client 2** to swap sides.
5. Compare the two. Red text on the right marks data that differs from the left.
6. Copy any wanted values from right to left by hand.
7. Click **Merge Clients** at the bottom.
8. Click **Back**, or open the profile. Log out and back in so the removed profile clears from recent lookups.

## Settings & fields
Carried over: documents, relationships, billing info (only if the kept profile has none), login (only if the kept profile has none and the removed one has email plus password), client indexes and types, reward points, account credit, contact logs (staff-entered ones only with Sales Team Management on), VAT ID, visit and payment history, SOAP/progress notes, uploaded documents, client forms, formula notes.

Not carried over: address, measurements, liability waiver status (signed documents stay), martial arts belts, before/after photos, referral type, emergency contact, custom fields, notes, staff alerts, reps, birthday, gender, profile history dates, alerts, membership status.

## Gotchas
- Staff need the Merge duplicate/Unmask client records permission.
- Search is punctuation-sensitive (OBrian vs O'Brian).
- If a field is filled on both sides, the left value wins and the right is deleted; if the left is blank, the right is not auto-copied, so copy it manually.
- Merging two profiles with different linked Mindbody accounts leaves one profile linked to both; pick the primary on Client Info afterward.
- After merging, reset membership status from Client Info.
- A half-merged profile showing a "merged" error: unmask it, reactivate if needed, then merge again.
- ⚠️ Irreversible / financial — confirm with the user first: a merge cannot be fully reversed (unmasking only separates the profiles again) and it moves payment history, credit and billing data.

## Related
- [Unmask Merged Clients tool](Unmask-Merged-Clients-tool.md)
- [Locate Duplicate Clients tool](203259613-Locate-Duplicate-Clients-tool.md)
- [Client Info screen overview](Client-Info-screen-overview.md)
- [Manage active and inactive client profiles](203257863-How-do-I-delete-deactivate-a-client.md)
- [Family accounts FAQ](Family-accounts-FAQ.md)
