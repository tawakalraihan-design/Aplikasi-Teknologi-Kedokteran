"""12 buku di folder Referensi aplikasi (D:\\Project ITS\\1_aplikasi Teknologi Kedokteran\\Referensi).

Setiap buku menjadi satu entri referensi.json berjenis "pustaka" dengan daftar bab:
judul asli, judul Indonesia, halaman PDF, ringkasan, alat, dan mata kuliah terkait.
Halaman = nomor halaman di file PDF (bukan nomor cetak), diambil dari daftar isi
dan pencarian judul bab di teks PDF (tools/v5 di scratchpad: digest.py).
"""

PUSTAKA = []


def K(bid, nama, judul, penulis, tahun, penerbit, file, ket, bab, halaman):
    alat, materi = [], []
    for b in bab:
        for a in b[4]:
            if a not in alat:
                alat.append(a)
        for m in b[5]:
            if m not in materi:
                materi.append(m)
    PUSTAKA.append({
        "id": "pustaka-" + bid, "judul": judul, "penulis": penulis, "tahun": tahun, "jenis": "pustaka",
        "url": "", "file": "Referensi\\" + file, "alat": alat, "materi": materi, "ket": ket,
        "penerbit": penerbit, "halaman": halaman, "singkat": nama,
        "bab": [{"no": i + 1, "asli": b[0], "judul": b[1], "hal": list(b[2]), "ringkas": b[3], "alat": list(b[4]), "materi": list(b[5])}
                for i, b in enumerate(bab)],
    })


# ================================================================ 1
K("ai-health", "AI in Health", "Artificial Intelligence in Health (AIH 2018, LNAI 11326)",
  "Fernando Koch, Isabelle Bichindaritz dkk. (ed.)", 2019, "Springer", "1_Artificial Intelligence in Health.pdf",
  "Kumpulan 17 makalah riset AI kesehatan: NLP catatan klinis, penjadwalan perawatan rumah, deteksi nyeri dari wajah, regulasi AI sebagai alat medis, "
  "sampai deep learning untuk memprediksi readmisi. Bagus untuk melihat cara peneliti menulis masalah, metode, dan evaluasi AI medis.",
  [("MeSHx-Notes", "MeSHx-Notes: kamus istilah MeSH untuk catatan klinis", (18, 27),
    "Membangun kamus istilah medis dari MeSH yang diperluas dengan kata-kata mirip (word embedding) agar sistem bisa mengenali istilah di catatan dokter yang ditulis bebas.",
    ["rme"], ["ilmu-data", "data-mining", "simrs"]),
   ("Multiagent Systems to Support Planning and Scheduling in Home Health Care", "Sistem multiagen untuk penjadwalan perawatan rumah", (28, 43),
    "Tinjauan literatur penjadwalan perawat home care: model optimasi, agen yang bernegosiasi jadwal, dan tantangan data nyata seperti jarak tempuh dan preferensi pasien.",
    ["telemedisin"], ["simrs", "tatalaksana"]),
   ("Ethical Surveillance: Applying Deep Learning and Contextual Integrity", "Pengawasan etis pasien demensia dengan LSTM", (44, 62),
    "Memantau pola tidur dan gerak pasien demensia dengan LSTM sambil membatasi data yang dibagikan menurut teori contextual integrity, supaya privasi tetap terjaga.",
    ["smartwatch"], ["ml-medis", "big-data", "monitoring"]),
   ("Active Learning for Conversational Therapy Classification", "Active learning (QBEC) untuk klasifikasi percakapan terapi", (63, 73),
    "Melabeli ucapan sesi terapi itu mahal. Query-by-committee memilih sampel yang paling diperdebatkan model untuk dilabeli manusia, sehingga label sedikit tetapi model tetap akurat.",
    [], ["ml-medis", "data-mining"]),
   ("Analysis of Topic Propagation in Therapy Sessions using PLDA", "Penyebaran topik dalam sesi terapi (PLDA)", (74, 90),
    "Partially Labeled LDA menemukan topik dalam transkrip konselor-pasien dan melacak bagaimana topik berpindah dari satu pembicara ke yang lain.",
    [], ["data-mining", "ilmu-data"]),
   ("Dr. AI, Where Did You Get Your Degree?", "Dr. AI: regulasi AI sebagai alat medis", (91, 98),
    "Membahas AI-as-a-Medical-Device (AIaMD): mengapa AI yang terus belajar sulit diatur dengan regulasi alat medis biasa, dan usulan kerangka validasi berbasis hasil klinis.",
    ["oralytic", "brainwave"], ["ml-medis", "kalibrasi", "tatalaksana"]),
   ("Design Principles and Action Reflection for Assistive Agents", "Argumentasi untuk agen asisten", (99, 113),
    "Agen asisten untuk lansia memakai teori aktivitas dan argumentasi formal untuk memutuskan kapan membantu dan menjelaskan alasannya kepada pengguna.",
    [], ["interaksi-pasien", "difabel"]),
   ("Microsoft HoloLens for Medication Coaching", "HoloLens sebagai pelatih minum obat (MCIA)", (114, 130),
    "Prototipe augmented reality di HoloLens yang menampilkan rencana obat, cara minum, dan pengingat untuk meningkatkan kepatuhan pasien.",
    ["pill-dispenser"], ["mobile", "interaksi-pasien", "tek-keperawatan"]),
   ("A Knowledge-Based Simulation Framework (INCA)", "INCA: simulasi alur perawatan kanker berbasis pengetahuan", (131, 142),
    "Kerangka simulasi alur pasien kanker dari data rumah sakit untuk menguji keputusan klinis dan kapasitas layanan sebelum diterapkan.",
    ["rme"], ["simrs", "big-data", "tatalaksana"]),
   ("Lifted Maximum Expected Utility (MEU-LJT)", "Utilitas harapan maksimum pada model relasional", (143, 156),
    "Algoritma inferensi probabilistik 'lifted' untuk memilih tindakan terbaik bagi banyak pasien sekaligus tanpa menghitung satu per satu.",
    [], ["ml-medis", "statistika"]),
   ("The Role of Usability Engineering in PEPPER", "Rekayasa usability pada PEPPER (insulin diabetes tipe 1)", (157, 176),
    "Evaluasi usability sistem rekomendasi dosis bolus insulin: tugas pengguna, skala SUS, dan perbaikan antarmuka berdasarkan temuan.",
    ["glukometer", "infus"], ["interaksi-pasien", "dtk", "design-thinking"]),
   ("Automated Pain Detection in Facial Videos", "Deteksi nyeri otomatis dari video wajah", (177, 195),
    "Fitur facial action unit dari video anak pasca operasi dipakai untuk klasifikasi nyeri; transfer learning menjembatani fitur otomatis dan fitur hasil kode manusia.",
    [], ["ml-medis", "citra", "visualisasi"]),
   ("Towards Automated Pain Detection in Children (face + EDA)", "Fusi wajah dan EDA untuk deteksi nyeri anak", (196, 204),
    "Menggabungkan sinyal electrodermal activity dengan fitur wajah; fusi multimodal dan adaptasi domain antar-rumah sakit menaikkan akurasi.",
    ["smartwatch"], ["ml-medis", "sinyal", "sensor"]),
   ("Interpretation of Best Medical Coding Practices by CBR", "Case-based reasoning untuk pengodean kanker", (205, 213),
    "Sistem penalaran berbasis kasus membantu petugas registri kanker memilih kode yang tepat dengan argumen dari kasus serupa.",
    ["rme"], ["simrs", "manajemen-data"]),
   ("Identification of Serious Illness Conversations", "Deep learning menemukan percakapan penyakit serius di catatan klinis", (214, 227),
    "Jaringan saraf membaca catatan EHR untuk menemukan dokumentasi diskusi tujuan perawatan dengan F1 sekitar 0,92, jauh lebih cepat daripada tinjauan manual.",
    ["rme"], ["ml-medis", "data-mining"]),
   ("Generating Reward Functions Using IRL for Cancer Screening", "Inverse reinforcement learning untuk skrining kanker", (228, 242),
    "Skrining kanker payudara dan paru dimodelkan sebagai POMDP; inverse RL (MaxEnt) mempelajari fungsi reward dari keputusan dokter.",
    ["mammografi", "ct"], ["ml-medis", "tatalaksana"]),
   ("Deep Learning Architectures for Vector Representations of Patients", "Representasi vektor pasien (CNN/RNN) untuk readmisi 30 hari", (243, 261),
    "Riwayat pasien diubah menjadi vektor oleh CNN dan RNN, lalu dipakai memprediksi risiko rawat ulang 30 hari pada pasien penyakit kronis.",
    ["rme"], ["ml-medis", "big-data", "ilmu-data"])],
  261)

# ================================================================ 2
K("biosinyal", "Biosignal Processing", "Biosignal Processing: Principles and Practices",
  "Hualou Liang, Joseph D. Bronzino, Donald R. Peterson (ed.)", 2013, "CRC Press", "2_Biosignal Processing.pdf",
  "Dasar pengolahan sinyal biomedis dari akuisisi sampai analisis kausalitas jaringan otak: sampling, filter, representasi waktu-frekuensi, "
  "spektrum EEG, MEG, registrasi citra otak, fNIR, dan Granger causality. Pendamping kuat mata kuliah Pengolahan Sinyal Biomedik.",
  [("Digital Biomedical Signal Acquisition and Processing", "Akuisisi dan pengolahan sinyal biomedis digital", (18, 37),
    "Sampling dan teorema Nyquist, kuantisasi (SNR naik sekitar 6 dB tiap tambahan 1 bit ADC), filter FIR dan IIR, respons frekuensi, contoh EKG dan filter notch 50/60 Hz.",
    ["ekg", "eeg", "emg", "holter"], ["sinyal", "instrumen", "eldig"]),
   ("Time–Frequency Signal Representations for Biomedical Signals", "Representasi waktu-frekuensi", (38, 61),
    "Sinyal biomedis tidak stasioner. Bab ini membandingkan spektrogram (STFT), distribusi Wigner-Ville dan kelas Cohen, serta wavelet untuk melihat frekuensi yang berubah terhadap waktu.",
    ["eeg", "ekg", "usg"], ["sinyal", "matek"]),
   ("Multivariate Spectral Analysis of Electroencephalogram", "Analisis spektral multivariat EEG", (62, 85),
    "Spektrum daya EEG, koherensi antar-kanal, efek konduksi volume di kulit kepala, dan pemisahan sumber (SOBI) untuk melihat aktivitas otak yang sebenarnya.",
    ["eeg", "brainmapping", "neurofeedback"], ["sinyal", "fisiologi"]),
   ("General Linear Modeling of Magnetoencephalography Data", "Model linear umum untuk data MEG", (86, 113),
    "GLM menghubungkan sinyal MEG dengan desain eksperimen, lalu peta statistik kortikal dikoreksi untuk perbandingan berganda dengan uji permutasi.",
    ["brainmapping"], ["sinyal", "statistika"]),
   ("Emergence of Groupwise Registration in MR Brain Study", "Registrasi citra MRI otak secara berkelompok", (114, 135),
    "Alih-alih menyelaraskan tiap otak ke satu templat, registrasi groupwise menyelaraskan semua subjek ke pusat populasi agar atlas tidak bias.",
    ["mri", "motion-correction"], ["citra", "pencitraan"]),
   ("Functional Optical Brain Imaging (fNIR)", "Pencitraan otak optik fungsional (fNIR)", (136, 169),
    "Cahaya inframerah dekat mengukur perubahan oksi- dan deoksihemoglobin di korteks saat tugas kognitif; prinsip optik, desain sensor, dan pengolahan data hemodinamik.",
    ["oksimeter", "brainmapping"], ["fismed", "sensor", "sinyal"]),
   ("Causality Analysis of Multivariate Neural Data", "Analisis kausalitas data saraf multivariat", (170, 213),
    "Granger causality dan model autoregresif multivariat di domain waktu dan frekuensi untuk mengetahui area otak mana yang memengaruhi area lain.",
    ["eeg"], ["sinyal", "statistika", "matek"])],
  213)

