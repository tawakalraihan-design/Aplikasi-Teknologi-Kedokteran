"use strict";

/* =========================================================
   PROYEK HANDS-ON: tiap alat dipecah jadi proyek kecil per
   komponen, dari sensor (elektrikal) → data (informatika) →
   antarmuka/casing (desain).
   ========================================================= */

const PSTATUS = { belum: "Belum mulai", jalan: "Sedang dikerjakan", selesai: "Selesai" };
const rupiah = (n) => (n ? "Rp" + Math.round(n).toLocaleString("id-ID") : "sudah ada / pinjam");
const proyekById = (id) => byId(S.proyek, id);
const proyekAlat = (aid) => S.proyek.filter((p) => p.alat === aid).sort((x, y) => x.tahap - y.tahap);
const proyekStatus = (id) => (S.progres.proyek || {})[id] || "belum";
const proyekBiaya = (p) => (p.bahan || []).reduce((s, b) => s + (+b[1] || 0), 0);
const proyekPakaiMateri = (mid) => S.proyek.filter((p) => (p.materi || []).includes(mid));
function setProyekStatus(id, st) { S.progres.proyek = S.progres.proyek || {}; S.progres.proyek[id] = st; saveLater("progres", 300); }

function proyekStep(p, i, denganAlat) {
  const st = proyekStatus(p.id);
  const a = denganAlat === true ? alatById(p.alat) : null;
  return `<a class="pstep s-${st}" href="#/proyek/${esc(p.id)}" style="--i:${i}">
    <span class="pnum">${st === "selesai" ? "✓" : p.tahap}</span>
    <div><b>${esc(p.judul)}</b><small>${a ? esc(a.singkatan || a.nama) + " · " : ""}${esc(p.level)} · ${esc(p.durasi)} · ${rupiah(proyekBiaya(p))}</small>
      <div class="bd-row">${(p.bidang || []).map((b) => BIDANG[b] ? bidangChip(b) : "").join("")}</div></div></a>`;
}

function proyekTrack(a) {
  const ps = proyekAlat(a.id);
  if (!ps.length) return "";
  const done = ps.filter((p) => proyekStatus(p.id) === "selesai").length;
  return `<section class="card panel">
    <div class="section-head"><div><h2>Proyek hands-on</h2><span class="sub">Bangun prototipe ${esc(a.singkatan || a.nama)} sedikit demi sedikit: ${ps.length} proyek kecil, ${done} selesai. Mulai dari tahap 1.</span></div>
      <div class="right"><a class="btn sm" href="#/proyek?alat=${esc(a.id)}">Semua proyek</a></div></div>
    <div class="ptrack">${ps.map(proyekStep).join("")}</div></section>`;
}

route(/^proyek(?:\?alat=([^/&]+))?$/, (v, fAlat) => {
  ui.proyekBidang = ui.proyekBidang || "Semua";
  ui.proyekLevel = ui.proyekLevel || "Semua";
  const draw = () => {
    const ok = (p) => (ui.proyekBidang === "Semua" || (p.bidang || []).includes(ui.proyekBidang)) && (ui.proyekLevel === "Semua" || p.level === ui.proyekLevel);
    const alatList = S.alat.filter((a) => (!fAlat || a.id === fAlat) && proyekAlat(a.id).some(ok));
    const total = S.proyek.length, done = S.proyek.filter((p) => proyekStatus(p.id) === "selesai").length, jalan = S.proyek.filter((p) => proyekStatus(p.id) === "jalan");
    v.innerHTML = `<div class="page">
      <div class="section-head"><div><h1>Proyek Hands-on</h1><span class="sub">Tiap alat dipecah jadi proyek kecil per komponen. Bahan bisa dicari di marketplace; harga adalah perkiraan.</span></div>
        <div class="right"><div class="mini-stats"><span><b>${done}</b> selesai</span><span><b>${jalan.length}</b> berjalan</span><span><b>${total}</b> proyek</span></div></div></div>
      ${jalan.length ? `<section class="card panel"><h3>Sedang kamu kerjakan</h3><div class="ptrack">${jalan.map((p, i) => proyekStep(p, i, true)).join("")}</div></section>` : ""}
      <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
        <div class="seg">${["Semua", ...BIDANG_URUT.filter((b) => b !== "Dasar")].map((b) => `<button data-pb="${b}" class="${ui.proyekBidang === b ? "on" : ""}">${b === "Semua" ? "Semua bidang" : `<span class="dot" style="background:${BIDANG[b].warna}"></span>${b}`}</button>`).join("")}</div>
        <div class="seg">${["Semua", "Pemula", "Menengah", "Lanjut"].map((l) => `<button data-pl="${l}" class="${ui.proyekLevel === l ? "on" : ""}">${l === "Semua" ? "Semua level" : l}</button>`).join("")}</div>
        ${fAlat ? `<a class="chip outline" href="#/proyek">Tampilkan semua alat ✕</a>` : ""}
      </div>
      <div class="ptrack-list stagger">${alatList.map((a, i) => { const ps = proyekAlat(a.id).filter(ok); return `<section class="card ptrack-card" style="--i:${i}">
        <a class="ptrack-alat" href="#/alat/${esc(a.id)}"><div class="mini-ilus">${gambarAlat(a)}</div><div><b>${esc(a.nama)}</b><small>${esc(a.kategori)} · ${ps.length} proyek · total ±${rupiah(ps.reduce((s, p) => s + proyekBiaya(p), 0))}</small></div></a>
        <div class="ptrack">${ps.map(proyekStep).join("")}</div></section>`; }).join("") || `<div class="empty">Tidak ada proyek yang cocok dengan filter.</div>`}</div>
    </div>`;
  };
  v.addEventListener("click", (e) => {
    const b = e.target.closest("[data-pb]"); if (b) { ui.proyekBidang = b.dataset.pb; draw(); }
    const l = e.target.closest("[data-pl]"); if (l) { ui.proyekLevel = l.dataset.pl; draw(); }
  });
  draw();
});

