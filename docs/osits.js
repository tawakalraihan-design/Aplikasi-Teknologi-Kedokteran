"use strict";

/* =========================================================
   v1.5: OSITS FISIKA (ONMIPA-PT bidang Fisika)
   Data: osits.json berisi entri "bidang" (5 bidang uji), "buku" (buku acuan
   di D:\Project ITS\Peserta_OSITS Fisika\Buku) dan "paket" (10 paket latsol).
   Cara belajar tiap soal (retrieval practice + worked example bertahap):
     1. coba kerjakan sendiri di kertas,
     2. buka petunjuk, lalu langkah satu per satu,
     3. bandingkan dengan jawaban akhir,
     4. nilai diri: Bisa / Ragu / Belum. Yang belum bisa muncul lagi di "Lanjutkan".
   Simulasi ujian memakai aturan asli: 120 menit untuk 2017, dan 2024 berurutan
   dengan batas waktu per soal (tidak bisa kembali ke soal sebelumnya).
   Rumus ditulis LaTeX $...$ dan dirender KaTeX (web/katex, tanpa internet).
   Progres: S.progres.osits = { nilai, catatan, hasil, sesi, tanggal }.
   ========================================================= */

ICON.osits = P("M12 12m-1.6 0a1.6 1.6 0 1 0 3.2 0a1.6 1.6 0 1 0-3.2 0M12 3c4.2 0 6 4 6 9s-1.8 9-6 9-6-4-6-9 1.8-9 6-9zM3.6 7.5c2.1-3.6 6.5-3.1 10.8-.6s7.1 6 5 9.6-6.5 3.1-10.8.6-7.1-6-5-9.6z");

const OSITS_NILAI = { bisa: ["Bisa", "var(--sudah)"], ragu: ["Ragu", "var(--sedang)"], belum: ["Belum bisa", "var(--danger)"] };
const OSITS_TINGKAT = ["Regional", "Nasional", "Wilayah"];
const ositsData = () => S.osits || [];
const ositsBidangList = () => ositsData().filter((x) => x.jenis === "bidang");
const ositsBidang = (id) => ositsBidangList().find((b) => b.id === id);
const ositsBuku = (id) => ositsData().find((x) => x.jenis === "buku" && x.id === id);
const ositsPaketList = () => ositsData().filter((x) => x.jenis === "paket");
const ositsPaket = (id) => ositsPaketList().find((p) => p.id === id);
const ositsSemua = () => ositsPaketList().flatMap((p) => p.soal.map((q) => [q, p]));
const ositsSoal = (id) => ositsSemua().find(([q]) => q.id === id) || [];
function osP() {
  const O = (S.progres.osits = S.progres.osits || {});
  O.nilai = O.nilai || {}; O.catatan = O.catatan || {}; O.hasil = O.hasil || {};
  return O;
}
const osNilai = (qid) => osP().nilai[qid] || null;
const osHitung = (list) => ({ total: list.length, bisa: list.filter(([q]) => osNilai(q.id) === "bisa").length, ragu: list.filter(([q]) => osNilai(q.id) === "ragu").length, belum: list.filter(([q]) => osNilai(q.id) === "belum").length });
const osPct = (h) => (h.total ? Math.round((h.bisa / h.total) * 100) : 0);
const osWarna = (bid) => (ositsBidang(bid) || {}).warna || "#8a8985";
const osSoalNo = (q, p) => `${p.tingkat} ${p.tahun} · ${(ositsBidang(p.bidang[0]) || {}).singkat || ""} no. ${q.no}`;
const osFmtWaktu = (dtk) => { dtk = Math.max(0, Math.round(dtk)); const j = Math.floor(dtk / 3600), m = Math.floor((dtk % 3600) / 60), s = dtk % 60; return (j ? j + ":" + String(m).padStart(2, "0") : m) + ":" + String(s).padStart(2, "0"); };

// Rumus: auto-render KaTeX pada elemen (dipakai juga oleh latihan.js).
function rumusIn(el) {
  if (!el || typeof renderMathInElement !== "function") return;
  try {
    renderMathInElement(el, { delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }], throwOnError: false, strict: "ignore", ignoredClasses: ["no-math"] });
  } catch (e) {}
}

// Soal berikutnya yang paling berguna: yang belum dinilai, lalu yang ragu/belum bisa.
function osBerikut(list) {
  list = list || ositsSemua();
  return list.find(([q]) => !osNilai(q.id)) || list.find(([q]) => osNilai(q.id) !== "bisa") || null;
}
function osTerbaik(pid) {
  const h = osP().hasil[pid] || [];
  return h.length ? h.reduce((a, b) => (b.skor / b.maks > a.skor / a.maks ? b : a)) : null;
}
function osDot(qid) {
  const n = osNilai(qid);
  return `<span class="os-dot${n ? " " + n : ""}" title="${n ? OSITS_NILAI[n][0] : "Belum dinilai"}"></span>`;
}
function osBar(h) {
  const w = (n) => (h.total ? (n / h.total) * 100 : 0);
  return `<div class="os-bar" title="${h.bisa} bisa · ${h.ragu} ragu · ${h.belum} belum bisa · ${h.total - h.bisa - h.ragu - h.belum} belum dicoba"><i class="b" style="width:${w(h.bisa)}%"></i><i class="r" style="width:${w(h.ragu)}%"></i><i class="x" style="width:${w(h.belum)}%"></i></div>`;
}
function osBukuBtn(file) {
  return DESKTOP ? `<button class="btn sm" data-file="${esc(file)}" hidden>${ico("file", 14)} Buka PDF</button>` : "";
}
function osSoalRow([q, p], showPaket) {
  return `<a class="os-row" href="#/osits/soal/${esc(q.id)}" style="--bc:${osWarna(q.bidang)}">
    ${osDot(q.id)}<span class="os-no">${q.no}</span>
    <div><b>${esc(q.topik)}</b><small>${showPaket ? esc(osSoalNo(q, p)) + " · " : ""}${q.bagian.length > 1 ? q.bagian.length + " bagian · " : ""}${q.menit ? q.menit + " menit" : q.poin + " poin"}</small></div>
    ${q.gambar ? `<span class="os-ic" title="Ada gambar">${ico("image", 15)}</span>` : ""}${ico("arrow", 16)}</a>`;
}

