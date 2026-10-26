"use strict";

/* ---------- mulai (dimuat paling akhir, setelah semua modul halaman) ---------- */
(async function start() {
  await load();
  applySettings();
  initSearch();
  $("#backBtn").addEventListener("click", goBack);
  // Laci menu (layar HP)
  document.addEventListener("click", (e) => {
    if (e.target.closest("#menuBtn")) { document.body.classList.toggle("laci"); return; }
    if (document.body.classList.contains("laci") && (e.target.closest("#scrim") || e.target.closest(".sidebar a"))) document.body.classList.remove("laci");
  });
  await migrateContent();
  window.addEventListener("hashchange", router);
  router();
  // Versi HP: simpan file aplikasi agar bisa dibuka tanpa internet.
  if (!DESKTOP && "serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(() => {});
})();
