"use strict";

/* =========================================================
   LATIHAN SOAL
   Pola diambil dari aplikasi belajar populer:
   - Duolingo: satu soal per layar, tombol Periksa, umpan balik
     langsung berwarna di bawah, combo/streak, XP.
   - Quizlet Match: papan pasangan dengan stopwatch.
   - Kahoot/Brilliant: skor, penjelasan setelah menjawab.
   - Retrieval practice (Roediger & Karpicke 2006): soal yang
     salah disimpan untuk diulang.
   ========================================================= */

const TIPE = {
  pg: "Pilihan ganda", kasus: "Studi kasus", bs: "Benar atau salah", cocok: "Cocokkan", urut: "Urutkan",
  isian: "Isian singkat", hitung: "Hitungan", multi: "Pilih semua yang benar", kategori: "Kelompokkan", celah: "Lengkapi kalimat", diagram: "Lengkapi diagram blok",
};
const shuffle = (arr) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0; [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pickN = (arr, n) => shuffle(arr).slice(0, n);
const today = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
const potong = (s, n = 90) => (s.length > n ? s.slice(0, n - 1).trim() + "…" : s);

function lat() {
  const L = S.progres.latihan = S.progres.latihan || {};
  L.xp = L.xp || 0; L.hari = L.hari || {}; L.alat = L.alat || {}; L.materi = L.materi || {}; L.salah = L.salah || []; L.match = L.match || {};
  return L;
}
function streak() {
  const L = lat();
  let n = 0; const d = new Date();
  if (!L.hari[today()]) d.setDate(d.getDate() - 1);
  for (;;) { const k = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; if (!L.hari[k]) break; n++; d.setDate(d.getDate() - 1); }
  return n;
}

// Jawaban teks dibandingkan tanpa beda huruf besar, aksen, tanda baca, dan spasi ganda.
const normal = (t) => String(t ?? "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9.,+\-/% ]/g, " ").replace(/\s+/g, " ").trim();
const angka = (t) => { const x = parseFloat(String(t).trim().replace(/\s/g, "").replace(",", ".")); return Number.isFinite(x) ? x : null; };
const fmtAngka = (x) => (Math.abs(x) >= 1000 || Number.isInteger(x) ? x.toLocaleString("id-ID") : x.toLocaleString("id-ID", { maximumFractionDigits: 4 }));
const soalMateri = (mid) => (S.soal || []).filter((q) => q.materi === mid);

/* ---------- soal otomatis dari data alat ---------- */
function autoSoal(a) {
  const out = [];
  const blok = (a.blok || []).filter((b) => b.nama);
  // Diagram blok bolong: satu komponen disembunyikan, pilih komponen yang tepat.
  const blokLain = [...new Set(S.alat.filter((x) => x.id !== a.id).flatMap((x) => (x.blok || []).map((b) => b.nama)))].filter((n) => !blok.some((b) => b.nama === n));
  if (blok.length >= 4 && blokLain.length >= 3) {
    const k = 1 + ((Math.random() * (blok.length - 2)) | 0);
    out.push({ id: `a:${a.id}:diagram`, alat: a.id, tipe: "diagram", auto: true, tanya: `Komponen apa yang hilang dari diagram blok ${a.singkatan || a.nama}?`, item: blok.map((b) => b.nama), kosong: k,
      opsi: [blok[k].nama, ...pickN(blokLain, 3)], jawab: 0, bahas: `${blok[k].nama}: ${blok[k].fungsi || "komponen ini berada di antara " + blok[k - 1].nama + " dan " + blok[k + 1].nama}.` });
  }
  const kontrib = (a.kontribusi || []).filter((k) => materiById(k.materi));
  if (blok.length >= 4) out.push({ id: `a:${a.id}:urut`, alat: a.id, tipe: "urut", auto: true, tanya: `Urutkan komponen ${a.singkatan || a.nama} dari masukan ke keluaran.`, item: blok.map((b) => b.nama), bahas: `Alur ${a.nama}: ${blok.map((b) => b.nama).join(" → ")}.` });
  const bf = blok.filter((b) => b.fungsi);
  if (bf.length >= 4) out.push({ id: `a:${a.id}:fungsi`, alat: a.id, tipe: "cocok", auto: true, tanya: `Cocokkan komponen ${a.singkatan || a.nama} dengan fungsinya.`, pasangan: pickN(bf, 4).map((b) => [b.nama, b.fungsi]), bahas: "Fungsi tiap komponen diambil dari diagram blok alat." });
  const lain = S.alat.filter((x) => x.id !== a.id).flatMap((x) => (x.blok || []).filter((b) => b.fungsi).map((b) => b.fungsi));
  bf.forEach((b) => {
    const salah = pickN([...new Set(lain.filter((f) => f !== b.fungsi))], 3);
    if (salah.length === 3) out.push({ id: `a:${a.id}:f:${b.id}`, alat: a.id, tipe: "pg", auto: true, tanya: `Pada ${a.nama}, komponen “${b.nama}” berfungsi untuk…`, opsi: [b.fungsi, ...salah], jawab: 0, bahas: `${b.nama}: ${b.fungsi}.` });
  });
  const pakai = new Set(kontrib.map((k) => k.materi));
  const bukan = S.materi.filter((m) => !pakai.has(m.id));
  blok.forEach((b) => {
    const inti = kontrib.filter((k) => +k.tingkat === 3 && (k.blok || []).includes(b.id));
    if (!inti.length || bukan.length < 3) return;
    const k = inti[(Math.random() * inti.length) | 0];
    out.push({ id: `a:${a.id}:mk:${b.id}`, alat: a.id, tipe: "pg", auto: true, tanya: `Mata kuliah mana yang berperan INTI saat membangun komponen “${b.nama}” pada ${a.singkatan || a.nama}?`, opsi: [materiById(k.materi).nama, ...pickN(bukan, 3).map((m) => m.nama)], jawab: 0, bahas: `${materiById(k.materi).nama}: ${k.peran || "berperan inti pada komponen ini"}.` });
  });
  const kp = kontrib.filter((k) => k.peran && k.peran.length > 12);
  if (kp.length >= 4) out.push({ id: `a:${a.id}:peran`, alat: a.id, tipe: "cocok", auto: true, tanya: `Cocokkan mata kuliah dengan perannya pada ${a.singkatan || a.nama}.`, pasangan: pickN(kp, 4).map((k) => [materiById(k.materi).nama, potong(k.peran, 80)]), bahas: "Peran ini diambil dari breakdown materi kuliah pada halaman alat." });
  return out;
}

function bankSoal(filter) {
  const manual = (S.soal || []).filter((s) => !filter || filter(s));
  const auto = S.alat.flatMap((a) => autoSoal(a)).filter((s) => !filter || filter(s));
  return [...manual, ...auto];
}
const soalById = (id) => (S.soal || []).find((s) => s.id === id) || S.alat.flatMap((a) => autoSoal(a)).find((s) => s.id === id);

/* ---------- beranda latihan ---------- */
route(/^latihan$/, (v) => {
  const L = lat();
  const nManual = (S.soal || []).length, nAuto = S.alat.reduce((s, a) => s + autoSoal(a).length, 0);
  const akur = (() => { const t = Object.values(L.alat).reduce((s, x) => [s[0] + (x.benar || 0), s[1] + (x.total || 0)], [0, 0]); return t[1] ? Math.round((t[0] / t[1]) * 100) : 0; })();
  const modes = [
    ["cepat", "⚡", "Latihan cepat", "10 soal acak dari semua alat. Cocok untuk pemanasan harian."],
    ["match", "🧩", "Match kilat", "Cocokkan 6 pasangan secepat mungkin. Kalahkan rekor waktumu."],
    ["urut", "🔀", "Urutkan alur sinyal", "Susun komponen alat dari masukan ke keluaran."],
    ["kasus", "🩺", "Studi kasus", "Soal skenario klinis dan pemecahan masalah alat."],
    ["diagram", "🧱", "Lengkapi diagram blok", "Satu komponen alat hilang. Tebak komponen yang tepat."],
    ["hitung", "🧮", "Soal hitungan", "Rumus dipakai sungguhan: frekuensi sampling, dosis, gain, dan lainnya."],
    ["kategori", "🗂️", "Kelompokkan", "Pilah istilah ke kelompok yang tepat."],
    ["celah", "✍️", "Lengkapi kalimat", "Isi kata yang hilang dari bank kata."],
    ["campur", "🎲", "Campuran tipe baru", "Isian singkat, pilih banyak, hitungan, dan kelompokkan dalam satu sesi."],
  ];
  v.innerHTML = `<div class="page">
    <section class="lat-hero card">
      <div><h1>Latihan Soal</h1><p class="sub">Belajar paling melekat dengan mengingat kembali, bukan membaca ulang. Jawab, lihat pembahasan, lalu ulangi yang salah.</p></div>
      <div class="lat-stats">
        <div class="ls"><span class="flame">🔥</span><b data-count="${streak()}">${streak()}</b><small>hari beruntun</small></div>
        <div class="ls"><span>⭐</span><b data-count="${L.xp}">${L.xp}</b><small>XP</small></div>
        <div class="ls"><span>🎯</span><b>${akur}%</b><small>akurasi</small></div>
        <div class="ls"><span>📚</span><b>${nManual + nAuto}</b><small>soal tersedia</small></div>
      </div>
    </section>
    <div class="mode-grid stagger">${modes.map(([k, e, t, d], i) => `<a class="card mode-card" href="#/latihan/mode/${k}" style="--i:${i}"><span class="mode-ico">${e}</span><b>${t}</b><p>${d}</p>${k === "match" && L.match.terbaik ? `<small>Rekor: ${L.match.terbaik.toFixed(1)} detik</small>` : ""}</a>`).join("")}
      <a class="card mode-card${L.salah.length ? "" : " dis"}" href="${L.salah.length ? "#/latihan/mode/salah" : "#/latihan"}" style="--i:${modes.length}"><span class="mode-ico">🔁</span><b>Ulangi yang salah</b><p>${L.salah.length ? `${L.salah.length} soal menunggu diulang.` : "Belum ada. Soal yang salah akan muncul di sini."}</p></a></div>
    <section class="section">
      <div class="section-head"><div><h2>Per mata kuliah</h2><span class="sub">Latihan dari modul tiap mata kuliah, dengan tipe soal campuran.</span></div>
        <div class="right"><div class="seg" id="latSem">${["Semua", 1, 2, 3, 4, 5, 6, 7].map((x) => `<button data-ls="${x}" class="${String(ui.latSem || "Semua") === String(x) ? "on" : ""}">${x === "Semua" ? "Semua" : "S" + x}</button>`).join("")}</div></div></div>
      <div class="lat-materi stagger" id="latMateri"></div>
    </section>
    <section class="section">
      <div class="section-head"><div><h2>Per alat</h2><span class="sub">Fokus pada penerapan satu alat.</span></div></div>
      <div class="lat-alat stagger">${S.alat.map((a, i) => { const r = L.alat[a.id] || {}; const n = bankSoal((s) => s.alat === a.id).length; return `<a class="card la-card" href="#/latihan/alat/${esc(a.id)}" style="--i:${i}">
        <div class="mini-ilus">${gambarAlat(a)}</div><div><b>${esc(a.singkatan || a.nama)}</b><small>${n} soal${r.terbaik != null ? ` · terbaik ${r.terbaik}%` : ""}</small></div>
        ${r.terbaik != null ? `<div class="ring sm" style="--p:${r.terbaik}" data-label="${r.terbaik}"></div>` : ""}</a>`; }).join("")}</div>
    </section>
    <section class="section">
      <div class="section-head"><div><h2>Studi lanjutan</h2></div></div>
      <div class="mode-grid">${(S.lanjutan || []).map((l) => `<a class="card mode-card" href="#/latihan/topik/${esc(l.id)}"><span class="mode-ico">${esc(l.ikon)}</span><b>${esc(l.nama)}</b><p>${(S.soal || []).filter((s) => s.alat === l.id).length} soal</p></a>`).join("")}</div>
    </section>
    <p class="muted" style="font-size:.84rem">${nManual} soal ditulis manual dan ${nAuto} soal dibuat otomatis dari diagram blok dan breakdown mata kuliah, sehingga soal ikut bertambah saat kamu menambah alat.</p>
  </div>`;
  const drawMateri = () => {
    const list = S.materi.filter((m) => soalMateri(m.id).length && (!ui.latSem || ui.latSem === "Semua" || m.semester === +ui.latSem))
      .sort((x, y) => (x.semester || 9) - (y.semester || 9) || x.nama.localeCompare(y.nama));
    $("#latMateri", v).innerHTML = list.map((m, i) => { const r = L.materi[m.id] || {}; const n = soalMateri(m.id).length; return `<a class="card lm-card" href="#/latihan/materi/${esc(m.id)}" style="--i:${Math.min(i, 16)};--bd:${BIDANG[bidangOf(m)].warna}">
      <span class="lm-sem">${esc(semShort(m))}</span><div><b>${esc(m.nama)}</b><small>${n} soal${r.terbaik != null ? ` · terbaik ${r.terbaik}%` : ""}</small></div>
      ${r.terbaik != null ? `<div class="ring sm" style="--p:${r.terbaik}" data-label="${r.terbaik}"></div>` : `<span class="lm-go">${ico("play", 14)}</span>`}</a>`; }).join("") || `<div class="empty">Tidak ada soal pada semester ini.</div>`;
  };
  v.addEventListener("click", (e) => { const b = e.target.closest("[data-ls]"); if (!b) return; ui.latSem = b.dataset.ls; $$("#latSem button", v).forEach((x) => x.classList.toggle("on", x === b)); drawMateri(); });
  drawMateri();
  countUp(v);
});

/* ---------- sesi latihan ---------- */
route(/^latihan\/(mode|alat|topik|materi)\/([^/]+)$/, (v, jenis, key) => {
  const L = lat();
  let soal = [], judul = "", konteks = null;
  if (jenis === "alat") { const a = alatById(key); if (!a) { location.hash = "#/latihan"; return; } konteks = a.id; judul = a.nama; soal = pickN(bankSoal((s) => s.alat === a.id), 10); }
  else if (jenis === "topik") { const t = (S.lanjutan || []).find((x) => x.id === key); judul = t ? t.nama : key; konteks = key; soal = pickN((S.soal || []).filter((s) => s.alat === key), 10); }
  else if (jenis === "materi") { const m = materiById(key); if (!m) { location.hash = "#/latihan"; return; } konteks = m.id; judul = m.nama; soal = campurTipe(soalMateri(m.id), 10); }
  else if (key === "cepat") { judul = "Latihan cepat"; soal = pickN(bankSoal((s) => alatById(s.alat) || materiById(s.materi)), 10); }
  else if (["diagram", "hitung", "kategori", "celah"].includes(key)) { judul = TIPE[key]; soal = pickN(bankSoal((s) => s.tipe === key), 10); }
  else if (key === "campur") { judul = "Campuran tipe baru"; soal = campurTipe(bankSoal((s) => ["isian", "hitung", "multi", "kategori", "celah", "diagram"].includes(s.tipe)), 10); }
  else if (key === "urut") { judul = "Urutkan alur sinyal"; soal = pickN(bankSoal((s) => s.tipe === "urut"), 8); }
  else if (key === "kasus") { judul = "Studi kasus"; soal = pickN(bankSoal((s) => s.tipe === "kasus"), 10); }
  else if (key === "salah") { judul = "Ulangi yang salah"; soal = L.salah.map(soalById).filter(Boolean).slice(0, 12); }
  else if (key === "match") { return matchGame(v); }
  if (!soal.length) { v.innerHTML = `<div class="page"><div class="empty">Belum ada soal untuk bagian ini. <a href="#/latihan">Kembali</a></div></div>`; return; }

  const sesi = { i: 0, benar: 0, combo: 0, comboMax: 0, xp: 0, salah: [], mulai: Date.now(), jawaban: null, terkunci: false };
  const tutup = () => (konteks && jenis === "alat" ? `#/alat/${konteks}` : konteks && jenis === "materi" ? `#/materi/${konteks}` : konteks ? `#/lanjutan/${konteks}` : "#/latihan");

  v.innerHTML = `<div class="quiz">
    <div class="q-top"><a class="q-x" href="#/latihan" title="Keluar">✕</a><div class="q-prog"><i id="qBar"></i></div><span class="q-combo" id="qCombo"></span><span class="q-xp" id="qXp">0 XP</span></div>
    <div class="q-stage" id="qStage"></div>
    <div class="q-foot" id="qFoot"></div>
  </div>`;

  const stage = $("#qStage", v), foot = $("#qFoot", v);
  const setFoot = (state, html) => { foot.className = "q-foot " + (state || ""); foot.innerHTML = html; };

  function render() {
    const s = soal[sesi.i];
    sesi.jawaban = null; sesi.terkunci = false;
    $("#qBar", v).style.width = (sesi.i / soal.length) * 100 + "%";
    const a = alatById(s.alat), lt = (S.lanjutan || []).find((x) => x.id === s.alat), mk = materiById(s.materi);
    const head = `<div class="q-meta"><span class="chip dark">${TIPE[s.tipe] || s.tipe}</span>${mk && jenis !== "materi" ? `<span class="chip outline">${esc(mk.nama)}</span>` : ""}${a ? `<span class="chip">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</span>` : lt ? `<span class="chip">${esc(lt.ikon)} ${esc(lt.singkat)}</span>` : ""}<span class="muted">${sesi.i + 1} / ${soal.length}</span></div>
      <h2 class="q-tanya">${esc(s.tanya)}</h2>`;
    let body = "";
    if (s.tipe === "pg" || s.tipe === "kasus") {
      sesi.urutOpsi = shuffle(s.opsi.map((o, i) => [o, i]));
      body = `<div class="q-opsi">${sesi.urutOpsi.map(([o], i) => `<button class="q-op" data-op="${i}"><kbd>${i + 1}</kbd><span>${esc(o)}</span></button>`).join("")}</div>`;
    } else if (s.tipe === "bs") {
      body = `<div class="q-opsi bs"><button class="q-op" data-op="1"><kbd>1</kbd><span>Benar</span></button><button class="q-op" data-op="0"><kbd>2</kbd><span>Salah</span></button></div>`;
    } else if (s.tipe === "cocok") {
      sesi.kiri = shuffle(s.pasangan.map((p, i) => [p[0], i])); sesi.kanan = shuffle(s.pasangan.map((p, i) => [p[1], i]));
      sesi.pilih = null; sesi.cocokSalah = 0; sesi.cocokSisa = s.pasangan.length;
      body = `<div class="q-match"><div class="col">${sesi.kiri.map(([t, i]) => `<button class="tile" data-l="${i}">${esc(t)}</button>`).join("")}</div>
        <div class="col">${sesi.kanan.map(([t, i]) => `<button class="tile" data-r="${i}">${esc(t)}</button>`).join("")}</div></div>`;
    } else if (s.tipe === "urut") {
      sesi.bank = shuffle(s.item.map((t, i) => [t, i])); sesi.susun = [];
      body = `<div class="q-urut"><div class="slot-row" id="slots"><span class="ph">Ketuk komponen di bawah sesuai urutan…</span></div><div class="bank-row" id="bank">${sesi.bank.map(([t, i]) => `<button class="tile" data-b="${i}">${esc(t)}</button>`).join("")}</div></div>`;
    } else if (s.tipe === "isian" || s.tipe === "hitung") {
      body = `<div class="q-isian"><input id="qIn" class="q-in" ${s.tipe === "hitung" ? 'inputmode="decimal" placeholder="Tulis angka, misal 2,5"' : 'placeholder="Ketik jawabanmu…"'} autocomplete="off" spellcheck="false">${s.satuan ? `<span class="q-sat">${esc(s.satuan)}</span>` : ""}</div>
        ${s.tipe === "hitung" ? `<p class="muted q-tip">Boleh memakai koma atau titik desimal. ${s.tol ? `Toleransi ±${fmtAngka(s.tol)}${s.satuan ? " " + esc(s.satuan) : ""}.` : "Jawaban harus tepat."}</p>` : ""}`;
    } else if (s.tipe === "multi") {
      sesi.urutOpsi = shuffle(s.opsi.map((o, i) => [o, i])); sesi.multi = new Set();
      body = `<p class="muted q-tip">Bisa lebih dari satu jawaban.</p><div class="q-opsi multi">${sesi.urutOpsi.map(([o], i) => `<button class="q-op" data-mo="${i}"><kbd class="cb">${ico("check", 14)}</kbd><span>${esc(o)}</span></button>`).join("")}</div>`;
    } else if (s.tipe === "kategori") {
      sesi.kItem = shuffle(s.item.map(([t, g], i) => ({ t, g, i, at: null }))); sesi.kPilih = null;
      body = `<div class="q-kat"><div class="kat-bank" id="katBank"></div><div class="kat-groups" style="--n:${s.kelompok.length}">${s.kelompok.map((g, gi) => `<div class="kat-g" data-kg="${gi}"><b>${esc(g)}</b><div class="kat-drop" id="kg${gi}"></div></div>`).join("")}</div></div>
        <p class="muted q-tip">Ketuk istilah, lalu ketuk kelompoknya. Ketuk lagi istilah di kelompok untuk mengembalikannya.</p>`;
    } else if (s.tipe === "celah") {
      sesi.gap = s.isi.map(() => null); sesi.kata = shuffle([...s.isi, ...s.pengecoh].map((t, i) => [t, i])); sesi.gapSel = 0;
      body = `<div class="q-celah" id="celahTeks"></div><div class="bank-row" id="kataBank">${sesi.kata.map(([t, i]) => `<button class="tile" data-w="${i}">${esc(t)}</button>`).join("")}</div>`;
    } else if (s.tipe === "diagram") {
      sesi.urutOpsi = shuffle(s.opsi.map((o, i) => [o, i]));
      body = `<div class="q-diag">${s.item.map((t, i) => `${i ? `<span class="qd-ar">${ico("arrow", 16)}</span>` : ""}<span class="qd-b${i === s.kosong ? " kosong" : ""}" style="--i:${i}">${i === s.kosong ? "?" : esc(t)}</span>`).join("")}</div>
        <div class="q-opsi">${sesi.urutOpsi.map(([o], i) => `<button class="q-op" data-op="${i}"><kbd>${i + 1}</kbd><span>${esc(o)}</span></button>`).join("")}</div>`;
    }
    stage.innerHTML = `<div class="q-card">${head}${body}</div>`;
    stage.firstElementChild.classList.add("enter");
    // Tombol Periksa harus ada dulu: drawKat/drawCelah mengatur status aktifnya.
    setFoot("", s.tipe === "cocok" ? `<span class="muted">Ketuk satu kotak kiri lalu pasangannya di kanan.</span>` : `<span></span><button class="btn primary lg" id="qCek" disabled>Periksa</button>`);
    if (s.tipe === "kategori") drawKat();
    if (s.tipe === "celah") drawCelah();
    if (s.tipe === "isian" || s.tipe === "hitung") setTimeout(() => $("#qIn", stage)?.focus(), 60);
  }

  function cekJawaban() {
    const s = soal[sesi.i];
    let ok = false;
    if (s.tipe === "pg" || s.tipe === "kasus" || s.tipe === "diagram") ok = sesi.urutOpsi[sesi.jawaban][1] === s.jawab;
    else if (s.tipe === "isian") { const x = normal($("#qIn", stage).value); ok = s.jawab.some((j) => normal(j) === x || (angka(j) != null && angka(j) === angka(x))); }
    else if (s.tipe === "hitung") { const x = angka($("#qIn", stage).value); ok = x != null && Math.abs(x - s.angka) <= s.tol + 1e-9; }
    else if (s.tipe === "multi") { const b = new Set(s.benar); ok = sesi.multi.size === b.size && [...sesi.multi].every((i) => b.has(sesi.urutOpsi[i][1])); }
    else if (s.tipe === "kategori") ok = sesi.kItem.every((x) => x.at === x.g);
    else if (s.tipe === "celah") ok = sesi.gap.every((w, i) => w != null && normal(sesi.kata.find((k) => k[1] === w)[0]) === normal(s.isi[i]));
    else if (s.tipe === "bs") ok = (sesi.jawaban === 1) === !!s.jawab;
    else if (s.tipe === "urut") ok = sesi.susun.every((x, i) => x === i) && sesi.susun.length === s.item.length;
    else if (s.tipe === "cocok") ok = sesi.cocokSalah === 0;
    selesaiSoal(ok);
  }

  function selesaiSoal(ok) {
    const s = soal[sesi.i];
    sesi.terkunci = true;
    if (ok) { sesi.benar++; sesi.combo++; sesi.comboMax = Math.max(sesi.comboMax, sesi.combo); sesi.xp += 10 + Math.min(sesi.combo - 1, 5) * 2; L.salah = L.salah.filter((x) => x !== s.id); }
    else { sesi.combo = 0; sesi.salah.push(s); if (!L.salah.includes(s.id)) L.salah.push(s.id); }
    $("#qXp", v).textContent = sesi.xp + " XP";
    const c = $("#qCombo", v); c.textContent = sesi.combo >= 2 ? `🔥 ${sesi.combo}` : ""; c.classList.remove("pop"); void c.offsetWidth; if (sesi.combo >= 2) c.classList.add("pop");
    // Tandai jawaban di layar
    if (s.tipe === "pg" || s.tipe === "kasus" || s.tipe === "diagram") $$(".q-op", stage).forEach((b, i) => { b.disabled = true; if (sesi.urutOpsi[i][1] === s.jawab) b.classList.add("benar"); else if (+b.dataset.op === sesi.jawaban) b.classList.add("salah"); });
    if (s.tipe === "diagram") { const k = $(".qd-b.kosong", stage); k.textContent = s.item[s.kosong]; k.classList.add(ok ? "benar" : "salah"); }
    if (s.tipe === "isian" || s.tipe === "hitung") { const i = $("#qIn", stage); i.disabled = true; i.classList.add(ok ? "benar" : "salah"); }
    if (s.tipe === "multi") $$(".q-op", stage).forEach((b, i) => { b.disabled = true; const benar = s.benar.includes(sesi.urutOpsi[i][1]), dipilih = sesi.multi.has(i); b.classList.add(benar ? (dipilih ? "benar" : "miss") : dipilih ? "salah" : "x"); });
    if (s.tipe === "kategori") $$("[data-ki]", stage).forEach((b) => { const it = sesi.kItem[+b.dataset.ki]; b.disabled = true; b.classList.add(it.at === it.g ? "benar" : "salah"); });
    if (s.tipe === "celah") $$("#celahTeks .gap", stage).forEach((g, i) => { g.disabled = true; const w = sesi.gap[i]; g.classList.add(w != null && normal(sesi.kata.find((k) => k[1] === w)[0]) === normal(s.isi[i]) ? "benar" : "salah"); });
    if (s.tipe === "bs") $$(".q-op", stage).forEach((b) => { b.disabled = true; if ((+b.dataset.op === 1) === !!s.jawab) b.classList.add("benar"); else if (+b.dataset.op === sesi.jawaban) b.classList.add("salah"); });
    if (s.tipe === "urut") $$("#slots .tile", stage).forEach((b, i) => b.classList.add(sesi.susun[i] === i ? "benar" : "salah"));
    const kunci = ok ? "" : s.tipe === "urut" ? `<div class="kunci">Urutan benar: ${s.item.map(esc).join(" → ")}</div>`
      : s.tipe === "isian" ? `<div class="kunci">Jawaban: ${esc(s.jawab[0])}${s.jawab.length > 1 ? ` (juga diterima: ${s.jawab.slice(1).map(esc).join(", ")})` : ""}</div>`
      : s.tipe === "hitung" ? `<div class="kunci">Jawaban: ${fmtAngka(s.angka)}${s.satuan ? " " + esc(s.satuan) : ""}</div>`
      : s.tipe === "multi" ? `<div class="kunci">Yang benar: ${s.benar.map((i) => esc(s.opsi[i])).join("; ")}</div>`
      : s.tipe === "kategori" ? `<div class="kunci">${s.kelompok.map((g, gi) => `<b>${esc(g)}:</b> ${s.item.filter(([, x]) => x === gi).map(([t]) => esc(t)).join(", ")}`).join("<br>")}</div>`
      : s.tipe === "celah" ? `<div class="kunci">${esc(s.teks.replace(/\[\[(\d+)\]\]/g, (_, i) => s.isi[+i]))}</div>` : "";
    setFoot(ok ? "ok" : "no", `<div class="fb"><b>${ok ? pujian() : "Belum tepat"}</b><p>${esc(s.bahas || "")}</p>${kunci}</div><button class="btn lg ${ok ? "ok" : "no"}" id="qNext">${sesi.i + 1 < soal.length ? "Lanjut" : "Lihat hasil"}</button>`);
    if (!ok) stage.firstElementChild.classList.add("shake");
    $("#qNext", v).focus();
  }

  function akhir() {
    const pct = Math.round((sesi.benar / soal.length) * 100);
    const detik = Math.round((Date.now() - sesi.mulai) / 1000);
    L.xp += sesi.xp; L.hari[today()] = (L.hari[today()] || 0) + soal.length;
    if (jenis === "alat" || jenis === "materi") { const g = L[jenis] = L[jenis] || {}; const r = g[konteks] = g[konteks] || {}; r.benar = (r.benar || 0) + sesi.benar; r.total = (r.total || 0) + soal.length; r.terbaik = Math.max(r.terbaik || 0, pct); }
    if (jenis !== "alat") soal.forEach((s) => { if (!alatById(s.alat)) return; const r = L.alat[s.alat] = L.alat[s.alat] || {}; r.total = (r.total || 0) + 1; r.benar = (r.benar || 0) + (sesi.salah.includes(s) ? 0 : 1); });
    if (jenis !== "materi") soal.forEach((s) => { if (!materiById(s.materi)) return; const r = L.materi[s.materi] = L.materi[s.materi] || {}; r.total = (r.total || 0) + 1; r.benar = (r.benar || 0) + (sesi.salah.includes(s) ? 0 : 1); });
    saveLater("progres", 200);
    $("#qBar", v).style.width = "100%";
    setFoot("", "");
    stage.innerHTML = `<div class="q-card q-end enter">
      <div class="end-ring ring" style="--p:${pct}" data-label="${pct}%"></div>
      <h2>${pct >= 80 ? `Luar biasa, ${esc(sapaan())}!` : pct >= 50 ? "Bagus, terus latihan!" : "Tidak apa-apa, ulangi lagi ya."}</h2>
      <div class="end-stats"><div><b>${sesi.benar}/${soal.length}</b><small>benar</small></div><div><b>+${sesi.xp}</b><small>XP</small></div><div><b>${sesi.comboMax}</b><small>combo terbaik</small></div><div><b>${Math.floor(detik / 60)}:${String(detik % 60).padStart(2, "0")}</b><small>waktu</small></div></div>
      ${sesi.salah.length ? `<div class="review"><h3>Yang perlu diulang</h3>${sesi.salah.map((s) => `<details><summary>${esc(s.tanya)}</summary><p>${esc(s.bahas || "")}</p></details>`).join("")}</div>` : ""}
      <div class="end-acts"><a class="btn" href="${tutup()}">Selesai</a>${sesi.salah.length ? `<a class="btn" href="#/latihan/mode/salah">Ulangi yang salah</a>` : ""}<button class="btn primary" id="lagi">Latihan lagi</button></div>
    </div>`;
    if (pct >= 80) confetti();
    $("#lagi", v).onclick = () => router();
  }

  v.addEventListener("click", (e) => {
    const s = soal[sesi.i];
    if (e.target.closest("#qNext")) { sesi.i++; sesi.i < soal.length ? render() : akhir(); return; }
    if (e.target.closest("#qCek")) { cekJawaban(); return; }
    if (sesi.terkunci || !s) return;
    const mo = e.target.closest("[data-mo]");
    if (mo) { const i = +mo.dataset.mo; sesi.multi.has(i) ? sesi.multi.delete(i) : sesi.multi.add(i); mo.classList.toggle("sel", sesi.multi.has(i)); $("#qCek", v).disabled = !sesi.multi.size; return; }
    const kb = e.target.closest("[data-ki]"), kg = e.target.closest("[data-kg]");
    // Ada istilah terpilih: ketukan di mana pun dalam kelompok (termasuk di atas istilah lain) menaruhnya di sana.
    if (kg && sesi.kPilih != null) { sesi.kItem[sesi.kPilih].at = +kg.dataset.kg; sesi.kPilih = null; drawKat(); return; }
    if (kb) { const it = sesi.kItem[+kb.dataset.ki]; if (it.at != null) { it.at = null; sesi.kPilih = null; } else sesi.kPilih = sesi.kPilih === +kb.dataset.ki ? null : +kb.dataset.ki; drawKat(); return; }
    const w = e.target.closest("[data-w]");
    if (w && !w.classList.contains("used")) { let g = sesi.gap[sesi.gapSel] == null ? sesi.gapSel : sesi.gap.indexOf(null); if (g < 0) return; sesi.gap[g] = +w.dataset.w; sesi.gapSel = sesi.gap.indexOf(null); drawCelah(); return; }
    const gp = e.target.closest("[data-g]");
    if (gp) { const g = +gp.dataset.g; if (sesi.gap[g] != null) sesi.gap[g] = null; sesi.gapSel = g; drawCelah(); return; }
    const op = e.target.closest(".q-op");
    if (op) { sesi.jawaban = +op.dataset.op; $$(".q-op", stage).forEach((b) => b.classList.toggle("sel", b === op)); $("#qCek", v).disabled = false; return; }
    const l = e.target.closest("[data-l]"), r = e.target.closest("[data-r]");
    if (l && !l.classList.contains("done")) { sesi.pilih = +l.dataset.l; $$("[data-l]", stage).forEach((b) => b.classList.toggle("sel", b === l)); return; }
    if (r && !r.classList.contains("done") && sesi.pilih != null) {
      const lb = $(`[data-l="${sesi.pilih}"]`, stage);
      if (+r.dataset.r === sesi.pilih) {
        [lb, r].forEach((b) => { b.classList.remove("sel"); b.classList.add("done", "benar"); });
        sesi.cocokSisa--; sesi.pilih = null;
        if (!sesi.cocokSisa) setTimeout(() => selesaiSoal(sesi.cocokSalah === 0), 350);
      } else {
        sesi.cocokSalah++;
        [lb, r].forEach((b) => { b.classList.add("salah"); setTimeout(() => b.classList.remove("salah"), 450); });
      }
      return;
    }
    const bk = e.target.closest("#bank [data-b]");
    if (bk) { sesi.susun.push(+bk.dataset.b); bk.classList.add("used"); drawSlots(); return; }
    const sl = e.target.closest("#slots [data-s]");
    if (sl) { const idx = +sl.dataset.s; const val = sesi.susun.splice(idx, 1)[0]; $(`#bank [data-b="${val}"]`, stage).classList.remove("used"); drawSlots(); }
  });
  v.addEventListener("input", (e) => { if (e.target.id === "qIn" && !sesi.terkunci) $("#qCek", v).disabled = !e.target.value.trim(); });
  function drawKat() {
    const s = soal[sesi.i];
    const tile = (x) => { const k = sesi.kItem.indexOf(x); return `<button class="tile${sesi.kPilih === k ? " sel" : ""}" data-ki="${k}">${esc(x.t)}</button>`; };
    $("#katBank", stage).innerHTML = sesi.kItem.filter((x) => x.at == null).map(tile).join("") || `<span class="ph">Semua istilah sudah dikelompokkan.</span>`;
    s.kelompok.forEach((_, gi) => { $("#kg" + gi, stage).innerHTML = sesi.kItem.filter((x) => x.at === gi).map(tile).join(""); });
    $$(".kat-g", stage).forEach((g) => g.classList.toggle("siap", sesi.kPilih != null));
    const cek = $("#qCek", v); if (cek) cek.disabled = sesi.kItem.some((x) => x.at == null);
  }
  function drawCelah() {
    const s = soal[sesi.i];
    $("#celahTeks", stage).innerHTML = esc(s.teks).replace(/\[\[(\d+)\]\]/g, (_, i) => { const w = sesi.gap[+i]; return `<button class="gap${w != null ? " isi" : ""}${+i === sesi.gapSel ? " sel" : ""}" data-g="${i}">${w != null ? esc(sesi.kata.find((k) => k[1] === w)[0]) : "&nbsp;"}</button>`; });
    $$("#kataBank [data-w]", stage).forEach((b) => b.classList.toggle("used", sesi.gap.includes(+b.dataset.w)));
    const cek = $("#qCek", v); if (cek) cek.disabled = sesi.gap.includes(null);
  }
  function drawSlots() {
    const s = soal[sesi.i];
    $("#slots", stage).innerHTML = sesi.susun.length ? sesi.susun.map((x, i) => `<button class="tile in" data-s="${i}"><em>${i + 1}</em>${esc(s.item[x])}</button>`).join("") : `<span class="ph">Ketuk komponen di bawah sesuai urutan…</span>`;
    const cek = $("#qCek", v); if (cek) cek.disabled = sesi.susun.length !== s.item.length;
  }
  // Pintasan keyboard: 1–4 memilih, Enter memeriksa/lanjut
  const onKey = (e) => {
    if (!document.body.contains(v)) { document.removeEventListener("keydown", onKey); return; }
    if (e.key === "Enter") { const b = $("#qNext", v) || $("#qCek:not([disabled])", v); if (b) { e.preventDefault(); b.click(); } }
    if (e.target.matches && e.target.matches("input, textarea")) return;
    const n = +e.key; if (n >= 1 && n <= 4) { const o = $$(".q-op", stage)[n - 1]; if (o && !o.disabled) o.click(); }
  };
  document.addEventListener("keydown", onKey);
  render();
});

// Ambil n soal dengan tipe sebanyak mungkin berbeda (round-robin per tipe), lalu acak urutannya.
function campurTipe(list, n) {
  const g = {};
  shuffle(list).forEach((q) => (g[q.tipe] = g[q.tipe] || []).push(q));
  const out = [], ks = shuffle(Object.keys(g));
  while (out.length < n && ks.some((k) => g[k].length)) for (const k of ks) if (g[k].length && out.length < n) out.push(g[k].pop());
  return shuffle(out);
}

const PUJIAN = ["Tepat sekali!", "Mantap!", "Benar!", "Keren!", "Sempurna!"];
const pujian = () => PUJIAN[(Math.random() * PUJIAN.length) | 0];

/* ---------- Match kilat (gaya Quizlet Match) ---------- */
function matchGame(v) {
  const L = lat();
  const pasangan = shuffle(bankSoal((s) => s.tipe === "cocok").flatMap((s) => s.pasangan.map((p) => [...p, s.alat])));
  const pakai = []; const kiriSet = new Set(), kananSet = new Set();
  for (const p of pasangan) { if (pakai.length >= 6) break; if (kiriSet.has(p[0]) || kananSet.has(p[1])) continue; kiriSet.add(p[0]); kananSet.add(p[1]); pakai.push(p); }
  const tiles = shuffle([...pakai.map((p, i) => ({ t: p[0], k: i })), ...pakai.map((p, i) => ({ t: p[1], k: i }))]);
  let pilih = null, sisa = pakai.length, penalti = 0, mulai = 0, timer = 0;
  v.innerHTML = `<div class="quiz">
    <div class="q-top"><a class="q-x" href="#/latihan" title="Keluar">✕</a><div class="q-prog"><i id="qBar" style="width:0"></i></div><span class="q-xp" id="mTime">0,0 dtk</span></div>
    <div class="q-stage"><div class="q-card match-card">
      <div class="q-meta"><span class="chip dark">Match kilat</span><span class="muted">${L.match.terbaik ? `Rekor: ${L.match.terbaik.toFixed(1)} detik` : "Belum ada rekor"}</span></div>
      <h2 class="q-tanya">Cocokkan pasangan secepat mungkin. Salah pasang menambah 1 detik.</h2>
      <div class="m-board">${tiles.map((x, i) => `<button class="tile m" data-k="${x.k}" data-i="${i}" style="--i:${i}">${esc(x.t)}</button>`).join("")}</div>
    </div></div><div class="q-foot"></div></div>`;
  const tick = () => { $("#mTime", v) && ($("#mTime", v).textContent = (((Date.now() - mulai) / 1000) + penalti).toFixed(1).replace(".", ",") + " dtk"); };
  v.addEventListener("click", (e) => {
    const t = e.target.closest(".tile.m"); if (!t || t.classList.contains("done")) return;
    if (!mulai) { mulai = Date.now(); timer = setInterval(tick, 100); }
    if (!pilih) { pilih = t; t.classList.add("sel"); return; }
    if (pilih === t) { t.classList.remove("sel"); pilih = null; return; }
    if (pilih.dataset.k === t.dataset.k) {
      [pilih, t].forEach((b) => { b.classList.remove("sel"); b.classList.add("done", "benar"); });
      sisa--; $("#qBar", v).style.width = ((pakai.length - sisa) / pakai.length) * 100 + "%";
      if (!sisa) {
        clearInterval(timer);
        const waktu = (Date.now() - mulai) / 1000 + penalti;
        const rekor = !L.match.terbaik || waktu < L.match.terbaik;
        if (rekor) L.match.terbaik = waktu;
        L.xp += 30; L.hari[today()] = (L.hari[today()] || 0) + pakai.length; saveLater("progres", 200);
        if (rekor) confetti();
        $(".q-foot", v).className = "q-foot ok";
        $(".q-foot", v).innerHTML = `<div class="fb"><b>${rekor ? "Rekor baru!" : "Selesai!"} ${waktu.toFixed(1).replace(".", ",")} detik</b><p>+30 XP. ${rekor ? "" : `Rekormu ${L.match.terbaik.toFixed(1).replace(".", ",")} detik.`}</p></div><div style="display:flex;gap:8px"><a class="btn" href="#/latihan">Selesai</a><button class="btn lg ok" id="mLagi">Main lagi</button></div>`;
        $("#mLagi", v).onclick = () => router();
      }
    } else {
      penalti += 1;
      [pilih, t].forEach((b) => { b.classList.add("salah"); setTimeout(() => b.classList.remove("salah", "sel"), 420); });
    }
    pilih = null;
  });
}

/* ---------- angka naik perlahan ---------- */
function countUp(root) {
  if (reduceMotion()) return;
  $$("[data-count]", root).forEach((el) => {
    const end = +el.dataset.count; if (!end) return;
    const t0 = performance.now(), dur = 900;
    const step = (t) => { const p = Math.min(1, (t - t0) / dur); el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))); if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  });
}
