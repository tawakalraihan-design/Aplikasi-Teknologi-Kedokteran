"""Membangun konten v1.3 ke defaultdata/.

Menulis modul.json dan referensi.json (baru), lalu MENAMBAH ke alat.json,
proyek.json, soal.json, dan materi.json. Aman dijalankan ulang: entri yang
dibuat skrip ini diganti, entri lain tidak disentuh.
Pemakaian: python3 tools/v4/build_v4.py
"""
import json, os, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DD = os.path.join(ROOT, "defaultdata")
sys.path.insert(0, HERE)

import dsl  # noqa: E402
import modul_s1, modul_s2, modul_s3, modul_s4, modul_s5, modul_lain  # noqa: E402,F401
from modul_s5 import SUB_BARU  # noqa: E402
from alat_baru import ALAT, KONTRIB_LAMA  # noqa: E402
from proyek_baru import PROYEK  # noqa: E402
from referensi_v4 import REF  # noqa: E402

# Mata kuliah yang semesternya terkonfirmasi dari folder D:\Semester N.
SEM_FOLDER = {
    "anatomi": 1, "biologi-kedokteran": 1, "fisika-mekanika": 1, "kalkulus": 1, "elektronika-medis": 1,
    "eldig": 2, "fisika-listrik-magnet": 2, "fisiologi": 2, "pengantar-tekkes": 2,
    "cad-medis": 3, "iot": 3, "manajemen-data": 3, "biomekanik": 3, "pencitraan": 3, "telinga": 3,
    "difabel": 4, "design-thinking": 4, "ilmu-data": 4, "mobile": 4, "sistem-tertanam": 4, "tek-keperawatan": 4,
    "dtk": 5, "kdm": 5, "ml-medis": 5, "purwarupa": 5, "visualisasi": 5,
}

ERR = []


def load(n):
    return json.load(open(os.path.join(DD, n + ".json"), encoding="utf-8"))


