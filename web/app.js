"use strict";

/* =========================================================
   Teknologi Kedokteran: aplikasi belajar (v1.3)
   Data: materi.json, alat.json, progres.json, proyek.json,
         soal.json, lanjutan.json, modul.json (penjelasan, studi
         kasus, bahan kuliah per mata kuliah), referensi.json
   Struktur: Mata kuliah → sub-materi bernomor; Alat → blok → kontribusi
             (mata kuliah + sub-materi yang dipakai alat itu)
   ========================================================= */

const VERSI_APP = "1.4";
const VERSI_KONTEN = 5;
const S = { materi: [], alat: [], progres: {}, proyek: [], soal: [], lanjutan: [], modul: [], referensi: [], dataDir: "", errors: {} };
const ui = { alatFilter: "Semua", alatView: "grid", materiFilter: "Semua", bidangFilter: "Semua", sumberFilter: "Semua", statusFilter: "semua", kelolaTab: "alat", selBlok: null };

const TINGKAT = { 3: "Inti", 2: "Penting", 1: "Pendukung" };
const STATUS = { belum: "Belum", sedang: "Sedang dipelajari", sudah: "Sudah dipelajari" };
const STATUS_NEXT = { belum: "sedang", sedang: "sudah", sudah: "belum" };
const KATEGORI_ALAT = ["Diagnostik", "Monitoring", "Pencitraan", "Terapi", "Bedah", "Life Support", "Rehabilitasi", "Laboratorium", "Perangkat Lunak"];
const KATEGORI_MATERI = ["Sains Dasar", "Ilmu Kedokteran Dasar", "Elektronika", "Komputasi", "Instrumentasi", "Pencitraan dan Radiasi", "Data dan AI", "Desain dan Fabrikasi", "Klinis", "Manajemen dan Keselamatan", "Riset dan Profesi"];
// Warna gradien thumbnail per kategori (palet hero Lovable).
const GRAD = {
  Diagnostik: "linear-gradient(135deg,#ff3029,#ff66f4)", Monitoring: "linear-gradient(135deg,#2483ff,#82bcff)",
  Pencitraan: "linear-gradient(135deg,#82bcff,#ff66f4)", Terapi: "linear-gradient(135deg,#fe7b02,#ff3029)",
  "Life Support": "linear-gradient(135deg,#2483ff,#ff66f4)", Rehabilitasi: "linear-gradient(135deg,#fe7b02,#ff66f4)",
  Laboratorium: "linear-gradient(135deg,#82bcff,#2483ff)", "Perangkat Lunak": "linear-gradient(135deg,#2483ff,#fe7b02)",
  Bedah: "linear-gradient(135deg,#ff3029,#2483ff)",
};
const gradOf = (k) => GRAD[k] || "linear-gradient(135deg,#82bcff,#fe7b02)";

/* ---------- ikon (garis tipis 1.5px) ---------- */
const P = (d) => `<path d="${d}" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>`;
const ICON = {
  home: P("M3 11 12 4l9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"),
  alat: P("M4 13h3l2-6 4 12 2-6h5"),
  materi: P("M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 21V5M8 7h7"),
  peta: P("M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"),
  kelola: P("M4 20h4L19 9l-4-4L4 16zM13.5 6.5l4 4"),
  setting: '<circle cx="12" cy="12" r="3" fill="none" stroke="currentColor" stroke-width="1.6"/>' + P("M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"),
  arrow: P("M4 12h15m-5-5 5 5-5 5"),
  up: P("m6 15 6-6 6 6"), down: P("m6 9 6 6 6-6"),
  plus: P("M12 5v14M5 12h14"),
  edit: P("M4 20h4L19 9l-4-4L4 16z"),
  trash: P("M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13"),
  grid: P("M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"),
  list: P("M8 6h12M8 12h12M8 18h12M4 6h.01M4 12h.01M4 18h.01"),
  shield: P("M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"),
  loop: P("M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3M18 3v4h-4M6 21v-4h4"),
  send: P("M12 19V5m-6 6 6-6 6 6"),
  link: P("M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"),
  back: P("M19 12H5m6-6-6 6 6 6"),
  proyek: P("M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.8-.7-.7-2.8z"),
  latihan: P("M9 11l3 3 8-8M20 12v7a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h9"),
  hta: P("M12 3v18M5 21h14M6 7h12M6 7l-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"),
  he: P("M4 19V9M10 19V5M16 19v-7M22 19H2M20 4l-4 4-3-2-4 4"),
  ph: '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/>' + P("M3 12h18M12 3c3 3 4 6 4 9s-1 6-4 9c-3-3-4-6-4-9s1-6 4-9z"),
  image: P("M4 5h16v14H4zM4 15l4-4 4 4 3-3 5 5M15 9h.01"),
  play: P("M7 4v16l13-8z"),
  pause: P("M8 5v14M16 5v14"),
  prev: P("M18 6 9 12l9 6zM6 6v12"), next: P("M6 6l9 6-9 6zM18 6v12"),
  ref: P("M6 3h11a1 1 0 0 1 1 1v17l-6.5-4L5 21V4a1 1 0 0 1 1-1zM9 8h6M9 11h4"),
  file: P("M7 3h7l5 5v12a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zM14 3v5h5M9 13h6M9 17h6"),
  bulb: P("M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"),
  check: P("m5 12 5 5 9-10"),
  kue: P("M4 20h16M5 20v-6h14v6M5 14c0-2 2-3 3.5-3h7c1.5 0 3.5 1 3.5 3M8 11V8M12 11V7M16 11V8M8 5.5v.01M12 4.5v.01M16 5.5v.01"),
  kisah: P("M12 6c-2-1.5-5-2-8-1.5V19c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5V4.5c-3-.5-6 0-8 1.5zM12 6v14.5"),
};
const ico = (n, size) => `<svg viewBox="0 0 24 24" aria-hidden="true"${size ? ` width="${size}" height="${size}"` : ""}>${ICON[n] || ""}</svg>`;

/* ---------- util ---------- */
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const slug = (s) => String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40) || "item";
const uniqueId = (base, list, self) => { let id = slug(base), n = 2; while (list.some((x) => x.id === id && x !== self)) id = slug(base) + "-" + n++; return id; };
const byId = (list, id) => list.find((x) => x.id === id);
const materiById = (id) => byId(S.materi, id);
const alatById = (id) => byId(S.alat, id);
const semLabel = (m) => (m && m.semester ? `Semester ${m.semester}${m.semesterPasti === false ? " (perkiraan)" : ""}` : "Tanpa semester");
const semShort = (m) => (m && m.semester ? (m.semesterPasti === false ? "≈S" : "S") + m.semester : "–");
const subsOf = (m) => (m && Array.isArray(m.sub) ? m.sub : []);
const subKey = (mid, no) => mid + "|" + no;
const subLabel = (s) => (s.no ? s.no + ". " : "") + s.nama;
const findSub = (m, no) => subsOf(m).find((s) => String(s.no) === String(no));

function toast(msg, err) {
  const t = document.createElement("div");
  t.className = "toast" + (err ? " err" : "");
  t.textContent = msg;
  $("#toasts").appendChild(t);
  setTimeout(() => t.remove(), err ? 6000 : 2600);
}

function confirmDialog(title, body, okLabel = "Hapus") {
  return new Promise((res) => {
    const m = $("#modal");
    m.innerHTML = `<div class="modal" role="dialog" aria-modal="true"><h2>${esc(title)}</h2><p class="muted">${body}</p>
      <div class="acts"><button class="btn" data-a="0">Batal</button><button class="btn primary" data-a="1">${esc(okLabel)}</button></div></div>`;
    m.hidden = false;
    const done = (v) => { m.hidden = true; m.innerHTML = ""; res(v); };
    m.onclick = (e) => { const a = e.target.closest("[data-a]"); if (a) done(a.dataset.a === "1"); else if (e.target === m) done(false); };
    $("[data-a='1']", m).focus();
  });
}

function openUrl(u) { fetch("api/open-url?u=" + encodeURIComponent(u)); }
// Referensi boleh berupa "judul: https://..." atau teks biasa.
function refHtml(r) {
  const m = String(r).match(/https?:\/\/\S+/);
  if (!m) return esc(r);
  const label = r.replace(m[0], "").replace(/[:\s]+$/, "").trim();
  return `${label ? esc(label) + " " : ""}<button class="link" data-url="${esc(m[0])}">${esc(label ? "buka tautan" : m[0].replace(/^https?:\/\//, "").slice(0, 60))}</button>`;
}

/* ---------- API ---------- */
async function load() {
  try {
    const r = await fetch("api/data", { cache: "no-store" });
    const d = await r.json();
    S.materi = Array.isArray(d.materi) ? d.materi : [];
    S.alat = Array.isArray(d.alat) ? d.alat : [];
    for (const k of ["proyek", "soal", "lanjutan", "modul", "referensi", "kisah"]) S[k] = Array.isArray(d[k]) ? d[k] : [];
    S.progres = d.progres && typeof d.progres === "object" && !Array.isArray(d.progres) ? d.progres : {};
    S.progres.status = S.progres.status || {};
    S.progres.sub = S.progres.sub || {};
    S.progres.pengaturan = S.progres.pengaturan || {};
    S.dataDir = d.dataDir || "";
    S.errors = d.errors || {};
  } catch (e) {
    toast("Gagal memuat data: " + e.message, true);
  }
}

let saveTimers = {};
async function save(name) {
  try {
    const r = await fetch("api/save/" + name, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(S[name]) });
    if (!r.ok) throw new Error(await r.text());
    return true;
  } catch (e) {
    toast("Gagal menyimpan " + name + ": " + e.message, true);
    return false;
  }
}
function saveLater(name, ms = 600) {
  clearTimeout(saveTimers[name]);
  saveTimers[name] = setTimeout(() => save(name), ms);
}

/* ---------- migrasi konten: hanya MENAMBAH, tidak pernah menghapus ---------- */
// Semester bawaan v1 untuk mata kuliah yang kini disamakan dengan silabus.
const SEM_V1 = { kimia: 2, eldig: 3, pemrograman: 2, sinyal: 5, biomekanik: 4 };
async function migrateContent() {
  if ((S.progres.versiKonten || 1) >= VERSI_KONTEN || Object.keys(S.errors || {}).length) return;
  let def;
  try { def = await (await fetch("api/defaults")).json(); } catch (e) { return; }
  await fetch("api/backup", { method: "POST" });
  const dari = S.progres.versiKonten || 1;
  let addM = 0, addS = 0, addA = 0, addK = 0;
  for (const d of def.materi) {
    const u = materiById(d.id);
    if (!u) { S.materi.push(d); addM++; addS += subsOf(d).length; continue; }
    // v3: bidang kuliah (Informatika/Elektrikal/Desain/Dasar) hanya diisi bila belum ada.
    if (u.bidang === undefined && d.bidang) u.bidang = d.bidang;
    if (dari < 4) {
      // v4: semester yang terkonfirmasi dari folder D:\Semester N, dan sub-materi baru (misal KDM, Visualisasi Data).
      if (u.semesterPasti === false && d.semesterPasti === true && u.semester === d.semester) u.semesterPasti = true;
      if (dari >= 2) {
        u.sub = Array.isArray(u.sub) ? u.sub : [];
        for (const s of subsOf(d)) if (!u.sub.some((x) => String(x.no) === String(s.no))) { u.sub.push(s); addS++; }
      }
    }
    if (dari >= 2) continue;
    if (d.alias && u.nama === d.alias) { u.alias = u.nama; u.nama = d.nama; }
    if (SEM_V1[d.id] !== undefined && u.semester === SEM_V1[d.id]) u.semester = d.semester;
    for (const k of ["sumber", "semesterPasti", "pengantar"]) if (u[k] === undefined && d[k] !== undefined) u[k] = d[k];
    u.sub = Array.isArray(u.sub) ? u.sub : [];
    for (const s of subsOf(d)) if (!u.sub.some((x) => String(x.no) === String(s.no) && x.nama === s.nama)) { u.sub.push(s); addS++; }
  }
  for (const d of def.alat) {
    const u = alatById(d.id);
    if (!u) { S.alat.push(d); addA++; continue; }
    if (u.ilustrasi === undefined && d.ilustrasi) u.ilustrasi = d.ilustrasi;
    if (dari >= 2 && dari < 4) {
      // v4: mata kuliah baru yang berperan pada alat lama (dari studi kasus modul).
      u.kontribusi = u.kontribusi || [];
      for (const dk of d.kontribusi || []) if (!u.kontribusi.some((k) => k.materi === dk.materi)) { u.kontribusi.push(dk); addK++; }
    }
    if (dari >= 2) continue;
    for (const k of ["referensi", "model", "sumber"]) if (u[k] === undefined && d[k] !== undefined) u[k] = d[k];
    if (Array.isArray(d.referensi)) for (const r of d.referensi) if (!u.referensi.includes(r)) u.referensi.push(r);
    u.kontribusi = u.kontribusi || [];
    for (const dk of d.kontribusi || []) {
      const uk = u.kontribusi.find((k) => k.materi === dk.materi);
      if (!uk) { u.kontribusi.push(dk); addK++; continue; }
      uk.sub = Array.isArray(uk.sub) ? uk.sub : [];
      for (const s of dk.sub || []) if (!uk.sub.includes(s)) uk.sub.push(s);
    }
  }
  // Proyek, soal, studi lanjutan, modul, referensi, dan kisah: tambahkan yang belum ada, milik pengguna tidak disentuh.
  const KONTEN = ["proyek", "soal", "lanjutan", "modul", "referensi", "kisah"];
  const tambah = {};
  for (const k of KONTEN) {
    tambah[k] = 0;
    for (const d of def[k] || []) if (!byId(S[k], d.id)) { S[k].push(d); tambah[k]++; }
  }
  S.progres.versiKonten = VERSI_KONTEN;
  let ok = (await save("materi")) && (await save("alat"));
  for (const k of KONTEN) if (tambah[k]) ok = ok && (await save(k));
  ok = ok && (await save("progres"));
  const bagian = [[addM, "mata kuliah"], [addS, "sub-materi"], [addA, "alat"], [addK, "keterkaitan"], [tambah.proyek, "proyek"], [tambah.soal, "soal"], [tambah.lanjutan, "studi lanjutan"], [tambah.modul, "modul materi"], [tambah.referensi, "referensi"], [tambah.kisah, "kisah"]].filter(([n]) => n).map(([n, l]) => `+${n} ${l}`);
  if (ok) toast(`Konten diperbarui ke v${VERSI_APP}${bagian.length ? ": " + bagian.join(", ") : ""}. Data lama tetap utuh.`);
}

