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

const TIPE = { pg: "Pilihan ganda", kasus: "Studi kasus", bs: "Benar atau salah", cocok: "Cocokkan", urut: "Urutkan" };
const shuffle = (arr) => { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = (Math.random() * (i + 1)) | 0; [a[i], a[j]] = [a[j], a[i]]; } return a; };
const pickN = (arr, n) => shuffle(arr).slice(0, n);
const today = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
const potong = (s, n = 90) => (s.length > n ? s.slice(0, n - 1).trim() + "…" : s);

function lat() {
  const L = S.progres.latihan = S.progres.latihan || {};
  L.xp = L.xp || 0; L.hari = L.hari || {}; L.alat = L.alat || {}; L.salah = L.salah || []; L.match = L.match || {};
  return L;
}
function streak() {
  const L = lat();
  let n = 0; const d = new Date();
  if (!L.hari[today()]) d.setDate(d.getDate() - 1);
  for (;;) { const k = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; if (!L.hari[k]) break; n++; d.setDate(d.getDate() - 1); }
  return n;
}

/* ---------- soal otomatis dari data alat ---------- */
function autoSoal(a) {
  const out = [];
  const blok = (a.blok || []).filter((b) => b.nama);
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
      <a class="card mode-card${L.salah.length ? "" : " dis"}" href="${L.salah.length ? "#/latihan/mode/salah" : "#/latihan"}" style="--i:4"><span class="mode-ico">🔁</span><b>Ulangi yang salah</b><p>${L.salah.length ? `${L.salah.length} soal menunggu diulang.` : "Belum ada. Soal yang salah akan muncul di sini."}</p></a></div>
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
  countUp(v);
});

