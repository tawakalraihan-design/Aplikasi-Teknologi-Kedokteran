# Referensi Teknologi Kedokteran v1.4: 12 buku di folder Referensi

Buku-buku di folder `Referensi` (di samping `TeknologiKedokteran.exe`) sudah diolah ke aplikasi. Di aplikasi: menu **Referensi → Buku di folder Referensi**, lalu klik **N bab dengan ringkasan**. Tiap bab punya ringkasan berbahasa Indonesia, halaman PDF, alat, dan mata kuliah terkait; bab yang membahas sebuah alat juga muncul di halaman alat itu (panel *Bacaan dari buku Referensi*). Nomor halaman = nomor halaman file PDF.

Total 12 buku, 187 bab, 47 soal latihan. Daftar referensi lain (buku teks, standar, jurnal, dataset) tetap di `Referensi-v1.3.md`.

## Artificial Intelligence in Health (AIH 2018, LNAI 11326)

Fernando Koch, Isabelle Bichindaritz dkk. (ed.) · Springer · 2019 · 261 halaman · `Referensi\1_Artificial Intelligence in Health.pdf`

Kumpulan 17 makalah riset AI kesehatan: NLP catatan klinis, penjadwalan perawatan rumah, deteksi nyeri dari wajah, regulasi AI sebagai alat medis, sampai deep learning untuk memprediksi readmisi. Bagus untuk melihat cara peneliti menulis masalah, metode, dan evaluasi AI medis.

Alat: RME, Telemedisin, Smartwatch, Oralytic, BrainWave, Dispenser Obat, Glukometer, Infusion Pump, Mammografi, CT Scan

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | MeSHx-Notes: kamus istilah MeSH untuk catatan klinis<br>*MeSHx-Notes* | 18–27 | Membangun kamus istilah medis dari MeSH yang diperluas dengan kata-kata mirip (word embedding) agar sistem bisa mengenali istilah di catatan dokter yang ditulis bebas. | RME | Ilmu Data Medis, Penggalian Data Medis, Sistem Informasi Manajemen Rumah Sakit |
| 2 | Sistem multiagen untuk penjadwalan perawatan rumah<br>*Multiagent Systems to Support Planning and Scheduling in Home Health Care* | 28–43 | Tinjauan literatur penjadwalan perawat home care: model optimasi, agen yang bernegosiasi jadwal, dan tantangan data nyata seperti jarak tempuh dan preferensi pasien. | Telemedisin | Sistem Informasi Manajemen Rumah Sakit, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 3 | Pengawasan etis pasien demensia dengan LSTM<br>*Ethical Surveillance: Applying Deep Learning and Contextual Integrity* | 44–62 | Memantau pola tidur dan gerak pasien demensia dengan LSTM sambil membatasi data yang dibagikan menurut teori contextual integrity, supaya privasi tetap terjaga. | Smartwatch | Pembelajaran Mesin Untuk Data Medis, Big Data dalam Kesehatan, Sistem Monitoring Elektronik Kesehatan |
| 4 | Active learning (QBEC) untuk klasifikasi percakapan terapi<br>*Active Learning for Conversational Therapy Classification* | 63–73 | Melabeli ucapan sesi terapi itu mahal. Query-by-committee memilih sampel yang paling diperdebatkan model untuk dilabeli manusia, sehingga label sedikit tetapi model tetap akurat. |  | Pembelajaran Mesin Untuk Data Medis, Penggalian Data Medis |
| 5 | Penyebaran topik dalam sesi terapi (PLDA)<br>*Analysis of Topic Propagation in Therapy Sessions using PLDA* | 74–90 | Partially Labeled LDA menemukan topik dalam transkrip konselor-pasien dan melacak bagaimana topik berpindah dari satu pembicara ke yang lain. |  | Penggalian Data Medis, Ilmu Data Medis |
| 6 | Dr. AI: regulasi AI sebagai alat medis<br>*Dr. AI, Where Did You Get Your Degree?* | 91–98 | Membahas AI-as-a-Medical-Device (AIaMD): mengapa AI yang terus belajar sulit diatur dengan regulasi alat medis biasa, dan usulan kerangka validasi berbasis hasil klinis. | Oralytic, BrainWave | Pembelajaran Mesin Untuk Data Medis, Kalibrasi dan Manajemen Alat Kesehatan, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 7 | Argumentasi untuk agen asisten<br>*Design Principles and Action Reflection for Assistive Agents* | 99–113 | Agen asisten untuk lansia memakai teori aktivitas dan argumentasi formal untuk memutuskan kapan membantu dan menjelaskan alasannya kepada pengguna. |  | Interaksi Pasien Dengan Teknologi Kedokteran, Desain Teknologi Difabel dan Alat Bantu |
| 8 | HoloLens sebagai pelatih minum obat (MCIA)<br>*Microsoft HoloLens for Medication Coaching* | 114–130 | Prototipe augmented reality di HoloLens yang menampilkan rencana obat, cara minum, dan pengingat untuk meningkatkan kepatuhan pasien. | Dispenser Obat | Pemrograman Perangkat Bergerak, Interaksi Pasien Dengan Teknologi Kedokteran, Teknologi dalam Bidang Keperawatan |
| 9 | INCA: simulasi alur perawatan kanker berbasis pengetahuan<br>*A Knowledge-Based Simulation Framework (INCA)* | 131–142 | Kerangka simulasi alur pasien kanker dari data rumah sakit untuk menguji keputusan klinis dan kapasitas layanan sebelum diterapkan. | RME | Sistem Informasi Manajemen Rumah Sakit, Big Data dalam Kesehatan, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 10 | Utilitas harapan maksimum pada model relasional<br>*Lifted Maximum Expected Utility (MEU-LJT)* | 143–156 | Algoritma inferensi probabilistik 'lifted' untuk memilih tindakan terbaik bagi banyak pasien sekaligus tanpa menghitung satu per satu. |  | Pembelajaran Mesin Untuk Data Medis, Statistika |
| 11 | Rekayasa usability pada PEPPER (insulin diabetes tipe 1)<br>*The Role of Usability Engineering in PEPPER* | 157–176 | Evaluasi usability sistem rekomendasi dosis bolus insulin: tugas pengguna, skala SUS, dan perbaikan antarmuka berdasarkan temuan. | Glukometer, Infusion Pump | Interaksi Pasien Dengan Teknologi Kedokteran, Desain Teknologi Kesehatan, Critical and Design Thinking |
| 12 | Deteksi nyeri otomatis dari video wajah<br>*Automated Pain Detection in Facial Videos* | 177–195 | Fitur facial action unit dari video anak pasca operasi dipakai untuk klasifikasi nyeri; transfer learning menjembatani fitur otomatis dan fitur hasil kode manusia. |  | Pembelajaran Mesin Untuk Data Medis, Pengolahan Citra Medis, Visualisasi Data Medis |
| 13 | Fusi wajah dan EDA untuk deteksi nyeri anak<br>*Towards Automated Pain Detection in Children (face + EDA)* | 196–204 | Menggabungkan sinyal electrodermal activity dengan fitur wajah; fusi multimodal dan adaptasi domain antar-rumah sakit menaikkan akurasi. | Smartwatch | Pembelajaran Mesin Untuk Data Medis, Pengolahan Sinyal Biomedik, Sensor dan Transduser Biomedis |
| 14 | Case-based reasoning untuk pengodean kanker<br>*Interpretation of Best Medical Coding Practices by CBR* | 205–213 | Sistem penalaran berbasis kasus membantu petugas registri kanker memilih kode yang tepat dengan argumen dari kasus serupa. | RME | Sistem Informasi Manajemen Rumah Sakit, Manajemen Data |
| 15 | Deep learning menemukan percakapan penyakit serius di catatan klinis<br>*Identification of Serious Illness Conversations* | 214–227 | Jaringan saraf membaca catatan EHR untuk menemukan dokumentasi diskusi tujuan perawatan dengan F1 sekitar 0,92, jauh lebih cepat daripada tinjauan manual. | RME | Pembelajaran Mesin Untuk Data Medis, Penggalian Data Medis |
| 16 | Inverse reinforcement learning untuk skrining kanker<br>*Generating Reward Functions Using IRL for Cancer Screening* | 228–242 | Skrining kanker payudara dan paru dimodelkan sebagai POMDP; inverse RL (MaxEnt) mempelajari fungsi reward dari keputusan dokter. | Mammografi, CT Scan | Pembelajaran Mesin Untuk Data Medis, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 17 | Representasi vektor pasien (CNN/RNN) untuk readmisi 30 hari<br>*Deep Learning Architectures for Vector Representations of Patients* | 243–261 | Riwayat pasien diubah menjadi vektor oleh CNN dan RNN, lalu dipakai memprediksi risiko rawat ulang 30 hari pada pasien penyakit kronis. | RME | Pembelajaran Mesin Untuk Data Medis, Big Data dalam Kesehatan, Ilmu Data Medis |