def dump(n, data):
    with open(os.path.join(DD, n + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


materi = load("materi")
alat = load("alat")
proyek = load("proyek")
soal = load("soal")
M = {m["id"]: m for m in materi}

# ---------- materi: sub baru dan semester terkonfirmasi ----------
for mid, subs in SUB_BARU.items():
    m = M[mid]
    for no, nama, rincian in subs:
        if not any(str(s["no"]) == no for s in m["sub"]):
            m["sub"].append({"no": no, "nama": nama, "rincian": rincian})
for mid, sem in SEM_FOLDER.items():
    if M[mid]["semester"] == sem:
        M[mid]["semesterPasti"] = True
    else:
        ERR.append("semester %s: data %s, folder %s" % (mid, M[mid]["semester"], sem))
SUBNO = {mid: {str(s["no"]) for s in m["sub"]} for mid, m in M.items()}

# ---------- alat: tambah alat baru, ganti versi lama buatan skrip ----------
baru_id = [a["id"] for a in ALAT]
alat = [a for a in alat if a["id"] not in baru_id] + ALAT
A = {a["id"]: a for a in alat}
BLOK = {aid: {b["id"] for b in a["blok"]} for aid, a in A.items()}


def tambah_kontrib(aid, mid, tingkat, blok, peran, sub=()):
    a = A[aid]
    if any(k["materi"] == mid for k in a["kontribusi"]):
        return False
    a["kontribusi"].append({"materi": mid, "tingkat": tingkat, "blok": list(blok), "peran": peran,
                            "sub": [str(s) for s in sub]})
    return True


n_lama = sum(tambah_kontrib(*k) for k in KONTRIB_LAMA)

# ---------- modul: validasi, lalu kaitkan studi kasus ke alat ----------
n_kasus = 0
for m in dsl.MODUL:
    mid = m["id"]
    if mid not in M:
        ERR.append("modul untuk materi tak dikenal: " + mid)
        continue
    for t in m["topik"]:
        # Nomor sub-materi berlaku global (urut PDF silabus). Mata kuliah pelengkap
        # tanpa sub merujuk sub milik mata kuliah lain: simpan sebagai "terkait".
        for s in list(t.get("sub", [])):
            if s in SUBNO[mid]:
                continue
            pemilik = [x for x, nos in SUBNO.items() if s in nos]
            if not pemilik:
                ERR.append("%s: topik '%s' merujuk sub %s yang tidak ada" % (mid, t["judul"], s))
                continue
            t["sub"].remove(s)
            t.setdefault("terkait", []).append({"materi": pemilik[0], "no": s})
        if "sub" in t and not t["sub"]:
            del t["sub"]
    for k in m["kasus"]:
        if k["alat"] not in A:
            ERR.append("%s: studi kasus alat tak dikenal %s" % (mid, k["alat"]))
            continue
        for b in k["blok"]:
            if b not in BLOK[k["alat"]]:
                ERR.append("%s: blok %s tidak ada di %s" % (mid, b, k["alat"]))
        n_kasus += tambah_kontrib(k["alat"], mid, 2, k["blok"], k["judul"] + ".")

for a in alat:
    for k in a["kontribusi"]:
        if k["materi"] not in M:
            ERR.append("%s: kontribusi materi tak dikenal %s" % (a["id"], k["materi"]))
            continue
        for b in k["blok"]:
            if b not in BLOK[a["id"]]:
                ERR.append("%s/%s: blok %s tidak ada" % (a["id"], k["materi"], b))
        for s in k["sub"]:
            if s not in SUBNO[k["materi"]]:
                ERR.append("%s/%s: sub %s tidak ada" % (a["id"], k["materi"], s))

# ---------- proyek ----------
pid_baru = {p["id"] for p in PROYEK}
proyek = [p for p in proyek if p["id"] not in pid_baru] + PROYEK
for p in PROYEK:
    if p["alat"] not in A:
        ERR.append("proyek %s: alat tak dikenal" % p["id"])
        continue
    for b in p["blok"]:
        if b not in BLOK[p["alat"]]:
            ERR.append("proyek %s: blok %s tidak ada" % (p["id"], b))
    for mid in p["materi"]:
        if mid not in M:
            ERR.append("proyek %s: materi %s tidak ada" % (p["id"], mid))

# ---------- soal: id stabil m-<materi>-NN ----------
soal = [q for q in soal if not str(q.get("id", "")).startswith("m-")]
TIPE_OK = {"pg", "kasus", "bs", "cocok", "urut", "isian", "hitung", "multi", "kategori", "celah"}
n_soal = 0
for mid, qs in dsl.SOAL.items():
    for i, q in enumerate(qs, 1):
        q = dict(q)
        q["id"] = "m-%s-%02d" % (mid, i)
        q["materi"] = mid
        if q["tipe"] not in TIPE_OK:
            ERR.append("%s: tipe soal %s" % (q["id"], q["tipe"]))
        if q.get("alat") and q["alat"] not in A:
            ERR.append("%s: alat %s" % (q["id"], q["alat"]))
        if q["tipe"] == "celah":
            n = len(re.findall(r"\[\[\d+\]\]", q["teks"]))
            if n != len(q["isi"]):
                ERR.append("%s: %d celah tapi %d isian" % (q["id"], n, len(q["isi"])))
        if q["tipe"] == "multi" and (not q["benar"] or max(q["benar"]) >= len(q["opsi"])):
            ERR.append("%s: indeks benar di luar opsi" % q["id"])
        if q["tipe"] == "kategori" and any(i2 >= len(q["kelompok"]) for _, i2 in q["item"]):
            ERR.append("%s: indeks kelompok di luar" % q["id"])
        soal.append(q)
        n_soal += 1

# ---------- modul.json: modul + daftar bahan kuliah ----------
kuliah = json.load(open(os.path.join(HERE, "kuliah.json"), encoding="utf-8"))
modul = []
for m in dsl.MODUL:
    d = {k: m[k] for k in ("id", "penjelasan", "topik", "kasus")}
    if m.get("karier"):
        d["karier"] = m["karier"]
    over = m.get("kuliahPoin", {})
    files = []
    for f in kuliah.get(m["id"], []):
        f = dict(f)
        for kunci, poin in over.items():
            if f["judul"].lower().startswith(kunci.lower()):
                f["poin"] = poin
        files.append(f)
    for kunci in over:
        if not any(f["judul"].lower().startswith(kunci.lower()) for f in files):
            ERR.append("%s: kuliahPoin '%s' tidak cocok dengan file mana pun" % (m["id"], kunci))
    d["kuliah"] = files
    modul.append(d)

# ---------- referensi.json ----------
ref = [dict(r) for r in REF]
seen_url = {r["url"] for r in ref if r["url"]}
for r in ref:
    for aid in r["alat"]:
        if aid not in A:
            ERR.append("referensi %s: alat %s" % (r["id"], aid))
    for mid in r["materi"]:
        if mid not in M:
            ERR.append("referensi %s: materi %s" % (r["id"], mid))

# Sumber proyek: alat dan materi diambil dari proyek yang memakainya.
dari_proyek = {}
for p in proyek:
    for s in p.get("referensi", []):
        mt = re.match(r"^(.*?):\s*(https?://\S+)$", s)
        if not mt:
            continue
        judul, url = mt.group(1).strip(), mt.group(2)
        e = dari_proyek.get(url)
        if not e:
            e = dari_proyek[url] = {"id": "p-" + slug(judul), "judul": judul, "penulis": "", "tahun": None,
                                    "jenis": "proyek", "url": url, "alat": [], "materi": [],
                                    "ket": "Sumber proyek hands-on", "proyek": []}
        if p["alat"] not in e["alat"]:
            e["alat"].append(p["alat"])
        for mid in p["materi"]:
            if mid not in e["materi"]:
                e["materi"].append(mid)
        e["proyek"].append(p["id"])
for url, e in dari_proyek.items():
    cur = next((r for r in ref if r["url"] == url), None)
    if cur:  # referensi pilihan yang juga dipakai proyek: gabungkan kaitannya
        cur.setdefault("proyek", []).extend(e["proyek"])
        for aid in e["alat"]:
            if aid not in cur["alat"]:
                cur["alat"].append(aid)
        continue
    nama = ", ".join(A[x]["singkatan"] for x in e["alat"][:3])
    e["ket"] = "Sumber proyek hands-on %s." % nama
    ref.append(e)

# Bahan kuliah Sobat: alat diambil dari studi kasus modul mata kuliahnya.
kasus_alat = {m["id"]: [] for m in dsl.MODUL}
for m in dsl.MODUL:
    for k in m["kasus"]:
        if k["alat"] not in kasus_alat[m["id"]]:
            kasus_alat[m["id"]].append(k["alat"])
for mid, files in kuliah.items():
    for i, f in enumerate(files, 1):
        ref.append({"id": "k-%s-%02d" % (mid, i), "judul": f["judul"], "penulis": "Bahan kuliah " + M[mid]["nama"],
                    "tahun": None, "jenis": "kuliah", "url": "", "file": f["file"], "alat": kasus_alat.get(mid, []),
                    "materi": [mid], "ket": "%s semester %s, %d halaman/slide." % (M[mid]["nama"], M[mid]["semester"], f["n"])})

ids = [r["id"] for r in ref]
dup = {x for x in ids if ids.count(x) > 1}
if dup:
    ERR.append("id referensi ganda: %s" % sorted(dup))

if ERR:
    print("VALIDASI GAGAL (%d):" % len(ERR))
    for e in ERR:
        print(" -", e)
    sys.exit(1)

dump("materi", materi)
dump("alat", alat)
dump("proyek", proyek)
dump("soal", soal)
dump("modul", modul)
dump("referensi", ref)
jenis = defaultdict(int)
for r in ref:
    jenis[r["jenis"]] += 1
print("alat %d (+%d baru), kontribusi lama +%d, dari studi kasus +%d" % (len(alat), len(ALAT), n_lama, n_kasus))
print("proyek %d, soal %d (+%d per materi), modul %d, referensi %d %s" % (
    len(proyek), len(soal), n_soal, len(modul), len(ref), dict(jenis)))
