# -*- coding: utf-8 -*-
"""DSL kecil untuk menulis soal OSITS beserta pembahasan bertahap.

S(...)  = satu soal; B(...) = satu bagian (a, b, c ...) dengan petunjuk, langkah, jawaban akhir.
Teks boleh memuat LaTeX di antara $...$ atau $$...$$.
"""

FOLDER = "D:\\Project ITS\\Peserta_OSITS Fisika"


def B(label, tanya="", poin=None, petunjuk="", langkah=(), jawab=""):
    d = {"label": label, "tanya": tanya, "petunjuk": petunjuk, "langkah": list(langkah), "jawab": jawab}
    if poin is not None:
        d["poin"] = poin
    return d


def S(no, bidang, topik, teks, bagian, gambar=None, poin=None, menit=None, konsep=(), buku=(), catatan=None):
    d = {"no": no, "bidang": bidang, "topik": topik, "teks": teks, "bagian": list(bagian),
         "konsep": list(konsep), "buku": list(buku)}
    if gambar:
        d["gambar"] = gambar
    if poin is not None:
        d["poin"] = poin
    if menit is not None:
        d["menit"] = menit
    if catatan:
        d["catatan"] = catatan
    return d


def PAKET(id, judul, tingkat, tahun, tanggal, bidang, waktu, aturan, file, soal, kalkulator=True, nilai_maks=None):
    for q in soal:
        q["id"] = id + "-" + str(q["no"])
        q["paket"] = id
        if "poin" not in q:
            q["poin"] = sum(b.get("poin", 0) for b in q["bagian"]) or nilai_maks or 10
    return {"id": id, "judul": judul, "tingkat": tingkat, "tahun": tahun, "tanggal": tanggal, "bidang": bidang,
            "waktu": waktu, "aturan": aturan, "file": FOLDER + "\\" + file, "kalkulator": kalkulator, "soal": soal}
