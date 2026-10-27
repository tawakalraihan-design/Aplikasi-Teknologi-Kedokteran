"use strict";

/* =========================================================
   Modul mata kuliah (v1.3): penjelasan, topik inti, studi kasus
   alat, latihan, dan bahan kuliah dari folder D:\Semester N.
   Plus halaman Referensi dengan keterangan alat pemakainya.
   ========================================================= */

const modulById = (id) => byId(S.modul, id);
const JENIS_REF = {
  pustaka: ["Buku di folder Referensi", "materi"], buku: ["Buku teks", "materi"], standar: ["Standar dan regulasi", "shield"], jurnal: ["Jurnal dan pedoman", "file"],
  dataset: ["Dataset", "grid"], web: ["Web dan perangkat lunak", "link"], proyek: ["Sumber proyek", "proyek"], kuliah: ["Bahan kuliah", "file"],
};
const JENIS_URUT = Object.keys(JENIS_REF);
const refPakaiAlat = (aid) => S.referensi.filter((r) => (r.alat || []).includes(aid));
const refPakaiMateri = (mid) => S.referensi.filter((r) => (r.materi || []).includes(mid));
const urutJenis = (a, b) => JENIS_URUT.indexOf(a.jenis) - JENIS_URUT.indexOf(b.jenis);
const kasusKey = (mid, aid, i) => `${mid}|${aid}|${i}`;
const kasusDone = (k) => !!(S.progres.kasus || {})[k];

function openFile(p) {
  fetch("api/open-file?p=" + encodeURIComponent(p)).then((r) => r.json()).then((d) => {
    if (!d.ok) toast("File tidak ditemukan di laptop ini: " + p, true);
  }).catch(() => toast("Gagal membuka file", true));
}
// Tombol "Buka" bahan kuliah hanya muncul bila file benar-benar ada di drive D.
async function tandaiFileAda(root) {
  const btns = $$("[data-file]", root);
  if (!btns.length || !DESKTOP) return;
  try {
    const r = await fetch("api/cek-file", { method: "POST", body: JSON.stringify(btns.map((b) => b.dataset.file)) });
    const ada = await r.json();
    btns.forEach((b, i) => { b.hidden = !ada[i]; b.closest(".kf")?.classList.toggle("ada", !!ada[i]); });
  } catch (e) {}
}

/* ---------- potongan halaman materi ---------- */
function modulNavHtml(md, nSoal, nKuliah) {
  const it = [["sec-penjelasan", "Penjelasan"], md.kasus.length && ["sec-kasus", `Studi kasus · ${md.kasus.length} alat`],
    nSoal && ["sec-latihan", `Latihan · ${nSoal} soal`], ["sec-sub", "Sub-materi"], nKuliah && ["sec-kuliah", `Bahan kuliah · ${nKuliah}`]].filter(Boolean);
  return `<nav class="mod-nav">${it.map(([id, l]) => `<button class="chip outline" data-jump="${id}">${l}</button>`).join("")}</nav>`;
}

function penjelasanHtml(m, md) {
  return `<section class="card panel mod-intro reveal" id="sec-penjelasan">
    <div class="section-head"><div><h2>${ico("bulb", 22)} Apa yang dipelajari</h2><span class="sub">Ringkasan mata kuliah dan topik intinya, disusun dari bahan kuliah dan silabus.</span></div></div>
    <p class="lead">${esc(md.penjelasan)}</p>
    ${md.karier ? `<p class="muted" style="font-size:.9rem"><b>Dipakai di dunia kerja:</b> ${esc(md.karier)}</p>` : ""}
    <div class="topik-list">${md.topik.map((t, i) => `<details class="topik-item"${i === 0 ? " open" : ""} style="--i:${i}">
      <summary><span class="tn">${i + 1}</span><b>${esc(t.judul)}</b>${(t.sub || []).map((no) => `<span class="chip sm" title="${esc(findSub(m, no)?.nama || "")}">Sub ${esc(no)}</span>`).join("")}<span class="chev">${ico("down", 16)}</span></summary>
      <div class="tbody"><p>${esc(t.isi)}</p>${t.poin.length ? `<ul>${t.poin.map((p) => `<li>${esc(p)}</li>`).join("")}</ul>` : ""}
        ${(t.terkait || []).length ? `<div class="chips"><span class="muted" style="font-size:.82rem">Lihat juga:</span>${t.terkait.map((x) => { const mm = materiById(x.materi); return mm ? `<a class="chip outline" href="#/materi/${esc(mm.id)}">${esc(mm.nama)} · sub ${esc(x.no)}</a>` : ""; }).join("")}</div>` : ""}
      </div></details>`).join("")}</div>
  </section>`;
}

