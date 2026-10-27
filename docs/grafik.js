"use strict";

/* =========================================================
   Grafik bergerak di beranda (v1.3):
   - garis EKG berjalan di belakang hero,
   - progres per bidang (cincin), per semester (kolom),
     dan aktivitas latihan 14 hari terakhir (garis).
   Grafik baru "tumbuh" saat terlihat di layar.
   ========================================================= */

// Satu siklus PQRST tiap `beat` satuan.
function ekgPath(w = 1200, h = 100, beat = 150) {
  const K = [[0, 0], [0.18, 0], [0.24, -0.08], [0.3, 0], [0.38, 0], [0.41, 0.1], [0.45, -0.62], [0.49, 0.22], [0.52, 0], [0.62, 0], [0.7, -0.16], [0.78, 0], [1, 0]];
  const mid = h * 0.66, pts = [];
  for (let x0 = 0; x0 < w; x0 += beat) K.forEach(([fx, fy]) => pts.push(`${(x0 + fx * beat).toFixed(1)} ${(mid + fy * h).toFixed(1)}`));
  return "M" + pts.join("L");
}
function heroEkgHtml() {
  const d = ekgPath();
  return `<svg class="hero-ekg" viewBox="0 0 1200 100" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <defs><linearGradient id="ekgG" x1="0" x2="1"><stop offset="0" stop-color="#2483ff"/><stop offset=".5" stop-color="#ff66f4"/><stop offset="1" stop-color="#fe7b02"/></linearGradient></defs>
    <path class="ekg-base" d="${d}"/><path class="ekg-run" d="${d}" pathLength="1000"/><path class="ekg-run r2" d="${d}" pathLength="1000"/></svg>`;
}

/* ---------- data progres ---------- */
// Satuan progres = sub-materi yang dicentang. Mata kuliah tanpa sub-materi
// dihitung satu poin, penuh bila statusnya "sudah".
function poinMateri(m) {
  const p = subProgress(m);
  return p.total ? { n: p.n, t: p.total } : { n: statusOf(m.id) === "sudah" ? 1 : 0, t: 1 };
}
function progresData() {
  const kumpul = (ms) => ms.reduce((a, m) => { const p = poinMateri(m); a.n += p.n; a.t += p.t; return a; }, { n: 0, t: 0, mk: ms.length });
  const bidang = BIDANG_URUT.map((b) => ({ b, ...kumpul(S.materi.filter((m) => bidangOf(m) === b)) })).filter((x) => x.mk);
  const sems = [...new Set(S.materi.map((m) => m.semester).filter(Boolean))].sort((a, b) => a - b);
  const semester = sems.map((s) => ({ s, ...kumpul(S.materi.filter((m) => m.semester === s)) }));
  const L = S.progres.latihan || {}, hari = [];
  for (let i = 13; i >= 0; i--) {
    const d = new Date(); d.setDate(d.getDate() - i);
    const k = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
    hari.push({ d, n: (L.hari || {})[k] || 0 });
  }
  return { bidang, semester, hari };
}
const pctOf = (x) => (x.t ? Math.round((x.n / x.t) * 100) : 0);

