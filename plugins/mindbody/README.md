# mindbody

Run a studio's **Mindbody** business software from your AI agent, in your own Chrome, through the
[Claude in Chrome](https://claude.com/chrome) extension. Ask in plain words:

- "What's on the schedule today, and which classes are full?"
- "Who's new in the 6pm tonight?"
- "Put Sam Smith in Tempo Strength at six." *(the agent shows what it's about to do and waits for your yes)*
- "Is Sam's membership active? Do they owe anything?"
- "How did last week's sales look?" · "Who were our top members last month?"
- "Which intro-offer clients haven't come back?" · "Who hasn't been in for 3 weeks?"

It works through Mindbody's own screens and reports, signed in as you. It never types passwords or card details, and it
asks before anything that moves money or can't be undone.

**Install:** see the [marketplace README](../../README.md#install). On Claude desktop, paste the prompt and Claude follows
[SETUP.md](SETUP.md).

## Safety

- 🟢 Reading (schedules, rosters, reports): the agent just does it.
- 🟡 Changing data (adding a client, logging a note): it says exactly what it will change first.
- 🔴 Money or irreversible (booking, late cancels, sales, refunds, voids, contracts, cancelling a class): a one-line
  preview and your explicit yes, every time.

Client records are personal data: the agent opens only what the task needs and doesn't copy client details elsewhere.

## What's inside

```
skills/mindbody/
  SKILL.md                    how the agent picks the right path, and the safety rules
  chrome-extension/
    recipes/README.md         verified URL + one-script recipes for the core jobs (schedule, rosters, booking,
                              cancelling, client status, notes, sales, attendance, intro offers, lapsed members)
    workflows/                17 step-by-step playbooks (selling, refunds, appointments, staff, contracts, closeout…)
    README.md                 how to drive Mindbody in the browser safely
    field-notes.md            what the live screens actually look like
  articles/                   ~225 reference pages condensed from Mindbody's support center, each linking its source
  catalog.md, direct-links.md indexes
```

Recipes are verified on Mindbody's API sandbox (site -99). If the agent reports that a screen didn't match, open an
issue or a pull request: recipes and field notes are plain Markdown.

Not affiliated with or endorsed by Mindbody. Mindbody is a trademark of its owner. Reference pages summarize Mindbody's
public support articles and link each original.
