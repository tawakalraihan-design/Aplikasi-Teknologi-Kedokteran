"use strict";

/* =========================================================
   v1.4
   - Kisah Deep Learning: kode Oralytic diceritakan bab demi bab
     dengan pola "Deep learning adalah… / Jika kita ingin membentuk… /
     Bayangkan jika Anda ingin membuat program… / seperti membuat kue…".
   - Pustaka: 12 buku di folder Referensi, dengan ringkasan per bab
     dan kaitan ke alat serta mata kuliah.
   ========================================================= */

const kisahById = (id) => (S.kisah || []).find((k) => k.id === id);
const pustakaList = () => S.referensi.filter((r) => r.jenis === "pustaka" && Array.isArray(r.bab));
const kisahDone = (kid, bid) => !!(((S.progres.kisah || {})[kid] || {})[bid]);
const kisahN = (k) => k.bab.filter((b) => kisahDone(k.id, b.id)).length;
const babDibaca = (pid, no) => !!(((S.progres.pustaka || {})[pid] || {})[no]);
const POLA = [
  ["adalah", "bulb", "Deep learning adalah", "#2483ff"],
  ["bentuk", "proyek", "Jika kita ingin membentuk ini", "#ff66f4"],
  ["bayangkan", "materi", "Bayangkan programnya", "#1f9d55"],
  ["kue", "kue", "Seperti membuat kue", "#fe7b02"],
];
const fmtHal = (h) => (h && h.length ? `hal. ${h[0]}–${h[1]}` : "");

function toggleProgres(grup, a, b) {
  const G = (S.progres[grup] = S.progres[grup] || {});
  const X = (G[a] = G[a] || {});
  if (X[b]) delete X[b]; else X[b] = true;
  saveLater("progres", 300);
  return !!X[b];
}

/* ---------- panel di halaman alat dan mata kuliah ---------- */
// Bab buku Referensi yang membahas alat/mata kuliah ini.
function bacaanHtml(cocok, judulLuas) {
  const hasil = [];
  for (const r of pustakaList()) for (const b of r.bab) if (cocok(b)) hasil.push([r, b]);
  if (!hasil.length) return "";
  return `<section class="card panel"><h3>${ico("materi", 18)} Bacaan dari buku Referensi</h3>
    <p class="muted" style="font-size:.84rem">${hasil.length} bab dari folder Referensi membahas ${esc(judulLuas)}.</p>
    <ul class="bacaan-list">${hasil.slice(0, 8).map(([r, b]) => `<li><a href="#/pustaka/${esc(r.id)}?bab=${b.no}"><b>${esc(b.judul)}</b><small>${esc(r.singkat || r.judul)} · bab ${b.no} · ${fmtHal(b.hal)}</small></a>${babDibaca(r.id, b.no) ? `<span class="bc-ok" title="Sudah dibaca">${ico("check", 14)}</span>` : ""}</li>`).join("")}</ul>
    ${hasil.length > 8 ? `<span class="muted" style="font-size:.8rem">dan ${hasil.length - 8} bab lain di halaman Referensi.</span>` : ""}</section>`;
}
// Bab Kisah Deep Learning yang memakai mata kuliah ini, atau kisah milik alat ini.
function kisahPanelHtml(opt) {
  const out = [];
  for (const k of S.kisah || []) {
    const bab = opt.materi ? k.bab.filter((b) => (b.materi || []).includes(opt.materi)) : opt.alat === k.alat ? k.bab : [];
    if (bab.length) out.push([k, bab]);
  }
  if (!out.length) return "";
  return out.map(([k, bab]) => `<section class="card panel kisah-mini"><h3>${esc(k.ikon || "📖")} ${esc(k.singkat)}</h3>
    <p class="muted" style="font-size:.84rem">${opt.materi ? `${bab.length} bab kisah memakai mata kuliah ini.` : `Kode alat ini diceritakan dalam ${bab.length} bab.`}</p>
    <div class="km-bab">${bab.slice(0, 6).map((b) => `<a class="chip outline${kisahDone(k.id, b.id) ? " on" : ""}" href="#/kisah/${esc(k.id)}/${esc(b.id)}">${kisahDone(k.id, b.id) ? ico("check", 12) : ""}${esc(b.judul.split(":")[0])}</a>`).join("")}</div>
    <a class="btn sm" href="#/kisah/${esc(k.id)}">${ico("arrow", 14)} Buka kisah</a></section>`).join("");
}