function progresHtml() {
  const D = progresData();
  const tglPendek = (d) => d.toLocaleDateString("id-ID", { day: "numeric", month: "short" });
  const totalSoal = D.hari.reduce((s, h) => s + h.n, 0);
  const maxSem = D.semester.reduce((m, x) => Math.max(m, pctOf(x)), 0);
  return `<section class="section pg reveal" id="pgSec">
    <div class="section-head"><div><h2>Progres belajarmu</h2><span class="sub">Dihitung dari sub-materi yang sudah kamu centang. Arahkan kursor ke grafik untuk melihat angkanya.</span></div></div>
    <div class="pg-grid">
      <div class="card pg-card"><h3>Per bidang</h3>
        <div class="pg-rings">${D.bidang.map((x, i) => { const p = pctOf(x); return `<div class="pg-ring-row" style="--c:${BIDANG[x.b].warna};--i:${i}">
          <div class="pg-ring"><svg viewBox="0 0 64 64" aria-hidden="true"><circle class="trk" cx="32" cy="32" r="26"/><circle class="val" cx="32" cy="32" r="26" pathLength="100" data-p="${p}"/></svg><b><span data-count="${p}">${p}</span>%</b></div>
          <div><b>${esc(x.b)}</b><small>${x.n} dari ${x.t} poin · ${x.mk} mata kuliah</small></div></div>`; }).join("")}</div>
      </div>
      <div class="card pg-card"><h3>Per semester</h3>
        <div class="pg-cols" style="--n:${D.semester.length}">
          <div class="pg-axis"><span>100%</span><span>50%</span><span>0</span></div>
          <div class="pg-plot">${D.semester.map((x, i) => { const p = pctOf(x); return `<div class="pg-col${p && p === maxSem ? " lbl" : ""}" style="--v:${p};--i:${i}" tabindex="0" data-tip="Semester ${x.s}: ${x.n} dari ${x.t} poin (${p}%)" aria-label="Semester ${x.s}: ${p} persen"><i><em>${p}%</em></i><span>S${x.s}</span></div>`; }).join("")}</div>
        </div>
      </div>
      <div class="card pg-card"><h3>Latihan 14 hari terakhir</h3>
        <div class="pg-spark" id="pgSpark" data-total="${totalSoal}"></div>
        <div class="pg-spark-foot"><span>${esc(tglPendek(D.hari[0].d))}</span><span class="muted">${totalSoal ? `${totalSoal} soal dijawab` : "Belum ada latihan dua minggu ini"}</span><span>Hari ini</span></div>
      </div>
    </div>
    <details class="pg-table"><summary>Lihat sebagai tabel</summary>
      <table><thead><tr><th>Kelompok</th><th>Poin dikuasai</th><th>Persen</th></tr></thead><tbody>
        ${D.bidang.map((x) => `<tr><td>Bidang ${esc(x.b)}</td><td>${x.n}/${x.t}</td><td>${pctOf(x)}%</td></tr>`).join("")}
        ${D.semester.map((x) => `<tr><td>Semester ${x.s}</td><td>${x.n}/${x.t}</td><td>${pctOf(x)}%</td></tr>`).join("")}
      </tbody></table>
      <table><thead><tr><th>Tanggal</th><th>Soal dijawab</th></tr></thead><tbody>${D.hari.map((h) => `<tr><td>${esc(h.d.toLocaleDateString("id-ID", { weekday: "short", day: "numeric", month: "short" }))}</td><td>${h.n}</td></tr>`).join("")}</tbody></table>
    </details>
    <div class="pg-tip" id="pgTip" hidden></div>
  </section>`;
}

