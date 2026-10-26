# -*- coding: utf-8 -*-
"""Bangun versi HP (PWA) ke folder docs/ untuk GitHub Pages.

docs/ = isi web/ + defaultdata/*.json + sw.js (daftar file untuk offline).
Jalankan setiap kali web/ atau defaultdata/ berubah, lalu commit docs/.
"""
import hashlib, json, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs"
if OUT.exists():
    shutil.rmtree(OUT)
shutil.copytree(ROOT / "web", OUT)
shutil.copytree(ROOT / "defaultdata", OUT / "defaultdata")
(OUT / ".nojekyll").write_text("")

files = sorted(str(p.relative_to(OUT)).replace("\\", "/") for p in OUT.rglob("*") if p.is_file() and p.name != ".nojekyll")
h = hashlib.sha256()
for f in files:
    h.update(f.encode()); h.update((OUT / f).read_bytes())
versi = h.hexdigest()[:10]

sw = """// Dibuat oleh tools/build_pwa.py. Versi isi: %(versi)s
// Strategi: ambil dari internet dulu (agar pembaruan langsung masuk),
// kalau offline pakai salinan tersimpan.
const CACHE = "tekkes-%(versi)s";
const FILES = %(files)s;

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(["./", ...FILES])).then(() => self.skipWaiting()));
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k.startsWith("tekkes-") && k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  const simpanan = () => caches.match(req, { ignoreSearch: true }).then((r) => r || caches.match("./"));
  const jaringan = fetch(req, { cache: "no-cache" }).then((res) => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
    return res;
  });
  // Sinyal lemah: setelah 4 detik pakai salinan tersimpan bila ada.
  const batas = new Promise((res) => setTimeout(() => simpanan().then((r) => r && res(r)), 4000));
  e.respondWith(Promise.race([jaringan.catch(simpanan), batas]));
});
""" % {"versi": versi, "files": json.dumps(files)}
(OUT / "sw.js").write_text(sw, encoding="utf-8")
print("docs/ siap:", len(files), "file, versi", versi)
