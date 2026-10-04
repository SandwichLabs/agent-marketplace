# Mindbody operations wiki (for AI agents)

A working knowledge base for agents that operate the **Mindbody business software** (`clients.mindbodyonline.com`) on behalf of a fitness studio, primarily through the **Claude in Chrome** extension. Built 2026-10-04 from Mindbody's public support center (support.mindbodyonline.com), condensed and rewritten for agent use. Every reference page links its original article.

## Start here

| If you need to… | Open |
| --- | --- |
| Do a core task cheaply (schedule, roster, book/cancel, client status, log a note, sales, attendance, intro/lapsed follow-ups) | [chrome-extension/recipes/README.md](chrome-extension/recipes/README.md): URL + one JS call each, verified on the sandbox |
| Do any other task in the browser (sell a pack, refunds, payroll…) | [chrome-extension/workflows/index.md](chrome-extension/workflows/index.md), after reading [chrome-extension/README.md](chrome-extension/README.md) once |
| Find how a screen or setting works | [catalog.md](catalog.md) (one line per page, grep it) or a category index below |
| Jump straight to a screen by URL | [direct-links.md](direct-links.md) |
| Record something the docs got wrong or didn't say | [chrome-extension/field-notes.md](chrome-extension/field-notes.md) |

## Reference articles by category

| Category | Pages |
| --- | --- |
| [Classes & courses](articles/classes-courses/index.md) | scheduling, editing, cancelling, sign-in, waitlists, class/course options |
| [Appointments](articles/appointments/index.md) | services, staff availability, booking, rescheduling, checkout |
| [Clients](articles/clients/index.md) | profiles, lookup, types/indexes, relationships, documents/waivers, duplicates |
| [Pricing, contracts & memberships](articles/pricing-memberships/index.md) | pricing options, service categories, contracts, memberships, promos, gift cards, declined autopays |
| [Point of sale & payments](articles/pos-payments/index.md) | checkout, returns/refunds/voids, account payments, tips, cash drawer, Mindbody Payments |
| [Staff](articles/staff/index.md) | adding staff, logins, permissions, pay rates, time clock |
| [Reports](articles/reports/index.md) | sales, attendance, payroll, autopay, retention, mailing lists, exporting |
| [Online booking](articles/online-booking/index.md) | consumer mode, branded web widgets/app, Mindbody app listing, cancellation policies, links |
| [Settings & navigation](articles/settings-navigation/index.md) | getting around, general setup, auto emails/texts, rooms, packages |
| [Marketing & leads](articles/marketing-leads/index.md) | Marketing Suite, smart lists, Sales Pipeline, Messenger[ai] |

## Page conventions

- Every reference page has YAML front matter (`title`, `category`, `source`, sometimes `source_updated`) and the sections **Where in Mindbody** (direct link + menu path), **Steps**, **Settings & fields**, **Gotchas**, **Related**.
- **Related** links point to local pages when this wiki has them, otherwise to the live support article. If a task needs one of those, fetch it (e.g. with Firecrawl or the browser) and read it.
- ⚠️ in Gotchas marks money-moving or irreversible actions. Always get the person's explicit go-ahead first.
- Bold text is an exact UI label.

## Scope and limits

- **Covered:** ~225 articles on the core Mindbody business software for a fitness studio.
- **Not covered:** Booker (Mindbody's separate salon/spa product), enterprise/multi-region tools, consumer Mindbody-app how-tos, non-English articles. The support center has roughly 1,500+ English articles, and new pages can be added in the same format.
- Mindbody changes its UI; support articles lag. When the screen disagrees with a page, trust the screen, proceed carefully, and add a [field note](chrome-extension/field-notes.md).
- Some features depend on the studio's software package; see [Software level features](articles/settings-navigation/203886078-Software-Level-Features-and-Options-Full-Breakdown.md).

## Layout

```
README.md            ← you are here
catalog.md           ← every page, one line each
direct-links.md      ← every in-app URL found in the docs
chrome-extension/
  README.md          ← how to drive Mindbody with Claude in Chrome
  field-notes.md     ← observed UI facts, open questions
  recipes/README.md  ← verified low-token recipes (R1-R10, W1-W3)
  workflows/         ← 17 playbooks (01-17) + index.md
articles/<category>/ ← reference pages + index.md per category
```
