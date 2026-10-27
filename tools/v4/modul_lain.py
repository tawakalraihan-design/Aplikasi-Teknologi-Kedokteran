"""Modul mata kuliah pelengkap (versi awal aplikasi) dan mata kuliah silabus
semester 6–7 yang belum punya file kuliah. Isinya lebih ringkas."""
from dsl import M, T, K, pg, kasus, bs, cocok, urut, isian, hitung, multi, kategori, celah

# ================================================================ PELENGKAP
M("anfis",
  "Anatomi dan Fisiologi Manusia adalah gabungan struktur (anatomi) dan fungsi (fisiologi). Mata kuliah pelengkap ini dipertahankan dari versi awal aplikasi; materi rincinya kini ada di "
  "mata kuliah Anatomi (semester 1) dan Fisiologi Kedokteran (semester 2). Pakai halaman ini sebagai ringkasan cepat sistem organ yang paling sering bertemu alat medis.",
  topik=[
    T("Sistem kardiovaskular", "Jantung, pembuluh, dan darah.", ["Empat ruang dan sistem konduksi", "Tekanan darah dan curah jantung", "Hemoglobin pengangkut O₂"]),
    T("Sistem respirasi dan saraf", "Pertukaran gas dan sinyal listrik.", ["Ventilasi dan difusi alveolus", "Neuron, potensial aksi, EEG", "Otot dan EMG"]),
    T("Sistem ginjal dan metabolisme", "Penyaringan dan pengaturan suhu.", ["Nefron dan GFR", "Keseimbangan cairan dan elektrolit", "Termoregulasi"]),
  ],
  kasus=[
    K("ekg", "Struktur dan fungsi jantung pada EKG", "Irama dan konduksi jantung.", ["Anatomi jantung dan sistem konduksi", "Arti gelombang P-QRS-T"],
      "Lihat modul Anatomi dan Fisiologi untuk studi kasus lengkap.", ["elektroda", "prosesor"]),
    K("inkubator", "Termoregulasi bayi", "Suhu bayi prematur.", ["Bayi kehilangan panas lewat konduksi, konveksi, radiasi, evaporasi", "Lapisan lemak tipis pada prematur"],
      "Inkubator menjaga lingkungan netral termal agar bayi tidak membakar energi untuk menghangatkan diri.", ["pemanas", "sensor"]),
  ],
  soal=[
    multi("Pilih semua cara bayi kehilangan panas.", ["Konduksi", "Konveksi", "Radiasi", "Evaporasi", "Fotosintesis"], [0, 1, 2, 3], "Inkubator mengurangi keempatnya.", "inkubator"),
    pg("Organ yang menyaring darah dan menghasilkan urin adalah…", ["Ginjal", "Hati", "Limpa", "Pankreas"], "Ginjal berisi sekitar satu juta nefron per sisi.", "hemodialisis"),
    bs("Potensial aksi saraf diawali masuknya ion Na⁺ ke dalam sel.", True, "Depolarisasi oleh Na⁺, repolarisasi oleh K⁺ keluar."),
  ])

M("fisdas",
  "Fisika Dasar adalah mata kuliah pelengkap yang merangkum mekanika, gelombang, optik, dan listrik. Rinciannya kini ada di Fisika Mekanika (S1) dan Fisika Listrik dan Magnet (S2). "
  "Bagian gelombang dan optik yang tidak dibahas di dua mata kuliah itu dirangkum di sini karena penting untuk USG, mikroskop, dan sinar-X.",
  topik=[
    T("Gelombang mekanik", "Gelombang memindahkan energi tanpa memindahkan materi.", ["v = f·λ", "Pemantulan, pembiasan, interferensi", "Efek Doppler"]),
    T("Optik", "Cahaya dibiaskan lensa untuk membentuk bayangan.", ["Hukum Snell n₁ sin θ₁ = n₂ sin θ₂", "Lensa cembung dan perbesaran", "Difraksi membatasi daya pisah"]),
    T("Gelombang elektromagnetik", "Spektrum dari radio sampai sinar gamma.", ["Energi foton E = h·f", "Sinar-X dan gamma bersifat pengion", "Cahaya tampak 400–700 nm"]),
  ],
  kasus=[
    K("usg", "Gelombang suara dalam jaringan", "Citra organ dari gema.", ["v = f·λ dengan v ≈ 1540 m/s", "Pemantulan di batas jaringan", "Efek Doppler untuk aliran darah"],
      "Pada 5 MHz, panjang gelombang di jaringan sekitar 0,3 mm; inilah batas kasar detail yang bisa dibedakan.", ["transduser"]),
    K("mikroskop", "Lensa dan perbesaran", "Sel dan mikroorganisme.", ["Lensa objektif dan okuler", "Hukum Snell dan minyak imersi", "Difraksi dan daya pisah"],
      "Minyak imersi mencegah cahaya terbias keluar di antara kaca dan lensa, sehingga apertur numerik naik.", ["objektif"]),
  ],
  soal=[
    hitung("Gelombang ultrasonik 5 MHz merambat 1540 m/s di jaringan. Berapa panjang gelombangnya (mm)?", 0.308, "λ = v/f = 1540/5×10⁶ = 0,308 mm.", tol=0.003, satuan="mm", alat="usg"),
    kategori("Kelompokkan gelombang berikut.", ["Gelombang mekanik", "Gelombang elektromagnetik"],
             [("Ultrasonik USG", 0), ("Suara", 0), ("Sinar-X", 1), ("Cahaya LED oksimeter", 1), ("Gelombang radio MRI", 1)], "Gelombang mekanik butuh medium."),
    bs("Energi foton makin besar bila frekuensinya makin tinggi.", True, "E = h·f; sinar-X berenergi tinggi sehingga bersifat pengion."),
  ])

M("matek",
  "Matematika Teknik (pelengkap) memuat alat matematika lanjutan: matriks, persamaan diferensial, bilangan kompleks, deret dan transformasi Fourier, serta transformasi Laplace. "
  "Alat-alat ini dipakai untuk rekonstruksi citra CT/MRI dan analisis filter.",
  topik=[
    T("Matriks dan sistem linear", "Banyak persamaan diselesaikan sekaligus.", ["Rekonstruksi CT dapat ditulis sebagai A·x = b", "Determinan dan invers", "Nilai eigen untuk PCA"], 1),
    T("Bilangan kompleks dan Fourier", "Sinyal dipecah menjadi sinus-kosinus.", ["e^(jωt) = cos ωt + j sin ωt", "Deret dan transformasi Fourier", "Data MRI mentah ada di ruang-k (domain Fourier)"]),
    T("Persamaan diferensial dan Laplace", "Model sistem dinamis.", ["Rangkaian RC sebagai PD orde satu", "Transformasi Laplace dan fungsi alih", "Kestabilan sistem kendali"]),
  ],
  kasus=[
    K("mri", "Ruang-k dan transformasi Fourier", "Citra MRI dari data frekuensi.", ["Transformasi Fourier 2D", "Ruang-k pusat = kontras, tepi = detail", "Invers FFT"],
      "Scanner MRI mengisi ruang-k baris demi baris; citra didapat dengan invers FFT 2D.", ["akuisisi", "rekonstruksi"]),
    K("ct", "Sistem linear rekonstruksi", "Peta atenuasi per piksel.", ["Persamaan A·x = b", "Metode iteratif (ART)", "Backprojection"],
      "Rekonstruksi iteratif menebak citra, menghitung proyeksinya, membandingkan dengan data, lalu memperbaiki tebakan.", ["rekonstruksi"]),
  ],
  soal=[
    pg("Data mentah MRI disimpan dalam domain…", ["Frekuensi (ruang-k)", "Waktu saja", "Hounsfield", "Desibel"], "Citra diperoleh dengan invers transformasi Fourier.", "mri"),
    hitung("Hitung determinan matriks [[2, 1], [3, 4]].", 5, "2×4 − 1×3 = 5.", tol=0),
    bs("Rangkaian RC dapat dimodelkan sebagai persamaan diferensial orde satu.", True, "RC dVc/dt + Vc = Vin."),
  ])