## Biosignal Processing: Principles and Practices

Hualou Liang, Joseph D. Bronzino, Donald R. Peterson (ed.) · CRC Press · 2013 · 213 halaman · `Referensi\2_Biosignal Processing.pdf`

Dasar pengolahan sinyal biomedis dari akuisisi sampai analisis kausalitas jaringan otak: sampling, filter, representasi waktu-frekuensi, spektrum EEG, MEG, registrasi citra otak, fNIR, dan Granger causality. Pendamping kuat mata kuliah Pengolahan Sinyal Biomedik.

Alat: EKG, EEG, EMG, Holter, USG, qEEG, NFB, MRI, MoCo, SpO2

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Akuisisi dan pengolahan sinyal biomedis digital<br>*Digital Biomedical Signal Acquisition and Processing* | 18–37 | Sampling dan teorema Nyquist, kuantisasi (SNR naik sekitar 6 dB tiap tambahan 1 bit ADC), filter FIR dan IIR, respons frekuensi, contoh EKG dan filter notch 50/60 Hz. | EKG, EEG, EMG, Holter | Pengolahan Sinyal Biomedik, Instrumentasi Biomedis, Elektronika Digital |
| 2 | Representasi waktu-frekuensi<br>*Time–Frequency Signal Representations for Biomedical Signals* | 38–61 | Sinyal biomedis tidak stasioner. Bab ini membandingkan spektrogram (STFT), distribusi Wigner-Ville dan kelas Cohen, serta wavelet untuk melihat frekuensi yang berubah terhadap waktu. | EEG, EKG, USG | Pengolahan Sinyal Biomedik, Matematika Teknik |
| 3 | Analisis spektral multivariat EEG<br>*Multivariate Spectral Analysis of Electroencephalogram* | 62–85 | Spektrum daya EEG, koherensi antar-kanal, efek konduksi volume di kulit kepala, dan pemisahan sumber (SOBI) untuk melihat aktivitas otak yang sebenarnya. | EEG, qEEG, NFB | Pengolahan Sinyal Biomedik, Fisiologi Kedokteran |
| 4 | Model linear umum untuk data MEG<br>*General Linear Modeling of Magnetoencephalography Data* | 86–113 | GLM menghubungkan sinyal MEG dengan desain eksperimen, lalu peta statistik kortikal dikoreksi untuk perbandingan berganda dengan uji permutasi. | qEEG | Pengolahan Sinyal Biomedik, Statistika |
| 5 | Registrasi citra MRI otak secara berkelompok<br>*Emergence of Groupwise Registration in MR Brain Study* | 114–135 | Alih-alih menyelaraskan tiap otak ke satu templat, registrasi groupwise menyelaraskan semua subjek ke pusat populasi agar atlas tidak bias. | MRI, MoCo | Pengolahan Citra Medis, Teknologi Pencitraan Medis |
| 6 | Pencitraan otak optik fungsional (fNIR)<br>*Functional Optical Brain Imaging (fNIR)* | 136–169 | Cahaya inframerah dekat mengukur perubahan oksi- dan deoksihemoglobin di korteks saat tugas kognitif; prinsip optik, desain sensor, dan pengolahan data hemodinamik. | SpO2, qEEG | Fisika Medis, Sensor dan Transduser Biomedis, Pengolahan Sinyal Biomedik |
| 7 | Analisis kausalitas data saraf multivariat<br>*Causality Analysis of Multivariate Neural Data* | 170–213 | Granger causality dan model autoregresif multivariat di domain waktu dan frekuensi untuk mengetahui area otak mana yang memengaruhi area lain. | EEG | Pengolahan Sinyal Biomedik, Statistika, Matematika Teknik |

## Emerging Technologies for Health and Medicine: Virtual Reality, Augmented Reality, AI, IoT, Robotics, Industry 4.0

Dac-Nhuong Le, Chung Van Le, Jolanda G. Tromp, Gia Nhu Nguyen (ed.) · Wiley-Scrivener · 2018 · 298 halaman · `Referensi\3_Emerging technologies for health-VR-AR.pdf`

19 bab tentang VR/AR untuk pendidikan dan terapi, AI untuk diagnosis kanker dan stroke, telemedisin, robot rehabilitasi, brain-computer interface, dan IoT untuk tunanetra serta rumah pintar. Banyak ide proyek kecil yang bisa dicoba di mata kuliah IoT, Robotika, dan Desain.

Alat: Oralytic, Robot Bedah, EEG, EMG, Prostesis Tangan, EMS, Mammografi, Telemedisin, X-Ray, Brace, BrainWave, NFB, Inkubator, Termometer

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Tinjauan aplikasi VR/AR di layanan kesehatan<br>*Reviews of the Implications of VR/AR Health Care Applications* | 33–49 | Peta penerapan VR dan AR: pelatihan bedah, terapi fobia dan nyeri, rehabilitasi, edukasi pasien, serta tantangan biaya dan validasi klinis. |  | Desain Teknologi Berbantu Komputer untuk Medis, Visualisasi Data Medis, Teknologi dalam Ilmu Kedokteran Medik |
| 2 | Simulasi 3D untuk belajar anatomi<br>*Using 3D Simulation in Medical Education* | 50–62 | Studi kelas: mahasiswa yang belajar anatomi dengan VR dibandingkan model plastik; skor ujian dan respons belajar dianalisis. |  | Anatomi, Desain Teknologi Berbantu Komputer untuk Medis |
| 3 | AR untuk membangun empati anak<br>*Building Empathy in Young Children using Augmented Reality* | 63–69 | Aplikasi AR untuk anak prasekolah di Malaysia mengenalkan kondisi orang lain agar anak belajar empati. |  | Critical and Design Thinking, Interaksi Pasien Dengan Teknologi Kedokteran |
| 4 | Latihan wawancara kerja dengan VR<br>*Effectiveness of Virtual Reality Mock Interview Training* | 70–77 | VR mock interview untuk penganggur dengan kecemasan; pre-test dan post-test menunjukkan kecemasan menurun. |  | Desain Teknologi Difabel dan Alat Bantu, Metode Penelitian Teknologi Kedokteran |
| 5 | AR dan VR di kedokteran gigi<br>*Augmenting Dental Care: A Current Perspective* | 78–94 | AR untuk bedah implan dan ortognatik, navigasi dental, simulasi pendidikan, serta edukasi pasien gigi. Relevan dengan proyek Oralytic. | Oralytic, Robot Bedah | Desain Teknologi Berbantu Komputer untuk Medis, Teknologi dalam Ilmu Kedokteran Bedah, Pengolahan Citra Medis |
| 6 | Metode evaluasi VR dan pengukuran psikofisiologis<br>*Review of Virtual Reality Evaluation Methods and Psychophysiological Measurement Tools* | 95–115 | Cara menilai sistem VR: usability, presence, beban kerja, serta sinyal fisiologis (EEG, EDA, detak jantung) sebagai ukuran objektif. | EEG | Desain Teknologi Kesehatan, Metode Penelitian Teknologi Kedokteran, Interaksi Pasien Dengan Teknologi Kedokteran |
| 7 | AI mHealth untuk stroke dan robot rehabilitasi<br>*AI Technologies for Mobile Health of Stroke Monitoring & Rehabilitation Robotics Control* | 116–126 | Sinyal EMG nirkabel dikenali dengan klasifikasi cerdas untuk memantau pasien stroke dan mengendalikan robot rehabilitasi. | EMG, Prostesis Tangan, EMS | Robotika untuk Kedokteran, Pengolahan Sinyal Biomedik, Pengantar Sistem Internet of Things |
| 8 | AI untuk diagnosis kanker payudara dan telemedisin<br>*Artificial Intelligence for Smart Cancer Diagnosis* | 127–139 | Mamogram dipra-proses (filter median), disegmentasi dengan fuzzy C-means, lalu dikompresi untuk dikirim lewat telemedisin. | Mammografi, Telemedisin | Pengolahan Citra Medis, Pembelajaran Mesin Untuk Data Medis |
| 9 | Aplikasi Mobile Doctor Brain AI<br>*Mobile Doctor Brain AI App* | 140–150 | Aplikasi seluler untuk stroke: klasifikasi SVM, case-based reasoning, dan optimasi PSO untuk mendukung keputusan dari data pemantauan. | EEG, Telemedisin | Pemrograman Perangkat Bergerak, Pembelajaran Mesin Untuk Data Medis |
| 10 | Teleradiologi cerdas berbasis cloud<br>*An AI Mobile Cloud Computing Tool* | 151–157 | Case-based reasoning dan jaringan saraf di cloud untuk mencari kasus radiologi serupa dan membantu diagnosis kanker dari jarak jauh. | Telemedisin, X-Ray | Big Data dalam Kesehatan, Pembelajaran Mesin Untuk Data Medis, Komunikasi Data Medis |
| 11 | Antarmuka kendali robot di Unity3D<br>*Advanced Intelligent Robot Control Interfaces* | 158–173 | Simulasi robot 5 derajat kebebasan di Unity3D: komponen sendi prismatik dan revolut, struktur kelas, dan antarmuka kendali virtual. | Robot Bedah | Robotika untuk Kedokteran, Sistem Kendali, Algoritma dan Pemrograman Komputer |
| 12 | Analisis teknologi telemedisin<br>*Analysis of Telemedicine Technologies* | 174–183 | Jenis layanan telemedisin dan telehealth, manfaat untuk pasien jantung dan daerah terpencil, serta hambatan adopsi. | Telemedisin | Komunikasi Data Medis, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 13 | Posisi kritis robot berjalan<br>*Critical Position using Environment Model Applied on Walking Robots* | 184–196 | Model matematis lingkungan dan dinamika robot berjalan untuk menemukan posisi kritis sebelum robot jatuh. |  | Robotika untuk Kedokteran, Pengantar Biomekanik |
| 14 | Pemulihan keseimbangan robot berjalan (NAO)<br>*The Walking Robot Equilibrium Recovery* | 197–207 | Kendali keseimbangan robot bipedal saat diganggu, memakai model pergelangan kaki dan pengendali LQR. | Prostesis Tangan | Sistem Kendali, Robotika untuk Kedokteran, Pengantar Biomekanik |
| 15 | Robot LEGO sebagai alat bantu belajar anak autis<br>*Development of A Robotic Teaching Aid for Disabled Children* | 208–218 | Robot LEGO Mindstorms dipakai mengajarkan bentuk dan interaksi sosial pada anak autis; hasil uji dibandingkan pengajaran biasa. |  | Desain Teknologi Difabel dan Alat Bantu, Robotika untuk Kedokteran |
| 16 | Robot rehabilitasi tungkai bawah dengan VR<br>*Training System Design of Lower Limb Rehabilitation Robot based on VR* | 219–238 | Perencanaan lintasan sendi, kecepatan, dan percepatan robot rehabilitasi, dipadukan dengan game VR agar latihan lebih menarik. | Brace, EMS | Robotika untuk Kedokteran, Pengantar Biomekanik, Sistem Kendali |
| 17 | Mengendalikan peralatan rumah dengan EEG (BCI)<br>*Automation of Appliances Using Electroencephalography* | 239–257 | Dasar gelombang otak, elektroda invasif dan non-invasif, serta brain-computer interface untuk menyalakan perangkat rumah. | EEG, BrainWave, NFB | Pengolahan Sinyal Biomedik, Pengantar Sistem Internet of Things, Desain Teknologi Difabel dan Alat Bantu |
| 18 | Tongkat pintar ultrasonik untuk tunanetra<br>*Designing a Beautiful Life for Indian Blind Peoples: A Smart Stick* | 258–271 | Sensor ultrasonik dan NodeMCU mendeteksi rintangan lalu memberi bunyi buzzer; data bisa dikirim lewat IoT. |  | Pengantar Sistem Internet of Things, Desain Teknologi Difabel dan Alat Bantu, Sensor dan Transduser Biomedis, Mikrokontroler dan Sistem Tertanam |
| 19 | Rumah pintar: asisten dan pemantau bayi<br>*Smart Home: Personal Assistant and Baby Monitoring System* | 272–298 | Modul sensor suhu, suara, dan kamera dengan pengenalan wajah untuk memantau bayi dan memberi notifikasi ke orang tua. | Inkubator, Termometer | Pengantar Sistem Internet of Things, Sistem Monitoring Elektronik Kesehatan, Sistem Tertanam pada Teknologi Kedokteran |

