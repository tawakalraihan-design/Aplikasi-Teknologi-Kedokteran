"use strict";

/* =========================================================
   Animasi breakdown komponen alat (v1.3).
   Sinyal "berjalan" dari blok ke blok. Di tiap tahap:
   - bagian ilustrasi yang sesuai menyala,
   - osiloskop mini menunjukkan bentuk sinyal di tahap itu
     (mentah berderau → diperkuat → difilter → disampling → diolah),
   - mata kuliah yang dipakai di blok itu ditampilkan.
   ========================================================= */

/* ---------- blok → bagian ilustrasi ---------- */
const PERAN_RE = [
  ["out", /tampil|layar|display|laporan|monitor|audiogram|aplikasi|dasbor|dokter|interpretasi|visual|fusi|hasil|okuler|notifikasi|respon/],
  ["pow", /catu|baterai|daya|pengaman|alarm|isolasi|keamanan|keselamatan/],
  ["data", /jaringan|ble|bluetooth|iot|platform|database|integrasi|standar|video|lis\b|transmisi|telemetri/],
  ["in", /elektroda|sensor|fotodioda|strip|ppg|imu|ekgjam|detektor|mikrofon|\btoko\b|doppler|radiometer|transduser|probe|manset|sampel|kuvet|kartu|kartrid|aspirasi|sampling|aplikator|aktif|netral|ujung|optik|cahaya|insersi|pemindaian|input|perangkat|wadah|visi|kamera|radiofarmaka|ukur|akuisisi|rekam|^led\b/],
  ["act", /motor|pompa|aktuator|aktuasi|generator|tabung|stimulator|pemanas|koil|kapasitor|magnet|gradien|\brf\b|pemancar|saklar|output|katup|vaporizer|flowmeter|gas|lengan|instrumen|cetak|receiver|led|pendingin|osilator|atenuator|magnetron|kolimator|kompresi|carm|rotor|humidifier|\buf\b|pencampur|fabrikasi|umpan/],
  ["mech", /desain|bantalan|evaluasi|mekanik|meja|socket|tali|kasur|kubah/],
];
// Beberapa blok namanya menyesatkan regex di atas; perannya ditetapkan langsung.
const PERAN_OVR = { "robot-bedah:konsol": "in", "autoklaf:tabung": "mech", "pill-dispenser:wadah": "mech" };
const peranBlok = (b, aid) => { const t = (b.id + " " + b.nama).toLowerCase(); return PERAN_OVR[aid + ":" + b.id] || (PERAN_RE.find(([, re]) => re.test(t)) || ["proc"])[0]; };
const PERAN_PART = {
  monitor: { in: "kabel", proc: "papan", out: "layar", pow: "casing", act: "papan", mech: "casing", data: "papan" },
  klip: { in: "sensor", proc: "bawah", out: "atas", pow: "bawah", act: "sensor", mech: "jari", data: "atas" },
  manset: { in: "manset", proc: "unit", out: "unit", pow: "unit", act: "pompa", mech: "selang", data: "unit" },
  usg: { in: "probe", proc: "konsol", out: "layar", pow: "badan", act: "probe", mech: "badan", data: "konsol" },
  xray: { in: "detektor", proc: "konsol", out: "konsol", pow: "konsol", act: "tabung", mech: "meja", data: "konsol" },
  gantry: { in: "cincin", proc: "konsol", out: "konsol", pow: "gantry", act: "cincin", mech: "meja", data: "konsol" },
  ventilator: { in: "selang", proc: "unit", out: "layar", pow: "unit", act: "unit", mech: "humidifier", data: "layar" },
  pompa: { in: "selang", proc: "unit", out: "unit", pow: "unit", act: "motor", mech: "kantong", data: "unit" },
  aed: { in: "pad", proc: "casing", out: "layar", pow: "kapasitor", act: "kapasitor", mech: "casing", data: "layar" },
  inkubator: { in: "kasur", proc: "unit", out: "unit", pow: "unit", act: "unit", mech: "kubah", data: "unit" },
  dialisis: { in: "pompa", proc: "badan", out: "layar", pow: "badan", act: "pompa", mech: "dialiser", data: "layar" },
  laptop: { in: "sinyal", proc: "data", out: "layar", pow: "alas", act: "data", mech: "alas", data: "data" },
  koil: { in: "kepala", proc: "unit", out: "unit", pow: "unit", act: "unit", mech: "kabel", data: "unit" },
  stimulator: { in: "pad", proc: "papan", out: "unit", pow: "unit", act: "papan", mech: "kabel", data: "unit" },
  konsol: { in: "aplikator", proc: "konsol", out: "konsol", pow: "konsol", act: "generator", mech: "lengan", data: "konsol" },
  brace: { in: "tubuh", proc: "depan", out: "tubuh", pow: "tali", act: "bantalan", mech: "depan", data: "tubuh" },
  genggam: { in: "sensor", proc: "papan", out: "layar", pow: "casing", act: "papan", mech: "casing", data: "layar" },
  analyzer: { in: "rak", proc: "optik", out: "layar", pow: "casing", act: "optik", mech: "casing", data: "layar" },
  sentrifus: { in: "rotor", proc: "badan", out: "badan", pow: "tutup", act: "motor", mech: "rotor", data: "badan" },
  mikroskop: { in: "meja", proc: "tubuh", out: "okuler", pow: "cahaya", act: "cahaya", mech: "tubuh", data: "tubuh" },
  jam: { in: "sensor", proc: "papan", out: "layar", pow: "bodi", act: "papan", mech: "tali", data: "papan" },
  telinga: { in: "perangkat", proc: "perangkat", out: "kabel", pow: "perangkat", act: "kabel", mech: "telinga", data: "kabel" },
  tangan: { in: "sensor", proc: "sensor", out: "telapak", pow: "aktuator", act: "aktuator", mech: "socket", data: "sensor" },
  robot: { in: "kamera", proc: "konsol", out: "konsol", pow: "meja", act: "lengan", mech: "meja", data: "konsol" },
  endoskop: { in: "ujung", proc: "prosesor", out: "prosesor", pow: "prosesor", act: "kendali", mech: "insersi", data: "prosesor" },
  dispenser: { in: "wadah", proc: "badan", out: "badan", pow: "badan", act: "motor", mech: "tutup", data: "badan" },
  kabinet: { in: "ruang", proc: "panel", out: "panel", pow: "katup", act: "ruang", mech: "badan", data: "panel" },
};
// Pengecualian kecil agar komponen menyala di tempat yang masuk akal.
const PART_OVR = {
  "inkubator:led": "kubah", "inkubator:radiometer": "bayi", "inkubator:pemanas": "unit",
  "telinga:transmisi": "kabel", "telinga:stimulator": "koklea", "telinga:elektroda": "koklea",
  "tangan:pemindaian": "socket", "tangan:desain": "telapak", "tangan:cetak": "jari",
  "endoskop:kanal": "kendali", "endoskop:cahaya": "kabel", "kabinet:tabung": "pintu",
};
function partFor(a, b) {
  const arc = IL[a.ilustrasi] ? a.ilustrasi : "monitor";
  const names = IL[arc].map((p) => p[0]);
  if (PART_OVR[arc + ":" + b.id]) return PART_OVR[arc + ":" + b.id];
  const t = (b.id + " " + b.nama).toLowerCase();
  const direct = names.find((n) => new RegExp(`(^|[^a-z])${n}([^a-z]|$)`).test(t));
  if (direct) return direct;
  return (PERAN_PART[arc] || PERAN_PART.monitor)[peranBlok(b, a.id)] || names[0];
}

