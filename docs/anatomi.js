"use strict";

/* =========================================================
   Anatomi alat: ilustrasi dipecah per komponen (blok), lalu
   tiap blok ditarik garis ke mata kuliah yang membangunnya,
   seperti mindmap. Garis diwarnai menurut bidang kuliah.
   ========================================================= */

const BIDANG = {
  Informatika: { warna: "#2483ff", ket: "Pemrograman, data, AI, IoT" },
  Elektrikal: { warna: "#fe7b02", ket: "Elektronika, sensor, kendali" },
  Desain: { warna: "#ff3fd8", ket: "CAD, purwarupa, desain produk" },
  Dasar: { warna: "#8a8985", ket: "Sains dasar, kedokteran, klinis" },
};
const BIDANG_URUT = ["Elektrikal", "Informatika", "Desain", "Dasar"];
const bidangOf = (m) => (m && BIDANG[m.bidang] ? m.bidang : "Dasar");
const bidangChip = (b, extra = "") => `<span class="bd-chip" style="--bd:${BIDANG[b].warna}"${extra}><i></i>${esc(b)}</span>`;

function anatomiHtml(a) {
  const blok = a.blok || [];
  const kontrib = (a.kontribusi || []).filter((k) => materiById(k.materi));
  const mats = kontrib.map((k) => [materiById(k.materi), k])
    .sort((x, y) => BIDANG_URUT.indexOf(bidangOf(x[0])) - BIDANG_URUT.indexOf(bidangOf(y[0])) || y[1].tingkat - x[1].tingkat);
  const hitung = BIDANG_URUT.map((b) => [b, mats.filter(([m]) => bidangOf(m) === b).length]).filter(([, n]) => n);
  let lastB = "";
  return `<section class="card anat-card">
    <div class="anat-head">
      <div><h2>Anatomi ${esc(a.singkatan || a.nama)}</h2><span class="sub">Komponen alat dipecah, lalu ditarik ke mata kuliah yang membangunnya. Arahkan kursor ke komponen atau mata kuliah.</span></div>
      <div class="right">
        <div class="bd-filter">${hitung.map(([b, n]) => `<button class="bd-chip on" data-bd="${b}" style="--bd:${BIDANG[b].warna}" title="${esc(BIDANG[b].ket)}"><i></i>${b} · ${n}</button>`).join("")}</div>
        <button class="btn sm" id="anatToggle">${ico("loop", 16)} <span>Rakit ulang</span></button>
      </div>
    </div>
    <div class="anat" id="anat">
      <svg class="anat-lines" id="anatLines" aria-hidden="true"></svg>
      <div class="anat-col anat-dev">
        <div class="anat-ilus${a.gambar && gambarUrl(a.gambar) ? " has-foto" : ""}" id="anatIlus">${a.gambar && gambarUrl(a.gambar) ? `<img class="anat-foto" src="${esc(gambarUrl(a.gambar))}" alt="Foto ${esc(a.nama)}" onerror="this.remove()">` : ""}${ilustrasiSvg(a)}</div>
        <div class="anat-cap"><b>${esc(a.nama)}</b><span>${blok.length} komponen · ${kontrib.length} mata kuliah</span></div>
      </div>
      <div class="anat-col anat-bloks">${blok.map((b, i) => `<button class="anat-node blok-node" data-ab="${esc(b.id)}" style="--i:${i}">
          <span class="bn">${i + 1}</span><span><b>${esc(b.nama)}</b><small>${esc(b.fungsi || "")}</small></span></button>`).join("")}</div>
      <div class="anat-col anat-mats">${mats.map(([m, k], i) => {
        const b = bidangOf(m);
        const head = b !== lastB ? `<div class="anat-grp" style="--bd:${BIDANG[b].warna};--i:${i}">${b}</div>` : "";
        lastB = b;
        return `${head}<a class="anat-node mat-node t${k.tingkat}" href="#/materi/${esc(m.id)}" data-am="${esc(m.id)}" data-bd="${b}" style="--bd:${BIDANG[b].warna};--i:${i}" title="${esc(TINGKAT[k.tingkat])}: ${esc(k.peran || "")}">
          <i></i><span>${esc(m.nama)}</span><em>${esc(semShort(m))}</em></a>`;
      }).join("")}</div>
    </div>
    <div class="anat-legend">${BIDANG_URUT.map((b) => bidangChip(b)).join("")}<span class="muted">Garis tebal = peran Inti, sedang = Penting, tipis = Pendukung. Garis putus-putus = berlaku untuk seluruh alat.</span></div>
  </section>`;
}