# ================================================================ 3
K("vr-ar", "Emerging Tech (VR/AR)", "Emerging Technologies for Health and Medicine: Virtual Reality, Augmented Reality, AI, IoT, Robotics, Industry 4.0",
  "Dac-Nhuong Le, Chung Van Le, Jolanda G. Tromp, Gia Nhu Nguyen (ed.)", 2018, "Wiley-Scrivener", "3_Emerging technologies for health-VR-AR.pdf",
  "19 bab tentang VR/AR untuk pendidikan dan terapi, AI untuk diagnosis kanker dan stroke, telemedisin, robot rehabilitasi, brain-computer interface, "
  "dan IoT untuk tunanetra serta rumah pintar. Banyak ide proyek kecil yang bisa dicoba di mata kuliah IoT, Robotika, dan Desain.",
  [("Reviews of the Implications of VR/AR Health Care Applications", "Tinjauan aplikasi VR/AR di layanan kesehatan", (33, 49),
    "Peta penerapan VR dan AR: pelatihan bedah, terapi fobia dan nyeri, rehabilitasi, edukasi pasien, serta tantangan biaya dan validasi klinis.",
    [], ["cad-medis", "visualisasi", "tek-medik"]),
   ("Using 3D Simulation in Medical Education", "Simulasi 3D untuk belajar anatomi", (50, 62),
    "Studi kelas: mahasiswa yang belajar anatomi dengan VR dibandingkan model plastik; skor ujian dan respons belajar dianalisis.",
    [], ["anatomi", "cad-medis"]),
   ("Building Empathy in Young Children using Augmented Reality", "AR untuk membangun empati anak", (63, 69),
    "Aplikasi AR untuk anak prasekolah di Malaysia mengenalkan kondisi orang lain agar anak belajar empati.",
    [], ["design-thinking", "interaksi-pasien"]),
   ("Effectiveness of Virtual Reality Mock Interview Training", "Latihan wawancara kerja dengan VR", (70, 77),
    "VR mock interview untuk penganggur dengan kecemasan; pre-test dan post-test menunjukkan kecemasan menurun.",
    [], ["difabel", "metopen"]),
   ("Augmenting Dental Care: A Current Perspective", "AR dan VR di kedokteran gigi", (78, 94),
    "AR untuk bedah implan dan ortognatik, navigasi dental, simulasi pendidikan, serta edukasi pasien gigi. Relevan dengan proyek Oralytic.",
    ["oralytic", "robot-bedah"], ["cad-medis", "tek-bedah", "citra"]),
   ("Review of Virtual Reality Evaluation Methods and Psychophysiological Measurement Tools", "Metode evaluasi VR dan pengukuran psikofisiologis", (95, 115),
    "Cara menilai sistem VR: usability, presence, beban kerja, serta sinyal fisiologis (EEG, EDA, detak jantung) sebagai ukuran objektif.",
    ["eeg"], ["dtk", "metopen", "interaksi-pasien"]),
   ("AI Technologies for Mobile Health of Stroke Monitoring & Rehabilitation Robotics Control", "AI mHealth untuk stroke dan robot rehabilitasi", (116, 126),
    "Sinyal EMG nirkabel dikenali dengan klasifikasi cerdas untuk memantau pasien stroke dan mengendalikan robot rehabilitasi.",
    ["emg", "prostesis-tangan", "stimulasi-listrik"], ["robotika", "sinyal", "iot"]),
   ("Artificial Intelligence for Smart Cancer Diagnosis", "AI untuk diagnosis kanker payudara dan telemedisin", (127, 139),
    "Mamogram dipra-proses (filter median), disegmentasi dengan fuzzy C-means, lalu dikompresi untuk dikirim lewat telemedisin.",
    ["mammografi", "telemedisin"], ["citra", "ml-medis"]),
   ("Mobile Doctor Brain AI App", "Aplikasi Mobile Doctor Brain AI", (140, 150),
    "Aplikasi seluler untuk stroke: klasifikasi SVM, case-based reasoning, dan optimasi PSO untuk mendukung keputusan dari data pemantauan.",
    ["eeg", "telemedisin"], ["mobile", "ml-medis"]),
   ("An AI Mobile Cloud Computing Tool", "Teleradiologi cerdas berbasis cloud", (151, 157),
    "Case-based reasoning dan jaringan saraf di cloud untuk mencari kasus radiologi serupa dan membantu diagnosis kanker dari jarak jauh.",
    ["telemedisin", "xray"], ["big-data", "ml-medis", "kdm"]),
   ("Advanced Intelligent Robot Control Interfaces", "Antarmuka kendali robot di Unity3D", (158, 173),
    "Simulasi robot 5 derajat kebebasan di Unity3D: komponen sendi prismatik dan revolut, struktur kelas, dan antarmuka kendali virtual.",
    ["robot-bedah"], ["robotika", "kendali", "pemrograman"]),
   ("Analysis of Telemedicine Technologies", "Analisis teknologi telemedisin", (174, 183),
    "Jenis layanan telemedisin dan telehealth, manfaat untuk pasien jantung dan daerah terpencil, serta hambatan adopsi.",
    ["telemedisin"], ["kdm", "tatalaksana"]),
   ("Critical Position using Environment Model Applied on Walking Robots", "Posisi kritis robot berjalan", (184, 196),
    "Model matematis lingkungan dan dinamika robot berjalan untuk menemukan posisi kritis sebelum robot jatuh.",
    [], ["robotika", "biomekanik"]),
   ("The Walking Robot Equilibrium Recovery", "Pemulihan keseimbangan robot berjalan (NAO)", (197, 207),
    "Kendali keseimbangan robot bipedal saat diganggu, memakai model pergelangan kaki dan pengendali LQR.",
    ["prostesis-tangan"], ["kendali", "robotika", "biomekanik"]),
   ("Development of A Robotic Teaching Aid for Disabled Children", "Robot LEGO sebagai alat bantu belajar anak autis", (208, 218),
    "Robot LEGO Mindstorms dipakai mengajarkan bentuk dan interaksi sosial pada anak autis; hasil uji dibandingkan pengajaran biasa.",
    [], ["difabel", "robotika"]),
   ("Training System Design of Lower Limb Rehabilitation Robot based on VR", "Robot rehabilitasi tungkai bawah dengan VR", (219, 238),
    "Perencanaan lintasan sendi, kecepatan, dan percepatan robot rehabilitasi, dipadukan dengan game VR agar latihan lebih menarik.",
    ["brace-skoliosis", "stimulasi-listrik"], ["robotika", "biomekanik", "kendali"]),
   ("Automation of Appliances Using Electroencephalography", "Mengendalikan peralatan rumah dengan EEG (BCI)", (239, 257),
    "Dasar gelombang otak, elektroda invasif dan non-invasif, serta brain-computer interface untuk menyalakan perangkat rumah.",
    ["eeg", "brainwave", "neurofeedback"], ["sinyal", "iot", "difabel"]),
   ("Designing a Beautiful Life for Indian Blind Peoples: A Smart Stick", "Tongkat pintar ultrasonik untuk tunanetra", (258, 271),
    "Sensor ultrasonik dan NodeMCU mendeteksi rintangan lalu memberi bunyi buzzer; data bisa dikirim lewat IoT.",
    [], ["iot", "difabel", "sensor", "mikro"]),
   ("Smart Home: Personal Assistant and Baby Monitoring System", "Rumah pintar: asisten dan pemantau bayi", (272, 298),
    "Modul sensor suhu, suara, dan kamera dengan pengenalan wajah untuk memantau bayi dan memberi notifikasi ke orang tua.",
    ["inkubator", "termometer"], ["iot", "monitoring", "sistem-tertanam"])],
  298)

# ================================================================ 4
K("wearable", "Wearable Healthcare", "Healthcare Implementations of Wearable Technology (FTF-HCR-F0083)",
  "Jose Fernandez, Freescale Semiconductor", 2014, "Freescale Technology Forum (slide)", "4_Healthcare Implementations of Wearable Technology.pdf",
  "Slide seminar tentang WaRP (Wearable Reference Platform): desain hibrida prosesor i.MX 6SoloLite (Android) dan mikrokontroler Kinetis KL16, "
  "sensor pedometer MMA9553, papan detak jantung, pengisian nirkabel, dan teknik hemat daya. Rujukan praktis untuk merancang smartwatch kesehatan.",
  [("Wearable Market Description", "Pasar perangkat wearable", (5, 12),
    "Segmen wearable kesehatan dan kebugaran (monitor detak jantung, pedometer, pemantau aktivitas), tren pasar, dan ragam pemakaian.",
    ["smartwatch"], ["monitoring", "tatalaksana"]),
   ("Market Challenge", "Tantangan desain: daya, ruang, kemudahan pakai", (13, 15),
    "Konsumsi daya, ukuran kecil, dan kenyamanan menjadi kunci. Pengisian USB sudah standar; pengisian nirkabel lebih cocok untuk perangkat tahan air.",
    ["smartwatch"], ["dtk", "sistem-tertanam"]),
   ("Freescale Wearable Reference Platform: WaRP", "Platform referensi WaRP", (16, 39),
    "Arsitektur hibrida: papan utama i.MX 6SoloLite menjalankan Android dengan LP-DDR2, pengisi baterai LiPo, USB OTG, layar; papan tambahan Kinetis KL16 untuk sensor dan pedometer MMA9553L.",
    ["smartwatch"], ["sistem-tertanam", "mikro", "eldig"]),
   ("Healthcare and Fitness Daughter Board and Standalone Mode", "Papan anak kesehatan: detak jantung dan mode mandiri", (40, 45),
    "Papan sensor kesehatan (bersama ROHM) untuk detak jantung kontinu, EKG, dan pedometer; bisa jalan mandiri hanya dengan MCU untuk menghemat baterai.",
    ["smartwatch", "oksimeter", "ekg"], ["sensor", "instrumen", "monitoring"]),
   ("Kinetis L16 MCU Basics", "Dasar mikrokontroler Kinetis L (ARM Cortex-M0+)", (46, 63),
    "Inti Cortex-M0+, Bit Manipulation Engine, Fast I/O, dan periferal yang membuat MCU kecil cocok untuk perangkat wearable.",
    ["smartwatch", "pill-dispenser"], ["mikro", "sistem-tertanam"]),
   ("Kinetis L16 MCU Power Saving Modes", "Mode hemat daya mikrokontroler", (64, 98),
    "Mode Wait, Stop, VLPS, dan deep sleep; clock gating, DMA asinkron, UART/SPI/TPM yang tetap bekerja saat inti tidur, untuk memperpanjang umur baterai.",
    ["smartwatch", "holter"], ["mikro", "sistem-tertanam", "elda"]),
   ("Demo", "Demo dan contoh pemakaian", (99, 101),
    "Demonstrasi WaRP: penghitung langkah, pemantauan detak jantung, dan sinkronisasi ke aplikasi.",
    ["smartwatch"], ["iot", "mobile"])],
  101)

