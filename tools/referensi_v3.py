# -*- coding: utf-8 -*-
"""Kumpulkan semua referensi v1.2 (proyek, studi lanjutan, desain latihan) ke Referensi-v1.2.md."""
import json, re, pathlib

D = pathlib.Path(__file__).resolve().parent.parent / "defaultdata"
alat = {a["id"]: a for a in json.load(open(D / "alat.json", encoding="utf-8"))}
proyek = json.load(open(D / "proyek.json", encoding="utf-8"))
lanjutan = json.load(open(D / "lanjutan.json", encoding="utf-8"))


def md(r):
    m = re.search(r"https?://\S+", r)
    if not m:
        return r
    label = r.replace(m.group(0), "").rstrip(": ").strip()
    return f"[{label or m.group(0)}]({m.group(0)})"


out = ["# Referensi Teknologi Kedokteran v1.2", "",
       "Sumber yang dipakai untuk proyek hands-on, studi lanjutan (HTA, Health Economics, Public Health), dan desain fitur latihan soal. Harga bahan proyek adalah perkiraan marketplace Indonesia (akhir 2026), jadi cek ulang sebelum membeli.", ""]

out += ["## 1. Proyek hands-on per alat", ""]
seen_alat = []
for p in proyek:
    if p["alat"] not in seen_alat:
        seen_alat.append(p["alat"])
for aid in seen_alat:
    a = alat.get(aid, {"nama": aid})
    refs = []
    for p in sorted([p for p in proyek if p["alat"] == aid], key=lambda x: x["tahap"]):
        for r in p.get("referensi", []):
            if r not in refs:
                refs.append(r)
    out.append(f"### {a['nama']}")
    out.append("")
    out += [f"- {md(r)}" for r in refs]
    out.append("")

out += ["## 2. Studi lanjutan", ""]
for l in lanjutan:
    out.append(f"### {l['nama']}")
    out.append("")
    out += [f"- {md(r)}" for r in l.get("referensi", [])]
    out.append("")

out += ["## 3. Desain fitur latihan soal", "",
        "- [Duolingo: jenis-jenis latihan (pilih, cocokkan, susun urutan)](https://duolingo.fandom.com/wiki/Exercise)",
        "- [Quizlet Match: mencocokkan pasangan dengan stopwatch](https://help.quizlet.com/hc/en-us/articles/360031183611)",
        "- [Kahoot: ringkasan studi manfaat kuis berbasis permainan](https://kahoot.com/blog/2020/07/01/dozens-of-studies-show-learning-benefits-of-kahoot/)",
        "- [Tinjauan literatur pengaruh Kahoot pada hasil belajar](https://www.universityxp.com/research/2021/8/28/a-literature-review-on-the-influence-of-kahoot-on-learning-outcomes-interaction-and-collaboration)",
        "- [Retrieval practice dan testing effect (Roediger & Karpicke, 2006)](https://yukaichou.com/gamification-analysis/retrieval-practice-testing-effect-roediger-karpicke-learning/)",
        ""]
n = sum(1 for l in out if l.startswith("- "))
out.insert(3, f"\nTotal {n} entri referensi.")
(pathlib.Path(__file__).resolve().parent.parent / "Referensi-v1.2.md").write_text("\n".join(out), encoding="utf-8")
print(n)