/* ---------- status belajar ---------- */
const subDone = (mid, no) => !!S.progres.sub[subKey(mid, no)];
function computedStatus(mid) {
  const subs = subsOf(materiById(mid));
  if (!subs.length) return null;
  const n = subs.filter((s) => subDone(mid, s.no)).length;
  return n === 0 ? "belum" : n === subs.length ? "sudah" : "sedang";
}
const statusOf = (id) => S.progres.status[id] || computedStatus(id) || "belum";
function setStatus(mid, st) { S.progres.status[mid] = st; saveLater("progres", 300); }
function toggleSub(mid, no) {
  const k = subKey(mid, no);
  if (S.progres.sub[k]) delete S.progres.sub[k]; else S.progres.sub[k] = true;
  // Status mata kuliah mengikuti sub-materi yang dicentang.
  S.progres.status[mid] = computedStatus(mid);
  saveLater("progres", 300);
}
function subProgress(m) {
  const subs = subsOf(m);
  const n = subs.filter((s) => subDone(m.id, s.no)).length;
  return { n, total: subs.length, pct: subs.length ? Math.round((n / subs.length) * 100) : 0 };
}

/* ---------- kesiapan alat ---------- */
// Tiap kontribusi berbobot tingkat (1–3). Nilainya 1 bila mata kuliah "sudah",
// atau proporsi sub-materi terkait yang sudah dicentang, atau 0,5 bila "sedang".
function nilaiKontribusi(k) {
  const st = statusOf(k.materi);
  if (st === "sudah") return 1;
  const subs = (k.sub || []).filter((no) => findSub(materiById(k.materi), no));
  if (subs.length) return subs.filter((no) => subDone(k.materi, no)).length / subs.length;
  return st === "sedang" ? 0.5 : 0;
}
function kesiapan(alat) {
  const k = (alat.kontribusi || []).filter((x) => materiById(x.materi));
  const total = k.reduce((s, x) => s + (+x.tingkat || 1), 0);
  if (!total) return 0;
  return Math.round((k.reduce((s, x) => s + (+x.tingkat || 1) * nilaiKontribusi(x), 0) / total) * 100);
}
const alatPakaiMateri = (mid) => S.alat.filter((a) => (a.kontribusi || []).some((k) => k.materi === mid));
const alatPakaiSub = (mid, no) => S.alat.filter((a) => (a.kontribusi || []).some((k) => k.materi === mid && (k.sub || []).map(String).includes(String(no))));
const progressMateri = (list) => (list.length ? Math.round((list.filter((m) => statusOf(m.id) === "sudah").length / list.length) * 100) : 0);

/* ---------- pengaturan tampilan ---------- */
function applySettings() {
  const p = S.progres.pengaturan || {};
  let theme = p.tema || "sistem";
  try { const t = localStorage.getItem("tema"); if (t && !p.tema) theme = t; } catch (e) {}
  if (theme === "sistem") document.documentElement.removeAttribute("data-theme");
  else document.documentElement.setAttribute("data-theme", theme === "gelap" ? "dark" : "light");
  document.documentElement.style.setProperty("--fs", (p.ukuranHuruf || 15) + "px");
  document.documentElement.classList.toggle("no-anim", p.animasi === false);
}
const sapaan = () => (S.progres.pengaturan || {}).sapaan || "Tuan Raihan";

/* ---------- navigasi ---------- */
function renderNav(route) {
  const item = ([h, i, l, on, n]) => `<a class="nav-item${on ? " active" : ""}" href="${h}" title="${l}">${ico(i)}<span>${l}</span>${n != null ? `<em class="nav-badge">${n}</em>` : ""}</a>`;
  const L = (S.progres.latihan || {});
  const groups = [
    ["Jelajahi", [
      ["#/", "home", "Beranda", route === ""],
      ["#/alat", "alat", "Alat Medis", route.startsWith("alat"), S.alat.length],
      ["#/materi", "materi", "Materi Kuliah", route.startsWith("materi"), S.materi.length],
      ["#/peta", "peta", "Peta Keterkaitan", route.startsWith("peta")],
      ["#/referensi", "ref", "Referensi", route.startsWith("referensi"), S.referensi.length || null],
    ]],
    ["Belajar", [
      ["#/proyek", "proyek", "Proyek Hands-on", route.startsWith("proyek"), S.proyek.length],
      ["#/latihan", "latihan", "Latihan Soal", route.startsWith("latihan"), L.salah && L.salah.length ? L.salah.length + " ulang" : null],
      ...(S.kisah || []).map((k) => [`#/kisah/${esc(k.id)}`, "kisah", esc(k.singkat), route.startsWith("kisah/" + k.id), `${kisahN(k)}/${k.bab.length}`]),
    ]],
    ["Studi Lanjutan", (S.lanjutan || []).map((l) => [`#/lanjutan/${esc(l.id)}`, ICON[l.id] ? l.id : "materi", esc(l.nama), route === "lanjutan/" + l.id])],
  ];
  $("#nav").innerHTML = groups.filter(([, it]) => it.length).map(([g, it]) => `<div class="nav-label">${g}</div>` + it.map(item).join("")).join("");
  $("#navBottom").innerHTML = `<div class="nav-sep"></div>` + [
    ["#/kelola", "kelola", "Kelola Konten", route.startsWith("kelola")],
    ["#/pengaturan", "setting", "Pengaturan", route.startsWith("pengaturan")],
  ].map(item).join("");
  // Menu bawah untuk layar HP; "Menu" membuka sidebar sebagai laci.
  const utama = [["#/", "home", "Beranda", route === ""], ["#/alat", "alat", "Alat", route.startsWith("alat")],
    ["#/proyek", "proyek", "Proyek", route.startsWith("proyek")], ["#/latihan", "latihan", "Latihan", route.startsWith("latihan")]];
  const lain = !utama.some((x) => x[3]);
  $("#tabBar").innerHTML = utama.map(([h, i, l, on]) => `<a class="tab${on ? " active" : ""}" href="${h}">${ico(i)}<span>${l}</span></a>`).join("")
    + `<button class="tab${lain ? " active" : ""}" id="menuBtn">${ico("list")}<span>Menu</span></button>`;
  document.body.classList.remove("laci");
}