M("rangkaian",
  "Rangkaian Listrik (pelengkap) memperdalam analisis rangkaian DC dan AC: metode mesh dan node, teorema Thevenin-Norton, fasor, impedansi, daya AC, dan respons frekuensi. "
  "Materi intinya sudah ada di Pengantar Elektronika Medis (S1) dan Fisika Listrik dan Magnet (S2).",
  topik=[
    T("Analisis mesh dan node", "Metode sistematis untuk rangkaian besar.", ["Mesh: KVL per loop", "Node: KCL per simpul", "Rangkaian jembatan Wheatstone untuk sensor regangan"], 41),
    T("Fasor dan impedansi", "Rangkaian AC dianalisis dengan bilangan kompleks.", ["Z_R = R, Z_L = jωL, Z_C = 1/(jωC)", "Daya aktif, reaktif, dan faktor daya"], 43),
    T("Respons frekuensi", "Penguatan rangkaian sebagai fungsi frekuensi.", ["Plot Bode", "Frekuensi cut-off −3 dB", "Filter orde satu dan dua"], 43),
  ],
  kasus=[
    K("ekg", "Impedansi elektroda-kulit", "Kualitas kontak elektroda.", ["Model RC kulit-elektroda", "Impedansi input penguat harus jauh lebih besar", "Ketidakseimbangan impedansi merusak CMRR"],
      "Kulit kering bisa berimpedansi ratusan kΩ; karena itu penguat EKG butuh impedansi input di atas 10 MΩ.", ["elektroda", "penguat"]),
    K("defibrilator", "Rangkaian RLC pembentuk gelombang", "Bentuk pulsa kejut.", ["Pelepasan kapasitor lewat induktor dan beban dada", "Redaman kritis dan kurang redam"],
      "Gelombang monofasik klasik (Lown) adalah respons RLC teredam; defibrilator modern memakai gelombang bifasik.", ["saklar"]),
  ],
  soal=[
    hitung("Jembatan Wheatstone seimbang dengan R1 = 1 kΩ, R2 = 2 kΩ, R3 = 1,5 kΩ. Berapa R4 (kΩ) jika R1/R2 = R3/R4?", 3, "R4 = R3·R2/R1 = 1,5 × 2 / 1 = 3 kΩ.", tol=0, satuan="kΩ"),
    pg("Impedansi kapasitor makin … bila frekuensi naik.", ["Kecil", "Besar", "Tetap", "Negatif tak hingga"], "Z_C = 1/(jωC)."),
    bs("Pada frekuensi cut-off, penguatan filter turun 3 dB dari penguatan pita lolos.", True, "−3 dB ≈ 70,7% amplitudo."),
  ])

M("elda",
  "Elektronika Analog (pelengkap) membahas penguat transistor dan op-amp secara mendalam, filter aktif, osilator, dan catu daya. Blok-blok ini adalah inti front-end analog alat biomedis.",
  topik=[
    T("Penguat op-amp", "Konfigurasi dasar dan penguat instrumentasi.", ["Inverting, non-inverting, diferensial, buffer", "Penguat instrumentasi 3 op-amp: G = 1 + 2R/Rg", "CMRR dan offset"], 43),
    T("Filter aktif", "Filter dengan op-amp tanpa induktor.", ["Sallen–Key dan multiple feedback", "Butterworth (datar) dan Chebyshev (curam)", "Notch twin-T untuk 50 Hz"], 43),
    T("Isolasi dan catu daya", "Keselamatan pasien di sisi analog.", ["Penguat isolasi dan optocoupler", "Konverter DC-DC terisolasi", "Regulator linear vs switching"]),
  ],
  kasus=[
    K("ekg", "Front-end analog EKG", "Sinyal jantung yang bersih dan aman.", ["Penguat instrumentasi", "Filter aktif band-pass", "Notch 50 Hz", "Isolasi pasien"],
      "Rantai klasik: IA gain 10 → HPF 0,5 Hz → gain 100 → LPF 150 Hz → isolasi → ADC.", ["penguat", "filter", "isolasi"]),
    K("oksimeter", "Penguat transimpedansi dan pemisah AC/DC", "Sinyal PPG kecil di atas komponen DC besar.", ["TIA", "HPF untuk komponen AC", "Penguat tahap kedua"],
      "Komponen AC PPG hanya sekitar 1% dari DC, jadi DC dipisahkan dulu sebelum AC dikuatkan.", ["tia"]),
  ],
  soal=[
    hitung("Penguat instrumentasi dengan R = 24,7 kΩ dan Rg = 1 kΩ. Berapa gain-nya? (G = 1 + 2R/Rg)", 50.4, "G = 1 + 49,4 = 50,4.", tol=0.1, alat="ekg"),
    pg("Filter dengan respons paling datar di pita lolos adalah…", ["Butterworth", "Chebyshev", "Elliptic", "Notch"], "Chebyshev lebih curam tetapi ber-riak."),
    bs("Penguat isolasi memutus jalur arus langsung antara pasien dan catu daya jala-jala.", True, "Isolasi galvanik dengan trafo, optik, atau kapasitif.", "ekg"),
  ])

M("fluida",
  "Mekanika Fluida dan Termodinamika (pelengkap) membahas aliran viskos, hukum Poiseuille, bilangan Reynolds, perpindahan panas, dan hukum termodinamika. Penting untuk pompa infus, "
  "ventilator, hemodialisis, dan inkubator.",
  topik=[
    T("Aliran viskos", "Fluida nyata punya viskositas.", ["Hukum Poiseuille: Q = πr⁴ΔP/(8ηL)", "Aliran sangat peka jari-jari (pangkat empat)", "Bilangan Reynolds: laminar < 2000, turbulen > 4000"], 26),
    T("Perpindahan panas", "Konduksi, konveksi, radiasi.", ["Q = m·c·ΔT", "Hukum pendinginan Newton", "Kelembapan dan penguapan"]),
    T("Termodinamika", "Energi dan entropi.", ["Hukum I: ΔU = Q − W", "Gas ideal PV = nRT", "Hukum II: efisiensi mesin panas"]),
  ],
  kasus=[
    K("infus", "Hukum Poiseuille pada selang infus", "Laju aliran yang berubah karena ukuran kanula.", ["Q ∝ r⁴", "Viskositas cairan (darah vs salin)", "Panjang selang"],
      "Kanula 18G mengalirkan jauh lebih cepat daripada 22G karena jari-jari dipangkatkan empat; ini alasan transfusi cepat memakai kanula besar.", ["peristaltik"]),
    K("inkubator", "Perpindahan panas di inkubator", "Suhu dan kelembapan bayi.", ["Konveksi udara hangat", "Evaporasi dari kulit", "Kelembapan untuk mengurangi kehilangan air"],
      "Menaikkan kelembapan mengurangi kehilangan panas lewat penguapan pada bayi prematur.", ["pemanas", "humidifier"]),
  ],
  soal=[
    hitung("Jari-jari pembuluh mengecil setengahnya. Menurut Poiseuille, aliran menjadi berapa kali semula?", 0.0625, "(1/2)⁴ = 1/16 = 0,0625.", tol=0.001, satuan="×"),
    pg("Aliran dengan bilangan Reynolds 500 termasuk…", ["Laminar", "Turbulen", "Transisi", "Supersonik"], "Re < 2000 laminar."),
    bs("Menaikkan kelembapan inkubator mengurangi kehilangan panas bayi lewat evaporasi.", True, "Udara lembap memperlambat penguapan dari kulit.", "inkubator"),
  ])

