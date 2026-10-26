# -*- coding: utf-8 -*-
"""Bangun konten bawaan v3: bidang mata kuliah, arketipe ilustrasi alat,
proyek hands-on, bank soal, dan materi studi lanjutan."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import proyek_v3, soal_v3, lanjutan_v3

ROOT = os.path.join(os.path.dirname(__file__), "..", "defaultdata")
load = lambda n: json.load(open(os.path.join(ROOT, n + ".json"), encoding="utf-8"))
def dump(n, d):
    with open(os.path.join(ROOT, n + ".json"), "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

materi, alat = load("materi"), load("alat")

# Bidang = tiga bidang peminatan kuliah + ilmu dasar/klinis bersama.
BIDANG = {
    "Informatika": ["pemrograman", "sinyal", "iot", "mobile", "kdm", "uav", "simrs", "citra", "statistika", "manajemen-data",
                    "ilmu-data", "ml-medis", "visualisasi", "data-mining", "big-data"],
    "Elektrikal": ["rangkaian", "elda", "eldig", "elektronika-medis", "sistem-tertanam", "sensor", "instrumen", "kendali", "mikro",
                   "monitoring", "robotika", "fisika-listrik-magnet", "k3", "kalibrasi"],
    "Desain": ["cad-medis", "design-thinking", "difabel", "purwarupa", "dtk", "biomaterial", "biomekanik"],
}
inv = {m: b for b, ms in BIDANG.items() for m in ms}
for m in materi:
    m["bidang"] = inv.get(m["id"], "Dasar")

# Arketipe ilustrasi SVG per alat (digambar di web/ilustrasi.js).
ARK = {
    "ekg": "monitor", "eeg": "monitor", "oksimeter": "klip", "tensimeter": "manset", "usg": "usg", "xray": "xray",
    "ct": "gantry", "mri": "gantry", "ventilator": "ventilator", "infus": "pompa", "defibrilator": "aed",
    "inkubator": "inkubator", "hemodialisis": "dialisis", "brainmapping": "laptop", "neurofeedback": "laptop",
    "tms": "koil", "ect": "stimulator", "tens": "stimulator", "stimulasi-listrik": "stimulator",
    "diatermi-sw": "konsol", "diatermi-mw": "konsol", "terapi-us": "konsol", "brace-skoliosis": "brace",
    "termometer": "genggam", "glukometer": "genggam", "kimia-klinik": "analyzer", "koagulasi": "analyzer",
    "cat": "analyzer", "elektrolit": "analyzer", "hematologi": "analyzer", "immunoassay": "analyzer",
    "urin-analyzer": "analyzer", "sentrifus": "sentrifus", "mikroskop": "mikroskop", "brainwave": "laptop",
    "motion-correction": "laptop",
}
for a in alat:
    a["ilustrasi"] = ARK.get(a["id"], "monitor")

mid = {m["id"]: m for m in materi}
aid = {a["id"]: a for a in alat}

proyek = proyek_v3.get()
for p in proyek:
    a = aid[p["alat"]]
    bids = {b["id"] for b in a["blok"]}
    assert all(b in bids for b in p["blok"]), (p["id"], p["blok"], bids)
    assert all(m in mid for m in p["materi"]), (p["id"], [m for m in p["materi"] if m not in mid])
    assert len({x["id"] for x in proyek}) == len(proyek)
for a in alat:
    assert any(p["alat"] == a["id"] for p in proyek), a["id"]

soal = soal_v3.get()
lan = lanjutan_v3.get()
lids = {l["id"] for l in lan}
for i, s in enumerate(soal):
    s["id"] = f"s{i + 1:03d}"
    assert s["alat"] in aid or s["alat"] in lids, s["alat"]
    if s["tipe"] in ("pg", "kasus"):
        assert len(s["opsi"]) == 4 and s["jawab"] == 0, s["tanya"]
for l in lan:
    for mo in l["modul"]:
        assert all(x in aid for x in mo["alat"]), mo["id"]

dump("materi", materi); dump("alat", alat); dump("proyek", proyek); dump("soal", soal); dump("lanjutan", lan)
from collections import Counter
print("materi", len(materi), Counter(m["bidang"] for m in materi))
print("proyek", len(proyek), "soal", len(soal), Counter(s["tipe"] for s in soal), "lanjutan", len(lan))
