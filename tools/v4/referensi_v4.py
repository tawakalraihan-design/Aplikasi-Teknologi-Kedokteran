"""Referensi pilihan untuk halaman Referensi v1.3.

Setiap entri: id, judul, penulis, tahun, jenis (buku/standar/jurnal/web/dataset),
url, alat[], materi[], ket. Buku memakai tautan pencarian WorldCat agar
Sobat bisa mencari edisi yang tersedia di perpustakaan. Referensi proyek
dan bahan kuliah ditambahkan otomatis oleh build_v4.py.
"""
from urllib.parse import quote_plus

REF = []


def W(q):
    return "https://search.worldcat.org/search?q=" + quote_plus(q)


def F(rid, judul, penulis, tahun, jenis, url, alat, materi, ket):
    REF.append({"id": rid, "judul": judul, "penulis": penulis, "tahun": tahun, "jenis": jenis,
                "url": url, "alat": list(alat), "materi": list(materi), "ket": ket})


# ---------- Buku teks ----------
F("webster", "Medical Instrumentation: Application and Design, ed. 5", "John G. Webster (ed.)", 2020, "buku",
  "https://search.worldcat.org/oclc/1131895650",
  ["ekg", "oksimeter", "tensimeter", "eeg", "emg", "ventilator", "infus", "defibrilator", "spirometer", "kapnograf",
   "patient-monitor", "holter", "esu", "termometer", "glukometer", "audiometer", "ctg"],
  ["instrumen", "sensor", "elda", "elektronika-medis", "k3", "sistem-tertanam"],
  "Buku pegangan utama instrumentasi medis: biopotensial, sensor, tekanan darah, respirasi, dan keselamatan listrik. Hampir semua diagram blok alat di aplikasi ini mengikuti bab-bab Webster.")
F("khandpur", "Handbook of Biomedical Instrumentation, ed. 3", "R. S. Khandpur", 2014, "buku", W("Khandpur Handbook of Biomedical Instrumentation"),
  ["ekg", "eeg", "emg", "patient-monitor", "defibrilator", "ventilator", "hemodialisis", "audiometer", "esu", "fototerapi", "inkubator", "endoskop"],
  ["instrumen", "tek-medik", "tek-bedah", "kalibrasi"],
  "Pelengkap Webster yang lebih praktis: blok diagram alat rumah sakit lengkap dengan spesifikasi dan perawatan.")
F("bushberg", "The Essential Physics of Medical Imaging, ed. 4", "Bushberg, Seibert, Leidholdt, Boone", 2020, "buku", W("Bushberg Essential Physics of Medical Imaging"),
  ["xray", "ct", "mri", "usg", "mammografi", "fluoroskopi", "pet"],
  ["radiasi", "pencitraan", "citra", "fismed"],
  "Fisika pencitraan dari sinar-X, CT, MRI, USG, sampai kedokteran nuklir dan proteksi radiasi.")
F("gray", "Gray's Anatomy for Students, ed. 4", "Drake, Vogl, Mitchell", 2019, "buku", W("Gray's Anatomy for Students Drake Vogl Mitchell"),
  ["ekg", "usg", "xray", "ct", "mri", "endoskop", "emg", "prostesis-tangan", "brace-skoliosis"],
  ["anatomi", "anfis"],
  "Buku anatomi yang juga dipakai di bahan kuliah Anatomi semester 1. Bagus untuk anatomi permukaan dan landmark penempatan elektroda atau probe.")
F("moore", "Clinically Oriented Anatomy, ed. 9", "Moore, Dalley, Agur", 2022, "buku", W("Moore Clinically Oriented Anatomy"),
  ["ekg", "usg", "endoskop", "robot-bedah"],
  ["anatomi", "tek-bedah"],
  "Anatomi dengan kotak klinis, cocok untuk menghubungkan struktur dengan prosedur dan pencitraan.")
F("sobotta", "Sobotta Atlas of Anatomy", "Paulsen, Waschke", 2023, "buku", W("Sobotta Atlas of Anatomy"),
  ["usg", "ct", "mri"], ["anatomi"],
  "Atlas gambar anatomi detail untuk mencocokkan potongan CT dan MRI.")