/* ---------- jenis sinyal per alat dan per tahap ---------- */
const DASAR = {
  ekg: "ekg", holter: "ekg", "patient-monitor": "ekg", defibrilator: "ekg", oksimeter: "ppg", smartwatch: "ppg",
  eeg: "eeg", brainmapping: "eeg", neurofeedback: "eeg", brainwave: "eeg", emg: "emg", "prostesis-tangan": "emg",
  ventilator: "napas", spirometer: "napas", "mesin-anestesi": "napas", kapnograf: "kapno", tensimeter: "tekanan", ctg: "ctg",
  audiometer: "audio", "alat-bantu-dengar": "audio", "implan-koklea": "audio",
  tens: "pulsa", ect: "pulsa", tms: "pulsa", esu: "rf", "stimulasi-listrik": "pulsa", "diatermi-sw": "rf", "diatermi-mw": "rf", "terapi-us": "rf",
  xray: "citra", ct: "citra", mri: "citra", usg: "citra", mammografi: "citra", fluoroskopi: "citra", pet: "citra", endoskop: "citra", mikroskop: "citra", "motion-correction": "citra",
  rme: "data", telemedisin: "data", "pill-dispenser": "data", "robot-bedah": "gerak",
  termometer: "suhu", inkubator: "suhu", autoklaf: "suhu", fototerapi: "suhu", glukometer: "kurva", "kimia-klinik": "kurva", koagulasi: "kurva", elektrolit: "kurva", immunoassay: "kurva", "urin-analyzer": "kurva", cat: "kurva", hematologi: "kurva",
};
const BACAAN = {
  ekg: "72 bpm", holter: "HR 68 · 2 PVC", "patient-monitor": "HR 72 · SpO₂ 98%", defibrilator: "Shock 200 J", oksimeter: "SpO₂ 98%", smartwatch: "72 bpm",
  tensimeter: "120/80", termometer: "36,8 °C", spirometer: "FEV1/FVC 0,78", kapnograf: "EtCO₂ 38", ctg: "FHR 140", audiometer: "25 dB HL",
  glukometer: "104 mg/dL", inkubator: "36,5 °C", autoklaf: "121 °C · 15 mnt", fototerapi: "35 µW/cm²/nm", ventilator: "Vt 450 mL", "mesin-anestesi": "Sevo 2%",
};
function tahapSinyal(a, b, i, n) {
  let peran = peranBlok(b, a.id);
  const t = (b.id + " " + b.nama).toLowerCase();
  if (i === 0 && (peran === "out" || peran === "proc")) peran = "in"; // blok pertama selalu masukan
  const dasar = DASAR[a.id] || "sinus";
  if (peran === "pow") return "daya";
  if (peran === "data" || dasar === "data") return "data";
  if (peran === "mech") return "mekanik";
  if (dasar === "citra") return peran === "in" || i === 0 ? "citra-mentah" : peran === "out" || i === n - 1 ? "citra-tampil" : peran === "act" ? "aksi" : "citra-olah";
  // Nama tahap pengolahan sinyal lebih spesifik daripada peran umum blok.
  if (/penguat|frontend|\btia\b|pengondisi|amplif/.test(t)) return "kuat";
  if (/filter|praproses|koreksi|bersih/.test(t)) return "bersih";
  if (/\badc\b|akuisisi|sampling|konversi/.test(t)) return "sampel";
  if (peran === "out") return "tampil";
  if (peran === "act") return "aksi";
  if (peran === "in") return "mentah";
  return "olah";
}
const KET_TAHAP = {
  mentah: "Sinyal asli dari tubuh atau sampel masih sangat kecil dan bercampur derau (gerak, jala-jala 50 Hz, pergeseran baseline).",
  kuat: "Sinyal diperkuat ratusan sampai ribuan kali agar bisa diolah. Derau ikut membesar, jadi penguat harus menolak derau mode bersama.",
  bersih: "Derau dibuang: frekuensi di luar pita sinyal disaring sehingga bentuk sinyal terlihat jelas.",
  sampel: "Sinyal analog diambil sampelnya pada frekuensi tertentu dan diubah menjadi angka digital.",
  olah: "Prosesor menghitung ciri penting dari data digital: puncak, frekuensi, atau nilai klinis.",
  tampil: "Hasil disajikan ke tenaga kesehatan: gelombang, angka, dan alarm.",
  aksi: "Komponen ini menghasilkan energi atau gerak yang bekerja pada pasien atau sampel.",
  daya: "Bagian daya dan keselamatan menjaga pasien terpisah dari bahaya listrik.",
  mekanik: "Bagian mekanis membentuk alat dan menyesuaikannya dengan tubuh pengguna.",
  data: "Data dikemas menjadi paket, diamankan, lalu dikirim atau disimpan.",
  "citra-mentah": "Detektor mencatat sinyal mentah (foton, gema, atau cahaya) yang belum berbentuk gambar.",
  "citra-olah": "Data mentah direkonstruksi dan diolah menjadi citra, derau ditekan dan kontras diatur.",
  "citra-tampil": "Citra akhir ditampilkan untuk dibaca dokter atau radiolog.",
};

