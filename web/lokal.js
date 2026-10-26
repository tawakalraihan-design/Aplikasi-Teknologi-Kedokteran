"use strict";

/* =========================================================
   Mode penyimpanan.
   - Windows (exe): aplikasi dilayani server lokal 127.0.0.1,
     data di folder data/ lewat api/*.
   - HP (PWA di GitHub Pages): tidak ada server, jadi api/*
     dijawab di sini dari IndexedDB, dan konten bawaan diambil
     dari defaultdata/*.json. Kode halaman tidak perlu tahu bedanya.
   ========================================================= */

const DESKTOP = location.hostname === "127.0.0.1";
const NAMA_DATA = ["materi", "alat", "progres", "proyek", "soal", "lanjutan"];
const gambarCache = {}; // nama file → object URL (mode HP)
const gambarUrl = (f) => (DESKTOP ? "gambar/" + encodeURIComponent(f) : gambarCache[f] || "");

const IDB = (() => {
  let dbp = null;
  const open = () => dbp || (dbp = new Promise((res, rej) => {
    const r = indexedDB.open("teknologi-kedokteran", 1);
    r.onupgradeneeded = () => { r.result.createObjectStore("data"); r.result.createObjectStore("gambar"); };
    r.onsuccess = () => res(r.result);
    r.onerror = () => rej(r.error);
  }));
  const tx = async (store, mode, fn) => {
    const db = await open();
    return new Promise((res, rej) => {
      const t = db.transaction(store, mode), s = t.objectStore(store);
      const out = fn(s);
      t.oncomplete = () => res(out && "result" in out ? out.result : undefined);
      t.onerror = () => rej(t.error);
    });
  };
  return {
    get: (store, k) => tx(store, "readonly", (s) => s.get(k)),
    put: (store, k, v) => tx(store, "readwrite", (s) => s.put(v, k)),
    keys: (store) => tx(store, "readonly", (s) => s.getAllKeys()),
  };
})();

if (!DESKTOP) {
  const asli = window.fetch.bind(window);
  const json = (v, status = 200) => new Response(JSON.stringify(v), { status, headers: { "Content-Type": "application/json" } });
  const bawaan = async (n) => { const r = await asli("defaultdata/" + n + ".json", { cache: "no-cache" }); return r.json(); };

  window.fetch = async (input, init = {}) => {
    const url = typeof input === "string" ? input : input.url;
    const m = url.match(/^(?:\.\/)?api\/([^?]+)(?:\?(.*))?$/);
    if (!m) return asli(input, init);
    const [, jalur, qs] = m, q = new URLSearchParams(qs || "");
    try {
      if (jalur === "data") {
        const out = { errors: {}, dataDir: "Penyimpanan aplikasi di perangkat ini" };
        for (const n of NAMA_DATA) {
          let v = await IDB.get("data", n);
          if (v === undefined) { v = await bawaan(n); await IDB.put("data", n, v); }
          out[n] = v;
        }
        // Siapkan URL foto alat agar <img> bisa langsung dipakai.
        for (const k of await IDB.keys("gambar")) if (!gambarCache[k]) gambarCache[k] = URL.createObjectURL(await IDB.get("gambar", k));
        return json(out);
      }
      if (jalur.startsWith("save/")) {
        const n = jalur.slice(5);
        if (!NAMA_DATA.includes(n)) return json({ error: "nama tidak dikenal" }, 400);
        const lama = await IDB.get("data", n);
        if (lama !== undefined) await IDB.put("data", n + ".bak", lama);
        await IDB.put("data", n, JSON.parse(init.body));
        return json({ ok: true });
      }
      if (jalur === "defaults") {
        const out = {};
        for (const n of ["materi", "alat", "proyek", "soal", "lanjutan"]) out[n] = await bawaan(n);
        return json(out);
      }
      if (jalur === "backup") {
        const folder = "cadangan-" + new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
        const isi = {};
        for (const n of NAMA_DATA) isi[n] = await IDB.get("data", n);
        await IDB.put("data", folder, isi);
        return json({ folder });
      }
      if (jalur === "upload-gambar") {
        const file = q.get("nama") + "." + (q.get("ext") || "jpg");
        const blob = init.body instanceof Blob ? init.body : new Blob([init.body]);
        await IDB.put("gambar", file, blob);
        gambarCache[file] = URL.createObjectURL(blob);
        return json({ file });
      }
      if (jalur === "open-url") { window.open(q.get("u"), "_blank", "noopener"); return json({ ok: true }); }
      if (jalur === "open-folder") return json({ ok: true });
      return json({ error: "tidak dikenal" }, 404);
    } catch (e) {
      return json({ error: String(e) }, 500);
    }
  };
}