# ================================================================ 5
K("ehr", "Implementasi RME", "Implementing an Electronic Health Record System",
  "James M. Walker, Eric J. Bieber, Frank Richards (ed.)", 2005, "Springer", "5_Implementing an Electronic Health Record System.pdf",
  "Pengalaman Geisinger Health System menerapkan rekam medis elektronik (Epic) dari nol: kesiapan organisasi, pemilihan vendor, infrastruktur, "
  "alur kerja, pelatihan, clinical decision support, sampai portal pasien. Pegangan untuk mata kuliah SIMRS dan Manajemen Data.",
  [("Organizational Climate", "Iklim organisasi", (18, 23),
    "RME berhasil bila pimpinan dan dokter mendukung. Geisinger memandang investasi TI sebagai strategi klinis, bukan sekadar biaya.",
    ["rme"], ["simrs", "tatalaksana"]),
   ("Needs Assessment", "Analisis kebutuhan", (24, 29),
    "Menetapkan tujuan dan ukuran keberhasilan sebelum membeli sistem: proses apa yang ingin diperbaiki dan bagaimana mengukurnya.",
    ["rme"], ["simrs", "design-thinking"]),
   ("Vendor Selection and Contract Negotiation", "Memilih vendor dan negosiasi kontrak", (30, 35),
    "Kriteria memilih vendor RME, kunjungan ke pengguna lain, isi kontrak (akses data, dukungan, biaya), dan rencana bila vendor gagal.",
    ["rme"], ["simrs", "kalibrasi"]),
   ("Infrastructure", "Infrastruktur jaringan dan server", (36, 50),
    "Bandwidth, server, keamanan, akses jarak jauh, dan ketersediaan tinggi. RME yang lambat akan ditinggalkan dokter.",
    ["rme", "telemedisin"], ["kdm", "simrs", "big-data"]),
   ("Workflow Assessment and Redesign", "Penilaian dan desain ulang alur kerja", (51, 54),
    "Memetakan alur kerja klinik (janji temu, pengambilan rekam medis) dan mendesain ulangnya agar RME menyederhanakan, bukan menambah pekerjaan.",
    ["rme"], ["simrs", "dtk"]),
   ("Staffing and Managing Implementation Teams", "Tim implementasi", (55, 59),
    "Peran physician champion, analis klinis, CMIO, dan staf sementara; cara mengelola tim saat go-live.",
    ["rme"], ["simrs", "tatalaksana"]),
   ("Usability", "Usability RME", (60, 70),
    "Prinsip antarmuka klinis: beban memori, tampilan hasil lab, uji usability dengan pengguna nyata, dan contoh kesalahan desain.",
    ["rme"], ["interaksi-pasien", "dtk", "visualisasi"]),
   ("Training", "Pelatihan pengguna", (71, 79),
    "Merancang pelatihan berbasis tugas nyata, pelatih dari kalangan klinis, lingkungan latihan, dan dukungan saat go-live.",
    ["rme"], ["simrs"]),
   ("Clinical Decision Support", "Clinical decision support (CDS)", (80, 89),
    "Pengingat, order set, dan peringatan yang membantu dokter tanpa menimbulkan kelelahan alarm.",
    ["rme"], ["simrs", "ml-medis", "tatalaksana"]),
   ("Translating Scope of Practice", "Menerjemahkan kewenangan klinis ke sistem", (90, 101),
    "Siapa boleh memesan apa: aturan supervisi, otorisasi order, dan peran tiap profesi diatur di RME.",
    ["rme"], ["simrs"]),
   ("System Integration", "Integrasi sistem", (102, 104),
    "Menghubungkan RME dengan penjadwalan, lab, radiologi, dan billing lewat antarmuka dan basis data bersama.",
    ["rme", "kimia-klinik"], ["kdm", "manajemen-data"]),
   ("Production Support", "Dukungan operasional", (105, 113),
    "Help desk, penanganan masalah, upgrade, dan keterampilan tim pendukung setelah sistem berjalan.",
    ["rme"], ["simrs"]),
   ("Managing the Client-Vendor Partnership", "Mengelola kemitraan dengan vendor", (114, 121),
    "Membangun hubungan jangka panjang dengan vendor: kelompok pengguna, permintaan fitur, dan eskalasi.",
    ["rme"], ["simrs", "tatalaksana"]),
   ("Phased Implementation", "Implementasi bertahap", (122, 130),
    "Menerapkan RME per klinik dan per fitur: daftar masalah, order entry, billing; pelajaran dari tiap gelombang go-live.",
    ["rme"], ["simrs"]),
   ("Optimizing Primary-Care Practices", "Optimasi di layanan primer", (131, 138),
    "Pesan internal, preferensi pengguna, dan pembagian tugas perawat-dokter agar RME menghemat waktu di klinik umum.",
    ["rme"], ["simrs", "tek-keperawatan"]),
   ("Optimizing Specialty Practices", "Optimasi di klinik spesialis", (139, 140),
    "Klinik spesialis butuh templat dan order khusus; implementasi menyesuaikan kompleksitasnya.",
    ["rme"], ["simrs"]),
   ("Special-Purpose Software", "Perangkat lunak khusus", (141, 151),
    "Kapan memakai software khusus (misal uji klinis, onkologi) di samping RME inti dan cara mengintegrasikannya.",
    ["rme"], ["simrs", "manajemen-data"]),
   ("Optimizing Inpatient Care", "RME di rawat inap: CPOE dan dokumentasi", (152, 163),
    "Computerized physician order entry, order set standar, catatan klinis, dan ringkasan pulang di bangsal.",
    ["rme", "infus"], ["simrs", "tek-keperawatan"]),
   ("Extending EHR Access to Patients", "Portal pasien", (164, 175),
    "Akses pasien ke rekam medis dan pesan aman: kata sandi, dukungan, akses orang tua, dan dampaknya ke beban kerja.",
    ["rme", "telemedisin"], ["simrs", "interaksi-pasien", "mobile"]),
   ("Extending EHR Access to External Physicians", "Akses untuk dokter luar", (176, 181),
    "Portal untuk dokter perujuk agar komunikasi dan kesinambungan perawatan lebih baik.",
    ["rme"], ["simrs", "kdm"]),
   ("Summary and Prospects", "Ringkasan, prospek, dan lampiran", (182, 252),
    "Rangkuman pelajaran Geisinger dan lampiran contoh dokumen: kebijakan keamanan, daftar periksa, dan formulir implementasi.",
    ["rme"], ["simrs", "manajemen-data"])],
  252)

# ================================================================ 6
K("lab", "Teknologi Lab Medis", "Introduction to Medical Laboratory Technology, ed. 5",
  "F. J. Baker, R. E. Silverton", 1976, "Butterworths", "6_Introduction to Medical Laboratory Technology.pdf",
  "Buku klasik teknisi laboratorium medis: peralatan gelas, mikroskop, kimia klinik, histologi, mikrobiologi, hematologi, dan golongan darah. "
  "Menjelaskan prinsip di balik alat laboratorium modern di aplikasi ini (hematology analyzer, kimia klinik, koagulasi, urin analyzer, autoklaf).",
  [("General Laboratory Glassware", "Peralatan gelas laboratorium", (8, 29),
    "Jenis gelas, pipet, labu, tabung sentrifus, cara membersihkan, dan air suling atau deionisasi.",
    ["sentrifus"], ["kimia", "k3"]),
   ("Elementary Microscopy", "Dasar mikroskopi", (30, 63),
    "Lensa, objektif, okuler, kondensor, diafragma, panjang fokus, dan cara memfokuskan untuk mendapat citra tajam.",
    ["mikroskop"], ["fisdas", "biologi-kedokteran"]),
   ("Safety Precautions", "Keselamatan laboratorium", (64, 70),
    "Penyimpanan bahan kimia mudah terbakar dan korosif, pertolongan pertama, dan kebiasaan aman di laboratorium.",
    ["autoklaf"], ["k3", "kimia"]),
   ("Collection and Reporting of Specimens", "Pengambilan dan pelaporan spesimen", (71, 79),
    "Wadah, antikoagulan, swab steril, pelabelan, dan pelaporan hasil agar spesimen tidak rusak atau tertukar.",
    ["hematologi", "urin-analyzer"], ["biologi-kedokteran", "manajemen-data"]),
   ("Some Fundamentals of Chemistry", "Dasar kimia: larutan dan titrasi", (80, 114),
    "Mol, ekuivalen, larutan standar, asam-basa, indikator, dan titrasi sebagai dasar semua pemeriksaan kimia.",
    ["kimia-klinik", "elektrolit"], ["kimia"]),
   ("Instrumentation", "Instrumentasi: kolorimetri, elektroda, kromatografi", (115, 156),
    "Hukum Beer-Lambert dan absorbansi, kolorimeter dan fotometer, elektroda pH, elektroforesis, dan kromatografi kertas.",
    ["kimia-klinik", "elektrolit", "immunoassay"], ["instrumen", "fismed", "kimia"]),
   ("Introduction to Clinical Chemistry", "Pengantar kimia klinik", (157, 174),
    "Cairan tubuh, plasma, hormon (tiroid, pituitari), dan metabolisme sebagai dasar memahami hasil laboratorium.",
    ["kimia-klinik"], ["fisiologi", "biologi-kedokteran"]),
   ("Gastric and Pancreatic Function", "Fungsi lambung, pankreas, dan glukosa darah", (175, 220),
    "Uji asam lambung, enzim pankreas, uji toleransi glukosa, dan pemeriksaan feses.",
    ["glukometer", "kimia-klinik"], ["fisiologi", "kimia"]),
   ("Liver Function Tests", "Uji fungsi hati", (221, 235),
    "Bilirubin, urobilinogen (reagen Ehrlich), garam empedu, dan jenis ikterus.",
    ["kimia-klinik", "fototerapi"], ["fisiologi", "kimia"]),
   ("Renal Function Tests", "Uji fungsi ginjal dan urinalisis", (236, 285),
    "Protein, glukosa, dan urea urin, strip reagen, bersihan, dan uji pemekatan.",
    ["urin-analyzer", "hemodialisis", "kimia-klinik"], ["fisiologi", "kimia"]),
   ("Chemical Analysis of Cerebrospinal Fluid", "Analisis kimia cairan serebrospinal", (286, 299),
    "Protein, globulin, glukosa, dan klorida CSF serta artinya pada meningitis.",
    ["kimia-klinik"], ["anatomi", "kimia"]),
   ("Introduction to Histology", "Pengantar histologi", (300, 312),
    "Sel, jaringan, inti, sitoplasma, dan pembelahan sel sebagai dasar membaca preparat.",
    ["mikroskop"], ["biologi-kedokteran", "anatomi"]),
   ("Fixation", "Fiksasi jaringan", (313, 328),
    "Formalin dan fiksatif lain menghentikan pembusukan dan mempertahankan struktur jaringan.",
    ["mikroskop"], ["biologi-kedokteran", "kimia"]),
   ("Decalcification", "Dekalsifikasi", (329, 337),
    "Melunakkan tulang dan gigi dengan asam atau kelator agar bisa diiris; uji titik akhir dekalsifikasi.",
    ["mikroskop"], ["biologi-kedokteran", "biomaterial"]),
   ("Dehydration, Clearing and Embedding", "Dehidrasi, penjernihan, dan penanaman paraffin", (338, 358),
    "Alkohol bertingkat, clearing, dan paraffin atau celloidin untuk membuat blok jaringan.",
    ["mikroskop"], ["biologi-kedokteran"]),
   ("Section Cutting", "Pemotongan dengan mikrotom", (359, 384),
    "Jenis mikrotom, sudut dan ketajaman pisau, ketebalan irisan, dan potong beku.",
    ["mikroskop"], ["biologi-kedokteran", "fisika-mekanika"]),
   ("Biological Staining", "Prinsip pewarnaan biologis", (385, 393),
    "Zat warna asam dan basa, hematoksilin, mordan, dan mengapa jaringan menyerap warna berbeda.",
    ["mikroskop"], ["kimia", "biologi-kedokteran"]),
   ("Staining Procedures", "Prosedur pewarnaan", (394, 426),
    "Langkah pewarnaan H&E dan pewarnaan khusus: larutan, waktu, dan hasil yang diharapkan.",
    ["mikroskop"], ["biologi-kedokteran"]),
   ("Cytological Techniques", "Teknik sitologi", (427, 438),
    "Apusan sel, fiksasi alkohol, dan pewarnaan Papanicolaou untuk skrining sel abnormal.",
    ["mikroskop"], ["biologi-kedokteran", "citra"]),
   ("Introduction to Microbiology", "Pengantar mikrobiologi", (439, 448),
    "Bakteri, virus, bentuk kokus dan basil, dan hubungan mikroorganisme dengan penyakit.",
    [], ["biologi-kedokteran"]),
   ("Microscopic Examination of Bacteria", "Pemeriksaan bakteri dengan mikroskop (Gram)", (449, 462),
    "Membuat apusan, fiksasi panas, pewarnaan Gram dan Ziehl-Neelsen.",
    ["mikroskop"], ["biologi-kedokteran"]),
   ("Sterilization", "Sterilisasi", (463, 473),
    "Uap bertekanan (autoklaf), panas kering, dan filtrasi; hubungan suhu, tekanan, waktu, dan spora.",
    ["autoklaf"], ["fluida", "k3", "biologi-kedokteran"]),
   ("The Use of Culture Media", "Penggunaan media kultur", (474, 478),
    "Inokulasi cawan petri dan tabung, isolasi koloni, dan syarat media yang baik.",
    [], ["biologi-kedokteran"]),
   ("Preparation of Culture Media", "Pembuatan media kultur", (479, 507),
    "Agar, kaldu nutrien, agar darah, pH, dan sterilisasi media.",
    ["autoklaf"], ["biologi-kedokteran", "kimia"]),
   ("Anaerobic Cultivation", "Kultur anaerob", (508, 512),
    "Toples anaerob, penggantian udara dengan hidrogen, dan indikator kondisi tanpa oksigen.",
    [], ["biologi-kedokteran"]),
   ("Antigen–Antibody Reactions", "Reaksi antigen-antibodi", (513, 517),
    "Aglutinasi, pengenceran serum, dan dasar uji serologi.",
    ["immunoassay"], ["biologi-kedokteran"]),
   ("Bacteriological Examination", "Pemeriksaan bakteriologis spesimen", (518, 544),
    "Pemeriksaan darah, sputum, urin, dan swab; inkubasi, identifikasi, dan uji kepekaan antibiotik.",
    [], ["biologi-kedokteran"]),
   ("Introduction to Haematology", "Pengantar hematologi", (545, 556),
    "Sel darah merah, sel darah putih, trombosit, sumsum tulang, dan morfologi pada apusan.",
    ["hematologi"], ["fisiologi", "biologi-kedokteran"]),
   ("Blood Coagulation", "Pembekuan darah", (557, 561),
    "Jalur intrinsik dan ekstrinsik, faktor pembekuan, protrombin, trombin, dan fibrin.",
    ["koagulasi"], ["fisiologi"]),
   ("Enumeration of Blood Cells", "Menghitung sel darah", (562, 595),
    "Hemositometer, pipet pengencer, kotak hitung, dan rumus jumlah sel; dasar sebelum ada hematology analyzer.",
    ["hematologi", "mikroskop"], ["instrumen", "statistika"]),
   ("Haemoglobin Estimation", "Pengukuran hemoglobin", (596, 602),
    "Metode absorptiometri dengan larutan standar dan konversi ke g/dL.",
    ["hematologi"], ["instrumen", "fismed"]),
   ("Erythrocyte Sedimentation Rate", "Laju endap darah dan fragilitas", (603, 610),
    "Metode Westergren dan Wintrobe, volume sel padat, dan uji fragilitas osmotik.",
    ["hematologi", "sentrifus"], ["fisiologi"]),
   ("Tests for Blood Coagulation", "Uji pembekuan darah", (611, 616),
    "Waktu perdarahan, waktu pembekuan, dan waktu protrombin.",
    ["koagulasi"], ["fisiologi", "instrumen"]),
   ("Haematological Indices", "Indeks hematologi", (617, 629),
    "MCV, MCH, dan MCHC dihitung dari hitung eritrosit, hemoglobin, dan hematokrit.",
    ["hematologi"], ["statistika", "fisiologi"]),
   ("Inheritance of the ABO Groups", "Pewarisan golongan darah ABO", (630, 632),
    "Genotipe, fenotipe, dan kemungkinan golongan darah anak dari orang tua.",
    [], ["biologi-kedokteran"]),
   ("The Rhesus System", "Sistem Rhesus", (633, 636),
    "Antigen D, Rh positif dan negatif, dan risiko inkompatibilitas pada kehamilan.",
    [], ["biologi-kedokteran"]),
   ("Blood Group Immunoglobulins", "Imunoglobulin golongan darah", (637, 644),
    "Antibodi IgM dan IgG, uji antiglobulin (Coombs).",
    ["immunoassay"], ["biologi-kedokteran"]),
   ("Blood Transfusion", "Transfusi darah", (645, 657),
    "Seleksi donor, penyimpanan darah di suhu terkendali, antikoagulan, dan pencegahan infeksi.",
    ["infus"], ["fisiologi", "k3"]),
   ("Blood Grouping Technique", "Teknik penggolongan darah dan lampiran", (658, 730),
    "Uji golongan darah di slide dan tabung, uji silang (crossmatch), serta lampiran metode dan tabel.",
    ["immunoassay", "sentrifus"], ["biologi-kedokteran", "instrumen"])],
  730)

