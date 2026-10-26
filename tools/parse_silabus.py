"""Ubah teks PDF 'Materi Teknologi Kedokteran' menjadi daftar mata kuliah + sub-materi bernomor."""
import json, re, sys

# Judul mata kuliah persis seperti di PDF (baris tanpa nomor), dengan id dan perkiraan semester.
# Semester 5 pasti (jadwal kuliah); selebihnya perkiraan dari urutan kurikulum.
KULIAH = [
    ("Kalkulus", "kalkulus", 1), ("kimia", "kimia", 1), ("Fisika Mekanika", "fisika-mekanika", 1),
    ("Anatomi", "anatomi", 1), ("Biologi Kedokteran", "biologi-kedokteran", 1),
    ("Pengantar Elektronika Medis", "elektronika-medis", 1),
    ("Fisika Listrik dan Magnet", "fisika-listrik-magnet", 2), ("Pengantar Penulisan Karya Ilmiah", "karya-ilmiah", 2),
    ("Fisiologi Kedokteran", "fisiologi", 2), ("Elektronika Digital", "eldig", 2),
    ("Algoritma dan Pemrograman Komputer", "pemrograman", 2), ("Pengantar Teknologi Kedokteran", "pengantar-tekkes", 2),
    ("Statistika", "statistika", 3), ("Pengantar Biomekanik", "biomekanik", 3), ("Telinga dan Pendengaran", "telinga", 3),
    ("Pengolahan Sinyal Biomedik", "sinyal", 5), ("Teknologi Pencitraan Medis", "pencitraan", 3),
    ("Desain Teknologi Berbantu Komputer untuk Medis", "cad-medis", 3), ("Pengantar Sistem Internet of Things", "iot", 3),
    ("Manajemen Data", "manajemen-data", 3), ("Teknologi dalam Ilmu Kedokteran Medik", "tek-medik", 4),
    ("Teknologi dalam Bidang Keperawatan", "tek-keperawatan", 4), ("Critical and Design Thinking", "design-thinking", 4),
    ("Pemrograman Perangkat Bergerak", "mobile", 4), ("Sistem Tertanam pada Teknologi Kedokteran", "sistem-tertanam", 4),
    ("Ilmu Data Medis", "ilmu-data", 4), ("Desain Teknologi Difabel dan Alat Bantu", "difabel", 4),
    ("Teknologi dalam Ilmu Kedokteran Bedah", "tek-bedah", 4), ("Komunikasi Data Medis", "kdm", 5),
    ("Interaksi Pasien Dengan Teknologi Kedokteran", "interaksi-pasien", 5), ("Pembelajaran Mesin Untuk Data Medis", "ml-medis", 5),
    ("Purwarupa Cepat Untuk Alat Kesehatan", "purwarupa", 5), ("Visualisasi Data Medis", "visualisasi", 5),
    ("Desain Teknologi Kesehatan", "dtk", 5), ("Metode Penelitian Teknologi Kedokteran", "metopen", 6),
    ("Penggalian Data Medis", "data-mining", 6), ("Big Data dalam Kesehatan", "big-data", 6),
    ("Pemrograman Unmanned Aerial Vehicle (UAV)", "uav", 6), ("Tatalaksana Klinis dan Rintisan Bisnis Digital", "tatalaksana", 7),
    ("Sistem Informasi Manajemen Rumah Sakit", "simrs", 7), ("Sistem Monitoring Elektronik Kesehatan", "monitoring", 7),
    ("Robotika untuk Kedokteran", "robotika", 7),
]
SEM_PASTI = {"sinyal", "kdm", "interaksi-pasien", "ml-medis", "purwarupa", "visualisasi", "dtk"}
NAMA_RESMI = {"kimia": "Kimia"}

lines = [l.rstrip() for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
heads = {h: (i, s) for h, i, s in KULIAH}
out, cur = [], None
for raw in lines:
    l = raw.strip()
    if l in heads:
        cid, sem = heads[l]
        cur = {"id": cid, "nama": NAMA_RESMI.get(cid, l), "semester": sem, "semesterPasti": cid in SEM_PASTI, "pengantar": "", "sub": []}
        out.append(cur)
        continue
    m = re.match(r"^(\d+)\.\s*(.*)$", l)
    if m:
        cur["sub"].append({"no": int(m.group(1)), "teks": m.group(2)})
    elif l.endswith(":") and not cur["sub"]:
        cur["pengantar"] = l.rstrip(":").strip()
    elif not cur["sub"]:
        # baris tanpa nomor di bawah judul (mis. "Praktek menulis Karya Ilmiah") = sub-materi tanpa nomor
        cur["sub"].append({"no": None, "teks": l})
    else:
        cur["sub"][-1]["teks"] += " " + l

for c in out:
    subs = []
    for s in c["sub"]:
        t = re.sub(r"\s+", " ", s["teks"]).strip()
        # Pecah nomor yang tertempel di satu baris PDF, mis. "Bedah Saraf 8. BTKV 9. Orthopedi"
        parts = re.split(r"\s+\d+\.\s+", t)
        for j, p in enumerate(parts):
            p = p.strip(" ,;")
            if not p:
                continue
            subs.append({"no": s["no"], "teks": p, "lanjutan": j > 0})
    # Gabungkan potongan "(Asam Basa, Kelarutan," + "Kompleks dan Pengendapan)"
    merged = []
    for s in subs:
        if merged and merged[-1]["teks"].count("(") > merged[-1]["teks"].count(")"):
            merged[-1]["teks"] += " " + s["teks"]
            continue
        merged.append(s)
    res, last = [], 0
    for s in merged:
        if not s["teks"]:
            continue
        no = s["no"]
        if s["lanjutan"]:
            no = f"{last}{chr(ord('a') + sum(1 for r in res if str(r['no']).startswith(str(last)) ))}"
        else:
            last = no
        t = s["teks"].rstrip(".")
        nama, rincian = t, ""
        if ":" in t:
            a, b = t.split(":", 1)
            if len(a) <= 90:
                nama, rincian = a.strip(), b.strip()
        res.append({"no": str(no) if no is not None else "", "nama": nama[0].upper() + nama[1:], "rincian": rincian})
    c["sub"] = res
json.dump(out, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), sum(len(c["sub"]) for c in out))
