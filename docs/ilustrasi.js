"use strict";

/* =========================================================
   Ilustrasi alat (SVG datar) yang bisa "dipecah" per komponen.
   Tiap arketipe = beberapa bagian; saat dipecah, tiap bagian
   bergeser sejauh (dx, dy) seperti gambar exploded view.
   viewBox 0 0 320 240. Warna lewat kelas agar ikut tema.
   ========================================================= */

const IL = {
  // Monitor biopotensial (EKG/EEG): layar, papan sirkuit, casing, kabel + elektroda
  monitor: [
    ["casing", 0, 26, `<rect class="b" x="58" y="40" width="204" height="138" rx="16"/><circle class="m" cx="236" cy="164" r="5"/><circle class="m" cx="220" cy="164" r="5"/><rect class="m" x="76" y="160" width="60" height="8" rx="4"/>`],
    ["papan", 0, -4, `<rect class="pcb" x="82" y="70" width="156" height="70" rx="6"/><rect class="ic" x="96" y="84" width="30" height="22" rx="3"/><rect class="ic" x="140" y="90" width="18" height="18" rx="3"/><rect class="ic" x="172" y="82" width="46" height="14" rx="3"/><path class="trace" d="M126 95h14M158 99h14M96 120h120"/>`],
    ["layar", 0, -42, `<rect class="s" x="74" y="54" width="172" height="100" rx="8"/><path class="w" d="M84 110h30l6-18 8 34 7-30 5 14h26l6-18 8 34 7-30 5 14h34"/>`],
    ["kabel", -38, 30, `<path class="c" d="M58 120c-30 0-34 40-12 62M46 182l-18 22M46 182l2 26M46 182l22 18"/><circle class="a" cx="26" cy="208" r="8"/><circle class="a" cx="48" cy="214" r="8"/><circle class="a" cx="70" cy="204" r="8"/>`],
  ],
  // Oksimeter jepit jari
  klip: [
    ["bawah", 0, 30, `<path class="b" d="M70 130h170a24 24 0 0 1 0 48H70z"/><rect class="m" x="186" y="148" width="40" height="10" rx="5"/>`],
    ["sensor", 0, 6, `<circle class="led" cx="140" cy="124" r="7"/><circle class="led ir" cx="160" cy="124" r="7"/><rect class="ic" x="130" y="136" width="40" height="8" rx="3"/>`],
    ["jari", -60, 0, `<path class="skin" d="M20 112h120a16 16 0 0 1 0 32H20z"/>`],
    ["atas", 0, -36, `<path class="b" d="M70 60h170a24 24 0 0 1 24 24v24H70z"/><rect class="s" x="150" y="68" width="96" height="34" rx="6"/><text class="t" x="160" y="92">98%</text><text class="t sm" x="208" y="92">72</text>`],
  ],
  // Tensimeter: manset, selang, unit
  manset: [
    ["manset", -40, 10, `<rect class="a soft" x="20" y="70" width="110" height="80" rx="14"/><path class="m" d="M30 86h90M30 134h90" stroke-width="3"/>`],
    ["selang", 0, 40, `<path class="c" d="M130 110c40 0 40 70 70 70h20"/>`],
    ["unit", 30, -10, `<rect class="b" x="170" y="48" width="130" height="150" rx="18"/><rect class="s" x="186" y="64" width="98" height="64" rx="8"/><text class="t" x="196" y="94">120</text><text class="t sm" x="196" y="116">80  72♥</text><circle class="a" cx="235" cy="164" r="16"/>`],
    ["pompa", 30, 46, `<rect class="pcb" x="196" y="140" width="40" height="22" rx="4"/><circle class="m" cx="250" cy="151" r="9"/>`],
  ],
  // USG: monitor, konsol, probe
  usg: [
    ["layar", 0, -36, `<rect class="b" x="90" y="16" width="160" height="104" rx="12"/><rect class="s" x="102" y="26" width="136" height="84" rx="6"/><path class="fan" d="M170 36 120 104h100z"/>`],
    ["konsol", 0, 6, `<rect class="b" x="80" y="128" width="180" height="40" rx="10"/><circle class="m" cx="210" cy="148" r="10"/><rect class="m" x="100" y="140" width="80" height="6" rx="3"/><rect class="m" x="100" y="152" width="60" height="6" rx="3"/>`],
    ["badan", 0, 40, `<rect class="b" x="130" y="170" width="80" height="50" rx="8"/><circle class="m" cx="140" cy="226" r="7"/><circle class="m" cx="200" cy="226" r="7"/>`],
    ["probe", -60, 10, `<path class="c" d="M80 150c-30 0-40 20-46 40"/><path class="a" d="M20 186h28l-4 30H24z"/><rect class="m" x="22" y="214" width="24" height="6" rx="3"/>`],
  ],
  // X-ray: tabung + kolimator, meja, detektor, konsol
  xray: [
    ["tabung", 0, -40, `<rect class="m" x="150" y="10" width="14" height="40" rx="4"/><rect class="b" x="110" y="40" width="96" height="40" rx="12"/><circle class="a" cx="158" cy="60" r="10"/>`],
    ["kolimator", 0, -16, `<path class="b" d="M136 84h44l-6 22h-32z"/><path class="beam" d="M142 108h32l40 72H102z"/>`],
    ["meja", 0, 18, `<rect class="b" x="40" y="168" width="240" height="14" rx="7"/><path class="skin" d="M90 154c20-10 120-10 140 0v14H90z"/><rect class="m" x="150" y="182" width="16" height="40"/>`],
    ["detektor", 0, 44, `<rect class="s" x="100" y="190" width="116" height="12" rx="4"/>`],
    ["konsol", 50, 0, `<rect class="b" x="254" y="70" width="56" height="74" rx="10"/><rect class="s" x="262" y="80" width="40" height="26" rx="4"/><circle class="m" cx="282" cy="124" r="6"/>`],
  ],
  // CT/MRI: gantry cincin + meja + komponen dalam
  gantry: [
    ["gantry", 30, -10, `<rect class="b" x="150" y="20" width="150" height="180" rx="40"/><circle class="hole" cx="225" cy="110" r="44"/>`],
    ["cincin", 60, -40, `<circle class="rg" cx="225" cy="110" r="62"/><circle class="a" cx="225" cy="44" r="8"/><rect class="ic" x="212" y="168" width="26" height="8" rx="3"/>`],
    ["meja", -50, 20, `<rect class="b" x="20" y="132" width="210" height="16" rx="8"/><path class="skin" d="M40 118c30-12 120-12 160 0v14H40z"/><rect class="m" x="70" y="148" width="20" height="60"/><rect class="m" x="40" y="206" width="80" height="10" rx="5"/>`],
    ["konsol", -10, 44, `<rect class="b" x="20" y="20" width="90" height="62" rx="10"/><rect class="s" x="28" y="28" width="74" height="40" rx="5"/><circle class="w2" cx="65" cy="48" r="12"/>`],
  ],
  // Ventilator
  ventilator: [
    ["layar", 0, -36, `<rect class="b" x="100" y="14" width="140" height="92" rx="12"/><rect class="s" x="112" y="24" width="116" height="72" rx="6"/><path class="w" d="M120 70c10-30 20-30 30 0s20 30 30 0 20-30 30 0"/>`],
    ["unit", 0, 8, `<rect class="b" x="90" y="112" width="160" height="90" rx="14"/><circle class="m" cx="122" cy="140" r="9"/><circle class="m" cx="150" cy="140" r="9"/><rect class="pcb" x="176" y="128" width="58" height="34" rx="4"/>`],
    ["selang", -50, 20, `<path class="c thick" d="M96 170c-40 0-56 20-56 44M96 186c-30 0-40 10-40 28"/><path class="a" d="M30 210h36v14H30z"/>`],
    ["humidifier", 60, 30, `<rect class="glass" x="256" y="150" width="44" height="60" rx="8"/><path class="water" d="M260 182h36v24h-36z"/>`],
  ],
  // Pompa infus / suntik
  pompa: [
    ["kantong", 0, -40, `<path class="m" d="M160 4v14"/><path class="glass" d="M130 18h60l-6 60h-48z"/><path class="water" d="M134 44h52l-4 32h-44z"/>`],
    ["selang", -40, 0, `<path class="c" d="M160 78c0 30-40 30-40 60s40 40 40 70"/><circle class="drop" cx="160" cy="88" r="4"/>`],
    ["unit", 30, 10, `<rect class="b" x="150" y="100" width="140" height="100" rx="14"/><rect class="s" x="166" y="114" width="70" height="36" rx="6"/><text class="t sm" x="174" y="138">25 mL/h</text><circle class="a" cx="262" cy="132" r="12"/>`],
    ["motor", 30, 50, `<rect class="pcb" x="170" y="160" width="100" height="26" rx="6"/><circle class="m" cx="190" cy="173" r="8"/><circle class="m" cx="214" cy="173" r="8"/><circle class="m" cx="238" cy="173" r="8"/>`],
  ],
  // Defibrilator / AED
  aed: [
    ["casing", 0, 24, `<rect class="b" x="80" y="40" width="160" height="150" rx="22"/><circle class="danger" cx="160" cy="150" r="20"/><path class="bolt" d="M162 136l-10 16h10l-4 14 12-18h-10z"/>`],
    ["layar", 0, -30, `<rect class="s" x="104" y="56" width="112" height="56" rx="8"/><path class="w" d="M112 86h20l5-14 6 26 5-20 5 8h40"/>`],
    ["kapasitor", 70, 6, `<rect class="a" x="244" y="86" width="34" height="56" rx="10"/><rect class="m" x="252" y="80" width="6" height="8"/><rect class="m" x="264" y="80" width="6" height="8"/>`],
    ["pad", -70, 20, `<path class="c" d="M80 160c-30 0-40 20-40 40"/><rect class="pad" x="14" y="190" width="46" height="30" rx="8"/><rect class="pad" x="64" y="196" width="46" height="30" rx="8"/>`],
  ],
  // Inkubator bayi
  inkubator: [
    ["kubah", 0, -40, `<path class="glass" d="M60 110c0-60 200-60 200 0z"/><circle class="m" cx="100" cy="96" r="10"/><circle class="m" cx="220" cy="96" r="10"/>`],
    ["bayi", 0, -8, `<ellipse class="skin" cx="160" cy="108" rx="34" ry="12"/><circle class="skin" cx="122" cy="104" r="10"/>`],
    ["kasur", 0, 14, `<rect class="b" x="56" y="118" width="208" height="20" rx="8"/>`],
    ["unit", 0, 44, `<rect class="b" x="70" y="142" width="180" height="56" rx="10"/><rect class="s" x="86" y="152" width="60" height="30" rx="5"/><text class="t sm" x="92" y="172">36.5°</text><rect class="pcb" x="160" y="152" width="74" height="30" rx="4"/><path class="heat" d="M170 160q4-6 0-12M186 160q4-6 0-12M202 160q4-6 0-12"/>`],
  ],
  // Hemodialisis
  dialisis: [
    ["badan", 0, 20, `<rect class="b" x="110" y="20" width="110" height="196" rx="16"/><rect class="m" x="126" y="140" width="78" height="60" rx="8"/>`],
    ["layar", 0, -34, `<rect class="s" x="122" y="30" width="86" height="56" rx="6"/><path class="w" d="M130 64h18l6-12 6 22 6-14h30"/>`],
    ["pompa", -60, 0, `<circle class="a" cx="70" cy="110" r="22"/><circle class="m" cx="70" cy="110" r="8"/><path class="c" d="M48 110c-20 0-30 20-30 50"/>`],
    ["dialiser", 70, 0, `<rect class="glass" x="244" y="70" width="28" height="100" rx="12"/><path class="fiber" d="M252 80v80M258 80v80M264 80v80"/>`],
  ],
  // Laptop / perangkat lunak
  laptop: [
    ["layar", 0, -30, `<rect class="b" x="60" y="26" width="200" height="130" rx="12"/><rect class="s" x="72" y="36" width="176" height="110" rx="6"/><path class="brain" d="M130 92c-14-30 30-46 40-26 18-18 46 8 30 30 10 22-26 36-36 20-14 14-46 0-34-24z"/>`],
    ["data", 70, -6, `<rect class="pcb" x="250" y="60" width="54" height="70" rx="6"/><path class="trace" d="M258 76h38M258 90h30M258 104h38M258 118h24"/>`],
    ["alas", 0, 30, `<path class="b" d="M40 160h240l16 26H24z"/><rect class="m" x="140" y="168" width="40" height="8" rx="4"/>`],
    ["sinyal", -70, 0, `<path class="w2" d="M10 90h10l6-16 8 30 6-22 6 8h12"/><path class="w2" d="M10 120h12l6-10 6 20 6-14h14"/>`],
  ],
  // Koil TMS
  koil: [
    ["koil", 0, -30, `<circle class="rg" cx="128" cy="70" r="36"/><circle class="rg" cx="192" cy="70" r="36"/><rect class="b" x="148" y="100" width="24" height="50" rx="8"/>`],
    ["kepala", 0, 24, `<path class="skin" d="M110 230c0-60 10-100 50-100s50 40 50 100z"/><path class="brain" d="M130 170c-6-18 18-26 26-14 10-10 26 4 18 18 6 12-14 20-20 10-8 8-26 0-24-14z"/>`],
    ["unit", 80, 20, `<rect class="b" x="234" y="110" width="76" height="100" rx="12"/><rect class="s" x="244" y="122" width="56" height="30" rx="5"/><rect class="a" x="246" y="164" width="52" height="34" rx="8"/>`],
    ["kabel", 40, -10, `<path class="c thick" d="M160 150c40 0 50 0 74 10"/>`],
  ],
  // Stimulator (TENS/EMS/ECT)
  stimulator: [
    ["unit", 0, -20, `<rect class="b" x="100" y="40" width="120" height="150" rx="20"/><rect class="s" x="116" y="56" width="88" height="44" rx="6"/><path class="w" d="M122 86h8v-16h6v16h8v-16h6v16h8v-16h6v16h8"/><circle class="a" cx="140" cy="140" r="14"/><circle class="m" cx="184" cy="140" r="10"/>`],
    ["papan", 60, 0, `<rect class="pcb" x="230" y="70" width="70" height="90" rx="6"/><rect class="ic" x="244" y="84" width="20" height="20" rx="3"/><rect class="ic" x="270" y="110" width="20" height="30" rx="3"/>`],
    ["kabel", -40, 30, `<path class="c" d="M120 190c-20 20-60 10-80 30M160 190c-10 20-20 26-30 34"/>`],
    ["pad", -60, 40, `<rect class="pad" x="14" y="196" width="50" height="34" rx="8"/><rect class="pad" x="104" y="200" width="50" height="34" rx="8"/>`],
  ],
  // Konsol terapi dengan lengan aplikator (diatermi, terapi US)
  konsol: [
    ["konsol", 0, 20, `<rect class="b" x="140" y="90" width="150" height="120" rx="16"/><rect class="s" x="156" y="104" width="118" height="44" rx="6"/><circle class="m" cx="180" cy="176" r="12"/><circle class="a" cx="250" cy="176" r="12"/>`],
    ["generator", 30, 56, `<rect class="pcb" x="170" y="190" width="90" height="22" rx="4"/><path class="w2" d="M176 201c6-8 10 8 16 0s10 8 16 0 10 8 16 0 10 8 16 0"/>`],
    ["lengan", -30, -20, `<path class="c thick" d="M150 110C110 100 90 60 80 40"/><rect class="m" x="70" y="26" width="24" height="20" rx="6"/>`],
    ["aplikator", -70, -10, `<path class="a" d="M30 40h50a20 20 0 0 1 0 40H30z"/><path class="wave" d="M20 96q10 -10 20 0t20 0t20 0"/>`],
  ],
  // Brace skoliosis
  brace: [
    ["tubuh", 0, 0, `<path class="skin" d="M120 20c-14 30-16 60-10 90-6 40-6 70 0 110h100c6-40 6-70 0-110 6-30 4-60-10-90z"/><path class="spine" d="M160 30c-14 30 14 60 0 90s14 60 0 90"/>`],
    ["depan", -60, 0, `<path class="a soft" d="M108 70c20-8 84-8 104 0l6 90c-20 10-96 10-116 0z"/>`],
    ["bantalan", 60, -10, `<rect class="pad" x="196" y="100" width="22" height="40" rx="8"/><rect class="pad" x="104" y="80" width="22" height="34" rx="8"/>`],
    ["tali", 0, 40, `<path class="c thick" d="M104 150h112M104 170h112"/>`],
  ],
  // Perangkat genggam (termometer, glukometer)
  genggam: [
    ["casing", 0, 20, `<rect class="b" x="110" y="30" width="100" height="180" rx="30"/><circle class="a" cx="160" cy="176" r="14"/>`],
    ["layar", 0, -26, `<rect class="s" x="124" y="50" width="72" height="56" rx="8"/><text class="t" x="132" y="86">36.8</text>`],
    ["papan", 66, 0, `<rect class="pcb" x="232" y="70" width="56" height="90" rx="6"/><rect class="ic" x="244" y="84" width="30" height="20" rx="3"/><rect class="ic" x="248" y="120" width="22" height="22" rx="3"/>`],
    ["sensor", -70, -10, `<rect class="m" x="30" y="40" width="50" height="16" rx="8"/><rect class="strip" x="40" y="70" width="18" height="60" rx="3"/><circle class="drop" cx="49" cy="78" r="4"/>`],
  ],
  // Analyzer laboratorium
  analyzer: [
    ["casing", 0, 26, `<rect class="b" x="40" y="60" width="240" height="140" rx="16"/><rect class="m" x="56" y="170" width="120" height="10" rx="5"/>`],
    ["layar", 70, -20, `<rect class="s" x="196" y="74" width="68" height="70" rx="6"/><path class="bars" d="M206 132v-18M218 132v-30M230 132v-12M242 132v-24M254 132v-36"/>`],
    ["rak", -60, -26, `<rect class="m" x="56" y="40" width="120" height="16" rx="4"/><rect class="glass" x="66" y="12" width="12" height="40" rx="5"/><rect class="glass" x="90" y="12" width="12" height="40" rx="5"/><rect class="glass" x="114" y="12" width="12" height="40" rx="5"/><rect class="glass" x="138" y="12" width="12" height="40" rx="5"/><path class="water" d="M68 34h8v16h-8zM92 30h8v20h-8zM116 36h8v14h-8zM140 32h8v18h-8z"/>`],
    ["optik", -10, 6, `<rect class="pcb" x="64" y="88" width="110" height="60" rx="6"/><circle class="led" cx="84" cy="118" r="7"/><path class="beam2" d="M92 118h44"/><rect class="glass" x="112" y="104" width="12" height="28" rx="3"/><rect class="ic" x="140" y="108" width="20" height="20" rx="3"/>`],
  ],
  // Sentrifus
  sentrifus: [
    ["tutup", 0, -44, `<path class="glass" d="M70 70c0-30 180-30 180 0z"/>`],
    ["rotor", 0, -10, `<ellipse class="m" cx="160" cy="92" rx="70" ry="16"/><rect class="glass" x="100" y="78" width="12" height="26" rx="5"/><rect class="glass" x="208" y="78" width="12" height="26" rx="5"/><rect class="glass" x="154" y="74" width="12" height="26" rx="5"/>`],
    ["badan", 0, 24, `<rect class="b" x="60" y="100" width="200" height="100" rx="20"/><rect class="s" x="84" y="130" width="70" height="30" rx="5"/><text class="t sm" x="90" y="150">4000 rpm</text><circle class="a" cx="220" cy="146" r="14"/>`],
    ["motor", 0, 56, `<rect class="pcb" x="130" y="196" width="60" height="24" rx="6"/><circle class="m" cx="160" cy="208" r="8"/>`],
  ],
  // Mikroskop
  mikroskop: [
    ["okuler", -10, -36, `<rect class="m" x="138" y="10" width="26" height="40" rx="6" transform="rotate(-20 151 30)"/>`],
    ["tubuh", 0, -10, `<path class="b" d="M120 50h60l10 40h-60z"/><rect class="m" x="150" y="86" width="20" height="34" rx="4"/><path class="b" d="M210 60c30 30 30 110 0 140h-24c24-36 24-104 0-130z"/>`],
    ["meja", 0, 18, `<rect class="b" x="100" y="128" width="120" height="12" rx="4"/><rect class="glass" x="134" y="122" width="52" height="6" rx="2"/>`],
    ["cahaya", 0, 46, `<rect class="b" x="80" y="196" width="160" height="24" rx="8"/><circle class="led" cx="160" cy="176" r="10"/><path class="beam2" d="M160 166v-24"/>`],
  ],
};