M("fismed",
  "Fisika Medis (pelengkap) membahas fisika yang terjadi di dalam tubuh dan interaksi energi dengan jaringan: biolistrik, bioakustik, optik jaringan, radiasi, dan efek panas.",
  topik=[
    T("Biolistrik", "Tubuh adalah sumber dan penghantar listrik.", ["Dipol jantung dan segitiga Einthoven", "Konduktivitas jaringan", "Bahaya arus: makroshock dan mikroshock"], 39),
    T("Interaksi energi dengan jaringan", "Setiap energi punya efek biologis.", ["Ultrasonik: panas dan kavitasi", "RF/mikrowave: pemanasan dielektrik", "Cahaya: absorpsi dan hamburan (jendela optik 650–950 nm)"]),
    T("Radiasi dan dosis", "Ukuran dosis radiasi.", ["Gray (Gy) = J/kg; sievert (Sv) memperhitungkan bobot", "Efek deterministik dan stokastik"]),
  ],
  kasus=[
    K("ekg", "Dipol jantung dan segitiga Einthoven", "Sumbu listrik jantung.", ["Sadapan I, II, III", "Hukum Einthoven II = I + III", "Vektor rata-rata QRS"],
      "Sumbu jantung normal −30° sampai +90°; deviasi sumbu menunjukkan hipertrofi atau gangguan konduksi.", ["elektroda"]),
    K("oksimeter", "Jendela optik jaringan", "Cahaya yang menembus jari.", ["Absorpsi air dan hemoglobin", "Jendela 650–950 nm", "Hukum Beer–Lambert"],
      "Merah 660 nm dan IR 940 nm dipilih karena berada di jendela optik dan perbedaan serapan HbO₂/Hb besar.", ["led", "fotodioda"]),
  ],
  soal=[
    celah("Hukum Einthoven menyatakan tegangan sadapan II sama dengan sadapan [[0]] ditambah sadapan [[1]].", ["I", "III"], ["aVR", "V1"], "II = I + III.", "ekg"),
    pg("Satuan dosis serap radiasi adalah…", ["Gray (Gy)", "Sievert (Sv)", "Becquerel (Bq)", "Tesla (T)"], "Gy = J/kg; Sv untuk dosis ekuivalen/efektif."),
    bs("Arus mikroshock sekecil puluhan mikroampere bisa berbahaya bila langsung mengenai jantung lewat kateter.", True, "Batas arus bocor tipe CF 10 µA kondisi normal.", "ekg"),
  ])

M("sensor",
  "Sensor dan Transduser Biomedis (pelengkap) membahas sensor yang mengubah besaran tubuh menjadi sinyal listrik: elektroda biopotensial, sensor suhu, tekanan, aliran, optik, kimia, "
  "dan piezoelektrik. Kini sebagian dibahas di IoT (S3) dan Sistem Tertanam (S4).",
  topik=[
    T("Elektroda biopotensial", "Antarmuka ion di tubuh dan elektron di kabel.", ["Ag/AgCl dengan gel: potensial setengah sel rendah dan stabil", "Elektroda kering dan kapasitif", "Impedansi kulit-elektroda"]),
    T("Sensor fisik", "Suhu, tekanan, aliran, gerak.", ["Termistor NTC, RTD, termokopel, IR (MLX90614)", "Sensor tekanan piezoresistif (jembatan)", "Akselerometer MEMS"]),
    T("Sensor optik, kimia, akustik", "Cahaya, ion, dan gelombang.", ["Fotodioda dan fototransistor", "ISE dan biosensor enzim", "Piezoelektrik untuk USG"]),
  ],
  kasus=[
    K("tensimeter", "Sensor tekanan piezoresistif", "Tekanan manset.", ["Jembatan Wheatstone", "Penguatan sinyal mV", "Kalibrasi"],
      "MPS20N0040D menghasilkan beberapa mV; HX710/HX711 menguatkan dan mendigitalkannya.", ["sensor", "pengondisi"]),
    K("termometer", "Sensor suhu", "Suhu tubuh.", ["Termistor NTC dan persamaan Steinhart–Hart", "Termometer IR dan emisivitas kulit", "Waktu respons"],
      "Termometer dahi IR cepat, tetapi dipengaruhi keringat dan suhu ruang; termistor ketiak lambat tetapi stabil.", ["sensor"]),
  ],
  soal=[
    pg("Elektroda Ag/AgCl dipilih untuk EKG karena…", ["Potensial setengah selnya stabil dan derau rendah", "Paling murah", "Tidak perlu kontak kulit", "Menyimpan muatan"], "Ag/AgCl tidak terpolarisasi.", "ekg"),
    kategori("Kelompokkan sensor berikut.", ["Sensor suhu", "Sensor tekanan", "Sensor optik"],
             [("Termistor NTC", 0), ("MLX90614", 0), ("MPS20N0040D", 1), ("Fotodioda", 2), ("MAX30102", 2)], "Pilih sensor sesuai besaran."),
    bs("Resistansi termistor NTC turun saat suhu naik.", True, "NTC = negative temperature coefficient.", "termometer"),
  ])

M("mikro",
  "Mikrokontroler dan Sistem Tertanam (pelengkap) membahas arsitektur mikrokontroler, pemrograman firmware, interrupt, timer, ADC, PWM, dan komunikasi serial. Materinya kini tersebar di "
  "Elektronika Digital (S2), IoT (S3), dan Sistem Tertanam (S4).",
  topik=[
    T("Arsitektur dan periferal", "CPU, memori, dan periferal dalam satu chip.", ["Flash, SRAM, EEPROM", "GPIO, timer, ADC, PWM", "Interrupt dan prioritas"], 67),
    T("Firmware", "Program yang berjalan di mikrokontroler.", ["Loop utama dan interrupt service routine", "Mesin keadaan (state machine)", "Debounce tombol"], 68),
    T("Komunikasi serial", "Bertukar data dengan sensor dan komputer.", ["UART, I²C, SPI", "Alamat I²C dan pull-up", "Baud rate"], 70),
  ],
  kasus=[
    K("infus", "Kendali motor stepper", "Laju infus.", ["Timer untuk pulsa langkah", "Konversi mL/jam ke langkah per detik", "State machine alarm"],
      "Satu putaran rotor peristaltik mendorong volume tertentu; firmware menghitung interval langkah dari laju yang diminta.", ["motor", "kontrol"]),
    K("oksimeter", "Membaca sensor I²C", "Data PPG dari MAX30102.", ["Alamat I²C 0x57", "Register FIFO", "Laju sampling"],
      "MAX30102 menyimpan sampel di FIFO; mikrokontroler membacanya lewat I²C secara berkala.", ["adc", "algoritma"]),
  ],
  soal=[
    cocok("Cocokkan protokol dengan jumlah kabel data utamanya.", [("UART", "TX dan RX"), ("I²C", "SDA dan SCL"), ("SPI", "MOSI, MISO, SCK, CS")], "I²C butuh resistor pull-up."),
    pg("Fungsi yang dijalankan otomatis saat ada kejadian perangkat keras disebut…", ["Interrupt service routine", "Bootloader", "Compiler", "Watchdog"], "ISR harus singkat."),
    bs("Debounce diperlukan karena kontak tombol mekanis bergetar beberapa milidetik saat ditekan.", True, "Tanpa debounce satu tekanan terbaca berkali-kali."),
  ])