function bindProgres(v) {
  const sec = $("#pgSec", v);
  if (!sec) return;
  const D = progresData(), tip = $("#pgTip", sec), box = $("#pgSpark", sec);
  let jalan = false;

  const tampil = () => {
    if (jalan) return; jalan = true;
    sec.classList.add("tumbuh");
    $$(".pg-ring .val", sec).forEach((c, i) => setTimeout(() => (c.style.strokeDashoffset = 100 - +c.dataset.p), reduceMotion() ? 0 : 120 + i * 90));
    if (typeof countUp === "function") countUp(sec);
    gambarSpark(true);
  };

  // Garis aktivitas: digambar ulang sesuai lebar kotak.
  function gambarSpark(anim) {
    const W = box.clientWidth || 280, H = 132, pad = { l: 26, r: 10, t: 14, b: 8 };
    const max = Math.max(4, ...D.hari.map((h) => h.n));
    const top = Math.ceil(max / 5) * 5;
    const x = (i) => pad.l + (i / (D.hari.length - 1)) * (W - pad.l - pad.r);
    const y = (n) => pad.t + (1 - n / top) * (H - pad.t - pad.b);
    const pts = D.hari.map((h, i) => [x(i), y(h.n)]);
    const line = "M" + pts.map((p) => p.map((q) => q.toFixed(1)).join(" ")).join("L");
    const area = `${line}L${x(D.hari.length - 1).toFixed(1)} ${y(0)}L${x(0).toFixed(1)} ${y(0)}Z`;
    const last = pts[pts.length - 1];
    box.innerHTML = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="Jumlah soal per hari selama 14 hari terakhir">
      <line class="g" x1="${pad.l}" x2="${W - pad.r}" y1="${y(top)}" y2="${y(top)}"/><line class="g" x1="${pad.l}" x2="${W - pad.r}" y1="${y(0)}" y2="${y(0)}"/>
      <text class="ax" x="${pad.l - 6}" y="${y(top) + 4}">${top}</text><text class="ax" x="${pad.l - 6}" y="${y(0) + 4}">0</text>
      <path class="ar${anim && !reduceMotion() ? " anim" : ""}" d="${area}"/><path class="ln${anim && !reduceMotion() ? " anim" : ""}" d="${line}" pathLength="1"/>
      <line class="xh" id="pgXh" y1="${pad.t}" y2="${y(0)}" x1="0" x2="0" hidden/>
      <circle class="dot end" cx="${last[0]}" cy="${last[1]}" r="4.5"/><text class="vl" x="${last[0] - 8}" y="${last[1] - 10}">${D.hari[D.hari.length - 1].n}</text>
      <circle class="dot hov" id="pgDot" r="4.5" cx="0" cy="0" hidden/>
      <rect class="hit" x="0" y="0" width="${W}" height="${H}"/></svg>`;
    const svg = $("svg", box), xh = $("#pgXh", box), dot = $("#pgDot", box);
    svg.addEventListener("pointermove", (e) => {
      const r = svg.getBoundingClientRect(), px = ((e.clientX - r.left) / r.width) * W;
      const i = Math.max(0, Math.min(D.hari.length - 1, Math.round(((px - pad.l) / (W - pad.l - pad.r)) * (D.hari.length - 1))));
      const [cx, cy] = pts[i];
      xh.hidden = dot.hidden = false;
      xh.setAttribute("x1", cx); xh.setAttribute("x2", cx); dot.setAttribute("cx", cx); dot.setAttribute("cy", cy);
      const h = D.hari[i];
      showTip(`<b>${esc(h.d.toLocaleDateString("id-ID", { weekday: "long", day: "numeric", month: "short" }))}</b>${h.n} soal`, r.left + (cx / W) * r.width, r.top + (cy / H) * r.height);
    });
    svg.addEventListener("pointerleave", () => { xh.hidden = dot.hidden = true; hideTip(); });
  }

  const showTip = (html, cx, cy) => {
    const s = sec.getBoundingClientRect();
    tip.innerHTML = html; tip.hidden = false;
    const w = tip.offsetWidth;
    tip.style.left = Math.max(4, Math.min(s.width - w - 4, cx - s.left - w / 2)) + "px";
    tip.style.top = cy - s.top - tip.offsetHeight - 12 + "px";
  };
  const hideTip = () => { tip.hidden = true; };
  const colTip = (c) => { const r = $("i", c).getBoundingClientRect(); showTip(esc(c.dataset.tip), r.left + r.width / 2, r.top); };
  sec.addEventListener("pointerover", (e) => { const c = e.target.closest(".pg-col"); if (c) colTip(c); });
  sec.addEventListener("pointerout", (e) => { const c = e.target.closest(".pg-col"); if (c && !c.contains(e.relatedTarget)) hideTip(); });
  sec.addEventListener("focusin", (e) => { const c = e.target.closest(".pg-col"); if (c) colTip(c); });
  sec.addEventListener("focusout", hideTip);

  gambarSpark(false);
  let lebar = box.clientWidth;
  new ResizeObserver(() => { if (box.clientWidth !== lebar) { lebar = box.clientWidth; gambarSpark(false); } }).observe(box);
  if (reduceMotion() || !("IntersectionObserver" in window)) { tampil(); return; }
  const io = new IntersectionObserver(([en]) => { if (en.isIntersecting) { tampil(); io.disconnect(); } }, { threshold: 0.2 });
  io.observe(sec);
}

/* ---------- muncul saat digulir ---------- */
// Bagian bertanda .reveal tetap terlihat bila skrip ini gagal; kelas .rv baru
// ditambahkan di sini, jadi konten tidak pernah "hilang".
function revealIn(root) {
  const els = $$(".reveal", root);
  if (!els.length || reduceMotion() || !("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: 0.06, rootMargin: "0px 0px -6% 0px" });
  els.forEach((el) => { el.classList.add("rv"); io.observe(el); });
}
