"use strict";

/* =========================================================
   STUDI LANJUTAN: Health Technology Assessment, Health
   Economics, Public Health. Modul + alat interaktif kecil.
   ========================================================= */

const lanjutanById = (id) => byId(S.lanjutan, id);
const LGRAD = { hta: "linear-gradient(135deg,#82bcff,#ff66f4)", he: "linear-gradient(135deg,#fe7b02,#ff66f4)", ph: "linear-gradient(135deg,#1f9d55,#82bcff)" };
const modDone = (id) => !!(S.progres.lanjutan || {})[id];

const HTA_DOMAIN = [
  ["masalah", "Masalah kesehatan", "Penyakit/kondisi apa yang ditangani? Seberapa besar bebannya di Indonesia (prevalensi, kematian)?"],
  ["teknis", "Karakteristik teknis", "Apa komponen utamanya, bagaimana cara kerja, apa kebutuhan listrik, pemeliharaan, dan pelatihannya?"],
  ["aman", "Keamanan", "Apa risiko bagi pasien dan operator (listrik, radiasi, infeksi)? Standar apa yang harus dipenuhi?"],
  ["efektif", "Efektivitas klinis", "Bukti apa yang menunjukkan hasil pasien membaik? Akurasi diagnostiknya (sensitivitas/spesifisitas)?"],
  ["biaya", "Biaya dan ekonomi", "Berapa harga beli, biaya per pemeriksaan, dan apakah efektif-biaya dibanding praktik saat ini?"],
  ["etis", "Etika", "Siapa yang diuntungkan atau dirugikan? Apakah aksesnya adil?"],
  ["organisasi", "Organisasi", "Apa yang berubah pada alur kerja, ruangan, SDM, dan rujukan?"],
  ["sosial", "Pasien dan sosial", "Bagaimana pengalaman pasien dan keluarga? Hambatan budaya atau ekonomi?"],
  ["hukum", "Hukum dan regulasi", "Izin edar (AKL/AKD), standar, kalibrasi, perlindungan data."],
];

function htaTool(v) {
  S.progres.hta = S.progres.hta || {};
  const pick = ui.htaAlat || S.alat[0]?.id;
  const draw = () => {
    const a = alatById(ui.htaAlat || pick);
    const d = S.progres.hta[a.id] = S.progres.hta[a.id] || {};
    const isi = HTA_DOMAIN.filter(([k]) => (d[k] || "").trim()).length;
    $("#tool", v).innerHTML = `<div class="section-head"><div><h2>Latihan HTA sebuah alat</h2><span class="sub">Pilih alat, lalu isi kesembilan domain HTA Core Model. Tersimpan otomatis.</span></div>
      <div class="right"><select class="sel" id="htaAlat">${S.alat.map((x) => `<option value="${esc(x.id)}" ${x.id === a.id ? "selected" : ""}>${esc(x.ikon)} ${esc(x.nama)}</option>`).join("")}</select></div></div>
      <div class="hta-meter"><div class="bar"><i style="width:${(isi / 9) * 100}%"></i></div><span>${isi}/9 domain terisi</span></div>
      <div class="hta-grid">${HTA_DOMAIN.map(([k, l, q], i) => `<div class="hta-dom" style="--i:${i}"><div class="hd"><span class="num">${i + 1}</span><b>${l}</b></div><p>${q}</p>
        ${k === "teknis" ? `<p class="hint-auto">Dari aplikasi: ${esc((a.blok || []).map((b) => b.nama).join(" → "))}.</p>` : ""}
        ${k === "aman" && a.keselamatan ? `<p class="hint-auto">Dari aplikasi: ${esc(a.keselamatan)}</p>` : ""}
        <textarea data-dom="${k}" rows="3" placeholder="Tulis jawabanmu…">${esc(d[k] || "")}</textarea></div>`).join("")}</div>`;
    $("#htaAlat", v).onchange = (e) => { ui.htaAlat = e.target.value; draw(); };
  };
  v.addEventListener("input", (e) => {
    const t = e.target.closest("[data-dom]"); if (!t) return;
    const a = alatById(ui.htaAlat || pick);
    S.progres.hta[a.id][t.dataset.dom] = t.value; saveLater("progres", 800);
    const isi = HTA_DOMAIN.filter(([k]) => (S.progres.hta[a.id][k] || "").trim()).length;
    $(".hta-meter i", v).style.width = (isi / 9) * 100 + "%"; $(".hta-meter span", v).textContent = `${isi}/9 domain terisi`;
  });
  draw();
}