M("instrumen",
  "Instrumentasi Biomedis (pelengkap) merangkai semua blok menjadi alat ukur utuh: sensor, pengondisi sinyal, isolasi, ADC, pengolahan, tampilan, serta spesifikasi akurasi dan keselamatan.",
  topik=[
    T("Rantai pengukuran", "Dari besaran tubuh ke angka di layar.", ["Sensor → penguat → filter → isolasi → ADC → prosesor → tampilan", "Karakteristik statis dan dinamis", "Sumber galat dan derau"]),
    T("Spesifikasi alat", "Angka yang menentukan mutu alat.", ["Akurasi, presisi, resolusi, rentang", "Bandwidth dan waktu respons", "Essential performance menurut IEC 60601"]),
  ],
  kasus=[
    K("ekg", "Merancang rantai akuisisi EKG", "Gelombang EKG diagnostik.", ["Spesifikasi bandwidth 0,05–150 Hz", "CMRR > 90 dB", "Isolasi tipe CF"],
      "Standar IEC 60601-2-25 menetapkan bandwidth dan akurasi EKG diagnostik.", ["penguat", "isolasi", "adc"]),
    K("glukometer", "Rantai pengukuran elektrokimia", "Glukosa darah.", ["Potensiostat", "TIA", "Kalibrasi kode strip"],
      "Arus mikroampere dari strip dikuatkan TIA, didigitalkan, lalu dikonversi ke mg/dL dengan kurva kalibrasi.", ["potensiostat", "adc"]),
  ],
  soal=[
    urut("Urutkan rantai instrumentasi biomedis.", ["Sensor", "Penguat", "Filter", "Isolasi", "ADC", "Prosesor", "Tampilan"], "Urutan umum front-end ke back-end."),
    pg("Standar khusus keselamatan dan kinerja EKG diagnostik adalah…", ["IEC 60601-2-25", "ISO 9001", "IEC 62304", "ISO 13485"], "Seri 60601-2-x adalah standar khusus per jenis alat.", "ekg"),
    bs("Resolusi tinggi selalu berarti akurasi tinggi.", False, "Alat bisa menampilkan dua desimal tetapi tetap salah kalibrasi."),
  ])

M("sinyal",
  "Pengolahan Sinyal Biomedik membahas cara menganalisis sinyal tubuh: asal dan karakteristik biopotensial, filter digital, analisis domain frekuensi (FFT), dan analisis waktu-frekuensi "
  "(STFT, wavelet). Mata kuliah silabus semester 5 ini belum punya file di folder kuliahmu, jadi modulnya disusun dari silabus dan referensi standar.",
  topik=[
    T("Karakteristik sinyal biopotensial", "Setiap sinyal punya amplitudo dan pita frekuensi khas.",
      ["EKG 0,5–5 mV, 0,05–150 Hz", "EEG 10–100 µV, 0,5–70 Hz", "EMG 0,1–5 mV, 20–500 Hz"], 115),
    T("Filter digital", "Filter diterapkan pada sampel angka.",
      ["FIR: selalu stabil, fase linear", "IIR: lebih efisien, bisa tidak stabil", "Moving average sebagai LPF sederhana"], [116, 119]),
    T("Domain frekuensi", "FFT memecah sinyal menjadi komponen frekuensi.",
      ["Resolusi frekuensi Δf = fs/N", "Spektrum daya dan metode Welch", "Aliasing bila fs < 2fmax"], [117, 120]),
    T("Waktu-frekuensi dan deteksi QRS", "Sinyal yang berubah memerlukan analisis lokal.",
      ["STFT dengan jendela", "Wavelet untuk transien", "Pan–Tompkins: band-pass → turunan → kuadrat → integrasi jendela → ambang adaptif"], [118, 121]),
  ],
  kasus=[
    K("ekg", "Algoritma Pan–Tompkins", "Lokasi kompleks QRS untuk detak jantung.", ["Band-pass 5–15 Hz", "Turunan dan kuadrat", "Integrasi jendela 150 ms", "Ambang adaptif"],
      "Pan–Tompkins menonjolkan QRS yang curam dan berenergi tinggi, lalu ambang adaptif menyesuaikan dengan amplitudo pasien.", ["filter", "prosesor"]),
    K("eeg", "Analisis spektral EEG", "Daya delta, theta, alpha, beta.", ["FFT/Welch", "Integrasi daya per pita", "Artefak 50 Hz"],
      "Daya alpha meningkat saat mata tertutup; ini uji cepat apakah rekaman EEG berfungsi.", ["filter", "komputer"]),
    K("emg", "RMS dan frekuensi median EMG", "Kekuatan dan kelelahan otot.", ["RMS jendela geser", "Spektrum dan frekuensi median", "Filter 20–450 Hz"],
      "Frekuensi median EMG bergeser turun selama kontraksi lama, penanda kelelahan otot.", ["filter", "analisis"]),
  ],
  soal=[
    hitung("Sinyal disampling 500 Hz dan dianalisis dengan FFT 1000 titik. Berapa resolusi frekuensinya (Hz)?", 0.5, "Δf = fs/N = 500/1000 = 0,5 Hz.", tol=0, satuan="Hz"),
    urut("Urutkan tahap algoritma Pan–Tompkins.", ["Band-pass filter", "Turunan", "Kuadrat", "Integrasi jendela", "Ambang adaptif"], "Urutan klasik 1985.", "ekg"),
    kategori("Kelompokkan sifat berikut.", ["Filter FIR", "Filter IIR"],
             [("Selalu stabil", 0), ("Fase bisa linear", 0), ("Butuh orde lebih kecil untuk respons curam", 1), ("Ada umpan balik keluaran", 1)], "Pilihan bergantung kebutuhan fase dan komputasi."),
    pg("Bila sinyal 300 Hz disampling 400 Hz, akan terjadi…", ["Aliasing", "Penguatan", "Kompresi lossless", "Notch"], "fs harus ≥ 2 × 300 = 600 Hz."),
    bs("Wavelet lebih cocok daripada FFT untuk menganalisis kejadian singkat yang muncul sesekali.", True, "Wavelet memberi resolusi waktu dan frekuensi sekaligus."),
  ])

M("radiasi",
  "Fisika Radiasi dan Proteksi Radiasi (pelengkap) membahas produksi sinar-X, interaksi radiasi dengan materi (fotolistrik, Compton), atenuasi, dosimetri, dan proteksi radiasi.",
  topik=[
    T("Produksi sinar-X", "Elektron cepat menumbuk anoda.", ["Bremsstrahlung (spektrum kontinu) dan karakteristik", "kVp menentukan energi maksimum", "Efisiensi tabung sekitar 1%, sisanya panas"]),
    T("Interaksi dan atenuasi", "Foton diserap atau dihamburkan.", ["Fotolistrik dominan di energi rendah (kontras tinggi)", "Compton dominan di energi diagnostik tinggi", "I = I₀·e^(−μx), HVL"]),
    T("Proteksi radiasi", "Dosis sekecil mungkin.", ["Waktu, jarak, perisai (ALARA)", "Nilai batas dosis pekerja 20 mSv/tahun rata-rata", "Dosimeter TLD/film badge"]),
  ],
  kasus=[
    K("xray", "Pemilihan kV dan filter", "Kontras dan dosis rontgen.", ["kV dan mAs", "Filter aluminium membuang foton lunak", "Kolimasi mengurangi hamburan"],
      "Filter aluminium menyerap foton berenergi rendah yang tidak sampai detektor tetapi menambah dosis kulit.", ["tabung", "kolimator"]),
    K("ct", "Dosis CT", "Dosis pasien per pemeriksaan.", ["CTDI dan DLP", "Modulasi arus tabung otomatis", "Protokol anak"],
      "CT kepala sekitar 2 mSv, CT abdomen sekitar 8 mSv; protokol anak menurunkan mAs.", ["tabung"]),
  ],
  soal=[
    hitung("HVL timbal untuk suatu energi adalah 0,25 mm. Berapa tebal (mm) untuk mengurangi intensitas menjadi 1/4?", 0.5, "Dua HVL: 2 × 0,25 = 0,5 mm.", tol=0, satuan="mm", alat="xray"),
    cocok("Cocokkan prinsip ALARA dengan contohnya.", [("Waktu", "Fluoroskopi berdenyut, bukan kontinu"), ("Jarak", "Mundur saat eksposi"), ("Perisai", "Apron timbal dan dinding berlapis Pb")], "Tiga prinsip proteksi eksternal."),
    bs("Efek Compton menghasilkan radiasi hambur yang mengurangi kontras citra.", True, "Grid anti-hambur dipakai untuk menguranginya.", "xray"),
  ])

