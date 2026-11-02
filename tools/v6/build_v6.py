"""Membangun konten v1.5 ke defaultdata/.

- osits.json (baru): fitur belajar OSITS/ONMIPA Fisika. Isinya daftar entri dengan "jenis":
  "bidang" (5 bidang uji), "buku" (buku acuan di folder Peserta_OSITS Fisika\\Buku),
  dan "paket" (10 paket soal latsol beserta pembahasan bertahap).
- soal.json: MENAMBAH soal latihan cepat OSITS (field "osits").
Aman dijalankan ulang: entri buatan skrip ini diganti, entri lain tidak disentuh.
Validasi: id unik, rujukan bidang/buku, file gambar ada, setiap bagian punya langkah dan jawaban,
dan SEMUA rumus LaTeX diuji render dengan KaTeX (node) agar tidak ada rumus rusak di aplikasi.
Pemakaian: python3 tools/v6/build_v6.py
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DD = os.path.join(ROOT, "defaultdata")
sys.path.insert(0, HERE)

import osits_bidang as OB  # noqa: E402
import osits_latihan as OL  # noqa: E402
import osits_nasional2017 as ON  # noqa: E402
import osits_regional as OR  # noqa: E402

ERR = []
PAKET = OR.PAKET_REG + ON.PAKET_NAS + OR.PAKET_24


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


materi = {m["id"] for m in load("materi")}
BID = {b["id"] for b in OB.BIDANG}
BUK = {b["id"] for b in OB.BUKU}

# ---------- validasi ----------
for b in OB.BIDANG:
    for m in b["materi"]:
        if m not in materi:
            ERR.append("bidang %s: materi %s tidak ada" % (b["id"], m))
    for r in b["buku"]:
        if r["buku"] not in BUK:
            ERR.append("bidang %s: buku %s" % (b["id"], r["buku"]))
for k in OB.BUKU:
    for x in k["bidang"]:
        if x not in BID:
            ERR.append("buku %s: bidang %s" % (k["id"], x))
ids = set()
for p in PAKET:
    for x in p["bidang"]:
        if x not in BID:
            ERR.append("paket %s: bidang %s" % (p["id"], x))
    for q in p["soal"]:
        if q["id"] in ids:
            ERR.append("soal ganda " + q["id"])
        ids.add(q["id"])
        if q["bidang"] not in BID:
            ERR.append("%s: bidang %s" % (q["id"], q["bidang"]))
        for x in q["buku"]:
            if x not in BUK:
                ERR.append("%s: buku %s" % (q["id"], x))
        if q.get("gambar") and not os.path.exists(os.path.join(ROOT, "web", "osits", q["gambar"])):
            ERR.append("%s: gambar %s tidak ada" % (q["id"], q["gambar"]))
        if not q["bagian"]:
            ERR.append(q["id"] + ": tanpa bagian")
        for b in q["bagian"]:
            if not b["jawab"] or not b["petunjuk"]:
                ERR.append("%s(%s): petunjuk/jawaban kosong" % (q["id"], b["label"]))
        tot = sum(b.get("poin", 0) for b in q["bagian"])
        if tot and tot != q["poin"]:
            ERR.append("%s: jumlah poin bagian %s ≠ %s" % (q["id"], tot, q["poin"]))
    if p["tingkat"] == "Nasional" and sum(q["poin"] for q in p["soal"]) != 100:
        ERR.append("%s: total poin bukan 100" % p["id"])
lat_ids = set()
for s in OL.SOAL:
    if s["osits"] not in BID:
        ERR.append("latihan %s: bidang %s" % (s["id"], s["osits"]))
    if s["id"] in lat_ids:
        ERR.append("latihan ganda " + s["id"])
    lat_ids.add(s["id"])

# ---------- uji render semua rumus dengan KaTeX ----------
teks = []


def kumpul(v, asal):
    if isinstance(v, str):
        if "$" in v:
            teks.append([asal, v])
    elif isinstance(v, list):
        for i, x in enumerate(v):
            kumpul(x, asal)
    elif isinstance(v, dict):
        for k, x in v.items():
            kumpul(x, asal + "." + k if k in ("bagian",) else asal)


for b in OB.BIDANG:
    kumpul(b, "bidang:" + b["id"])
for p in PAKET:
    for q in p["soal"]:
        kumpul(q, q["id"])
for s in OL.SOAL:
    kumpul(s, s["id"])

uji = os.path.join(HERE, "uji_katex.js")
r = subprocess.run(["node", uji], input=json.dumps(teks), capture_output=True, text=True)
if r.returncode != 0:
    ERR.append("KaTeX: " + (r.stdout + r.stderr).strip()[:3000])
else:
    print(r.stdout.strip())

if ERR:
    print("GAGAL validasi:\n- " + "\n- ".join(ERR))
    sys.exit(1)

# ---------- tulis ----------
osits = [dict(jenis="bidang", **b) for b in OB.BIDANG] + [dict(jenis="buku", **b) for b in OB.BUKU] + [dict(jenis="paket", **p) for p in PAKET]
dump("osits", osits)
soal = ganti(load("soal"), OL.SOAL)
dump("soal", soal)
n_soal = sum(len(p["soal"]) for p in PAKET)
n_bag = sum(len(q["bagian"]) for p in PAKET for q in p["soal"])
print("osits.json: %d bidang, %d buku, %d paket, %d soal uraian/isian (%d bagian bertahap)" % (len(OB.BIDANG), len(OB.BUKU), len(PAKET), n_soal, n_bag))
print("soal.json: %d soal (+%d latihan cepat OSITS)" % (len(soal), len(OL.SOAL)))