function icerTool(v) {
  const st = ui.icer = ui.icer || { c0: 20000000, c1: 50000000, e0: 4.2, e1: 4.8, wtp: 75000000 };
  const fmt = (n) => Math.round(n).toLocaleString("id-ID");
  const draw = () => {
    const dC = st.c1 - st.c0, dE = st.e1 - st.e0;
    const icer = dE !== 0 ? dC / dE : Infinity;
    let verdict, cls;
    if (dE >= 0 && dC <= 0) { verdict = "Dominan: lebih murah dan lebih efektif. Adopsi."; cls = "ok"; }
    else if (dE <= 0 && dC >= 0) { verdict = "Didominasi: lebih mahal dan tidak lebih efektif. Tolak."; cls = "bad"; }
    else if (dE > 0) { verdict = icer <= st.wtp ? `Efektif-biaya: ICER Rp${fmt(icer)}/QALY ≤ ambang Rp${fmt(st.wtp)}.` : `Belum efektif-biaya: ICER Rp${fmt(icer)}/QALY > ambang Rp${fmt(st.wtp)}.`; cls = icer <= st.wtp ? "ok" : "bad"; }
    else { verdict = `Lebih murah tapi kurang efektif: hemat Rp${fmt(-icer)} per QALY yang hilang. Pertimbangkan ambang.`; cls = "warn"; }
    // Bidang efektivitas biaya
    const W = 300, H = 220, cx = W / 2, cy = H / 2;
    const sx = Math.max(Math.abs(dE), 0.1) * 1.4, sy = Math.max(Math.abs(dC), Math.abs(st.wtp * sx), 1) * 1.1;
    const px = cx + (dE / sx) * (W / 2), py = cy - (dC / sy) * (H / 2);
    const tx = cx + W / 2, ty = cy - ((st.wtp * sx) / sy) * (H / 2);
    $("#tool", v).innerHTML = `<div class="section-head"><div><h2>Kalkulator ICER</h2><span class="sub">Bandingkan alat/intervensi baru dengan praktik saat ini. Isi biaya per pasien (Rp) dan QALY per pasien.</span></div></div>
      <div class="icer">
        <div class="icer-in">
          <div class="form-row">${["c0:Biaya praktik saat ini (Rp)", "c1:Biaya alat baru (Rp)"].map((x) => { const [k, l] = x.split(":"); return `<div class="field"><label>${l}</label><input type="number" data-ic="${k}" value="${st[k]}"></div>`; }).join("")}</div>
          <div class="form-row">${["e0:QALY praktik saat ini", "e1:QALY alat baru"].map((x) => { const [k, l] = x.split(":"); return `<div class="field"><label>${l}</label><input type="number" step="0.01" data-ic="${k}" value="${st[k]}"></div>`; }).join("")}</div>
          <div class="field"><label>Ambang willingness-to-pay per QALY (Rp)</label><input type="number" data-ic="wtp" value="${st.wtp}"><span class="hint">Contoh: ±1× PDB per kapita Indonesia. Ambang resmi bisa berbeda; lihat pedoman HTA Indonesia.</span></div>
          <div class="icer-out">
            <div><small>ΔBiaya</small><b>Rp${fmt(dC)}</b></div><div><small>ΔQALY</small><b>${dE.toFixed(2)}</b></div><div><small>ICER</small><b>${isFinite(icer) ? "Rp" + fmt(icer) : "–"}</b></div>
          </div>
          <div class="verdict ${cls}">${verdict}</div>
        </div>
        <svg class="ceplane" viewBox="0 0 ${W} ${H}">
          <rect x="0" y="0" width="${W}" height="${H}" rx="12" class="ce-bg"/>
          <path class="ce-ax" d="M0 ${cy}H${W}M${cx} 0V${H}"/>
          <path class="ce-wtp" d="M${W - tx} ${H - ty}L${tx} ${ty}"/>
          <text x="${W - 8}" y="14" text-anchor="end" class="ce-t">lebih mahal</text><text x="${W - 8}" y="${H - 8}" text-anchor="end" class="ce-t">lebih efektif →</text>
          <text x="8" y="${H - 8}" class="ce-t">lebih murah</text>
          <circle cx="${Math.min(W - 8, Math.max(8, px))}" cy="${Math.min(H - 8, Math.max(8, py))}" r="8" class="ce-pt ${cls}"/>
        </svg>
      </div>`;
  };
  v.addEventListener("change", (e) => { const t = e.target.closest("[data-ic]"); if (!t) return; st[t.dataset.ic] = +t.value || 0; draw(); });
  draw();
}