M("k3",
  "Keselamatan Listrik Medis dan K3 (pelengkap) membahas bahaya listrik pada pasien dan petugas, klasifikasi alat menurut IEC 60601-1, arus bocor, pembumian, serta K3 di rumah sakit.",
  topik=[
    T("Bahaya arus listrik", "Efek arus pada tubuh bergantung besarnya dan jalurnya.", ["Makroshock lewat kulit: 1 mA terasa, 10–20 mA tidak bisa melepas, 100 mA fibrilasi", "Mikroshock langsung ke jantung: puluhan µA berbahaya"]),
    T("Klasifikasi IEC 60601-1", "Kelas proteksi dan tipe bagian terapan.", ["Kelas I (pembumian), kelas II (isolasi ganda), catu internal", "Tipe B, BF, CF (CF untuk kontak jantung)", "Batas arus bocor pasien tipe CF 10 µA kondisi normal"]),
    T("K3 rumah sakit", "Keselamatan petugas dan lingkungan.", ["Pengujian keselamatan listrik berkala", "Bahaya radiasi, kimia, biologi", "Prosedur lockout/tagout saat perawatan alat"]),
  ],
  kasus=[
    K("defibrilator", "Bagian terapan tahan defibrilasi", "Keselamatan pasien dan alat lain saat kejut.", ["Simbol defibrillation-proof", "Proteksi input monitor", "Keselamatan penolong"],
      "Monitor EKG harus tahan kejut defibrilator yang mengenai elektrodanya tanpa rusak atau membahayakan.", ["elektroda"]),
    K("mri", "Keselamatan di lingkungan MRI", "Bahaya proyektil, pemanasan RF, dan bising.", ["Zona I–IV", "Label MR Safe/Conditional/Unsafe", "SAR"],
      "Kabel EKG biasa dapat membentuk loop dan memanas akibat RF; MRI memakai monitor khusus MR Conditional.", ["rf"]),
  ],
  soal=[
    kategori("Kelompokkan tipe bagian terapan.", ["Tipe B", "Tipe BF", "Tipe CF"],
             [("Meja periksa", 0), ("Elektroda EKG permukaan", 1), ("Kateter intrakardiak", 2)], "CF paling ketat karena kontak jantung langsung."),
    pg("Arus sekitar 100 mA yang melewati dada dapat menyebabkan…", ["Fibrilasi ventrikel", "Hanya kesemutan", "Tidak ada efek", "Hipotermia"], "Makroshock berbahaya pada rentang ini."),
    bs("Alat kelas II tidak memerlukan kabel pembumian karena memakai isolasi ganda.", True, "Simbol kotak ganda."),
  ])

M("kendali",
  "Sistem Kendali (pelengkap) membahas kendali loop terbuka dan tertutup, fungsi alih, kestabilan, dan pengendali PID. Banyak alat terapi dan life support memakai loop tertutup.",
  topik=[
    T("Loop terbuka dan tertutup", "Umpan balik membuat sistem tahan gangguan.", ["Sensor → pembanding → pengendali → aktuator → plant", "Galat = setpoint − terukur"]),
    T("Pengendali PID", "Tiga suku pengendali.", ["P: sebanding galat", "I: menghapus galat tunak", "D: meredam lonjakan"]),
    T("Kestabilan", "Sistem tidak boleh berosilasi liar.", ["Overshoot dan settling time", "Margin fase dan margin gain", "Tuning Ziegler–Nichols"]),
  ],
  kasus=[
    K("inkubator", "Kendali suhu inkubator", "Suhu udara atau kulit bayi yang stabil.", ["PID pemanas", "Mode suhu udara vs suhu kulit", "Batas overshoot"],
      "Overshoot suhu berbahaya untuk bayi, sehingga pengendali disetel lambat tetapi stabil.", ["pemanas", "sensor", "kontrol"]),
    K("ventilator", "Kendali tekanan dan aliran", "Volume dan tekanan napas sesuai setelan.", ["Loop cepat katup/turbin", "Mode volume vs tekanan", "Alarm bila galat besar"],
      "Mode tekanan terkendali menjaga tekanan tetap; volume mengikuti komplians paru.", ["aktuator", "sensor", "kontrol"]),
  ],
  soal=[
    cocok("Cocokkan suku PID dengan fungsinya.", [("P", "Respons sebanding galat saat ini"), ("I", "Menghapus galat tunak"), ("D", "Meredam perubahan cepat")], "Ketiganya dijumlahkan."),
    pg("Inkubator yang memakai sensor suhu untuk mengatur pemanas termasuk sistem…", ["Loop tertutup", "Loop terbuka", "Tanpa kendali", "Manual"], "Ada umpan balik dari sensor.", "inkubator"),
    bs("Menaikkan gain P terlalu besar dapat membuat sistem berosilasi.", True, "Gain besar mengurangi margin kestabilan."),
  ])

M("citra",
  "Pengolahan Citra Medis (pelengkap) membahas representasi citra digital, enhancement, filtering, segmentasi, registrasi, dan rekonstruksi. Banyak bagiannya kini ada di sub-materi "
  "Teknologi Pencitraan Medis (S3).",
  topik=[
    T("Representasi dan enhancement", "Citra adalah matriks angka.", ["Bit depth dan rentang dinamis", "Windowing CT (level dan width)", "Histogram equalization"], [126, 128]),
    T("Filtering dan segmentasi", "Membersihkan derau dan memisahkan objek.", ["Median untuk derau garam-merica", "Deteksi tepi Sobel/Canny", "Thresholding Otsu, region growing"], [124, 125]),
    T("Registrasi dan rekonstruksi", "Menyelaraskan dan membangun citra.", ["Registrasi rigid dan non-rigid", "Filtered backprojection", "Rekonstruksi iteratif"], [124, 130]),
  ],
  kasus=[
    K("ct", "Windowing CT", "Organ berbeda dari satu data.", ["Window otak (L40/W80)", "Window paru (L−600/W1500)", "Window tulang (L400/W1800)"],
      "Satu data CT ditampilkan dengan beberapa window agar otak, paru, dan tulang masing-masing terlihat jelas.", ["tampilan"]),
    K("motion-correction", "Registrasi citra", "Gerak antar-frame.", ["Transformasi rigid 6 parameter", "Fungsi biaya", "Interpolasi"],
      "Koreksi gerak adalah registrasi tiap frame ke frame referensi.", ["estimasi", "resampling"]),
  ],
  soal=[
    pg("Filter terbaik untuk derau garam-merica adalah…", ["Median", "Mean", "High-pass", "Notch"], "Median membuang piksel ekstrem tanpa mengaburkan tepi."),
    hitung("Window CT level 40 width 80. Berapa batas atas HU yang masih tampil putih penuh?", 80, "Rentang = L ± W/2 = 0 sampai 80 HU.", tol=0, satuan="HU", alat="ct"),
    bs("Thresholding Otsu memilih ambang secara otomatis dari histogram.", True, "Otsu meminimalkan varians dalam kelas."),
  ])

