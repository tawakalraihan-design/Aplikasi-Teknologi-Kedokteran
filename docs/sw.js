// Dibuat oleh tools/build_pwa.py. Versi isi: 9954b95abb
// Strategi: ambil dari internet dulu (agar pembaruan langsung masuk),
// kalau offline pakai salinan tersimpan.
const CACHE = "tekkes-9954b95abb";
const FILES = ["anatomi.js", "app.js", "breakdown.js", "defaultdata/alat.json", "defaultdata/kisah.json", "defaultdata/lanjutan.json", "defaultdata/materi.json", "defaultdata/modul.json", "defaultdata/osits.json", "defaultdata/progres.json", "defaultdata/proyek.json", "defaultdata/referensi.json", "defaultdata/soal.json", "grafik.js", "ikon/ikon-180.png", "ikon/ikon-192.png", "ikon/ikon-512.png", "ikon/ikon-maskable-512.png", "ilustrasi.js", "index.html", "katex/LICENSE", "katex/auto-render.min.js", "katex/fonts/KaTeX_AMS-Regular.woff2", "katex/fonts/KaTeX_Caligraphic-Bold.woff2", "katex/fonts/KaTeX_Caligraphic-Regular.woff2", "katex/fonts/KaTeX_Fraktur-Bold.woff2", "katex/fonts/KaTeX_Fraktur-Regular.woff2", "katex/fonts/KaTeX_Main-Bold.woff2", "katex/fonts/KaTeX_Main-BoldItalic.woff2", "katex/fonts/KaTeX_Main-Italic.woff2", "katex/fonts/KaTeX_Main-Regular.woff2", "katex/fonts/KaTeX_Math-BoldItalic.woff2", "katex/fonts/KaTeX_Math-Italic.woff2", "katex/fonts/KaTeX_SansSerif-Bold.woff2", "katex/fonts/KaTeX_SansSerif-Italic.woff2", "katex/fonts/KaTeX_SansSerif-Regular.woff2", "katex/fonts/KaTeX_Script-Regular.woff2", "katex/fonts/KaTeX_Size1-Regular.woff2", "katex/fonts/KaTeX_Size2-Regular.woff2", "katex/fonts/KaTeX_Size3-Regular.woff2", "katex/fonts/KaTeX_Size4-Regular.woff2", "katex/fonts/KaTeX_Typewriter-Regular.woff2", "katex/katex.min.css", "katex/katex.min.js", "kisah.js", "lanjutan.js", "latihan.js", "lokal.js", "main.js", "manifest.webmanifest", "modul.js", "osits.js", "osits/nas17-ed-1.png", "osits/nas17-kt-1.png", "osits/nas17-mek-2.png", "osits/nas17-mek-3.png", "osits/nas17-mek-4.png", "osits/nas17-tf-1.png", "osits/nas17-tf-3.png", "osits/reg17-ed-1.png", "osits/reg17-ed-7.png", "osits/reg17-ed-8.png", "osits/reg17-ed-9.png", "osits/reg17-mek-2.png", "osits/reg17-mek-4.png", "osits/reg17-mek-5.png", "osits/reg17-tf-8.png", "osits/wil24-me-5.png", "osits/wil24-me-9.png", "proyek.js", "styles.css"];

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
