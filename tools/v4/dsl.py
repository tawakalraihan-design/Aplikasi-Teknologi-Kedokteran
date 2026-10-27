"""Bahasa kecil untuk menulis konten v1.3 (modul materi, soal, alat baru).

Setiap mata kuliah ditulis dengan M(...). Soal ditulis dengan fungsi
pendek per tipe. Untuk pg/kasus/multi, opsi pertama TIDAK harus benar:
pg dan kasus memakai jawab=0 (opsi pertama benar, diacak saat tampil).
"""

MODUL = []   # urutan penulisan dipertahankan
SOAL = {}    # materi id -> [soal]


def T(judul, isi, poin=(), sub=None):
    """Topik inti dalam satu mata kuliah. sub = nomor sub-materi terkait."""
    t = {"judul": judul, "isi": isi, "poin": list(poin)}
    if sub:
        t["sub"] = [str(s) for s in (sub if isinstance(sub, (list, tuple)) else [sub])]
    return t


def K(alat, judul, deteksi, pelajari, aplikasi, blok=()):
    """Studi kasus: bagaimana materi ini dipakai pada satu alat."""
    return {"alat": alat, "judul": judul, "deteksi": deteksi, "pelajari": list(pelajari),
            "aplikasi": aplikasi, "blok": list(blok)}


def M(mid, penjelasan, topik=(), kasus=(), soal=(), kuliah_poin=None, karier=None):
    d = {"id": mid, "penjelasan": penjelasan, "topik": list(topik), "kasus": list(kasus)}
    if kuliah_poin:
        d["kuliahPoin"] = kuliah_poin  # judul file -> poin, untuk file berisi gambar saja
    if karier:
        d["karier"] = karier
    MODUL.append(d)
    SOAL.setdefault(mid, []).extend(soal)
    return d


# ---------- tipe soal ----------
def _q(tipe, tanya, bahas, alat=None, **kw):
    q = {"tipe": tipe, "tanya": tanya, "bahas": bahas}
    if alat:
        q["alat"] = alat
    q.update(kw)
    return q


def pg(tanya, opsi, bahas, alat=None):
    return _q("pg", tanya, bahas, alat, opsi=list(opsi), jawab=0)


def kasus(tanya, opsi, bahas, alat=None):
    return _q("kasus", tanya, bahas, alat, opsi=list(opsi), jawab=0)


def bs(tanya, benar, bahas, alat=None):
    return _q("bs", tanya, bahas, alat, jawab=bool(benar))


def cocok(tanya, pasangan, bahas, alat=None):
    return _q("cocok", tanya, bahas, alat, pasangan=[list(p) for p in pasangan])


def urut(tanya, item, bahas, alat=None):
    return _q("urut", tanya, bahas, alat, item=list(item))


def isian(tanya, jawab, bahas, alat=None):
    """Jawaban teks pendek; jawab = daftar jawaban yang diterima."""
    return _q("isian", tanya, bahas, alat, jawab=list(jawab))


def hitung(tanya, angka, bahas, tol=None, satuan="", alat=None):
    """Soal hitungan; benar bila |x - angka| <= tol (bawaan 2% dari angka)."""
    if tol is None:
        tol = abs(angka) * 0.02 or 0.01
    return _q("hitung", tanya, bahas, alat, angka=angka, tol=tol, satuan=satuan)


def multi(tanya, opsi, benar, bahas, alat=None):
    """Pilih semua yang benar; benar = indeks opsi yang benar."""
    return _q("multi", tanya, bahas, alat, opsi=list(opsi), benar=list(benar))


def kategori(tanya, kelompok, item, bahas, alat=None):
    """Kelompokkan; item = [(teks, indeks_kelompok), ...]."""
    return _q("kategori", tanya, bahas, alat, kelompok=list(kelompok), item=[[t, i] for t, i in item])


def celah(teks, isi, pengecoh, bahas, alat=None, tanya="Lengkapi kalimat berikut."):
    """teks memakai [[0]], [[1]], ... sebagai celah; isi = kata yang benar per celah."""
    return _q("celah", tanya, bahas, alat, teks=teks, isi=list(isi), pengecoh=list(pengecoh))