/* ---------- beranda: kartu cepat dan pencarian ---------- */
function ositsQuickHtml() {
  const semua = ositsSemua();
  if (!semua.length) return "";
  const h = osHitung(semua), nx = osBerikut(semua);
  return `<a class="card quick-card" href="${nx ? "#/osits/soal/" + esc(nx[0].id) : "#/osits"}" style="--i:2;--qc:#82bcff">
    <span class="q-ico">${ico("osits", 22)}</span><div><small>${h.bisa ? "Lanjutkan OSITS Fisika" : "Baru: persiapan OSITS Fisika"}</small><b>${nx ? esc(nx[0].topik) : "Semua soal sudah dikuasai"}</b>
    <span class="muted">${h.bisa} dari ${h.total} soal dikuasai</span></div>${ico("arrow", 18)}</a>`;
}
function ositsCari(q) {
  const hit = (s) => String(s || "").toLowerCase().includes(q);
  return ositsSemua().filter(([s]) => hit(s.topik) || hit(s.teks) || (s.konsep || []).some(hit)).slice(0, 6);
}

/* =========================================================
   HUB
   ========================================================= */
route(/^osits$/, (v) => {
  const semua = ositsSemua();
  if (!semua.length) { v.innerHTML = `<div class="page"><div class="empty">Data OSITS belum ada. Pastikan file data\\osits.json tersedia.</div></div>`; return; }
  const O = osP();
  const draw = () => {
    const h = osHitung(semua), pct = osPct(h), nx = osBerikut(semua);
    const hari = O.tanggal ? Math.ceil((new Date(O.tanggal + "T00:00:00") - new Date(new Date().toDateString())) / 864e5) : null;
    const nSim = Object.values(O.hasil).reduce((s, a) => s + a.length, 0);
    const nLat = (S.soal || []).filter((s) => s.osits).length;
    v.innerHTML = `<div class="page">
      <section class="os-hero card">
        <div class="kh-main">
          <span class="hero-badge"><i></i>ONMIPA-PT · Bidang Fisika</span>
          <h1>OSITS Fisika</h1>
          <p class="lead">${semua.length} soal asli dari 10 paket latsol (Regional dan Nasional 2017, Wilayah 2024). Setiap soal dibahas bertahap: coba sendiri dulu, buka petunjuk, ikuti langkah satu per satu, bandingkan jawaban akhir, lalu nilai dirimu.</p>
          <div class="kh-act">
            ${nx ? `<a class="btn primary" href="#/osits/soal/${esc(nx[0].id)}">${ico("play", 16)} ${h.bisa + h.ragu + h.belum ? "Lanjutkan" : "Mulai"}: ${esc(nx[0].topik)}</a>` : ""}
            <a class="btn" href="#/latihan/osits/semua">${ico("latihan", 16)} Latihan cepat · ${nLat} soal</a>
          </div>
        </div>
        <div class="kh-ring"><div class="ring" style="--p:${pct}" data-label="${pct}%"></div><small>${h.bisa} dari ${h.total} dikuasai</small></div>
      </section>

      <div class="os-stats stagger">
        <div class="card os-stat" style="--i:0;--sc:var(--sudah)"><b data-count="${h.bisa}">${h.bisa}</b><span>bisa</span></div>
        <div class="card os-stat" style="--i:1;--sc:var(--sedang)"><b data-count="${h.ragu}">${h.ragu}</b><span>ragu</span></div>
        <div class="card os-stat" style="--i:2;--sc:var(--danger)"><b data-count="${h.belum}">${h.belum}</b><span>belum bisa</span></div>
        <div class="card os-stat" style="--i:3;--sc:var(--inti)"><b data-count="${nSim}">${nSim}</b><span>simulasi selesai</span></div>
        <label class="card os-stat os-tgl" style="--i:4;--sc:var(--penting)">
          ${hari != null ? `<b>${hari > 0 ? "H−" + hari : hari === 0 ? "Hari ini" : "Lewat"}</b>` : `<b>${ico("plus", 18)}</b>`}
          <span>tanggal OSITS</span><input type="date" id="osTgl" value="${esc(O.tanggal || "")}" title="Atur tanggal lomba untuk hitung mundur"></label>
      </div>

      <section class="section">
        <div class="section-head"><div><h2>Lima bidang uji</h2><span class="sub">Ringkasan konsep, rumus kunci, strategi, dan bab buku acuan untuk tiap bidang.</span></div></div>
        <div class="os-bidang-grid stagger">${ositsBidangList().map((b, i) => { const l = semua.filter(([q]) => q.bidang === b.id), hb = osHitung(l); return `<a class="card os-bidang" href="#/osits/bidang/${esc(b.id)}" style="--i:${i};--bc:${b.warna}">
          <span class="os-bico">${esc(b.ikon)}</span><b>${esc(b.nama)}</b><p>${esc(b.ringkas.split(". ")[0].replace(/\.$/, ""))}.</p>
          ${osBar(hb)}<small>${hb.bisa}/${hb.total} soal dikuasai · ${b.konsep.length} konsep</small></a>`; }).join("")}</div>
      </section>

      ${OSITS_TINGKAT.map((t) => { const ps = ositsPaketList().filter((p) => p.tingkat === t); if (!ps.length) return ""; return `<section class="section">
        <div class="section-head"><div><h2>${t} ${ps[0].tahun}</h2><span class="sub">${esc(ps[0].aturan)}</span></div></div>
        <div class="os-paket-grid stagger">${ps.map((p, i) => { const l = p.soal.map((q) => [q, p]), hp = osHitung(l), tb = osTerbaik(p.id); return `<article class="card os-paket" style="--i:${i}">
          <div class="op-head"><div class="op-bd">${p.bidang.map((b) => `<span class="bd-dot" style="--bd:${osWarna(b)}"></span>`).join("")}</div><small>${esc(p.tanggal)}</small></div>
          <h3>${esc(p.judul)}</h3>
          <p class="muted">${p.soal.length} soal · ${p.waktu} menit${p.kalkulator ? "" : " · tanpa kalkulator"}${tb ? ` · simulasi terbaik ${Math.round((tb.skor / tb.maks) * 100)}%` : ""}</p>
          ${osBar(hp)}
          <div class="op-act"><a class="btn sm" href="#/osits/paket/${esc(p.id)}">${ico("list", 14)} Daftar soal</a><a class="btn sm primary" href="#/osits/ujian/${esc(p.id)}">${ico("play", 14)} Simulasi</a></div>
        </article>`; }).join("")}</div></section>`; }).join("")}

      <section class="card panel">
        <h3>${ico("bulb", 18)} Cara memakai pembahasan bertahap</h3>
        <div class="os-cara">${[["1", "Coba dulu", "Kerjakan di kertas tanpa melihat apa pun, minimal 5–10 menit per soal."], ["2", "Petunjuk", "Bila buntu, buka petunjuk: hanya ide awal, bukan jawaban."], ["3", "Langkah demi langkah", "Buka satu langkah, lalu coba lanjutkan sendiri sebelum membuka berikutnya."], ["4", "Nilai diri", "Bisa, Ragu, atau Belum bisa. Soal yang ragu dan belum bisa diulang lebih dulu."]].map(([n, t, d]) => `<div><span>${n}</span><b>${t}</b><small>${d}</small></div>`).join("")}</div>
        <p class="muted" style="font-size:.84rem">Pembahasan disusun ulang dari soal asli, bukan kunci resmi panitia. Bila menemukan kejanggalan, cek ke buku acuan di tiap bidang.</p>
      </section>

      <section class="section">
        <div class="section-head"><div><h2>Buku acuan</h2><span class="sub">Dari folder <code>Peserta_OSITS Fisika\\Buku</code> di laptop.</span></div></div>
        <div class="os-buku-grid">${ositsData().filter((x) => x.jenis === "buku").map((k) => `<div class="card os-buku"><div><b>${esc(k.singkat)}</b><small>${esc(k.penulis)} · ${k.halaman} hal.</small><p>${esc(k.ket)}</p>
          <div class="chips">${k.bidang.map((b) => `<span class="chip"><span class="bd-dot" style="--bd:${osWarna(b)}"></span>${esc((ositsBidang(b) || {}).singkat || b)}</span>`).join("")}</div></div>${osBukuBtn(k.file)}</div>`).join("")}</div>
      </section>
    </div>`;
    if (typeof countUp === "function") countUp(v);
    tandaiFileAda(v);
  };
  v.addEventListener("click", (e) => { const f = e.target.closest("[data-file]"); if (f) openFile(f.dataset.file); });
  v.addEventListener("change", (e) => { if (e.target.id === "osTgl") { O.tanggal = e.target.value || undefined; saveLater("progres", 200); draw(); } });
  draw();
});

