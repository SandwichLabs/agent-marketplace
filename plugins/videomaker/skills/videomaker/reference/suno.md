# An original track from Suno (instrumental)

When the owner wants music made for the reel, write them a Suno prompt instead of picking a stock track. They make it
in Suno and drop the WAV into `music/`; the skill takes it from there.

**Rights first.** Ask which Suno plan they're on. Songs made on a free plan are generally not licensed for commercial
use; a business needs a paid plan for its posts. Check Suno's current terms with them if unsure.

## Settings to give them

| Setting | Value |
| --- | --- |
| Mode | **Custom** |
| Model | The latest |
| Instrumental | **On** |
| Title | The reel's topic, e.g. `Free Week` |
| Generations | Two or three batches. Keep any take that passes the checklist below |

## Style of Music

Fill in the genre and tempo to suit the business (house, electro, trap, rock), and keep the structure words. They
make a reel-shaped track with a breakdown, a build and a drop.

```
<genre, e.g. French house, electro-funk>, <tempo, 120–130> BPM, instrumental, four-on-the-floor kick from the first beat, punchy club mix, side-chained bass, short breakdown with drums out, snare-roll build-up, one bar of silence before the drop, massive drop, high energy gym anthem, clean hard ending, no fade out
```

## Exclude Styles

```
vocals, singing, rap, spoken word, choir, acoustic, lo-fi, ballad, slow, half-time, ambient intro, long intro, fade out
```

## Lyrics box (structure tags only)

With Instrumental on, the tags still steer the arrangement:

```
[Intro: kick and bass from beat one]
[Build]
[Drop]
[Breakdown: drums out]
[Build-Up: snare roll, riser]
[Break: one bar of silence]
[Drop: biggest moment]
[Outro: ends on one hard hit]
```

## A take passes if

1. The kick starts within the first few seconds (no long ambient intro).
2. There's a breakdown, then a build, then a drop that clearly hits harder.
3. The tempo holds steady all the way (no half-time section).
4. It ends on a hit, not a fade (or there's a hit to cut on).

Ask them to download it as **WAV** (cleaner beat detection than MP3) into `music/`, then run
`reelmaker analyze music/<file>.wav` and check that the drop candidates match what they hear.
