# The track: choosing it, the catalog, rights

Everything in a reel is timed to the track, and the reel is built around its drop. Pick well, then let
`reelmaker music` measure it.

## What makes a good reel track

1. **A real drop**: a moment that hits clearly harder after a build or a quieter stretch. No drop, no hype reel.
2. **About 118–135 BPM**: fast enough for a cut on every beat, slow enough to read the words.
3. **A quieter stretch before the drop** (a breakdown or a filtered build), so the drop lands.
4. **Instrumental**: sung words fight on-screen words.
5. **Room before the drop**: about 15 s for a 30 s reel, about 30 s for 60 s. `reelmaker music` finds a window that fits,
   or says it can't.

`reelmaker analyze <track>` prints the tempo, an energy bar per bar of the song and the drop candidates. The owner's
ears win: if they say the drop is at 1:12, use `--drop-at 72`.

## The curated catalog

`reference/catalog.json` lists instrumental tracks a business may bake into its own posts, with the tempo and the drop
measured by the analyser. `reelmaker catalog` lists them; `reelmaker fetch <id>` downloads one into `music/` with a
`<id>.license.txt` beside it (source, licence, date, and the credit line if one is needed).

| Source | Licence | Credit | Notes |
| --- | --- | --- | --- |
| **Mixkit** | Mixkit Stock Music Free License ([mixkit.co/license](https://mixkit.co/license/)) | Not required | Allowed in social media posts and online ads. Not allowed: remixing into a music-only track, or registering the tracks with a rights-management service. |
| **Incompetech** (Kevin MacLeod) | CC BY 4.0 ([licences](https://incompetech.com/music/royalty-free/licenses/)) | **Required, visible**: put the credit from the licence note in the caption | A paid licence on incompetech.com removes the credit requirement. |

When suggesting tracks, match the topic: dark and driving (Night Terrors, In a Heartbeat) for intensity, bright and
uplifting (Electro Dreams, Golden Storm, Take this Higher) for offers and community, rock (Sports Rock) for a sporty
feel. Prefer no-credit tracks unless the owner doesn't mind a credit line. The catalog's tracks were chosen by their
measured shape, not by ear, so suggest the owner plays one before posting.

## Other sources the owner may use

- **Pixabay Music**: free for commercial video with no credit, but only by downloading in a browser (its terms forbid
  scripted downloads). Skip tracks marked **"Content ID Registered"**, which can get a reel muted or claimed. Have the
  owner download it and drop it in `music/`.
- **Free Music Archive**: only tracks under CC BY or CC0, always with a credit. Uneven quality, and some artists use
  Content ID.
- **An original from Suno** (`reference/suno.md`): needs a paid Suno plan for commercial use.
- **Not suitable for a business's posts**: Uppbeat's free tier (individuals only), the YouTube Audio Library (its terms
  cover YouTube), Bensound's free licence, and any track under a non-commercial (NC) licence.

## Commercial songs (the radio, streaming)

A business account can't bake a commercial song into its video: Instagram, Facebook and TikTok may mute, block or remove
it, and businesses only get the platforms' commercial libraries (Meta's Sound Collection, TikTok's Commercial Music
Library). If the owner wants a song from those libraries, render with `reelmaker render <reel> --no-music` (the edit is
still timed to the track you analysed), then they add the same song in the app's music picker and line it up by ear.

## Keep the paper trail

Each fetched track gets a licence note in `music/`. For tracks the owner brings, ask where they came from and write a
short `<file>.license.txt` the same way. If a platform ever mutes a reel, the note is what they dispute it with.