## Healthcare Implementations of Wearable Technology (FTF-HCR-F0083)

Jose Fernandez, Freescale Semiconductor · Freescale Technology Forum (slide) · 2014 · 101 halaman · `Referensi\4_Healthcare Implementations of Wearable Technology.pdf`

Slide seminar tentang WaRP (Wearable Reference Platform): desain hibrida prosesor i.MX 6SoloLite (Android) dan mikrokontroler Kinetis KL16, sensor pedometer MMA9553, papan detak jantung, pengisian nirkabel, dan teknik hemat daya. Rujukan praktis untuk merancang smartwatch kesehatan.

Alat: Smartwatch, SpO2, EKG, Dispenser Obat, Holter

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Pasar perangkat wearable<br>*Wearable Market Description* | 5–12 | Segmen wearable kesehatan dan kebugaran (monitor detak jantung, pedometer, pemantau aktivitas), tren pasar, dan ragam pemakaian. | Smartwatch | Sistem Monitoring Elektronik Kesehatan, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 2 | Tantangan desain: daya, ruang, kemudahan pakai<br>*Market Challenge* | 13–15 | Konsumsi daya, ukuran kecil, dan kenyamanan menjadi kunci. Pengisian USB sudah standar; pengisian nirkabel lebih cocok untuk perangkat tahan air. | Smartwatch | Desain Teknologi Kesehatan, Sistem Tertanam pada Teknologi Kedokteran |
| 3 | Platform referensi WaRP<br>*Freescale Wearable Reference Platform: WaRP* | 16–39 | Arsitektur hibrida: papan utama i.MX 6SoloLite menjalankan Android dengan LP-DDR2, pengisi baterai LiPo, USB OTG, layar; papan tambahan Kinetis KL16 untuk sensor dan pedometer MMA9553L. | Smartwatch | Sistem Tertanam pada Teknologi Kedokteran, Mikrokontroler dan Sistem Tertanam, Elektronika Digital |
| 4 | Papan anak kesehatan: detak jantung dan mode mandiri<br>*Healthcare and Fitness Daughter Board and Standalone Mode* | 40–45 | Papan sensor kesehatan (bersama ROHM) untuk detak jantung kontinu, EKG, dan pedometer; bisa jalan mandiri hanya dengan MCU untuk menghemat baterai. | Smartwatch, SpO2, EKG | Sensor dan Transduser Biomedis, Instrumentasi Biomedis, Sistem Monitoring Elektronik Kesehatan |
| 5 | Dasar mikrokontroler Kinetis L (ARM Cortex-M0+)<br>*Kinetis L16 MCU Basics* | 46–63 | Inti Cortex-M0+, Bit Manipulation Engine, Fast I/O, dan periferal yang membuat MCU kecil cocok untuk perangkat wearable. | Smartwatch, Dispenser Obat | Mikrokontroler dan Sistem Tertanam, Sistem Tertanam pada Teknologi Kedokteran |
| 6 | Mode hemat daya mikrokontroler<br>*Kinetis L16 MCU Power Saving Modes* | 64–98 | Mode Wait, Stop, VLPS, dan deep sleep; clock gating, DMA asinkron, UART/SPI/TPM yang tetap bekerja saat inti tidur, untuk memperpanjang umur baterai. | Smartwatch, Holter | Mikrokontroler dan Sistem Tertanam, Sistem Tertanam pada Teknologi Kedokteran, Elektronika Analog |
| 7 | Demo dan contoh pemakaian<br>*Demo* | 99–101 | Demonstrasi WaRP: penghitung langkah, pemantauan detak jantung, dan sinkronisasi ke aplikasi. | Smartwatch | Pengantar Sistem Internet of Things, Pemrograman Perangkat Bergerak |

## Implementing an Electronic Health Record System

James M. Walker, Eric J. Bieber, Frank Richards (ed.) · Springer · 2005 · 252 halaman · `Referensi\5_Implementing an Electronic Health Record System.pdf`

Pengalaman Geisinger Health System menerapkan rekam medis elektronik (Epic) dari nol: kesiapan organisasi, pemilihan vendor, infrastruktur, alur kerja, pelatihan, clinical decision support, sampai portal pasien. Pegangan untuk mata kuliah SIMRS dan Manajemen Data.