// Halaman induk dipakai tombol Kembali bila riwayat kosong (misalnya baru membuka aplikasi).
function induk(path) {
  if (!path) return null;
  const p = path.split("?")[0].split("/");
  if (p[0] === "kelola" && p[1]) return p[2] && p[2] !== "baru" ? `${p[1]}/${p[2]}` : "kelola";
  if (p[0] === "latihan" && p[1]) return "latihan";
  if (p[0] === "lanjutan") return "";
  if (p.length > 1 || path.includes("?")) return p[0];
  return "";
}
const nav = { stack: [], dir: 1 };
function goBack() {
  if (nav.stack.length > 1) { history.back(); return; }
  const cur = location.hash.replace(/^#\/?/, "");
  const up = induk(cur);
  location.hash = "#/" + (up || "");
}
function renderBack(path) {
  const b = $("#backBtn");
  if (!b) return;
  b.hidden = path === "";
  const up = induk(path);
  b.title = nav.stack.length > 1 ? "Kembali ke halaman sebelumnya (Alt + ←)" : `Kembali ke ${up ? up.split("/")[0] : "Beranda"}`;
}

const routes = [];
const route = (re, fn) => routes.push([re, fn]);

function router() {
  const path = location.hash.replace(/^#\/?/, "");
  // Catat riwayat sendiri agar tombol Kembali tahu apakah ada halaman sebelumnya.
  const i = nav.stack.lastIndexOf(path);
  if (i >= 0 && i === nav.stack.length - 2) { nav.stack.pop(); nav.dir = -1; }
  else if (nav.stack[nav.stack.length - 1] !== path) { nav.stack.push(path); nav.dir = 1; }
  renderNav(path);
  renderBack(path);
  closeSearch();
  // Ganti elemen view agar event listener halaman sebelumnya ikut terbuang.
  const old = $("#view");
  const view = old.cloneNode(false);
  view.classList.remove("enter", "enter-back");
  old.replaceWith(view);
  for (const [re, fn] of routes) {
    const m = path.match(re);
    if (m) {
      fn(view, ...m.slice(1).map((x) => (x == null ? x : decodeURIComponent(x))));
      view.scrollTop = 0;
      view.classList.add(nav.dir < 0 ? "enter-back" : "enter");
      if (typeof revealIn === "function") revealIn(view);
      const errs = Object.values(S.errors || {});
      if (errs.length) view.insertAdjacentHTML("afterbegin", `<div class="page" style="margin-bottom:16px">${errs.map((e) => `<div class="banner">${esc(e)}</div>`).join("")}</div>`);
      view.addEventListener("click", (e) => { const u = e.target.closest("[data-url]"); if (u) { e.preventDefault(); openUrl(u.dataset.url); } });
      return;
    }
  }
  location.hash = "#/";
}

/* ---------- komponen ---------- */
function statusBtn(mid) {
  const st = statusOf(mid);
  return `<button class="status-btn s-${st}" data-status="${esc(mid)}" title="Klik untuk mengubah status belajar"><span class="dot"></span>${STATUS[st]}</button>`;
}
function bindStatus(root, after) {
  root.addEventListener("click", (e) => {
    const b = e.target.closest("[data-status]");
    if (!b) return;
    e.stopPropagation(); e.preventDefault();
    const id = b.dataset.status;
    setStatus(id, STATUS_NEXT[statusOf(id)]);
    $$(`[data-status="${CSS.escape(id)}"]`, root).forEach((el) => (el.outerHTML = statusBtn(id)));
    after && after();
  });
}
function subCheck(mid, s, extra = "") {
  return `<button class="sub-check${subDone(mid, s.no) ? " on" : ""}" data-sub="${esc(mid)}" data-no="${esc(s.no)}">
    <span class="box"></span><span class="no">${esc(s.no || "•")}</span>
    <span class="sname">${esc(s.nama)}${s.rincian ? `<span class="srinci">${esc(s.rincian)}</span>` : ""}${extra}</span></button>`;
}
function bindSubs(root, after) {
  root.addEventListener("click", (e) => {
    if (e.target.closest("[data-goto]")) return;
    const b = e.target.closest("[data-sub]");
    if (!b) return;
    e.preventDefault();
    toggleSub(b.dataset.sub, b.dataset.no);
    $$(`[data-sub="${CSS.escape(b.dataset.sub)}"][data-no="${CSS.escape(b.dataset.no)}"]`, root).forEach((el) => el.classList.toggle("on", subDone(b.dataset.sub, b.dataset.no)));
    $$(`[data-status="${CSS.escape(b.dataset.sub)}"]`, root).forEach((el) => (el.outerHTML = statusBtn(b.dataset.sub)));
    after && after();
  });
  root.addEventListener("click", (e) => { const g = e.target.closest("[data-goto]"); if (g) { e.preventDefault(); e.stopPropagation(); location.hash = g.dataset.goto; } });
}

function alatCard(a) {
  const p = kesiapan(a);
  const dots = (a.kontribusi || []).slice().sort((x, y) => y.tingkat - x.tingkat).map((k) => `<span class="dot t${k.tingkat}" title="${esc(materiById(k.materi)?.nama || k.materi)}"></span>`).join("");
  return `<a class="alat-card" href="#/alat/${esc(a.id)}">
    <div class="alat-thumb" style="--thumb-grad:${gradOf(a.kategori)}"><span class="kat">${esc(a.kategori || "")}</span>${gambarAlat(a)}</div>
    <div><h3>${esc(a.nama)}</h3><p class="desc">${esc(a.ringkasan)}</p></div>
    <div class="mini-dots">${dots}</div>
    <div class="foot"><span>${(a.kontribusi || []).length} mata kuliah</span><div class="bar"><i style="width:${p}%"></i></div><span>${p}%</span></div>
  </a>`;
}

function materiRow(m, compact) {
  const n = alatPakaiMateri(m.id).length;
  const sp = subProgress(m);
  const src = m.sumber === "Silabus ITS" ? "" : `<span class="badge-src">pelengkap</span>`;
  return `<a class="materi-row" href="#/materi/${esc(m.id)}">
    ${statusBtn(m.id)}
    <div><div class="name"><span class="bd-dot" style="--bd:${BIDANG[bidangOf(m)].warna}" title="${bidangOf(m)}"></span>${esc(m.nama)}${compact ? "" : src}</div>${compact ? "" : `<div class="meta">${bidangOf(m)} · ${esc(m.kategori || "")}${m.alias ? " · dulu: " + esc(m.alias) : ""}</div>`}</div>
    ${compact ? `<span class="muted" style="font-size:.8rem">${sp.total ? `${sp.n}/${sp.total}` : ""}</span>` :
      `<div class="subprog">${sp.total ? `<div class="bar"><i style="width:${sp.pct}%"></i></div>${sp.n}/${sp.total}` : `<span>tanpa sub-materi</span>`}</div>
       <span class="chip sem">${esc(semShort(m))}</span><span class="chip">${n} alat</span>`}
  </a>`;
}

function groupBySemester(list) {
  const g = {};
  list.forEach((m) => { const k = m.semester || 0; (g[k] = g[k] || []).push(m); });
  return Object.keys(g).map(Number).sort((a, b) => (a || 99) - (b || 99)).map((k) => [k, g[k]]);
}
const semHeadLabel = (s, list) => (s ? `Semester ${s}${list.some((m) => m.semesterPasti === false) ? " (sebagian perkiraan)" : ""}` : "Tanpa semester");

/* =========================================================
   BERANDA
   ========================================================= */
route(/^$/, (v) => {
  const sudah = S.materi.filter((m) => statusOf(m.id) === "sudah").length;
  const subTotal = S.materi.reduce((s, m) => s + subsOf(m).length, 0);
  const subDoneN = S.materi.reduce((s, m) => s + subProgress(m).n, 0);
  const top = S.alat.slice().sort((a, b) => kesiapan(b) - kesiapan(a)).slice(0, 8);
  const sedang = S.materi.filter((m) => statusOf(m.id) === "sedang").slice(0, 6);
  const saran = S.alat.slice(0, 6);
  const L = S.progres.latihan || {};
  const pj = S.proyek.filter((p) => (S.progres.proyek || {})[p.id] === "jalan");
  const pSelesai = S.proyek.filter((p) => (S.progres.proyek || {})[p.id] === "selesai").length;
  const proyekBerikut = pj[0] || S.proyek.find((p) => p.tahap === 1 && !(S.progres.proyek || {})[p.id]);
  const nStreak = typeof streak === "function" ? streak() : 0;
  const jam = new Date().getHours();
  const waktu = jam < 11 ? "pagi" : jam < 15 ? "siang" : jam < 19 ? "sore" : "malam";
  v.innerHTML = `<div class="page">
    <section class="hero">
      ${typeof heroEkgHtml === "function" ? heroEkgHtml() : ""}
      <span class="hero-badge"><i></i>Selamat ${waktu} · ${new Date().toLocaleDateString("id-ID", { weekday: "long", day: "numeric", month: "long" })}</span>
      <h1 class="hero-greet"><span>Selamat Datang ${esc(sapaan())},</span><span class="grad-text">Selamat Belajar</span></h1>
      <p>Pilih alat Teknologi Kedokteran untuk melihat komponennya dipecah dan mata kuliah yang membangunnya, lalu bangun prototipenya lewat proyek kecil.</p>
      <div class="prompt-card">
        <input id="heroSearch" placeholder="Cari alat, mata kuliah, atau sub-materi… misalnya “EEG” atau “filter digital”" autocomplete="off">
        <div class="prompt-row">${saran.map((a) => `<a class="chip outline" href="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</a>`).join("")}
          <button class="go" id="heroGo" title="Cari">${ico("send")}</button></div>
      </div>
      <div class="prompt-results card" id="heroResults" hidden></div>
      <div class="stats">
        <div class="stat"><b data-count="${S.alat.length}">${S.alat.length}</b><span>alat medis</span></div>
        <div class="stat"><b data-count="${S.materi.length}">${S.materi.length}</b><span>mata kuliah</span></div>
        <div class="stat"><b><span data-count="${subDoneN}">${subDoneN}</span><span style="font-size:1rem;color:var(--text-3)">/${subTotal}</span></b><span>sub-materi dikuasai</span></div>
        <div class="stat"><b data-count="${sudah}">${sudah}</b><span>mata kuliah tuntas</span></div>
      </div>
    </section>
    <section class="quick stagger">
      <a class="card quick-card" href="${proyekBerikut ? "#/proyek/" + esc(proyekBerikut.id) : "#/proyek"}" style="--i:0;--qc:#fe7b02">
        <span class="q-ico">${ico("proyek", 22)}</span><div><small>${pj.length ? "Lanjutkan proyek" : "Mulai proyek hands-on"}</small><b>${esc(proyekBerikut ? proyekBerikut.judul : "Proyek Hands-on")}</b>
        <span class="muted">${pSelesai} dari ${S.proyek.length} proyek selesai</span></div>${ico("arrow", 18)}</a>
      <a class="card quick-card" href="#/latihan" style="--i:1;--qc:#2483ff">
        <span class="q-ico">${ico("latihan", 22)}</span><div><small>Latihan soal</small><b>${nStreak ? `🔥 ${nStreak} hari beruntun` : "Mulai latihan hari ini"}</b>
        <span class="muted">${L.xp || 0} XP${L.salah && L.salah.length ? ` · ${L.salah.length} soal perlu diulang` : ""}</span></div>${ico("arrow", 18)}</a>
      ${(S.kisah || []).slice(0, 1).map((k) => { const n = kisahN(k), b = k.bab.find((x) => !kisahDone(k.id, x.id)); return `<a class="card quick-card" href="#/kisah/${esc(k.id)}${b && n ? "/" + esc(b.id) : ""}" style="--i:2;--qc:#ff66f4">
        <span class="q-ico">${ico("kue", 22)}</span><div><small>${n ? "Lanjutkan kisah" : "Baru: dari kode Oralytic"}</small><b>${esc(k.singkat)}${b && n ? ": " + esc(b.judul.split(":")[0]) : ""}</b>
        <span class="muted">${n} dari ${k.bab.length} bab dibaca</span></div>${ico("arrow", 18)}</a>`; }).join("")}
      ${(S.lanjutan || []).slice(0, (S.kisah || []).length ? 2 : 3).map((l, i) => `<a class="card quick-card sm" href="#/lanjutan/${esc(l.id)}" style="--i:${i + 3};--qc:${["#ff66f4", "#fe7b02", "#1f9d55"][i]}">
        <span class="q-ico">${ico(ICON[l.id] ? l.id : "materi", 22)}</span><div><small>Studi lanjutan</small><b>${esc(l.nama)}</b>
        <span class="muted">${(l.modul || []).filter((m) => (S.progres.lanjutan || {})[m.id]).length}/${(l.modul || []).length} modul</span></div></a>`).join("")}
    </section>
    ${typeof progresHtml === "function" ? progresHtml() : ""}
    <section class="section">
      <div class="section-head"><div><h2>Alat Teknologi Kedokteran</h2><span class="sub">Diurutkan dari yang paling siap kamu pahami.</span></div>
        <div class="right"><a class="btn" href="#/alat">Lihat semua ${S.alat.length} alat</a></div></div>
      ${S.alat.length ? `<div class="alat-grid">${top.map(alatCard).join("")}</div>` : `<div class="empty">Belum ada alat. <a class="btn primary sm" href="#/kelola/alat/baru">Tambah alat</a></div>`}
    </section>
    <section class="section">
      <div class="section-head"><div><h2>Sedang dipelajari</h2><span class="sub">${sedang.length ? "Lanjutkan dari sini." : "Centang sub-materi di halaman mata kuliah untuk mulai melacak."}</span></div>
        <div class="right"><a class="btn" href="#/materi">Semua mata kuliah</a></div></div>
      ${sedang.length ? `<div class="card"><div class="materi-list">${sedang.map((m) => materiRow(m)).join("")}</div></div>` : ""}
    </section>
  </div>`;
  bindStatus(v);
  if (typeof countUp === "function") countUp($(".hero", v));
  if (typeof bindProgres === "function") bindProgres(v);
  const inp = $("#heroSearch", v), box = $("#heroResults", v);
  const run = () => { const html = searchHtml(inp.value); box.hidden = !html; box.innerHTML = html || ""; };
  inp.addEventListener("input", run);
  inp.addEventListener("keydown", (e) => { if (e.key === "Enter") { const f = $(".sr-item", box); if (f) location.hash = f.dataset.href; } });
  $("#heroGo", v).onclick = () => { run(); const f = $(".sr-item", box); if (f) location.hash = f.dataset.href; else inp.focus(); };
  box.addEventListener("click", (e) => { const it = e.target.closest(".sr-item"); if (it) location.hash = it.dataset.href; });
});

/* =========================================================
   DAFTAR ALAT
   ========================================================= */
route(/^alat$/, (v) => {
  const kats = ["Semua", ...new Set(S.alat.map((a) => a.kategori).filter(Boolean))];
  const draw = () => {
    const list = S.alat.filter((a) => ui.alatFilter === "Semua" || a.kategori === ui.alatFilter);
    v.innerHTML = `<div class="page">
      <div class="section-head"><div><h1>Alat Medis</h1><span class="sub">Pilih alat untuk melihat breakdown mata kuliah dan sub-materi yang membangunnya.</span></div>
        <div class="right"><div class="seg"><button data-view="grid" class="${ui.alatView === "grid" ? "on" : ""}" title="Kartu">${ico("grid")}</button><button data-view="list" class="${ui.alatView === "list" ? "on" : ""}" title="Tabel">${ico("list")}</button></div>
        <a class="btn primary" href="#/kelola/alat/baru">${ico("plus")} Tambah alat</a></div></div>
      <div class="chips">${kats.map((k) => `<button class="chip filter-chip${ui.alatFilter === k ? " on" : ""}" data-kat="${esc(k)}">${esc(k)}${k === "Semua" ? "" : ` · ${S.alat.filter((a) => a.kategori === k).length}`}</button>`).join("")}</div>
      ${!list.length ? `<div class="empty">Tidak ada alat pada kategori ini.</div>` : ui.alatView === "grid" ? `<div class="alat-grid">${list.map(alatCard).join("")}</div>` :
      `<div class="card"><table class="list-table"><thead><tr><th></th><th>Alat</th><th>Kategori</th><th>Mata kuliah</th><th>Mata kuliah inti</th><th style="width:200px">Kesiapan</th></tr></thead><tbody>
      ${list.map((a) => { const p = kesiapan(a); return `<tr class="click" data-href="#/alat/${esc(a.id)}"><td style="font-size:22px;width:48px">${esc(a.ikon || "🔧")}</td><td><b>${esc(a.nama)}</b><div class="muted" style="font-size:.85rem">${esc(a.singkatan || "")}${a.model ? " · " + esc(a.model) : ""}</div></td><td>${esc(a.kategori)}</td><td>${(a.kontribusi || []).length}</td>
        <td style="font-size:.86rem;color:var(--text-2)">${(a.kontribusi || []).filter((k) => k.tingkat == 3).map((k) => esc(materiById(k.materi)?.nama || k.materi)).join(", ")}</td>
        <td><div style="display:flex;gap:8px;align-items:center"><div class="bar" style="flex:1"><i style="width:${p}%"></i></div>${p}%</div></td></tr>`; }).join("")}
      </tbody></table></div>`}
    </div>`;
  };
  v.addEventListener("click", (e) => {
    const k = e.target.closest("[data-kat]"); if (k) { ui.alatFilter = k.dataset.kat; draw(); }
    const w = e.target.closest("[data-view]"); if (w) { ui.alatView = w.dataset.view; draw(); }
    const r = e.target.closest("[data-href]"); if (r) location.hash = r.dataset.href;
  });
  draw();
});

/* =========================================================
   DETAIL ALAT (sorotan utama)
   ========================================================= */
route(/^alat\/([^/]+)$/, (v, id) => {
  const a = alatById(id);
  if (!a) { v.innerHTML = `<div class="page"><div class="empty">Alat tidak ditemukan. <a href="#/alat">Kembali</a></div></div>`; return; }
  ui.selBlok = null;
  const blok = a.blok || [];
  const kontrib = (a.kontribusi || []).filter((k) => materiById(k.materi));
  const blokNama = (bid) => byId(blok, bid)?.nama || bid;

  const drawReady = () => {
    const p = kesiapan(a);
    const r = $("#readyRing", v);
    if (r) { r.style.setProperty("--p", p); r.dataset.label = p + "%"; }
    const subRefs = kontrib.flatMap((k) => (k.sub || []).map((no) => [k.materi, no])).filter(([m, no]) => findSub(materiById(m), no));
    const c = $("#readyCount", v);
    if (c) c.textContent = subRefs.length
      ? `${subRefs.filter(([m, no]) => subDone(m, no) || statusOf(m) === "sudah").length} dari ${subRefs.length} sub-materi dikuasai`
      : `${kontrib.filter((k) => statusOf(k.materi) === "sudah").length} dari ${kontrib.length} mata kuliah tuntas`;
  };

  const semMap = {};
  kontrib.forEach((k) => { const s = materiById(k.materi).semester || 0; (semMap[s] = semMap[s] || { 3: 0, 2: 0, 1: 0 })[k.tingkat || 1]++; });
  const semKeys = Object.keys(semMap).map(Number).sort((x, y) => (x || 99) - (y || 99));
  const semMax = Math.max(1, ...semKeys.map((s) => semMap[s][1] + semMap[s][2] + semMap[s][3]));
  const groups = [3, 2, 1].map((t) => [t, kontrib.filter((k) => (+k.tingkat || 1) === t).sort((x, y) => (materiById(x.materi).semester || 99) - (materiById(y.materi).semester || 99))]).filter(([, l]) => l.length);

  v.innerHTML = `<div class="page">
    <div class="breadcrumb"><a href="#/alat">Alat Medis</a><span>/</span><span>${esc(a.kategori || "")}</span><span>/</span><span style="color:var(--text)">${esc(a.nama)}</span></div>
    ${anatomiHtml(a)}
    ${typeof breakdownHtml === "function" ? breakdownHtml(a) : ""}
    <section class="card detail-head" style="--thumb-grad:${gradOf(a.kategori)}">
      <div class="alat-ico">${esc(a.ikon || "🔧")}</div>
      <div class="info">
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><h1>${esc(a.nama)}</h1>${a.singkatan ? `<span class="chip dark">${esc(a.singkatan)}</span>` : ""}<span class="chip outline">${esc(a.kategori || "")}</span></div>
        <p>${esc(a.ringkasan)}</p>
        ${a.model ? `<p style="font-size:.9rem;color:var(--text-3)">Model yang dicatat: ${esc(a.model)}</p>` : ""}
      </div>
      <div class="ready">
        <div class="ring" id="readyRing" style="--p:0" data-label="0%"></div>
        <div><b>Kesiapan kamu</b><small id="readyCount"></small>
          <div style="display:flex;gap:6px;flex-wrap:wrap;margin-top:8px"><a class="btn sm primary" href="#/latihan/alat/${esc(a.id)}">${ico("latihan")} Latihan soal</a><a class="btn sm" href="#/kelola/alat/${esc(a.id)}">${ico("edit")} Edit</a></div></div>
      </div>
    </section>

    <div class="detail-grid">
      <div class="section">
        <section class="card">
          <div class="section-head" style="padding:22px 22px 14px"><div><h2>Diagram blok alat</h2><span class="sub">Klik blok untuk menyaring mata kuliah yang membangunnya.</span></div>
            <div class="right"><button class="btn sm" id="clearBlok" hidden>Tampilkan semua</button></div></div>
          <div class="flow-wrap"><div class="flow" id="flow">
            ${blok.map((b, i) => {
              const ks = kontrib.filter((k) => (k.blok || []).includes(b.id)).sort((x, y) => y.tingkat - x.tingkat);
              return `${i ? `<div class="flow-arrow">${ico("arrow")}</div>` : ""}<button class="blok" data-blok="${esc(b.id)}">
                <span class="bn">Blok ${i + 1}</span><h4>${esc(b.nama)}</h4><p>${esc(b.fungsi || "")}</p>
                <div class="mini-dots">${ks.map((k) => `<span class="dot t${k.tingkat}" title="${esc(materiById(k.materi).nama)}"></span>`).join("")}</div></button>`;
            }).join("") || `<div class="empty" style="flex:1">Belum ada blok. Tambahkan lewat Edit alat.</div>`}
          </div></div>
          ${a.umpanBalik ? `<div class="flow-hint">${ico("loop", 18)} Alat ini memakai kendali umpan balik: hasil sensor dipakai lagi untuk mengatur aktuator.</div>` : ""}
          ${a.keselamatan ? `<div class="safety-bar">${ico("shield", 18)} Keselamatan &amp; daya berlaku untuk semua blok</div>` : ""}
          <div class="flow-hint"><span class="legend"><span class="dot t3"></span> Inti</span><span class="legend"><span class="dot t2"></span> Penting</span><span class="legend"><span class="dot t1"></span> Pendukung</span><span>Titik pada blok = mata kuliah yang berperan di blok itu.</span></div>
        </section>

        <section class="card">
          <div class="section-head" style="padding:22px 22px 4px"><div><h2>Breakdown materi kuliah</h2><span class="sub" id="bdSub">${kontrib.length} mata kuliah berkontribusi. Centang sub-materi yang sudah kamu kuasai.</span></div></div>
          ${groups.map(([t, list]) => `<div class="kontrib-group"><div class="kg-head"><span class="dot t${t}"></span>${TINGKAT[t]} · ${list.length}</div>
            ${list.map((k) => { const m = materiById(k.materi); const subs = (k.sub || []).map((no) => findSub(m, no)).filter(Boolean); return `<div class="kontrib" data-k="${esc(k.materi)}" data-bloks="${esc((k.blok || []).join(" "))}">
              <div class="num t${t}">${esc(semShort(m))}</div>
              <div><div class="title"><a href="#/materi/${esc(m.id)}">${esc(m.nama)}</a><span class="muted" style="font-size:.84rem">${esc(semLabel(m))}</span></div>
                <p class="peran">${esc(k.peran || "")}</p>
                ${(k.blok || []).length ? `<div class="chips">${k.blok.map((b) => `<span class="chip">${esc(blokNama(b))}</span>`).join("")}</div>` : ""}
                ${subs.length ? `<div class="sub-list">${subs.map((s) => subCheck(m.id, s)).join("")}</div>` : ""}</div>
              ${statusBtn(m.id)}</div>`; }).join("")}</div>`).join("") || `<div class="empty" style="margin:22px">Belum ada mata kuliah yang dihubungkan. Klik <b>Edit alat</b> untuk menambahkan.</div>`}
        </section>
        ${proyekTrack(a)}
      </div>

      <aside class="detail-side">
        <section class="card panel"><h3>Prinsip kerja</h3><p class="txt">${esc(a.prinsipKerja || "Belum diisi.")}</p></section>
        ${a.keselamatan ? `<section class="card panel warn"><h3>Keselamatan</h3><p class="txt">${esc(a.keselamatan)}</p></section>` : ""}
        <section class="card panel"><h3>Mata kuliah per semester</h3><p class="muted" style="font-size:.85rem">Kapan bekal untuk alat ini kamu dapatkan.</p>
          <div class="sem-bars">${semKeys.map((s) => { const c = semMap[s]; return `<div class="sem-bar"><span>${s ? "Semester " + s : "Lainnya"}</span><div class="track">
            ${[3, 2, 1].map((t) => c[t] ? `<i class="t${t}" style="width:${(c[t] / semMax) * 100}%"></i>` : "").join("")}</div><b>${c[1] + c[2] + c[3]}</b></div>`; }).join("")}</div></section>
        ${typeof kisahPanelHtml === "function" ? kisahPanelHtml({ alat: a.id }) : ""}
        ${refPanelHtml(a.referensi, refPakaiAlat(a.id), "#/referensi?alat=" + encodeURIComponent(a.id))}
        ${typeof bacaanHtml === "function" ? bacaanHtml((b) => (b.alat || []).includes(a.id), a.singkatan || a.nama) : ""}
        <section class="card panel"><h3>Catatan pribadi</h3><textarea class="notes" id="alatNotes" placeholder="Catatan praktikum, pertanyaan, atau link referensi…">${esc(a.catatan || "")}</textarea><span class="muted" style="font-size:.8rem">Tersimpan otomatis.</span></section>
      </aside>
    </div>
  </div>`;

  drawReady();
  bindStatus(v, drawReady);
  bindSubs(v, drawReady);

  const flow = $("#flow", v);
  const highlight = (bloks) => {
    $$(".blok", v).forEach((b) => b.classList.toggle("hl", bloks.includes(b.dataset.blok)));
    flow.classList.toggle("dim", bloks.length > 0 || !!ui.selBlok);
  };
  const applySel = () => {
    $$(".blok", v).forEach((b) => b.classList.toggle("sel", b.dataset.blok === ui.selBlok));
    let n = 0;
    $$(".kontrib", v).forEach((r) => { const on = !ui.selBlok || r.dataset.bloks.split(" ").includes(ui.selBlok); r.classList.toggle("faded", !on); if (on) n++; });
    $$(".kontrib-group", v).forEach((g) => g.classList.toggle("faded", !$$(".kontrib:not(.faded)", g).length));
    $("#clearBlok", v).hidden = !ui.selBlok;
    $("#bdSub", v).textContent = ui.selBlok ? `${n} mata kuliah berperan di blok "${blokNama(ui.selBlok)}"` : `${kontrib.length} mata kuliah berkontribusi. Centang sub-materi yang sudah kamu kuasai.`;
    flow.classList.toggle("dim", !!ui.selBlok);
  };
  flow.addEventListener("click", (e) => { const b = e.target.closest(".blok"); if (!b) return; ui.selBlok = ui.selBlok === b.dataset.blok ? null : b.dataset.blok; applySel(); });
  $("#clearBlok", v).onclick = () => { ui.selBlok = null; applySel(); };
  $$(".kontrib", v).forEach((r) => {
    r.addEventListener("mouseenter", () => highlight(r.dataset.bloks.split(" ").filter(Boolean)));
    r.addEventListener("mouseleave", () => { highlight([]); applySel(); });
  });
  $("#alatNotes", v).addEventListener("input", (e) => { a.catatan = e.target.value; saveLater("alat", 800); });
  if (typeof bindBreakdown === "function") bindBreakdown(v, a);
  bindAnatomi(v, a, (bid) => {
    ui.selBlok = ui.selBlok === bid ? null : bid;
    applySel();
    if (ui.selBlok) $("#bdSub", v).closest(".card").scrollIntoView({ behavior: reduceMotion() ? "auto" : "smooth", block: "start" });
  });
});

/* =========================================================
   DAFTAR MATERI
   ========================================================= */
route(/^materi$/, (v) => {
  const kats = ["Semua", ...new Set(S.materi.map((m) => m.kategori).filter(Boolean))];
  const draw = () => {
    const list = S.materi.filter((m) => (ui.materiFilter === "Semua" || m.kategori === ui.materiFilter)
      && (ui.bidangFilter === "Semua" || bidangOf(m) === ui.bidangFilter)
      && (ui.sumberFilter === "Semua" || (ui.sumberFilter === "Silabus ITS") === (m.sumber === "Silabus ITS"))
      && (ui.statusFilter === "semua" || statusOf(m.id) === ui.statusFilter));
    v.innerHTML = `<div class="page">
      <div class="section-head"><div><h1>Materi Kuliah</h1><span class="sub">Mata kuliah beserta sub-materinya. Kesiapan tiap alat dihitung dari sub-materi yang kamu centang.</span></div>
        <div class="right"><a class="btn primary" href="#/kelola/materi/baru">${ico("plus")} Tambah mata kuliah</a></div></div>
      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
        <div class="seg">${["Semua", "Silabus ITS", "Pelengkap"].map((s) => `<button data-src="${s}" class="${ui.sumberFilter === s ? "on" : ""}">${s}</button>`).join("")}</div>
        <div class="seg">${["Semua", ...BIDANG_URUT].map((b) => `<button data-bdf="${b}" class="${ui.bidangFilter === b ? "on" : ""}">${b === "Semua" ? "Semua bidang" : `<span class="dot" style="background:${BIDANG[b].warna}"></span>${b} · ${S.materi.filter((m) => bidangOf(m) === b).length}`}</button>`).join("")}</div>
        <div class="seg" style="margin-left:auto">${["semua", "belum", "sedang", "sudah"].map((s) => `<button data-st="${s}" class="${ui.statusFilter === s ? "on" : ""}">${s === "semua" ? "Semua status" : `<span class="dot" style="background:var(--${s})"></span>${STATUS[s].split(" ")[0]}`}</button>`).join("")}</div>
      </div>
      <div class="chips">${kats.map((k) => `<button class="chip filter-chip${ui.materiFilter === k ? " on" : ""}" data-kat="${esc(k)}">${esc(k)}</button>`).join("")}</div>
      ${list.length ? `<div class="card"><div class="materi-list">${groupBySemester(list).map(([s, l]) =>
        `<div class="sem-head">${esc(semHeadLabel(s, l))} <span class="muted">· ${l.length} mata kuliah</span><div class="bar"><i style="width:${progressMateri(l)}%"></i></div></div>${l.map((m) => materiRow(m)).join("")}`).join("")}</div></div>` : `<div class="empty">Tidak ada mata kuliah yang cocok dengan filter.</div>`}
      <p class="muted" style="font-size:.85rem">"Pelengkap" = mata kuliah umum dari versi awal aplikasi, disimpan agar tidak ada materi yang hilang. "(perkiraan)" = semester ditebak dari urutan silabus; ubah lewat Kelola Konten bila berbeda.</p>
    </div>`;
  };
  v.addEventListener("click", (e) => {
    const k = e.target.closest("[data-kat]"); if (k) { ui.materiFilter = k.dataset.kat; draw(); }
    const s = e.target.closest("[data-st]"); if (s) { ui.statusFilter = s.dataset.st; draw(); }
    const r = e.target.closest("[data-src]"); if (r) { ui.sumberFilter = r.dataset.src; draw(); }
    const b = e.target.closest("[data-bdf]"); if (b) { ui.bidangFilter = b.dataset.bdf; draw(); }
  });
  bindStatus(v, () => { if (ui.statusFilter !== "semua") draw(); });
  draw();
});

/* =========================================================
   DETAIL MATERI (mata kuliah + sub-materi)
   ========================================================= */
route(/^materi\/([^/]+)$/, (v, id) => {
  const m = materiById(id);
  if (!m) { v.innerHTML = `<div class="page"><div class="empty">Materi tidak ditemukan. <a href="#/materi">Kembali</a></div></div>`; return; }
  const used = alatPakaiMateri(m.id).map((a) => [a, a.kontribusi.find((k) => k.materi === m.id)]).sort((x, y) => y[1].tingkat - x[1].tingkat);
  const subs = subsOf(m);
  const md = modulById(m.id);
  const nSoal = typeof soalMateri === "function" ? soalMateri(m.id).length : 0;
  const drawSeg = () => `<div class="seg" id="stSeg">${["belum", "sedang", "sudah"].map((s) => `<button data-set="${s}" class="${statusOf(m.id) === s ? "on" : ""}"><span class="dot" style="background:var(--${s})"></span>${STATUS[s]}</button>`).join("")}</div>`;
  const drawProg = () => { const sp = subProgress(m); const el = $("#subProg", v); if (el) el.innerHTML = sp.total ? `<div class="bar" style="flex:1"><i style="width:${sp.pct}%"></i></div><span>${sp.n} dari ${sp.total} sub-materi dikuasai</span>` : ""; };
  v.innerHTML = `<div class="page">
    <div class="breadcrumb"><a href="#/materi">Materi Kuliah</a><span>/</span><span>${esc(semLabel(m))}</span><span>/</span><span style="color:var(--text)">${esc(m.nama)}</span></div>
    <section class="card detail-head">
      <div class="alat-ico">${ico("materi", 34)}</div>
      <div class="info">
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><h1>${esc(m.nama)}</h1><span class="chip dark">${esc(semLabel(m))}</span>${bidangChip(bidangOf(m))}<span class="chip outline">${esc(m.kategori || "")}</span>${m.sumber !== "Silabus ITS" ? `<span class="chip outline">Pelengkap</span>` : ""}</div>
        ${m.alias ? `<p style="font-size:.9rem;color:var(--text-3)">Sebelumnya bernama "${esc(m.alias)}".</p>` : ""}
        <p>${esc(m.ringkasan || "")}</p>
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:4px">${drawSeg()}<a class="btn sm" href="#/kelola/materi/${esc(m.id)}">${ico("edit")} Edit</a></div>
        <div id="subProg" style="display:flex;gap:10px;align-items:center;font-size:.86rem;color:var(--text-3);max-width:520px"></div>
      </div>
      ${nSoal ? `<a class="btn primary hd-cta" href="#/latihan/materi/${esc(m.id)}">${ico("latihan")} Latihan ${nSoal} soal</a>` : ""}
    </section>
    ${md ? modulNavHtml(md, nSoal, (md.kuliah || []).length) : ""}
    <div class="detail-grid">
      <div class="section">
        ${md ? penjelasanHtml(m, md) + kasusHtml(m, md) + latihanMateriHtml(m) : ""}
        <section class="card panel" id="sec-sub"><div class="section-head"><div><h2>Sub-materi</h2><span class="sub">${subs.length ? `${m.pengantar ? esc(m.pengantar) + ". " : ""}Centang yang sudah kamu kuasai. Label di bawah tiap sub-materi = alat yang memakainya.` : "Belum ada sub-materi. Tambahkan lewat Edit."}</span></div></div>
          ${subs.length ? `<div class="sub-list">${subs.map((s) => { const al = alatPakaiSub(m.id, s.no); return subCheck(m.id, s, al.length ? `<span class="used">${al.map((a) => `<span class="chip" data-goto="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</span>`).join("")}</span>` : ""); }).join("")}</div>` : ""}
          ${(m.topik || []).length ? `<h3 style="margin-top:14px">Topik tambahan</h3><ul class="topik">${m.topik.map((t) => `<li>${esc(t)}</li>`).join("")}</ul>` : ""}
        </section>
        <section class="card panel"><h2>Dipakai pada ${used.length} alat</h2>
          ${used.length ? `<div class="used-grid">${used.map(([a, k]) => `<a class="card used-card" href="#/alat/${esc(a.id)}"><div class="alat-ico">${esc(a.ikon || "🔧")}</div>
            <div><div style="display:flex;gap:8px;align-items:center"><b>${esc(a.nama)}</b><span class="dot t${k.tingkat}" title="${TINGKAT[k.tingkat]}"></span><span class="muted" style="font-size:.8rem">${TINGKAT[k.tingkat]}</span></div><p>${esc(k.peran || "")}</p></div></a>`).join("")}</div>`
            : `<p class="muted">Belum dihubungkan ke alat mana pun. Hubungkan lewat <a href="#/kelola" class="link">Kelola Konten → Alat</a>.</p>`}
        </section>
        ${(() => { const ps = proyekPakaiMateri(m.id); return ps.length ? `<section class="card panel"><h2>Dipraktikkan di ${ps.length} proyek hands-on</h2><span class="muted" style="font-size:.9rem">Proyek kecil yang memakai ilmu mata kuliah ini.</span>
          <div class="ptrack">${ps.slice(0, 12).map((p, i) => proyekStep(p, i, true)).join("")}</div>${ps.length > 12 ? `<a class="btn sm" href="#/proyek">Lihat semua proyek</a>` : ""}</section>` : ""; })()}
      </div>
      <aside class="detail-side">
        ${md ? kuliahHtml(m, md) : ""}
        ${typeof kisahPanelHtml === "function" ? kisahPanelHtml({ materi: m.id }) : ""}
        ${refPanelHtml(m.referensi, refPakaiMateri(m.id), "#/referensi?q=" + encodeURIComponent(m.nama))}
        ${typeof bacaanHtml === "function" ? bacaanHtml((b) => (b.materi || []).includes(m.id), m.nama) : ""}
        <section class="card panel"><h3>Catatan pribadi</h3><textarea class="notes" id="mNotes" style="min-height:220px" placeholder="Ringkasan kuliah, rumus penting, tips ujian…">${esc(m.catatan || "")}</textarea><span class="muted" style="font-size:.8rem">Tersimpan otomatis.</span></section>
      </aside>
    </div>
  </div>`;
  drawProg();
  bindSubs(v, () => { drawProg(); $("#stSeg", v).outerHTML = drawSeg(); });
  v.addEventListener("click", (e) => { const b = e.target.closest("[data-set]"); if (!b) return; setStatus(m.id, b.dataset.set); $("#stSeg", v).outerHTML = drawSeg(); });
  $("#mNotes", v).addEventListener("input", (e) => { m.catatan = e.target.value; saveLater("materi", 800); });
  if (md) bindModul(v, m, md);
});

/* =========================================================
   PETA KETERKAITAN
   ========================================================= */
route(/^peta$/, (v) => {
  const rows = S.materi.filter((m) => alatPakaiMateri(m.id).length).sort((a, b) => (a.semester || 99) - (b.semester || 99));
  v.innerHTML = `<div class="page">
    <div class="section-head"><div><h1>Peta Keterkaitan</h1><span class="sub">Baris = mata kuliah yang dipakai alat, kolom = alat. Titik makin besar = peran makin inti. Klik titik untuk membuka alat.</span></div>
      <div class="right"><span class="legend"><span class="dot t3"></span> Inti</span><span class="legend"><span class="dot t2"></span> Penting</span><span class="legend"><span class="dot t1"></span> Pendukung</span></div></div>
    <div class="card matrix-wrap"><table class="matrix"><thead><tr><th>Mata kuliah</th>${S.alat.map((a) => `<th><a href="#/alat/${esc(a.id)}" title="${esc(a.nama)}"><span>${esc(a.ikon || "🔧")}</span><span>${esc(a.singkatan || a.nama)}</span></a></th>`).join("")}<th>Total</th></tr></thead>
    <tbody>${rows.map((m) => { let tot = 0; return `<tr><th><a href="#/materi/${esc(m.id)}">${esc(m.nama)}</a><small>${esc(semShort(m))}</small></th>${S.alat.map((a) => { const k = (a.kontribusi || []).find((x) => x.materi === m.id); if (k) tot++; return `<td>${k ? `<a href="#/alat/${esc(a.id)}" title="${esc(a.nama)}: ${esc(k.peran || "")}"><span class="dot t${k.tingkat}"></span></a>` : ""}</td>`; }).join("")}<td class="total">${tot}</td></tr>`; }).join("")}</tbody></table></div>
  </div>`;
});

/* =========================================================
   KELOLA KONTEN
   ========================================================= */
route(/^kelola$/, (v) => {
  const draw = () => {
    const t = ui.kelolaTab;
    v.innerHTML = `<div class="page">
      <div class="section-head"><div><h1>Kelola Konten</h1><span class="sub">Tambah dan ubah alat maupun mata kuliah. Perubahan langsung tersimpan ke folder data.</span></div>
        <div class="right"><a class="btn primary" href="#/kelola/${t}/baru">${ico("plus")} Tambah ${t === "alat" ? "alat" : "mata kuliah"}</a></div></div>
      <div class="seg tabs"><button class="${t === "alat" ? "on" : ""}" data-tab="alat">Alat (${S.alat.length})</button><button class="${t === "materi" ? "on" : ""}" data-tab="materi">Mata kuliah (${S.materi.length})</button></div>
      <div class="card">${t === "alat"
        ? S.alat.map((a, i) => `<div class="kelola-row"><div class="alat-ico">${esc(a.ikon || "🔧")}</div><div><b>${esc(a.nama)}</b><div class="muted" style="font-size:.84rem">${esc(a.kategori || "")} · ${(a.blok || []).length} blok · ${(a.kontribusi || []).length} mata kuliah</div></div>
            <div style="display:flex;gap:4px"><button class="btn sm ghost" data-move="${i}" data-dir="-1" title="Naikkan">${ico("up")}</button><button class="btn sm ghost" data-move="${i}" data-dir="1" title="Turunkan">${ico("down")}</button></div>
            <a class="btn sm" href="#/kelola/alat/${esc(a.id)}">${ico("edit")} Edit</a></div>`).join("") || `<div class="empty">Belum ada alat.</div>`
        : groupBySemester(S.materi).map(([s, l]) => `<div class="sem-head">${esc(semHeadLabel(s, l))}</div>${l.map((m) => `<div class="kelola-row"><div class="alat-ico">${ico("materi", 20)}</div><div><b>${esc(m.nama)}</b><div class="muted" style="font-size:.84rem">${esc(m.kategori || "")} · ${subsOf(m).length} sub-materi · dipakai ${alatPakaiMateri(m.id).length} alat</div></div><span></span>
            <a class="btn sm" href="#/kelola/materi/${esc(m.id)}">${ico("edit")} Edit</a></div>`).join("")}`).join("") || `<div class="empty">Belum ada mata kuliah.</div>`}
      </div>
    </div>`;
  };
  v.addEventListener("click", (e) => {
    const tb = e.target.closest("[data-tab]"); if (tb) { ui.kelolaTab = tb.dataset.tab; draw(); return; }
    const mv = e.target.closest("[data-move]");
    if (mv) { const i = +mv.dataset.move, j = i + +mv.dataset.dir; if (j < 0 || j >= S.alat.length) return; [S.alat[i], S.alat[j]] = [S.alat[j], S.alat[i]]; draw(); saveLater("alat", 400); }
  });
  draw();
});

const fld = (label, name, val, opt = {}) => `<div class="field"><label for="f_${name}">${label}</label>${
  opt.area ? `<textarea id="f_${name}" name="${name}" rows="${opt.rows || 3}" class="${opt.mono ? "mono" : ""}" placeholder="${esc(opt.ph || "")}">${esc(val)}</textarea>`
  : opt.select ? `<select id="f_${name}" name="${name}">${opt.select.map((o) => `<option value="${esc(o[0])}" ${String(o[0]) === String(val) ? "selected" : ""}>${esc(o[1])}</option>`).join("")}</select>`
  : `<input id="f_${name}" name="${name}" value="${esc(val)}" ${opt.list ? `list="${opt.list}"` : ""} type="${opt.type || "text"}" placeholder="${esc(opt.ph || "")}">`
}${opt.hint ? `<span class="hint">${opt.hint}</span>` : ""}</div>`;

// Sub-materi ditulis satu per baris: "39. Nama sub-materi: rincian"
const subsToText = (subs) => subs.map((s) => `${s.no ? s.no + ". " : ""}${s.nama}${s.rincian ? ": " + s.rincian : ""}`).join("\n");
function textToSubs(text) {
  return text.split("\n").map((l) => l.trim()).filter(Boolean).map((l) => {
    const m = l.match(/^([0-9]+[a-z]?)[.)]\s*(.*)$/i);
    let no = "", body = l;
    if (m) { no = m[1]; body = m[2]; }
    const i = body.indexOf(":");
    return i > 0 && i <= 90 ? { no, nama: body.slice(0, i).trim(), rincian: body.slice(i + 1).trim() } : { no, nama: body, rincian: "" };
  });
}

route(/^kelola\/materi\/([^/]+)$/, (v, id) => {
  const isNew = id === "baru";
  const orig = isNew ? null : materiById(id);
  if (!isNew && !orig) { location.hash = "#/kelola"; return; }
  const m = orig ? JSON.parse(JSON.stringify(orig)) : { nama: "", semester: "", kategori: "", ringkasan: "", sub: [], topik: [], referensi: [], catatan: "" };
  ui.kelolaTab = "materi";
  v.innerHTML = `<div class="page"><form class="form" id="fm" autocomplete="off">
    <div class="breadcrumb"><a href="#/kelola">Kelola Konten</a><span>/</span><span style="color:var(--text)">${isNew ? "Mata kuliah baru" : esc(m.nama)}</span></div>
    <h1>${isNew ? "Tambah mata kuliah" : "Edit mata kuliah"}</h1>
    <section class="card form-card">
      ${fld("Nama mata kuliah *", "nama", m.nama, { ph: "contoh: Komunikasi Data Medis" })}
      <div class="form-row">${fld("Semester", "semester", m.semester ?? "", { type: "number", ph: "1–8" })}${fld("Kategori", "kategori", m.kategori, { list: "katMateri", ph: "pilih atau ketik baru" })}${fld("Sumber", "sumber", m.sumber || "Silabus ITS", { select: [["Silabus ITS", "Silabus ITS"], ["Pelengkap", "Pelengkap"]] })}${fld("Bidang", "bidang", bidangOf(m), { select: BIDANG_URUT.map((b) => [b, b + " · " + BIDANG[b].ket]), hint: "Warna garis pada anatomi alat mengikuti bidang ini." })}</div>
      ${fld("Ringkasan", "ringkasan", m.ringkasan, { area: true, ph: "Apa yang dipelajari dan kenapa penting untuk alat medis." })}
      ${fld("Sub-materi", "sub", subsToText(subsOf(m)), { area: true, rows: 10, mono: true, hint: "Satu sub-materi per baris dengan format <b>nomor. Nama: rincian</b>, misalnya <code>218. Protokol HL7: struktur pesan, segmen</code>. Rincian setelah titik dua boleh dikosongkan. Jangan ubah nomor yang sudah ada, karena dipakai untuk menghubungkan ke alat." })}
      ${fld("Topik tambahan", "topik", (m.topik || []).join("\n"), { area: true, rows: 3, hint: "Opsional, satu per baris." })}
      ${fld("Referensi", "referensi", (m.referensi || []).join("\n"), { area: true, rows: 3, hint: "Buku, jurnal, atau link. Satu per baris." })}
    </section>
    <datalist id="katMateri">${[...new Set([...KATEGORI_MATERI, ...S.materi.map((x) => x.kategori).filter(Boolean)])].map((k) => `<option value="${esc(k)}">`).join("")}</datalist>
    <div class="form-actions">${isNew ? "" : `<button type="button" class="btn danger" id="del">${ico("trash")} Hapus</button>`}
      <div class="right"><a class="btn" href="${isNew ? "#/kelola" : "#/materi/" + esc(m.id)}">Batal</a><button class="btn primary lg" type="submit">Simpan</button></div></div>
  </form></div>`;
  const f = $("#fm", v);
  f.onsubmit = async (e) => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(f));
    if (!d.nama.trim()) { toast("Nama wajib diisi", true); return; }
    const semBaru = d.semester ? +d.semester : null;
    const out = Object.assign(orig || {}, {
      nama: d.nama.trim(), semester: semBaru, kategori: d.kategori.trim(), sumber: d.sumber, bidang: d.bidang, ringkasan: d.ringkasan.trim(),
      sub: textToSubs(d.sub),
      topik: d.topik.split("\n").map((s) => s.trim()).filter(Boolean), referensi: d.referensi.split("\n").map((s) => s.trim()).filter(Boolean),
    });
    if (orig && semBaru !== m.semester) out.semesterPasti = true;
    if (isNew) { out.id = uniqueId(out.nama, S.materi); out.catatan = ""; out.semesterPasti = true; S.materi.push(out); }
    if (await save("materi")) { toast("Mata kuliah tersimpan"); location.hash = "#/materi/" + out.id; }
  };
  const del = $("#del", v);
  if (del) del.onclick = async () => {
    const n = alatPakaiMateri(orig.id).length;
    if (!(await confirmDialog("Hapus mata kuliah?", `“${esc(orig.nama)}” akan dihapus${n ? ` dan dilepas dari <b>${n} alat</b> yang memakainya` : ""}. Salinan sebelumnya tersimpan sebagai materi.json.bak.`))) return;
    S.materi = S.materi.filter((x) => x !== orig);
    S.alat.forEach((a) => (a.kontribusi = (a.kontribusi || []).filter((k) => k.materi !== orig.id)));
    delete S.progres.status[orig.id];
    await save("materi"); if (n) await save("alat"); saveLater("progres");
    toast("Mata kuliah dihapus"); location.hash = "#/kelola";
  };
});

route(/^kelola\/alat\/([^/]+)$/, (v, id) => {
  const isNew = id === "baru";
  const orig = isNew ? null : alatById(id);
  if (!isNew && !orig) { location.hash = "#/kelola"; return; }
  const a = orig ? JSON.parse(JSON.stringify(orig)) : { nama: "", singkatan: "", kategori: "", ikon: "🔧", model: "", ringkasan: "", prinsipKerja: "", keselamatan: "", umpanBalik: false, blok: [], kontribusi: [], referensi: [], catatan: "" };
  a.blok = a.blok || []; a.kontribusi = a.kontribusi || []; a.referensi = a.referensi || [];
  ui.kelolaTab = "alat";
  const matOpts = () => S.materi.slice().sort((x, y) => (x.semester || 99) - (y.semester || 99)).map((m) => [m.id, `${semShort(m)} · ${m.nama}`]);

  const collect = () => {
    const f = $("#fa", v);
    ["nama", "singkatan", "kategori", "ikon", "model", "ringkasan", "prinsipKerja", "keselamatan", "ilustrasi"].forEach((k) => (a[k] = f.elements[k].value));
    a.referensi = f.elements.referensi.value.split("\n").map((s) => s.trim()).filter(Boolean);
    a.umpanBalik = f.elements.umpanBalik.checked;
    $$(".rep-blok", v).forEach((el, i) => { a.blok[i].nama = $("[data-f=nama]", el).value; a.blok[i].fungsi = $("[data-f=fungsi]", el).value; });
    $$(".rep-k", v).forEach((el, i) => {
      const k = a.kontribusi[i];
      k.materi = $("[data-f=materi]", el).value; k.tingkat = +$("[data-f=tingkat]", el).value; k.peran = $("[data-f=peran]", el).value;
      k.blok = $$("[data-f=blok]:checked", el).map((c) => c.value);
      k.sub = $$("[data-f=sub]:checked", el).map((c) => c.value);
    });
  };
  const drawRep = () => {
    a.blok.forEach((b, i) => { if (!b.id) b.id = uniqueId(b.nama || "blok-" + (i + 1), a.blok, b); });
    $("#blokRep", v).innerHTML = a.blok.map((b, i) => `<div class="rep-item rep-blok"><div class="rep-top">
        <span class="chip" style="margin-bottom:6px">Blok ${i + 1}</span>
        <div class="field"><label>Nama blok</label><input data-f="nama" value="${esc(b.nama)}" placeholder="contoh: Penguat Instrumentasi"></div>
        <div class="field" style="flex:2"><label>Fungsi</label><input data-f="fungsi" value="${esc(b.fungsi || "")}" placeholder="Apa yang dikerjakan blok ini"></div>
        <button type="button" class="btn sm ghost" data-bup="${i}" title="Geser kiri">${ico("up")}</button><button type="button" class="btn sm ghost" data-bdown="${i}" title="Geser kanan">${ico("down")}</button>
        <button type="button" class="btn sm ghost danger" data-bdel="${i}" title="Hapus blok">${ico("trash")}</button></div></div>`).join("") || `<p class="muted">Belum ada blok. Blok = bagian/subsistem alat, misalnya Sensor → Penguat → Filter → ADC → Tampilan.</p>`;
    $("#kRep", v).innerHTML = a.kontribusi.map((k, i) => { const mm = materiById(k.materi); const subs = subsOf(mm); return `<div class="rep-item rep-k"><div class="rep-top">
        ${fld("Mata kuliah", "m" + i, k.materi, { select: matOpts() }).replace("<select", '<select data-f="materi"')}
        <div class="field" style="flex:0 0 160px"><label>Tingkat peran</label><select data-f="tingkat">${[3, 2, 1].map((t) => `<option value="${t}" ${+k.tingkat === t ? "selected" : ""}>${TINGKAT[t]}</option>`).join("")}</select></div>
        <button type="button" class="btn sm ghost danger" data-kdel="${i}" title="Hapus">${ico("trash")}</button></div>
        <div class="field"><label>Peran mata kuliah ini pada alat</label><textarea data-f="peran" rows="2" placeholder="contoh: Merancang filter notch 50 Hz untuk membuang derau jala-jala">${esc(k.peran || "")}</textarea></div>
        <div class="field"><label>Berperan di blok</label><div class="check-list">${a.blok.map((b, bi) => `<label><input type="checkbox" data-f="blok" value="${esc(b.id)}" ${(k.blok || []).includes(b.id) ? "checked" : ""}>${esc(b.nama || "Blok " + (bi + 1))}</label>`).join("") || `<span class="muted">Tambahkan blok dulu di atas.</span>`}</div></div>
        <div class="field"><label>Sub-materi yang dipakai alat ini</label><div class="check-list">${subs.map((s) => `<label title="${esc(s.rincian || "")}"><input type="checkbox" data-f="sub" value="${esc(s.no)}" ${(k.sub || []).map(String).includes(String(s.no)) ? "checked" : ""}>${esc(subLabel(s))}</label>`).join("") || `<span class="muted">Mata kuliah ini belum punya sub-materi.</span>`}</div></div>
      </div>`; }).join("") || `<p class="muted">Belum ada mata kuliah yang dihubungkan.</p>`;
  };

  v.innerHTML = `<div class="page"><form class="form" id="fa" autocomplete="off">
    <div class="breadcrumb"><a href="#/kelola">Kelola Konten</a><span>/</span><span style="color:var(--text)">${isNew ? "Alat baru" : esc(a.nama)}</span></div>
    <h1>${isNew ? "Tambah alat medis" : "Edit alat"}</h1>
    <section class="card form-card"><h2>Informasi alat</h2>
      <div class="form-row">${fld("Nama alat *", "nama", a.nama, { ph: "contoh: Elektromiograf" })}${fld("Singkatan", "singkatan", a.singkatan, { ph: "EMG" })}</div>
      <div class="form-row">${fld("Kategori", "kategori", a.kategori, { list: "katAlat", ph: "pilih atau ketik baru" })}${fld("Ikon (emoji)", "ikon", a.ikon, { hint: "Tekan Win + . untuk memilih emoji.", ph: "🔧" })}${fld("Model/merek", "model", a.model || "", { ph: "opsional" })}</div>
      ${fld("Ringkasan", "ringkasan", a.ringkasan, { area: true, rows: 2 })}
      <div class="gambar-edit">
        <div class="mini-ilus lg" id="gPrev">${gambarAlat(a)}</div>
        <div class="gambar-fields">
          ${fld("Ilustrasi bawaan", "ilustrasi", a.ilustrasi || "monitor", { select: Object.keys(IL).map((k) => [k, ILNAMA[k] || k]), hint: "Bentuk gambar yang dipecah per komponen di halaman alat." })}
          <div class="field"><label>Foto alat sendiri (opsional)</label>
            <div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center"><label class="btn sm" for="gFile">${ico("image")} Pilih foto…</label><input type="file" id="gFile" accept="image/png,image/jpeg,image/webp,image/gif" hidden>
              <button type="button" class="btn sm ghost" id="gHapus" ${a.gambar ? "" : "hidden"}>Pakai ilustrasi saja</button><span class="muted" id="gNama" style="font-size:.82rem">${esc(a.gambar || "")}</span></div>
            <span class="hint">Foto disimpan di folder data/gambar. Di halaman alat, foto tampil lebih dulu lalu berganti ke ilustrasi saat komponennya dipecah.</span></div>
        </div>
      </div>
      ${fld("Prinsip kerja", "prinsipKerja", a.prinsipKerja, { area: true, rows: 5 })}
      ${fld("Keselamatan", "keselamatan", a.keselamatan, { area: true, rows: 2, ph: "Risiko dan standar keselamatan" })}
      ${fld("Referensi", "referensi", a.referensi.join("\n"), { area: true, rows: 3, hint: "Satu per baris. Boleh berupa <code>Judul: https://…</code>." })}
      <label style="display:flex;gap:8px;align-items:center;font-weight:500"><input type="checkbox" name="umpanBalik" ${a.umpanBalik ? "checked" : ""} style="accent-color:var(--text)"> Alat memakai kendali umpan balik (loop tertutup)</label>
    </section>
    <section class="card form-card"><div class="section-head"><div><h2>Diagram blok</h2><span class="sub">Urutkan dari input (sensor) ke output (tampilan/aktuator).</span></div><div class="right"><button type="button" class="btn" id="addBlok">${ico("plus")} Tambah blok</button></div></div>
      <div class="repeater" id="blokRep"></div></section>
    <section class="card form-card"><div class="section-head"><div><h2>Mata kuliah yang berkontribusi</h2><span class="sub">Inti = wajib dikuasai, Penting = sangat membantu, Pendukung = latar belakang. Centang sub-materi yang benar-benar dipakai alat.</span></div><div class="right"><button type="button" class="btn" id="addK">${ico("plus")} Hubungkan mata kuliah</button></div></div>
      <div class="repeater" id="kRep"></div></section>
    <datalist id="katAlat">${[...new Set([...KATEGORI_ALAT, ...S.alat.map((x) => x.kategori).filter(Boolean)])].map((k) => `<option value="${esc(k)}">`).join("")}</datalist>
    <div class="form-actions">${isNew ? "" : `<button type="button" class="btn danger" id="del">${ico("trash")} Hapus alat</button>`}
      <div class="right"><a class="btn" href="${isNew ? "#/kelola" : "#/alat/" + esc(a.id)}">Batal</a><button class="btn primary lg" type="submit">Simpan alat</button></div></div>
  </form></div>`;
  drawRep();
  const prev = () => { const f = $("#fa", v); $("#gPrev", v).innerHTML = gambarAlat({ ...a, ilustrasi: f.elements.ilustrasi.value, kategori: f.elements.kategori.value }); };
  $("#fa", v).elements.ilustrasi.addEventListener("change", prev);
  $("#gFile", v).addEventListener("change", async (e) => {
    const file = e.target.files[0]; if (!file) return;
    if (file.size > 15 * 1024 * 1024) { toast("Foto terlalu besar (maks. 15 MB)", true); return; }
    const ext = (file.name.split(".").pop() || "jpg").toLowerCase();
    try {
      const r = await fetch(`api/upload-gambar?nama=${encodeURIComponent(slug(a.id || a.singkatan || a.nama || "alat") + "-" + Date.now().toString(36))}&ext=${encodeURIComponent(ext)}`, { method: "POST", body: file });
      if (!r.ok) throw new Error(await r.text());
      a.gambar = (await r.json()).file;
      $("#gNama", v).textContent = a.gambar; $("#gHapus", v).hidden = false; prev();
      toast("Foto diunggah. Klik Simpan alat untuk memakainya.");
    } catch (er) { toast("Gagal mengunggah foto: " + er.message, true); }
  });

  v.addEventListener("click", (e) => {
    const t = e.target.closest("button"); if (!t) return;
    if (t.id === "gHapus") { a.gambar = ""; $("#gNama", v).textContent = ""; t.hidden = true; prev(); return; }
    const swap = (arr, i, j) => { if (j >= 0 && j < arr.length) [arr[i], arr[j]] = [arr[j], arr[i]]; };
    if (t.id === "addBlok") { collect(); a.blok.push({ id: "", nama: "", fungsi: "" }); drawRep(); $$(".rep-blok [data-f=nama]", v).pop().focus(); }
    else if (t.id === "addK") {
      collect();
      if (!S.materi.length) { toast("Tambahkan mata kuliah dulu", true); return; }
      const free = S.materi.find((m) => !a.kontribusi.some((k) => k.materi === m.id)) || S.materi[0];
      a.kontribusi.push({ materi: free.id, tingkat: 2, blok: [], sub: [], peran: "" }); drawRep();
    }
    else if (t.dataset.bdel != null) { collect(); const b = a.blok.splice(+t.dataset.bdel, 1)[0]; a.kontribusi.forEach((k) => (k.blok = (k.blok || []).filter((x) => x !== b.id))); drawRep(); }
    else if (t.dataset.bup != null) { collect(); swap(a.blok, +t.dataset.bup, +t.dataset.bup - 1); drawRep(); }
    else if (t.dataset.bdown != null) { collect(); swap(a.blok, +t.dataset.bdown, +t.dataset.bdown + 1); drawRep(); }
    else if (t.dataset.kdel != null) { collect(); a.kontribusi.splice(+t.dataset.kdel, 1); drawRep(); }
  });
  v.addEventListener("change", (e) => {
    if (e.target.matches(".rep-blok [data-f=nama]")) { collect(); drawRep(); }
    // Ganti mata kuliah → kosongkan sub-materi lama lalu tampilkan sub-materi mata kuliah baru.
    if (e.target.matches(".rep-k [data-f=materi]")) { collect(); const i = $$(".rep-k", v).indexOf(e.target.closest(".rep-k")); a.kontribusi[i].sub = []; drawRep(); }
  });

  $("#fa", v).onsubmit = async (e) => {
    e.preventDefault();
    collect();
    if (!a.nama.trim()) { toast("Nama alat wajib diisi", true); return; }
    a.blok = a.blok.filter((b) => b.nama.trim());
    const ids = new Set(a.blok.map((b) => b.id));
    a.kontribusi.forEach((k) => (k.blok = k.blok.filter((b) => ids.has(b))));
    const dup = a.kontribusi.map((k) => k.materi).find((m, i, arr) => arr.indexOf(m) !== i);
    if (dup) { toast(`Mata kuliah “${materiById(dup)?.nama}” dihubungkan dua kali. Gabungkan jadi satu.`, true); return; }
    a.nama = a.nama.trim();
    if (isNew) { a.id = uniqueId(a.singkatan || a.nama, S.alat); S.alat.push(a); }
    else Object.keys(a).forEach((k) => (orig[k] = a[k]));
    if (await save("alat")) { toast("Alat tersimpan"); location.hash = "#/alat/" + a.id; }
  };
  const del = $("#del", v);
  if (del) del.onclick = async () => {
    if (!(await confirmDialog("Hapus alat?", `“${esc(orig.nama)}” beserta diagram dan breakdown materinya akan dihapus. Salinan sebelumnya tersimpan sebagai alat.json.bak.`))) return;
    S.alat = S.alat.filter((x) => x !== orig);
    await save("alat"); toast("Alat dihapus"); location.hash = "#/alat";
  };
});

/* =========================================================
   EKSPOR / IMPOR (pindah progres antara laptop dan HP)
   Impor hanya menambah dan menggabungkan; tidak ada yang dihapus.
   ========================================================= */
async function eksporData() {
  const isi = { aplikasi: "teknologi-kedokteran", versi: VERSI_APP, tanggal: new Date().toISOString() };
  for (const n of NAMA_DATA) isi[n] = S[n];
  const teks = JSON.stringify(isi, null, 1);
  if (DESKTOP) {
    const r = await fetch("api/ekspor", { method: "POST", headers: { "Content-Type": "application/json" }, body: teks });
    if (r.ok) toast("Ekspor tersimpan: " + (await r.json()).file); else toast("Gagal mengekspor", true);
    return;
  }
  const nama = `progres-teknologi-kedokteran-${new Date().toISOString().slice(0, 10)}.json`;
  const file = new File([teks], nama, { type: "application/json" });
  // iPhone: lembar Bagikan → "Simpan ke File"; peramban lain: unduh biasa.
  if (navigator.canShare && navigator.canShare({ files: [file] })) {
    try { await navigator.share({ files: [file], title: nama }); return; } catch (e) { if (e.name === "AbortError") return; }
  }
  const a = document.createElement("a");
  a.href = URL.createObjectURL(file); a.download = nama; document.body.appendChild(a); a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
}

const PERINGKAT = { status: { belum: 0, sedang: 1, sudah: 2 }, proyek: { belum: 0, jalan: 1, selesai: 2 } };
function gabungProgres(L, I) {
  const lebih = (map, a, b) => ((map[b] ?? -1) > (map[a] ?? -1) ? b : a);
  const obj = (k) => (L[k] = L[k] && typeof L[k] === "object" ? L[k] : {});
  for (const [k, v] of Object.entries(I.status || {})) obj("status")[k] = L.status[k] ? lebih(PERINGKAT.status, L.status[k], v) : v;
  for (const [k, v] of Object.entries(I.proyek || {})) obj("proyek")[k] = L.proyek[k] ? lebih(PERINGKAT.proyek, L.proyek[k], v) : v;
  for (const k of ["sub", "proyekLangkah", "lanjutan", "kasus"]) for (const [x, v] of Object.entries(I[k] || {})) if (v) obj(k)[x] = v;
  for (const k of ["proyekCatatan", "lanjutanCatatan"]) for (const [x, v] of Object.entries(I[k] || {})) if (v && !obj(k)[x]) L[k][x] = v;
  for (const [aid, dom] of Object.entries(I.hta || {})) { const d = (obj("hta")[aid] = L.hta[aid] || {}); for (const [x, v] of Object.entries(dom || {})) if (v && !d[x]) d[x] = v; }
  if (I.latihan) {
    const A = (L.latihan = L.latihan || {}), B = I.latihan;
    A.xp = Math.max(A.xp || 0, B.xp || 0);
    A.hari = A.hari || {}; for (const [d, n] of Object.entries(B.hari || {})) A.hari[d] = Math.max(A.hari[d] || 0, n);
    for (const g of ["alat", "materi"]) {
      A[g] = A[g] || {};
      for (const [k, r] of Object.entries(B[g] || {})) { const a = (A[g][k] = A[g][k] || {}); for (const f of ["benar", "total", "terbaik"]) if (r[f] != null) a[f] = Math.max(a[f] || 0, r[f]); }
    }
    A.salah = [...new Set([...(A.salah || []), ...(B.salah || [])])];
    A.match = A.match || {}; if (B.match && B.match.terbaik) A.match.terbaik = A.match.terbaik ? Math.min(A.match.terbaik, B.match.terbaik) : B.match.terbaik;
  }
}
async function imporData(I) {
  if (!I || I.aplikasi !== "teknologi-kedokteran") throw new Error("Ini bukan file ekspor Teknologi Kedokteran.");
  await fetch("api/backup", { method: "POST" });
  const n = {};
  for (const k of ["materi", "alat", "proyek", "soal", "lanjutan", "modul", "referensi"]) {
    n[k] = 0;
    for (const x of I[k] || []) {
      const u = byId(S[k], x.id);
      if (!u) { S[k].push(x); n[k]++; continue; }
      if (x.catatan && !u.catatan) u.catatan = x.catatan;
      if (k === "materi" && x.bidang && !u.bidang) u.bidang = x.bidang;
      if (k === "alat" && x.gambar && !u.gambar) u.gambar = x.gambar;
    }
  }
  gabungProgres(S.progres, I.progres || {});
  for (const k of ["materi", "alat", "proyek", "soal", "lanjutan", "modul", "referensi", "progres"]) await save(k);
  return n;
}

/* =========================================================
   PENGATURAN
   ========================================================= */
route(/^pengaturan$/, (v) => {
  const p = S.progres.pengaturan;
  const draw = () => {
    v.innerHTML = `<div class="page" style="max-width:900px">
      <h1>Pengaturan</h1>
      <section class="card">
        <div class="setting"><div class="lbl"><b>Tema</b><small>Ikuti Windows, atau pilih terang/gelap.</small></div>
          <div class="seg">${[["sistem", "Sistem"], ["terang", "Terang"], ["gelap", "Gelap"]].map(([k, l]) => `<button data-tema="${k}" class="${(p.tema || "sistem") === k ? "on" : ""}">${l}</button>`).join("")}</div></div>
        <div class="setting"><div class="lbl"><b>Ukuran huruf</b><small>Untuk layar 14" dengan skala 150%, "Normal" sudah pas.</small></div>
          <div class="seg">${[[14, "Kecil"], [15, "Normal"], [16.5, "Besar"], [18, "Sangat besar"]].map(([k, l]) => `<button data-fs="${k}" class="${(p.ukuranHuruf || 15) == k ? "on" : ""}">${l}</button>`).join("")}</div></div>
        <div class="setting"><div class="lbl"><b>Animasi</b><small>Animasi pecah komponen, garis mindmap, transisi halaman, dan konfeti. Matikan bila laptop terasa berat.</small></div>
          <div class="seg">${[[true, "Nyala"], [false, "Mati"]].map(([k, l]) => `<button data-anim="${k}" class="${(p.animasi !== false) === k ? "on" : ""}">${l}</button>`).join("")}</div></div>
        <div class="setting"><div class="lbl"><b>Sapaan di beranda</b><small>Tampil sebagai "Selamat Datang ${esc(sapaan())}, Selamat Belajar".</small></div>
          <div class="field" style="width:240px"><input id="sapaanIn" value="${esc(sapaan())}" maxlength="40"></div></div>
      </section>
      <section class="card">
        <div class="setting"><div class="lbl"><b>Pindahkan progres</b><small>Ekspor semua progres, catatan, dan konten buatanmu ke satu file, lalu impor di perangkat lain (laptop ↔ iPhone). Impor hanya menambah dan menggabungkan, tidak menghapus apa pun.</small></div>
          <div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn primary" id="ekspor">Ekspor progres</button><label class="btn" for="imporFile">Impor progres</label><input type="file" id="imporFile" accept=".json,application/json" hidden></div></div>
        <div class="setting"><div class="lbl"><b>${DESKTOP ? "Folder data" : "Penyimpanan"}</b><small>${DESKTOP ? "Semua konten tersimpan sebagai JSON: materi, alat, proyek, soal, lanjutan, modul, referensi, dan progres. Foto alat ada di subfolder gambar." : "Data tersimpan di perangkat ini. Selalu buka aplikasi dari ikon Layar Utama, dan ekspor progres sebelum menghapus aplikasi atau ganti HP."}</small><div style="margin-top:6px"><code class="path">${esc(S.dataDir)}</code></div></div>
          ${DESKTOP ? `<button class="btn" id="openDir">Buka folder</button>` : ""}</div>
        <div class="setting"><div class="lbl"><b>Cadangan</b><small>${DESKTOP ? "Salin semua data ke folder cadangan/ bertanggal." : "Simpan salinan data di penyimpanan aplikasi. Untuk file cadangan, pakai Ekspor progres."}</small></div>
          <button class="btn primary" id="backup">Buat cadangan sekarang</button></div>
        <div class="setting"><div class="lbl"><b>Muat ulang data</b><small>Setelah mengedit file JSON di luar aplikasi.</small></div>
          <button class="btn" id="reload">Muat ulang</button></div>
        <div class="setting"><div class="lbl"><b>Reset status belajar</b><small>Semua mata kuliah dan sub-materi kembali "Belum". Konten tidak dihapus.</small></div>
          <button class="btn danger" id="resetSt">Reset</button></div>
      </section>
      <p class="muted" style="font-size:.85rem">Teknologi Kedokteran v${VERSI_APP} · konten versi ${S.progres.versiKonten || 1} · data lokal di laptopmu, tanpa internet.</p>
    </div>`;
  };
  v.addEventListener("change", async (e) => {
    if (e.target.id !== "imporFile" || !e.target.files[0]) return;
    try {
      const n = await imporData(JSON.parse(await e.target.files[0].text()));
      const tambah = Object.entries(n).filter(([, x]) => x).map(([k, x]) => `+${x} ${k}`);
      toast("Impor selesai. Progres digabung" + (tambah.length ? ", " + tambah.join(", ") : "") + ".");
      renderNav("pengaturan"); draw();
    } catch (er) { toast("Gagal mengimpor: " + er.message, true); }
    e.target.value = "";
  });
  v.addEventListener("input", (e) => { if (e.target.id === "sapaanIn") { p.sapaan = e.target.value.trim(); saveLater("progres", 800); } });
  v.addEventListener("click", async (e) => {
    const t = e.target.closest("[data-tema]"); if (t) { p.tema = t.dataset.tema; try { localStorage.setItem("tema", p.tema); } catch (er) {} applySettings(); saveLater("progres"); draw(); }
    const f = e.target.closest("[data-fs]"); if (f) { p.ukuranHuruf = +f.dataset.fs; applySettings(); saveLater("progres"); draw(); }
    const an = e.target.closest("[data-anim]"); if (an) { p.animasi = an.dataset.anim === "true"; applySettings(); saveLater("progres"); draw(); }
    if (e.target.closest("#ekspor")) eksporData();
    if (e.target.closest("#openDir")) fetch("api/open-folder", { method: "POST" });
    if (e.target.closest("#backup")) { const r = await fetch("api/backup", { method: "POST" }); if (r.ok) { const d = await r.json(); toast("Cadangan dibuat: " + d.folder); } else toast("Gagal membuat cadangan", true); }
    if (e.target.closest("#reload")) { await load(); applySettings(); toast("Data dimuat ulang"); draw(); renderNav("pengaturan"); }
    if (e.target.closest("#resetSt") && (await confirmDialog("Reset status belajar?", "Semua mata kuliah dan sub-materi akan kembali berstatus Belum.", "Reset"))) { S.progres.status = {}; S.progres.sub = {}; await save("progres"); toast("Status direset"); }
  });
  draw();
});

/* =========================================================
   PENCARIAN (Ctrl+K dan kotak di beranda)
   ========================================================= */
function searchItems(q) {
  q = q.trim().toLowerCase();
  if (!q) return null;
  const hit = (s) => String(s || "").toLowerCase().includes(q);
  const al = S.alat.filter((a) => hit(a.nama) || hit(a.singkatan) || hit(a.kategori) || hit(a.model) || hit(a.ringkasan) || (a.blok || []).some((b) => hit(b.nama))).slice(0, 6);
  const ma = S.materi.filter((m) => hit(m.nama) || hit(m.alias) || hit(m.kategori)).slice(0, 6);
  const su = [];
  for (const m of S.materi) for (const s of subsOf(m)) if (hit(s.nama) || hit(s.rincian)) su.push([m, s]);
  const pr = S.proyek.filter((p) => hit(p.judul) || hit(p.tujuan)).slice(0, 5);
  const rf = S.referensi.filter((r) => r.jenis !== "kuliah" && (hit(r.judul) || hit(r.penulis))).slice(0, 4);
  // v1.4: bab Kisah Deep Learning dan bab buku Referensi.
  const kb = [];
  for (const k of S.kisah || []) for (const b of k.bab) if (hit(b.judul) || hit(b.adalah) || (b.istilah || []).some((x) => hit(x.nama))) kb.push([k, b]);
  for (const r of S.referensi) if (r.jenis === "pustaka") for (const b of r.bab || []) if (hit(b.judul) || hit(b.asli) || hit(b.ringkas)) kb.push([r, b]);
  return { al, ma, su: su.slice(0, 8), pr, rf, kb: kb.slice(0, 6) };
}
function searchHtml(q) {
  const r = searchItems(q);
  if (!r) return "";
  const { al, ma, su, pr, rf, kb } = r;
  if (!al.length && !ma.length && !su.length && !pr.length && !rf.length && !kb.length) return `<div class="sr-empty">Tidak ada hasil untuk “${esc(q)}”</div>`;
  let i = 0;
  const item = (href, html) => `<div class="sr-item" data-i="${i++}" data-href="${href}">${html}</div>`;
  return (al.length ? `<div class="sr-group">Alat</div>` + al.map((a) => item("#/alat/" + a.id, `<span style="font-size:20px">${esc(a.ikon || "🔧")}</span><b>${esc(a.nama)}</b><small>${esc(a.kategori || "")}</small>`)).join("") : "")
    + (ma.length ? `<div class="sr-group">Mata kuliah</div>` + ma.map((m) => item("#/materi/" + m.id, `${ico("materi", 18)}<span>${esc(m.nama)}</span><small>${esc(semShort(m))}</small>`)).join("") : "")
    + (pr.length ? `<div class="sr-group">Proyek hands-on</div>` + pr.map((p) => item("#/proyek/" + p.id, `${ico("proyek", 18)}<span>${esc(p.judul)}</span><small>${esc(alatById(p.alat)?.singkatan || p.alat)} · tahap ${p.tahap}</small>`)).join("") : "")
    + (su.length ? `<div class="sr-group">Sub-materi</div>` + su.map(([m, s]) => item("#/materi/" + m.id, `<span class="muted" style="min-width:34px">${esc(s.no)}</span><span>${esc(s.nama)}<span class="sr-sub">${esc(m.nama)}</span></span>`)).join("") : "")
    + (rf.length ? `<div class="sr-group">Referensi</div>` + rf.map((x) => item(x.jenis === "pustaka" ? "#/pustaka/" + x.id : "#/referensi?q=" + encodeURIComponent(x.judul.slice(0, 40)), `${ico("ref", 18)}<span>${esc(x.judul)}</span><small>${esc(x.jenis)}</small>`)).join("") : "")
    + (kb.length ? `<div class="sr-group">Bab kisah dan buku</div>` + kb.map(([x, b]) => x.jenis === "pustaka"
      ? item(`#/pustaka/${x.id}?bab=${b.no}`, `${ico("materi", 18)}<span>${esc(b.judul)}<span class="sr-sub">${esc(x.singkat || x.judul)} · bab ${b.no}</span></span><small>${esc(fmtHal(b.hal))}</small>`)
      : item(`#/kisah/${x.id}/${b.id}`, `${ico("kisah", 18)}<span>${esc(b.judul)}<span class="sr-sub">${esc(x.singkat)}</span></span><small>${esc(b.tahap)}</small>`)).join("") : "");
}

let srSel = 0;
function closeSearch() { const r = $("#searchResults"); if (r) r.hidden = true; }
function runSearch(q) {
  const box = $("#searchResults");
  const html = searchHtml(q);
  box.innerHTML = html; box.hidden = !html; srSel = 0; markSel();
}
function markSel() { $$("#searchResults .sr-item").forEach((el) => el.classList.toggle("sel", +el.dataset.i === srSel)); }
function goSel(i) { const it = $(`#searchResults .sr-item[data-i="${i}"]`); if (!it) return; $("#searchInput").value = ""; closeSearch(); $("#searchInput").blur(); location.hash = it.dataset.href; }

function initSearch() {
  const inp = $("#searchInput");
  inp.addEventListener("input", () => runSearch(inp.value));
  inp.addEventListener("focus", () => inp.value && runSearch(inp.value));
  inp.addEventListener("keydown", (e) => {
    const n = $$("#searchResults .sr-item").length;
    if (e.key === "ArrowDown") { srSel = Math.min(srSel + 1, n - 1); markSel(); e.preventDefault(); }
    else if (e.key === "ArrowUp") { srSel = Math.max(srSel - 1, 0); markSel(); e.preventDefault(); }
    else if (e.key === "Enter") { goSel(srSel); e.preventDefault(); }
    else if (e.key === "Escape") { inp.value = ""; closeSearch(); inp.blur(); }
  });
  $("#searchResults").addEventListener("mousedown", (e) => { const it = e.target.closest(".sr-item"); if (it) { e.preventDefault(); goSel(+it.dataset.i); } });
  inp.addEventListener("blur", () => setTimeout(closeSearch, 120));
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") { e.preventDefault(); inp.focus(); inp.select(); }
    if (e.altKey && e.key === "ArrowLeft") { e.preventDefault(); goBack(); }
  });
}