function kasusTabHtml(m, k, i) {
  const a = alatById(k.alat);
  const done = k.pelajari.filter((_, j) => kasusDone(kasusKey(m.id, k.alat, j))).length;
  return `<button class="kasus-tab${i === 0 ? " on" : ""}" data-ki="${i}" style="--i:${i}"><span class="ki">${esc(a?.ikon || "🔧")}</span><span>${esc(a?.singkatan || a?.nama || k.alat)}</span>
    <i class="kring" style="--p:${k.pelajari.length ? Math.round((done / k.pelajari.length) * 100) : 0}"></i></button>`;
}

function kasusBodyHtml(m, k) {
  const a = alatById(k.alat);
  if (!a) return `<div class="empty">Alat ${esc(k.alat)} belum ada di data kamu.</div>`;
  const blokNama = (bid) => byId(a.blok || [], bid)?.nama || bid;
  return `<div class="kasus-card">
    <div class="kasus-head" style="--thumb-grad:${gradOf(a.kategori)}">
      <div class="kasus-ilus">${ilustrasiSvg(a, { cls: "mini" })}</div>
      <div class="kh-txt"><small>${esc(a.nama)} · ${esc(a.kategori || "")}</small><h3>${esc(k.judul)}</h3>
        ${k.blok.length ? `<div class="chips">${k.blok.map((b) => `<span class="chip">${esc(blokNama(b))}</span>`).join("")}</div>` : ""}</div>
      <a class="btn sm" href="#/alat/${esc(a.id)}">Buka alat ${ico("arrow", 14)}</a>
    </div>
    <div class="kasus-grid">
      <div class="kasus-box"><h4>${ico("alat", 18)} Yang dideteksi atau dikerjakan alat</h4><p>${esc(k.deteksi)}</p></div>
      <div class="kasus-box"><h4>${ico("latihan", 18)} Yang harus kamu pelajari</h4>
        <div class="checklist">${k.pelajari.map((p, j) => { const key = kasusKey(m.id, k.alat, j); return `<button class="kc${kasusDone(key) ? " on" : ""}" data-kk="${esc(key)}" style="--i:${j}"><span class="box">${ico("check", 14)}</span><span>${esc(p)}</span></button>`; }).join("")}</div></div>
      <div class="kasus-box wide"><h4>${ico("bulb", 18)} Penerapan di alat</h4><p>${esc(k.aplikasi)}</p></div>
    </div>
  </div>`;
}

function kasusHtml(m, md) {
  if (!md.kasus.length) return "";
  return `<section class="card panel reveal" id="sec-kasus">
    <div class="section-head"><div><h2>Studi kasus alat</h2><span class="sub">Bagaimana ${esc(m.nama)} dipakai di ${md.kasus.length} alat nyata. Centang poin yang sudah kamu kuasai.</span></div></div>
    <div class="kasus-tabs" role="tablist">${md.kasus.map((k, i) => kasusTabHtml(m, k, i)).join("")}</div>
    <div class="kasus-body" id="kasusBody">${kasusBodyHtml(m, md.kasus[0])}</div>
  </section>`;
}

function latihanMateriHtml(m) {
  const qs = typeof soalMateri === "function" ? soalMateri(m.id) : [];
  if (!qs.length) return "";
  const r = ((S.progres.latihan || {}).materi || {})[m.id];
  const tipe = [...new Set(qs.map((q) => q.tipe))];
  return `<section class="card latihan-cta reveal" id="sec-latihan">
    <div class="lc-ico">${ico("latihan", 28)}</div>
    <div><h2>Latihan soal ${esc(m.nama)}</h2>
      <p class="muted">${qs.length} soal dengan ${tipe.length} tipe. Tiap sesi mengambil 10 soal acak dan mencampur tipe soal.</p>
      <div class="chips">${tipe.map((t) => `<span class="chip">${esc(TIPE[t] || t)}</span>`).join("")}</div></div>
    <div class="lc-act">${r ? `<div class="lc-best"><b>${r.terbaik || 0}%</b><small>skor terbaik</small></div>` : ""}<a class="btn primary" href="#/latihan/materi/${esc(m.id)}">${ico("play", 16)} Mulai latihan</a></div>
  </section>`;
}

