"""The track: measured beats and downbeats, a per-bar energy profile, the drop, and a splice of the song down to the
reel's bar window on measured downbeats. Beat detection follows the sizzle pipeline: librosa's beat tracker, and the
downbeat phase is the beat offset (0-3) carrying the most kick energy under 150 Hz."""
import hashlib, json, pathlib, sys

from . import tools


def _sig(p: pathlib.Path) -> str:
    st = p.stat()
    return hashlib.sha1(f"{p.name}:{st.st_size}:{int(st.st_mtime)}".encode()).hexdigest()[:12]


def analyze(track: pathlib.Path, bpm_hint: float = 124.0, cache_dir: pathlib.Path | None = None) -> dict:
    track = pathlib.Path(track).resolve()
    cache = (cache_dir or track.parent / ".analysis") / f"{track.stem}.{_sig(track)}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    import numpy as np, librosa
    src = track
    if track.suffix.lower() not in (".wav", ".flac", ".ogg", ".aif", ".aiff"):
        # decode through ffmpeg: librosa's mp3/m4a backends vary by machine
        src = cache.with_suffix(".wav")
        src.parent.mkdir(parents=True, exist_ok=True)
        tools.ff("-i", track, "-ac", "1", "-ar", "22050", src)
    y, sr = librosa.load(str(src), sr=22050, mono=True)
    if src != track:
        src.unlink(missing_ok=True)
    hop = 128  # 5.8 ms beat resolution
    onset = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    tempo, frames = librosa.beat.beat_track(onset_envelope=onset, sr=sr, hop_length=hop, start_bpm=bpm_hint, tightness=400, units="frames")
    beats = librosa.frames_to_time(frames, sr=sr, hop_length=hop)
    if len(beats) < 16:
        raise SystemExit(f"{track.name}: found only {len(beats)} beats; is this a steady-tempo track?")
    S = np.abs(librosa.stft(y, hop_length=hop, n_fft=2048))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
    low = librosa.onset.onset_strength(S=librosa.amplitude_to_db(S[freqs < 150]), sr=sr, hop_length=hop)
    kick = np.array([low[max(0, f - 2):f + 3].max() for f in frames])
    phase = int(np.argmax([kick[p::4].mean() for p in range(4)]))
    downbeats = beats[phase::4]
    # librosa's own tempo is quantised to whole frame lags; the beats themselves follow the onsets, so the slope of a
    # straight line through all of them is the true tempo
    tempo = float(60 / np.polyfit(np.arange(len(beats)), beats, 1)[0])
    rms = librosa.feature.rms(y=y, hop_length=hop)[0]
    lowE = S[freqs < 150].mean(axis=0)
    t = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=hop)
    bars = []
    for i, b0 in enumerate(downbeats):
        b1 = downbeats[i + 1] if i + 1 < len(downbeats) else b0 + 4 * 60 / tempo
        m = (t >= b0) & (t < b1)
        bars.append({"bar": i, "t": round(float(b0), 3), "rms": round(float(rms[m].mean()), 4) if m.any() else 0.0,
                     "low": round(float(lowE[m].mean()), 3) if m.any() else 0.0})
    mr = max(b["rms"] for b in bars) or 1
    ml = max(b["low"] for b in bars) or 1
    for b in bars:
        b["e"] = round(0.6 * b["rms"] / mr + 0.4 * b["low"] / ml, 3)
    res = {"track": str(track), "bpm": round(tempo, 3), "beats": [round(float(x), 4) for x in beats], "phase": phase,
           "downbeats": [round(float(x), 4) for x in downbeats], "bars": bars, "duration": round(len(y) / sr, 3)}
    res["drops"] = drops(res)
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(res))
    return res


def drops(a: dict, top: int = 5) -> list:
    """Candidate drops: bars where energy jumps after a lower stretch. Score = mean energy of the next 2 bars minus the
    previous 2, plus a bonus when the drop lands on a 4-bar phrase from the first loud bar."""
    e = [b["e"] for b in a["bars"]]
    first = next((i for i, x in enumerate(e) if x > 0.35), 0)
    cands = []
    for i in range(2, len(e) - 1):
        after, before = sum(e[i:i + 2]) / len(e[i:i + 2]), (e[i - 1] + e[i - 2]) / 2
        if e[i] < 0.55:
            continue
        score = after - before + (0.05 if (i - first) % 4 == 0 else 0)
        if score > 0.08:
            cands.append({"bar": i, "t": a["bars"][i]["t"], "score": round(score, 3)})
    cands.sort(key=lambda c: -c["score"])
    keep = []
    for c in cands:  # one candidate per 4-bar neighbourhood
        if all(abs(c["bar"] - k["bar"]) >= 4 for k in keep):
            keep.append(c)
    return keep[:top]


def table(a: dict, mark=None, window=None) -> str:
    out = [f"tempo {a['bpm']:.1f} BPM, {len(a['bars'])} bars, {a['duration']:.1f} s, downbeat phase {a['phase']}"]
    for b in a["bars"]:
        tag = ""
        if window and window[0] <= b["bar"] < window[1]:
            tag = f" ← reel bar {b['bar'] - window[0] + 1}"
        if mark is not None and b["bar"] == mark:
            tag += "  DROP"
        out.append(f"bar {b['bar']:3d} {b['t']:7.2f}s  {'#' * int(30 * b['e']):30s}{tag}")
    if a.get("drops"):
        out.append("drop candidates: " + ", ".join(f"bar {d['bar']} @ {d['t']:.2f}s ({d['score']:+.2f})" for d in a["drops"]))
    return "\n".join(out)