# ================================================================ 7
K("alkes-bedah", "Medical Devices (Bedah & Citra)", "Medical Devices: Surgical and Image-Guided Technologies",
  "Martin Culjat, Rahul Singh, Hua Lee (ed.)", 2013, "Wiley", "7_Medical devices and technology.pdf",
  "Buku teknik alat medis untuk bedah dan pencitraan: proses desain dan regulasi, laparoskopi, bedah mata, robot bedah, kateter, elektrosurgeri, ablasi, "
  "laser, stent, alat bantu jantung, implan ortopedi, endoskopi, USG, sinar-X, dan neuronavigasi. Sangat dekat dengan Teknologi Bedah dan Pencitraan.",
  [("Introduction", "Pengantar dan sejarah alat medis", (25, 34),
    "Sejarah alat bedah dari zaman kuno sampai rekayasa modern, dan klasifikasi besar alat medis.",
    [], ["pengantar-tekkes", "tek-bedah"]),
   ("Design of Medical Devices", "Desain dan regulasi alat medis", (35, 52),
    "Alur pengembangan dari konsep, prototipe, verifikasi-validasi, manajemen risiko, kelas alat (I, II, III), standar internasional, sampai produksi.",
    ["oralytic"], ["dtk", "purwarupa", "kalibrasi"]),
   ("Instrumentation for Laparoscopic Surgery", "Instrumen bedah laparoskopi", (53, 72),
    "Trokar, insuflasi, grasper, gunting, stapler, dan teknik akses perut minimal invasif.",
    ["endoskop", "robot-bedah"], ["tek-bedah", "biomekanik"]),
   ("Surgical Instruments in Ophthalmology", "Instrumen bedah mata: fakoemulsifikasi dan vitrektomi", (73, 86),
    "Handpiece ultrasonik memecah lensa katarak, sistem irigasi-aspirasi menjaga tekanan bola mata, pemotong vitreus untuk bedah retina.",
    ["fakoemulsifikasi"], ["tek-bedah", "fluida"]),
   ("Surgical Robotics", "Robot bedah", (87, 122),
    "Sistem master-slave, tingkat otonomi, robot ortopedi dan bedah saraf, umpan balik gaya, dan tantangan keselamatan.",
    ["robot-bedah"], ["robotika", "kendali", "tek-bedah"]),
   ("Catheters in Vascular Therapy", "Kateter dan guidewire", (123, 144),
    "Desain kateter, guidewire, balon angioplasti, dan cara alat dinavigasi di dalam pembuluh darah.",
    ["kateter-stent", "fluoroskopi"], ["biomaterial", "tek-bedah"]),
   ("Energy-Based Hemostatic Surgical Devices", "Alat hemostasis berbasis energi (elektrosurgeri)", (145, 160),
    "Arus frekuensi tinggi memotong dan mengoagulasi jaringan; mode monopolar dan bipolar, elektroda netral, dan bahaya luka bakar.",
    ["esu"], ["k3", "fisika-listrik-magnet", "tek-bedah"]),
   ("Tissue Ablation Systems", "Sistem ablasi jaringan (RFA, mikrogelombang, krio)", (161, 186),
    "Panas atau dingin menghancurkan tumor; deposisi energi, pemodelan suhu, dan pemantauan zona ablasi.",
    ["rfa", "diatermi-mw"], ["fismed", "tek-bedah"]),
   ("Lasers in Medicine", "Laser dalam kedokteran", (187, 222),
    "Prinsip laser, interaksi laser-jaringan (fototermal, fotoablasi), laser retina, dermatologi, dan OCT.",
    ["laser-medis", "fototerapi"], ["fismed", "radiasi"]),
   ("Vascular and Cardiovascular Devices", "Stent dan katup jantung transkateter", (223, 242),
    "Stent logam dan pelepas obat, nitinol yang bisa kembali ke bentuk asal, katup transkateter, dan desain permukaan.",
    ["kateter-stent"], ["biomaterial", "tek-bedah"]),
   ("Mechanical Circulatory Support Devices", "Alat bantu sirkulasi mekanis (LVAD, IABP)", (243, 264),
    "Pompa darah pulsatil dan kontinu (HeartMate), balon intra-aorta, kontrol aliran, dan komplikasi.",
    ["lvad"], ["fluida", "kendali", "biomaterial"]),
   ("Orthopedic Implants", "Implan ortopedi", (265, 300),
    "Penggantian sendi panggul dan lutut, implan tulang belakang, fiksasi fraktur, keausan permukaan, dan pemilihan material.",
    ["brace-skoliosis", "prostesis-tangan"], ["biomaterial", "biomekanik", "cad-medis"]),
   ("Endoscopy", "Endoskopi", (301, 326),
    "Endoskop kaku dan fleksibel, sumber cahaya, kamera video, kanal instrumen, dan desain optik.",
    ["endoskop"], ["tek-bedah", "pencitraan"]),
   ("Medical Ultrasound Devices", "Perangkat ultrasonografi", (327, 364),
    "Material piezoelektrik, transduser larik linear dan fase, pembentukan berkas, frekuensi dan resolusi, serta aplikasi terapi.",
    ["usg", "terapi-us"], ["pencitraan", "sensor", "fismed"]),
   ("Medical X-ray Imaging", "Pencitraan sinar-X", (365, 398),
    "Produksi foton, interaksi dengan jaringan, film versus detektor digital, ukuran piksel, dan teknik akuisisi.",
    ["xray", "fluoroskopi", "mammografi", "ct"], ["radiasi", "pencitraan"]),
   ("Navigation in Neurosurgery", "Navigasi dalam bedah saraf", (399, 454),
    "Pelacakan optik dan elektromagnetik, registrasi citra ke pasien, USG intraoperatif, dan ablasi laser terarah.",
    ["neuronavigasi", "mri", "ct"], ["tek-bedah", "citra", "robotika"])],
  454)

# ================================================================ 8
K("etika", "Etika Medis", "Medical Ethics in Clinical Practice",
  "Matjaž Zwitter", 2019, "Springer", "8_Medical Ethics in Clinical Practice.pdf",
  "Etika kedokteran yang dekat dengan praktik: empat prinsip (otonomi, beneficence, non-maleficence, keadilan), komunikasi, malapraktik, sumber daya "
  "terbatas, awal dan akhir kehidupan, genetika, riset klinis, dan seminar kasus untuk mahasiswa. Penting untuk alat yang menyentuh data dan keputusan pasien.",
  [("Ethics and Law", "Etika dan hukum", (14, 18), "Beda norma etika dan aturan hukum, serta kapan keduanya berbenturan.", [], ["interaksi-pasien", "tatalaksana"]),
   ("Ethical Codes and Declarations", "Kode etik dan deklarasi", (19, 25), "Sumpah Hipokrates, Deklarasi Helsinki dan Jenewa, serta kode etik profesi.", [], ["interaksi-pasien", "metopen"]),
   ("Ethical Theories", "Teori etika", (26, 32), "Utilitarianisme, etika kebajikan, deontologi, dan empat prinsip bioetika.", [], ["interaksi-pasien"]),
   ("Moral Status", "Status moral", (33, 38), "Siapa yang punya hak moral: embrio, pasien koma, hewan percobaan.", [], ["biologi-kedokteran"]),
   ("Ethical Analysis", "Analisis etika kasus", (39, 44), "Langkah menimbang manfaat, risiko, dan otonomi; contoh penolakan transfusi.", ["infus"], ["interaksi-pasien", "tatalaksana"]),
   ("Autonomy and Its Limitations", "Otonomi dan batasnya", (45, 46), "Hak pasien memutuskan, pengambil keputusan pengganti, dan kapan otonomi dibatasi.", [], ["interaksi-pasien"]),
   ("Communication", "Komunikasi dengan pasien", (47, 62), "Menyampaikan kabar buruk, informed consent, dan informasi bagi keluarga.", ["telemedisin"], ["interaksi-pasien"]),
   ("Relations in the Medical Team", "Hubungan dalam tim medis", (63, 66), "Kerja sama dokter-perawat, perbedaan pendapat, dan komunikasi tim.", [], ["tek-keperawatan"]),
   ("Professional Malpractice", "Malapraktik", (67, 72), "Kesalahan medis, kompensasi, peran media, dan budaya belajar dari kesalahan.", ["rme"], ["k3", "kalibrasi"]),
   ("Limited Resources, Priorities", "Sumber daya terbatas dan prioritas", (73, 81), "Daftar tunggu, biaya, korupsi, dan cara adil membagi layanan.", [], ["tatalaksana", "simrs"]),
   ("Image of a Physician", "Citra dokter", (82, 89), "Kepercayaan publik, praktik swasta, burnout, dan keberatan hati nurani.", [], ["interaksi-pasien"]),
   ("Preventive Medicine", "Kedokteran pencegahan", (90, 94), "Vaksinasi, skrining, gaya hidup, dan etika program kesehatan masyarakat.", ["oralytic"], ["tek-medik"]),
   ("Ethics at the Beginning of Life", "Etika di awal kehidupan", (95, 103), "Kontrasepsi, aborsi, reproduksi berbantu, dan diagnosis prenatal.", ["usg", "ctg"], ["biologi-kedokteran"]),
   ("Pediatrics", "Pediatri", (104, 111), "Hak anak, keputusan orang tua, penolakan vaksin, dan riset pada anak.", ["inkubator"], ["interaksi-pasien"]),
   ("Genetics", "Genetika", (112, 119), "Uji genetik, konseling, kerahasiaan, dan seleksi embrio.", [], ["biologi-kedokteran"]),
   ("Emergency Medicine and Transplantation", "Gawat darurat, ICU, dan transplantasi", (120, 125), "Menghentikan terapi di ICU, mati batang otak, dan donasi organ.", ["ventilator", "patient-monitor"], ["tek-medik"]),
   ("The Elderly and the Mentally Ill", "Lansia dan pasien gangguan jiwa", (126, 133), "Otonomi yang berkurang, perawatan paksa, dan perlindungan dari penelantaran.", ["pill-dispenser"], ["interaksi-pasien", "difabel"]),
   ("Dying and Death", "Menjelang kematian", (134, 140), "Perawatan paliatif, eutanasia, dan bunuh diri berbantuan dokter.", [], ["interaksi-pasien"]),
   ("Research", "Riset dan uji klinis", (141, 155), "Fase uji klinis, informed consent, komite etik, dan plasebo.", ["oralytic"], ["metopen", "statistika"]),
   ("Unproven Methods of Diagnostics and Treatment", "Metode diagnosis dan terapi yang belum terbukti", (156, 161), "Pengobatan alternatif, hak pasien memilih, dan tanggung jawab dokter.", [], ["metopen"]),
   ("Physicians Beyond Patient Care", "Dokter di luar pelayanan pasien", (162, 169), "Kedokteran olahraga, industri farmasi, dan konflik kepentingan.", [], ["tatalaksana"]),
   ("Student Seminars", "Seminar kasus mahasiswa", (170, 217), "Kumpulan kasus untuk diskusi kelompok dengan pertanyaan pemandu.", [], ["interaksi-pasien", "design-thinking"])],
  217)