function bindAnatomi(root, a, onBlok) {
  const stage = $("#anat", root);
  if (!stage) return;
  const svg = $("#anatLines", root);
  const kontrib = (a.kontribusi || []).filter((k) => materiById(k.materi));
  const off = new Set();

  const rel = (el) => { let x = 0, y = 0, n = el; while (n && n !== stage) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; } return { x, y, w: el.offsetWidth, h: el.offsetHeight }; };
  const curve = (x1, y1, x2, y2) => { const c = Math.max(30, (x2 - x1) * 0.5); return `M${x1} ${y1}C${x1 + c} ${y1} ${x2 - c} ${y2} ${x2} ${y2}`; };

  const draw = () => {
    svg.setAttribute("width", stage.scrollWidth); svg.setAttribute("height", stage.scrollHeight);
    const dev = rel($("#anatIlus", root));
    const dx = dev.x + dev.w - 6, dy = dev.y + dev.h / 2;
    let html = "", i = 0;
    $$(".blok-node", stage).forEach((n) => {
      const r = rel(n);
      html += `<path class="ln ln-dev" data-b="${n.dataset.ab}" pathLength="1" style="--i:${i++}" d="${curve(dx, dy, r.x, r.y + r.h / 2)}"/>`;
    });
    kontrib.forEach((k) => {
      const mn = $(`.mat-node[data-am="${CSS.escape(k.materi)}"]`, stage);
      if (!mn) return;
      const m = rel(mn), b = bidangOf(materiById(k.materi)), w = { 3: 2.4, 2: 1.6, 1: 1 }[k.tingkat] || 1;
      const ends = (k.blok || []).map((bid) => $(`.blok-node[data-ab="${CSS.escape(bid)}"]`, stage)).filter(Boolean);
      if (!ends.length) {
        html += `<path class="ln ln-all" data-m="${k.materi}" data-bd="${b}" pathLength="1" style="--c:${BIDANG[b].warna};--w:${w};--i:${i++}" d="${curve(dx, dy, m.x, m.y + m.h / 2)}"/>`;
        return;
      }
      ends.forEach((bn) => {
        const r = rel(bn);
        html += `<path class="ln" data-m="${k.materi}" data-b="${bn.dataset.ab}" data-bd="${b}" pathLength="1" style="--c:${BIDANG[b].warna};--w:${w};--i:${i++}" d="${curve(r.x + r.w, r.y + r.h / 2, m.x, m.y + m.h / 2)}"/>`;
      });
    });
    svg.innerHTML = html;
    applyOff();
  };

  const applyOff = () => {
    $$(".mat-node", stage).forEach((n) => n.classList.toggle("off", off.has(n.dataset.bd)));
    $$(".anat-grp", stage).forEach((g) => g.classList.toggle("off", off.has(g.textContent.trim())));
    $$(".ln[data-bd]", svg).forEach((p) => p.classList.toggle("off", off.has(p.dataset.bd)));
  };

  const focus = (sel) => {
    stage.classList.toggle("focus", !!sel);
    $$(".hl", stage).forEach((n) => n.classList.remove("hl"));
    if (!sel) return;
    const lines = $$(sel.b ? `.ln[data-b="${CSS.escape(sel.b)}"]` : `.ln[data-m="${CSS.escape(sel.m)}"]`, svg);
    lines.forEach((p) => {
      p.classList.add("hl");
      if (p.dataset.m) $(`.mat-node[data-am="${CSS.escape(p.dataset.m)}"]`, stage)?.classList.add("hl");
      if (p.dataset.b) $(`.blok-node[data-ab="${CSS.escape(p.dataset.b)}"]`, stage)?.classList.add("hl");
    });
    if (sel.b) $(`.blok-node[data-ab="${CSS.escape(sel.b)}"]`, stage)?.classList.add("hl");
    if (sel.m) $(`.mat-node[data-am="${CSS.escape(sel.m)}"]`, stage)?.classList.add("hl");
  };

  stage.addEventListener("mouseover", (e) => {
    const b = e.target.closest(".blok-node"), m = e.target.closest(".mat-node");
    focus(b ? { b: b.dataset.ab } : m ? { m: m.dataset.am } : null);
  });
  stage.addEventListener("mouseleave", () => focus(null));
  stage.addEventListener("click", (e) => { const b = e.target.closest(".blok-node"); if (b && onBlok) onBlok(b.dataset.ab); });
  root.addEventListener("click", (e) => {
    const c = e.target.closest(".bd-filter [data-bd]");
    if (!c) return;
    const b = c.dataset.bd;
    off.has(b) ? off.delete(b) : off.add(b);
    c.classList.toggle("on", !off.has(b));
    applyOff();
  });

  const tgl = $("#anatToggle", root);
  const setOpen = (open) => {
    stage.classList.toggle("open", open);
    $("span", tgl).textContent = open ? "Rakit ulang" : "Pecah komponen";
    if (open) { draw(); svg.classList.remove("drawn"); void svg.offsetWidth; svg.classList.add("drawn"); }
  };
  tgl.onclick = () => setOpen(!stage.classList.contains("open"));

  const ro = new ResizeObserver(() => stage.classList.contains("open") && draw());
  ro.observe(stage);
  draw();
  // Mulai dalam keadaan terakit, lalu pecah sendiri agar animasinya terlihat.
  setTimeout(() => setOpen(true), reduceMotion() ? 0 : 450);
}

const reduceMotion = () => document.documentElement.classList.contains("no-anim") || matchMedia("(prefers-reduced-motion: reduce)").matches;