Alat: RME, Telemedisin, Kimia Klinik, Infusion Pump

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Iklim organisasi<br>*Organizational Climate* | 18–23 | RME berhasil bila pimpinan dan dokter mendukung. Geisinger memandang investasi TI sebagai strategi klinis, bukan sekadar biaya. | RME | Sistem Informasi Manajemen Rumah Sakit, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 2 | Analisis kebutuhan<br>*Needs Assessment* | 24–29 | Menetapkan tujuan dan ukuran keberhasilan sebelum membeli sistem: proses apa yang ingin diperbaiki dan bagaimana mengukurnya. | RME | Sistem Informasi Manajemen Rumah Sakit, Critical and Design Thinking |
| 3 | Memilih vendor dan negosiasi kontrak<br>*Vendor Selection and Contract Negotiation* | 30–35 | Kriteria memilih vendor RME, kunjungan ke pengguna lain, isi kontrak (akses data, dukungan, biaya), dan rencana bila vendor gagal. | RME | Sistem Informasi Manajemen Rumah Sakit, Kalibrasi dan Manajemen Alat Kesehatan |
| 4 | Infrastruktur jaringan dan server<br>*Infrastructure* | 36–50 | Bandwidth, server, keamanan, akses jarak jauh, dan ketersediaan tinggi. RME yang lambat akan ditinggalkan dokter. | RME, Telemedisin | Komunikasi Data Medis, Sistem Informasi Manajemen Rumah Sakit, Big Data dalam Kesehatan |
| 5 | Penilaian dan desain ulang alur kerja<br>*Workflow Assessment and Redesign* | 51–54 | Memetakan alur kerja klinik (janji temu, pengambilan rekam medis) dan mendesain ulangnya agar RME menyederhanakan, bukan menambah pekerjaan. | RME | Sistem Informasi Manajemen Rumah Sakit, Desain Teknologi Kesehatan |
| 6 | Tim implementasi<br>*Staffing and Managing Implementation Teams* | 55–59 | Peran physician champion, analis klinis, CMIO, dan staf sementara; cara mengelola tim saat go-live. | RME | Sistem Informasi Manajemen Rumah Sakit, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 7 | Usability RME<br>*Usability* | 60–70 | Prinsip antarmuka klinis: beban memori, tampilan hasil lab, uji usability dengan pengguna nyata, dan contoh kesalahan desain. | RME | Interaksi Pasien Dengan Teknologi Kedokteran, Desain Teknologi Kesehatan, Visualisasi Data Medis |
| 8 | Pelatihan pengguna<br>*Training* | 71–79 | Merancang pelatihan berbasis tugas nyata, pelatih dari kalangan klinis, lingkungan latihan, dan dukungan saat go-live. | RME | Sistem Informasi Manajemen Rumah Sakit |
| 9 | Clinical decision support (CDS)<br>*Clinical Decision Support* | 80–89 | Pengingat, order set, dan peringatan yang membantu dokter tanpa menimbulkan kelelahan alarm. | RME | Sistem Informasi Manajemen Rumah Sakit, Pembelajaran Mesin Untuk Data Medis, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 10 | Menerjemahkan kewenangan klinis ke sistem<br>*Translating Scope of Practice* | 90–101 | Siapa boleh memesan apa: aturan supervisi, otorisasi order, dan peran tiap profesi diatur di RME. | RME | Sistem Informasi Manajemen Rumah Sakit |
| 11 | Integrasi sistem<br>*System Integration* | 102–104 | Menghubungkan RME dengan penjadwalan, lab, radiologi, dan billing lewat antarmuka dan basis data bersama. | RME, Kimia Klinik | Komunikasi Data Medis, Manajemen Data |
| 12 | Dukungan operasional<br>*Production Support* | 105–113 | Help desk, penanganan masalah, upgrade, dan keterampilan tim pendukung setelah sistem berjalan. | RME | Sistem Informasi Manajemen Rumah Sakit |
| 13 | Mengelola kemitraan dengan vendor<br>*Managing the Client-Vendor Partnership* | 114–121 | Membangun hubungan jangka panjang dengan vendor: kelompok pengguna, permintaan fitur, dan eskalasi. | RME | Sistem Informasi Manajemen Rumah Sakit, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 14 | Implementasi bertahap<br>*Phased Implementation* | 122–130 | Menerapkan RME per klinik dan per fitur: daftar masalah, order entry, billing; pelajaran dari tiap gelombang go-live. | RME | Sistem Informasi Manajemen Rumah Sakit |
| 15 | Optimasi di layanan primer<br>*Optimizing Primary-Care Practices* | 131–138 | Pesan internal, preferensi pengguna, dan pembagian tugas perawat-dokter agar RME menghemat waktu di klinik umum. | RME | Sistem Informasi Manajemen Rumah Sakit, Teknologi dalam Bidang Keperawatan |
| 16 | Optimasi di klinik spesialis<br>*Optimizing Specialty Practices* | 139–140 | Klinik spesialis butuh templat dan order khusus; implementasi menyesuaikan kompleksitasnya. | RME | Sistem Informasi Manajemen Rumah Sakit |
| 17 | Perangkat lunak khusus<br>*Special-Purpose Software* | 141–151 | Kapan memakai software khusus (misal uji klinis, onkologi) di samping RME inti dan cara mengintegrasikannya. | RME | Sistem Informasi Manajemen Rumah Sakit, Manajemen Data |
| 18 | RME di rawat inap: CPOE dan dokumentasi<br>*Optimizing Inpatient Care* | 152–163 | Computerized physician order entry, order set standar, catatan klinis, dan ringkasan pulang di bangsal. | RME, Infusion Pump | Sistem Informasi Manajemen Rumah Sakit, Teknologi dalam Bidang Keperawatan |
| 19 | Portal pasien<br>*Extending EHR Access to Patients* | 164–175 | Akses pasien ke rekam medis dan pesan aman: kata sandi, dukungan, akses orang tua, dan dampaknya ke beban kerja. | RME, Telemedisin | Sistem Informasi Manajemen Rumah Sakit, Interaksi Pasien Dengan Teknologi Kedokteran, Pemrograman Perangkat Bergerak |
| 20 | Akses untuk dokter luar<br>*Extending EHR Access to External Physicians* | 176–181 | Portal untuk dokter perujuk agar komunikasi dan kesinambungan perawatan lebih baik. | RME | Sistem Informasi Manajemen Rumah Sakit, Komunikasi Data Medis |
| 21 | Ringkasan, prospek, dan lampiran<br>*Summary and Prospects* | 182–252 | Rangkuman pelajaran Geisinger dan lampiran contoh dokumen: kebijakan keamanan, daftar periksa, dan formulir implementasi. | RME | Sistem Informasi Manajemen Rumah Sakit, Manajemen Data |

## Introduction to Medical Laboratory Technology, ed. 5

F. J. Baker, R. E. Silverton · Butterworths · 1976 · 730 halaman · `Referensi\6_Introduction to Medical Laboratory Technology.pdf`

Buku klasik teknisi laboratorium medis: peralatan gelas, mikroskop, kimia klinik, histologi, mikrobiologi, hematologi, dan golongan darah. Menjelaskan prinsip di balik alat laboratorium modern di aplikasi ini (hematology analyzer, kimia klinik, koagulasi, urin analyzer, autoklaf).

