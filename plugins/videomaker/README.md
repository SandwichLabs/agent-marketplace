# videomaker

Finished, beat-matched promo reels from your own footage, made on your computer by your AI agent. No editing app,
and the same look every time. Ask in plain words:

- "Make a 30-second reel for the free week from my clips."
- "Do a hype video for the new Saturday class, using the swing clips first."
- "Set up our video template: logo, colours, hours and the offer."
- "Same reel, different song." · "Make it 60 seconds."

Two skills:

| Skill | What it does | Runs in |
| --- | --- | --- |
| **video-template** | Builds your brand's **video kit** from your logo and website: colours, fonts, the opening hook, a start card with your logo, an out card that animates your hours, address, offer and URL, and the text styles. Shows it all moving in a storyboard you can play, even over one of your own clips. | Any Claude with code execution, including a chat |
| **videomaker** | Turns a folder of clips and photos plus a track into a 1080×1920 MP4. It sets up its own tools, tags your footage, cuts every shot on the beat with the drop on cue, renders, and writes the caption. It can suggest a royalty-free track or write a Suno prompt for an original. | Claude desktop's **Code tab** or Claude Code (needs your files) |

**Install** in Claude desktop's Code tab or Claude Code:

```
/plugin marketplace add SandwichLabs/agent-marketplace
/plugin install videomaker@sandwichlabs
```

Or paste the prompt at the top of [SETUP.md](SETUP.md) and Claude walks you through it, including the first setup.

## How it works

```
clips/ + music/ + kit/                      your folder
   │ ingest: proxies, shots split at scene cuts, contact sheets → Claude tags the shots
   │ music: beats and downbeats measured, the drop found, the song cut to 16 or 32 bars on the beat
   │ edit.json: sections, shots, text and cards on the bar grid (Claude writes it)
   ▼
headless Chrome draws every frame (kit + footage) → ffmpeg encodes → reels/<name>/reel.mp4 + caption.txt
```

- **One engine, two views.** The storyboard and the renderer run the same drawing code
  (`skills/video-template/runtime/`), so what you approve in the storyboard is what renders.
- **Positions are musical.** The edit says "bar 9, beat 3", never seconds, so a different song re-times the whole reel.
- **Setup without a password.** uv, Python, ffmpeg and a browser install into your user folder. Your own Google Chrome
  is used if you have it. First setup takes about two minutes; after that a 30-second reel renders in 1–3 minutes.

## What's inside

```
skills/video-template/
  SKILL.md                 gather assets → brand.json → storyboard artifact → iterate → save the kit
  kit/                     the neutral starter kit: brand.json, cards.js, open-licence fonts
  runtime/                 fx.js (motion helpers, beat grid) and reel.js (the edit interpreter)
  scripts/storyboard.py    builds the self-contained storyboard page (standard library only)
  reference/               kit-api.md, design.md
skills/videomaker/
  SKILL.md                 the automatic run, from setup to the rendered reel and caption
  bin/reelmaker            launcher: installs uv on first use, runs the engine in its own locked environment
  engine/                  the reelmaker Python package (doctor, ingest, music, check, stills, preview, render, board)
                           and the compositor page (web/)
  reference/               setup, craft, edit format, music, Suno, captions
```

Your footage, music and kit stay in your folder. Nothing is uploaded unless you ask Claude to publish a preview for you.

## Fonts

The starter kit ships Space Grotesk, DM Sans and Space Mono, all under the SIL Open Font License.