M("biomaterial",
  "Biomaterial (pelengkap) membahas material yang berkontak dengan tubuh: logam, polimer, keramik, dan komposit, beserta biokompatibilitas, degradasi, dan sterilisasi.",
  topik=[
    T("Jenis biomaterial", "Setiap kelas material punya kelebihan.", ["Logam: titanium, stainless 316L, CoCr", "Polimer: UHMWPE, PEEK, silikon, PMMA", "Keramik: alumina, hidroksiapatit"]),
    T("Biokompatibilitas", "Material tidak boleh memicu reaksi berbahaya.", ["ISO 10993 uji biologis", "Sitotoksisitas, sensitisasi, iritasi", "Stress shielding pada implan yang terlalu kaku"]),
    T("Membran dan material terapi", "Material fungsional.", ["Membran dialiser polisulfon", "Hidrogel elektroda", "Material cetak 3D untuk ortosis (PLA, PETG, TPU, nilon)"]),
  ],
  kasus=[
    K("hemodialisis", "Membran dialiser", "Ureum dan kreatinin yang dibuang.", ["Pori membran dan berat molekul", "Biokompatibilitas darah", "Sterilisasi"],
      "Membran high-flux polisulfon membuang molekul tengah seperti β2-mikroglobulin lebih baik dari membran lama.", ["dialiser"]),
    K("brace-skoliosis", "Material brace", "Kekakuan dan kenyamanan brace.", ["Modulus elastisitas", "Ketebalan dan ventilasi", "Material lunak di bantalan"],
      "Brace butuh kombinasi material kaku (PE/PETG) untuk gaya korektif dan busa lunak di bantalan.", ["fabrikasi", "bantalan"]),
  ],
  soal=[
    pg("Standar uji biokompatibilitas alat kesehatan adalah…", ["ISO 10993", "ISO 9001", "IEC 60601-1", "ISO 15197"], "ISO 10993 mengatur uji biologis."),
    kategori("Kelompokkan biomaterial.", ["Logam", "Polimer", "Keramik"], [("Titanium", 0), ("Stainless 316L", 0), ("PEEK", 1), ("Silikon", 1), ("Hidroksiapatit", 2)], "Tiga kelas utama."),
    bs("Implan yang jauh lebih kaku dari tulang dapat menyebabkan stress shielding.", True, "Tulang sekitar menerima beban lebih kecil lalu menipis."),
  ])

M("kalibrasi",
  "Kalibrasi dan Manajemen Alat Kesehatan (pelengkap) membahas kalibrasi alat ukur, ketertelusuran, pemeliharaan preventif dan korektif, serta manajemen siklus hidup alat di rumah sakit.",
  topik=[
    T("Kalibrasi dan ketertelusuran", "Membandingkan alat dengan standar yang lebih teliti.", ["Rantai ketertelusuran ke standar nasional/SI", "Ketidakpastian pengukuran", "Sertifikat kalibrasi dan label"]),
    T("Pemeliharaan alat", "Alat dijaga agar tetap aman dan akurat.", ["Preventive maintenance terjadwal", "Corrective maintenance saat rusak", "Uji keselamatan listrik"]),
    T("Manajemen siklus hidup", "Dari perencanaan sampai penghapusan.", ["Perencanaan, pengadaan, instalasi, pelatihan, pemeliharaan, penghapusan", "Inventaris dan riwayat alat", "Peran instalasi pemeliharaan sarana (IPSRS) dan elektromedis"]),
  ],
  kasus=[
    K("tensimeter", "Kalibrasi tensimeter digital", "Akurasi tekanan darah.", ["Pembanding manometer standar", "Titik uji 0, 50, 100, 150, 200, 250 mmHg", "Toleransi ±3 mmHg"],
      "Tensimeter disambungkan paralel dengan manometer standar; tekanan dinaikkan bertahap dan selisihnya dicatat.", ["sensor", "manset"]),
    K("defibrilator", "Uji energi defibrilator", "Energi yang benar-benar dilepas.", ["Defibrillator analyzer dengan beban 50 Ω", "Toleransi energi ±15%", "Waktu pengisian"],
      "Energi yang dipilih 200 J harus terukur sekitar 170–230 J pada analyzer.", ["kapasitor"]),
  ],
  soal=[
    urut("Urutkan siklus hidup alat kesehatan.", ["Perencanaan", "Pengadaan", "Instalasi dan uji fungsi", "Pemakaian dan pemeliharaan", "Penghapusan"], "Manajemen alat mencakup seluruh siklus."),
    hitung("Defibrilator disetel 200 J. Toleransi ±15%. Berapa energi minimum yang masih lolos (J)?", 170, "200 × 0,85 = 170 J.", tol=0, satuan="J", alat="defibrilator"),
    bs("Kalibrasi berarti memperbaiki alat yang rusak.", False, "Kalibrasi membandingkan dengan standar dan mencatat penyimpangan; perbaikan adalah pemeliharaan korektif."),
  ])

# ================================================================ SEMESTER 6–7
M("metopen",
  "Metode Penelitian Teknologi Kedokteran membekali cara merancang dan menulis penelitian: metode ilmiah, jenis penelitian, kebaruan, plagiarisme, sampai menulis pendahuluan, dasar teori, "
  "metodologi, hasil, dan daftar pustaka, serta analisis dan visualisasi data.",
  topik=[
    T("Metode ilmiah dan jenis penelitian", "Penelitian dimulai dari pertanyaan yang bisa diuji.", ["Observasi → hipotesis → eksperimen → analisis → kesimpulan", "Eksperimental, observasional, rekayasa (design and build)", "Kebaruan (novelty)"], [245, 246, 247, 248]),
    T("Menulis penelitian", "Struktur tugas akhir.", ["Pendahuluan, dasar teori, metodologi, hasil, kesimpulan", "Daftar pustaka dengan pengelola referensi", "Plagiarisme dan cara menghindarinya"], [249, 252, 253, 254, 255, 256]),
    T("Analisis dan visualisasi data", "Menyajikan hasil secara jujur.", ["Uji statistik yang sesuai", "Grafik yang menjawab pertanyaan penelitian"], 257),
  ],
  kasus=[
    K("ekg", "Penelitian validasi prototipe", "Akurasi alat buatan sendiri.", ["Desain eksperimen", "Alat pembanding standar", "Analisis Bland–Altman"],
      "Penelitian rekayasa yang kuat membandingkan prototipe dengan alat standar pada subjek dan kondisi yang dicatat rinci.", ["tampilan"]),
  ],
  soal=[
    urut("Urutkan langkah metode ilmiah.", ["Observasi", "Rumusan masalah", "Hipotesis", "Eksperimen", "Analisis", "Kesimpulan"], "Siklus metode ilmiah."),
    pg("Unsur yang membedakan penelitian dari pekerjaan rutin adalah…", ["Kebaruan (novelty)", "Panjang laporan", "Jumlah halaman", "Warna sampul"], "Penelitian harus menambah pengetahuan."),
    bs("Hipotesis harus dapat diuji dan mungkin dibuktikan salah.", True, "Prinsip falsifiabilitas."),
  ])