/* =========================================================
   BIDANG
   ========================================================= */
route(/^osits\/bidang\/([^/]+)$/, (v, bid) => {
  const b = ositsBidang(bid);
  if (!b) { location.hash = "#/osits"; return; }
  const list = ositsSemua().filter(([q]) => q.bidang === b.id);
  const h = osHitung(list), pct = osPct(h), nx = osBerikut(list);
  const nLat = (S.soal || []).filter((s) => s.osits === b.id).length;
  const mk = (b.materi || []).map(materiById).filter(Boolean);
  v.innerHTML = `<div class="page">
    <a class="link" href="#/osits">${ico("back", 14)} OSITS Fisika</a>
    <section class="os-hero card" style="--bc:${b.warna}">
      <div class="kh-main">
        <span class="hero-badge"><i style="background:${b.warna}"></i>Bidang uji ONMIPA</span>
        <h1>${esc(b.ikon)} ${esc(b.nama)}</h1>
        <p class="lead">${esc(b.ringkas)}</p>
        <div class="kh-act">
          ${nx ? `<a class="btn primary" href="#/osits/soal/${esc(nx[0].id)}">${ico("play", 16)} Kerjakan: ${esc(nx[0].topik)}</a>` : ""}
          ${nLat ? `<a class="btn" href="#/latihan/osits/${esc(b.id)}">${ico("latihan", 16)} Latihan cepat · ${nLat} soal</a>` : ""}
        </div>
      </div>
      <div class="kh-ring"><div class="ring" style="--p:${pct}" data-label="${pct}%"></div><small>${h.bisa} dari ${h.total} soal</small></div>
    </section>

    <section class="section">
      <div class="section-head"><div><h2>Konsep dan rumus kunci</h2><span class="sub">${b.konsep.length} konsep yang paling sering keluar di soal latsol.</span></div></div>
      <div class="os-konsep-grid">${b.konsep.map((k, i) => `<article class="card os-konsep reveal" style="--i:${i}"><h3><span>${i + 1}</span>${esc(k.judul)}</h3><p>${esc(k.isi)}</p>${k.rumus.map((r) => `<div class="os-rumus">${esc(r)}</div>`).join("")}</article>`).join("")}</div>
    </section>

    <div class="os-two">
      <section class="card panel"><h3>${ico("bulb", 18)} Strategi mengerjakan</h3><ul class="os-ul">${b.strategi.map((s) => `<li>${esc(s)}</li>`).join("")}</ul>
        ${mk.length ? `<h3 style="margin-top:8px">Mata kuliah terkait</h3><div class="chips">${mk.map((m) => `<a class="chip outline" href="#/materi/${esc(m.id)}">${esc(m.nama)}</a>`).join("")}</div>` : ""}</section>
      <section class="card panel"><h3>${ico("materi", 18)} Bab buku acuan</h3>
        <ul class="os-bab">${b.buku.map((r) => { const k = ositsBuku(r.buku); return k ? `<li><div><b>${esc(r.bab)}</b><small>${esc(k.singkat)}${r.hal ? ` · mulai hal. PDF ${r.hal}` : ""}</small></div>${osBukuBtn(k.file)}</li>` : ""; }).join("")}</ul>
        <p class="muted" style="font-size:.8rem">Nomor halaman hanya untuk buku yang teksnya terbaca (Griffiths, Krane). Ketik nomornya di kotak halaman pembaca PDF.</p></section>
    </div>

    <section class="section">
      <div class="section-head"><div><h2>Soal bidang ini</h2><span class="sub">${list.length} soal dari semua paket. Titik warna = penilaian dirimu.</span></div></div>
      <div class="card os-list">${list.map((x) => osSoalRow(x, true)).join("")}</div>
    </section>
  </div>`;
  v.addEventListener("click", (e) => { const f = e.target.closest("[data-file]"); if (f) openFile(f.dataset.file); });
  rumusIn(v);
  tandaiFileAda(v);
});