Alat: Sentrifus, Mikroskop, Autoklaf, Hematologi, Urinalisis, Kimia Klinik, ISE, FIA, Glukometer, Fototerapi, HD, Koagulasi, Infusion Pump

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Peralatan gelas laboratorium<br>*General Laboratory Glassware* | 8–29 | Jenis gelas, pipet, labu, tabung sentrifus, cara membersihkan, dan air suling atau deionisasi. | Sentrifus | Kimia, Keselamatan Listrik Medis dan K3 |
| 2 | Dasar mikroskopi<br>*Elementary Microscopy* | 30–63 | Lensa, objektif, okuler, kondensor, diafragma, panjang fokus, dan cara memfokuskan untuk mendapat citra tajam. | Mikroskop | Fisika Dasar, Biologi Kedokteran |
| 3 | Keselamatan laboratorium<br>*Safety Precautions* | 64–70 | Penyimpanan bahan kimia mudah terbakar dan korosif, pertolongan pertama, dan kebiasaan aman di laboratorium. | Autoklaf | Keselamatan Listrik Medis dan K3, Kimia |
| 4 | Pengambilan dan pelaporan spesimen<br>*Collection and Reporting of Specimens* | 71–79 | Wadah, antikoagulan, swab steril, pelabelan, dan pelaporan hasil agar spesimen tidak rusak atau tertukar. | Hematologi, Urinalisis | Biologi Kedokteran, Manajemen Data |
| 5 | Dasar kimia: larutan dan titrasi<br>*Some Fundamentals of Chemistry* | 80–114 | Mol, ekuivalen, larutan standar, asam-basa, indikator, dan titrasi sebagai dasar semua pemeriksaan kimia. | Kimia Klinik, ISE | Kimia |
| 6 | Instrumentasi: kolorimetri, elektroda, kromatografi<br>*Instrumentation* | 115–156 | Hukum Beer-Lambert dan absorbansi, kolorimeter dan fotometer, elektroda pH, elektroforesis, dan kromatografi kertas. | Kimia Klinik, ISE, FIA | Instrumentasi Biomedis, Fisika Medis, Kimia |
| 7 | Pengantar kimia klinik<br>*Introduction to Clinical Chemistry* | 157–174 | Cairan tubuh, plasma, hormon (tiroid, pituitari), dan metabolisme sebagai dasar memahami hasil laboratorium. | Kimia Klinik | Fisiologi Kedokteran, Biologi Kedokteran |
| 8 | Fungsi lambung, pankreas, dan glukosa darah<br>*Gastric and Pancreatic Function* | 175–220 | Uji asam lambung, enzim pankreas, uji toleransi glukosa, dan pemeriksaan feses. | Glukometer, Kimia Klinik | Fisiologi Kedokteran, Kimia |
| 9 | Uji fungsi hati<br>*Liver Function Tests* | 221–235 | Bilirubin, urobilinogen (reagen Ehrlich), garam empedu, dan jenis ikterus. | Kimia Klinik, Fototerapi | Fisiologi Kedokteran, Kimia |
| 10 | Uji fungsi ginjal dan urinalisis<br>*Renal Function Tests* | 236–285 | Protein, glukosa, dan urea urin, strip reagen, bersihan, dan uji pemekatan. | Urinalisis, HD, Kimia Klinik | Fisiologi Kedokteran, Kimia |
| 11 | Analisis kimia cairan serebrospinal<br>*Chemical Analysis of Cerebrospinal Fluid* | 286–299 | Protein, globulin, glukosa, dan klorida CSF serta artinya pada meningitis. | Kimia Klinik | Anatomi, Kimia |
| 12 | Pengantar histologi<br>*Introduction to Histology* | 300–312 | Sel, jaringan, inti, sitoplasma, dan pembelahan sel sebagai dasar membaca preparat. | Mikroskop | Biologi Kedokteran, Anatomi |
| 13 | Fiksasi jaringan<br>*Fixation* | 313–328 | Formalin dan fiksatif lain menghentikan pembusukan dan mempertahankan struktur jaringan. | Mikroskop | Biologi Kedokteran, Kimia |
| 14 | Dekalsifikasi<br>*Decalcification* | 329–337 | Melunakkan tulang dan gigi dengan asam atau kelator agar bisa diiris; uji titik akhir dekalsifikasi. | Mikroskop | Biologi Kedokteran, Biomaterial |
| 15 | Dehidrasi, penjernihan, dan penanaman paraffin<br>*Dehydration, Clearing and Embedding* | 338–358 | Alkohol bertingkat, clearing, dan paraffin atau celloidin untuk membuat blok jaringan. | Mikroskop | Biologi Kedokteran |
| 16 | Pemotongan dengan mikrotom<br>*Section Cutting* | 359–384 | Jenis mikrotom, sudut dan ketajaman pisau, ketebalan irisan, dan potong beku. | Mikroskop | Biologi Kedokteran, Fisika Mekanika |
| 17 | Prinsip pewarnaan biologis<br>*Biological Staining* | 385–393 | Zat warna asam dan basa, hematoksilin, mordan, dan mengapa jaringan menyerap warna berbeda. | Mikroskop | Kimia, Biologi Kedokteran |
| 18 | Prosedur pewarnaan<br>*Staining Procedures* | 394–426 | Langkah pewarnaan H&E dan pewarnaan khusus: larutan, waktu, dan hasil yang diharapkan. | Mikroskop | Biologi Kedokteran |
| 19 | Teknik sitologi<br>*Cytological Techniques* | 427–438 | Apusan sel, fiksasi alkohol, dan pewarnaan Papanicolaou untuk skrining sel abnormal. | Mikroskop | Biologi Kedokteran, Pengolahan Citra Medis |
| 20 | Pengantar mikrobiologi<br>*Introduction to Microbiology* | 439–448 | Bakteri, virus, bentuk kokus dan basil, dan hubungan mikroorganisme dengan penyakit. |  | Biologi Kedokteran |
| 21 | Pemeriksaan bakteri dengan mikroskop (Gram)<br>*Microscopic Examination of Bacteria* | 449–462 | Membuat apusan, fiksasi panas, pewarnaan Gram dan Ziehl-Neelsen. | Mikroskop | Biologi Kedokteran |
| 22 | Sterilisasi<br>*Sterilization* | 463–473 | Uap bertekanan (autoklaf), panas kering, dan filtrasi; hubungan suhu, tekanan, waktu, dan spora. | Autoklaf | Mekanika Fluida dan Termodinamika, Keselamatan Listrik Medis dan K3, Biologi Kedokteran |
| 23 | Penggunaan media kultur<br>*The Use of Culture Media* | 474–478 | Inokulasi cawan petri dan tabung, isolasi koloni, dan syarat media yang baik. |  | Biologi Kedokteran |
| 24 | Pembuatan media kultur<br>*Preparation of Culture Media* | 479–507 | Agar, kaldu nutrien, agar darah, pH, dan sterilisasi media. | Autoklaf | Biologi Kedokteran, Kimia |
| 25 | Kultur anaerob<br>*Anaerobic Cultivation* | 508–512 | Toples anaerob, penggantian udara dengan hidrogen, dan indikator kondisi tanpa oksigen. |  | Biologi Kedokteran |
| 26 | Reaksi antigen-antibodi<br>*Antigen–Antibody Reactions* | 513–517 | Aglutinasi, pengenceran serum, dan dasar uji serologi. | FIA | Biologi Kedokteran |
| 27 | Pemeriksaan bakteriologis spesimen<br>*Bacteriological Examination* | 518–544 | Pemeriksaan darah, sputum, urin, dan swab; inkubasi, identifikasi, dan uji kepekaan antibiotik. |  | Biologi Kedokteran |
| 28 | Pengantar hematologi<br>*Introduction to Haematology* | 545–556 | Sel darah merah, sel darah putih, trombosit, sumsum tulang, dan morfologi pada apusan. | Hematologi | Fisiologi Kedokteran, Biologi Kedokteran |
| 29 | Pembekuan darah<br>*Blood Coagulation* | 557–561 | Jalur intrinsik dan ekstrinsik, faktor pembekuan, protrombin, trombin, dan fibrin. | Koagulasi | Fisiologi Kedokteran |
| 30 | Menghitung sel darah<br>*Enumeration of Blood Cells* | 562–595 | Hemositometer, pipet pengencer, kotak hitung, dan rumus jumlah sel; dasar sebelum ada hematology analyzer. | Hematologi, Mikroskop | Instrumentasi Biomedis, Statistika |
| 31 | Pengukuran hemoglobin<br>*Haemoglobin Estimation* | 596–602 | Metode absorptiometri dengan larutan standar dan konversi ke g/dL. | Hematologi | Instrumentasi Biomedis, Fisika Medis |
| 32 | Laju endap darah dan fragilitas<br>*Erythrocyte Sedimentation Rate* | 603–610 | Metode Westergren dan Wintrobe, volume sel padat, dan uji fragilitas osmotik. | Hematologi, Sentrifus | Fisiologi Kedokteran |
| 33 | Uji pembekuan darah<br>*Tests for Blood Coagulation* | 611–616 | Waktu perdarahan, waktu pembekuan, dan waktu protrombin. | Koagulasi | Fisiologi Kedokteran, Instrumentasi Biomedis |
| 34 | Indeks hematologi<br>*Haematological Indices* | 617–629 | MCV, MCH, dan MCHC dihitung dari hitung eritrosit, hemoglobin, dan hematokrit. | Hematologi | Statistika, Fisiologi Kedokteran |
| 35 | Pewarisan golongan darah ABO<br>*Inheritance of the ABO Groups* | 630–632 | Genotipe, fenotipe, dan kemungkinan golongan darah anak dari orang tua. |  | Biologi Kedokteran |
| 36 | Sistem Rhesus<br>*The Rhesus System* | 633–636 | Antigen D, Rh positif dan negatif, dan risiko inkompatibilitas pada kehamilan. |  | Biologi Kedokteran |
| 37 | Imunoglobulin golongan darah<br>*Blood Group Immunoglobulins* | 637–644 | Antibodi IgM dan IgG, uji antiglobulin (Coombs). | FIA | Biologi Kedokteran |
| 38 | Transfusi darah<br>*Blood Transfusion* | 645–657 | Seleksi donor, penyimpanan darah di suhu terkendali, antikoagulan, dan pencegahan infeksi. | Infusion Pump | Fisiologi Kedokteran, Keselamatan Listrik Medis dan K3 |
| 39 | Teknik penggolongan darah dan lampiran<br>*Blood Grouping Technique* | 658–730 | Uji golongan darah di slide dan tabung, uji silang (crossmatch), serta lampiran metode dan tabel. | FIA, Sentrifus | Biologi Kedokteran, Instrumentasi Biomedis |

## Medical Devices: Surgical and Image-Guided Technologies

Martin Culjat, Rahul Singh, Hua Lee (ed.) · Wiley · 2013 · 454 halaman · `Referensi\7_Medical devices and technology.pdf`

Buku teknik alat medis untuk bedah dan pencitraan: proses desain dan regulasi, laparoskopi, bedah mata, robot bedah, kateter, elektrosurgeri, ablasi, laser, stent, alat bantu jantung, implan ortopedi, endoskopi, USG, sinar-X, dan neuronavigasi. Sangat dekat dengan Teknologi Bedah dan Pencitraan.