M("data-mining",
  "Penggalian Data Medis membahas teknik menemukan pola dari data besar: data warehousing dan preprocessing, clustering, klasifikasi, penanganan nilai hilang, association rule, dan sequential pattern.",
  topik=[
    T("Persiapan data", "Data warehouse dan preprocessing.", ["Integrasi data dari SIMRS, LIS, PACS", "Penanganan nilai hilang: hapus, imputasi rata-rata, model", "Transformasi dan diskretisasi"], [258, 261]),
    T("Clustering dan klasifikasi", "Menemukan kelompok dan memprediksi kelas.", ["K-means, hierarchical", "Decision tree, Naive Bayes, SVM", "Validasi silang"], [259, 260]),
    T("Association dan sequential pattern", "Hubungan antar-item dan urutan waktu.", ["Support, confidence, lift (algoritma Apriori)", "Pola urutan diagnosis atau resep"], [262, 263]),
  ],
  kasus=[
    K("kimia-klinik", "Pola hasil laboratorium", "Kombinasi hasil lab yang sering muncul bersama.", ["Association rule", "Support dan confidence", "Interpretasi klinis"],
      "Aturan 'HbA1c tinggi → kreatinin tinggi' dengan confidence tinggi dapat memicu skrining ginjal pada pasien diabetes.", ["lis"]),
  ],
  soal=[
    cocok("Cocokkan ukuran association rule.", [("Support", "Seberapa sering item muncul bersama"), ("Confidence", "Peluang B muncul bila A muncul"), ("Lift", "Seberapa kuat dibanding kebetulan")], "Apriori memakai ambang support dan confidence."),
    pg("Teknik mengisi nilai yang hilang dengan rata-rata kolom disebut…", ["Imputasi", "Normalisasi", "Diskretisasi", "Agregasi"], "Imputasi sederhana; ada juga imputasi berbasis model."),
    bs("Lift lebih besar dari 1 berarti item A dan B muncul bersama lebih sering daripada kebetulan.", True, "Lift = 1 berarti independen."),
  ])

M("big-data",
  "Big Data dalam Kesehatan membahas pengelolaan dan analisis data kesehatan berskala besar: karakteristik big data, platform terdistribusi, data genomik dan citra, analitik populasi, serta tata kelola dan privasi. "
  "Mata kuliah ini belum punya sub-materi di silabus aplikasi, sehingga modulnya disusun dari topik umum.",
  topik=[
    T("Karakteristik big data kesehatan", "Data tumbuh lebih cepat dari kemampuan mengolahnya.", ["Volume, velocity, variety, veracity, value", "Sumber: RME, wearable, genomik, citra, klaim asuransi"]),
    T("Platform dan arsitektur", "Data diproses terdistribusi.", ["Data lake dan data warehouse", "Hadoop/Spark untuk pemrosesan paralel", "Cloud dan komputasi edge"]),
    T("Analitik dan tata kelola", "Dari data ke kebijakan.", ["Analitik deskriptif, prediktif, preskriptif", "Kesehatan populasi dan surveilans", "Privasi, anonimisasi, UU PDP"]),
  ],
  kasus=[
    K("smartwatch", "Data wearable skala populasi", "Pola aktivitas dan detak jantung jutaan pengguna.", ["Velocity data streaming", "Kualitas dan bias data", "Anonimisasi"],
      "Data detak istirahat dari jutaan jam pintar pernah dipakai untuk mendeteksi lonjakan flu di tingkat wilayah.", ["aplikasi"]),
    K("rme", "Analitik data rekam medis nasional", "Tren penyakit dan efektivitas layanan.", ["Integrasi lintas fasilitas", "Standar data", "Privasi"],
      "Data SATUSEHAT yang terintegrasi memungkinkan pemantauan penyakit tidak menular per wilayah.", ["integrasi"]),
  ],
  soal=[
    multi("Pilih semua sumber big data kesehatan.", ["Rekam medis elektronik", "Wearable", "Data genomik", "Citra medis", "Ramalan cuaca"], [0, 1, 2, 3], "Cuaca bisa dipakai sebagai data pendukung, tetapi bukan sumber data kesehatan."),
    cocok("Cocokkan jenis analitik.", [("Deskriptif", "Apa yang terjadi"), ("Prediktif", "Apa yang akan terjadi"), ("Preskriptif", "Apa yang sebaiknya dilakukan")], "Tingkat kematangan analitik."),
    bs("Anonimisasi data menghapus atau menyamarkan identitas agar pasien tidak dapat dikenali.", True, "Langkah penting sebelum data dibagi untuk riset."),
  ])

M("uav",
  "Pemrograman Unmanned Aerial Vehicle membahas sistem drone: komponen, pemanfaatan (termasuk pengiriman logistik kesehatan), pemrograman dasar, kontrol dan navigasi, keamanan, komunikasi, dan interaksi manusia-UAV.",
  topik=[
    T("Sistem UAV", "Komponen drone.", ["Flight controller, ESC, motor, baling-baling, baterai LiPo", "IMU dan GPS untuk stabilisasi", "Telemetri dan remote control"], [265, 266]),
    T("Pemrograman dan navigasi", "Drone diprogram untuk misi otomatis.", ["Waypoint mission", "PID untuk sikap (roll, pitch, yaw)", "Protokol MAVLink"], [267, 268, 270]),
    T("Keamanan dan interaksi", "Terbang aman di sekitar manusia.", ["Geofence dan return-to-home", "Regulasi penerbangan", "Antarmuka operator"], [269, 271]),
  ],
  kasus=[
    K("defibrilator", "Drone pengantar AED", "Henti jantung di luar rumah sakit.", ["Waktu tempuh vs ambulans", "Navigasi GPS", "Pendaratan aman"],
      "Uji coba di beberapa negara menunjukkan drone bisa mengantar AED lebih cepat dari ambulans ke lokasi terpencil.", ["elektroda"]),
  ],
  soal=[
    pg("Sensor yang membantu drone menjaga kestabilan sikap adalah…", ["IMU (akselerometer + giroskop)", "Termometer", "Fotodioda", "Mikrofon"], "IMU memberi data orientasi ke flight controller."),
    bs("Geofence mencegah drone terbang keluar dari area yang ditentukan.", True, "Fitur keselamatan penting."),
    isian("Protokol komunikasi yang umum dipakai antara ground station dan flight controller adalah …", ["MAVLink"], "MAVLink dipakai ArduPilot dan PX4."),
  ])

M("tatalaksana",
  "Tatalaksana Klinis dan Rintisan Bisnis Digital membahas peran insinyur klinis di rumah sakit (clinical engineering), instrumentasi medis, risiko klinis, keselamatan dan privasi pasien, "
  "serta perencanaan dan manajemen proyek rekayasa, termasuk merintis bisnis teknologi kesehatan.",
  topik=[
    T("Clinical engineering", "Insinyur yang mengelola teknologi di rumah sakit.", ["Manajemen alat, pelatihan pengguna, investigasi insiden", "Evaluasi pengadaan berbasis kebutuhan klinis"], [272, 273]),
    T("Risiko klinis dan keselamatan pasien", "Mencegah cedera akibat alat.", ["Manajemen risiko ISO 14971", "Pelaporan insiden dan analisis akar masalah", "Privasi pasien"], [274, 275]),
    T("Proyek dan bisnis digital", "Dari ide ke produk.", ["Perencanaan proyek: lingkup, jadwal, biaya", "Model bisnis dan validasi pasar", "Regulasi produk"], 276),
  ],
  kasus=[
    K("infus", "Investigasi insiden pompa infus", "Kelebihan dosis obat.", ["Analisis akar masalah", "Faktor manusia dan desain antarmuka", "Tindakan korektif"],
      "Banyak insiden pompa infus berasal dari salah ketik laju; pustaka obat dan batas dosis adalah solusi rekayasa.", ["antarmuka"]),
    K("defibrilator", "Manajemen risiko alat kegawatdaruratan", "Kesiapan defibrilator.", ["ISO 14971", "Jadwal uji", "Pelatihan"],
      "Risiko utama defibrilator bukan rusak saat dipakai, melainkan baterai habis atau pad kedaluwarsa; cek harian menurunkan risiko itu.", ["pengisi"]),
  ],
  soal=[
    pg("Standar manajemen risiko alat kesehatan adalah…", ["ISO 14971", "ISO 10993", "IEC 62304", "ISO 15197"], "ISO 14971: identifikasi, evaluasi, pengendalian risiko."),
    urut("Urutkan langkah manajemen risiko.", ["Identifikasi bahaya", "Estimasi risiko", "Evaluasi risiko", "Pengendalian risiko", "Pemantauan pasca-pasar"], "Siklus ISO 14971."),
    bs("Analisis akar masalah bertujuan mencari siapa yang harus disalahkan.", False, "Tujuannya menemukan penyebab sistemik agar tidak terulang."),
  ])