/* ---------- gelombang dasar (t dalam detik) ---------- */
const gauss = (x, m, s) => Math.exp(-((x - m) ** 2) / (2 * s * s));
const GEL = {
  ekg: (t) => { const p = t % 0.83 / 0.83; return 0.12 * gauss(p, 0.18, 0.025) - 0.12 * gauss(p, 0.36, 0.008) + 1 * gauss(p, 0.39, 0.01) - 0.25 * gauss(p, 0.42, 0.01) + 0.3 * gauss(p, 0.65, 0.04); },
  ppg: (t) => { const p = t % 0.83 / 0.83; return 0.9 * gauss(p, 0.25, 0.08) + 0.35 * gauss(p, 0.55, 0.07) - 0.4; },
  eeg: (t) => 0.5 * Math.sin(2 * Math.PI * 10 * t) * (0.6 + 0.4 * Math.sin(2 * Math.PI * 0.5 * t)) + 0.25 * Math.sin(2 * Math.PI * 4 * t + 1),
  emg: (t) => { const env = Math.max(0, Math.sin(2 * Math.PI * 0.4 * t)) ** 2; return env * (Math.sin(2 * Math.PI * 90 * t) * 0.6 + Math.sin(2 * Math.PI * 143 * t + 2) * 0.4); },
  napas: (t) => Math.sin(2 * Math.PI * 0.25 * t) * 0.8,
  kapno: (t) => { const p = t % 4 / 4; return p < 0.45 ? -0.8 + 1.6 * Math.min(1, Math.max(0, (p - 0.05) / 0.08)) * (0.92 + 0.08 * p) : -0.8 + 1.6 * Math.max(0, 1 - (p - 0.45) / 0.05); },
  tekanan: (t) => { const p = t % 6 / 6; return (1 - p) * 0.9 - 0.45 + Math.sin(2 * Math.PI * 1.2 * t) * 0.18 * gauss(p, 0.5, 0.18); },
  ctg: (t) => 0.3 * Math.sin(2 * Math.PI * 0.3 * t) + 0.15 * Math.sin(2 * Math.PI * 1.7 * t) - 0.6 * gauss(t % 12, 8, 1.2),
  audio: (t) => Math.sin(2 * Math.PI * 6 * t) * 0.5 + Math.sin(2 * Math.PI * 17 * t) * 0.25 * Math.sin(2 * Math.PI * 0.7 * t),
  pulsa: (t) => { const p = t % 0.25 / 0.25; return p < 0.08 ? 0.9 : p < 0.16 ? -0.5 : 0; },
  rf: (t) => Math.sin(2 * Math.PI * 30 * t) * (0.5 + 0.5 * Math.sin(2 * Math.PI * 0.5 * t) ** 2),
  suhu: (t) => Math.tanh(((t % 10) - 3) / 2) * 0.7,
  kurva: (t) => { const p = t % 6 / 6; return 0.8 * (1 - Math.exp(-p * 5)) - 0.4; },
  gerak: (t) => 0.55 * Math.sin(2 * Math.PI * 0.4 * t) + 0.2 * Math.sin(2 * Math.PI * 1.3 * t + 1),
  sinus: (t) => Math.sin(2 * Math.PI * 1.2 * t) * 0.7,
};
// Derau citra: tabel acak tetap, diganti tiap 1/6 detik.
const NZ_N = 26, NZ = Array.from({ length: 8 }, () => Float32Array.from({ length: NZ_N * NZ_N }, Math.random));
const derau = (t) => 0.22 * Math.sin(2 * Math.PI * 50 * t) + 0.25 * Math.sin(2 * Math.PI * 0.3 * t) + 0.16 * (Math.sin(t * 913.7) * Math.cos(t * 377.1));