# ================================================================ 9
K("telemedisin", "Telemedicine Technologies", "Telemedicine Technologies: Information Technologies in Medicine and Telehealth",
  "Bernard Fong, A. C. M. Fong, C. K. Li", 2011, "Wiley", "9_Telemedicine Technologies_ Information Technologies in Medicine.pdf",
  "Teknologi di balik telemedisin: jaringan komunikasi, pemantauan pasien nirkabel, pengolahan informasi medis, penerapan sistem, keamanan data, "
  "dan perawatan komunitas. Pendamping mata kuliah Komunikasi Data Medis, IoT, dan Sistem Monitoring.",
  [("Introduction", "Pengantar telemedisin", (25, 38), "Definisi, sejarah, layanan, dan peran internet serta sensor dalam telemedisin.", ["telemedisin"], ["kdm", "pengantar-tekkes"]),
   ("Communication Networks and Services", "Jaringan dan layanan komunikasi", (39, 60), "Sinyal, kanal radio, modulasi, pemancar-penerima, dan jaringan kabel maupun nirkabel.", ["telemedisin"], ["kdm", "iot"]),
   ("Wireless Technology in Patient Monitoring", "Teknologi nirkabel untuk pemantauan pasien", (61, 90), "Body area network, sensor yang dikenakan, pemantauan di rumah sakit dan rumah, serta keandalan tautan.", ["patient-monitor", "smartwatch", "holter"], ["monitoring", "iot", "kdm"]),
   ("Technologies in Medical Information Processing", "Pengolahan informasi medis", (91, 130), "Pengukuran tanda vital, citra medis, kompresi, dan pengolahan data jantung serta darah.", ["ekg", "tensimeter", "rme"], ["sinyal", "citra", "manajemen-data"]),
   ("Wireless Telemedicine System Deployment", "Menerapkan sistem telemedisin nirkabel", (131, 160), "Perencanaan jaringan, lapisan protokol, akses kanal, kapasitas, dan kualitas layanan.", ["telemedisin"], ["kdm", "iot"]),
   ("Technologies for Safeguarding Medical Data and Privacy", "Keamanan dan privasi data medis", (161, 194), "Enkripsi, autentikasi, watermark citra, dan kebijakan privasi informasi kesehatan.", ["rme", "telemedisin"], ["kdm", "manajemen-data", "simrs"]),
   ("Information Technology in Alternative Medicine", "TI dalam pengobatan alternatif", (195, 218), "Sensor tubuh, latihan, dan basis data pengobatan tradisional.", [], ["iot", "ilmu-data"]),
   ("Caring for the Community", "Perawatan komunitas dan telecare", (219, 252), "Telecare untuk lansia, alarm darurat, dan layanan kesehatan berbasis komunitas.", ["telemedisin", "pill-dispenser"], ["monitoring", "tek-keperawatan"]),
   ("Future Trends in Healthcare Technology", "Tren masa depan", (253, 284), "Rumah pintar, jaringan nirkabel generasi baru, dan sistem kesehatan terhubung.", ["smartwatch", "telemedisin"], ["iot", "big-data"])],
  284)

# ================================================================ 10
K("crispr", "Precision Medicine & CRISPR", "Precision Medicine, CRISPR, and Genome Engineering (AEMB 1016)",
  "Stephen H. Tsang (ed.)", 2017, "Springer", "10_Precision Medicine, CRISPR, and Genome Engineering.pdf",
  "Rekayasa genom untuk kedokteran presisi: vektor virus, AAV dengan nuklease, CRISPR dalam biologi perkembangan, fasilitas hewan transgenik, "
  "zebrafish, tanaman, skrining CRISPR untuk target obat, retina, dan masa depan serta etikanya. Konteks untuk Studi Lanjutan dan Biologi Kedokteran.",
  [("Viral Vectors, Engineered Cells and the CRISPR Revolution", "Vektor virus, sel rekayasa, dan revolusi CRISPR", (10, 34), "Adenovirus, lentivirus, dan AAV sebagai kurir gen; terapi gen dan sel CAR-T; bagaimana CRISPR-Cas mempercepat penyuntingan.", [], ["biologi-kedokteran"]),
   ("Combining Engineered Nucleases with Adeno-associated Viral Vectors", "Nuklease rekayasa + vektor AAV", (35, 49), "Mengantar CRISPR, TALEN, dan ZFN ke jaringan in vivo dengan AAV: kapasitas muatan dan target jaringan.", [], ["biologi-kedokteran"]),
   ("From Reductionism to Holism: CRISPR in Developmental Biology", "Dari reduksionisme ke holisme", (50, 79), "dCas untuk mengatur ekspresi gen, epigenetik, sel punca, dan skrining genom luas.", [], ["biologi-kedokteran", "big-data"]),
   ("A Transgenic Core Facility's Experience in Genome Editing", "Pengalaman fasilitas hewan transgenik", (80, 95), "Merancang sgRNA, injeksi zigot mencit, dan mengukur keberhasilan penyuntingan.", [], ["biologi-kedokteran", "metopen"]),
   ("Genome Editing to Study Ca2+ Homeostasis in Zebrafish Cone Photoreceptors", "Zebrafish untuk mempelajari kalsium di fotoreseptor", (96, 105), "Mutasi pada mitokondria dan kalsium sel kerucut retina zebrafish.", [], ["biologi-kedokteran", "fisiologi"]),
   ("CRISPR: From Prokaryotic Immune Systems to Plant Genome Editing", "CRISPR: dari imun bakteri ke tanaman", (106, 126), "Asal-usul CRISPR sebagai sistem imun bakteri dan penerapannya pada padi dan tanaman lain.", [], ["biologi-kedokteran"]),
   ("Target Discovery for Precision Medicine Using High-Throughput Genome Engineering", "Skrining CRISPR untuk target obat", (127, 149), "Skrining pustaka sgRNA menemukan gen resistansi obat kanker dan target terapi baru; analisis data skala besar.", [], ["big-data", "ilmu-data", "biologi-kedokteran"]),
   ("CRISPR in the Retina", "CRISPR di retina", (150, 158), "Retinitis pigmentosa, model sel punca pasien, dan peluang terapi gen mata.", [], ["biologi-kedokteran"]),
   ("The Future of CRISPR Applications", "Masa depan CRISPR dan etikanya", (159, 181), "Penyuntingan germline, regulasi, persepsi publik, dan pertimbangan etika.", [], ["biologi-kedokteran", "metopen"])],
  181)

# ================================================================ 11
K("robot-bedah", "Robotic Surgery", "Robotic Surgery: Smart Materials, Robotic Structures, and Artificial Muscles",
  "Mohsen Shahinpoor, Soheil Gheshmi", 2015, "Pan Stanford / CRC Press", "11_Robotic surgery.pdf",
  "Robot bedah dari sisi rekayasa: sejarah dan konfigurasi (termasuk da Vinci), kinematika dan ruang kerja dengan transformasi homogen, robot bedah mata, "
  "robot laparoskopi yang bisa dilipat, serta material pintar IPMC untuk umpan balik gaya. Pegangan untuk mata kuliah Robotika.",
  [("Introduction to Surgical Robots", "Pengantar robot bedah", (17, 48), "Sejarah robot bedah dari PUMA, ROBODOC, sampai da Vinci; konfigurasi master-slave dan manfaat bedah minimal invasif.", ["robot-bedah"], ["robotika", "tek-bedah"]),
   ("Surgical Robots' Kinematics and Workspace", "Kinematika dan ruang kerja robot bedah", (49, 88), "Sistem koordinat, matriks rotasi, transformasi homogen, kinematika maju dan balik, serta ruang kerja manipulator.", ["robot-bedah"], ["robotika", "kendali", "matek"]),
   ("Intraocular Robotic Surgical System", "Robot bedah intraokular", (89, 126), "Rancangan robot untuk operasi katarak (fakoemulsifikasi) dengan ketelitian di bawah milimeter.", ["robot-bedah", "fakoemulsifikasi"], ["robotika", "tek-bedah", "cad-medis"]),
   ("Deployable Laparoscopic Robotic Surgical System", "Robot laparoskopi yang bisa dilipat", (127, 166), "Struktur lengan yang dilipat saat masuk dan dibuka di dalam perut, dikendalikan dari konsol.", ["robot-bedah", "endoskop"], ["robotika", "cad-medis", "purwarupa"]),
   ("Applications of Smart Materials in Robotic Surgery", "Material pintar dan otot buatan (IPMC)", (167, 182), "Ionic polymer-metal composite melengkung bila diberi tegangan dan menghasilkan tegangan bila dibengkokkan; dipakai untuk sensor dan umpan balik gaya.", ["robot-bedah", "prostesis-tangan"], ["biomaterial", "sensor", "robotika"]),
   ("Summary and Conclusions", "Ringkasan dan lampiran perhitungan", (183, 206), "Rangkuman, arah riset, dan lampiran turunan kinematika.", ["robot-bedah"], ["robotika"])],
  206)

# ================================================================ 12
K("cta", "MDCT Angiography", "Multidetector-Row CT Angiography (Medical Radiology)",
  "Carlo Catalano, Roberto Passariello (ed.)", 2005, "Springer", "12_Row CT Angiography Medical Radiology Diagnostic Imaging.pdf",
  "CT angiografi multidetektor dari prinsip teknis sampai penerapan per pembuluh darah: pitch, dosis, ECG gating, rekonstruksi (MPR, MIP, volume rendering), "
  "pemberian kontras, dan CTA otak, karotis, aorta, paru, koroner, hati, ginjal, perifer, dan vena.",
  [("MDCT Angiography: Evolution", "Evolusi CT angiografi", (5, 12), "Dari CT spiral satu baris ke multidetektor dan bagaimana CTA menggantikan angiografi kateter diagnostik.", ["ct"], ["pencitraan"]),
   ("MDCT: Technical Principles", "Prinsip teknis MDCT", (13, 25), "Lebar detektor, pitch, waktu rotasi, rekonstruksi, ECG gating, dan dosis radiasi.", ["ct"], ["pencitraan", "radiasi"]),
   ("MDCT: Image Processing", "Pengolahan citra MDCT", (26, 41), "Multiplanar reformatting, MIP, surface dan volume rendering, serta endoskopi virtual.", ["ct"], ["citra", "visualisasi", "cad-medis"]),
   ("Contrast Medium Administration", "Pemberian media kontras", (42, 55), "Kecepatan injeksi, dosis iodin, waktu tunda, bolus tracking, dan puncak penyangatan arteri.", ["ct", "infus"], ["pencitraan", "fisiologi"]),
   ("CTA of Intracranial Circulation", "CTA pembuluh intrakranial", (56, 60), "Teknik pemeriksaan aneurisma dan pembuluh otak.", ["ct"], ["pencitraan", "anatomi"]),
   ("Carotid Arteries", "Arteri karotis", (61, 86), "Stenosis, plak, risiko stroke, dan perbandingan dengan USG Doppler dan MRA.", ["ct", "usg"], ["pencitraan", "anatomi"]),
   ("Thoracic Aorta", "Aorta torakalis", (87, 101), "Diseksi, aneurisma, cangkok aorta, dan gating jantung.", ["ct"], ["pencitraan"]),
   ("Pulmonary Circulation", "Sirkulasi paru dan emboli paru", (102, 123), "CTA sebagai pemeriksaan utama emboli paru.", ["ct"], ["pencitraan", "tek-medik"]),
   ("Coronary Arteries", "Arteri koroner", (124, 135), "Stenosis koroner, sinkronisasi EKG, dan resolusi waktu.", ["ct", "ekg"], ["pencitraan", "fisiologi"]),
   ("Abdominal Aorta", "Aorta abdominalis", (136, 153), "Aneurisma aorta perut dan evaluasi sebelum dan sesudah stent graft.", ["ct", "kateter-stent"], ["pencitraan", "tek-bedah"]),
   ("Hepatic Vessels", "Pembuluh hati", (154, 165), "Fase arteri dan portal untuk perencanaan bedah dan transplantasi hati.", ["ct"], ["pencitraan", "anatomi"]),
   ("Splanchnic Vessels", "Pembuluh splanknik", (166, 174), "Arteri dan vena mesenterika pada iskemia usus.", ["ct"], ["pencitraan"]),
   ("Renal Arteries", "Arteri renalis", (175, 184), "Stenosis arteri ginjal dan hipertensi renovaskular.", ["ct"], ["pencitraan"]),
   ("Peripheral Arteries", "Arteri perifer", (185, 196), "Penyakit arteri tungkai dan teknik pemindaian panjang.", ["ct"], ["pencitraan"]),
   ("Three-Dimensional Evaluation of the Venous System", "Evaluasi vena 3D", (197, 213), "CT venografi untuk trombosis dan varises.", ["ct"], ["pencitraan", "visualisasi"])],
  213)


