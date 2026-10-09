// cards.js — the starter kit: text styles, cards and the grade, drawn on the 1080x1920 canvas.
// Kit API 1 (see the video-template skill's reference/kit-api.md). Classic script; needs fx.js. Exposes globalThis.KIT.
// Look: stacked display caps, one accent colour (the last word of a line, strike-throughs, the offer pill), soft dark
// scrims under type for legibility over footage, the logo at the end. Colours, fonts and copy come from brand.json.
(function () {
  const { W, H, clamp, lerp, prog, ease, hash, spring, font, tracked, fit, letters, slam, shadowed, noShadow, pill, scrim, vignette, grain, leak } = FX;
  let B, C, F, SAFE, CW;
  const fam = role => `'${B.fonts[role].family}', ${role === 'mono' ? 'monospace' : 'sans-serif'}`;
  const out = (t, t1, d = 0.15) => 1 - prog(t, t1 - d, t1);

  // ---------------- text styles: (ctx, line, k) ----------------
  // line: { text, lines[] (split on "/"), words[], t0, t1, beats[] (one time per word), b0, b1, ...extra keys from edit.json }
  // k: { t, i, g (beat grid), bi, SAFE, CW, logo, brand }

  // HOOK: the opening statement, stacked and frame-filling. On screen at frame 0 when the line starts at bar 1.
  // strike: N = accent strike-through across each line, starting N beats in (one line per half beat).
  function hook(ctx, ln, k) {
    const a = out(k.t, ln.t1, 0.2); if (a <= 0) return;
    const rows = ln.lines, longest = rows.reduce((m, r) => r.length > m.length ? r : m, '');
    const size = Math.min(230, fit(ctx, longest, CW, { family: fam('display'), weight: 700 }, 230));
    const lh = size * 0.98, y0 = 960 - (rows.length - 1) * lh / 2 + size * 0.35;
    ctx.globalAlpha = a; scrim(ctx, y0 - size * 1.4, y0 + (rows.length - 1) * lh + size * 0.9, 0.55); shadowed(ctx);
    font(ctx, size, { family: fam('display') });
    const instant = ln.b0 < 0.01;
    rows.forEach((r, j) => {
      const y = y0 + j * lh;
      ctx.fillStyle = ln.accent === j || (ln.accent === 'last' && j === rows.length - 1) ? C.accent : C.ink;
      if (instant) tracked(ctx, r, SAFE.l, y, -size * 0.04);
      else letters(ctx, r, SAFE.l, y, k.t, ln.t0 + j * k.g.spb * 0.5, { st: 0.02, rise: 40, track: -size * 0.04 });
      if (ln.strike != null) {
        const p = ease.expo(prog(k.bi, ln.b0 + ln.strike + j * 0.5, ln.b0 + ln.strike + j * 0.5 + 0.35));
        if (p > 0) { ctx.save(); noShadow(ctx); ctx.fillStyle = C.accent; ctx.letterSpacing = `${-size * 0.04}px`;
          ctx.fillRect(SAFE.l - 10, y - size * 0.37, (ctx.measureText(r).width + 20) * p, size * 0.13); ctx.restore(); }
      }
    });
  }

  // SLAM: one word per beat (every: beats between words), each slams in; the last word is accent.
  function slamStyle(ctx, ln, k) {
    const a = out(k.t, ln.t1); if (a <= 0) return;
    const ws = ln.words.map(w => w.toUpperCase());
    const size = Math.min(290, ...ws.map(w => fit(ctx, w, CW + 20, { family: fam('display'), weight: 700 }, 290)));
    const lh = size * 0.92, y0 = 1000 - (ws.length - 2) * lh * 0.5;
    ctx.globalAlpha = a; scrim(ctx, y0 - size * 1.2, y0 + (ws.length - 1) * lh + size * 0.6, 0.5);
    font(ctx, size, { family: fam('display') });
    ws.forEach((w, j) => {
      const tw = ln.beats[j]; if (k.t < tw) return;
      const y = y0 + j * lh, col = j === ws.length - 1 ? C.accent : C.ink;
      ctx.save(); ctx.fillStyle = col; shadowed(ctx, 40, 0.6);
      slam(ctx, () => tracked(ctx, w, SAFE.l, y, -size * 0.05), k.t, tw, SAFE.l + CW / 2, y - size * 0.35, 0.45);
      if (j === ws.length - 1) { // echo outline on the landing word
        noShadow(ctx); const e = prog(k.t, tw, tw + 2 * k.g.spb);
        ctx.globalAlpha = a * 0.3 * (1 - e); ctx.strokeStyle = col; ctx.lineWidth = 3; ctx.letterSpacing = `${-size * 0.05}px`;
        const d = size * 0.9 * ease.out3(prog(k.t, tw, tw + k.g.spb));
        ctx.strokeText(w, SAFE.l, y - d); ctx.strokeText(w, SAFE.l, y + d); ctx.letterSpacing = '0px';
      }
      ctx.restore();
    });
  }

  // STACK: up to three short lines rise in one per beat (every), the last one accent. "REAL, LASTING / STRENGTH."
  function stack(ctx, ln, k) {
    const a = out(k.t, ln.t1); if (a <= 0) return;
    const rows = ln.lines.map(r => r.toUpperCase()), every = ln.every ?? 1;
    const size = Math.min(ln.size || 130, ...rows.map(r => fit(ctx, r, CW, { family: fam('display'), weight: 700 }, 150)));
    const lh = size * 1.0, y0 = 960 - (rows.length - 1) * lh / 2 + size * 0.35;
    ctx.globalAlpha = a; scrim(ctx, y0 - size * 1.5, y0 + (rows.length - 1) * lh + size, 0.6); shadowed(ctx, 30, 0.6);
    font(ctx, size, { family: fam('display') });
    rows.forEach((r, j) => {
      ctx.fillStyle = j === rows.length - 1 ? C.accent : C.ink;
      letters(ctx, r, SAFE.l, y0 + j * lh, k.t, k.g.beat(ln.b0 + j * every), { st: 0.02, rise: 40, track: -4 });
    });
  }

  // QUIET: thin, slow, lots of air, for the breakdown. "NO EGO. / NO PRESSURE." Second line accent, one per bar.
  function quiet(ctx, ln, k) {
    const a = out(k.t, ln.t1, 0.3); if (a <= 0) return;
    const rows = ln.lines.map(r => r.toUpperCase()), every = ln.every ?? 4, drift = (k.bi - ln.b0) * 5;
    const size = Math.min(150, ...rows.map(r => fit(ctx, r, CW, { family: fam('display'), weight: 300 }, 150)));
    ctx.globalAlpha = a; scrim(ctx, 600, 1300, 0.5); shadowed(ctx, 30, 0.5);
    font(ctx, size, { family: fam('display'), weight: 300 });
    rows.forEach((r, j) => {
      const tb = ln.b0 + j * every; if (k.bi < tb) return;
      ctx.fillStyle = j === 0 ? C.ink : C.accent;
      letters(ctx, r, SAFE.l + (j ? drift * 0.4 : -drift), 880 + j * size * 1.07, k.t, k.g.beat(tb), { st: 0.05, d: 0.5, rise: 30, track: -4 });
    });
  }

  // LABEL: a big name with an optional mono tag above it (tag: "CLASS", "SERVICE", "NEW"; none by default), for what
  // the business sells. Two beats each reads well.
  function label(ctx, ln, k) {
    const a = out(k.t, ln.t1, 0.1); if (a <= 0) return;
    const name = ln.lines.join(' ').toUpperCase(), tag = (ln.tag || '').toUpperCase();
    ctx.globalAlpha = a; scrim(ctx, 720, 1260, 0.5); shadowed(ctx, 30, 0.6);
    font(ctx, 32, { family: fam('mono'), weight: 700 }); ctx.fillStyle = C.accent; ctx.letterSpacing = '4px';
    ctx.fillText(tag, SAFE.l, 880); ctx.letterSpacing = '0px';
    const size = Math.min(150, fit(ctx, name, CW, { family: fam('display'), weight: 700 }, 150));
    font(ctx, size, { family: fam('display') }); ctx.fillStyle = ln.accent ? C.accent : C.ink;
    letters(ctx, name, SAFE.l + k.g.pulse(k.t, 0.12) * 4, 880 + size * 1.05, k.t, ln.t0, { st: 0.012, d: 0.12, rise: 50, track: -size * 0.04 });
  }

  // SHOUT: the lift into the drop. Each word falls toward the lens on its beat and stacks; at the line's end (put
  // it right on the drop downbeat) the words shatter outward. Pair with a section hit on the drop.
  function shout(ctx, ln, k) {
    const ws = ln.words.map(w => w.toUpperCase()), T = ln.t1;
    const size = Math.min(330, ...ws.map(w => fit(ctx, w, CW + 30, { family: fam('display'), weight: 700 }, 330)));
    const lh = size * 0.9, y0 = 960 - (ws.length - 1) * lh / 2 + size * 0.35;
    const tremble = k.t < T ? 6 * ease.in3(prog(k.t, T - 2 * k.g.spb * 4, T)) : 0;
    font(ctx, size, { family: fam('display') });
    ws.forEach((w, j) => {
      const dt0 = k.t - ln.beats[j]; if (dt0 < 0) return;
      const tf = 0.11;
      let sc = dt0 < tf ? 1 + 2 * (1 - (dt0 / tf) ** 2) : 1 - 0.09 * Math.exp(-14 * (dt0 - tf)) * Math.sin(2 * Math.PI * 6 * (dt0 - tf));
      let al = dt0 < tf ? clamp(dt0 / 0.04) : 1, x = SAFE.l, y = y0 + j * lh, rot = 0;
      if (k.t >= T) {
        const dt = k.t - T, vx = (hash(j, 11) - 0.5) * 3200, vy = -700 - hash(j, 12) * 1400, w0 = (hash(j, 13) - 0.5) * 9;
        x += vx * dt; y += vy * dt + 0.5 * 5200 * dt * dt; rot = w0 * dt; sc = 1 + dt * 0.8; al = clamp(1 - dt / 0.7);
        if (al <= 0) return;
      } else { x += (hash(k.i, j) - .5) * tremble; y += (hash(k.i, j + 5) - .5) * tremble; }
      ctx.save(); ctx.globalAlpha = al; ctx.translate(x + CW / 2, y - size * 0.35); ctx.rotate(rot); ctx.scale(sc, sc); ctx.translate(-(x + CW / 2), -(y - size * 0.35));
      shadowed(ctx, 40, 0.7); ctx.fillStyle = j === ws.length - 1 ? C.accent : C.ink;
      tracked(ctx, w, x, y, -size * 0.05);
      ctx.restore();
    });
  }
  shout.tail = 0.8;

  // CAPTION: one sentence in the body face, low in the safe area. For extra info, never the main message.
  function caption(ctx, ln, k) {
    const a = Math.min(prog(k.t, ln.t0, ln.t0 + 0.2), out(k.t, ln.t1)); if (a <= 0) return;
    ctx.globalAlpha = a; scrim(ctx, 1200, 1480, 0.6);
    font(ctx, 46, { family: fam('body'), weight: 400 }); ctx.fillStyle = C.ink; shadowed(ctx, 20, 0.5);
    ln.lines.forEach((r, j) => letters(ctx, r, SAFE.l, 1340 + j * 60, k.t, ln.t0 + j * 0.1, { st: 0.012, rise: 12 }));
  }

  // ---------------- cards: { beats, draw(ctx, k, props) } — k.s = seconds into the card, k.card = {t0, t1, b0, b1} ----------------
  function drawLogo(ctx, k, x, y, w, t0, flicker) {
    const L = k.logo;
    if (!L || !(L.naturalWidth || L.width)) { // wordmark fallback
      font(ctx, Math.round(w / 6.5), { family: fam('mono'), weight: 700 }); ctx.fillStyle = C.ink; ctx.letterSpacing = '6px';
      ctx.textAlign = 'center'; ctx.globalAlpha *= clamp((k.t - t0) / 0.3); ctx.fillText(B.short || B.name, x + w / 2, y + w * 0.3); ctx.textAlign = 'left'; ctx.letterSpacing = '0px';
      return w * 0.4;
    }
    const h = w * (L.naturalHeight || L.height) / (L.naturalWidth || L.width);
    let on = clamp((k.t - t0) / 0.4);
    if (flicker && B.logo_style === 'neon') { // the neon sign strikes: on-off pattern, then a steady buzz
      const seq = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1], f = Math.floor((k.t - t0) * 30);
      on = f < 0 ? 0 : f >= seq.length ? 0.93 + 0.07 * hash(k.i, 4) : seq[f] * (0.6 + 0.4 * hash(f, 2));
    }
    ctx.save(); ctx.globalAlpha *= on;
    if (B.logo_style === 'neon') { ctx.shadowColor = C.accent; ctx.shadowBlur = 60 * on; }
    ctx.drawImage(L, x, y, w, h);
    if (B.logo_style === 'neon') { ctx.globalCompositeOperation = 'screen'; ctx.globalAlpha = on * 0.5; ctx.filter = 'blur(24px)'; ctx.drawImage(L, x, y, w, h); }
    ctx.restore();
    return h;
  }

  // START: "bug" (default) = the logo fades in small at the top over the hook footage and leaves by the card's end;
  // the hook line keeps frame 0. "full" = a logo card on black. "none" draws nothing. Set brand.start_card or props.style.
  const start = {
    beats: 4,
    draw(ctx, k, p) {
      const { t0, t1 } = k.card, style = p.style || B.start_card || 'bug';
      if (style === 'none') return;
      if (style === 'full') {
        const a = out(k.t, t1, 0.25); ctx.globalAlpha = a; ctx.fillStyle = C.bg; ctx.fillRect(0, 0, W, H);
        const w = 560; drawLogo(ctx, k, (W - w) / 2, 620, w, t0 + 0.05, true);
        return;
      }
      const a = Math.min(ease.out3(prog(k.t, t0, t0 + k.g.spb)), out(k.t, t1, k.g.spb));
      if (a <= 0) return;
      ctx.globalAlpha = a;
      const w = 200, y = SAFE.top + 10 - (1 - a) * 20;
      if (k.logo) drawLogo(ctx, k, SAFE.l, y, w, t0, false);
      else {
        noShadow(ctx); font(ctx, 26, { family: fam('mono'), weight: 700 }); // wordmark with a beat square
        const pz = k.g.pulse(k.t, 0.12); ctx.fillStyle = C.accent; ctx.fillRect(SAFE.l, y - 8 * pz, 12, 12 + 8 * pz);
        ctx.fillStyle = C.ink; ctx.letterSpacing = '5px'; ctx.fillText(B.short || B.name, SAFE.l + 28, y + 12); ctx.letterSpacing = '0px';
      }
    },
  };

  // OUTRO: darken, the neon logo strikes, the offer, the pill, the URL; then the hours (one row per beat) and the
  // address lower-third. Timings scale with the card's length (12 beats by default). Hours are skipped while empty.
  const outro = {
    beats: 12,
    draw(ctx, k, p) {
      const { b0, b1 } = k.card, len = b1 - b0, at = f => k.g.beat(b0 + f * len);
      ctx.fillStyle = `rgba(${FX.T.scrim},${0.55 * ease.out3(prog(k.t, at(0), at(0.08)))})`; ctx.fillRect(0, 0, W, H);
      const hours = p.hours || [], hasHours = hours.length > 0;
      const logoW = hasHours ? 340 : 480;
      let y = hasHours ? 290 : 330;
      y += drawLogo(ctx, k, (W - logoW) / 2, y, logoW, at(0), true) + 110;
      shadowed(ctx, 30, .6);
      font(ctx, 100, { family: fam('display') }); ctx.fillStyle = C.ink;
      const head = (p.offer?.headline || '').toUpperCase();
      const hs = Math.min(100, fit(ctx, head, CW + 60, { family: fam('display'), weight: 700 }, 100)); font(ctx, hs, { family: fam('display') });
      letters(ctx, head, W / 2, y, k.t, at(1 / 6), { st: 0.025, rise: 40, align: 'center', track: -3 });
      noShadow(ctx);
      if (p.offer?.pill) pill(ctx, p.offer.pill.toUpperCase(), W / 2, y + 115, k.t, at(2 / 6), { size: 40, family: fam('mono') });
      font(ctx, 36, { family: fam('mono'), weight: 700 }); ctx.fillStyle = B.colors.ink2 || C.ink;
      if (p.url) letters(ctx, p.url.toUpperCase(), W / 2, y + 220, k.t, at(3 / 6), { st: 0.012, rise: 10, align: 'center', track: 3 });
      y += 290;
      if (hasHours) { // rows tick in one per beat
        font(ctx, 34, { family: fam('mono'), weight: 700 }); ctx.letterSpacing = '3px';
        hours.slice(0, 4).forEach((h, j) => {
          const tb = at(7 / 12) + j * k.g.spb, a = ease.out3(prog(k.t, tb, tb + 0.2)); if (a <= 0) return;
          const yy = y + j * 52 + (1 - a) * 14;
          ctx.globalAlpha = a; ctx.fillStyle = C.accent; ctx.textAlign = 'left'; ctx.fillText(h.days.toUpperCase(), SAFE.l + 40, yy);
          ctx.fillStyle = C.ink; ctx.textAlign = 'right'; ctx.fillText(h.time.toUpperCase(), SAFE.r - 40, yy);
        });
        ctx.textAlign = 'left'; ctx.letterSpacing = '0px'; ctx.globalAlpha = 1;
        y += Math.min(4, hours.length) * 52 + 10;
      }
      if (p.address) { // broadcast lower-third
        const pa = ease.out5(prog(k.t, at(8 / 12), at(9 / 12))), y0 = Math.min(y, SAFE.bot - 175);
        if (pa > 0) {
          ctx.fillStyle = C.bg; ctx.fillRect(SAFE.l - 20, y0, (CW + 40) * pa, 170);
          ctx.fillStyle = C.accent; ctx.fillRect(SAFE.l - 20, y0, 12, 170 * pa);
          font(ctx, 80, { family: fam('display') }); ctx.fillStyle = C.ink;
          letters(ctx, (p.address.city || '').toUpperCase(), SAFE.l + 20, y0 + 92, k.t, at(8 / 12) + k.g.spb * 0.5, { st: 0.03, rise: 20, track: -3 });
          font(ctx, 32, { family: fam('mono'), weight: 700 }); ctx.fillStyle = C.accent;
          letters(ctx, (p.address.line || '').toUpperCase(), SAFE.l + 24, y0 + 145, k.t, at(8 / 12) + k.g.spb * 1.5, { st: 0.015, rise: 10, track: 3 });
        }
      }
    },
  };

  // LOWER: a lower-third for a service, product, class or person. props: { title, tag }.
  const lower = {
    beats: 8,
    draw(ctx, k, p) {
      const { t0, t1 } = k.card, pa = Math.min(ease.out5(prog(k.t, t0, t0 + 0.35)), out(k.t, t1, 0.25)), y0 = SAFE.bot - 200;
      if (pa <= 0) return;
      ctx.fillStyle = C.bg; ctx.fillRect(SAFE.l - 20, y0, (CW + 40) * pa, 160);
      ctx.fillStyle = C.accent; ctx.fillRect(SAFE.l - 20, y0, 12, 160 * pa);
      font(ctx, 28, { family: fam('mono'), weight: 700 }); ctx.fillStyle = C.accent; ctx.letterSpacing = '4px';
      ctx.globalAlpha = pa; ctx.fillText((p.tag || '').toUpperCase(), SAFE.l + 24, y0 + 50); ctx.letterSpacing = '0px';
      font(ctx, 72, { family: fam('display') }); ctx.fillStyle = C.ink;
      letters(ctx, (p.title || '').toUpperCase(), SAFE.l + 20, y0 + 125, k.t, t0 + 0.15, { st: 0.02, rise: 20, track: -2 });
    },
  };

  globalThis.KIT = {
    api: 1,
    setup({ brand }) {
      B = brand; C = brand.colors; SAFE = brand.safe; CW = SAFE.r - SAFE.l; F = brand.fonts;
      const gr = brand.grade || {};
      this.filter = `contrast(${gr.contrast ?? 1.08}) saturate(${gr.saturate ?? 0.95}) brightness(${gr.brightness ?? 1.12})`;
    },
    filter: 'none',
    // the shot layer: a soft-light wash of the accent pulls mixed gym lighting toward the brand
    grade(L) { const a = B.grade?.wash ?? 0.28; if (!a) return; L.save(); L.globalCompositeOperation = 'soft-light'; L.globalAlpha = a; L.fillStyle = C.accent; L.fillRect(0, 0, W, H); L.restore(); },
    post(ctx) { vignette(ctx, B.grade?.vignette ?? 0.6); },
    finish(ctx, k) { if (B.grade?.grain) grain(ctx, k.i, B.grade.grain); },
    text: { hook, slam: slamStyle, stack, quiet, label, shout, caption },
    cards: { start, outro, lower },
    // what the storyboard lists, in order
    catalog: [
      ['hook', 'Opening statement, stacked caps, already on screen at frame 0. Optional accent strike-through.'],
      ['slam', 'One word per beat, each slams in; the last word lands accent.'],
      ['stack', 'Two or three short lines rise in a beat apart, the last in accent.'],
      ['quiet', 'Thin and slow for the breakdown: one line per bar.'],
      ['label', 'A big name with an optional mono tag, for services, products or classes. Two beats each.'],
      ['shout', 'The lift: words fall in on the beat and shatter on the drop.'],
      ['caption', 'One sentence in the body face, low in the frame.'],
      ['start', 'Start card: the logo fades in small over the hook footage within one bar.'],
      ['lower', 'Lower-third for a class or a coach.'],
      ['outro', 'Out card: logo, offer, pill, URL, hours one row per beat, the address.'],
    ],
  };
})();