def choose_window(a: dict, bars: int, drop_bar: int, drop_at=None, start_bar=None):
    """-> (start, drop) in the song's bar numbering (0-based). drop_bar is where the drop lands in the reel (1-based)."""
    n = len(a["bars"])
    if bars > n:
        raise SystemExit(f"the track has only {n} full bars; asked for {bars}")
    if start_bar is not None:
        return start_bar, start_bar + drop_bar - 1
    if drop_at is not None:
        d = min(range(n), key=lambda i: abs(a["bars"][i]["t"] - drop_at))
        cands = [d]
    else:
        cands = [c["bar"] for c in a.get("drops") or []] or [max(range(n), key=lambda i: a["bars"][i]["e"])]
    for d in cands:
        s = d - (drop_bar - 1)
        if s >= 0 and s + bars <= n:
            return s, d
    d = cands[0]
    s = max(0, min(n - bars, d - (drop_bar - 1)))
    print(f"note: no drop candidate fits {drop_bar - 1} bars of build inside the song; using bars {s}–{s + bars - 1} "
          f"(the drop lands at reel bar {d - s + 1})", file=sys.stderr)
    return s, d


def splice(a: dict, ranges: list, out_dir: pathlib.Path, xfade=0.012, fade_out=0.35) -> dict:
    """Cut [first, end) bar ranges on measured downbeats with tiny fades at the joins, concat, and write
    track.wav, track.m4a and beats.json (t=0 = the first downbeat) into out_dir."""
    beats, phase, spb = a["beats"], a["phase"], 60 / a["bpm"]

    def db(n):
        k = phase + 4 * n
        return beats[k] if k < len(beats) else beats[-1] + (k - len(beats) + 1) * spb

    segs, out_beats, energy, t = [], [], [], 0.0
    for b0, b1 in ranges:
        s0, s1 = db(b0), db(b1)
        for k in range(phase + 4 * b0, phase + 4 * b1):
            bt = beats[k] if k < len(beats) else db(b0) + (k - phase - 4 * b0) * spb
            out_beats.append(round(t + bt - s0, 4))
        energy += [a["bars"][i]["e"] for i in range(b0, min(b1, len(a["bars"])))]
        segs.append((s0, s1))
        t += s1 - s0
    dur = t
    f = []
    for i, (s0, s1) in enumerate(segs):
        pre = xfade if i else 0
        chain = f"[0:a]atrim={s0 - pre:.4f}:{s1:.4f},asetpts=PTS-STARTPTS,afade=t=in:d={xfade}:curve=tri"
        if i < len(segs) - 1:
            chain += f",afade=t=out:st={s1 - s0 + pre - xfade:.4f}:d={xfade}"
        f.append(chain + f"[s{i}]")
    tail = f",afade=t=out:st={max(0, dur - fade_out):.4f}:d={fade_out}" if fade_out else ""
    f.append("".join(f"[s{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1,atrim=0:{dur:.4f}{tail}[o]")
    out_dir.mkdir(parents=True, exist_ok=True)
    tools.ff("-i", a["track"], "-filter_complex", ";".join(f), "-map", "[o]", "-ar", "48000", out_dir / "track.wav")
    tools.ff("-i", out_dir / "track.wav", "-c:a", "aac", "-b:a", "256k", out_dir / "track.m4a")
    res = {"track": "track.m4a", "bpm": a["bpm"], "beats": out_beats, "phase": 0, "duration": round(dur, 4), "energy": energy,
           "source": {"file": a["track"], "ranges": ranges}}
    (out_dir / "beats.json").write_text(json.dumps(res, indent=1))
    return res


def make_track(track, reel_dir: pathlib.Path, bars=16, drop_bar=9, drop_at=None, start_bar=None, ending="fade", bpm_hint=124.0):
    a = analyze(pathlib.Path(track), bpm_hint)
    s, d = choose_window(a, bars, drop_bar, drop_at, start_bar)
    ranges = [(s, s + bars)]
    fade = 0.35
    if ending == "song":  # finish on the song's own last two bars (its real ending) instead of a fade
        last = max(i for i, b in enumerate(a["bars"]) if b["e"] > 0.25) + 1
        if last - 2 > s + bars - 2:
            ranges = [(s, s + bars - 2), (last - 2, last)]
            fade = 0.0
    res = splice(a, ranges, reel_dir, fade_out=fade)
    print(table(a, mark=d, window=(s, s + bars)))
    print(f"\nreel track: song bars {', '.join(f'{x}–{y - 1}' for x, y in ranges)} → {bars} bars, {res['duration']:.2f} s at "
          f"{a['bpm']:.1f} BPM; drop at reel bar {d - s + 1} ({(d - s) * 4 * 60 / a['bpm']:.2f} s)")
    print(f"wrote {reel_dir / 'track.wav'}, track.m4a, beats.json")
    res["drop_bar"] = d - s + 1
    (reel_dir / "beats.json").write_text(json.dumps(res, indent=1))
    return res
