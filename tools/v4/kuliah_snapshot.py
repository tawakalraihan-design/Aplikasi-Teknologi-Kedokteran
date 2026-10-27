"""Membuat tools/v4/kuliah.json: daftar file bahan kuliah Sobat per mata kuliah.

Sumber: hasil ekstraksi folder D:\\Semester N\\<mata kuliah>\\Materi Kuliah
(judul slide per file). Dijalankan sekali saat akuisisi; hasilnya dipakai
build_v4.py sehingga build tidak butuh akses ke drive D.
Pemakaian: python3 tools/v4/kuliah_snapshot.py /path/ke/poin.json
"""
import json, re, sys, os

FOLDER = {
    ("S1", "Anatomi"): "anatomi", ("S1", "Biologi Kedokteran"): "biologi-kedokteran",
    ("S1", "Fisika Mekanika"): "fisika-mekanika", ("S1", "Kalkulus"): "kalkulus",
    ("S1", "Pengantar Elektronika Medis"): "elektronika-medis",
    ("S2", "Elektronika Digital"): "eldig", ("S2", "Fisika Listrik & Magnet"): "fisika-listrik-magnet",
    ("S2", "Fisiologi Kedokteran"): "fisiologi", ("S2", "Pengantar Teknologi Kedokteran"): "pengantar-tekkes",
    ("S3", "Desain Teknologi berbantu Komputer untuk Medis"): "cad-medis", ("S3", "Internet of Things"): "iot",
    ("S3", "Manajemen Data"): "manajemen-data", ("S3", "Pengantar Biomekanik"): "biomekanik",
    ("S3", "Teknologi Pencitraan Medis"): "pencitraan", ("S3", "Telinga dan Pendengaran"): "telinga",
    ("S4", "Desain Teknologi Difabel & Critical Desain Thinking"): "difabel",
    ("S4", "Ilmu Data Medis"): "ilmu-data", ("S4", "Pemrograman Perangkat Bergerak"): "mobile",
    ("S4", "Sistem Tertanam pada Teknologi Kedokteran"): "sistem-tertanam",
    ("S4", "Teknologi Pada Bidang Keperawatan"): "tek-keperawatan",
    ("S5", "Desain Teknologi Kedokteran"): "dtk", ("S5", "Komunikasi Data Medis"): "kdm",
    ("S5", "Machine Learning"): "ml-medis", ("S5", "Purwarupa Cepat"): "purwarupa",
    ("S5", "Visualisasi Data"): "visualisasi",
}
# File yang isinya untuk mata kuliah lain di folder gabungan.
KE_DT = ["CRITICAL  DESIGN THINKING.pdf"]

BUANG = re.compile(r"(ITS\b|Departemen|Terdiri dari|\d+/\d+$|^by |Matematika 1|Kuliah \d+$|libgen|Semester Gasal|^\W*$|^Slide \d+|^Thank|^Terima kasih|^Terimakasih|^Pertanyaan|^Questions?$|^Q ?& ?A)", re.I)


def judul_file(nama):
    t = os.path.splitext(nama)[0]
    t = re.sub(r"\s*\(\d+\)", "", t)
    t = re.sub(r"\.pptx$", "", t)
    t = re.sub(r"\s+", " ", t).strip(" -_")
    if "Dugan Um" in t:
        t = "Dugan Um - Solid Modeling and Applications (Springer, 2016)"
    return t


def bersih(poin, judul):
    out, seen = [], set()
    for p in poin:
        p = re.sub(r"\s+", " ", p).strip(" -–—:·•")
        if len(p) < 6 or len(p) > 80 or BUANG.search(p):
            continue
        k = p.lower()[:22]
        if k in seen or k in judul.lower():
            continue
        seen.add(k)
        out.append(p)
    return out[:8]


def main(src):
    poin = json.load(open(src))
    hasil = {}
    for key, v in poin.items():
        parts = key.split("/")
        sem, mk, rel = parts[0], parts[1], "/".join(parts[2:])
        mid = FOLDER[(sem, mk)]
        nama = parts[-1]
        if mid == "difabel" and nama in KE_DT:
            mid = "design-thinking"
        path = "D:\\Semester %s\\%s\\%s" % (sem[1:], mk, rel.replace("/", "\\"))
        jd = judul_file(nama)
        kontrak = bool(re.search(r"kontrak|course agreement|RPS", nama, re.I))
        hasil.setdefault(mid, []).append({
            "file": path, "judul": jd, "n": v["n"], "jenis": os.path.splitext(nama)[1][1:].lower(),
            "poin": bersih(v["poin"], jd), "kontrak": kontrak,
        })

    def kunci(x):
        m = re.match(r"\D*?(\d+)", x["judul"])
        return (0 if x["kontrak"] else 1, int(m.group(1)) if m else 999, x["judul"].lower())
    for mid in hasil:
        hasil[mid].sort(key=kunci)
    tujuan = os.path.join(os.path.dirname(__file__), "kuliah.json")
    json.dump(hasil, open(tujuan, "w"), ensure_ascii=False, indent=1)
    print(tujuan, {k: len(v) for k, v in hasil.items()})


if __name__ == "__main__":
    main(sys.argv[1])