# ---------------------------------------------------------------- soal dari buku
SOAL = []


def Q(pid, materi, alat, tipe, tanya, bahas, **kw):
    q = {"id": "p-%s-%02d" % (pid, sum(1 for s in SOAL if s["pustaka"] == "pustaka-" + pid) + 1), "tipe": tipe, "tanya": tanya, "bahas": bahas,
         "materi": materi, "pustaka": "pustaka-" + pid}
    if alat:
        q["alat"] = alat
    q.update(kw)
    SOAL.append(q)


# 1 AI in Health
Q("ai-health", "ml-medis", "", "pg", "Mengapa query-by-committee (active learning) berguna untuk data percakapan terapi?",
  "Melabeli data mahal; active learning memilih sampel yang paling diperdebatkan model agar label manusia dipakai seefisien mungkin.",
  opsi=["Memilih sampel paling diperdebatkan untuk dilabeli, sehingga label sedikit tetapi efektif", "Menghapus semua data tak berlabel", "Membuat model tanpa data", "Mempercepat GPU"], jawab=0)
Q("ai-health", "ml-medis", "oralytic", "bs", "Menurut bab 'Dr. AI', AI yang terus belajar setelah dipasarkan lebih sulit diatur dengan regulasi alat medis konvensional.",
  "Benar. Regulasi lama mengasumsikan alat tidak berubah setelah disetujui; AI adaptif perlu kerangka validasi berbasis hasil.", jawab=True)
Q("ai-health", "ml-medis", "", "cocok", "Cocokkan makalah AIH 2018 dengan metodenya.",
  "Setiap makalah memakai metode AI yang berbeda untuk masalah kesehatan berbeda.",
  pasangan=[["Pengawasan pasien demensia", "LSTM + contextual integrity"], ["Skrining kanker", "Inverse reinforcement learning (POMDP)"],
            ["Pengodean registri kanker", "Case-based reasoning"], ["Readmisi 30 hari", "Representasi vektor pasien CNN/RNN"]])
Q("ai-health", "interaksi-pasien", "glukometer", "pg", "Apa fokus bab PEPPER tentang diabetes tipe 1?",
  "Bab ini menunjukkan rekayasa usability: tugas pengguna, kuesioner, dan perbaikan antarmuka sistem rekomendasi bolus insulin.",
  opsi=["Rekayasa usability sistem rekomendasi dosis insulin", "Desain sensor glukosa baru", "Algoritma CT scan", "Robot bedah"], jawab=0)
# 2 Biosinyal
Q("biosinyal", "sinyal", "ekg", "hitung", "Setiap tambahan 1 bit ADC menaikkan SNR kuantisasi sekitar 6 dB. Berapa dB kira-kira SNR kuantisasi ADC 12 bit (pakai 6,02·N)?",
  "SNR ≈ 6,02 × 12 + 1,76 ≈ 74 dB; dengan pendekatan 6,02·N saja = 72,24 dB.", angka=72.24, tol=1, satuan="dB")
Q("biosinyal", "sinyal", "eeg", "pg", "Mengapa spektrogram atau wavelet dipakai untuk sinyal biomedis, bukan hanya transformasi Fourier biasa?",
  "Sinyal biomedis tidak stasioner; representasi waktu-frekuensi menunjukkan frekuensi yang berubah terhadap waktu.",
  opsi=["Karena frekuensi sinyal berubah terhadap waktu (tidak stasioner)", "Karena Fourier tidak bisa dihitung komputer", "Karena sinyal biomedis selalu sinus murni", "Karena wavelet tidak butuh sampling"], jawab=0)
Q("biosinyal", "sinyal", "eeg", "cocok", "Cocokkan metode dengan kegunaannya di buku Biosignal Processing.",
  "Masing-masing bab memperkenalkan alat analisis untuk pertanyaan berbeda.",
  pasangan=[["Koherensi", "Keterkaitan dua kanal EEG per frekuensi"], ["Granger causality", "Area otak mana memengaruhi area lain"],
            ["GLM + permutasi", "Peta statistik MEG dengan koreksi perbandingan berganda"], ["Registrasi groupwise", "Menyelaraskan banyak MRI otak ke pusat populasi"]])
Q("biosinyal", "fismed", "oksimeter", "bs", "fNIR mengukur perubahan oksihemoglobin dan deoksihemoglobin di korteks memakai cahaya inframerah dekat.",
  "Benar. Prinsipnya mirip oksimeter: absorbansi cahaya pada dua panjang gelombang berbeda untuk dua jenis hemoglobin.", jawab=True)
# 3 VR/AR
Q("vr-ar", "citra", "mammografi", "urut", "Urutkan alur diagnosis kanker payudara pintar pada bab AI for Smart Cancer Diagnosis.",
  "Mamogram dipra-proses, disegmentasi, lalu dikompresi dan dikirim lewat telemedisin.",
  item=["Akuisisi mamogram", "Filter median (hapus derau)", "Segmentasi fuzzy C-means", "Kompresi citra", "Kirim lewat telemedisin"])
Q("vr-ar", "iot", "", "pg", "Komponen utama tongkat pintar untuk tunanetra pada bab 18 adalah…",
  "Sensor ultrasonik mengukur jarak rintangan, NodeMCU memproses, buzzer memberi peringatan.",
  opsi=["Sensor ultrasonik, NodeMCU, dan buzzer", "Kamera termal dan GPU", "Elektroda EEG", "Tabung sinar-X"], jawab=0)
Q("vr-ar", "robotika", "emg", "kategori", "Kelompokkan bab buku Emerging Technologies menurut teknologinya.",
  "Buku ini memuat VR/AR, AI, dan robotika untuk kesehatan.",
  kelompok=["VR/AR", "AI", "Robotika"],
  item=[["Simulasi 3D anatomi", 0], ["AR kedokteran gigi", 0], ["Mobile Doctor Brain AI", 1], ["Teleradiologi cloud CBR", 1], ["Robot rehabilitasi tungkai", 2], ["Keseimbangan robot NAO", 2]])
Q("vr-ar", "difabel", "eeg", "bs", "Brain-computer interface pada bab 17 memungkinkan peralatan rumah dinyalakan memakai sinyal EEG.",
  "Benar. Pola gelombang otak dikenali lalu diterjemahkan menjadi perintah perangkat.", jawab=True)
# 4 Wearable
Q("wearable", "sistem-tertanam", "smartwatch", "pg", "Mengapa WaRP memakai desain hibrida prosesor aplikasi (i.MX 6SoloLite) dan MCU (Kinetis KL16)?",
  "MCU hemat daya menangani sensor terus-menerus, prosesor besar hanya bangun saat butuh tampilan atau aplikasi, sehingga baterai awet.",
  opsi=["Agar sensor bisa dibaca terus oleh MCU hemat daya sementara prosesor besar tidur", "Agar harga lebih mahal", "Karena Android tidak bisa membaca sensor", "Agar tidak perlu baterai"], jawab=0)
Q("wearable", "mikro", "smartwatch", "multi", "Pilih teknik hemat daya mikrokontroler Kinetis L yang dibahas di slide.",
  "Mode tidur bertingkat, clock gating, dan periferal yang tetap bekerja saat inti tidur adalah kunci umur baterai wearable.",
  opsi=["Mode Stop dan VLPS", "Clock gating periferal", "UART/SPI tetap bekerja saat inti tidur", "DMA asinkron", "Menaikkan tegangan inti", "Mematikan semua interupsi selamanya"], benar=[0, 1, 2, 3])
Q("wearable", "sensor", "smartwatch", "isian", "Sensor pedometer pada papan WaRP bernomor seri MMA…",
  "MMA9553L adalah akselerometer dengan fungsi pedometer bawaan.", jawab=["9553", "9553l", "mma9553", "mma9553l"])
# 5 EHR
Q("ehr", "simrs", "rme", "urut", "Urutkan langkah implementasi RME menurut buku Geisinger.",
  "Mulai dari kesiapan organisasi, kebutuhan, vendor, infrastruktur, alur kerja, lalu pelatihan dan go-live bertahap.",
  item=["Menilai iklim organisasi", "Analisis kebutuhan", "Memilih vendor", "Menyiapkan infrastruktur", "Desain ulang alur kerja", "Pelatihan dan go-live bertahap"])
Q("ehr", "simrs", "rme", "pg", "Apa peran physician champion dalam implementasi RME?",
  "Dokter yang dipercaya rekan sejawat memimpin perubahan, menjembatani tim TI dan klinis.",
  opsi=["Dokter yang memimpin perubahan dan menjembatani tim klinis dengan tim TI", "Teknisi server", "Perwakilan vendor", "Petugas billing"], jawab=0)
Q("ehr", "simrs", "rme", "bs", "Clinical decision support yang terlalu banyak peringatan bisa menyebabkan kelelahan alarm sehingga peringatan penting diabaikan.",
  "Benar. Buku menekankan CDS harus tepat sasaran agar tetap diperhatikan.", jawab=True)
Q("ehr", "kdm", "rme", "cocok", "Cocokkan istilah RME dengan artinya.",
  "Istilah-istilah ini sering muncul di bab rawat inap, integrasi, dan portal pasien.",
  pasangan=[["CPOE", "Dokter memesan obat/tes langsung di komputer"], ["Order set", "Paket order standar untuk kondisi tertentu"],
            ["Portal pasien", "Akses pasien ke rekam medis dan pesan aman"], ["Integrasi sistem", "RME terhubung dengan lab, radiologi, billing"]])
# 6 Lab
Q("lab", "instrumen", "kimia-klinik", "hitung", "Larutan standar 100 mg/dL memberi absorbansi 0,40. Sampel memberi absorbansi 0,30. Berapa kadar sampel (Beer-Lambert)?",
  "Absorbansi sebanding konsentrasi: C = 0,30/0,40 × 100 = 75 mg/dL.", angka=75, tol=0.5, satuan="mg/dL")
Q("lab", "biologi-kedokteran", "mikroskop", "urut", "Urutkan tahap pembuatan preparat histologi.",
  "Fiksasi → (dekalsifikasi bila tulang) → dehidrasi → penanaman paraffin → pemotongan mikrotom → pewarnaan.",
  item=["Fiksasi", "Dehidrasi dengan alkohol bertingkat", "Penanaman dalam paraffin", "Pemotongan dengan mikrotom", "Pewarnaan H&E"])
Q("lab", "fisiologi", "hematologi", "hitung", "Hb 15 g/dL dan hematokrit 45%. Berapa MCHC (g/dL)?",
  "MCHC = Hb / Hct × 100 = 15 / 45 × 100 = 33,3 g/dL.", angka=33.3, tol=0.2, satuan="g/dL")
Q("lab", "fisiologi", "koagulasi", "kategori", "Kelompokkan faktor menurut jalur pembekuan.",
  "Faktor jaringan dan VII di jalur ekstrinsik; XII, XI, IX di jalur intrinsik; X, protrombin, fibrinogen di jalur bersama.",
  kelompok=["Ekstrinsik", "Intrinsik", "Bersama"],
  item=[["Faktor jaringan (tromboplastin)", 0], ["Faktor VII", 0], ["Faktor XII", 1], ["Faktor IX", 1], ["Protrombin → trombin", 2], ["Fibrinogen → fibrin", 2]])