/* =========================================================
   PAKET
   ========================================================= */
route(/^osits\/paket\/([^/]+)$/, (v, pid) => {
  const p = ositsPaket(pid);
  if (!p) { location.hash = "#/osits"; return; }
  const list = p.soal.map((q) => [q, p]), h = osHitung(list), hasil = (osP().hasil[p.id] || []).slice().reverse();
  v.innerHTML = `<div class="page">
    <a class="link" href="#/osits">${ico("back", 14)} OSITS Fisika</a>
    <section class="card panel os-paket-head">
      <div class="chips"><span class="chip dark">${esc(p.tingkat)} ${p.tahun}</span><span class="chip">${esc(p.tanggal)}</span><span class="chip">${p.waktu} menit</span>${p.bidang.map((b) => `<a class="chip outline" href="#/osits/bidang/${esc(b)}"><span class="bd-dot" style="--bd:${osWarna(b)}"></span>${esc(ositsBidang(b).nama)}</a>`).join("")}</div>
      <h1>${esc(p.judul)}</h1>
      <p class="muted">${esc(p.aturan)}</p>
      ${osBar(h)}<small class="muted">${h.bisa} bisa · ${h.ragu} ragu · ${h.belum} belum bisa · ${h.total - h.bisa - h.ragu - h.belum} belum dicoba</small>
      <div class="kh-act"><a class="btn primary" href="#/osits/ujian/${esc(p.id)}">${ico("play", 16)} Simulasi ujian ${p.waktu} menit</a>${osBukuBtn(p.file).replace("Buka PDF", "PDF soal asli")}</div>
    </section>
    <div class="card os-list">${list.map((x) => osSoalRow(x, false)).join("")}</div>
    ${hasil.length ? `<section class="card panel"><h3>Riwayat simulasi</h3><div class="os-hasil">${hasil.slice(0, 8).map((r) => `<div><b>${Math.round((r.skor / r.maks) * 100)}%</b><small>${r.skor.toLocaleString("id-ID")} / ${r.maks} poin · ${osFmtWaktu(r.durasi)} · ${new Date(r.t).toLocaleDateString("id-ID", { day: "numeric", month: "short" })}</small></div>`).join("")}</div></section>` : ""}
  </div>`;
  v.addEventListener("click", (e) => { const f = e.target.closest("[data-file]"); if (f) openFile(f.dataset.file); });
  tandaiFileAda(v);
});

/* =========================================================
   SOAL: pembahasan bertahap
   ========================================================= */