F("guyton", "Guyton and Hall Textbook of Medical Physiology, ed. 14", "John E. Hall, Michael E. Hall", 2021, "buku", W("Guyton and Hall Textbook of Medical Physiology"),
  ["ekg", "oksimeter", "tensimeter", "ventilator", "spirometer", "kapnograf", "hemodialisis", "eeg", "emg", "fototerapi", "mesin-anestesi"],
  ["fisiologi", "anfis"],
  "Faal kardiovaskular, respirasi, ginjal, saraf, dan otot yang menjadi dasar sinyal yang diukur alat.")
F("tortora", "Principles of Anatomy and Physiology", "Tortora, Derrickson", 2020, "buku", W("Tortora Derrickson Principles of Anatomy and Physiology"),
  [], ["anfis", "anatomi", "fisiologi", "biologi-kedokteran"],
  "Pengantar anatomi-fisiologi yang mudah dibaca untuk semester awal.")
F("campbell", "Campbell Biology, ed. 12", "Urry, Cain, Wasserman, Minorsky, Orr", 2020, "buku", W("Campbell Biology Urry"),
  ["mikroskop", "hematologi", "immunoassay", "autoklaf"], ["biologi-kedokteran"],
  "Biologi sel, genetika, dan sistem organ untuk Biologi Kedokteran.")
F("hobbie", "Intermediate Physics for Medicine and Biology, ed. 5", "Hobbie, Roth", 2015, "buku", W("Hobbie Roth Intermediate Physics for Medicine and Biology"),
  ["ekg", "mri", "tms", "defibrilator", "kapnograf", "fototerapi"], ["fismed", "fisika-listrik-magnet"],
  "Fisika untuk biologi dan kedokteran: biolistrik, difusi, optik, dan radiasi.")
F("halliday", "Fundamentals of Physics", "Halliday, Resnick, Walker", 2021, "buku", W("Halliday Resnick Walker Fundamentals of Physics"),
  ["usg", "ctg", "esu", "implan-koklea"], ["fisika-mekanika", "fisika-listrik-magnet", "fisdas"],
  "Mekanika, gelombang, listrik, dan magnet yang dipakai di Fisika Mekanika serta Fisika Listrik dan Magnet.")
F("anton", "Calculus: Early Transcendentals", "Howard Anton, Bivens, Davis", 2021, "buku", W("Anton Calculus Early Transcendentals"),
  ["spirometer", "ct", "pet"], ["kalkulus", "matek"],
  "Buku kalkulus yang dirujuk bahan kuliah Kalkulus. Integral dipakai untuk volume spirometri dan transformasi Radon.")
F("hayt", "Engineering Circuit Analysis", "Hayt, Kemmerly, Phillips, Durbin", 2019, "buku", W("Hayt Kemmerly Engineering Circuit Analysis"),
  ["ekg", "defibrilator", "esu"], ["rangkaian", "elektronika-medis"],
  "Analisis rangkaian DC, transien, dan AC.")
F("sedra", "Microelectronic Circuits", "Sedra, Smith", 2020, "buku", W("Sedra Smith Microelectronic Circuits"),
  ["ekg", "eeg", "emg", "oksimeter"], ["elda", "elektronika-medis"],
  "Op-amp, penguat instrumentasi, dan filter aktif untuk front-end biopotensial.")
F("vahid", "Embedded System Design: A Unified Hardware/Software Introduction", "Frank Vahid, Tony Givargis", 2002, "buku", W("Vahid Givargis Embedded System Design"),
  ["smartwatch", "holter", "pill-dispenser", "patient-monitor", "alat-bantu-dengar"], ["sistem-tertanam", "mikro"],
  "Dirujuk bahan kuliah Sistem Tertanam: prosesor, memori, antarmuka, dan perancangan sistem tertanam.")
F("smith-dsp", "The Scientist and Engineer's Guide to Digital Signal Processing", "Steven W. Smith", 1997, "buku", "https://www.dspguide.com/",
  ["ekg", "eeg", "emg", "alat-bantu-dengar", "implan-koklea", "ctg", "holter"], ["sinyal", "kdm"],
  "Buku DSP gratis daring: konvolusi, FFT, filter digital. Cocok untuk Pengolahan Sinyal dan Komunikasi Data Medis.")
