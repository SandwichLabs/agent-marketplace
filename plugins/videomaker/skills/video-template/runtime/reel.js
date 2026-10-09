// reel.js — the edit interpreter. Turns an edit.json (sections, text, cards on a bar grid) plus a measured beat
// grid into frames, drawing footage through a media provider and type/cards through the brand kit (cards.js).
// Shared by the storyboard artifact (procedural stand-in footage) and the videomaker renderer (real clips), so a
// preview and a render can't disagree. Classic script; needs fx.js loaded first. Exposes globalThis.REEL.
//
// Positions in edit.json are musician counts, 1-based: "9" = bar 9, "9:3" = bar 9 beat 3, "9:3.5" = the "and" of 3.
// Lengths are in beats. Sections take bars:[first, last] inclusive.
(function () {
  const { W, H, clamp, prog, ease, hash, spring, Grid, buf, clear, cover, flash, rgbSplit, glitch, burst, duotone } = FX;

  function pos(x, total) { // -> 0-based beat index
    if (x === 'end') return total;
    if (typeof x === 'number') throw new Error(`position ${x}: write positions as "bar" or "bar:beat" strings (1-based)`);
    const m = /^\s*(\d+)(?::(\d+(?:\.\d+)?))?\s*$/.exec(String(x));
    if (!m) throw new Error(`bad position "${x}" (want "bar" or "bar:beat", e.g. "9" or "9:3")`);
    return (+m[1] - 1) * 4 + (m[2] ? +m[2] - 1 : 0);
  }

  function create({ edit, beats, library = { sources: {}, shots: {} }, kit, brand, logo = null, media, standins = false }) {
    const g = new Grid(beats); g.duration = beats.duration;
    const fps = edit.fps || 30;
    const totalBeats = g.index(beats.duration);
    const warnings = [];
    const warn = m => { if (!warnings.includes(m)) warnings.push(m); };
    FX.theme(brand);
    kit.setup?.({ brand, logo });
    const SAFE = brand.safe || { l: 84, r: 930, top: 250, bot: 1480 };

    // ---- shots ----
    const shotInfo = id => {
      const s = library.shots[id] || Object.values(library.shots).find(x => x.name === id);
      if (!s) { if (!standins) warn(`unknown shot "${id}" (not in library.json); drawing a stand-in`); return { src: null, a: 0, b: 8, id }; }
      return s;
    };

    // ---- cut list ----
    const cuts = [], sectionsN = [];
    for (const [si, sec] of (edit.sections || []).entries()) {
      const b0 = (sec.bars[0] - 1) * 4, b1 = sec.bars[1] * 4;
      sectionsN.push({ ...sec, b0, b1 });
      const shots = (sec.shots || []).map(s => typeof s === 'string' ? { id: s } : s);
      if (!shots.length) { warn(`section "${sec.name || si}" has no shots`); continue; }
      const base = { speed: sec.speed, push: sec.push, punch: sec.punch, zoom: sec.zoom, duotone: sec.duotone };
      let k = 0;
      const lay = (from, to, step) => {
        for (let b = from; b < to - 1e-6; b += step) { cuts.push({ b, ...base, ...shots[k % shots.length], sec: si }); k++; }
      };
      const cut = sec.cut ?? 1;
      if (cut === 'hold') { const n = shots.length, step = (b1 - b0) / n; lay(b0, b1, step); }
      else if (Array.isArray(cut)) { const part = (b1 - b0) / cut.length; cut.forEach((st, j) => lay(b0 + j * part, b0 + (j + 1) * part, st)); }
      else lay(b0, b1, +cut);
    }
    cuts.sort((a, b) => a.b - b.b);
    cuts.forEach((c, k) => { c.k = k; c.t0 = g.beat(c.b); c.t1 = k + 1 < cuts.length ? g.beat(cuts[k + 1].b) : beats.duration; c.info = shotInfo(c.id); });
    if (cuts.length && cuts[0].b > 0) warn('the first section does not start at bar 1: frames before it are black');

    function cutAt(t) {
      const b = g.index(t);
      let k = cuts.length - 1;
      while (k > 0 && cuts[k].b > b + 1e-6) k--;
      return cuts[k];
    }
    // fit the cut inside the source shot: slow it down rather than freeze; in = -1 (default) picks a fixed spot
    function clipTime(c, s) {
      const dur = (c.info.b - c.info.a) - 0.04, len = c.t1 - c.t0;
      let speed = c.speed ?? 1;
      if (len * speed > dur) speed = dur / len;
      const room = Math.max(0, dur - len * speed);
      const inp = (c.in ?? -1) < 0 ? room * hash(c.k, 77) : Math.min(c.in, room);
      return c.info.a + inp + s * speed;
    }

    // ---- text + cards ----
    const lines = (edit.text || []).map((x, n) => {
      if (x.hook === true) { // the kit's fixed opening line (brand.hook, mode "template")
        const hk = brand.hook || {};
        if (!hk.text) warn('a line asks for the kit hook ("hook": true) but brand.json has no hook.text');
        x = { at: '1', len: 6, style: hk.style || 'hook', text: hk.text || '', ...(hk.strike != null ? { strike: hk.strike } : {}), ...x };
      }
      const b0 = pos(x.at, totalBeats), b1 = b0 + (x.len ?? 4);
      const words = x.words || String(x.text || '').replace(/\//g, ' ').split(/\s+/).filter(Boolean);
      const every = x.every ?? 1;
      const style = kit.text[x.style] ? x.style : (warn(`unknown text style "${x.style}"; using "${Object.keys(kit.text)[0]}"`), Object.keys(kit.text)[0]);
      return { ...x, n, style, b0, b1, t0: g.beat(b0), t1: g.beat(b1), lines: String(x.text || words.join(' ')).split('/').map(s => s.trim()), words,
        beats: words.map((_, i) => g.beat(b0 + i * every)) };
    });
    const cards = (edit.cards || []).map(x => {
      const def = kit.cards[x.card];
      if (!def) { warn(`unknown card "${x.card}"`); return null; }
      const b0 = pos(x.at, totalBeats), b1 = x.len != null ? b0 + x.len : (x.at === 'end' ? totalBeats : Math.min(totalBeats, b0 + (def.beats || 8)));
      return { ...x, def, b0, b1, t0: g.beat(b0), t1: Math.min(beats.duration, g.beat(b1)), props: { ...brand, ...(x.props || {}) } };
    }).filter(Boolean);

    // ---- one-shot hits at section starts: flash / shake / rgb / burst / glitch ----
    const hits = sectionsN.filter(s => s.hit).map(s => ({ t: g.beat(s.b0), b: s.b0, ...(s.hit === true ? { flash: true, shake: true, rgb: true } : s.hit) }));
    if (hits.filter(h => h.flash).length > 2) warn('more than two flashes in one reel: keep flashes for the drop');

    function camera(t) {
      let sc = 1, x = 0, y = 0, rot = 0;
      for (const h of hits) {
        if (!h.shake) continue;
        const dt = t - h.t; if (dt < 0 || dt > 2) continue;
        const m = h.shake === true ? 1 : h.shake;
        sc += 0.12 * m * Math.exp(-5 * dt) * Math.cos(2 * Math.PI * 2.4 * dt);
        x += spring(dt, 50 * m, 9, 7, 0.3); y += spring(dt, 40 * m, 11, 7, 1.1); rot += spring(dt, 0.025 * m, 5, 6);
      }
      return { sc, x, y, rot };
    }

    const ctxFor = (t, i) => ({ t, i, g, bi: g.index(t), brand, C: brand.colors, SAFE, CW: SAFE.r - SAFE.l, logo, FX, duration: beats.duration });

    function drawShot(F, t, i) {
      const c = cutAt(t); if (!c) return null;
      const s = t - c.t0, u = clamp(s / (c.t1 - c.t0));
      const zoom = (c.zoom ?? 1.04) + (c.push ?? 0.03) * ease.inOut3(u) + (c.punch ?? 0) * g.pulse(t, 0.14);
      const L = clear(buf('shot'));
      const src = c.info.src ? media.get(c.info.src) : media.standin(c.id);
      L.filter = kit.filter || 'none'; if (src) cover(L, src, { zoom }); L.filter = 'none';
      const k = ctxFor(t, i);
      kit.grade?.(L, k);
      if (!c.info.src) media.label?.(L, c.id);
      const near = hits.find(h => h.glitch && Math.abs(g.index(t) - h.b) < 0.25);
      if (near) glitch(F, buf('shot'), 90 * (1 - Math.abs(g.index(t) - near.b) * 4), Math.floor(g.index(t) * 8));
      else F.drawImage(buf('shot'), 0, 0);
      if (c.duotone) duotone(F, buf('shot'), brand.colors.bg, brand.colors.accent, c.duotone === true ? 1 : c.duotone);
      return c;
    }

    function draw(out, t, i) {
      const F = clear(buf('frame'));
      F.fillStyle = brand.colors.bg; F.fillRect(0, 0, W, H);
      drawShot(F, t, i);
      const k = ctxFor(t, i);
      kit.post?.(F, k);
      for (const ln of lines) {
        const fn = kit.text[ln.style], tail = fn.tail || 0;
        if (t >= ln.t0 && t < ln.t1 + tail) { F.save(); fn(F, ln, k); F.restore(); }
      }
      for (const cd of cards) if (t >= cd.t0 && t < cd.t1 + (cd.def.tail || 0)) { F.save(); cd.def.draw(F, { ...k, s: t - cd.t0, card: cd }, cd.props); F.restore(); }
      // composite through the camera, then the hits
      out.setTransform(1, 0, 0, 1, 0, 0); out.globalAlpha = 1; out.globalCompositeOperation = 'source-over'; out.filter = 'none';
      out.fillStyle = '#050506'; out.fillRect(0, 0, W, H);
      const cam = camera(t);
      out.save(); out.translate(W / 2 + cam.x, H / 2 + cam.y); out.rotate(cam.rot); out.scale(cam.sc, cam.sc); out.translate(-W / 2, -H / 2);
      const rgbHit = hits.find(h => h.rgb && t >= h.t && t < h.t + 0.35);
      if (rgbHit) { const dt = t - rgbHit.t; rgbSplit(out, buf('frame'), 40 * Math.exp(-9 * dt), 8 * Math.exp(-9 * dt)); }
      else out.drawImage(buf('frame'), 0, 0);
      out.restore();
      for (const h of hits) {
        const dt = t - h.t;
        if (h.flash) flash(out, 0.85 * Math.exp(-Math.max(0, dt) * 14) * (dt >= 0 ? 1 : 0), brand.colors.cream || '#fff');
        if (h.burst) burst(out, dt, { y: H * 0.45, seed: 3, colors: [brand.colors.cream || '#fff', brand.colors.ink, brand.colors.accent] });
      }
      kit.finish?.(out, k);
    }

    // cue times for contact sheets: just after every section start, the middle of each line and card
    function cues() {
      const c = [];
      for (const s of sectionsN) c.push({ t: g.beat(s.b0 + 0.5), label: `${s.name || 'section'} · bar ${s.bars[0]}` });
      for (const l of lines) c.push({ t: (l.t0 + l.t1) / 2, label: `${l.style}: ${l.lines.join(' ')}`.slice(0, 40) });
      for (const cd of cards) c.push({ t: Math.min(cd.t1 - 0.05, cd.t0 + (cd.t1 - cd.t0) * 0.75), label: `card: ${cd.card}` });
      return c.filter(x => x.t < beats.duration).sort((a, b) => a.t - b.t);
    }

    return {
      fps, duration: Math.floor(beats.duration * fps) / fps, grid: g, cuts, lines, cards, sections: sectionsN, warnings, cues, draw,
      need(t) { const c = cutAt(t); return c && c.info.src ? [[c.info.src, clipTime(c, t - c.t0)]] : []; },
      sources: [...new Set(cuts.map(c => c.info.src).filter(Boolean))],
    };
  }

  globalThis.REEL = { create, pos };
})();