function breakdownHtml(a) {
  const blok = a.blok || [];
  if (blok.length < 2) return "";
  return `<section class="card bd-card" id="bdCard">
    <div class="section-head" style="padding:22px 22px 6px"><div><h2>Animasi breakdown komponen</h2><span class="sub">Ikuti sinyal dari masukan sampai keluaran. Tiap tahap menyalakan komponennya dan mata kuliah yang dipakai.</span></div>
      <div class="right bd-ctrl"><button class="btn sm" id="bdPrev" title="Tahap sebelumnya">${ico("prev", 16)}</button><button class="btn sm primary" id="bdPlay">${ico("pause", 16)} <span>Jeda</span></button><button class="btn sm" id="bdNext" title="Tahap berikutnya">${ico("next", 16)}</button></div></div>
    <div class="bd-track" style="--n:${blok.length}"><div class="bd-line"><i id="bdFill"></i><span class="bd-pulse" id="bdPulse"></span></div>
      <div class="bd-steps">${blok.map((b, i) => `<button class="bd-step" data-st="${i}" title="${esc(b.fungsi || "")}"><span class="n">${i + 1}</span><span class="l">${esc(b.nama)}</span></button>`).join("")}</div></div>
    <div class="bd-stage">
      <div class="bd-ilus" id="bdIlus">${ilustrasiSvg(a, { cls: "bd" })}</div>
      <div class="bd-scope"><canvas id="bdScope" aria-label="Bentuk sinyal pada tahap ini"></canvas><div class="bd-tag" id="bdTag"></div></div>
      <div class="bd-info" id="bdInfo" aria-live="polite"></div>
    </div>
  </section>`;
}

