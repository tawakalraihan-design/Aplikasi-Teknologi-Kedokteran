"""Membangun konten v1.4 ke defaultdata/.

- kisah.json (baru): Kisah Deep Learning dari kode Oralytic.
- referensi.json: MENAMBAH 12 buku folder Referensi (jenis "pustaka", dengan daftar bab).
- soal.json: MENAMBAH soal kisah dan soal dari buku.
- alat.json: MENAMBAH Oralytic dan 6 alat dari buku.
Aman dijalankan ulang: entri buatan skrip ini diganti, entri lain tidak disentuh.
Pemakaian: python3 tools/v5/build_v5.py
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DD = os.path.join(ROOT, "defaultdata")
sys.path.insert(0, HERE)

import kisah_oralytic as KO  # noqa: E402
import pustaka as PU  # noqa: E402

ERR = []


def load(n):
    p = os.path.join(DD, n + ".json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []


def dump(n, data):
    with open(os.path.join(DD, n + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def ganti(lama, baru):
    ids = {x["id"] for x in baru}
    return [x for x in lama if x["id"] not in ids] + baru


materi, alat, soal, referensi = load("materi"), load("alat"), load("soal"), load("referensi")
alat = ganti(alat, [KO.ALAT] + PU.ALAT_BUKU)
referensi = ganti(referensi, PU.PUSTAKA)
soal = ganti(soal, KO.SOAL + PU.SOAL)

M = {m["id"] for m in materi}
A = {a["id"]: a for a in alat}

# ---------- validasi ----------
for a in [KO.ALAT] + PU.ALAT_BUKU:
    blok = {b["id"] for b in a["blok"]}
    for k in a["kontribusi"]:
        if k["materi"] not in M:
            ERR.append("alat %s: materi %s tidak ada" % (a["id"], k["materi"]))
        for b in k["blok"]:
            if b not in blok:
                ERR.append("alat %s: blok %s tidak ada" % (a["id"], b))
for b in KO.BAB:
    for m in b["materi"]:
        if m not in M:
            ERR.append("kisah %s: materi %s" % (b["id"], m))
    for k in ("adalah", "bentuk", "bayangkan", "kue"):
        awal = {"adalah": "Deep learning adalah", "bentuk": "Jika kita ingin membentuk", "bayangkan": "Bayangkan jika Anda ingin membuat program", "kue": "Bayangkan Anda seperti membuat kue"}[k]
        if not b[k].startswith(awal):
            ERR.append("kisah %s: %s tidak diawali '%s'" % (b["id"], k, awal))
for p in PU.PUSTAKA:
    for x in p["alat"]:
        if x not in A:
            ERR.append("%s: alat %s" % (p["id"], x))
    for x in p["materi"]:
        if x not in M:
            ERR.append("%s: materi %s" % (p["id"], x))
    hal = 0
    for b in p["bab"]:
        if b["hal"][0] < hal or b["hal"][1] < b["hal"][0] or b["hal"][1] > p["halaman"]:
            ERR.append("%s bab %s: halaman %s" % (p["id"], b["no"], b["hal"]))
        hal = b["hal"][0]
bab_kisah = {b["id"] for b in KO.BAB}
for q in KO.SOAL + PU.SOAL:
    if q["materi"] not in M:
        ERR.append("soal %s: materi %s" % (q["id"], q["materi"]))
    if q.get("alat") and q["alat"] not in A:
        ERR.append("soal %s: alat %s" % (q["id"], q["alat"]))
    if q.get("bab") and q["bab"] not in bab_kisah:
        ERR.append("soal %s: bab %s" % (q["id"], q["bab"]))
    t = q["tipe"]
    if t in ("pg", "kasus") and not (0 <= q["jawab"] < len(q["opsi"])):
        ERR.append("soal %s: jawab" % q["id"])
    if t == "multi" and any(i >= len(q["opsi"]) for i in q["benar"]):
        ERR.append("soal %s: benar" % q["id"])
    if t == "celah" and q["teks"].count("[[") != len(q["isi"]):
        ERR.append("soal %s: celah" % q["id"])
    if t == "kategori" and any(g >= len(q["kelompok"]) for _, g in q["item"]):
        ERR.append("soal %s: kategori" % q["id"])
ids = [q["id"] for q in soal]
if len(ids) != len(set(ids)):
    ERR.append("id soal ganda")

if ERR:
    print("\n".join(ERR))
    sys.exit(1)

dump("alat", alat)
dump("referensi", referensi)
dump("soal", soal)
dump("kisah", [KO.KISAH])
print("alat %d, referensi %d (pustaka %d, bab %d), soal %d (kisah %d, buku %d), kisah bab %d"
      % (len(alat), len(referensi), len(PU.PUSTAKA), sum(len(p["bab"]) for p in PU.PUSTAKA),
         len(soal), len(KO.SOAL), len(PU.SOAL), len(KO.BAB)))