route(/^proyek\/([^/]+)$/, (v, id) => {
  const p = proyekById(id);
  if (!p) { v.innerHTML = `<div class="page"><div class="empty">Proyek tidak ditemukan. <a href="#/proyek">Kembali</a></div></div>`; return; }
  const a = alatById(p.alat) || { nama: p.alat, blok: [] };
  const seri = proyekAlat(p.alat), idx = seri.indexOf(p);
  const prev = seri[idx - 1], next = seri[idx + 1];
  const blokNama = (bid) => byId(a.blok || [], bid)?.nama || bid;
  const langkahKey = (i) => p.id + "|" + i;
  S.progres.proyekLangkah = S.progres.proyekLangkah || {};
  const seg = () => `<div class="seg" id="pSeg">${Object.entries(PSTATUS).map(([k, l]) => `<button data-ps="${k}" class="${proyekStatus(p.id) === k ? "on" : ""}">${l}</button>`).join("")}</div>`;
  v.innerHTML = `<div class="page">
    <div class="breadcrumb"><a href="#/proyek">Proyek</a><span>/</span><a href="#/alat/${esc(a.id || "")}">${esc(a.nama)}</a><span>/</span><span style="color:var(--text)">Tahap ${p.tahap}</span></div>
    <section class="card detail-head" style="--thumb-grad:${gradOf(a.kategori)}">
      <div class="mini-ilus lg">${a.id ? gambarAlat(a) : ""}</div>
      <div class="info">
        <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><span class="chip dark">Tahap ${p.tahap} dari ${seri.length}</span><span class="chip outline">${esc(p.level)}</span><span class="chip outline">${esc(p.durasi)}</span>${(p.bidang || []).map((b) => BIDANG[b] ? bidangChip(b) : "").join("")}</div>
        <h1>${esc(p.judul)}</h1>
        <p>${esc(p.tujuan)}</p>
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap">${seg()}</div>
      </div>
    </section>
    <div class="detail-grid">
      <div class="section">
        <section class="card panel"><h2>Langkah kerja</h2><p class="muted" style="font-size:.88rem">Centang langkah yang sudah selesai.</p>
          <div class="sub-list">${(p.langkah || []).map((l, i) => `<button class="sub-check${S.progres.proyekLangkah[langkahKey(i)] ? " on" : ""}" data-lk="${i}"><span class="box"></span><span class="no">${i + 1}</span><span class="sname">${esc(l)}</span></button>`).join("")}</div>
          ${p.hasil ? `<div class="hasil">${ico("send", 16)} <span><b>Hasil akhir:</b> ${esc(p.hasil)}</span></div>` : ""}
        </section>
        <section class="card panel"><h2>Bahan dan perkiraan biaya</h2>
          <table class="list-table bahan"><tbody>${(p.bahan || []).map((b) => `<tr><td>${esc(b[0])}</td><td class="num">${rupiah(+b[1])}</td></tr>`).join("")}
            <tr class="tot"><td>Total perkiraan</td><td class="num">${rupiah(proyekBiaya(p))}</td></tr></tbody></table>
          <p class="muted" style="font-size:.82rem;margin-top:8px">Harga perkiraan marketplace Indonesia (Tokopedia/Shopee) akhir 2026. Cek ulang sebelum membeli; alat lab seperti osiloskop dan multimeter bisa dipinjam dari laboratorium kampus.</p>
        </section>
        <section class="card panel"><h2>Mata kuliah yang kamu pakai</h2>
          <div class="used-grid">${(p.materi || []).map((mid) => { const m = materiById(mid); if (!m) return ""; const b = bidangOf(m); return `<a class="card used-card" href="#/materi/${esc(m.id)}"><div class="alat-ico" style="color:${BIDANG[b].warna}">${ico("materi", 22)}</div><div><b>${esc(m.nama)}</b><p>${esc(semLabel(m))} · ${b}</p></div></a>`; }).join("")}</div>
          ${(p.blok || []).length ? `<h3 style="margin-top:14px">Komponen ${esc(a.singkatan || a.nama)} yang dibangun</h3><div class="chips">${p.blok.map((b) => `<span class="chip">${esc(blokNama(b))}</span>`).join("")}</div>` : ""}
        </section>
      </div>
      <aside class="detail-side">
        ${p.keselamatan ? `<section class="card panel warn"><h3>${ico("shield", 18)} Keselamatan</h3><p class="txt">${esc(p.keselamatan)}</p></section>` : ""}
        ${(p.referensi || []).length ? `<section class="card panel"><h3>Referensi proyek</h3><ul class="ref-list">${p.referensi.map((r) => `<li>${refHtml(r)}</li>`).join("")}</ul></section>` : ""}
        <section class="card panel"><h3>Catatan proyek</h3><textarea class="notes" id="pNotes" placeholder="Hasil uji, kendala, foto rangkaian, link kode…">${esc((S.progres.proyekCatatan || {})[p.id] || "")}</textarea><span class="muted" style="font-size:.8rem">Tersimpan otomatis.</span></section>
        <div class="pnav">${prev ? `<a class="btn" href="#/proyek/${esc(prev.id)}">← Tahap ${prev.tahap}</a>` : "<span></span>"}${next ? `<a class="btn primary" href="#/proyek/${esc(next.id)}">Tahap ${next.tahap} →</a>` : ""}</div>
      </aside>
    </div>
  </div>`;
  v.addEventListener("click", (e) => {
    const s = e.target.closest("[data-ps]");
    if (s) { setProyekStatus(p.id, s.dataset.ps); $("#pSeg", v).outerHTML = seg(); if (s.dataset.ps === "selesai") confetti(); return; }
    const l = e.target.closest("[data-lk]");
    if (l) {
      const k = langkahKey(l.dataset.lk);
      if (S.progres.proyekLangkah[k]) delete S.progres.proyekLangkah[k]; else S.progres.proyekLangkah[k] = true;
      l.classList.toggle("on", !!S.progres.proyekLangkah[k]);
      const n = (p.langkah || []).filter((_, i) => S.progres.proyekLangkah[langkahKey(i)]).length;
      const st = n === 0 ? "belum" : n === p.langkah.length ? "selesai" : "jalan";
      if (st !== proyekStatus(p.id)) { setProyekStatus(p.id, st); $("#pSeg", v).outerHTML = seg(); if (st === "selesai") confetti(); }
      saveLater("progres", 300);
    }
  });
  $("#pNotes", v).addEventListener("input", (e) => { S.progres.proyekCatatan = S.progres.proyekCatatan || {}; S.progres.proyekCatatan[p.id] = e.target.value; saveLater("progres", 800); });
});

/* ---------- konfeti kecil (tanpa pustaka) ---------- */
function confetti() {
  if (reduceMotion()) return;
  const wrap = document.createElement("div");
  wrap.className = "confetti";
  const cols = ["#82bcff", "#2483ff", "#ff66f4", "#ff3029", "#fe7b02", "#1f9d55"];
  wrap.innerHTML = Array.from({ length: 70 }, () => `<i style="--x:${Math.random() * 100}vw;--d:${0.9 + Math.random() * 1.4}s;--r:${Math.random() * 720 - 360}deg;--s:${Math.random() * 0.4}s;background:${cols[(Math.random() * cols.length) | 0]}"></i>`).join("");
  document.body.appendChild(wrap);
  setTimeout(() => wrap.remove(), 2600);
}
