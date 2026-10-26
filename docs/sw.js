// Dibuat oleh tools/build_pwa.py. Versi isi: 5b15d362c1
// Strategi: ambil dari internet dulu (agar pembaruan langsung masuk),
// kalau offline pakai salinan tersimpan.
const CACHE = "tekkes-5b15d362c1";
const FILES = ["anatomi.js", "app.js", "defaultdata/alat.json", "defaultdata/lanjutan.json", "defaultdata/materi.json", "defaultdata/progres.json", "defaultdata/proyek.json", "defaultdata/soal.json", "ikon/ikon-180.png", "ikon/ikon-192.png", "ikon/ikon-512.png", "ikon/ikon-maskable-512.png", "ilustrasi.js", "index.html", "lanjutan.js", "latihan.js", "lokal.js", "main.js", "manifest.webmanifest", "proyek.js", "styles.css"];

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