M("simrs",
  "Sistem Informasi Manajemen Rumah Sakit membahas perangkat lunak yang mengelola alur layanan rumah sakit: pendaftaran, rekam medis, farmasi, laboratorium, radiologi, billing, dan pelaporan, "
  "serta integrasi dengan BPJS dan SATUSEHAT. Silabus aplikasi belum memuat sub-materinya, sehingga modul ini disusun dari topik umum.",
  topik=[
    T("Modul SIMRS", "Setiap unit punya modul.", ["Pendaftaran dan rawat jalan/inap", "Farmasi, laboratorium (LIS), radiologi (RIS/PACS)", "Billing dan klaim BPJS"]),
    T("Integrasi dan standar", "SIMRS harus bicara dengan sistem lain.", ["HL7 v2 dan FHIR", "DICOM untuk citra", "Bridging BPJS dan SATUSEHAT"]),
    T("Keamanan dan keberlanjutan", "Sistem harus andal 24 jam.", ["Hak akses dan audit", "Cadangan dan pemulihan bencana", "Pelatihan pengguna"]),
  ],
  kasus=[
    K("rme", "RME sebagai inti SIMRS", "Data pasien yang terpusat.", ["Alur data antar-modul", "Standar FHIR", "Hak akses"],
      "Hasil lab dari LIS dan citra dari PACS masuk ke RME pasien sehingga dokter melihat semuanya di satu layar.", ["integrasi", "database"]),
    K("ct", "PACS dan RIS untuk radiologi", "Citra dan laporan radiologi.", ["DICOM", "Worklist modalitas", "Arsip citra"],
      "RIS mengirim worklist ke CT, CT mengirim citra DICOM ke PACS, dan laporan radiolog kembali ke SIMRS.", ["tampilan"]),
  ],
  soal=[
    cocok("Cocokkan sistem dengan fungsinya.", [("LIS", "Sistem informasi laboratorium"), ("PACS", "Arsip dan komunikasi citra"), ("RIS", "Sistem informasi radiologi")], "Ketiganya terhubung ke SIMRS."),
    pg("Standar untuk mengirim citra medis antar-sistem adalah…", ["DICOM", "HTML", "MP3", "CSV"], "DICOM menyimpan citra dan metadata pasien.", "ct"),
    bs("SIMRS yang baik membutuhkan cadangan data dan rencana pemulihan bencana.", True, "Layanan rumah sakit berjalan 24 jam."),
  ])

M("monitoring",
  "Sistem Monitoring Elektronik Kesehatan membahas sistem yang memantau pasien secara terus-menerus, dari monitor samping ranjang dan central station sampai pemantauan jarak jauh di rumah. "
  "Silabus aplikasi belum memuat sub-materinya, sehingga modul ini disusun dari topik umum.",
  topik=[
    T("Monitor pasien multiparameter", "Satu monitor membaca banyak tanda vital.", ["EKG, SpO₂, NIBP, suhu, laju napas, EtCO₂", "Tren dan alarm", "Early warning score"]),
    T("Central station dan telemetri", "Banyak monitor terhubung.", ["Jaringan rumah sakit", "Telemetri pasien rawat jalan di bangsal", "Integrasi ke RME"]),
    T("Pemantauan jarak jauh", "Pasien kronis dipantau dari rumah.", ["Tensimeter dan glukometer terhubung", "Wearable dan patch", "Ambang eskalasi ke tenaga kesehatan"]),
  ],
  kasus=[
    K("patient-monitor", "Early warning score otomatis", "Pasien yang memburuk sebelum henti jantung.", ["Skor dari detak, napas, tekanan, SpO₂, suhu, kesadaran", "Ambang eskalasi", "Integrasi ke perawat"],
      "Monitor menjumlahkan skor tiap parameter; skor tinggi memanggil tim respons cepat.", ["prosesor", "tampilan"]),
    K("holter", "Pemantauan ritme jangka panjang", "Aritmia yang jarang.", ["Rekaman kontinu", "Analisis otomatis", "Laporan ringkas"],
      "Holter dan patch EKG memperluas pemantauan dari rumah sakit ke kehidupan sehari-hari pasien.", ["analisis"]),
  ],
  soal=[
    multi("Pilih semua parameter yang umum di monitor pasien.", ["EKG", "SpO₂", "Tekanan darah non-invasif", "Suhu", "Kadar kolesterol"], [0, 1, 2, 3], "Kolesterol diperiksa di laboratorium.", "patient-monitor"),
    pg("Sistem penilaian yang menjumlahkan skor tanda vital untuk mendeteksi perburukan disebut…", ["Early warning score", "Skor Apgar", "Indeks massa tubuh", "Glasgow Coma Scale"], "Contoh: NEWS2.", "patient-monitor"),
    bs("Monitor pasien tetap harus membunyikan alarm lokal walaupun koneksi ke central station terputus.", True, "Alarm lokal adalah lapisan keselamatan terakhir.", "patient-monitor"),
  ])

M("robotika",
  "Robotika untuk Kedokteran membahas konsep rekayasa robot, robot prostetik, bedah minimal invasif, dan interaksi manusia-mesin.",
  topik=[
    T("Dasar robotika", "Robot terdiri dari mekanik, sensor, aktuator, dan kendali.", ["Derajat kebebasan (DOF)", "Kinematika maju dan balik", "Aktuator: motor DC, servo, stepper, pneumatik"], 279),
    T("Robot prostetik", "Prostesis aktif digerakkan sinyal tubuh.", ["Kendali mioelektrik dari EMG", "Umpan balik sensorik", "Desain ringan dan hemat daya"], 280),
    T("Bedah minimal invasif dan HMI", "Robot membantu dokter.", ["Teleoperasi dan remote center of motion", "Penskalaan gerak dan penyaring tremor", "Haptik dan ergonomi konsol"], [281, 282]),
  ],
  kasus=[
    K("robot-bedah", "Robot bedah minimal invasif", "Operasi lewat sayatan kecil.", ["Remote center of motion di titik trokar", "Instrumen 7 DOF", "Penyaring tremor"],
      "Lengan robot berputar mengelilingi titik masuk trokar agar dinding perut tidak robek saat instrumen bergerak.", ["lengan", "instrumen", "kontrol"]),
    K("prostesis-tangan", "Prostesis mioelektrik", "Gerak tangan dari kontraksi otot sisa.", ["Sinyal EMG", "Klasifikasi pola gerak", "Aktuator servo"],
      "Elektroda EMG di lengan bawah membaca kontraksi; kontroler menerjemahkannya menjadi buka/tutup tangan.", ["kontrol", "aktuasi"]),
    K("emg", "EMG sebagai antarmuka manusia-mesin", "Niat gerak pengguna.", ["Amplitudo dan pola EMG", "Ambang dan klasifikasi", "Latensi"],
      "Latensi kendali di bawah 300 ms agar prostesis terasa responsif.", ["analisis"]),
  ],
  soal=[
    pg("Kendali prostesis yang memakai sinyal listrik otot disebut…", ["Mioelektrik", "Pneumatik", "Hidraulik", "Optik"], "Sinyal EMG dari otot sisa.", "prostesis-tangan"),
    isian("Jumlah gerakan independen sebuah robot disebut derajat …", ["kebebasan", "kebebasan (DOF)", "DOF"], "DOF = degrees of freedom."),
    bs("Robot bedah teleoperasi bergerak sendiri tanpa kendali dokter.", False, "Dokter mengendalikan dari konsol.", "robot-bedah"),
  ])