function kuliahHtml(m, md) {
  const fs = md.kuliah || [];
  if (!fs.length) return "";
  const folder = (fs[0].file.match(/^(.*\\Semester \d+\\[^\\]+)/) || [])[1] || "";
  return `<section class="card panel" id="sec-kuliah"><h3>${ico("file", 18)} Bahan kuliah · ${fs.length} file</h3>
    <p class="muted" style="font-size:.84rem">Dari folder <code class="path">${esc(folder)}</code>${DESKTOP ? ". Tombol Buka muncul bila file ada di laptop ini." : ". File ini ada di laptop; di HP hanya ringkasannya."}</p>
    <div class="kuliah-list">${fs.map((f) => `<div class="kf"><span class="kf-ico j-${esc(f.jenis)}">${esc(f.jenis.toUpperCase().slice(0, 4))}</span>
      <div class="kf-main"><b>${esc(f.judul)}</b><small>${f.kontrak ? "Kontrak kuliah · " : ""}${f.n} ${f.jenis === "pdf" ? "halaman" : "slide"}</small>
        ${f.poin.length ? `<details><summary>Isi</summary><ul>${f.poin.map((p) => `<li>${esc(p)}</li>`).join("")}</ul></details>` : ""}</div>
      ${DESKTOP ? `<button class="btn sm" data-file="${esc(f.file)}" hidden>Buka</button>` : ""}</div>`).join("")}</div>
  </section>`;
}

function refItemMini(r) {
  if (r.jenis === "pustaka") return `<li><a class="link" href="#/pustaka/${esc(r.id)}"><b>${esc(r.singkat || r.judul)}</b></a> <span class="muted">· ${r.bab.length} bab · folder Referensi</span></li>`;
  return `<li><b>${esc(r.judul)}</b>${r.penulis ? ` <span class="muted">· ${esc(r.penulis)}${r.tahun ? " " + r.tahun : ""}</span>` : ""}
    ${r.url ? ` <button class="link" data-url="${esc(r.url)}">buka</button>` : ""}</li>`;
}
// Panel referensi di halaman alat/materi: teks lama milik pengguna + referensi terkait dari referensi.json.
function refPanelHtml(lama, terkait, href) {
  const pilih = terkait.filter((r) => r.jenis !== "kuliah").sort(urutJenis);
  if (!(lama || []).length && !pilih.length) return "";
  return `<section class="card panel"><h3>Referensi</h3>
    ${(lama || []).length ? `<ul class="ref-list">${lama.map((r) => `<li>${refHtml(r)}</li>`).join("")}</ul>` : ""}
    ${pilih.length ? `<ul class="ref-list">${pilih.slice(0, 7).map(refItemMini).join("")}</ul>` : ""}
    ${terkait.length ? `<a class="btn sm" href="${href}">${ico("ref", 16)} Semua referensi (${terkait.length})</a>` : ""}</section>`;
}

function bindModul(v, m, md) {
  v.addEventListener("click", (e) => {
    const j = e.target.closest("[data-jump]");
    if (j) { $("#" + j.dataset.jump, v)?.scrollIntoView({ behavior: reduceMotion() ? "auto" : "smooth", block: "start" }); return; }
    const t = e.target.closest("[data-ki]");
    if (t) {
      $$(".kasus-tab", v).forEach((x) => x.classList.toggle("on", x === t));
      const body = $("#kasusBody", v);
      body.innerHTML = kasusBodyHtml(m, md.kasus[+t.dataset.ki]);
      body.classList.remove("swap"); void body.offsetWidth; body.classList.add("swap");
      return;
    }
    const c = e.target.closest("[data-kk]");
    if (c) {
      const P = (S.progres.kasus = S.progres.kasus || {});
      if (P[c.dataset.kk]) delete P[c.dataset.kk]; else P[c.dataset.kk] = true;
      c.classList.toggle("on", !!P[c.dataset.kk]);
      const on = $(".kasus-tab.on", v), ki = on ? +on.dataset.ki : 0;
      on.outerHTML = kasusTabHtml(m, md.kasus[ki], ki).replace('class="kasus-tab"', 'class="kasus-tab on"');
      saveLater("progres", 300);
      return;
    }
    const f = e.target.closest("[data-file]");
    if (f) openFile(f.dataset.file);
  });
  tandaiFileAda(v);
}

/* =========================================================
   HALAMAN REFERENSI
   ========================================================= */
