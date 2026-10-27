// Dibuat oleh tools/build_pwa.py. Versi isi: c7974145bb
// Strategi: ambil dari internet dulu (agar pembaruan langsung masuk),
// kalau offline pakai salinan tersimpan.
const CACHE = "tekkes-c7974145bb";
const FILES = ["anatomi.js", "app.js", "breakdown.js", "defaultdata/alat.json", "defaultdata/kisah.json", "defaultdata/lanjutan.json", "defaultdata/materi.json", "defaultdata/modul.json", "defaultdata/progres.json", "defaultdata/proyek.json", "defaultdata/referensi.json", "defaultdata/soal.json", "grafik.js", "ikon/ikon-180.png", "ikon/ikon-192.png", "ikon/ikon-512.png", "ikon/ikon-maskable-512.png", "ilustrasi.js", "index.html", "kisah.js", "lanjutan.js", "latihan.js", "lokal.js", "main.js", "manifest.webmanifest", "modul.js", "proyek.js", "styles.css"];

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
