"""Menulis Referensi-v1.5.md: buku acuan OSITS Fisika per bidang, daftar paket latsol,
dan ringkasan semua soal beserta jawaban akhir (rumus LaTeX tetap terbaca di Obsidian).

Pemakaian: python3 tools/v6/tulis_md.py
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
data = json.load(open(os.path.join(ROOT, "defaultdata", "osits.json"), encoding="utf-8"))
bidang = [x for x in data if x["jenis"] == "bidang"]
buku = {x["id"]: x for x in data if x["jenis"] == "buku"}
paket = [x for x in data if x["jenis"] == "paket"]
B = {b["id"]: b for b in bidang}
n_soal = sum(len(p["soal"]) for p in paket)

out = ["# Referensi Teknologi Kedokteran v1.5: OSITS Fisika", "",
       "Fitur baru **OSITS Fisika** (menu Belajar → OSITS Fisika) disusun dari folder `D:\\Project ITS\\Peserta_OSITS Fisika`: "
       "%d paket latsol ONMIPA-PT (%d soal) dan %d buku di subfolder `Buku`. Di aplikasi, setiap soal dibahas bertahap "
       "(petunjuk → langkah → jawaban akhir). File ini merangkum buku acuan dan jawaban akhir untuk dibaca di luar aplikasi." % (len(paket), n_soal, len(buku)), "",
       "> Pembahasan disusun ulang dari soal asli, bukan kunci resmi panitia. Soal yang memakai tafsiran diberi catatan.", "",
       "## Buku acuan per bidang", ""]
for b in bidang:
    out += ["### %s %s" % (b["ikon"], b["nama"]), "", b["ringkas"], ""]
    for r in b["buku"]:
        k = buku[r["buku"]]
        out.append("- **%s**: %s%s" % (k["singkat"], r["bab"], " (mulai hal. PDF %d)" % r["hal"] if r.get("hal") else ""))
    out.append("")
out += ["## Daftar buku", "", "| Buku | Penulis | Hal. | Bidang | File |", "|---|---|---|---|---|"]
for k in buku.values():
    out.append("| %s | %s | %d | %s | `%s` |" % (k["judul"], k["penulis"], k["halaman"], ", ".join(B[x]["singkat"] for x in k["bidang"]), k["file"].split("\\")[-1]))
out.append("")
out += ["## Paket soal dan jawaban akhir", ""]
for p in paket:
    out += ["### %s %d · %s" % (p["tingkat"], p["tahun"], p["judul"]), "",
            "%s · %d menit · %d soal · `%s`" % (p["tanggal"], p["waktu"], len(p["soal"]), p["file"].split("\\")[-1]), "", p["aturan"], ""]
    for q in p["soal"]:
        out.append("**%d. %s** (%s)%s" % (q["no"], q["topik"], B[q["bidang"]]["singkat"], " · *" + q["catatan"] + "*" if q.get("catatan") else ""))
        out.append("")
        for b in q["bagian"]:
            out.append("- %s%s" % ("(%s) " % b["label"] if b["label"] else "", b["jawab"].replace("\n", " ")))
        out.append("")
open(os.path.join(ROOT, "Referensi-v1.5.md"), "w", encoding="utf-8").write("\n".join(out))
print("Referensi-v1.5.md:", len(out), "baris")