function diagTool(v) {
  const st = ui.diag = ui.diag || { se: 90, sp: 90, prev: 5 };
  $("#tool", v).innerHTML = `<div class="section-head"><div><h2>Simulator akurasi alat diagnostik</h2><span class="sub">Geser prevalensi dan lihat bagaimana nilai prediktif positif (PPV) berubah walau alatnya sama.</span></div></div>
    <div class="diag"><div class="diag-in">
      ${[["se", "Sensitivitas", 50, 100], ["sp", "Spesifisitas", 50, 100], ["prev", "Prevalensi di populasi", 0.5, 50]].map(([k, l, mn, mx]) => `<div class="field"><label>${l}: <b data-dv="${k}">${st[k]}%</b></label><input type="range" min="${mn}" max="${mx}" step="0.5" value="${st[k]}" data-dg="${k}"></div>`).join("")}
      <div id="diagOut"></div></div><div class="people" id="people"></div></div>`;
  const drawOut = () => {
    const N = 1000, sakit = Math.round(N * st.prev / 100), sehat = N - sakit;
    const TP = Math.round(sakit * st.se / 100), FN = sakit - TP, TN = Math.round(sehat * st.sp / 100), FP = sehat - TN;
    const ppv = TP + FP ? (TP / (TP + FP)) * 100 : 0, npv = TN + FN ? (TN / (TN + FN)) * 100 : 0;
    // 100 ikon orang; 1 ikon ≈ 10 orang, dibulatkan
    const icons = [];
    const s100 = (x) => Math.round(x / 10);
    [["tp", s100(TP)], ["fn", s100(FN)], ["fp", s100(FP)]].forEach(([c, n]) => { for (let i = 0; i < n; i++) icons.push(c); });
    while (icons.length < 100) icons.push("tn");
    icons.length = 100;
    $("#diagOut", v).innerHTML = `<table class="t22"><tr><th></th><th>Sakit</th><th>Sehat</th></tr><tr><th>Tes +</th><td class="tp">${TP}</td><td class="fp">${FP}</td></tr><tr><th>Tes −</th><td class="fn">${FN}</td><td class="tn">${TN}</td></tr></table>
      <div class="icer-out"><div><small>PPV</small><b>${ppv.toFixed(1)}%</b></div><div><small>NPV</small><b>${npv.toFixed(1)}%</b></div><div><small>Positif palsu</small><b>${FP}</b></div></div>
      <p class="muted" style="font-size:.86rem">Dari ${N} orang, ${TP + FP} dites positif dan hanya ${TP} yang benar sakit. ${ppv < 50 ? "Di populasi berprevalensi rendah, sebagian besar hasil positif ternyata palsu, jadi perlu tes konfirmasi." : "Prevalensi cukup tinggi sehingga hasil positif lebih bisa dipercaya."}</p>`;
    $("#people", v).innerHTML = icons.map((c) => `<span class="pp ${c}"></span>`).join("") +
      `<div class="pp-leg"><span><i class="pp tp"></i>Positif benar</span><span><i class="pp fp"></i>Positif palsu</span><span><i class="pp fn"></i>Negatif palsu</span><span><i class="pp tn"></i>Negatif benar</span><span class="muted">1 ikon ≈ 10 orang</span></div>`;
  };
  v.addEventListener("input", (e) => { const t = e.target.closest("[data-dg]"); if (!t) return; st[t.dataset.dg] = +t.value; $(`[data-dv="${t.dataset.dg}"]`, v).textContent = t.value + "%"; drawOut(); });
  drawOut();
}