F("gonzalez", "Digital Image Processing, ed. 4", "Gonzalez, Woods", 2018, "buku", W("Gonzalez Woods Digital Image Processing"),
  ["xray", "ct", "mammografi", "endoskop", "mikroskop", "hematologi"], ["citra", "pencitraan"],
  "Peningkatan citra, filter, segmentasi, dan morfologi.")
F("um", "Solid Modeling and Applications", "Dugan Um", 2016, "buku", W("Dugan Um Solid Modeling and Applications"),
  ["prostesis-tangan", "brace-skoliosis", "pill-dispenser"], ["cad-medis", "purwarupa"],
  "Ada di bahan kuliah CAD Medis semester 3: pemodelan solid dan aplikasinya.")
F("bi-wang", "Computer Aided Design and Manufacturing", "Zhuming Bi, Xiaoqin Wang", 2020, "buku", W("Bi Wang Computer Aided Design and Manufacturing"),
  ["prostesis-tangan", "brace-skoliosis"], ["cad-medis", "purwarupa"],
  "CAD/CAM dan fabrikasi digital.")
F("hall-biomech", "Basic Biomechanics", "Susan J. Hall", 2021, "buku", W("Susan Hall Basic Biomechanics"),
  ["brace-skoliosis", "prostesis-tangan", "emg", "stimulasi-listrik"], ["biomekanik"],
  "Kinematika dan kinetika tubuh manusia, otot, sendi, dan tulang.")
F("geron", "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, ed. 3", "Aurélien Géron", 2022, "buku", W("Geron Hands-On Machine Learning"),
  ["mammografi", "endoskop", "holter", "ctg", "smartwatch"], ["ml-medis", "ilmu-data", "data-mining"],
  "Praktik supervised, unsupervised, dan deep learning dengan Python.")
F("loizou-book", "Speech Enhancement: Theory and Practice", "Philipos C. Loizou", 2013, "buku", W("Loizou Speech Enhancement Theory and Practice"),
  ["alat-bantu-dengar", "implan-koklea"], ["sinyal", "telinga"],
  "Peredam derau dan peningkatan bicara, dasar DSP alat bantu dengar.")
F("dorsch", "Understanding Anesthesia Equipment", "Dorsch, Dorsch", 2008, "buku", W("Dorsch Understanding Anesthesia Equipment"),
  ["mesin-anestesi", "kapnograf", "ventilator"], ["tek-bedah", "fluida"],
  "Rujukan klasik komponen mesin anestesi, vaporizer, dan sirkuit napas.")

# ---------- Standar dan regulasi ----------
F("iec60601-1", "IEC 60601-1: Medical electrical equipment, general requirements for basic safety and essential performance", "IEC", 2020, "standar",
  "https://meddeviceguide.com/blog/iec-60601-1-medical-electrical-equipment-safety-guide",
  ["ekg", "eeg", "emg", "patient-monitor", "defibrilator", "esu", "ventilator", "infus", "inkubator", "holter"], ["k3", "kalibrasi", "tatalaksana"],
  "Standar induk keselamatan alat elektromedis: isolasi tipe B, BF, CF dan batas arus bocor.")
F("iec60601-2-25", "IEC 60601-2-25: Electrocardiographs", "IEC", 2011, "standar", "",
  ["ekg", "holter"], ["instrumen", "k3"], "Persyaratan khusus elektrokardiograf: respons frekuensi, derau, proteksi defibrilasi.")
F("iec60601-2-2", "IEC 60601-2-2: High frequency surgical equipment", "IEC", 2017, "standar", "",
  ["esu"], ["k3", "kalibrasi"], "Persyaratan khusus ESU: daya keluaran, arus bocor frekuensi tinggi, pemantau pad netral.")
F("iec60601-2-27", "IEC 60601-2-27: ECG monitoring equipment", "IEC", 2011, "standar", "",
  ["patient-monitor"], ["k3", "monitoring"], "Persyaratan monitor EKG, termasuk alarm dan deteksi lead-off.")
F("iso80601-2-61", "ISO 80601-2-61: Pulse oximeter equipment", "ISO", 2017, "standar", "https://www.iso.org/search.html?q=80601-2-61",
  ["oksimeter", "smartwatch", "patient-monitor"], ["kalibrasi", "sensor"], "Akurasi SpO₂ (ARMS) dan uji klinis oksimeter.")