function bindBreakdown(root, a) {
  const card = $("#bdCard", root);
  if (!card) return;
  const blok = a.blok, n = blok.length;
  const kontrib = (a.kontribusi || []).filter((k) => materiById(k.materi));
  const tahap = blok.map((b, i) => ({ b, part: partFor(a, b), jenis: tahapSinyal(a, b, i, n), mk: kontrib.filter((k) => (k.blok || []).includes(b.id)).sort((x, y) => y.tingkat - x.tingkat) }));
  const dasar = GEL[DASAR[a.id]] || GEL.sinus;
  const canvas = $("#bdScope", card), ctx = canvas.getContext("2d");
  const st = { i: 0, main: !reduceMotion(), terlihat: false, t0: performance.now(), timer: 0 };
  const DUR = 3400;

  const label = { mentah: "Sinyal mentah", kuat: "Setelah penguat", bersih: "Setelah filter", sampel: "Sampel digital", olah: "Hasil olah", tampil: "Ditampilkan", aksi: "Keluaran energi", daya: "Daya dan isolasi", mekanik: "Bagian mekanis", data: "Paket data", "citra-mentah": "Data detektor", "citra-olah": "Rekonstruksi", "citra-tampil": "Citra akhir" };
  const set = (i, user) => {
    st.i = (i + n) % n;
    const T = tahap[st.i];
    $$(".bd-step", card).forEach((s, j) => { s.classList.toggle("on", j === st.i); s.classList.toggle("lewat", j < st.i); });
    const x = n > 1 ? (st.i / (n - 1)) * 100 : 0;
    $("#bdFill", card).style.width = x + "%";
    $("#bdPulse", card).style.left = x + "%";
    $$("#bdIlus .part", card).forEach((p) => p.classList.toggle("on", p.dataset.part === T.part));
    $("#bdTag", card).textContent = label[T.jenis] || "";
    $("#bdInfo", card).innerHTML = `<small>Tahap ${st.i + 1} dari ${n}</small><h3>${esc(T.b.nama)}</h3><p>${esc(T.b.fungsi || "")}</p>
      <p class="bd-ket">${esc(KET_TAHAP[T.jenis] || "")}</p>
      ${T.mk.length ? `<div class="bd-mk"><b>Mata kuliah di tahap ini</b>${T.mk.slice(0, 6).map((k, j) => { const m = materiById(k.materi); return `<a class="bd-chip-mk t${k.tingkat}" href="#/materi/${esc(m.id)}" style="--bd:${BIDANG[bidangOf(m)].warna};--i:${j}" title="${esc(k.peran || "")}"><i></i>${esc(m.nama)}</a>`; }).join("")}</div>` : `<p class="muted" style="font-size:.85rem">Belum ada mata kuliah yang dikaitkan khusus ke blok ini.</p>`}`;
    $("#bdInfo", card).classList.remove("swap"); void $("#bdInfo", card).offsetWidth; $("#bdInfo", card).classList.add("swap");
    st.t0 = performance.now();
    if (user) jadwal();
    if (reduceMotion()) gambar(performance.now());
  };
  const jadwal = () => { clearTimeout(st.timer); if (st.main && st.terlihat) st.timer = setTimeout(() => set(st.i + 1), DUR); };
  const setMain = (v) => {
    st.main = v;
    $("#bdPlay", card).innerHTML = v ? `${ico("pause", 16)} <span>Jeda</span>` : `${ico("play", 16)} <span>Putar</span>`;
    card.classList.toggle("jalan", v);
    jadwal();
  };

  /* osiloskop */
  const ukur = () => {
    const r = canvas.getBoundingClientRect(), d = window.devicePixelRatio || 1;
    canvas.width = Math.max(1, r.width * d); canvas.height = Math.max(1, r.height * d);
    ctx.setTransform(d, 0, 0, d, 0, 0);
    return r;
  };
  let box = ukur();
  const css = getComputedStyle(document.documentElement);
  const warna = () => ({ grid: css.getPropertyValue("--border").trim() || "#ddd", line: "#1f9d55", acc: "#2483ff", warn: "#fe7b02", text: css.getPropertyValue("--text-2").trim() || "#555" });
  function gambar(now) {
    const W = box.width, H = box.height;
    if (!W || !H) return;
    const c = warna(), T = tahap[st.i], tt = now / 1000, j = T.jenis;
    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = c.grid; ctx.lineWidth = 1; ctx.globalAlpha = 0.6;
    for (let x = 0; x < W; x += 24) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
    for (let y = 0; y < H; y += 24) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
    ctx.globalAlpha = 1;
    const mid = H / 2, span = 3; // 3 detik terakhir
    const xOf = (k) => (k / W) * span;
    const garis = (f, opt = {}) => {
      ctx.beginPath(); ctx.strokeStyle = opt.c || c.line; ctx.lineWidth = opt.w || 2;
      for (let x = 0; x <= W; x += 1.5) { const y = mid - f(tt - span + xOf(x)) * H * (opt.g || 0.36); x ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }
      ctx.stroke();
    };
    if (j === "mentah") garis((t) => dasar(t) * 0.45 + derau(t) * 0.55, { c: c.warn, w: 1.4 });
    else if (j === "kuat") garis((t) => dasar(t) * 0.95 + derau(t) * 0.45, { c: c.warn, w: 1.6 });
    else if (j === "bersih") garis(dasar, { w: 2.2 });
    else if (j === "sampel") {
      const fs = 18; ctx.fillStyle = c.acc; ctx.strokeStyle = c.acc;
      for (let x = (W - ((tt * fs * W) / span) % (W / (fs * span))) % (W / (fs * span)); x <= W; x += W / (fs * span)) {
        const y = mid - dasar(tt - span + xOf(x)) * H * 0.36;
        ctx.globalAlpha = 0.35; ctx.beginPath(); ctx.moveTo(x, mid); ctx.lineTo(x, y); ctx.stroke(); ctx.globalAlpha = 1;
        ctx.beginPath(); ctx.arc(x, y, 2.6, 0, 7); ctx.fill();
      }
    } else if (j === "olah" || j === "tampil") {
      garis(dasar, { w: 2.2 });
      // Tandai puncak yang "terdeteksi" prosesor.
      ctx.fillStyle = c.acc;
      let prev = 0, prev2 = 0;
      for (let x = 0; x <= W; x += 2) { const v = dasar(tt - span + xOf(x)); if (prev > prev2 && prev > v && prev > 0.45) { const px = x - 2, py = mid - prev * H * 0.36 - 10; ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px - 5, py - 8); ctx.lineTo(px + 5, py - 8); ctx.fill(); } prev2 = prev; prev = v; }
      if (j === "tampil") { ctx.fillStyle = c.text; ctx.font = "700 20px " + (css.getPropertyValue("--font-display") || "sans-serif"); ctx.textAlign = "right"; ctx.fillText(BACAAN[a.id] || a.singkatan || "", W - 12, 28); ctx.textAlign = "left"; }
    } else if (j === "aksi") {
      const f = DASAR[a.id] && GEL[DASAR[a.id]] && ["pulsa", "rf"].includes(DASAR[a.id]) ? dasar : (t) => { const p = t % 0.6 / 0.6; return p < 0.3 ? 0.8 : -0.1; };
      garis(f, { c: c.warn, w: 2.4 });
    } else if (j === "daya") {
      ctx.strokeStyle = c.acc; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(0, mid - H * 0.25); ctx.lineTo(W * 0.42, mid - H * 0.25); ctx.stroke();
      ctx.setLineDash([6, 6]); ctx.strokeStyle = c.warn; ctx.beginPath(); ctx.moveTo(W / 2, 10); ctx.lineTo(W / 2, H - 10); ctx.stroke(); ctx.setLineDash([]);
      ctx.strokeStyle = c.line; ctx.beginPath(); ctx.moveTo(W * 0.58, mid + H * 0.15); ctx.lineTo(W, mid + H * 0.15); ctx.stroke();
      ctx.fillStyle = c.text; ctx.font = "600 12px sans-serif"; ctx.fillText("Jala-jala / catu", 8, mid - H * 0.25 - 8); ctx.fillText("Sisi pasien", W * 0.58 + 6, mid + H * 0.15 - 8);
    } else if (j === "data") {
      ctx.fillStyle = c.acc;
      for (let k = 0; k < 7; k++) { const x = ((tt * 90 + k * (W / 6)) % (W + 40)) - 40; ctx.globalAlpha = 0.85; ctx.fillRect(x, mid - 12, 30, 24); ctx.globalAlpha = 1; ctx.fillStyle = "#fff"; ctx.font = "700 10px monospace"; ctx.fillText(((k * 37 + 11) % 256).toString(16).padStart(2, "0").toUpperCase(), x + 7, mid + 4); ctx.fillStyle = c.acc; }
    } else if (j === "mekanik") {
      ctx.strokeStyle = c.acc; ctx.lineWidth = 2; const r = Math.min(W, H) * 0.3, a0 = tt * 0.8;
      ctx.beginPath(); for (let k = 0; k <= 24; k++) { const ang = a0 + (k / 24) * Math.PI * 2, rr = r * (k % 2 ? 0.82 : 1); const x = W / 2 + Math.cos(ang) * rr, y = mid + Math.sin(ang) * rr; k ? ctx.lineTo(x, y) : ctx.moveTo(x, y); } ctx.stroke();
      ctx.beginPath(); ctx.arc(W / 2, mid, r * 0.3, 0, 7); ctx.stroke();
    } else {
      // Citra: sel piksel dari derau acak (mentah) → fantom bersih (olah/tampil).
      const N = NZ_N, cw = Math.min(W - 16, H - 16) / N, ch = cw, ox = (W - cw * N) / 2, oy = (H - ch * N) / 2, mul = j === "citra-mentah" ? 0.9 : j === "citra-olah" ? 0.35 : 0.06, fr = NZ[Math.floor(tt * 6) % NZ.length];
      for (let yy = 0; yy < N; yy++) for (let xx = 0; xx < N; xx++) {
        const dx = (xx - N / 2) / (N / 2), dy = (yy - N / 2) / (N / 2);
        let v = dx * dx / 0.8 + dy * dy / 0.95 < 1 ? 0.55 : 0.05;
        if ((dx + 0.3) ** 2 + (dy + 0.1) ** 2 < 0.05) v = 0.95;
        if ((dx - 0.35) ** 2 + (dy - 0.2) ** 2 < 0.03) v = 0.2;
        v = Math.max(0, Math.min(1, v * (1 - mul * 0.5) + (fr[yy * N + xx] - 0.5) * mul));
        ctx.fillStyle = j === "citra-tampil" ? `hsl(${210 - v * 180} 80% ${20 + v * 55}%)` : `rgb(${v * 255 | 0},${v * 255 | 0},${v * 255 | 0})`;
        ctx.fillRect(ox + xx * cw, oy + yy * ch, cw + 0.5, ch + 0.5);
      }
    }
    // Garis waktu kecil: sisa durasi tahap.
    if (st.main) { const p = Math.min(1, (now - st.t0) / DUR); ctx.fillStyle = c.acc; ctx.globalAlpha = 0.5; ctx.fillRect(0, H - 3, W * p, 3); ctx.globalAlpha = 1; }
  }
  const loop = (now) => {
    if (!document.body.contains(canvas)) return;
    if (st.terlihat && !reduceMotion()) gambar(now);
    requestAnimationFrame(loop);
  };

  card.addEventListener("click", (e) => {
    const s = e.target.closest("[data-st]"); if (s) { set(+s.dataset.st, true); return; }
    if (e.target.closest("#bdPrev")) set(st.i - 1, true);
    if (e.target.closest("#bdNext")) set(st.i + 1, true);
    if (e.target.closest("#bdPlay")) setMain(!st.main);
  });
  card.addEventListener("mouseenter", () => clearTimeout(st.timer));
  card.addEventListener("mouseleave", jadwal);
  new ResizeObserver(() => { box = ukur(); gambar(performance.now()); }).observe(canvas);
  new IntersectionObserver(([en]) => { st.terlihat = en.isIntersecting; jadwal(); }, { threshold: 0.25 }).observe(card);
  set(0);
  setMain(st.main);
  gambar(performance.now());
  requestAnimationFrame(loop);
}