route(/^lanjutan\/([^/]+)$/, (v, id) => {
  const L = lanjutanById(id);
  if (!L) { v.innerHTML = `<div class="page"><div class="empty">Materi tidak ditemukan.</div></div>`; return; }
  S.progres.lanjutan = S.progres.lanjutan || {};
  const nSoal = (S.soal || []).filter((s) => s.alat === L.id).length;
  const prog = () => { const n = L.modul.filter((m) => modDone(m.id)).length; return [n, L.modul.length]; };
  const [n0, t0] = prog();
  v.innerHTML = `<div class="page">
    <div class="breadcrumb"><span>Studi Lanjutan</span><span>/</span><span style="color:var(--text)">${esc(L.nama)}</span></div>
    <section class="card detail-head lan-head" style="--thumb-grad:${LGRAD[L.id] || gradOf("")}">
      <div class="alat-ico">${esc(L.ikon || "📘")}</div>
      <div class="info">
        <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><h1>${esc(L.nama)}</h1><span class="chip dark">${esc(L.singkat)}</span><span class="chip outline">Materi tambahan sekolah lanjut</span></div>
        <p>${esc(L.ringkasan)}</p>
        <div id="lanProg" class="lan-prog"><div class="bar"><i style="width:${(n0 / t0) * 100}%"></i></div><span>${n0} dari ${t0} modul dipelajari</span></div>
      </div>
      <div class="ready"><a class="btn primary" href="#/latihan/topik/${esc(L.id)}">${ico("latihan", 18)} Latihan ${nSoal} soal</a></div>
    </section>
    <section class="card panel kaitan"><h3>Kaitan dengan Teknologi Kedokteran</h3><p class="txt">${esc(L.kaitan)}</p></section>
    <div class="detail-grid">
      <div class="section">
        <div class="modul-list stagger">${L.modul.map((m, i) => `<details class="card modul" style="--i:${i}" ${i === 0 ? "open" : ""}>
          <summary><span class="mnum">${i + 1}</span><b>${esc(m.judul)}</b><button class="mdone${modDone(m.id) ? " on" : ""}" data-md="${esc(m.id)}" title="Tandai sudah dipelajari"><span class="box"></span>Sudah</button></summary>
          <ul class="poin">${m.poin.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>
          ${(m.alat || []).length ? `<div class="chips"><span class="muted" style="font-size:.84rem">Contoh alat:</span>${m.alat.map((aid) => { const a = alatById(aid); return a ? `<a class="chip" href="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</a>` : ""; }).join("")}</div>` : ""}
        </details>`).join("")}</div>
        <section class="card panel" id="tool"></section>
      </div>
      <aside class="detail-side">
        <section class="card panel"><h3>Referensi</h3><ul class="ref-list">${(L.referensi || []).map((r) => `<li>${refHtml(r)}</li>`).join("")}</ul></section>
        <section class="card panel"><h3>Catatan</h3><textarea class="notes" id="lNotes" placeholder="Ringkasan bacaan, ide tesis…">${esc((S.progres.lanjutanCatatan || {})[L.id] || "")}</textarea><span class="muted" style="font-size:.8rem">Tersimpan otomatis.</span></section>
      </aside>
    </div>
  </div>`;
  v.addEventListener("click", (e) => {
    const b = e.target.closest("[data-md]"); if (!b) return;
    e.preventDefault(); e.stopPropagation();
    const k = b.dataset.md;
    if (S.progres.lanjutan[k]) delete S.progres.lanjutan[k]; else S.progres.lanjutan[k] = true;
    b.classList.toggle("on", !!S.progres.lanjutan[k]);
    const [n, t] = prog();
    $("#lanProg", v).innerHTML = `<div class="bar"><i style="width:${(n / t) * 100}%"></i></div><span>${n} dari ${t} modul dipelajari</span>`;
    if (n === t) confetti();
    saveLater("progres", 300);
  });
  $("#lNotes", v).addEventListener("input", (e) => { S.progres.lanjutanCatatan = S.progres.lanjutanCatatan || {}; S.progres.lanjutanCatatan[L.id] = e.target.value; saveLater("progres", 800); });
  ({ hta: htaTool, icer: icerTool, diagnostik: diagTool })[L.alatInteraktif]?.(v);
});