// Gradien kategori dipakai sebagai warna aksen ilustrasi.
function ilustrasiSvg(a, opt = {}) {
  const parts = IL[a.ilustrasi] || IL.monitor;
  const gid = "ilg-" + Math.random().toString(36).slice(2, 8);
  const stops = (gradOf(a.kategori).match(/#[0-9a-f]{6}/gi) || ["#82bcff", "#2483ff"]);
  return `<svg class="ilus${opt.cls ? " " + opt.cls : ""}" viewBox="0 0 320 240" role="img" aria-label="Ilustrasi ${esc(a.nama)}">
    <defs><linearGradient id="${gid}" x1="0" y1="0" x2="1" y2="1">${stops.map((c, i) => `<stop offset="${i / Math.max(1, stops.length - 1)}" stop-color="${c}"/>`).join("")}</linearGradient></defs>
    <g style="--acc:url(#${gid})">${parts.map(([n, dx, dy, svg], i) => `<g class="part" data-part="${n}" style="--dx:${dx}px;--dy:${dy}px;--i:${i}">${svg}</g>`).join("")}</g></svg>`;
}

const ILNAMA = {
  monitor: "Monitor biopotensial (EKG/EEG)", klip: "Klip jari (oksimeter)", manset: "Manset + unit (tensimeter)", usg: "Ultrasonografi", xray: "Sinar-X",
  gantry: "Gantry (CT/MRI)", ventilator: "Ventilator", pompa: "Pompa infus", aed: "Defibrilator", inkubator: "Inkubator bayi", dialisis: "Mesin dialisis",
  laptop: "Perangkat lunak / laptop", koil: "Koil stimulator (TMS)", stimulator: "Stimulator listrik", konsol: "Konsol terapi", brace: "Brace / ortosis",
  genggam: "Alat genggam", analyzer: "Analyzer laboratorium", sentrifus: "Sentrifus", mikroskop: "Mikroskop",
};

// Kotak gambar: foto milik pengguna bila ada, kalau tidak ilustrasi.
function gambarAlat(a, opt = {}) {
  if (a.gambar && gambarUrl(a.gambar)) return `<img class="alat-foto${opt.cls ? " " + opt.cls : ""}" src="${esc(gambarUrl(a.gambar))}" alt="${esc(a.nama)}" onerror="this.replaceWith(document.createRange().createContextualFragment(this.dataset.fb))" data-fb="${esc(ilustrasiSvg(a, opt))}">`;
  return ilustrasiSvg(a, opt);
}