/* =========================================================
   KISAH
   ========================================================= */
route(/^kisah$/, (v) => {
  const ks = S.kisah || [];
  if (ks.length === 1) { location.replace("#/kisah/" + ks[0].id); return; }
  v.innerHTML = `<div class="page"><div class="section-head"><div><h1>Kisah</h1><span class="sub">Cerita belajar dari kode proyek sendiri.</span></div></div>
    ${ks.length ? `<div class="mode-grid">${ks.map((k) => `<a class="card mode-card" href="#/kisah/${esc(k.id)}"><span class="mode-ico">${esc(k.ikon || "📖")}</span><b>${esc(k.judul)}</b><p>${kisahN(k)}/${k.bab.length} bab dibaca</p></a>`).join("")}</div>` : `<div class="empty">Belum ada kisah.</div>`}</div>`;
});

route(/^kisah\/([^/]+)$/, (v, kid) => {
  const k = kisahById(kid);
  if (!k) { location.hash = "#/kisah"; return; }
  const n = kisahN(k), pct = Math.round((n / k.bab.length) * 100);
  const nSoal = (S.soal || []).filter((s) => s.kisah === k.id).length;
  const lanjut = k.bab.find((b) => !kisahDone(k.id, b.id)) || k.bab[0];
  const tahap = [...new Set(k.bab.map((b) => b.tahap))];
  const al = alatById(k.alat);
  v.innerHTML = `<div class="page">
    <section class="kisah-hero card">
      <div class="kh-main">
        <span class="hero-badge"><i></i>Dari folder <code>${esc(k.sumber.split("\\").slice(-1)[0])}</code></span>
        <h1>${esc(k.judul)}</h1>
        <p class="lead">${esc(k.ringkasan)}</p>
        <div class="kh-act"><a class="btn primary" href="#/kisah/${esc(k.id)}/${esc(lanjut.id)}">${ico("play", 16)} ${n ? "Lanjut membaca" : "Mulai membaca"}</a>
          ${nSoal ? `<a class="btn" href="#/latihan/kisah/${esc(k.id)}">${ico("latihan", 16)} Latihan ${nSoal} soal</a>` : ""}
          ${al ? `<a class="btn" href="#/alat/${esc(al.id)}">${esc(al.ikon)} Lihat breakdown ${esc(al.singkatan)}</a>` : ""}</div>
      </div>
      <div class="kh-ring"><div class="ring" style="--p:${pct}" data-label="${pct}%"></div><small>${n} dari ${k.bab.length} bab</small></div>
    </section>

    <section class="card panel">
      <div class="section-head"><div><h2>Cara membaca setiap bab</h2><span class="sub">Setiap bab menceritakan satu bagian kode dengan empat langkah yang sama.</span></div></div>
      <div class="pola-grid stagger">${POLA.map(([key, ic, l, w], i) => `<div class="pola" style="--pw:${w};--i:${i}"><span class="pola-ico">${ico(ic, 20)}</span><b>${esc(l)}</b><small>${esc(k.pola[i] || "")}</small></div>`).join("")}</div>
    </section>

    <section class="card panel">
      <div class="section-head"><div><h2>${ico("kue", 22)} Resepnya: dari dapur ke kode</h2><span class="sub">Setiap bahan dan langkah membuat kue punya padanan di proyek deep learning.</span></div></div>
      <div class="resep">${k.resep.map((r, i) => `<div class="resep-row" style="--i:${i}"><span class="rr-no">${i + 1}</span><b class="rr-kue">${esc(r.kue)}</b><span class="rr-dl">${esc(r.dl)}</span><code class="path">${esc(r.file)}</code></div>`).join("")}</div>
    </section>

    ${tahap.map((t) => `<section class="section">
      <div class="section-head"><div><h2>${esc(t)}</h2></div></div>
      <div class="bab-grid stagger">${k.bab.map((b, i) => [b, i]).filter(([b]) => b.tahap === t).map(([b, i], j) => `<a class="card bab-card${kisahDone(k.id, b.id) ? " done" : ""}" href="#/kisah/${esc(k.id)}/${esc(b.id)}" style="--i:${j}">
        <span class="bc-no">${i}</span><div><b>${esc(b.judul)}</b><small>${esc(b.file.slice(0, 2).join(", "))}${b.file.length > 2 ? " …" : ""}</small></div>
        <span class="bc-st">${kisahDone(k.id, b.id) ? ico("check", 16) : ico("arrow", 16)}</span></a>`).join("")}</div>
    </section>`).join("")}
  </div>`;
  if (typeof countUp === "function") countUp(v);
});