Alat: Oralytic, Endoskop, Robot Bedah, Fako, Kateter-Stent, Fluoroskopi, ESU, RFA, MWD, Laser, Fototerapi, LVAD, Brace, Prostesis Tangan, USG, US Terapi, X-Ray, Mammografi, CT Scan, Neuronavigasi, MRI

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Pengantar dan sejarah alat medis<br>*Introduction* | 25–34 | Sejarah alat bedah dari zaman kuno sampai rekayasa modern, dan klasifikasi besar alat medis. |  | Pengantar Teknologi Kedokteran, Teknologi dalam Ilmu Kedokteran Bedah |
| 2 | Desain dan regulasi alat medis<br>*Design of Medical Devices* | 35–52 | Alur pengembangan dari konsep, prototipe, verifikasi-validasi, manajemen risiko, kelas alat (I, II, III), standar internasional, sampai produksi. | Oralytic | Desain Teknologi Kesehatan, Purwarupa Cepat Untuk Alat Kesehatan, Kalibrasi dan Manajemen Alat Kesehatan |
| 3 | Instrumen bedah laparoskopi<br>*Instrumentation for Laparoscopic Surgery* | 53–72 | Trokar, insuflasi, grasper, gunting, stapler, dan teknik akses perut minimal invasif. | Endoskop, Robot Bedah | Teknologi dalam Ilmu Kedokteran Bedah, Pengantar Biomekanik |
| 4 | Instrumen bedah mata: fakoemulsifikasi dan vitrektomi<br>*Surgical Instruments in Ophthalmology* | 73–86 | Handpiece ultrasonik memecah lensa katarak, sistem irigasi-aspirasi menjaga tekanan bola mata, pemotong vitreus untuk bedah retina. | Fako | Teknologi dalam Ilmu Kedokteran Bedah, Mekanika Fluida dan Termodinamika |
| 5 | Robot bedah<br>*Surgical Robotics* | 87–122 | Sistem master-slave, tingkat otonomi, robot ortopedi dan bedah saraf, umpan balik gaya, dan tantangan keselamatan. | Robot Bedah | Robotika untuk Kedokteran, Sistem Kendali, Teknologi dalam Ilmu Kedokteran Bedah |
| 6 | Kateter dan guidewire<br>*Catheters in Vascular Therapy* | 123–144 | Desain kateter, guidewire, balon angioplasti, dan cara alat dinavigasi di dalam pembuluh darah. | Kateter-Stent, Fluoroskopi | Biomaterial, Teknologi dalam Ilmu Kedokteran Bedah |
| 7 | Alat hemostasis berbasis energi (elektrosurgeri)<br>*Energy-Based Hemostatic Surgical Devices* | 145–160 | Arus frekuensi tinggi memotong dan mengoagulasi jaringan; mode monopolar dan bipolar, elektroda netral, dan bahaya luka bakar. | ESU | Keselamatan Listrik Medis dan K3, Fisika Listrik dan Magnet, Teknologi dalam Ilmu Kedokteran Bedah |
| 8 | Sistem ablasi jaringan (RFA, mikrogelombang, krio)<br>*Tissue Ablation Systems* | 161–186 | Panas atau dingin menghancurkan tumor; deposisi energi, pemodelan suhu, dan pemantauan zona ablasi. | RFA, MWD | Fisika Medis, Teknologi dalam Ilmu Kedokteran Bedah |
| 9 | Laser dalam kedokteran<br>*Lasers in Medicine* | 187–222 | Prinsip laser, interaksi laser-jaringan (fototermal, fotoablasi), laser retina, dermatologi, dan OCT. | Laser, Fototerapi | Fisika Medis, Fisika Radiasi dan Proteksi Radiasi |
| 10 | Stent dan katup jantung transkateter<br>*Vascular and Cardiovascular Devices* | 223–242 | Stent logam dan pelepas obat, nitinol yang bisa kembali ke bentuk asal, katup transkateter, dan desain permukaan. | Kateter-Stent | Biomaterial, Teknologi dalam Ilmu Kedokteran Bedah |
| 11 | Alat bantu sirkulasi mekanis (LVAD, IABP)<br>*Mechanical Circulatory Support Devices* | 243–264 | Pompa darah pulsatil dan kontinu (HeartMate), balon intra-aorta, kontrol aliran, dan komplikasi. | LVAD | Mekanika Fluida dan Termodinamika, Sistem Kendali, Biomaterial |
| 12 | Implan ortopedi<br>*Orthopedic Implants* | 265–300 | Penggantian sendi panggul dan lutut, implan tulang belakang, fiksasi fraktur, keausan permukaan, dan pemilihan material. | Brace, Prostesis Tangan | Biomaterial, Pengantar Biomekanik, Desain Teknologi Berbantu Komputer untuk Medis |
| 13 | Endoskopi<br>*Endoscopy* | 301–326 | Endoskop kaku dan fleksibel, sumber cahaya, kamera video, kanal instrumen, dan desain optik. | Endoskop | Teknologi dalam Ilmu Kedokteran Bedah, Teknologi Pencitraan Medis |
| 14 | Perangkat ultrasonografi<br>*Medical Ultrasound Devices* | 327–364 | Material piezoelektrik, transduser larik linear dan fase, pembentukan berkas, frekuensi dan resolusi, serta aplikasi terapi. | USG, US Terapi | Teknologi Pencitraan Medis, Sensor dan Transduser Biomedis, Fisika Medis |
| 15 | Pencitraan sinar-X<br>*Medical X-ray Imaging* | 365–398 | Produksi foton, interaksi dengan jaringan, film versus detektor digital, ukuran piksel, dan teknik akuisisi. | X-Ray, Fluoroskopi, Mammografi, CT Scan | Fisika Radiasi dan Proteksi Radiasi, Teknologi Pencitraan Medis |
| 16 | Navigasi dalam bedah saraf<br>*Navigation in Neurosurgery* | 399–454 | Pelacakan optik dan elektromagnetik, registrasi citra ke pasien, USG intraoperatif, dan ablasi laser terarah. | Neuronavigasi, MRI, CT Scan | Teknologi dalam Ilmu Kedokteran Bedah, Pengolahan Citra Medis, Robotika untuk Kedokteran |

## Medical Ethics in Clinical Practice

Matjaž Zwitter · Springer · 2019 · 217 halaman · `Referensi\8_Medical Ethics in Clinical Practice.pdf`

Etika kedokteran yang dekat dengan praktik: empat prinsip (otonomi, beneficence, non-maleficence, keadilan), komunikasi, malapraktik, sumber daya terbatas, awal dan akhir kehidupan, genetika, riset klinis, dan seminar kasus untuk mahasiswa. Penting untuk alat yang menyentuh data dan keputusan pasien.

