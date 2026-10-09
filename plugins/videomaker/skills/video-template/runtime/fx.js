// fx.js — the kit runtime: beat clock, easing, type and image helpers for a 1080x1920 canvas.
// Brand-neutral and dependency-free. A classic script (no import/export) so the same file runs inlined in the
// storyboard artifact and loaded by the videomaker renderer. Everything is deterministic: same frame in, same
// pixels out, no wall clock and no Math.random.
(function () {
  const W = 1080, H = 1920;
  const T = { bg: '#0C0D0F', ink: '#F2F0ED', accent: '#EA8E3E', scrim: '12,13,15', display: 'sans-serif', body: 'sans-serif', mono: 'monospace' };

  // ---------- math / easing ----------
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const lerp = (a, b, t) => a + (b - a) * t;
  const prog = (t, a, b) => clamp((t - a) / (b - a));
  const ease = {
    out3: t => 1 - (1 - t) ** 3, in3: t => t ** 3, inOut3: t => t < .5 ? 4 * t ** 3 : 1 - (-2 * t + 2) ** 3 / 2,
    out5: t => 1 - (1 - t) ** 5, expo: t => t === 1 ? 1 : 1 - 2 ** (-10 * t),
    back: t => { const c = 1.9; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2; },
  };
  // deterministic hash noise: same (a,b) -> same value in [0,1)
  const hash = (a, b = 0) => { let h = (a * 374761393 + b * 668265263) | 0; h = (h ^ (h >>> 13)) * 1274126177; return ((h ^ (h >>> 16)) >>> 0) / 4294967296; };
  // damped spring kicked at dt=0; 0 before the hit
  const spring = (dt, amp, freq = 4, damp = 6, phase = 0) => dt < 0 ? 0 : amp * Math.exp(-damp * dt) * Math.sin(2 * Math.PI * freq * dt + phase);

  // ---------- beat grid ----------
  // From beats.json { bpm, beats:[s...] } measured off the track; beat(n) interpolates, never assumes a fixed tempo.
  class Grid {
    constructor(b) { Object.assign(this, b); this.spb = 60 / b.bpm; }
    beat(n) {
      const i = Math.floor(n), f = n - i, B = this.beats;
      if (i < 0) return B[0] + n * this.spb;
      if (i >= B.length - 1) return B[B.length - 1] + (n - (B.length - 1)) * this.spb;
      return lerp(B[i], B[i + 1], f);
    }
    bar(n) { return this.beat(n * 4); }
    index(t) {
      const B = this.beats;
      if (t <= B[0]) return (t - B[0]) / this.spb;
      let lo = 0, hi = B.length - 1;
      if (t >= B[hi]) return hi + (t - B[hi]) / this.spb;
      while (hi - lo > 1) { const m = (lo + hi) >> 1; B[m] <= t ? lo = m : hi = m; }
      return lo + (t - B[lo]) / (B[lo + 1] - B[lo]);
    }
    since(t, div = 1) { const n = Math.floor(this.index(t) * div) / div; return t - this.beat(n); }
    pulse(t, decay = 0.18, div = 1) { return Math.exp(-this.since(t, div) / decay * 3); }
  }
  // a steady click grid for previews when there is no track (the storyboard)
  const clickGrid = (bpm = 124, bars = 64) => new Grid({ bpm, beats: Array.from({ length: bars * 4 }, (_, i) => i * 60 / bpm) });

  // ---------- canvas plumbing ----------
  const layer = (w = W, h = H) => { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; };
  const scratch = {};
  const buf = name => scratch[name] ||= layer();
  function clear(c) { const x = c.getContext('2d'); x.setTransform(1, 0, 0, 1, 0, 0); x.globalAlpha = 1; x.globalCompositeOperation = 'source-over'; x.filter = 'none'; x.clearRect(0, 0, c.width, c.height); return x; }
  function cover(ctx, src, { zoom = 1, x = 0, y = 0, rot = 0, w = W, h = H, cx = 0.5, cy = 0.5 } = {}) {
    const sw = src.videoWidth || src.naturalWidth || src.width, sh = src.videoHeight || src.naturalHeight || src.height;
    if (!sw) return;
    const s = Math.max(w / sw, h / sh) * zoom;
    ctx.save(); ctx.translate(w / 2 + x, h / 2 + y); if (rot) ctx.rotate(rot);
    ctx.drawImage(src, -sw * s * cx, -sh * s * cy, sw * s, sh * s);
    ctx.restore();
  }

  // ---------- type ----------
  function font(ctx, size, { family = T.display, weight = 700, style = '' } = {}) { ctx.font = `${style} ${weight} ${size}px ${family}`; }
  function tracked(ctx, str, x, y, track = 0, align = 'left') {
    ctx.letterSpacing = `${track}px`;
    const w = ctx.measureText(str).width;
    const x0 = align === 'center' ? x - w / 2 + track / 2 : align === 'right' ? x - w : x;
    ctx.textAlign = 'left'; ctx.fillText(str, x0, y); ctx.letterSpacing = '0px';
    return w;
  }
  const fitCache = new Map();
  function fit(ctx, str, width, opts = {}, max = 600) { // largest size at which str fits width
    const k = `${str}|${width}|${JSON.stringify(opts)}|${max}`;
    if (fitCache.has(k)) return fitCache.get(k);
    let lo = 8, hi = max;
    while (hi - lo > 1) { const m = (lo + hi) >> 1; font(ctx, m, opts); ctx.letterSpacing = `${(opts.track || 0) * m}px`; (ctx.measureText(str).width <= width ? lo = m : hi = m); }
    ctx.letterSpacing = '0px'; fitCache.set(k, lo); return lo;
  }
  // per-letter rise-in starting at t0
  function letters(ctx, str, x, y, t, t0, { st = 0.03, d = 0.22, rise = 60, align = 'left', track = 0, scaleIn = 0 } = {}) {
    ctx.letterSpacing = `${track}px`;
    const total = ctx.measureText(str).width;
    const x0 = align === 'center' ? x - total / 2 : align === 'right' ? x - total : x;
    ctx.textAlign = 'left';
    for (let i = 0; i < str.length; i++) {
      const p = ease.out3(prog(t, t0 + i * st, t0 + i * st + d));
      if (p <= 0) continue;
      const cx = x0 + ctx.measureText(str.slice(0, i)).width, cy = y + (1 - p) * rise;
      ctx.save(); ctx.globalAlpha *= p;
      if (scaleIn) { const sc = 1 + (1 - p) * scaleIn; ctx.translate(cx, cy); ctx.scale(sc, sc); ctx.fillText(str[i], 0, 0); }
      else ctx.fillText(str[i], cx, cy);
      ctx.restore();
    }
    ctx.letterSpacing = '0px';
    return total;
  }
  // scale-down "slam" of whatever draw() paints, pivoting on (cx, cy)
  function slam(ctx, draw, t, t0, cx, cy, amt = 0.35) {
    if (t < t0) return;
    const p = prog(t, t0, t0 + 0.16), sc = lerp(1 + amt, 1, ease.back(p));
    ctx.save(); ctx.globalAlpha *= clamp(p * 3); ctx.translate(cx, cy); ctx.scale(sc, sc); ctx.translate(-cx, -cy); draw(); ctx.restore();
  }
  function shadowed(ctx, blur = 30, a = 0.55) { ctx.shadowColor = `rgba(0,0,0,${a})`; ctx.shadowBlur = blur; ctx.shadowOffsetY = 4; }
  function noShadow(ctx) { ctx.shadowColor = 'transparent'; ctx.shadowBlur = 0; ctx.shadowOffsetY = 0; }
  function pill(ctx, text, cx, cy, t, t0, { size = 46, bg = T.accent, ink = T.bg, family = T.mono } = {}) {
    const p = ease.out5(prog(t, t0, t0 + 0.28));
    if (p <= 0) return;
    font(ctx, size, { family, weight: 700 }); ctx.letterSpacing = '4px';
    const tw = ctx.measureText(text).width, w = (tw + 72) * p, h = size * 1.9;
    ctx.save(); noShadow(ctx); ctx.fillStyle = bg; ctx.beginPath(); ctx.roundRect(cx - w / 2, cy - h / 2, w, h, h / 2); ctx.fill();
    ctx.beginPath(); ctx.rect(cx - w / 2, cy - h / 2, w, h); ctx.clip();
    ctx.fillStyle = ink; ctx.textBaseline = 'middle'; ctx.textAlign = 'left'; ctx.fillText(text, cx - tw / 2 + 2, cy + 2); ctx.restore();
    ctx.letterSpacing = '0px';
  }

  // ---------- image treatments ----------
  function scrim(ctx, y0, y1, a = 0.7) { // dark gradient band behind text
    const g = ctx.createLinearGradient(0, y0, 0, y1);
    g.addColorStop(0, `rgba(${T.scrim},0)`); g.addColorStop(.5, `rgba(${T.scrim},${a})`); g.addColorStop(1, `rgba(${T.scrim},0)`);
    ctx.fillStyle = g; ctx.fillRect(0, y0, W, y1 - y0);
  }
  function vignette(ctx, strength = 0.55) {
    const g = ctx.createRadialGradient(W / 2, H * .45, H * .25, W / 2, H * .5, H * .75);
    g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, `rgba(0,0,0,${strength})`);
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  }
  function flash(ctx, a, color = '#fff') { if (a <= 0.003) return; ctx.save(); ctx.globalAlpha = clamp(a); ctx.fillStyle = color; ctx.fillRect(0, 0, W, H); ctx.restore(); }
  let grainTiles;
  function grain(ctx, frame, alpha = 0.07) {
    if (!grainTiles) grainTiles = Array.from({ length: 6 }, (_, k) => {
      const c = layer(360, 640), x = c.getContext('2d'), d = x.createImageData(360, 640);
      for (let i = 0; i < d.data.length; i += 4) { const v = hash(i, k + 7) * 255; d.data[i] = d.data[i + 1] = d.data[i + 2] = v; d.data[i + 3] = 255; }
      x.putImageData(d, 0, 0); return c;
    });
    ctx.save(); ctx.globalAlpha = alpha; ctx.globalCompositeOperation = 'overlay'; ctx.imageSmoothingEnabled = false;
    ctx.drawImage(grainTiles[frame % 6], 0, 0, W, H); ctx.restore();
  }
  function duotone(ctx, src, dark = T.bg, light = T.accent, amt = 1) {
    const t = clear(buf('duo'));
    t.filter = 'grayscale(1) contrast(1.25)'; t.drawImage(src, 0, 0); t.filter = 'none';
    t.globalCompositeOperation = 'multiply'; t.fillStyle = light; t.fillRect(0, 0, W, H);
    t.globalCompositeOperation = 'screen'; t.fillStyle = dark; t.fillRect(0, 0, W, H);
    ctx.save(); ctx.globalAlpha = amt; ctx.drawImage(buf('duo'), 0, 0); ctx.restore();
  }
  function leak(ctx, t, a = 0.35, seed = 0, rgb = '234,142,62') { // drifting warm light leak
    ctx.save(); ctx.globalCompositeOperation = 'screen';
    for (let k = 0; k < 2; k++) {
      const x = W * (.2 + .6 * (0.5 + 0.5 * Math.sin(t * .7 + seed + k * 2.1))), y = H * (.15 + .7 * hash(seed, k));
      const g = ctx.createRadialGradient(x, y, 0, x, y, 700);
      g.addColorStop(0, `rgba(${rgb},${a})`); g.addColorStop(.5, `rgba(${rgb},${a * .35})`); g.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    }
    ctx.restore();
  }
  function glitch(ctx, src, amount, seed) { // horizontal slice displacement
    ctx.drawImage(src, 0, 0);
    const n = 6 + Math.floor(hash(seed, 1) * 8);
    for (let i = 0; i < n; i++) {
      const y = hash(seed, i * 3) * H, h = 8 + hash(seed, i * 3 + 1) * 120, dx = (hash(seed, i * 3 + 2) - .5) * 2 * amount;
      ctx.drawImage(src, 0, y, W, h, dx, y, W, h);
    }
  }
  function rgbSplit(ctx, src, amt, dy = 0) { // one chromatic hit
    if (amt < 0.5) { ctx.drawImage(src, 0, 0); return; }
    const acc = clear(buf('rgb-acc'));
    for (const [col, ox, oy] of [['#f00', -amt, -dy], ['#0f0', 0, 0], ['#00f', amt, dy]]) {
      const t = clear(buf('rgb-ch'));
      t.drawImage(src, 0, 0); t.globalCompositeOperation = 'multiply'; t.fillStyle = col; t.fillRect(0, 0, W, H);
      t.globalCompositeOperation = 'destination-in'; t.drawImage(src, 0, 0);
      acc.globalCompositeOperation = 'lighter'; acc.drawImage(buf('rgb-ch'), ox, oy);
    }
    ctx.drawImage(buf('rgb-acc'), 0, 0);
  }
  function burst(ctx, dt, { x = W / 2, y = H / 2, n = 160, speed = [500, 2600], drag = 2.4, gravity = 1400, life = 1.4, seed = 1, colors = ['#FFF4E6', '#F2F0ED', '#EA8E3E'] } = {}) {
    if (dt < 0 || dt > life) return;
    ctx.save(); ctx.globalCompositeOperation = 'screen';
    for (let k = 0; k < n; k++) {
      const a = hash(k, seed) * Math.PI * 2, v = lerp(speed[0], speed[1], hash(k, seed + 1) ** 1.6);
      const decay = (1 - Math.exp(-drag * dt)) / drag;
      const px = x + Math.cos(a) * v * decay, py = y + Math.sin(a) * v * decay + 0.5 * gravity * dt * dt;
      const r = 2 + hash(k, seed + 2) * 7 * (1 - dt / life), al = (1 - dt / life) ** 1.5 * (0.5 + 0.5 * hash(k, seed + 3));
      ctx.globalAlpha = al; ctx.fillStyle = colors[k % colors.length];
      ctx.beginPath(); ctx.arc(px, py, r, 0, Math.PI * 2); ctx.fill();
    }
    ctx.restore();
  }

  // brand tokens from brand.json: colours, font families, scrim colour
  function theme(brand) {
    const c = brand.colors || {}, f = brand.fonts || {};
    Object.assign(T, { bg: c.bg || T.bg, ink: c.ink || T.ink, accent: c.accent || T.accent });
    const hex = (c.bg || T.bg).replace('#', '');
    T.scrim = [0, 2, 4].map(i => parseInt(hex.slice(i, i + 2), 16)).join(',');
    for (const role of ['display', 'body', 'mono']) if (f[role]) T[role] = `'${f[role].family}', ${role === 'mono' ? 'monospace' : 'sans-serif'}`;
    return T;
  }

  globalThis.FX = {
    W, H, T, theme, clamp, lerp, prog, ease, hash, spring, Grid, clickGrid, layer, buf, clear, cover,
    font, tracked, fit, letters, slam, shadowed, noShadow, pill, scrim, vignette, flash, grain, duotone, leak, glitch, rgbSplit, burst,
  };
})();