ui.osBuka = ui.osBuka || {}; // id soal → [tingkat buka tiap bagian]
route(/^osits\/soal\/([^/]+)$/, (v, sid) => {
  const [q, p] = ositsSoal(sid);
  if (!q) { location.hash = "#/osits"; return; }
  const O = osP();
  const idx = p.soal.indexOf(q), prev = p.soal[idx - 1], next = p.soal[idx + 1];
  const buka = (ui.osBuka[q.id] = ui.osBuka[q.id] || q.bagian.map(() => 0));
  // Tingkat buka: 0 tertutup, 1 petunjuk, 2..n+1 langkah ke-1..n, n+2 jawaban akhir.
  const bagianHtml = (b, i) => {
    const n = b.langkah.length, t = buka[i], akhir = n + 2;
    return `<section class="card os-bagian${t >= akhir ? " selesai" : ""}" data-bi="${i}">
      <div class="ob-head">${b.label ? `<span class="ob-lbl">${esc(b.label)}</span>` : ""}<div class="ob-tanya">${b.tanya ? esc(b.tanya) : `<span class="muted">Kerjakan soal di atas.</span>`}</div>${b.poin ? `<span class="chip">${b.poin} poin</span>` : ""}</div>
      ${t >= 1 ? `<div class="ob-pet"><b>${ico("bulb", 15)} Petunjuk</b><p>${esc(b.petunjuk)}</p></div>` : ""}
      ${t >= 2 && n ? `<ol class="ob-langkah">${b.langkah.slice(0, Math.min(t - 1, n)).map((l) => `<li>${esc(l)}</li>`).join("")}</ol>` : ""}
      ${t >= akhir ? `<div class="ob-jawab"><b>${ico("check", 15)} Jawaban akhir</b><div>${esc(b.jawab)}</div></div>` : ""}
      <div class="ob-act">
        ${t === 0 ? `<button class="btn sm" data-ob="pet">${ico("bulb", 14)} Lihat petunjuk</button>` : ""}
        ${t >= 1 && t - 1 < n ? `<button class="btn sm primary" data-ob="langkah">Langkah berikutnya · ${t}/${n}</button>` : ""}
        ${t < akhir ? `<button class="btn sm ghost" data-ob="jawab">${t >= 1 && t - 1 >= n ? "Lihat jawaban akhir" : "Langsung ke jawaban"}</button>` : `<button class="btn sm ghost" data-ob="tutup">Tutup lagi</button>`}
      </div>
    </section>`;
  };
  const nilaiHtml = () => `<div class="os-nilai">${Object.entries(OSITS_NILAI).map(([k, [l, w]]) => `<button class="os-nb${osNilai(q.id) === k ? " on" : ""}" data-nilai="${k}" style="--nc:${w}">${l}</button>`).join("")}</div>`;
  const b0 = ositsBidang(q.bidang);
  v.innerHTML = `<div class="page os-soal-page">
    <div class="kp-top"><a class="link" href="#/osits/paket/${esc(p.id)}">${ico("back", 14)} ${esc(p.tingkat)} ${p.tahun} · ${esc(p.judul)}</a>
      <div class="kp-prog">${p.soal.map((x) => `<a href="#/osits/soal/${esc(x.id)}" class="${x === q ? "on" : ""}${osNilai(x.id) ? " os-" + osNilai(x.id) : ""}" title="${x.no}. ${esc(x.topik)}"></a>`).join("")}</div></div>
    <header class="os-shead">
      <div class="chips"><span class="chip dark">Soal ${q.no} dari ${p.soal.length}</span><a class="chip outline" href="#/osits/bidang/${esc(q.bidang)}"><span class="bd-dot" style="--bd:${b0.warna}"></span>${esc(b0.nama)}</a><span class="chip">${q.menit ? q.menit + " menit" : q.poin + " poin"}</span></div>
      <h1>${esc(q.topik)}</h1>
    </header>
    <section class="card os-teks">
      <div class="os-teks-isi">${esc(q.teks)}</div>
      ${q.gambar ? `<figure class="os-gambar"><img src="osits/${esc(q.gambar)}" alt="Gambar soal ${q.no}" loading="lazy"></figure>` : ""}
    </section>
    ${q.catatan ? `<div class="banner">${esc(q.catatan)}</div>` : ""}
    <div class="os-bagian-list">${q.bagian.map(bagianHtml).join("")}</div>
    <div class="os-two">
      <section class="card panel"><h3>Seberapa kamu menguasai soal ini?</h3>${nilaiHtml()}
        <textarea id="osCat" class="os-cat" placeholder="Catatan pribadi: bagian yang membuat buntu, rumus yang lupa…">${esc(O.catatan[q.id] || "")}</textarea></section>
      <section class="card panel"><h3>Konsep dan bacaan</h3>
        <div class="chips">${(q.konsep || []).map((k) => `<span class="chip">${esc(k)}</span>`).join("")}</div>
        <ul class="os-bab">${(q.buku || []).map(ositsBuku).filter(Boolean).map((k) => `<li><div><b>${esc(k.singkat)}</b><small>${esc(k.judul)}</small></div>${osBukuBtn(k.file)}</li>`).join("")}</ul></section>
    </div>
    <p class="muted" style="font-size:.8rem">Pembahasan disusun ulang, bukan kunci resmi panitia ONMIPA.</p>
    <div class="kp-foot card">
      <button class="btn" data-ob="semua">${ico("list", 16)} Buka semua pembahasan</button>
      <span style="flex:1"></span>
      ${prev ? `<a class="btn" href="#/osits/soal/${esc(prev.id)}">${ico("back", 16)} Sebelumnya</a>` : ""}
      ${next ? `<a class="btn primary" href="#/osits/soal/${esc(next.id)}">Berikutnya ${ico("arrow", 16)}</a>` : `<a class="btn primary" href="#/osits/ujian/${esc(p.id)}">Simulasi paket ini ${ico("arrow", 16)}</a>`}
    </div>
  </div>`;
  rumusIn(v);
  tandaiFileAda(v);
  const gambarUlang = (i) => { const el = $(`[data-bi="${i}"]`, v); el.outerHTML = bagianHtml(q.bagian[i], i); rumusIn($(`[data-bi="${i}"]`, v)); };
  v.addEventListener("click", (e) => {
    const f = e.target.closest("[data-file]"); if (f) { openFile(f.dataset.file); return; }
    const nb = e.target.closest("[data-nilai]");
    if (nb) {
      const k = nb.dataset.nilai;
      if (O.nilai[q.id] === k) delete O.nilai[q.id]; else O.nilai[q.id] = k;
      saveLater("progres", 300);
      $(".os-nilai", v).outerHTML = nilaiHtml();
      $$(".kp-prog a", v).forEach((a, j) => { a.className = (p.soal[j] === q ? "on" : "") + (osNilai(p.soal[j].id) ? " os-" + osNilai(p.soal[j].id) : ""); });
      if (O.nilai[q.id] === "bisa" && next) toast("Mantap. Lanjut ke soal berikutnya kapan pun siap.");
      return;
    }
    const ob = e.target.closest("[data-ob]");
    if (!ob) return;
    const a = ob.dataset.ob;
    if (a === "semua") { q.bagian.forEach((b, i) => { buka[i] = b.langkah.length + 2; gambarUlang(i); }); return; }
    const i = +ob.closest("[data-bi]").dataset.bi, n = q.bagian[i].langkah.length;
    buka[i] = a === "pet" ? 1 : a === "langkah" ? buka[i] + 1 : a === "jawab" ? n + 2 : 0;
    gambarUlang(i);
    if (a === "langkah" || a === "jawab") $(`[data-bi="${i}"] ${a === "jawab" ? ".ob-jawab" : ".ob-langkah li:last-child"}`, v)?.scrollIntoView({ block: "nearest", behavior: "smooth" });
  });
  v.addEventListener("input", (e) => {
    if (e.target.id !== "osCat") return;
    const t = e.target.value.trim();
    if (t) O.catatan[q.id] = e.target.value; else delete O.catatan[q.id];
    saveLater("progres", 900);
  });
});

