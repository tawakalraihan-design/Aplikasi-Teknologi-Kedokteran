"""Menulis Referensi-v1.4.md (12 buku folder Referensi, per bab) dan
Kisah-Deep-Learning-Oralytic.md (kisah lengkap untuk dibaca di luar aplikasi).

Pemakaian: python3 tools/v5/tulis_md.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DD = os.path.join(ROOT, "defaultdata")


def load(n):
    return json.load(open(os.path.join(DD, n + ".json"), encoding="utf-8"))


ref, alat, materi, soal = load("referensi"), load("alat"), load("materi"), load("soal")
A = {a["id"]: a for a in alat}
M = {m["id"]: m for m in materi}
pus = [r for r in ref if r["jenis"] == "pustaka"]

out = ["# Referensi Teknologi Kedokteran v1.4: 12 buku di folder Referensi", "",
       "Buku-buku di folder `Referensi` (di samping `TeknologiKedokteran.exe`) sudah diolah ke aplikasi. "
       "Di aplikasi: menu **Referensi → Buku di folder Referensi**, lalu klik **N bab dengan ringkasan**. "
       "Tiap bab punya ringkasan berbahasa Indonesia, halaman PDF, alat, dan mata kuliah terkait; bab yang membahas sebuah alat "
       "juga muncul di halaman alat itu (panel *Bacaan dari buku Referensi*). Nomor halaman = nomor halaman file PDF.", "",
       "Total %d buku, %d bab, %d soal latihan. Daftar referensi lain (buku teks, standar, jurnal, dataset) tetap di `Referensi-v1.3.md`."
       % (len(pus), sum(len(r["bab"]) for r in pus), sum(1 for q in soal if q.get("pustaka"))), ""]
for r in pus:
    out += ["## %s" % r["judul"], "",
            "%s · %s · %s · %d halaman · `%s`" % (r["penulis"], r["penerbit"], r["tahun"], r["halaman"], r["file"]), "",
            r["ket"], ""]
    al = ", ".join(A[x]["singkatan"] or A[x]["nama"] for x in r["alat"] if x in A)
    if al:
        out += ["Alat: " + al, ""]
    out += ["| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |", "|---|---|---|---|---|---|"]
    for b in r["bab"]:
        out.append("| %d | %s<br>*%s* | %d–%d | %s | %s | %s |" % (
            b["no"], b["judul"], b["asli"], b["hal"][0], b["hal"][1], b["ringkas"],
            ", ".join(A[x]["singkatan"] or A[x]["nama"] for x in b["alat"] if x in A),
            ", ".join(M[x]["nama"] for x in b["materi"] if x in M)))
    out.append("")
open(os.path.join(ROOT, "Referensi-v1.4.md"), "w", encoding="utf-8").write("\n".join(out))

k = load("kisah")[0]
out = ["# %s" % k["judul"], "", k["ringkasan"], "", "Sumber: `%s` (hanya dibaca, tidak diubah)." % k["sumber"], "",
       "Setiap bab memakai pola yang sama:", ""] + ["%d. %s" % (i + 1, p) for i, p in enumerate(k["pola"])] + [
       "", "## Resep: dari dapur ke kode", "", "| Bahan kue | Padanan deep learning | File Oralytic |", "|---|---|---|"]
out += ["| %s | %s | `%s` |" % (r["kue"], r["dl"], r["file"]) for r in k["resep"]]
for i, b in enumerate(k["bab"]):
    out += ["", "## Bab %d. %s" % (i, b["judul"]), "", "*%s* · %s" % (b["tahap"], ", ".join("`%s`" % f for f in b["file"])), "",
            "**Deep learning adalah…** " + b["adalah"][len("Deep learning adalah "):], "",
            "**Jika kita ingin membentuk ini…** " + b["bentuk"], "",
            "**Bayangkan programnya…** " + b["bayangkan"], "",
            "**Seperti membuat kue…** " + b["kue"], ""]
    if b["langkah"]:
        out += ["Langkah di kode:", ""] + ["%d. %s" % (j + 1, x) for j, x in enumerate(b["langkah"])] + [""]
    if b["kode"]:
        out += ["Potongan kode (`%s`):" % b["kode"]["file"], "", "```python", b["kode"]["isi"], "```", "", b["kode"]["ket"], ""]
    if b["angka"]:
        out += ["Angka: " + "; ".join("%s = %s" % (a["label"], a["nilai"]) for a in b["angka"]) + ".", ""]
    if b["istilah"]:
        out += ["Istilah:", ""] + ["- **%s**: %s" % (x["nama"], x["arti"]) for x in b["istilah"]] + [""]
    if b["catatan"]:
        out += ["> " + b["catatan"], ""]
    out.append("Mata kuliah: " + ", ".join(M[m]["nama"] for m in b["materi"] if m in M) + ".")
open(os.path.join(ROOT, "Kisah-Deep-Learning-Oralytic.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("Referensi-v1.4.md dan Kisah-Deep-Learning-Oralytic.md ditulis")
