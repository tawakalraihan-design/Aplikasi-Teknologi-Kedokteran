"""Menulis Referensi-v1.3.md dari defaultdata/referensi.json.

Pemakaian: python3 tools/v4/referensi_md.py
"""
import json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DD = os.path.join(ROOT, "defaultdata")


def load(n):
    return json.load(open(os.path.join(DD, n + ".json"), encoding="utf-8"))


ref, alat, materi = load("referensi"), load("alat"), load("materi")
A = {a["id"]: a for a in alat}
M = {m["id"]: m for m in materi}
JENIS = [("buku", "Buku teks"), ("standar", "Standar dan regulasi"), ("jurnal", "Jurnal dan pedoman"),
         ("dataset", "Dataset"), ("web", "Web dan perangkat lunak"), ("proyek", "Sumber proyek hands-on")]

out = ["# Referensi Teknologi Kedokteran v1.3", "",
       "Sumber untuk modul mata kuliah, studi kasus alat, 23 alat baru, dan proyeknya. "
       "Di aplikasi, daftar ini ada di menu **Referensi** dan tiap entri menyebut alat yang memakainya. "
       "Buku dan standar ditautkan ke pencarian WorldCat atau halaman resmi penerbit/badan standar; "
       "standar IEC/ISO berbayar, jadi biasanya diakses lewat perpustakaan ITS.", "",
       "Total %d entri: %s." % (len(ref), ", ".join("%d %s" % (sum(r["jenis"] == j for r in ref), l.lower())
                                                    for j, l in JENIS + [("kuliah", "bahan kuliah")])), ""]

for j, label in JENIS:
    rs = [r for r in ref if r["jenis"] == j]
    if not rs:
        continue
    out += ["## " + label, ""]
    for r in rs:
        judul = "[%s](%s)" % (r["judul"], r["url"]) if r["url"] else r["judul"]
        siapa = " · ".join(str(x) for x in (r.get("penulis"), r.get("tahun")) if x)
        al = ", ".join(A[x]["singkatan"] or A[x]["nama"] for x in r["alat"] if x in A)
        baris = "- %s%s" % (judul, " — " + siapa if siapa else "")
        if r.get("ket"):
            baris += ". " + r["ket"].rstrip(".") + "."
        if al:
            baris += " *Alat:* " + al + "."
        out.append(baris)
    out.append("")

# Bahan kuliah: cukup ringkasan per mata kuliah, berkasnya ada di D:\Semester N.
kul = defaultdict(list)
for r in ref:
    if r["jenis"] == "kuliah":
        kul[r["materi"][0]].append(r)
out += ["## Bahan kuliah dari D:\\Semester 1–5", "",
        "Berkas asli tetap di laptop; aplikasi hanya menyimpan judul, jumlah halaman, dan ringkasan isinya. "
        "Di versi laptop tombol **Buka** membuka berkasnya langsung.", "",
        "| Semester | Mata kuliah | Berkas | Dipakai untuk alat |", "|---|---|---|---|"]
for mid in sorted(kul, key=lambda x: (M[x]["semester"] or 9, M[x]["nama"])):
    al = ", ".join(A[x]["singkatan"] or A[x]["nama"] for x in kul[mid][0]["alat"] if x in A)
    out.append("| %s | %s | %d | %s |" % (M[mid]["semester"], M[mid]["nama"], len(kul[mid]), al or "–"))
out.append("")

with open(os.path.join(ROOT, "Referensi-v1.3.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Referensi-v1.3.md:", len(ref), "entri,", len(kul), "mata kuliah dengan bahan kuliah")