/* ---------- sesi latihan ---------- */
route(/^latihan\/(mode|alat|topik)\/([^/]+)$/, (v, jenis, key) => {
  const L = lat();
  let soal = [], judul = "", konteks = null;
  if (jenis === "alat") { const a = alatById(key); if (!a) { location.hash = "#/latihan"; return; } konteks = a.id; judul = a.nama; soal = pickN(bankSoal((s) => s.alat === a.id), 10); }
  else if (jenis === "topik") { const t = (S.lanjutan || []).find((x) => x.id === key); judul = t ? t.nama : key; konteks = key; soal = pickN((S.soal || []).filter((s) => s.alat === key), 10); }
  else if (key === "cepat") { judul = "Latihan cepat"; soal = pickN(bankSoal((s) => alatById(s.alat)), 10); }
  else if (key === "urut") { judul = "Urutkan alur sinyal"; soal = pickN(bankSoal((s) => s.tipe === "urut"), 8); }
  else if (key === "kasus") { judul = "Studi kasus"; soal = pickN(bankSoal((s) => s.tipe === "kasus"), 10); }
  else if (key === "salah") { judul = "Ulangi yang salah"; soal = L.salah.map(soalById).filter(Boolean).slice(0, 12); }
  else if (key === "match") { return matchGame(v); }
  if (!soal.length) { v.innerHTML = `<div class="page"><div class="empty">Belum ada soal untuk bagian ini. <a href="#/latihan">Kembali</a></div></div>`; return; }

  const sesi = { i: 0, benar: 0, combo: 0, comboMax: 0, xp: 0, salah: [], mulai: Date.now(), jawaban: null, terkunci: false };
  const tutup = () => (konteks && jenis === "alat" ? `#/alat/${konteks}` : konteks ? `#/lanjutan/${konteks}` : "#/latihan");

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
    const a = alatById(s.alat), lt = (S.lanjutan || []).find((x) => x.id === s.alat);
    const head = `<div class="q-meta"><span class="chip dark">${TIPE[s.tipe] || s.tipe}</span>${a ? `<span class="chip">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</span>` : lt ? `<span class="chip">${esc(lt.ikon)} ${esc(lt.singkat)}</span>` : ""}<span class="muted">${sesi.i + 1} / ${soal.length}</span></div>
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
    }
    stage.innerHTML = `<div class="q-card">${head}${body}</div>`;
    stage.firstElementChild.classList.add("enter");
    setFoot("", s.tipe === "cocok" ? `<span class="muted">Ketuk satu kotak kiri lalu pasangannya di kanan.</span>` : `<span></span><button class="btn primary lg" id="qCek" disabled>Periksa</button>`);
  }

  function cekJawaban() {
    const s = soal[sesi.i];
    let ok = false;
    if (s.tipe === "pg" || s.tipe === "kasus") ok = sesi.urutOpsi[sesi.jawaban][1] === s.jawab;
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
    if (s.tipe === "pg" || s.tipe === "kasus") $$(".q-op", stage).forEach((b, i) => { b.disabled = true; if (sesi.urutOpsi[i][1] === s.jawab) b.classList.add("benar"); else if (+b.dataset.op === sesi.jawaban) b.classList.add("salah"); });
    if (s.tipe === "bs") $$(".q-op", stage).forEach((b) => { b.disabled = true; if ((+b.dataset.op === 1) === !!s.jawab) b.classList.add("benar"); else if (+b.dataset.op === sesi.jawaban) b.classList.add("salah"); });
    if (s.tipe === "urut") $$("#slots .tile", stage).forEach((b, i) => b.classList.add(sesi.susun[i] === i ? "benar" : "salah"));
    const kunci = s.tipe === "urut" && !ok ? `<div class="kunci">Urutan benar: ${s.item.map(esc).join(" → ")}</div>` : "";
    setFoot(ok ? "ok" : "no", `<div class="fb"><b>${ok ? pujian() : "Belum tepat"}</b><p>${esc(s.bahas || "")}</p>${kunci}</div><button class="btn lg ${ok ? "ok" : "no"}" id="qNext">${sesi.i + 1 < soal.length ? "Lanjut" : "Lihat hasil"}</button>`);
    if (!ok) stage.firstElementChild.classList.add("shake");
    $("#qNext", v).focus();
  }

  function akhir() {
    const pct = Math.round((sesi.benar / soal.length) * 100);
    const detik = Math.round((Date.now() - sesi.mulai) / 1000);
    L.xp += sesi.xp; L.hari[today()] = (L.hari[today()] || 0) + soal.length;
    if (jenis === "alat") { const r = L.alat[konteks] = L.alat[konteks] || {}; r.benar = (r.benar || 0) + sesi.benar; r.total = (r.total || 0) + soal.length; r.terbaik = Math.max(r.terbaik || 0, pct); }
    else soal.forEach((s, i) => { if (!alatById(s.alat)) return; const r = L.alat[s.alat] = L.alat[s.alat] || {}; r.total = (r.total || 0) + 1; r.benar = (r.benar || 0) + (sesi.salah.includes(s) ? 0 : 1); });
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
  function drawSlots() {
    const s = soal[sesi.i];
    $("#slots", stage).innerHTML = sesi.susun.length ? sesi.susun.map((x, i) => `<button class="tile in" data-s="${i}"><em>${i + 1}</em>${esc(s.item[x])}</button>`).join("") : `<span class="ph">Ketuk komponen di bawah sesuai urutan…</span>`;
    $("#qCek", v).disabled = sesi.susun.length !== s.item.length;
  }
  // Pintasan keyboard: 1–4 memilih, Enter memeriksa/lanjut
  const onKey = (e) => {
    if (!document.body.contains(v)) { document.removeEventListener("keydown", onKey); return; }
    if (e.key === "Enter") { const b = $("#qNext", v) || $("#qCek:not([disabled])", v); if (b) { e.preventDefault(); b.click(); } }
    const n = +e.key; if (n >= 1 && n <= 4) { const o = $$(".q-op", stage)[n - 1]; if (o && !o.disabled) o.click(); }
  };
  document.addEventListener("keydown", onKey);
  render();
});

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