route(/^kisah\/([^/]+)\/([^/]+)$/, (v, kid, bid) => {
  const k = kisahById(kid);
  const i = k ? k.bab.findIndex((b) => b.id === bid) : -1;
  if (i < 0) { location.hash = k ? "#/kisah/" + kid : "#/kisah"; return; }
  const b = k.bab[i], prev = k.bab[i - 1], next = k.bab[i + 1];
  const nSoal = (S.soal || []).filter((s) => s.kisah === k.id && s.bab === b.id).length;
  const mk = (b.materi || []).map(materiById).filter(Boolean);
  const draw = () => {
    const done = kisahDone(k.id, b.id);
    v.innerHTML = `<div class="page kisah-page">
      <div class="kp-top"><a class="link" href="#/kisah/${esc(k.id)}">${ico("back", 14)} ${esc(k.singkat)}</a>
        <div class="kp-prog">${k.bab.map((x, j) => `<a href="#/kisah/${esc(k.id)}/${esc(x.id)}" class="${j === i ? "on" : ""}${kisahDone(k.id, x.id) ? " done" : ""}" title="${j}. ${esc(x.judul)}"></a>`).join("")}</div></div>
      <header class="kp-head reveal">
        <div class="chips"><span class="chip dark">Bab ${i} dari ${k.bab.length - 1}</span><span class="chip">${esc(b.tahap)}</span></div>
        <h1>${esc(b.judul)}</h1>
        <div class="kp-files">${b.file.map((f) => `<code class="path">${esc(f)}</code>`).join("")}</div>
      </header>
      <div class="kp-cerita">${POLA.map(([key, ic, l, w], j) => `<section class="cerita reveal" style="--pw:${w};--i:${j}">
        <div class="ct-side"><span class="pola-ico">${ico(ic, 22)}</span><small>${j + 1}</small></div>
        <div class="ct-body"><h3>${esc(l)}</h3><p>${esc(b[key])}</p></div></section>`).join("")}</div>
      <div class="kp-grid">
        <div class="kp-main">
          ${b.langkah.length ? `<section class="card panel"><h3>${ico("list", 18)} Langkah di kode</h3><ol class="kp-langkah">${b.langkah.map((x) => `<li>${esc(x)}</li>`).join("")}</ol></section>` : ""}
          ${b.kode ? `<section class="card panel kode-panel"><div class="kode-head"><h3>${ico("file", 18)} Potongan kode</h3><code class="path">${esc(b.kode.file)}</code><button class="btn sm" id="salinKode">Salin</button></div>
            <pre class="kode"><code>${esc(b.kode.isi)}</code></pre><p class="muted" style="font-size:.88rem">${esc(b.kode.ket)}</p></section>` : ""}
          ${b.catatan ? `<div class="banner info">${esc(b.catatan)}</div>` : ""}
        </div>
        <aside class="kp-side">
          ${b.angka.length ? `<section class="card panel"><h3>Angka dari Oralytic</h3><div class="angka-list">${b.angka.map((a) => `<div class="angka"><b>${esc(a.nilai)}</b><small>${esc(a.label)}</small></div>`).join("")}</div></section>` : ""}
          ${b.istilah.length ? `<section class="card panel"><h3>Istilah penting</h3><dl class="istilah">${b.istilah.map((x) => `<dt>${esc(x.nama)}</dt><dd>${esc(x.arti)}</dd>`).join("")}</dl></section>` : ""}
          ${mk.length ? `<section class="card panel"><h3>Mata kuliah yang dipakai</h3><div class="chips">${mk.map((m) => `<a class="chip outline" href="#/materi/${esc(m.id)}"><span class="bd-dot" style="--bd:${BIDANG[bidangOf(m)].warna}"></span>${esc(m.nama)}</a>`).join("")}</div></section>` : ""}
        </aside>
      </div>
      <div class="kp-foot card">
        <button class="btn${done ? "" : " primary"}" id="tandaiBab">${ico("check", 16)} ${done ? "Sudah dibaca" : "Tandai sudah dibaca"}</button>
        ${nSoal ? `<a class="btn" href="#/latihan/kisah/${esc(k.id)}~${esc(b.id)}">${ico("latihan", 16)} Latihan bab ini · ${nSoal} soal</a>` : ""}
        <span style="flex:1"></span>
        ${prev ? `<a class="btn" href="#/kisah/${esc(k.id)}/${esc(prev.id)}">${ico("back", 16)} Sebelumnya</a>` : ""}
        ${next ? `<a class="btn primary" href="#/kisah/${esc(k.id)}/${esc(next.id)}">Berikutnya ${ico("arrow", 16)}</a>` : `<a class="btn primary" href="#/latihan/kisah/${esc(k.id)}">Latihan semua bab ${ico("arrow", 16)}</a>`}
      </div>
    </div>`;
    if (typeof revealIn === "function") revealIn(v);
  };
  v.addEventListener("click", (e) => {
    if (e.target.closest("#tandaiBab")) {
      const on = toggleProgres("kisah", k.id, b.id);
      if (on && next) toast("Bab selesai. Lanjut ke bab berikutnya kapan pun kamu siap.");
      draw();
      return;
    }
    if (e.target.closest("#salinKode")) navigator.clipboard?.writeText(b.kode.isi).then(() => toast("Kode disalin"));
  });
  draw();
});