/* =========================================================
   SIMULASI UJIAN
   ========================================================= */
// Sesi aktif disimpan di progres agar waktu tetap berjalan walau aplikasi ditutup.
route(/^osits\/ujian\/([^/]+)$/, (v, pid) => {
  const p = ositsPaket(pid);
  if (!p) { location.hash = "#/osits"; return; }
  const O = osP();
  const urut = p.soal.some((q) => q.menit); // 2024: berurutan dengan waktu per soal
  const maks = p.soal.reduce((s, q) => s + q.poin, 0);
  let timer = null;
  const henti = () => { clearInterval(timer); timer = null; };
  const sesi = () => (O.sesi && O.sesi.paket === p.id ? O.sesi : null);
  const simpan = () => saveLater("progres", 200);
  const tick = (fn) => { henti(); fn(); timer = setInterval(() => { if (!document.body.contains(v)) { henti(); return; } fn(); }, 1000); };

  function intro() {
    henti();
    const lain = O.sesi && O.sesi.paket !== p.id ? ositsPaket(O.sesi.paket) : null;
    const hasil = (O.hasil[p.id] || []).slice().reverse();
    v.innerHTML = `<div class="page">
      <a class="link" href="#/osits/paket/${esc(p.id)}">${ico("back", 14)} ${esc(p.judul)}</a>
      <section class="os-hero card os-ujian-intro">
        <div class="kh-main">
          <span class="hero-badge"><i></i>Simulasi ujian · ${esc(p.tingkat)} ${p.tahun}</span>
          <h1>${esc(p.judul)}</h1>
          <p class="lead">${esc(p.aturan)}</p>
          <ul class="os-ul">
            <li>Siapkan kertas dan pena${p.kalkulator ? " serta kalkulator saintifik" : ". Kalkulator tidak boleh dipakai"}.</li>
            <li>${urut ? "Soal muncul satu per satu dengan waktu masing-masing. Saat waktunya habis, soal berikutnya terbuka otomatis dan kamu tidak bisa kembali." : `Semua ${p.soal.length} soal tampil sekaligus dengan waktu total ${p.waktu} menit. Pembahasan disembunyikan selama ujian.`}</li>
            <li>Setelah selesai, cocokkan tiap jawabanmu dengan jawaban akhir, lalu beri nilai Benar, Sebagian, atau Salah.</li>
            <li>Waktu tetap berjalan walau aplikasi ditutup.</li>
          </ul>
          ${lain ? `<div class="banner">Masih ada simulasi ${esc(lain.judul)} yang berjalan. Memulai yang ini akan membatalkannya.</div>` : ""}
          <div class="kh-act"><button class="btn primary lg" id="osMulai">${ico("play", 16)} Mulai ${p.waktu} menit</button></div>
        </div>
        <div class="os-ujian-angka"><div><b>${p.soal.length}</b><small>soal</small></div><div><b>${p.waktu}</b><small>menit</small></div><div><b>${maks}</b><small>poin</small></div></div>
      </section>
      ${hasil.length ? `<section class="card panel"><h3>Riwayat</h3><div class="os-hasil">${hasil.slice(0, 8).map((r) => `<div><b>${Math.round((r.skor / r.maks) * 100)}%</b><small>${r.skor.toLocaleString("id-ID")} / ${r.maks} · ${osFmtWaktu(r.durasi)} · ${new Date(r.t).toLocaleDateString("id-ID", { day: "numeric", month: "short", year: "numeric" })}</small></div>`).join("")}</div></section>` : ""}
    </div>`;
  }

  // Header berwaktu: total untuk mode semua, per soal untuk mode berurutan.
  function barHtml(sisa, label) {
    return `<div class="os-ujian-bar card"><div><small>${esc(p.tingkat)} ${p.tahun} · ${esc(p.judul)}</small><b>${label}</b></div>
      <div class="os-jam${sisa < 300 ? " mepet" : ""}" id="osJam">${osFmtWaktu(sisa)}</div>
      <button class="btn sm" id="osKumpul">${urut ? "Kirim & lanjut" : "Kumpulkan"}</button><button class="btn sm ghost" id="osBatal" title="Batalkan simulasi">✕</button></div>`;
  }
  const soalUjianHtml = (q) => `<section class="card os-teks os-u-soal"><div class="os-u-no">${q.no}</div><div>
    <div class="os-teks-isi">${esc(q.teks)}</div>
    ${q.gambar ? `<figure class="os-gambar"><img src="osits/${esc(q.gambar)}" alt="Gambar soal ${q.no}"></figure>` : ""}
    ${q.bagian.some((b) => b.tanya) ? `<ol class="os-u-bag">${q.bagian.map((b) => `<li data-l="${esc(b.label)}">${esc(b.tanya)}${b.poin ? ` <span class="chip">${b.poin} poin</span>` : ""}</li>`).join("")}</ol>` : ""}
    <small class="muted">${q.menit ? q.menit + " menit · " : ""}${q.poin} poin</small></div></section>`;

  function berjalan() {
    const s = sesi();
    if (urut) {
      const q = p.soal[s.i];
      const batas = s.mulaiSoal + q.menit * 60000;
      v.innerHTML = `<div class="page os-ujian">${barHtml((batas - Date.now()) / 1000, `Soal ${s.i + 1} dari ${p.soal.length}`)}
        <div class="os-u-prog">${p.soal.map((x, j) => `<i class="${j < s.i ? "done" : j === s.i ? "on" : ""}"></i>`).join("")}</div>
        ${soalUjianHtml(q)}</div>`;
      rumusIn(v);
      tick(() => {
        const sisa = (batas - Date.now()) / 1000;
        const j = $("#osJam", v); if (j) { j.textContent = osFmtWaktu(sisa); j.classList.toggle("mepet", sisa < 120); }
        if (sisa <= 0) lanjutUrut(true);
      });
    } else {
      const batas = s.mulai + p.waktu * 60000;
      v.innerHTML = `<div class="page os-ujian">${barHtml((batas - Date.now()) / 1000, `${p.soal.length} soal · ${maks} poin`)}
        ${p.soal.map(soalUjianHtml).join("")}
        <div class="kp-foot card"><span class="muted">Sudah selesai semua?</span><span style="flex:1"></span><button class="btn primary" id="osKumpul2">Kumpulkan dan nilai</button></div></div>`;
      rumusIn(v);
      tick(() => {
        const sisa = (batas - Date.now()) / 1000;
        const j = $("#osJam", v); if (j) { j.textContent = osFmtWaktu(sisa); j.classList.toggle("mepet", sisa < 300); }
        if (sisa <= 0) { toast("Waktu habis. Saatnya menilai jawabanmu."); kumpul(); }
      });
    }
  }
  function lanjutUrut(habis) {
    const s = sesi();
    // Bila aplikasi lama ditutup, lompati soal yang waktunya sudah habis.
    let t = s.mulaiSoal;
    s.i++;
    if (habis) { t += p.soal[s.i - 1].menit * 60000; while (s.i < p.soal.length && t + p.soal[s.i].menit * 60000 <= Date.now()) { t += p.soal[s.i].menit * 60000; s.i++; } }
    s.mulaiSoal = habis ? t : Date.now();
    simpan();
    if (s.i >= p.soal.length) kumpul(); else berjalan();
  }
  function kumpul() {
    const s = sesi(); if (!s) return;
    henti();
    s.selesai = s.selesai || Date.now();
    s.skor = s.skor || {};
    simpan();
    penilaian();
  }
  function skorTotal() {
    const s = sesi(); let n = 0;
    for (const q of p.soal) q.bagian.forEach((b, i) => { const k = s.skor[q.id + "|" + i]; const bobot = b.poin || q.poin / q.bagian.length; if (k != null) n += bobot * k; });
    return Math.round(n * 10) / 10;
  }
  function penilaian() {
    henti();
    const s = sesi();
    const nBag = p.soal.reduce((a, q) => a + q.bagian.length, 0), nDinilai = Object.keys(s.skor).length;
    const opsi = [[1, "Benar"], [0.5, "Sebagian"], [0, "Salah"]];
    v.innerHTML = `<div class="page">
      <section class="card panel os-nilai-head"><h1>Nilai jawabanmu</h1>
        <p class="muted">Waktu pengerjaan ${osFmtWaktu((s.selesai - s.mulai) / 1000)}. Bandingkan setiap bagian dengan jawaban akhir, lalu pilih Benar, Sebagian, atau Salah. Buka soal untuk melihat langkah lengkapnya.</p>
        <div class="os-skor"><b id="osSkor">${skorTotal().toLocaleString("id-ID")}</b><span>/ ${maks} poin · <span id="osDinilai">${nDinilai}</span>/${nBag} bagian dinilai</span></div></section>
      ${p.soal.map((q) => `<section class="card panel os-n-soal"><div class="os-n-top"><span class="os-u-no">${q.no}</span><b>${esc(q.topik)}</b><a class="link" href="#/osits/soal/${esc(q.id)}">langkah lengkap</a></div>
        ${q.bagian.map((b, i) => { const k = s.skor[q.id + "|" + i]; return `<div class="os-n-bag"><div class="os-n-j">${b.label ? `<span class="ob-lbl">${esc(b.label)}</span>` : ""}<div>${esc(b.jawab)}</div></div>
          <div class="seg" data-sk="${esc(q.id)}|${i}">${opsi.map(([val, l]) => `<button class="${k === val ? "on" : ""}" data-v="${val}">${l}</button>`).join("")}</div></div>`; }).join("")}</section>`).join("")}
      <div class="kp-foot card"><button class="btn ghost" id="osBuang">Buang tanpa menyimpan</button><span style="flex:1"></span><button class="btn primary" id="osSimpan">Simpan hasil</button></div>
    </div>`;
    rumusIn(v);
  }
  function selesai() {
    const s = sesi(), skor = skorTotal(), pct = Math.round((skor / maks) * 100);
    (O.hasil[p.id] = O.hasil[p.id] || []).push({ t: Date.now(), skor, maks, durasi: Math.round((s.selesai - s.mulai) / 1000) });
    // Penilaian simulasi menjadi penilaian diri tiap soal (bukti terbaru).
    for (const q of p.soal) {
      const ks = q.bagian.map((b, i) => s.skor[q.id + "|" + i]).filter((x) => x != null);
      if (!ks.length) continue;
      const r = ks.reduce((a, b) => a + b, 0) / ks.length;
      O.nilai[q.id] = r >= 1 ? "bisa" : r > 0 ? "ragu" : "belum";
    }
    delete O.sesi;
    saveLater("progres", 100);
    const lemah = p.soal.filter((q) => O.nilai[q.id] && O.nilai[q.id] !== "bisa");
    v.innerHTML = `<div class="page"><div class="q-card q-end enter os-akhir">
      <div class="end-ring ring" style="--p:${pct}" data-label="${pct}%"></div>
      <h2>${pct >= 70 ? `Hebat, ${esc(sapaan())}!` : pct >= 40 ? "Sudah di jalur yang benar." : "Ini baru awal. Ulangi lewat pembahasan bertahap."}</h2>
      <div class="end-stats"><div><b>${skor.toLocaleString("id-ID")}</b><small>dari ${maks} poin</small></div><div><b>${osFmtWaktu((s.selesai - s.mulai) / 1000)}</b><small>waktu</small></div><div><b>${lemah.length}</b><small>soal perlu diulang</small></div></div>
      ${lemah.length ? `<div class="review"><h3>Ulangi dengan pembahasan bertahap</h3><div class="card os-list">${lemah.map((q) => osSoalRow([q, p], false)).join("")}</div></div>` : ""}
      <div class="end-acts"><a class="btn" href="#/osits">OSITS Fisika</a><a class="btn primary" href="#/osits/paket/${esc(p.id)}">Lihat paket</a></div></div></div>`;
    if (pct >= 80 && typeof confetti === "function") confetti();
  }

  v.addEventListener("click", async (e) => {
    const t = e.target;
    if (t.closest("#osMulai")) { O.sesi = { paket: p.id, mulai: Date.now(), mulaiSoal: Date.now(), i: 0 }; simpan(); berjalan(); return; }
    if (t.closest("#osKumpul") || t.closest("#osKumpul2")) {
      if (urut) { lanjutUrut(false); return; }
      if (await confirmDialog("Kumpulkan sekarang?", `Sisa waktu masih berjalan. Setelah dikumpulkan kamu langsung menilai jawaban.`, "Kumpulkan")) kumpul();
      return;
    }
    if (t.closest("#osBatal")) { if (await confirmDialog("Batalkan simulasi?", "Waktu dan jawaban sesi ini tidak disimpan.", "Batalkan")) { delete O.sesi; simpan(); intro(); } return; }
    if (t.closest("#osBuang")) { if (await confirmDialog("Buang hasil?", "Penilaian sesi ini tidak disimpan.", "Buang")) { delete O.sesi; simpan(); intro(); } return; }
    if (t.closest("#osSimpan")) {
      const s = sesi(), nBag = p.soal.reduce((a, q) => a + q.bagian.length, 0);
      if (Object.keys(s.skor).length < nBag && !(await confirmDialog("Masih ada yang belum dinilai", "Bagian yang belum dinilai dihitung 0 poin. Tetap simpan?", "Simpan"))) return;
      selesai(); return;
    }
    const sk = t.closest("[data-sk] button");
    if (sk) {
      const s = sesi(), key = sk.parentElement.dataset.sk;
      s.skor[key] = +sk.dataset.v; simpan();
      $$("button", sk.parentElement).forEach((b) => b.classList.toggle("on", b === sk));
      $("#osSkor", v).textContent = skorTotal().toLocaleString("id-ID");
      $("#osDinilai", v).textContent = Object.keys(s.skor).length;
    }
  });

  const s = sesi();
  if (!s) intro();
  else if (s.selesai) penilaian();
  else if (!urut && Date.now() >= s.mulai + p.waktu * 60000) kumpul();
  else if (urut && Date.now() >= s.mulaiSoal + p.soal[s.i].menit * 60000) lanjutUrut(true);
  else berjalan();
});