Alat: Infusion Pump, Telemedisin, RME, Oralytic, USG, CTG, Inkubator, Ventilator, Patient Monitor, Dispenser Obat

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Etika dan hukum<br>*Ethics and Law* | 14–18 | Beda norma etika dan aturan hukum, serta kapan keduanya berbenturan. |  | Interaksi Pasien Dengan Teknologi Kedokteran, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 2 | Kode etik dan deklarasi<br>*Ethical Codes and Declarations* | 19–25 | Sumpah Hipokrates, Deklarasi Helsinki dan Jenewa, serta kode etik profesi. |  | Interaksi Pasien Dengan Teknologi Kedokteran, Metode Penelitian Teknologi Kedokteran |
| 3 | Teori etika<br>*Ethical Theories* | 26–32 | Utilitarianisme, etika kebajikan, deontologi, dan empat prinsip bioetika. |  | Interaksi Pasien Dengan Teknologi Kedokteran |
| 4 | Status moral<br>*Moral Status* | 33–38 | Siapa yang punya hak moral: embrio, pasien koma, hewan percobaan. |  | Biologi Kedokteran |
| 5 | Analisis etika kasus<br>*Ethical Analysis* | 39–44 | Langkah menimbang manfaat, risiko, dan otonomi; contoh penolakan transfusi. | Infusion Pump | Interaksi Pasien Dengan Teknologi Kedokteran, Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 6 | Otonomi dan batasnya<br>*Autonomy and Its Limitations* | 45–46 | Hak pasien memutuskan, pengambil keputusan pengganti, dan kapan otonomi dibatasi. |  | Interaksi Pasien Dengan Teknologi Kedokteran |
| 7 | Komunikasi dengan pasien<br>*Communication* | 47–62 | Menyampaikan kabar buruk, informed consent, dan informasi bagi keluarga. | Telemedisin | Interaksi Pasien Dengan Teknologi Kedokteran |
| 8 | Hubungan dalam tim medis<br>*Relations in the Medical Team* | 63–66 | Kerja sama dokter-perawat, perbedaan pendapat, dan komunikasi tim. |  | Teknologi dalam Bidang Keperawatan |
| 9 | Malapraktik<br>*Professional Malpractice* | 67–72 | Kesalahan medis, kompensasi, peran media, dan budaya belajar dari kesalahan. | RME | Keselamatan Listrik Medis dan K3, Kalibrasi dan Manajemen Alat Kesehatan |
| 10 | Sumber daya terbatas dan prioritas<br>*Limited Resources, Priorities* | 73–81 | Daftar tunggu, biaya, korupsi, dan cara adil membagi layanan. |  | Tatalaksana Klinis dan Rintisan Bisnis Digital, Sistem Informasi Manajemen Rumah Sakit |
| 11 | Citra dokter<br>*Image of a Physician* | 82–89 | Kepercayaan publik, praktik swasta, burnout, dan keberatan hati nurani. |  | Interaksi Pasien Dengan Teknologi Kedokteran |
| 12 | Kedokteran pencegahan<br>*Preventive Medicine* | 90–94 | Vaksinasi, skrining, gaya hidup, dan etika program kesehatan masyarakat. | Oralytic | Teknologi dalam Ilmu Kedokteran Medik |
| 13 | Etika di awal kehidupan<br>*Ethics at the Beginning of Life* | 95–103 | Kontrasepsi, aborsi, reproduksi berbantu, dan diagnosis prenatal. | USG, CTG | Biologi Kedokteran |
| 14 | Pediatri<br>*Pediatrics* | 104–111 | Hak anak, keputusan orang tua, penolakan vaksin, dan riset pada anak. | Inkubator | Interaksi Pasien Dengan Teknologi Kedokteran |
| 15 | Genetika<br>*Genetics* | 112–119 | Uji genetik, konseling, kerahasiaan, dan seleksi embrio. |  | Biologi Kedokteran |
| 16 | Gawat darurat, ICU, dan transplantasi<br>*Emergency Medicine and Transplantation* | 120–125 | Menghentikan terapi di ICU, mati batang otak, dan donasi organ. | Ventilator, Patient Monitor | Teknologi dalam Ilmu Kedokteran Medik |
| 17 | Lansia dan pasien gangguan jiwa<br>*The Elderly and the Mentally Ill* | 126–133 | Otonomi yang berkurang, perawatan paksa, dan perlindungan dari penelantaran. | Dispenser Obat | Interaksi Pasien Dengan Teknologi Kedokteran, Desain Teknologi Difabel dan Alat Bantu |
| 18 | Menjelang kematian<br>*Dying and Death* | 134–140 | Perawatan paliatif, eutanasia, dan bunuh diri berbantuan dokter. |  | Interaksi Pasien Dengan Teknologi Kedokteran |
| 19 | Riset dan uji klinis<br>*Research* | 141–155 | Fase uji klinis, informed consent, komite etik, dan plasebo. | Oralytic | Metode Penelitian Teknologi Kedokteran, Statistika |
| 20 | Metode diagnosis dan terapi yang belum terbukti<br>*Unproven Methods of Diagnostics and Treatment* | 156–161 | Pengobatan alternatif, hak pasien memilih, dan tanggung jawab dokter. |  | Metode Penelitian Teknologi Kedokteran |
| 21 | Dokter di luar pelayanan pasien<br>*Physicians Beyond Patient Care* | 162–169 | Kedokteran olahraga, industri farmasi, dan konflik kepentingan. |  | Tatalaksana Klinis dan Rintisan Bisnis Digital |
| 22 | Seminar kasus mahasiswa<br>*Student Seminars* | 170–217 | Kumpulan kasus untuk diskusi kelompok dengan pertanyaan pemandu. |  | Interaksi Pasien Dengan Teknologi Kedokteran, Critical and Design Thinking |

## Telemedicine Technologies: Information Technologies in Medicine and Telehealth

Bernard Fong, A. C. M. Fong, C. K. Li · Wiley · 2011 · 284 halaman · `Referensi\9_Telemedicine Technologies_ Information Technologies in Medicine.pdf`

Teknologi di balik telemedisin: jaringan komunikasi, pemantauan pasien nirkabel, pengolahan informasi medis, penerapan sistem, keamanan data, dan perawatan komunitas. Pendamping mata kuliah Komunikasi Data Medis, IoT, dan Sistem Monitoring.

Alat: Telemedisin, Patient Monitor, Smartwatch, Holter, EKG, NIBP, RME, Dispenser Obat

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Pengantar telemedisin<br>*Introduction* | 25–38 | Definisi, sejarah, layanan, dan peran internet serta sensor dalam telemedisin. | Telemedisin | Komunikasi Data Medis, Pengantar Teknologi Kedokteran |
| 2 | Jaringan dan layanan komunikasi<br>*Communication Networks and Services* | 39–60 | Sinyal, kanal radio, modulasi, pemancar-penerima, dan jaringan kabel maupun nirkabel. | Telemedisin | Komunikasi Data Medis, Pengantar Sistem Internet of Things |
| 3 | Teknologi nirkabel untuk pemantauan pasien<br>*Wireless Technology in Patient Monitoring* | 61–90 | Body area network, sensor yang dikenakan, pemantauan di rumah sakit dan rumah, serta keandalan tautan. | Patient Monitor, Smartwatch, Holter | Sistem Monitoring Elektronik Kesehatan, Pengantar Sistem Internet of Things, Komunikasi Data Medis |
| 4 | Pengolahan informasi medis<br>*Technologies in Medical Information Processing* | 91–130 | Pengukuran tanda vital, citra medis, kompresi, dan pengolahan data jantung serta darah. | EKG, NIBP, RME | Pengolahan Sinyal Biomedik, Pengolahan Citra Medis, Manajemen Data |
| 5 | Menerapkan sistem telemedisin nirkabel<br>*Wireless Telemedicine System Deployment* | 131–160 | Perencanaan jaringan, lapisan protokol, akses kanal, kapasitas, dan kualitas layanan. | Telemedisin | Komunikasi Data Medis, Pengantar Sistem Internet of Things |
| 6 | Keamanan dan privasi data medis<br>*Technologies for Safeguarding Medical Data and Privacy* | 161–194 | Enkripsi, autentikasi, watermark citra, dan kebijakan privasi informasi kesehatan. | RME, Telemedisin | Komunikasi Data Medis, Manajemen Data, Sistem Informasi Manajemen Rumah Sakit |
| 7 | TI dalam pengobatan alternatif<br>*Information Technology in Alternative Medicine* | 195–218 | Sensor tubuh, latihan, dan basis data pengobatan tradisional. |  | Pengantar Sistem Internet of Things, Ilmu Data Medis |
| 8 | Perawatan komunitas dan telecare<br>*Caring for the Community* | 219–252 | Telecare untuk lansia, alarm darurat, dan layanan kesehatan berbasis komunitas. | Telemedisin, Dispenser Obat | Sistem Monitoring Elektronik Kesehatan, Teknologi dalam Bidang Keperawatan |
| 9 | Tren masa depan<br>*Future Trends in Healthcare Technology* | 253–284 | Rumah pintar, jaringan nirkabel generasi baru, dan sistem kesehatan terhubung. | Smartwatch, Telemedisin | Pengantar Sistem Internet of Things, Big Data dalam Kesehatan |

## Precision Medicine, CRISPR, and Genome Engineering (AEMB 1016)

Stephen H. Tsang (ed.) · Springer · 2017 · 181 halaman · `Referensi\10_Precision Medicine, CRISPR, and Genome Engineering.pdf`

Rekayasa genom untuk kedokteran presisi: vektor virus, AAV dengan nuklease, CRISPR dalam biologi perkembangan, fasilitas hewan transgenik, zebrafish, tanaman, skrining CRISPR untuk target obat, retina, dan masa depan serta etikanya. Konteks untuk Studi Lanjutan dan Biologi Kedokteran.

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Vektor virus, sel rekayasa, dan revolusi CRISPR<br>*Viral Vectors, Engineered Cells and the CRISPR Revolution* | 10–34 | Adenovirus, lentivirus, dan AAV sebagai kurir gen; terapi gen dan sel CAR-T; bagaimana CRISPR-Cas mempercepat penyuntingan. |  | Biologi Kedokteran |
| 2 | Nuklease rekayasa + vektor AAV<br>*Combining Engineered Nucleases with Adeno-associated Viral Vectors* | 35–49 | Mengantar CRISPR, TALEN, dan ZFN ke jaringan in vivo dengan AAV: kapasitas muatan dan target jaringan. |  | Biologi Kedokteran |
| 3 | Dari reduksionisme ke holisme<br>*From Reductionism to Holism: CRISPR in Developmental Biology* | 50–79 | dCas untuk mengatur ekspresi gen, epigenetik, sel punca, dan skrining genom luas. |  | Biologi Kedokteran, Big Data dalam Kesehatan |
| 4 | Pengalaman fasilitas hewan transgenik<br>*A Transgenic Core Facility's Experience in Genome Editing* | 80–95 | Merancang sgRNA, injeksi zigot mencit, dan mengukur keberhasilan penyuntingan. |  | Biologi Kedokteran, Metode Penelitian Teknologi Kedokteran |
| 5 | Zebrafish untuk mempelajari kalsium di fotoreseptor<br>*Genome Editing to Study Ca2+ Homeostasis in Zebrafish Cone Photoreceptors* | 96–105 | Mutasi pada mitokondria dan kalsium sel kerucut retina zebrafish. |  | Biologi Kedokteran, Fisiologi Kedokteran |
| 6 | CRISPR: dari imun bakteri ke tanaman<br>*CRISPR: From Prokaryotic Immune Systems to Plant Genome Editing* | 106–126 | Asal-usul CRISPR sebagai sistem imun bakteri dan penerapannya pada padi dan tanaman lain. |  | Biologi Kedokteran |
| 7 | Skrining CRISPR untuk target obat<br>*Target Discovery for Precision Medicine Using High-Throughput Genome Engineering* | 127–149 | Skrining pustaka sgRNA menemukan gen resistansi obat kanker dan target terapi baru; analisis data skala besar. |  | Big Data dalam Kesehatan, Ilmu Data Medis, Biologi Kedokteran |
| 8 | CRISPR di retina<br>*CRISPR in the Retina* | 150–158 | Retinitis pigmentosa, model sel punca pasien, dan peluang terapi gen mata. |  | Biologi Kedokteran |
| 9 | Masa depan CRISPR dan etikanya<br>*The Future of CRISPR Applications* | 159–181 | Penyuntingan germline, regulasi, persepsi publik, dan pertimbangan etika. |  | Biologi Kedokteran, Metode Penelitian Teknologi Kedokteran |

