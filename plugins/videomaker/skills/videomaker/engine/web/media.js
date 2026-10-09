// media.js — the footage provider for reel.js: one <video> (or <img>) per library source, frame-exact seeks for the
// renderer, free-running playback with drift correction for the live preview. Exposes globalThis.MEDIA.
(function () {
  const { W, H, clamp } = FX;
  function create(library) {
    const pool = new Map();
    function el(src) {
      if (pool.has(src)) return pool.get(src);
      const s = library.sources[src];
      let e;
      if (!s) e = null;
      else if (s.kind === 'image') { e = new Image(); e.decoding = 'sync'; e.src = '/' + s.url; }
      else { e = document.createElement('video'); e.src = '/' + s.url; e.muted = true; e.playsInline = true; e.preload = 'auto'; e.crossOrigin = 'anonymous'; }
      pool.set(src, e);
      return e;
    }
    const loaded = v => {
      if (v.tagName === 'IMG') return v.complete && v.naturalWidth ? Promise.resolve() : new Promise((res, rej) => { v.onload = res; v.onerror = () => rej(new Error(`image ${v.src}`)); });
      return v.readyState >= 2 ? Promise.resolve() : new Promise((res, rej) => {
        v.addEventListener('loadeddata', res, { once: true }); v.addEventListener('error', () => rej(new Error(`video ${v.src} (codec not supported by this browser?)`)), { once: true });
      });
    };
    async function seek(src, t) {
      const v = el(src); if (!v) return;
      await loaded(v);
      if (v.tagName === 'IMG') return;
      t = clamp(t, 0, v.duration - 0.02);
      if (Math.abs(v.currentTime - t) < 1e-4 && v._presented === t) return;
      await new Promise(res => {
        let fired = false; const done = () => { if (!fired) { fired = true; res(); } };
        if (v.requestVideoFrameCallback) v.requestVideoFrameCallback(done);
        v.addEventListener('seeked', () => setTimeout(done, 40), { once: true }); // rVFC can skip when the frame didn't change
        v.currentTime = t;
      });
      v._presented = t;
    }
    function sync(src, t) { // preview: free-run, resync on drift
      const v = el(src); if (!v || v.tagName === 'IMG' || v.readyState < 2) return;
      t = clamp(t, 0, v.duration - 0.02);
      if (Math.abs(v.currentTime - t) > 0.12) v.currentTime = t;
      if (v.paused) v.play().catch(() => {});
    }
    function pauseExcept(active) { for (const [k, v] of pool) if (v && v.tagName === 'VIDEO' && !active.has(k)) v.pause(); }
    // a labelled stand-in for shots that aren't in the library yet
    const st = document.createElement('canvas'); st.width = 540; st.height = 960;
    function standin() {
      const x = st.getContext('2d'), g = x.createLinearGradient(0, 0, 540, 960);
      g.addColorStop(0, '#2a2018'); g.addColorStop(1, '#0c0d0f'); x.fillStyle = g; x.fillRect(0, 0, 540, 960); return st;
    }
    function label(L, id) { L.font = "700 46px monospace"; L.fillStyle = 'rgba(255,255,255,.35)'; L.textAlign = 'center'; L.fillText(`[ missing: ${id} ]`, W / 2, H * 0.88); L.textAlign = 'left'; }
    return { get: el, seek, sync, pauseExcept, standin, label };
  }
  globalThis.MEDIA = { create };
})();