F("iso80601-2-55", "ISO 80601-2-55: Respiratory gas monitors", "ISO", 2018, "standar", "https://www.iso.org/search.html?q=80601-2-55",
  ["kapnograf", "mesin-anestesi", "patient-monitor"], ["k3", "sensor"], "Persyaratan monitor gas napas, termasuk CO₂ dan agen anestesi.")
F("iso15197", "ISO 15197: Blood glucose monitoring systems for self-testing", "ISO", 2013, "standar", "https://www.iso.org/search.html?q=15197",
  ["glukometer"], ["kalibrasi", "statistika"], "Syarat akurasi glukometer: 95% hasil dalam ±15 mg/dL atau ±15%.")
F("iso10993", "ISO 10993: Biological evaluation of medical devices", "ISO", 2018, "standar", "https://www.iso.org/search.html?q=10993",
  ["implan-koklea", "prostesis-tangan", "brace-skoliosis", "endoskop"], ["biomaterial", "purwarupa"],
  "Uji biokompatibilitas bahan yang bersentuhan dengan tubuh.")
F("iso14971", "ISO 14971: Application of risk management to medical devices", "ISO", 2019, "standar", "https://www.iso.org/standard/72704.html",
  ["robot-bedah", "pill-dispenser", "infus", "ventilator"], ["tatalaksana", "dtk", "k3"],
  "Kerangka manajemen risiko alat kesehatan dari desain sampai pasca pasar.")
F("iso17665", "ISO 17665: Sterilization of health care products, moist heat", "ISO", 2024, "standar", "https://www.iso.org/search.html?q=17665",
  ["autoklaf"], ["k3", "kalibrasi"], "Validasi dan pengendalian rutin sterilisasi uap.")
F("iso8253", "ISO 8253-1: Acoustics, audiometric test methods", "ISO", 2010, "standar", "https://www.iso.org/search.html?q=8253-1",
  ["audiometer"], ["telinga", "kalibrasi"], "Metode audiometri nada murni hantaran udara dan tulang.")
F("permenkes24", "Permenkes No. 24 Tahun 2022 tentang Rekam Medis", "Kementerian Kesehatan RI", 2022, "standar",
  "https://peraturan.bpk.go.id/Details/245544",
  ["rme", "telemedisin"], ["manajemen-data", "simrs"], "Dasar hukum kewajiban rekam medis elektronik dan integrasi ke SATUSEHAT.")
F("fhir", "HL7 FHIR (Fast Healthcare Interoperability Resources)", "HL7 International", 2023, "standar", "https://hl7.org/fhir/",
  ["rme", "telemedisin", "patient-monitor"], ["manajemen-data", "simrs", "kdm"], "Standar pertukaran data kesehatan berbasis REST dan JSON.")
F("ieee802156", "IEEE 802.15.6: Wireless Body Area Networks", "IEEE", 2012, "standar", "",
  ["smartwatch", "holter", "patient-monitor"], ["kdm", "iot"], "Standar jaringan area tubuh yang dibahas di Komunikasi Data Medis.")

# ---------- Jurnal dan pedoman klinis ----------
F("spiro2019", "Standardization of Spirometry 2019 Update (ATS/ERS)", "Graham dkk.", 2019, "jurnal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC6794117", ["spirometer"], ["fisiologi", "kalibrasi"],
  "Kriteria manuver, kalibrasi syringe 3 L, dan interpretasi spirometri.")
F("aap2022", "AAP Clinical Practice Guideline: Hyperbilirubinemia in the Newborn", "American Academy of Pediatrics", 2022, "jurnal",
  "https://www.aap.org/en/patient-care/hyperbilirubinemia/", ["fototerapi"], ["tek-medik", "fisiologi"],
  "Ambang fototerapi dan pemantauan bilirubin pada bayi.")
F("pantompkins", "A Real-Time QRS Detection Algorithm", "Pan, Tompkins", 1985, "jurnal",
  "https://en.wikipedia.org/wiki/Pan%E2%80%93Tompkins_algorithm", ["ekg", "holter", "patient-monitor"], ["sinyal"],
  "Algoritma deteksi QRS yang paling banyak dipakai.")