## Robotic Surgery: Smart Materials, Robotic Structures, and Artificial Muscles

Mohsen Shahinpoor, Soheil Gheshmi · Pan Stanford / CRC Press · 2015 · 206 halaman · `Referensi\11_Robotic surgery.pdf`

Robot bedah dari sisi rekayasa: sejarah dan konfigurasi (termasuk da Vinci), kinematika dan ruang kerja dengan transformasi homogen, robot bedah mata, robot laparoskopi yang bisa dilipat, serta material pintar IPMC untuk umpan balik gaya. Pegangan untuk mata kuliah Robotika.

Alat: Robot Bedah, Fako, Endoskop, Prostesis Tangan

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Pengantar robot bedah<br>*Introduction to Surgical Robots* | 17–48 | Sejarah robot bedah dari PUMA, ROBODOC, sampai da Vinci; konfigurasi master-slave dan manfaat bedah minimal invasif. | Robot Bedah | Robotika untuk Kedokteran, Teknologi dalam Ilmu Kedokteran Bedah |
| 2 | Kinematika dan ruang kerja robot bedah<br>*Surgical Robots' Kinematics and Workspace* | 49–88 | Sistem koordinat, matriks rotasi, transformasi homogen, kinematika maju dan balik, serta ruang kerja manipulator. | Robot Bedah | Robotika untuk Kedokteran, Sistem Kendali, Matematika Teknik |
| 3 | Robot bedah intraokular<br>*Intraocular Robotic Surgical System* | 89–126 | Rancangan robot untuk operasi katarak (fakoemulsifikasi) dengan ketelitian di bawah milimeter. | Robot Bedah, Fako | Robotika untuk Kedokteran, Teknologi dalam Ilmu Kedokteran Bedah, Desain Teknologi Berbantu Komputer untuk Medis |
| 4 | Robot laparoskopi yang bisa dilipat<br>*Deployable Laparoscopic Robotic Surgical System* | 127–166 | Struktur lengan yang dilipat saat masuk dan dibuka di dalam perut, dikendalikan dari konsol. | Robot Bedah, Endoskop | Robotika untuk Kedokteran, Desain Teknologi Berbantu Komputer untuk Medis, Purwarupa Cepat Untuk Alat Kesehatan |
| 5 | Material pintar dan otot buatan (IPMC)<br>*Applications of Smart Materials in Robotic Surgery* | 167–182 | Ionic polymer-metal composite melengkung bila diberi tegangan dan menghasilkan tegangan bila dibengkokkan; dipakai untuk sensor dan umpan balik gaya. | Robot Bedah, Prostesis Tangan | Biomaterial, Sensor dan Transduser Biomedis, Robotika untuk Kedokteran |
| 6 | Ringkasan dan lampiran perhitungan<br>*Summary and Conclusions* | 183–206 | Rangkuman, arah riset, dan lampiran turunan kinematika. | Robot Bedah | Robotika untuk Kedokteran |

## Multidetector-Row CT Angiography (Medical Radiology)

Carlo Catalano, Roberto Passariello (ed.) · Springer · 2005 · 213 halaman · `Referensi\12_Row CT Angiography Medical Radiology Diagnostic Imaging.pdf`

CT angiografi multidetektor dari prinsip teknis sampai penerapan per pembuluh darah: pitch, dosis, ECG gating, rekonstruksi (MPR, MIP, volume rendering), pemberian kontras, dan CTA otak, karotis, aorta, paru, koroner, hati, ginjal, perifer, dan vena.

Alat: CT Scan, Infusion Pump, USG, EKG, Kateter-Stent

| Bab | Judul | Hal. | Ringkasan | Alat | Mata kuliah |
|---|---|---|---|---|---|
| 1 | Evolusi CT angiografi<br>*MDCT Angiography: Evolution* | 5–12 | Dari CT spiral satu baris ke multidetektor dan bagaimana CTA menggantikan angiografi kateter diagnostik. | CT Scan | Teknologi Pencitraan Medis |
| 2 | Prinsip teknis MDCT<br>*MDCT: Technical Principles* | 13–25 | Lebar detektor, pitch, waktu rotasi, rekonstruksi, ECG gating, dan dosis radiasi. | CT Scan | Teknologi Pencitraan Medis, Fisika Radiasi dan Proteksi Radiasi |
| 3 | Pengolahan citra MDCT<br>*MDCT: Image Processing* | 26–41 | Multiplanar reformatting, MIP, surface dan volume rendering, serta endoskopi virtual. | CT Scan | Pengolahan Citra Medis, Visualisasi Data Medis, Desain Teknologi Berbantu Komputer untuk Medis |
| 4 | Pemberian media kontras<br>*Contrast Medium Administration* | 42–55 | Kecepatan injeksi, dosis iodin, waktu tunda, bolus tracking, dan puncak penyangatan arteri. | CT Scan, Infusion Pump | Teknologi Pencitraan Medis, Fisiologi Kedokteran |
| 5 | CTA pembuluh intrakranial<br>*CTA of Intracranial Circulation* | 56–60 | Teknik pemeriksaan aneurisma dan pembuluh otak. | CT Scan | Teknologi Pencitraan Medis, Anatomi |
| 6 | Arteri karotis<br>*Carotid Arteries* | 61–86 | Stenosis, plak, risiko stroke, dan perbandingan dengan USG Doppler dan MRA. | CT Scan, USG | Teknologi Pencitraan Medis, Anatomi |
| 7 | Aorta torakalis<br>*Thoracic Aorta* | 87–101 | Diseksi, aneurisma, cangkok aorta, dan gating jantung. | CT Scan | Teknologi Pencitraan Medis |
| 8 | Sirkulasi paru dan emboli paru<br>*Pulmonary Circulation* | 102–123 | CTA sebagai pemeriksaan utama emboli paru. | CT Scan | Teknologi Pencitraan Medis, Teknologi dalam Ilmu Kedokteran Medik |
| 9 | Arteri koroner<br>*Coronary Arteries* | 124–135 | Stenosis koroner, sinkronisasi EKG, dan resolusi waktu. | CT Scan, EKG | Teknologi Pencitraan Medis, Fisiologi Kedokteran |
| 10 | Aorta abdominalis<br>*Abdominal Aorta* | 136–153 | Aneurisma aorta perut dan evaluasi sebelum dan sesudah stent graft. | CT Scan, Kateter-Stent | Teknologi Pencitraan Medis, Teknologi dalam Ilmu Kedokteran Bedah |
| 11 | Pembuluh hati<br>*Hepatic Vessels* | 154–165 | Fase arteri dan portal untuk perencanaan bedah dan transplantasi hati. | CT Scan | Teknologi Pencitraan Medis, Anatomi |
| 12 | Pembuluh splanknik<br>*Splanchnic Vessels* | 166–174 | Arteri dan vena mesenterika pada iskemia usus. | CT Scan | Teknologi Pencitraan Medis |
| 13 | Arteri renalis<br>*Renal Arteries* | 175–184 | Stenosis arteri ginjal dan hipertensi renovaskular. | CT Scan | Teknologi Pencitraan Medis |
| 14 | Arteri perifer<br>*Peripheral Arteries* | 185–196 | Penyakit arteri tungkai dan teknik pemindaian panjang. | CT Scan | Teknologi Pencitraan Medis |
| 15 | Evaluasi vena 3D<br>*Three-Dimensional Evaluation of the Venous System* | 197–213 | CT venografi untuk trombosis dan varises. | CT Scan | Teknologi Pencitraan Medis, Visualisasi Data Medis |