ui.refJenis = "semua"; ui.refAlat = ""; ui.refQ = ""; ui.refBuka = {};
route(/^referensi(?:\?.*)?$/, (v) => {
  const qs = new URLSearchParams(location.hash.split("?")[1] || "");
  if (qs.has("alat")) { ui.refAlat = qs.get("alat"); ui.refJenis = "semua"; }
  if (qs.has("q")) ui.refQ = qs.get("q");
  if (qs.has("jenis")) ui.refJenis = qs.get("jenis");
  const hitungAlat = {};
  S.referensi.forEach((r) => (r.alat || []).forEach((a) => (hitungAlat[a] = (hitungAlat[a] || 0) + 1)));

  const cocok = (r) => {
    if (ui.refAlat && !(r.alat || []).includes(ui.refAlat)) return false;
    const q = ui.refQ.trim().toLowerCase();
    if (!q) return true;
    const t = [r.judul, r.penulis, r.ket, ...(r.alat || []).map((a) => alatById(a)?.nama || a), ...(r.materi || []).map((x) => materiById(x)?.nama || x), ...(r.bab || []).map((b) => b.judul + " " + b.asli + " " + b.ringkas)].join(" ").toLowerCase();
    return t.includes(q);
  };
  const item = (r, i) => {
    const [, ic] = JENIS_REF[r.jenis] || ["", "link"];
    const al = (r.alat || []).map(alatById).filter(Boolean);
    const ma = (r.materi || []).map(materiById).filter(Boolean);
    return `<div class="ref-item" style="--i:${Math.min(i, 12)}"><span class="ri-ico j-${esc(r.jenis)}">${ico(ic, 20)}</span>
      <div class="ri-main"><div class="ri-title">${esc(r.judul)}</div>
        <div class="ri-meta">${[r.penulis, r.tahun].filter(Boolean).map(esc).join(" · ")}${r.file ? `<code class="path">${esc(r.file)}</code>` : ""}</div>
        ${r.ket ? `<p>${esc(r.ket)}</p>` : ""}
        ${r.jenis === "pustaka" ? (() => { const nb = r.bab.filter((b) => babDibaca(r.id, b.no)).length; return `<div class="ri-bab"><a class="btn sm" href="#/pustaka/${esc(r.id)}">${ico("materi", 16)} ${r.bab.length} bab dengan ringkasan</a><span class="muted">${nb ? `${nb} bab sudah dibaca` : esc(r.bab.slice(0, 3).map((b) => b.judul).join(" · ")) + " …"}</span></div>`; })() : ""}
        <div class="ri-use">${al.length ? `<span class="muted">Untuk alat:</span>${al.map((a) => `<a class="chip${a.id === ui.refAlat ? " dark" : ""}" href="#/alat/${esc(a.id)}">${esc(a.ikon)} ${esc(a.singkatan || a.nama)}</a>`).join("")}` : `<span class="muted">Referensi umum, belum dikaitkan ke alat tertentu.</span>`}</div>
        ${ma.length ? `<div class="ri-use"><span class="muted">Mata kuliah:</span>${ma.slice(0, 6).map((m) => `<a class="chip outline" href="#/materi/${esc(m.id)}"><span class="bd-dot" style="--bd:${BIDANG[bidangOf(m)].warna}"></span>${esc(m.nama)}</a>`).join("")}</div>` : ""}
      </div>
      <div class="ri-act">${r.url ? `<button class="btn sm" data-url="${esc(r.url)}">${ico("link", 16)} Buka</button>` : ""}${r.file && DESKTOP ? `<button class="btn sm" data-file="${esc(r.file)}" hidden>${ico("file", 16)} Buka file</button>` : ""}</div></div>`;
  };

  const draw = () => {
    const list = S.referensi.filter(cocok);
    const perJenis = JENIS_URUT.map((j) => [j, list.filter((r) => r.jenis === j)]).filter(([, l]) => l.length);
    const tampil = ui.refJenis === "semua" ? perJenis : perJenis.filter(([j]) => j === ui.refJenis);
    const al = alatById(ui.refAlat);
    const grup = (j, l) => {
      const batas = ui.refBuka[j] ? l.length : 12;
      // Bahan kuliah dikelompokkan per mata kuliah agar mudah dipindai.
      if (j === "kuliah") {
        const g = {};
        l.forEach((r) => { const k = (r.materi || [])[0] || ""; (g[k] = g[k] || []).push(r); });
        const ks = Object.keys(g).sort((x, y) => ((materiById(x)?.semester || 9) - (materiById(y)?.semester || 9)) || String(materiById(x)?.nama).localeCompare(materiById(y)?.nama));
        return ks.slice(0, ui.refBuka[j] ? ks.length : 6).map((k) => `<details class="ref-sub"${ui.refAlat || ui.refQ ? " open" : ""}><summary><b>${esc(materiById(k)?.nama || k)}</b><span class="muted">${esc(semShort(materiById(k)))} · ${g[k].length} file</span></summary>${g[k].map(item).join("")}</details>`).join("")
          + (ks.length > 6 && !ui.refBuka[j] ? `<button class="btn sm" data-more="${j}">Tampilkan semua ${ks.length} mata kuliah</button>` : "");
      }
      return l.slice(0, batas).map(item).join("") + (l.length > batas ? `<button class="btn sm" data-more="${j}">Tampilkan ${l.length - batas} lagi</button>` : "");
    };
    v.innerHTML = `<div class="page">
      <div class="section-head"><div><h1>Referensi</h1><span class="sub">${S.referensi.length} referensi: buku di folder Referensi, buku teks, standar, jurnal, dataset, sumber proyek, dan bahan kuliahmu. Tiap referensi menyebut alat yang memakainya.</span></div></div>
      <div class="ref-stats stagger">${perJenis.length ? JENIS_URUT.map((j, i) => { const n = S.referensi.filter((r) => r.jenis === j && cocok(r)).length; return n ? `<button class="ref-stat${ui.refJenis === j ? " on" : ""}" data-jenis="${j}" style="--i:${i}"><span class="ri-ico j-${j}">${ico(JENIS_REF[j][1], 18)}</span><b data-count="${n}">${n}</b><small>${JENIS_REF[j][0]}</small></button>` : ""; }).join("") : ""}</div>
      <div class="ref-filter">
        <div class="field"><input id="refQ" placeholder="Cari judul, penulis, alat, atau mata kuliah…" value="${esc(ui.refQ)}" autocomplete="off"></div>
        <div class="field"><select id="refAlat"><option value="">Semua alat</option>${S.alat.slice().sort((x, y) => x.nama.localeCompare(y.nama)).map((a) => `<option value="${esc(a.id)}"${a.id === ui.refAlat ? " selected" : ""}>${esc(a.ikon)} ${esc(a.nama)} (${hitungAlat[a.id] || 0})</option>`).join("")}</select></div>
        ${ui.refJenis !== "semua" || ui.refAlat || ui.refQ ? `<button class="btn" id="refReset">Hapus filter</button>` : ""}
      </div>
      ${al ? `<div class="banner info">${esc(al.ikon)} Menampilkan ${list.length} referensi yang dipakai untuk <b>${esc(al.nama)}</b>. <a class="link" href="#/alat/${esc(al.id)}">Buka halaman alat</a></div>` : ""}
      ${tampil.length ? tampil.map(([j, l]) => `<section class="section ref-group"><div class="section-head"><div><h2>${esc(JENIS_REF[j][0])}</h2><span class="sub">${l.length} referensi</span></div></div><div class="card ref-list-card">${grup(j, l)}</div></section>`).join("")
        : `<div class="empty">Tidak ada referensi yang cocok.</div>`}
    </div>`;
    if (typeof countUp === "function") countUp(v);
    tandaiFileAda(v);
  };
  v.addEventListener("click", (e) => {
    const j = e.target.closest("[data-jenis]"); if (j) { ui.refJenis = ui.refJenis === j.dataset.jenis ? "semua" : j.dataset.jenis; draw(); return; }
    const mo = e.target.closest("[data-more]"); if (mo) { ui.refBuka[mo.dataset.more] = true; draw(); return; }
    if (e.target.closest("#refReset")) { ui.refJenis = "semua"; ui.refAlat = ""; ui.refQ = ""; history.replaceState(null, "", "#/referensi"); draw(); return; }
    const f = e.target.closest("[data-file]"); if (f) openFile(f.dataset.file);
  });
  v.addEventListener("change", (e) => { if (e.target.id === "refAlat") { ui.refAlat = e.target.value; draw(); } });
  let t;
  v.addEventListener("input", (e) => {
    if (e.target.id !== "refQ") return;
    clearTimeout(t);
    t = setTimeout(() => { ui.refQ = e.target.value; const pos = e.target.selectionStart; draw(); const i = $("#refQ", v); i.focus(); i.setSelectionRange(pos, pos); }, 220);
  });
  draw();
});
