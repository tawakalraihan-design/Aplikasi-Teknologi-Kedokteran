// Menguji semua rumus ($...$ dan $$...$$) dengan KaTeX yang sama seperti di aplikasi (web/katex).
// Masukan: JSON [[asal, teks], ...] dari stdin. Keluar dengan kode 1 bila ada rumus gagal dirender.
const path = require("path");
const katex = require(path.join(__dirname, "..", "..", "web", "katex", "katex.min.js"));
let masuk = "";
process.stdin.on("data", (d) => (masuk += d));
process.stdin.on("end", () => {
  const daftar = JSON.parse(masuk);
  const re = /\$\$([\s\S]+?)\$\$|\$([^$]+?)\$/g;
  let n = 0, gagal = [];
  for (const [asal, teks] of daftar) {
    const sisa = teks.replace(re, "");
    if (sisa.includes("$")) gagal.push(`${asal}: tanda $ tidak berpasangan → ${teks.slice(0, 80)}`);
    for (const m of teks.matchAll(re)) {
      n++;
      try { katex.renderToString(m[1] || m[2], { displayMode: !!m[1], throwOnError: true, strict: "ignore" }); }
      catch (e) { gagal.push(`${asal}: ${e.message.slice(0, 160)}`); }
    }
  }
  if (gagal.length) { console.log(gagal.join("\n")); process.exit(1); }
  console.log(`KaTeX: ${n} rumus terender tanpa galat.`);
});