/* =========================================================
   PUSTAKA (buku di folder Referensi)
   ========================================================= */
ui.pusQ = "";
route(/^pustaka\/([^/?]+)(?:\?.*)?$/, (v, pid) => {
  const r = S.referensi.find((x) => x.id === pid && x.jenis === "pustaka");
  if (!r) { location.hash = "#/referensi?jenis=pustaka"; return; }
  const qs = new URLSearchParams(location.hash.split("?")[1] || "");
  const fokus = +qs.get("bab") || 0;
  const nSoal = (S.soal || []).filter((s) => s.pustaka === r.id).length;
  const draw = () => {
    const nBaca = r.bab.filter((b) => babDibaca(r.id, b.no)).length;
    const pct = Math.round((nBaca / r.bab.length) * 100);
    const q = ui.pusQ.trim().toLowerCase();
    const cocok = (b) => !q || [b.judul, b.asli, b.ringkas, ...(b.alat || []).map((a) => alatById(a)?.nama || a), ...(b.materi || []).map((m) => materiById(m)?.nama || m)].join(" ").toLowerCase().includes(q);
    const al = (r.alat || []).map(alatById).filter(Boolean);
    v.innerHTML = `<div class="page">
      <a class="link" href="#/referensi?jenis=pustaka">${ico("back", 14)} Referensi</a>
      <section class="pus-hero card">
        <div class="ph-cover"><span>${esc((r.singkat || r.judul).slice(0, 28))}</span><small>${r.tahun || ""}</small></div>
        <div class="ph-main">
          <small class="muted">${esc([r.penulis, r.penerbit, r.tahun].filter(Boolean).join(" · "))}</small>
          <h1>${esc(r.judul)}</h1>
          <p class="lead">${esc(r.ket)}</p>
          <div class="chips"><span class="chip">${r.bab.length} bab</span><span class="chip">${r.halaman} halaman PDF</span></div><code class="path">${esc(r.file)}</code>
          <div class="kh-act">${DESKTOP ? `<button class="btn primary" data-file="${esc(r.file)}" hidden>${ico("file", 16)} Buka PDF</button>` : ""}
            ${nSoal ? `<a class="btn" href="#/latihan/pustaka/${esc(r.id)}">${ico("latihan", 16)} Latihan ${nSoal} soal</a>` : ""}</div>
        </div>
        <div class="kh-ring"><div class="ring" style="--p:${pct}" data-label="${pct}%"></div><small>${nBaca} dari ${r.bab.length} bab dibaca</small></div>
      </section>
      ${al.length ? `<section class="card panel"><h3>Alat yang dibahas</h3><div class="chips">${al.map((a) => `<a class="chip" href="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</a>`).join("")}</div></section>` : ""}
      <div class="ref-filter"><div class="field"><input id="pusQ" placeholder="Cari di ${r.bab.length} bab: judul, ringkasan, alat, mata kuliah…" value="${esc(ui.pusQ)}" autocomplete="off"></div></div>
      <div class="pus-bab stagger">${r.bab.filter(cocok).map((b, i) => { const ok = babDibaca(r.id, b.no); return `<article class="card pb${ok ? " done" : ""}${b.no === fokus ? " fokus" : ""}" id="bab-${b.no}" style="--i:${Math.min(i, 14)}">
        <div class="pb-no">${b.no}</div>
        <div class="pb-main"><h3>${esc(b.judul)}</h3><small class="muted">${esc(b.asli)} · ${fmtHal(b.hal)}</small>
          <p>${esc(b.ringkas)}</p>
          <div class="chips">${(b.alat || []).map(alatById).filter(Boolean).map((a) => `<a class="chip" href="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</a>`).join("")}${(b.materi || []).map(materiById).filter(Boolean).map((m) => `<a class="chip outline" href="#/materi/${esc(m.id)}"><span class="bd-dot" style="--bd:${BIDANG[bidangOf(m)].warna}"></span>${esc(m.nama)}</a>`).join("")}</div></div>
        <button class="pb-cek${ok ? " on" : ""}" data-baca="${b.no}" title="${ok ? "Sudah dibaca" : "Tandai sudah dibaca"}"><span class="box">${ico("check", 14)}</span><span>${ok ? "Dibaca" : "Tandai"}</span></button>
      </article>`; }).join("") || `<div class="empty">Tidak ada bab yang cocok.</div>`}</div>
      <p class="muted" style="font-size:.84rem">Nomor halaman mengikuti nomor halaman di file PDF (bukan nomor cetak), jadi bisa langsung diketik di kotak halaman pembaca PDF.</p>
    </div>`;
    tandaiFileAda(v);
    if (typeof countUp === "function") countUp(v);
  };
  v.addEventListener("click", (e) => {
    const c = e.target.closest("[data-baca]");
    if (c) { toggleProgres("pustaka", r.id, c.dataset.baca); const y = v.scrollTop; draw(); v.scrollTop = y; return; }
    const f = e.target.closest("[data-file]"); if (f) openFile(f.dataset.file);
  });
  let t;
  v.addEventListener("input", (e) => {
    if (e.target.id !== "pusQ") return;
    clearTimeout(t);
    t = setTimeout(() => { ui.pusQ = e.target.value; const pos = e.target.selectionStart; draw(); const inp = $("#pusQ", v); inp.focus(); inp.setSelectionRange(pos, pos); }, 200);
  });
  draw();
  if (fokus) requestAnimationFrame(() => $("#bab-" + fokus, v)?.scrollIntoView({ block: "center" }));
});