Q("lab", "k3", "autoklaf", "pg", "Mengapa sterilisasi uap bertekanan (autoklaf) lebih efektif daripada air mendidih biasa?",
  "Tekanan menaikkan titik didih air sehingga suhu mencapai sekitar 121 °C yang mampu membunuh spora.",
  opsi=["Tekanan menaikkan suhu uap sampai sekitar 121 °C sehingga spora mati", "Karena uap mengandung alkohol", "Karena autoklaf memakai sinar UV", "Karena tekanan menghancurkan gelas"], jawab=0)
Q("lab", "biologi-kedokteran", "", "pg", "Seorang ibu Rh negatif mengandung bayi Rh positif. Risiko yang dibahas di bab sistem Rhesus adalah…",
  "Ibu bisa membentuk anti-D yang menyerang eritrosit janin pada kehamilan berikutnya (penyakit hemolitik bayi baru lahir).",
  opsi=["Pembentukan anti-D yang dapat menyerang eritrosit janin", "Bayi pasti golongan darah O", "Tidak ada risiko sama sekali", "Hemoglobin ibu naik"], jawab=0)
# 7 Medical devices
Q("alkes-bedah", "k3", "esu", "pg", "Mengapa elektroda netral (grounding pad) ESU harus menempel lebar dan rapat?",
  "Arus kembali disebar di area luas sehingga kerapatan arus rendah; bila menempel sebagian, kerapatan arus naik dan bisa membakar kulit.",
  opsi=["Agar kerapatan arus rendah dan tidak terjadi luka bakar", "Agar arus lebih besar di elektroda aktif", "Agar ESU lebih hemat listrik", "Agar pasien tidak bergerak"], jawab=0)
Q("alkes-bedah", "dtk", "", "urut", "Urutkan proses pengembangan alat medis menurut bab Design of Medical Devices.",
  "Konsep → kebutuhan dan risiko → prototipe → verifikasi dan validasi → persetujuan regulasi → produksi.",
  item=["Konsep dan kebutuhan pengguna", "Analisis risiko", "Prototipe", "Verifikasi dan validasi", "Pengajuan regulasi", "Produksi dan pasca-pasar"])
Q("alkes-bedah", "biomaterial", "kateter-stent", "pg", "Sifat nitinol yang membuatnya cocok untuk stent adalah…",
  "Nitinol punya superelastisitas dan memori bentuk: bisa dilipat di kateter lalu kembali ke bentuk semula di pembuluh.",
  opsi=["Memori bentuk dan superelastisitas", "Sangat rapuh", "Menghantarkan sinar-X", "Larut dalam darah"], jawab=0)
Q("alkes-bedah", "pencitraan", "usg", "pg", "Bahan aktif transduser USG yang mengubah tegangan menjadi getaran dan sebaliknya adalah…",
  "Efek piezoelektrik (misal PZT) bekerja dua arah: memancarkan dan menerima gelombang ultrasonik.",
  opsi=["Material piezoelektrik", "Kawat superkonduktor", "Fosfor sintilator", "Tabung vakum"], jawab=0)
Q("alkes-bedah", "fluida", "lvad", "bs", "LVAD generasi baru umumnya memakai pompa aliran kontinu (rotari) yang lebih kecil daripada pompa pulsatil generasi awal.",
  "Benar. Pompa rotari kontinu lebih kecil dan awet, meski pasien bisa tidak punya denyut nadi teraba.", jawab=True)
Q("alkes-bedah", "tek-bedah", "", "cocok", "Cocokkan alat dengan bab buku Medical Devices.",
  "Buku ini membahas alat bedah dan pencitraan satu per satu.",
  pasangan=[["Fakoemulsifikasi", "Bedah mata"], ["RFA", "Ablasi jaringan"], ["IABP dan LVAD", "Bantuan sirkulasi mekanis"], ["Pelacakan optik", "Navigasi bedah saraf"]])
# 8 Etika
Q("etika", "interaksi-pasien", "", "multi", "Pilih empat prinsip bioetika yang dibahas Zwitter.",
  "Empat prinsip: menghormati otonomi, berbuat baik (beneficence), tidak merugikan (non-maleficence), dan keadilan.",
  opsi=["Otonomi", "Beneficence", "Non-maleficence", "Keadilan", "Efisiensi biaya", "Popularitas"], benar=[0, 1, 2, 3])
Q("etika", "metopen", "oralytic", "pg", "Sebelum menguji aplikasi deteksi karies pada pasien sungguhan, langkah etika yang wajib adalah…",
  "Riset pada manusia butuh persetujuan komite etik dan informed consent dari peserta.",
  opsi=["Persetujuan komite etik dan informed consent", "Langsung dipasang di aplikasi", "Merahasiakan dari pasien", "Meminta izin vendor GPU"], jawab=0)
Q("etika", "interaksi-pasien", "", "bs", "Menurut Zwitter, otonomi pasien bersifat mutlak sehingga tidak pernah boleh dibatasi.",
  "Salah. Otonomi bisa dibatasi, misalnya bila pasien tidak kompeten atau keputusannya membahayakan orang lain.", jawab=False)
# 9 Telemedisin
Q("telemedisin", "kdm", "telemedisin", "pg", "Body area network (BAN) pada pemantauan pasien nirkabel adalah…",
  "BAN menghubungkan sensor yang dikenakan pasien ke gateway untuk dikirim ke sistem pemantauan.",
  opsi=["Jaringan sensor di sekitar tubuh pasien yang terhubung ke gateway", "Jaringan antar-rumah sakit", "Kabel EKG 12 sadapan", "Server pusat data"], jawab=0)
Q("telemedisin", "kdm", "rme", "multi", "Pilih teknik pengamanan data medis yang dibahas di bab Safeguarding Medical Data.",
  "Enkripsi, autentikasi, kontrol akses, dan watermark citra melindungi kerahasiaan dan keaslian data.",
  opsi=["Enkripsi", "Autentikasi pengguna", "Watermark citra medis", "Kontrol akses berbasis peran", "Mengirim data tanpa kata sandi", "Membagikan data di media sosial"], benar=[0, 1, 2, 3])
Q("telemedisin", "monitoring", "patient-monitor", "bs", "Pemantauan pasien nirkabel harus mempertimbangkan keandalan tautan karena data yang hilang bisa berarti alarm yang terlewat.",
  "Benar. Buku menekankan kualitas layanan dan keandalan jaringan untuk data vital.", jawab=True)
# 10 CRISPR
Q("crispr", "biologi-kedokteran", "", "pg", "Mengapa AAV sering dipakai untuk mengantar perangkat penyunting gen in vivo?",
  "AAV relatif aman, imunogenisitas rendah, dan bisa menargetkan jaringan tertentu, meski kapasitas muatannya kecil (~4,7 kb).",
  opsi=["Aman dan bisa menargetkan jaringan, meski muatannya terbatas", "Muatannya tidak terbatas", "Menyebabkan infeksi berat", "Hanya bekerja pada bakteri"], jawab=0)
Q("crispr", "big-data", "", "pg", "Skrining CRISPR genom luas untuk menemukan target obat menghasilkan data yang dianalisis dengan…",
  "Ribuan sgRNA dihitung frekuensinya sebelum dan sesudah perlakuan; analisis data skala besar menemukan gen yang berpengaruh.",
  opsi=["Analisis data skala besar dari frekuensi ribuan sgRNA", "Mikroskop cahaya biasa saja", "Satu kali uji titrasi", "Kuesioner pasien"], jawab=0)
Q("crispr", "biologi-kedokteran", "", "bs", "Penyuntingan germline berbeda dari terapi gen somatik karena perubahannya diturunkan ke generasi berikutnya.",
  "Benar. Itulah sebabnya bab terakhir menekankan regulasi dan etika penyuntingan germline.", jawab=True)
# 11 Robotic surgery
Q("robot-bedah", "robotika", "robot-bedah", "pg", "Matriks transformasi homogen 4×4 pada kinematika robot bedah menggabungkan…",
  "Rotasi 3×3 dan translasi 3×1 dalam satu matriks sehingga posisi ujung alat bisa dihitung dengan perkalian matriks berantai.",
  opsi=["Rotasi dan translasi dalam satu matriks", "Gaya dan torsi", "Tegangan dan arus", "Massa dan percepatan"], jawab=0)
Q("robot-bedah", "biomaterial", "robot-bedah", "pg", "IPMC dalam bab material pintar dimanfaatkan karena…",
  "IPMC melengkung bila diberi tegangan dan menghasilkan tegangan bila dibengkokkan, sehingga bisa menjadi aktuator sekaligus sensor gaya.",
  opsi=["Bisa menjadi aktuator dan sensor gaya sekaligus", "Sangat berat dan kaku", "Hanya menghantarkan panas", "Tidak bereaksi pada listrik"], jawab=0)
Q("robot-bedah", "robotika", "robot-bedah", "bs", "Pada konfigurasi master-slave seperti da Vinci, gerakan tangan dokter di konsol diterjemahkan menjadi gerakan alat di tubuh pasien.",
  "Benar. Sistem juga bisa menskalakan gerakan dan meredam tremor.", jawab=True)
# 12 CTA
Q("cta", "pencitraan", "ct", "hitung", "Kolimasi 16 × 1,25 mm (20 mm) dan meja bergerak 30 mm per rotasi. Berapa pitch-nya?",
  "Pitch = gerak meja per rotasi / lebar kolimasi total = 30 / 20 = 1,5.", angka=1.5, tol=0.01, satuan="")
Q("cta", "visualisasi", "ct", "cocok", "Cocokkan teknik rekonstruksi CTA dengan hasilnya.",
  "Bab pengolahan citra MDCT membandingkan tampilan 2D dan 3D.",
  pasangan=[["MPR", "Irisan di bidang mana pun"], ["MIP", "Piksel paling terang sepanjang sinar, pembuluh berkontras menonjol"],
            ["Volume rendering", "Tampilan 3D dengan transparansi"], ["Endoskopi virtual", "Melihat lumen dari dalam"]])
Q("cta", "pencitraan", "ct", "pg", "Mengapa CTA koroner memerlukan ECG gating?",
  "Jantung bergerak; gating memilih data pada fase diastolik yang tenang agar arteri koroner tidak kabur.",
  opsi=["Agar citra diambil pada fase jantung yang tenang sehingga tidak kabur", "Agar dosis kontras nol", "Agar pasien tidak perlu bernapas", "Agar CT tidak memakai sinar-X"], jawab=0)
Q("cta", "fisiologi", "ct", "bs", "Pada CTA, waktu tunda dan kecepatan injeksi kontras diatur agar pemindaian bertepatan dengan puncak penyangatan arteri.",
  "Benar. Bolus tracking atau test bolus dipakai untuk menentukan waktu mulai pemindaian.", jawab=True)


# ---------------------------------------------------------------- alat baru dari buku
ALAT_BUKU = []


def A(aid, nama, singkatan, kategori, ikon, ilustrasi, ringkasan, prinsip, keselamatan, blok, kontribusi, sumber):
    ALAT_BUKU.append({
        "id": aid, "nama": nama, "singkatan": singkatan, "kategori": kategori, "ikon": ikon,
        "ringkasan": ringkasan, "prinsipKerja": prinsip, "keselamatan": keselamatan,
        "blok": [{"id": b, "nama": n, "fungsi": f} for b, n, f in blok],
        "kontribusi": [{"materi": k[0], "tingkat": k[1], "blok": list(k[2]), "peran": k[3], "sub": []} for k in kontribusi],
        "catatan": "", "umpanBalik": False, "referensi": [], "model": "", "ilustrasi": ilustrasi, "sumber": sumber,
    })


