# -*- coding: utf-8 -*-
"""Materi Studi Lanjutan: HTA, Health Economics, Public Health (v1.2)."""

L = [
    {
        "id": "hta", "nama": "Health Technology Assessment", "singkat": "HTA", "ikon": "⚖️",
        "ringkasan": "Menilai nilai sebuah teknologi kesehatan secara menyeluruh: apakah efektif, aman, sepadan dengan biayanya, dan layak diterapkan di sistem kesehatan.",
        "kaitan": "Setelah kamu bisa merancang alat, pertanyaan berikutnya adalah: perlukah alat ini dibeli rumah sakit atau dijamin JKN? HTA adalah jembatan dari laboratorium ke kebijakan.",
        "alatInteraktif": "hta",
        "modul": [
            {"id": "hta-1", "judul": "Apa itu HTA dan kenapa alat kesehatan butuh HTA", "poin": [
                "HTA: evaluasi sistematis dan multidisiplin tentang dampak teknologi kesehatan untuk mendukung keputusan.",
                "Teknologi = obat, alat, prosedur, program, dan sistem informasi.",
                "Alat berbeda dari obat: hasil bergantung pada operator (kurva belajar), desain cepat berganti, butuh infrastruktur dan pemeliharaan.",
                "Pengguna hasil HTA: Kemenkes/BPJS (paket manfaat), rumah sakit (pengadaan), dan industri (desain sesuai kebutuhan)."],
             "alat": ["mri", "ct", "hemodialisis"]},
            {"id": "hta-2", "judul": "Proses HTA: dari topik sampai rekomendasi", "poin": [
                "Pemilihan topik dan prioritas (beban penyakit, biaya, ketidakpastian).",
                "Scoping dengan PICO: Population, Intervention, Comparator, Outcome.",
                "Assessment: tinjauan sistematis bukti klinis dan evaluasi ekonomi.",
                "Appraisal: komite menimbang bukti bersama nilai sosial, etika, dan anggaran.",
                "Rekomendasi, implementasi, lalu evaluasi ulang."],
             "alat": ["defibrilator", "glukometer"]},
            {"id": "hta-3", "judul": "HTA Core Model: 9 domain penilaian", "poin": [
                "1 Masalah kesehatan dan pemakaian teknologi saat ini.",
                "2 Deskripsi dan karakteristik teknis teknologi.",
                "3 Keamanan.", "4 Efektivitas klinis.", "5 Biaya dan evaluasi ekonomi.",
                "6 Analisis etis.", "7 Aspek organisasi.", "8 Aspek pasien dan sosial.", "9 Aspek hukum.",
                "Domain 1–5 disebut 'rapid REA' dan sering dikerjakan lebih dulu."],
             "alat": ["usg", "ventilator"]},
            {"id": "hta-4", "judul": "HTA di Indonesia", "poin": [
                "Komite Penilaian Teknologi Kesehatan (InaHTAC) memberi rekomendasi untuk paket manfaat JKN.",
                "Pedoman PTK Indonesia telah direvisi; mencakup perspektif, pembanding, ambang efektivitas biaya, dan analisis dampak anggaran.",
                "Contoh topik nasional: terapi pengganti ginjal (hemodialisis vs CAPD), skrining penyakit tidak menular.",
                "Peluang bagi lulusan Teknologi Kedokteran: penilaian alat kesehatan dalam negeri dan uji kelayakan teknis."],
             "alat": ["hemodialisis", "tensimeter"]},
            {"id": "hta-5", "judul": "Menilai alat: bukti klinis, mutu, dan regulasi", "poin": [
                "Hierarki bukti: tinjauan sistematis dan RCT di puncak, studi observasional, lalu opini ahli.",
                "Akurasi diagnostik: sensitivitas, spesifisitas, nilai prediktif, kurva ROC.",
                "Keselamatan listrik dan kinerja esensial (IEC 60601-1), manajemen risiko (ISO 14971), sistem mutu (ISO 13485).",
                "Izin edar alat kesehatan di Indonesia (AKL/AKD) dan kandungan lokal (TKDN)."],
             "alat": ["ekg", "oksimeter", "termometer"]},
        ],
        "referensi": [
            "WHO (2011), Health technology assessment of medical devices: https://www.who.int/publications/i/item/9789241501361",
            "WHO (2024), Health technology assessment of medical devices, edisi 2: https://www.who.int/publications/i/item/9789240110878",
            "WHO, Needs assessment for medical devices: https://www.who.int/publications/i/item/9789241501385",
            "EUnetHTA, HTA Core Model training course: https://www.EUnetHTA.eu/wp-content/uploads/2018/01/HTACoreModelTrainingCourse2015pv_revised.pdf",
            "EUPATI, ringkasan HTA Core Model: https://learning.eupati.eu/mod/page/view.php?id=956",
            "Kemenkes, Pedoman HTA Indonesia (bahasa Inggris): https://htaindonesia.kemkes.go.id/detail-publikasi-regulasi/pedoman-hta-bahasa-inggris",
            "HITAP, Navigating HTA implementation: review of Indonesia's revised HTA guideline: https://hitap.net/wp-content/uploads/2023/09/Navigating-HTA-implementation-a-review-of-Indonesias-revised-HTA-guideline.pdf",
            "Evolution of Health Technology Assessment in Indonesia (UI): https://dara.ui.ac.id/research-output/0275fc74-f03e-4cc6-8a89-048e47c2f4a5",
            "NICE health technology evaluations: the manual (2022): https://www.nice.org.uk/process/pmg36/resources/nice-health-technology-evaluations-themanual-pdf-72286779244741",
            "Panduan ringkas IEC 60601-1: https://meddeviceguide.com/blog/iec-60601-1-medical-electrical-equipment-safety-guide",
        ],
    },
    {
        "id": "he", "nama": "Health Economics", "singkat": "Ekonomi Kesehatan", "ikon": "💰",
        "ringkasan": "Ilmu tentang pilihan dalam sumber daya kesehatan yang terbatas: berapa biaya sebuah alat, berapa manfaat kesehatannya, dan apakah sepadan.",
        "kaitan": "Alat yang hebat secara teknis bisa gagal diadopsi bila terlalu mahal untuk manfaatnya. Evaluasi ekonomi membantu kamu merancang alat yang terjangkau dan meyakinkan pembeli.",
        "alatInteraktif": "icer",
        "modul": [
            {"id": "he-1", "judul": "Konsep dasar: kelangkaan dan biaya peluang", "poin": [
                "Anggaran kesehatan terbatas, jadi membeli satu alat berarti tidak membeli yang lain (opportunity cost).",
                "Efisiensi teknis (hasil maksimum dari input tertentu) vs efisiensi alokatif (memilih program yang paling bernilai).",
                "Pemerataan (equity): siapa yang menanggung biaya dan siapa yang menerima manfaat."],
             "alat": ["mri", "usg"]},
            {"id": "he-2", "judul": "Jenis evaluasi ekonomi", "poin": [
                "Cost-minimization: hasil dianggap setara, pilih yang termurah.",
                "Cost-effectiveness: hasil dalam unit alami (kasus terdeteksi, mmHg turun).",
                "Cost-utility: hasil dalam QALY atau DALY sehingga antar-penyakit bisa dibandingkan.",
                "Cost-benefit: manfaat dinilai dalam uang.",
                "Perspektif menentukan biaya yang dihitung: pasien, rumah sakit, pembayar (BPJS), atau masyarakat."],
             "alat": ["glukometer", "tensimeter"]},
            {"id": "he-3", "judul": "Biaya alat kesehatan sepanjang umurnya", "poin": [
                "Biaya investasi (harga beli, instalasi, pelatihan) dibagi umur ekonomis alat (annuitisasi).",
                "Biaya operasional: bahan habis pakai, listrik, kalibrasi, pemeliharaan, tenaga kerja.",
                "Biaya per pemeriksaan = (biaya tahunan total) / (jumlah pemeriksaan per tahun), jadi utilisasi sangat menentukan.",
                "Biaya langsung medis, langsung non-medis (transport pasien), dan tidak langsung (produktivitas hilang)."],
             "alat": ["ct", "hemodialisis", "kimia-klinik"]},
            {"id": "he-4", "judul": "QALY, DALY, dan ICER", "poin": [
                "QALY = tahun hidup × utilitas (0 = meninggal, 1 = sehat sempurna). Indonesia punya value set EQ-5D-5L sendiri.",
                "DALY = tahun hidup hilang + tahun hidup dengan disabilitas; dipakai WHO untuk beban penyakit.",
                "ICER = ΔBiaya / ΔEfek. Dibandingkan dengan ambang willingness-to-pay (sering dirujuk 1–3× PDB per kapita, dengan kritik).",
                "Bidang efektivitas biaya (cost-effectiveness plane) membagi hasil menjadi 4 kuadran: dominan, didominasi, dan dua kuadran trade-off."],
             "alat": ["defibrilator", "ventilator"]},
            {"id": "he-5", "judul": "Pemodelan dan ketidakpastian", "poin": [
                "Pohon keputusan untuk kejadian jangka pendek (misal skrining → diagnosis → terapi).",
                "Model Markov untuk penyakit kronis dengan keadaan berulang (misal gagal ginjal).",
                "Diskonto biaya dan manfaat masa depan (Indonesia umumnya 3%).",
                "Analisis sensitivitas satu arah (tornado), probabilistik (Monte Carlo), dan kurva penerimaan (CEAC).",
                "Analisis dampak anggaran (BIA) menjawab apakah anggaran sanggup menanggung adopsi."],
             "alat": ["hemodialisis", "inkubator"]},
            {"id": "he-6", "judul": "Melaporkan evaluasi ekonomi", "poin": [
                "Gunakan checklist CHEERS 2022 (28 item) agar laporan transparan.",
                "Nyatakan perspektif, horizon waktu, diskonto, sumber data biaya, dan metode ketidakpastian.",
                "Untuk alat: laporkan asumsi utilisasi, umur ekonomis, dan kurva belajar."],
             "alat": ["ekg"]},
        ],
        "referensi": [
            "Drummond dkk., Methods for the Economic Evaluation of Health Care Programmes, ed. 4 (Oxford): https://ideas.repec.org/b/oxp/obooks/9780199665884.html",
            "CHEERS 2022 statement (ISPOR): https://www.ispor.org/heor-resources/good-practices/article/consolidated-health-economic-evaluation-reporting-standards-2022-cheers-2022-statement-updated-reporting-guidance-for-health-economic-evaluations",
            "CHEERS 2022 (teks lengkap, PMC): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8755935/",
            "ISPOR, Budget Impact Analysis good practice II: https://www.ispor.org/heor-resources/good-practices/article/principles-of-good-practice-for-budget-impact-analysis-ii",
            "Purba dkk. (2017), Indonesian EQ-5D-5L value set: https://link.springer.com/article/10.1007/s40273-017-0538-9",
            "Studi pilot WTP per QALY sebagai ambang efektivitas biaya di Indonesia: https://www.ispor.org/publications/journals/value-in-health/abstract/Volume-21--Supplemental-S2/A-Pilot-Study-For-Estimation-Of-Willingness-To-Pay-Per-Quality-Adjusted-Life-Year-(WTP-PER-QALY)-as-Cost-Effectiveness-Threshold-in-Indonesia",
            "Tabel ambang efektivitas biaya antarnegara (Health Research Policy and Systems): https://health-policy-systems.biomedcentral.com/articles/10.1186/s12961-020-00647-0/tables/2",
            "Cost-effectiveness of AED deployment in selected public locations: https://deepblue.lib.umich.edu/handle/2027.42/72546?show=full",
            "HITAP, studi HTA Indonesia tentang terapi ESRD: https://hitap.net/wp-content/uploads/2017/04/Indonesia-HTA-studies-on-treatment-of-ESRD-and-PAH-26-30-Oct-2015.pdf",
        ],
    },
    {
        "id": "ph", "nama": "Public Health", "singkat": "Kesehatan Masyarakat", "ikon": "🌏",
        "ringkasan": "Ilmu menjaga kesehatan populasi: mengukur masalah kesehatan, mencegah penyakit, dan memastikan teknologi sampai ke orang yang membutuhkan.",
        "kaitan": "Alat yang akurat di laboratorium bisa menyesatkan di populasi bila prevalensi rendah. Kesehatan masyarakat mengajarkan kapan sebuah alat berguna, untuk siapa, dan bagaimana menjangkau mereka.",
        "alatInteraktif": "diagnostik",
        "modul": [
            {"id": "ph-1", "judul": "Epidemiologi dasar untuk insinyur kesehatan", "poin": [
                "Insidensi (kasus baru) dan prevalensi (semua kasus) menentukan kebutuhan alat.",
                "Desain studi: potong lintang, kohort, kasus-kontrol, dan uji klinis acak.",
                "Bias dan perancu (confounding) memengaruhi validitas data dari alat."],
             "alat": ["tensimeter", "glukometer"]},
            {"id": "ph-2", "judul": "Akurasi alat diagnostik di populasi", "poin": [
                "Sensitivitas = TP/(TP+FN); spesifisitas = TN/(TN+FP).",
                "PPV dan NPV bergantung pada prevalensi: alat yang sama bisa menghasilkan banyak positif palsu di populasi berprevalensi rendah.",
                "Kurva ROC dan pemilihan ambang (cut-off) sesuai tujuan: skrining butuh sensitivitas tinggi, konfirmasi butuh spesifisitas tinggi."],
             "alat": ["ekg", "oksimeter", "urin-analyzer"]},
            {"id": "ph-3", "judul": "Skrining dan deteksi dini", "poin": [
                "Kriteria Wilson–Jungner: penyakit penting, fase laten dapat dideteksi, ada tes yang dapat diterima, ada pengobatan efektif, biaya seimbang.",
                "Contoh di Indonesia: skrining hipertensi dan diabetes di Posbindu/puskesmas, skrining bayi baru lahir.",
                "Desain alat skrining: murah, cepat, mudah dipakai kader, dan tervalidasi."],
             "alat": ["tensimeter", "glukometer", "termometer"]},
            {"id": "ph-4", "judul": "Sistem kesehatan dan teknologi", "poin": [
                "Enam building blocks WHO: layanan, tenaga kesehatan, informasi, produk dan teknologi medis, pembiayaan, tata kelola.",
                "WHO Priority Medical Devices dan Global Atlas of Medical Devices memetakan ketersediaan alat antarnegara.",
                "Siklus hidup alat: perencanaan kebutuhan, pengadaan, donasi, pemeliharaan, dan penghapusan."],
             "alat": ["oksimeter", "ventilator", "inkubator"]},
            {"id": "ph-5", "judul": "Konteks Indonesia", "poin": [
                "Survei Kesehatan Indonesia (SKI) 2023 sebagai sumber data prevalensi penyakit nasional.",
                "Transformasi sistem kesehatan 6 pilar: layanan primer, rujukan, ketahanan kesehatan (termasuk alat kesehatan dalam negeri), pembiayaan, SDM, dan teknologi kesehatan.",
                "JKN-BPJS sebagai pembayar utama memengaruhi alat apa yang tersedia di fasilitas."],
             "alat": ["tensimeter", "hemodialisis"]},
            {"id": "ph-6", "judul": "Kesehatan digital dan data", "poin": [
                "Surveilans memakai data dari alat (IoT, rekam medis elektronik).",
                "Interoperabilitas (HL7 FHIR, SATUSEHAT) agar data alat masuk sistem nasional.",
                "Etika dan privasi data kesehatan."],
             "alat": ["infus", "termometer"]},
        ],
        "referensi": [
            "WHO, Global atlas of medical devices 2022: https://www.who.int/publications/i/item/9789240062207",
            "WHO, daftar priority medical devices untuk penyakit kardiovaskular dan diabetes (2021): https://www.who.int/news/item/30-06-2021-who-launches-list-of-priority-medical-devices-for-management-of-cardiovascular-diseases-and-diabetes",
            "WHO, Health system building blocks (National Health Planning Tools): https://extranet.who.int/nhptool/BuildingBlock.aspx",
            "Ulasan penerapan kerangka building blocks WHO (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC5651704",
            "Kemenkes BKPK, Survei Kesehatan Indonesia 2023: https://www.badankebijakan.kemkes.go.id/hasil-ski-2023/",
            "Kemenkes, Transformasi kesehatan: https://www.kemkes.go.id/id/transformasi-kesehatan-wujud-konkret-hadirnya-negara-dalam-mewujudkan-indonesia-sehat",
            "WHO, Health technology assessment of medical devices: https://www.who.int/publications/i/item/9789241501361",
        ],
    },
]


def get():
    return L