F("loizou1998", "Mimicking the Human Ear (IEEE Signal Processing Magazine)", "Philipos C. Loizou", 1998, "jurnal",
  "https://ecs.utdallas.edu/loizou/cimplants/tutorial/tutorial.htm", ["implan-koklea"], ["telinga", "sinyal"],
  "Tutorial klasik pemrosesan sinyal implan koklea (strategi CIS).")
F("openmha", "Open Master Hearing Aid (openMHA): platform riset alat bantu dengar", "Kayser dkk.", 2022, "jurnal",
  "https://doaj.org/article/e189d4dbe0ca427b8d66faa5b412d873", ["alat-bantu-dengar"], ["sinyal", "telinga"],
  "Perangkat lunak terbuka untuk algoritma alat bantu dengar.")
F("ctgdb", "Open access intrapartum CTG database", "Chudáček dkk.", 2014, "jurnal",
  "https://pmc.ncbi.nlm.nih.gov/articles/PMC3898997", ["ctg"], ["sinyal", "ilmu-data"],
  "Deskripsi database CTG terbuka CTU-UHB.")
F("enable", "e-NABLE: komunitas tangan prostetik cetak 3D", "e-NABLE", 2024, "web",
  "https://en.wikipedia.org/wiki/E-NABLE", ["prostesis-tangan"], ["difabel", "purwarupa"],
  "Contoh nyata desain terbuka tangan prostetik body-powered yang bisa dicetak sendiri.")
F("ski2023", "Survei Kesehatan Indonesia (SKI) 2023", "Kementerian Kesehatan RI", 2023, "web",
  "https://www.badankebijakan.kemkes.go.id/hasil-ski-2023/", ["tensimeter", "glukometer"], ["visualisasi", "ilmu-data", "statistika"],
  "Data prevalensi nasional yang dipakai di kuliah Visualisasi Data.")

# ---------- Dataset dan perangkat lunak ----------
F("mitdb", "MIT-BIH Arrhythmia Database", "PhysioNet", 2005, "dataset", "https://physionet.org/content/mitdb/1.0.0/",
  ["ekg", "holter", "patient-monitor"], ["sinyal", "ml-medis"], "48 rekaman EKG 30 menit beranotasi, standar uji detektor aritmia.")
F("emgdb", "Examples of Electromyograms", "PhysioNet", 2009, "dataset", "https://physionet.org/content/emgdb/",
  ["emg"], ["sinyal", "fisiologi"], "Contoh EMG sehat, miopati, dan neuropati.")
F("kvasir", "Kvasir: dataset citra endoskopi saluran cerna", "Simula", 2017, "dataset", "https://datasets.simula.no/kvasir",
  ["endoskop"], ["citra", "ml-medis"], "Citra endoskopi beranotasi untuk klasifikasi temuan.")
F("radon", "scikit-image: transformasi Radon dan rekonstruksi", "scikit-image", 2024, "web",
  "https://scikit-image.org/docs/0.25.x/auto_examples/transform/plot_radon_transform.html",
  ["ct", "pet", "mammografi"], ["pencitraan", "kalkulus"], "Contoh FBP dan SART dengan Python.")
F("slicer", "3D Slicer Training Compendium", "3D Slicer", 2024, "web", "https://training.slicer.org/",
  ["ct", "mri", "xray", "brace-skoliosis"], ["pencitraan", "cad-medis"], "Pelatihan segmentasi dan visualisasi citra medis 3D.")
F("vam", "Virtual Anesthesia Machine", "University of Florida", 2024, "web",
  "https://simulation.health.ufl.edu/education-training/virtual-anesthesia-machine/", ["mesin-anestesi"], ["tek-bedah", "fisiologi"],
  "Simulator interaktif aliran gas di mesin anestesi.")
F("dvrk", "da Vinci Research Kit (dVRK)", "Johns Hopkins University", 2024, "web", "https://github.com/jhu-dvrk",
  ["robot-bedah"], ["robotika", "kendali"], "Perangkat lunak riset terbuka untuk robot bedah.")
F("webrtc", "WebRTC samples", "WebRTC Project", 2024, "web", "https://webrtc.github.io/samples/",
  ["telemedisin"], ["kdm", "mobile"], "Contoh kode video call di browser.")