A("lvad", "Left Ventricular Assist Device", "LVAD", "Life Support", "🫀", "pompa",
  "Pompa darah yang ditanam untuk membantu ventrikel kiri yang gagal, sebagai jembatan menuju transplantasi atau terapi jangka panjang.",
  "Kanula masuk di apeks ventrikel kiri menyedot darah ke pompa rotari (aksial atau sentrifugal, rotor dilevitasi magnet) lalu mengalirkannya ke aorta. "
  "Kabel driveline keluar dari kulit menuju pengendali dan baterai yang dibawa pasien. Pengendali mengatur kecepatan rotor dan memantau daya, aliran perkiraan, serta indeks pulsatilitas.",
  "Risiko trombosis pompa, perdarahan (pasien memakai antikoagulan), infeksi driveline, dan gagal daya. Baterai cadangan wajib dibawa; alarm daya dan aliran rendah harus ditanggapi segera.",
  [("kanula", "Kanula inflow", "Menyedot darah dari ventrikel kiri"), ("pompa", "Pompa rotari", "Rotor dilevitasi magnet mendorong aliran kontinu"),
   ("graft", "Graft outflow", "Mengalirkan darah ke aorta"), ("driveline", "Driveline", "Kabel daya dan data menembus kulit"),
   ("kontroler", "Kontroler", "Mengatur kecepatan, menghitung aliran, alarm"), ("baterai", "Baterai", "Sumber daya portabel dan cadangan")],
  [("fluida", 3, ["pompa", "kanula", "graft"], "Aliran darah, tekanan, dan kurva H-Q pompa rotari."),
   ("fisiologi", 3, ["kanula"], "Gagal jantung, curah jantung, dan interaksi pompa dengan ventrikel."),
   ("biomaterial", 3, ["pompa", "graft", "driveline"], "Hemokompatibilitas permukaan pompa dan graft."),
   ("kendali", 2, ["kontroler"], "Kendali kecepatan rotor dan deteksi suction."),
   ("elektronika-medis", 2, ["kontroler", "baterai"], "Motor driver dan manajemen baterai."),
   ("k3", 2, ["baterai", "driveline"], "Alarm daya, cadangan baterai, dan pencegahan infeksi."),
   ("tek-bedah", 2, ["kanula"], "Prosedur implantasi di bedah jantung.")],
  "Medical Devices: Surgical and Image-Guided Technologies, bab 11")

A("fakoemulsifikasi", "Mesin Fakoemulsifikasi", "Fako", "Bedah", "👁️", "konsol",
  "Mesin bedah katarak yang memecah lensa keruh dengan getaran ultrasonik lalu menyedotnya lewat sayatan kecil.",
  "Handpiece berisi kristal piezoelektrik yang menggetarkan jarum titanium pada sekitar 28–45 kHz untuk mengemulsikan lensa. "
  "Sistem fluidik mengalirkan cairan irigasi ke bilik mata dan menyedot pecahan lensa dengan pompa peristaltik atau venturi, sambil menjaga tekanan intraokular stabil. "
  "Pedal kaki mengatur tahapan irigasi, aspirasi, dan daya ultrasonik.",
  "Lonjakan vakum (post-occlusion surge) bisa membuat bilik mata kolaps; panas jarum bisa membakar luka kornea. Kalibrasi tekanan irigasi dan uji handpiece sebelum operasi.",
  [("handpiece", "Handpiece ultrasonik", "Kristal piezoelektrik menggetarkan jarum"), ("generator", "Generator daya US", "Mengatur frekuensi dan daya getar"),
   ("irigasi", "Irigasi", "Botol cairan dan tekanan infus ke bilik mata"), ("aspirasi", "Pompa aspirasi", "Peristaltik atau venturi menyedot pecahan lensa"),
   ("pedal", "Pedal kaki", "Mengatur tahap irigasi, aspirasi, dan US"), ("konsol", "Konsol dan sensor", "Memantau vakum dan tekanan")],
  [("tek-bedah", 3, ["handpiece", "pedal"], "Teknik bedah katarak dan bedah mata."),
   ("fluida", 3, ["irigasi", "aspirasi"], "Keseimbangan aliran masuk-keluar dan tekanan intraokular."),
   ("sensor", 2, ["handpiece", "konsol"], "Transduser piezoelektrik dan sensor vakum."),
   ("elda", 2, ["generator"], "Generator ultrasonik dan penyesuaian resonansi."),
   ("anatomi", 2, ["handpiece"], "Anatomi mata: kornea, kapsul lensa, bilik depan."),
   ("kendali", 2, ["aspirasi", "konsol"], "Kendali vakum untuk mencegah lonjakan."),
   ("robotika", 1, ["handpiece"], "Robot intraokular untuk ketelitian sub-milimeter.")],
  "Medical Devices bab 4; Robotic Surgery bab 3")

A("kateter-stent", "Kateter, Balon, dan Stent", "Kateter-Stent", "Terapi", "🩸", "klip",
  "Alat intervensi lewat pembuluh darah: guidewire dan kateter menuju sumbatan, balon melebarkan, stent menahan pembuluh tetap terbuka.",
  "Lewat akses arteri femoral atau radial, guidewire dimajukan di bawah panduan fluoroskopi, disusul kateter. Balon dikembangkan dengan tekanan beberapa atmosfer untuk "
  "melebarkan stenosis, lalu stent (baja, kobalt-krom, atau nitinol; bisa melepas obat) dikembangkan dan menetap di dinding pembuluh.",
  "Risiko diseksi pembuluh, trombosis stent, restenosis, nefropati karena kontras, dan paparan radiasi fluoroskopi bagi pasien dan operator.",
  [("akses", "Sheath akses", "Pintu masuk di arteri femoral atau radial"), ("guidewire", "Guidewire", "Kawat lentur penuntun ke lokasi sumbatan"),
   ("kateter", "Kateter", "Tabung penghantar alat dan kontras"), ("balon", "Balon angioplasti", "Melebarkan stenosis dengan tekanan"),
   ("stent", "Stent", "Penyangga logam atau nitinol, bisa melepas obat"), ("citra", "Panduan fluoroskopi", "Melihat posisi alat dan aliran kontras")],
  [("biomaterial", 3, ["stent", "guidewire", "kateter"], "Nitinol, kobalt-krom, polimer pelepas obat, dan hemokompatibilitas."),
   ("fluida", 2, ["balon", "kateter"], "Tekanan balon dan aliran dalam pembuluh."),
   ("tek-bedah", 3, ["akses", "guidewire"], "Prosedur intervensi kardiovaskular."),
   ("radiasi", 2, ["citra"], "Proteksi radiasi saat fluoroskopi."),
   ("anatomi", 2, ["akses"], "Anatomi arteri koroner dan perifer."),
   ("cad-medis", 1, ["stent"], "Desain geometri strut stent.")],
  "Medical Devices bab 6 dan 10; MDCT Angiography bab 10")

A("rfa", "Ablasi Radiofrekuensi", "RFA", "Terapi", "🔥", "konsol",
  "Menghancurkan tumor atau jaringan aritmia dengan panas dari arus radiofrekuensi yang dialirkan lewat jarum atau kateter.",
  "Generator 375–500 kHz mengalirkan arus dari elektroda aktif ke pad netral. Arus menimbulkan pemanasan resistif di jaringan sekitar ujung elektroda sampai 60–100 °C sehingga "
  "terjadi nekrosis koagulasi. Termokopel di ujung elektroda dan pengukuran impedansi dipakai mengendalikan daya agar zona ablasi cukup tanpa mengarangkan jaringan.",
  "Luka bakar di pad netral, cedera organ di dekat tumor, dan efek heat-sink pembuluh besar yang membuat ablasi tidak tuntas. Pantau impedansi dan suhu.",
  [("generator", "Generator RF", "Sumber arus 375–500 kHz"), ("elektroda", "Elektroda jarum/kateter", "Menyalurkan arus ke jaringan target"),
   ("pad", "Pad netral", "Jalur kembali arus dengan kerapatan rendah"), ("sensor", "Termokopel dan impedansi", "Memantau suhu dan perubahan jaringan"),
   ("kendali", "Kendali daya", "Mengatur daya agar suhu target tercapai"), ("citra", "Panduan citra", "USG atau CT untuk menempatkan jarum")],
  [("fismed", 3, ["elektroda"], "Pemanasan resistif dan distribusi suhu jaringan."),
   ("fisika-listrik-magnet", 2, ["generator", "pad"], "Arus bolak-balik dan kerapatan arus."),
   ("kendali", 3, ["kendali", "sensor"], "Kendali suhu tertutup berbasis termokopel."),
   ("sensor", 2, ["sensor"], "Termokopel dan pengukuran impedansi."),
   ("k3", 2, ["pad"], "Pencegahan luka bakar di pad netral."),
   ("pencitraan", 2, ["citra"], "Panduan USG atau CT."),
   ("tek-bedah", 2, ["elektroda"], "Onkologi intervensi dan elektrofisiologi jantung.")],
  "Medical Devices bab 8")

A("laser-medis", "Laser Medis dan OCT", "Laser", "Terapi", "🔆", "konsol",
  "Laser untuk memotong, mengoagulasi, atau menguapkan jaringan (mata, kulit, bedah), dan OCT untuk mencitrakan lapisan retina dengan cahaya.",
  "Medium laser dipompa sehingga terjadi emisi terstimulasi; cahaya koheren satu panjang gelombang keluar lewat serat optik atau lengan. Efek pada jaringan tergantung panjang gelombang "
  "(diserap air, hemoglobin, atau melanin), daya, dan lama pulsa: fototermal, fotoablasi, atau fotomekanik. OCT memakai interferometri cahaya inframerah dekat koherensi rendah "
  "untuk membuat penampang retina beresolusi mikrometer.",
  "Bahaya mata (kelas 3B dan 4): kacamata pelindung sesuai panjang gelombang, tanda area laser, kunci interlock. Risiko kebakaran di dekat oksigen dan asap bedah.",
  [("medium", "Medium dan pompa laser", "Menghasilkan emisi terstimulasi"), ("resonator", "Resonator optik", "Cermin yang memperkuat cahaya koheren"),
   ("penghantar", "Serat atau lengan optik", "Mengantar berkas ke jaringan"), ("kendali", "Kendali pulsa", "Mengatur daya, durasi, dan frekuensi pulsa"),
   ("pengaman", "Interlock dan pembidik", "Berkas pembidik dan pengaman area"), ("oct", "Modul OCT", "Interferometer untuk citra penampang retina")],
  [("fismed", 3, ["medium", "penghantar"], "Interaksi laser-jaringan dan koefisien absorpsi."),
   ("radiasi", 2, ["pengaman"], "Klasifikasi laser dan proteksi radiasi optik."),
   ("fisika-listrik-magnet", 2, ["resonator"], "Gelombang elektromagnetik dan koherensi."),
   ("pencitraan", 2, ["oct"], "Prinsip interferometri OCT."),
   ("k3", 2, ["pengaman"], "Kacamata, interlock, dan pencegahan kebakaran."),
   ("tek-bedah", 2, ["penghantar"], "Bedah mata, dermatologi, dan bedah umum.")],
  "Medical Devices bab 9")

A("neuronavigasi", "Sistem Neuronavigasi", "Neuronavigasi", "Bedah", "🧭", "konsol",
  "GPS bedah saraf: menampilkan posisi ujung alat bedah secara langsung di atas citra MRI atau CT pasien.",
  "Citra MRI/CT praoperasi dimuat lalu diregistrasikan ke kepala pasien memakai fiducial atau pemindaian permukaan. Kamera inframerah melacak penanda reflektif pada alat "
  "(atau medan elektromagnetik melacak koil kecil), sehingga posisi ujung alat dihitung dengan transformasi koordinat dan ditampilkan di tiga bidang serta 3D. "
  "USG intraoperatif bisa dipakai mengoreksi pergeseran otak (brain shift).",
  "Kesalahan registrasi dan brain shift membuat posisi tampilan berbeda dari kenyataan; verifikasi landmark selama operasi. Jangan menghalangi pandangan kamera ke penanda.",
  [("citra", "Citra praoperasi", "MRI atau CT kepala pasien"), ("registrasi", "Registrasi", "Menyelaraskan citra dengan kepala pasien"),
   ("pelacak", "Pelacak optik/EM", "Kamera IR atau medan magnet melacak alat"), ("alat", "Alat bertanda", "Pointer dan instrumen dengan penanda"),
   ("komputasi", "Komputasi transformasi", "Menghitung posisi ujung alat di ruang citra"), ("tampilan", "Tampilan navigasi", "Tiga bidang dan 3D di layar")],
  [("citra", 3, ["citra", "registrasi"], "Registrasi citra dan transformasi koordinat."),
   ("robotika", 2, ["komputasi"], "Transformasi homogen dan kinematika."),
   ("pencitraan", 2, ["citra"], "MRI dan CT sebagai peta bedah."),
   ("sensor", 2, ["pelacak"], "Kamera inframerah dan sensor elektromagnetik."),
   ("tek-bedah", 3, ["alat", "tampilan"], "Alur kerja bedah saraf."),
   ("anatomi", 2, ["tampilan"], "Neuroanatomi untuk verifikasi landmark."),
   ("visualisasi", 1, ["tampilan"], "Tampilan 3D yang mudah dibaca dokter bedah.")],
  "Medical Devices bab 16")
