"""Proyek hands-on untuk alat baru v1.3 (format defaultdata/proyek.json).

Harga bahan adalah perkiraan harga marketplace Indonesia 2026 (Rupiah).
Alat yang berbahaya bila dirakit sendiri (sinar-X, RF bedah, gas anestesi,
radioaktif) diberi proyek simulasi perangkat lunak, bukan perangkat keras.
"""

R = {
    "webster": "Webster, Medical Instrumentation: Application and Design, ed. 5 (Wiley): https://search.worldcat.org/oclc/1131895650",
    "venturi": "Arduino Venturi Flow Meter (Maker Portal): https://makersportal.com/blog/2020/7/24/arduino-venturi-flow-meter",
    "spiro2019": "Graham dkk. (2019), Standardization of Spirometry 2019 Update, ATS/ERS: https://pmc.ncbi.nlm.nih.gov/articles/PMC6794117",
    "scd30": "Adafruit SCD-30, sensor CO₂ NDIR: https://learn.adafruit.com/adafruit-scd30",
    "radon": "scikit-image, transformasi Radon dan filtered back projection: https://scikit-image.org/docs/0.25.x/auto_examples/transform/plot_radon_transform.html",
    "proteksi": "Radiation protection of patients (ringkasan): https://en.wikipedia.org/wiki/Radiation_protection_of_patients",
    "fhir": "HL7 FHIR, standar pertukaran data kesehatan: https://hl7.org/fhir/",
    "webrtc": "WebRTC samples (getUserMedia, RTCPeerConnection): https://webrtc.github.io/samples/",
    "permenkes24": "Permenkes No. 24 Tahun 2022 tentang Rekam Medis: https://peraturan.bpk.go.id/Details/245544",
    "max30102": "MAX30102 + ESP32 (Microcontrollers Lab): https://microcontrollerslab.com/esp32-heart-rate-pulse-oximeter-max30102/",
    "bangle": "Bangle.js, jam tangan pintar open source (Hackster): https://hackster.io/news/the-bangle-js-an-open-sourced-javascript-powered-smart-watch-6359962646c2",
    "dvrk": "da Vinci Research Kit (dVRK), perangkat riset robot bedah open source: https://github.com/jhu-dvrk",
    "rtc": "DS3231 Real Time Clock + Arduino (HowToMechatronics): https://howtomechatronics.com/tutorials/arduino/arduino-ds3231-real-time-clock-tutorial/",
    "mqtt": "ESP32 MQTT publish-subscribe (Random Nerd Tutorials): https://randomnerdtutorials.com/esp32-mqtt-publish-subscribe-arduino-ide/",
    "microsd": "ESP32 dan modul microSD (Random Nerd Tutorials): https://randomnerdtutorials.com/esp32-microsd-card-arduino/",
    "ad8232": "SparkFun AD8232 Heart Rate Monitor Hookup Guide: https://learn.sparkfun.com/tutorials/ad8232-heart-rate-monitor-hookup-guide/all",
    "mitdb": "MIT-BIH Arrhythmia Database (PhysioNet): https://physionet.org/content/mitdb/1.0.0/",
    "emgdb": "Examples of Electromyograms (PhysioNet): https://physionet.org/content/emgdb/",
    "bioamp_emg": "Upside Down Labs, visualisasi EMG 2 kanal: https://www.hackster.io/upsidedownlabs/visualizing-2-channel-emg-on-lcd-display-module-d094cf",
    "muscleshield": "DIY Muscle BioAmp Shield (GitHub): https://github.com/upsidedownlabs/DIY-Muscle-BioAmp-Shield",
    "openmha": "Open Master Hearing Aid (openMHA), platform riset alat bantu dengar: https://doaj.org/article/e189d4dbe0ca427b8d66faa5b412d873",
    "loizou": "Loizou, Cochlear Implants tutorial (UT Dallas): https://ecs.utdallas.edu/loizou/cimplants/tutorial/tutorial.htm",
    "kvasir": "Kvasir, dataset citra endoskopi saluran cerna (Simula): https://datasets.simula.no/kvasir",
    "ctgdb": "Chudáček dkk. (2014), Open access intrapartum CTG database, BMC Pregnancy and Childbirth: https://pmc.ncbi.nlm.nih.gov/articles/PMC3898997",
    "enable": "e-NABLE, komunitas tangan prostetik cetak 3D: https://en.wikipedia.org/wiki/E-NABLE",
    "max6675": "Termokopel tipe K dengan MAX6675 + Arduino (Random Nerd Tutorials): https://randomnerdtutorials.com/arduino-k-type-thermocouple-max6675",
    "aap": "AAP, panduan hiperbilirubinemia neonatus: https://www.aap.org/en/patient-care/hyperbilirubinemia/",
    "vam": "Virtual Anesthesia Machine (University of Florida): https://simulation.health.ufl.edu/education-training/virtual-anesthesia-machine/",
    "iec60601": "Panduan ringkas IEC 60601-1: https://meddeviceguide.com/blog/iec-60601-1-medical-electrical-equipment-safety-guide",
}

PROYEK = []


def P(alat, tahap, blok, judul, level, durasi, bidang, materi, tujuan, bahan, langkah, hasil, keselamatan, ref):
    PROYEK.append({
        "id": "%s-%d" % (alat, tahap), "alat": alat, "tahap": tahap, "blok": list(blok), "judul": judul,
        "level": level, "durasi": durasi, "bidang": list(bidang), "materi": list(materi), "tujuan": tujuan,
        "bahan": [list(b) for b in bahan], "langkah": list(langkah), "hasil": hasil, "keselamatan": keselamatan,
        "referensi": [R[k] for k in ref],
    })


ESP32 = ("ESP32 DevKit V1 + kabel USB", 70000)
NANO = ("Arduino Nano (klon) + kabel USB", 55000)
BB = ("Breadboard 830 titik + kabel jumper", 35000)
PB = ("Power bank (catu terisolasi dari jala-jala)", 0)
OLED = ("OLED 0,96 inci I2C", 30000)
LAPTOP = ("Laptop dengan Python 3 (gratis: numpy, scipy, matplotlib)", 0)

# ---------- Spirometer ----------
P("spirometer", 1, ["sensor", "tekanan", "adc"], "Flowmeter venturi dengan sensor tekanan diferensial", "Menengah", "1–2 minggu",
  ["Elektrikal", "Desain"], ["fluida", "fisika-mekanika", "sensor", "sistem-tertanam"],
  "Membuktikan bahwa beda tekanan di leher venturi sebanding dengan kuadrat laju aliran (Bernoulli).",
  [NANO, BB, ("Sensor tekanan diferensial MPXV7002DP", 180000), ("Pipa PVC 1 inci + reducer (venturi) atau cetak 3D", 30000), ("Selang silikon 4 mm 1 meter", 10000)],
  ["Buat venturi dari pipa atau cetak 3D (diameter masuk 25 mm, leher 12 mm).", "Sambung dua tap tekanan ke port P1 dan P2 sensor.", "Baca tegangan di A0, kurangi offset nol saat tidak ada aliran.", "Hitung laju aliran Q = A2·√(2ΔP / (ρ(1 − (A2/A1)²))), lalu tampilkan di Serial Plotter."],
  "Grafik laju aliran (L/s) saat meniup pelan dan kuat, beserta tabel ΔP terhadap Q.",
  "Gunakan mouthpiece sendiri per orang dan cuci setelah dipakai. Jangan menghirup lewat alat.",
  ["venturi", "webster"])
P("spirometer", 2, ["integrasi", "interpretasi"], "Menghitung FEV1, FVC, dan rasio FEV1/FVC", "Menengah", "1 minggu",
  ["Informatika", "Dasar"], ["kalkulus", "fisiologi", "statistika", "pemrograman"],
  "Mengubah sinyal aliran menjadi volume dan membaca pola obstruktif atau restriktif seperti di klinik paru.",
  [LAPTOP, ("Data aliran dari proyek tahap 1 (CSV)", 0), ("Syringe 3 L (pinjam lab) untuk verifikasi, opsional", 0)],
  ["Integrasikan aliran dengan metode trapesium untuk mendapat volume terhadap waktu.", "Tentukan awal hembusan dengan back-extrapolation, lalu baca volume pada 1 detik (FEV1) dan volume akhir (FVC).", "Gambar kurva aliran-volume dan volume-waktu.", "Bandingkan rasio FEV1/FVC dengan batas 0,70 dan diskusikan arti klinisnya."],
  "Notebook yang mengeluarkan FEV1, FVC, FEV1/FVC, PEF, dan dua kurva spirometri.",
  "Hasil hanya untuk belajar, bukan diagnosis. Hentikan manuver bila pusing.",
  ["spiro2019"])

# ---------- Kapnograf ----------
P("kapnograf", 1, ["sumber", "detektor", "prosesor"], "Mengukur CO₂ dengan sensor NDIR", "Pemula", "1 minggu",
  ["Elektrikal", "Informatika"], ["fismed", "kimia", "sensor", "sistem-tertanam"],
  "Melihat prinsip NDIR: CO₂ menyerap inframerah 4,26 µm sehingga konsentrasi dapat diukur.",
  [ESP32, BB, ("Sensor CO₂ NDIR SCD30 atau MH-Z19B", 250000), OLED],
  ["Sambungkan sensor lewat I2C atau UART.", "Baca ppm CO₂ di ruang tertutup dan terbuka.", "Hembuskan napas pelan di dekat sensor dan amati kenaikan ppm.", "Diskusikan mengapa sensor ruangan terlalu lambat untuk kapnogram napas demi napas."],
  "Grafik ppm CO₂ terhadap waktu dan catatan waktu respon sensor.",
  "Jangan menutup mulut-hidung pada wadah tertutup. Ini bukan alat klinis.",
  ["scd30", "webster"])
P("kapnograf", 2, ["prosesor", "tampilan"], "Simulator kapnogram dan alarm EtCO₂", "Menengah", "1 minggu",
  ["Informatika", "Dasar"], ["fisiologi", "sinyal", "pemrograman", "visualisasi"],
  "Memahami fase I sampai IV kapnogram dan pola klinis (hipoventilasi, bronkospasme, intubasi esofagus).",
  [LAPTOP],
  ["Buat fungsi pembangkit kapnogram dengan parameter laju napas, EtCO₂, dan kemiringan plateau.", "Tambahkan pola: sirip hiu (bronkospasme), EtCO₂ naik bertahap (hipoventilasi), garis datar (apnea).", "Deteksi napas dan hitung EtCO₂ tiap napas.", "Buat alarm bila EtCO₂ di luar 35–45 mmHg atau tidak ada napas 20 detik."],
  "Program yang menampilkan kapnogram real-time beserta alarm.",
  "Simulasi untuk belajar membaca gelombang.",
  ["webster"])

# ---------- Mammografi ----------
P("mammografi", 1, ["detektor", "cad"], "Meningkatkan kontras citra mammogram", "Menengah", "1 minggu",
  ["Informatika"], ["pencitraan", "citra", "pemrograman"],
  "Melatih teknik peningkatan kontras (CLAHE, unsharp masking) yang dipakai untuk melihat mikrokalsifikasi.",
  [LAPTOP, ("Citra mammogram contoh dari dataset terbuka", 0)],
  ["Muat citra dan tampilkan histogramnya.", "Terapkan windowing, ekualisasi histogram, dan CLAHE.", "Gunakan filter top-hat untuk menonjolkan bintik terang kecil.", "Bandingkan hasil dan tulis kapan masing-masing membantu."],
  "Panel perbandingan citra asli dan hasil peningkatan.",
  "Data pasien harus anonim.",
  ["radon", "proteksi"])
P("mammografi", 2, ["cad"], "Detektor kandidat mikrokalsifikasi sederhana", "Lanjut", "2 minggu",
  ["Informatika"], ["citra", "ml-medis", "statistika"],
  "Membangun alur CAD: kandidat, fitur, klasifikasi, lalu menilai sensitivitas dan positif palsu.",
  [LAPTOP],
  ["Deteksi kandidat dengan ambang lokal dan connected components.", "Hitung fitur luas, kontras, dan kebulatan tiap kandidat.", "Latih classifier sederhana (random forest) pada label contoh.", "Gambar kurva FROC atau ROC dan diskusikan trade-off."],
  "Notebook CAD sederhana dengan metrik evaluasi.",
  "Hasil bukan diagnosis; CAD selalu dibaca ulang radiolog.",
  ["radon"])

# ---------- Fluoroskopi ----------
P("fluoroskopi", 1, ["generator", "tabung"], "Kalkulator dosis fluoroskopi dan ALARA", "Pemula", "3 hari",
  ["Dasar", "Informatika"], ["radiasi", "k3", "pemrograman"],
  "Melihat pengaruh mode pulsa, jarak, dan waktu terhadap dosis kulit pasien dan petugas.",
  [LAPTOP],
  ["Modelkan laju dosis sebanding mA, kuadrat kVp, dan 1/jarak².", "Bandingkan mode kontinu dengan pulsa 15, 7,5, dan 3,75 pulsa per detik.", "Hitung dosis petugas pada jarak 0,5 m, 1 m, dan 2 m dengan dan tanpa apron.", "Buat grafik dan rekomendasi singkat ALARA."],
  "Lembar kerja atau skrip yang menunjukkan penurunan dosis tiap langkah proteksi.",
  "Model sederhana untuk edukasi, bukan perhitungan dosis resmi.",
  ["proteksi"])
P("fluoroskopi", 2, ["intensifier", "tampilan"], "Filter derau temporal pada video fluoroskopi", "Menengah", "1 minggu",
  ["Informatika"], ["pencitraan", "citra", "sinyal"],
  "Memahami mengapa fluoroskopi dosis rendah berderau dan bagaimana rata-rata rekursif mengurangi derau.",
  [LAPTOP],
  ["Buat video sintetis kateter bergerak dengan derau Poisson.", "Terapkan rata-rata rekursif y = αx + (1 − α)y_lama.", "Ukur SNR dan amati efek ekor (lag) saat α kecil.", "Tambahkan deteksi gerak agar filter melemah di area bergerak."],
  "Video sebelum dan sesudah filter beserta grafik SNR.",
  "Simulasi perangkat lunak.",
  ["radon"])

# ---------- Telemedisin ----------
P("telemedisin", 1, ["video", "jaringan"], "Konsultasi video WebRTC di jaringan lokal", "Menengah", "1 minggu",
  ["Informatika"], ["kdm", "mobile", "iot"],
  "Memahami alur sinyal WebRTC (getUserMedia, offer-answer, ICE) dan dampak bandwidth pada kualitas video.",
  [LAPTOP, ("Dua perangkat (laptop dan ponsel) di Wi-Fi yang sama", 0)],
  ["Jalankan contoh WebRTC peer connection di dua browser.", "Ukur resolusi, frame rate, dan bitrate dari statistik getStats().", "Batasi bandwidth dan catat penurunan kualitas.", "Tulis kebutuhan minimum bandwidth untuk telekonsultasi."],
  "Tabel bitrate, latensi, dan kualitas video pada beberapa kondisi jaringan.",
  "Jangan merekam atau membagikan wajah orang lain tanpa izin.",
  ["webrtc"])
P("telemedisin", 2, ["perangkat", "platform", "dokter"], "Mengirim data tensi ke dasbor dokter dalam format FHIR", "Lanjut", "2 minggu",
  ["Informatika"], ["manajemen-data", "simrs", "visualisasi", "pemrograman"],
  "Membuat alur data pasien ke dokter dengan sumber daya FHIR Observation.",
  [LAPTOP, ESP32],
  ["Buat JSON FHIR Observation untuk tekanan darah (kode LOINC 85354-9).", "Kirim dari ESP32 atau skrip ke server lokal sederhana.", "Simpan dan tampilkan tren di dasbor web.", "Tambahkan tanda bahaya bila sistolik di atas 180 mmHg."],
  "Dasbor sederhana yang menampilkan riwayat tensi pasien.",
  "Gunakan data fiktif; jangan mengunggah data pasien asli ke server publik.",
  ["fhir"])

# ---------- RME ----------
P("rme", 1, ["input", "database"], "Basis data rekam medis mini", "Menengah", "1 minggu",
  ["Informatika"], ["manajemen-data", "pemrograman"],
  "Merancang tabel pasien, kunjungan, diagnosis, dan tindakan, lalu menulis query klinis.",
  [LAPTOP, ("SQLite (gratis)", 0)],
  ["Buat diagram entitas pasien, kunjungan, diagnosis (ICD-10), dan tindakan.", "Buat tabel dan isi data fiktif.", "Tulis query: kunjungan per bulan, 10 diagnosis terbanyak, pasien dengan hipertensi.", "Tambahkan tabel audit yang mencatat siapa mengubah apa."],
  "Basis data SQLite dan kumpulan query yang terdokumentasi.",
  "Gunakan data fiktif.",
  ["permenkes24"])
P("rme", 2, ["standar", "integrasi", "keamanan"], "Ekspor rekam medis ke FHIR dan hak akses", "Lanjut", "2 minggu",
  ["Informatika"], ["manajemen-data", "simrs", "iot"],
  "Mengubah data lokal menjadi sumber daya FHIR (Patient, Encounter, Condition) dan menerapkan hak akses per peran.",
  [LAPTOP],
  ["Petakan kolom tabel ke elemen FHIR.", "Buat skrip ekspor ke JSON Bundle.", "Validasi struktur dengan contoh resmi FHIR.", "Buat aturan akses: dokter bisa menulis, perekam medis membaca, pasien hanya datanya sendiri."],
  "Bundle FHIR hasil ekspor dan tabel matriks hak akses.",
  "Gunakan data fiktif.",
  ["fhir", "permenkes24"])

# ---------- Smartwatch ----------
P("smartwatch", 1, ["ppg", "mcu"], "Denyut dan SpO₂ di pergelangan dengan MAX30102", "Menengah", "1 minggu",
  ["Elektrikal", "Informatika"], ["sensor", "fisiologi", "sistem-tertanam"],
  "Membandingkan PPG di pergelangan dengan di jari dan melihat pengaruh gerak.",
  [ESP32, ("Modul MAX30102", 45000), OLED, ("Strap jam atau velcro", 15000), PB],
  ["Pasang sensor di jari, lalu di pergelangan.", "Bandingkan amplitudo sinyal AC dan kestabilan denyut.", "Gerakkan tangan dan amati artefak.", "Tambahkan filter bandpass 0,5–4 Hz dan bandingkan hasilnya."],
  "Grafik PPG jari vs pergelangan dan catatan pengaruh gerak.",
  "Pakai power bank, jangan sambil diisi dari charger.",
  ["max30102", "bangle"])
P("smartwatch", 2, ["imu", "ble", "aplikasi"], "Penghitung langkah dan deteksi jatuh dengan BLE", "Menengah", "1–2 minggu",
  ["Informatika", "Elektrikal"], ["sensor", "mobile", "iot", "ml-medis"],
  "Mengolah data akselerometer menjadi langkah dan kejadian jatuh, lalu mengirim notifikasi ke ponsel lewat BLE.",
  [ESP32, ("Modul IMU MPU6050", 25000), PB, ("Aplikasi nRF Connect (gratis)", 0)],
  ["Baca magnitudo percepatan 50 Hz.", "Hitung langkah dengan deteksi puncak dan ambang adaptif.", "Deteksi jatuh: lonjakan di atas 2,5 g diikuti diam beberapa detik.", "Kirim jumlah langkah dan peringatan jatuh sebagai karakteristik BLE."],
  "Gelang purwarupa yang mengirim langkah dan peringatan jatuh ke ponsel.",
  "Uji jatuh dengan menjatuhkan alat ke kasur, bukan menjatuhkan diri.",
  ["bangle"])

# ---------- Robot bedah ----------
P("robot-bedah", 1, ["lengan", "kontrol"], "Lengan robot 2 sendi dengan kinematika balik", "Menengah", "1–2 minggu",
  ["Elektrikal", "Informatika"], ["robotika", "kalkulus", "kendali", "fisika-mekanika"],
  "Menghitung sudut sendi dari posisi ujung (kinematika balik), dasar gerak instrumen robot bedah.",
  [NANO, BB, ("2 servo MG90S", 50000), ("Rangka akrilik atau cetak 3D", 40000), ("Catu 5 V 2 A", 35000)],
  ["Ukur panjang dua lengan.", "Turunkan rumus kinematika balik dua sendi dengan hukum kosinus.", "Kirim titik (x, y) dari Serial dan gerakkan servo.", "Uji kesalahan posisi pada beberapa titik dan catat."],
  "Lengan robot yang ujungnya menuju koordinat yang diminta.",
  "Jauhkan jari dari servo saat bergerak.",
  ["dvrk"])
P("robot-bedah", 2, ["konsol", "kontrol"], "Teleoperasi master-slave dengan skala gerak dan filter tremor", "Lanjut", "2 minggu",
  ["Elektrikal", "Informatika"], ["robotika", "kendali", "sinyal"],
  "Meniru konsol robot bedah: gerakan joystick diskalakan dan getaran tangan difilter sebelum menggerakkan lengan.",
  [NANO, ("Joystick analog 2 sumbu", 15000), ("Lengan dari tahap 1", 0)],
  ["Baca joystick sebagai master.", "Skalakan gerakan 5:1 sehingga gerak besar menjadi gerak kecil.", "Terapkan filter lowpass sekitar 2 Hz untuk meredam tremor 8–12 Hz.", "Tambahkan tombol kopling: lepas untuk reposisi, tahan untuk menggerakkan."],
  "Demo teleoperasi dengan perbandingan gerak sebelum dan sesudah filter.",
  "Kecepatan servo dibatasi agar tidak menyentak.",
  ["dvrk"])

# ---------- Dispenser obat ----------
P("pill-dispenser", 1, ["wadah", "motor", "rtc"], "Kotak obat putar terjadwal", "Pemula", "1–2 minggu",
  ["Elektrikal", "Desain"], ["sistem-tertanam", "eldig", "purwarupa", "cad-medis"],
  "Membuat dispenser yang memutar ke slot berikutnya tepat pada jam minum obat.",
  [NANO, ("Modul RTC DS3231", 25000), ("Motor stepper 28BYJ-48 + driver ULN2003", 30000), ("Buzzer + LED", 5000), ("Wadah 7 slot cetak 3D", 50000)],
  ["Desain wadah putar 7 slot di CAD dan cetak.", "Set waktu RTC dan simpan jadwal (misal 07.00, 13.00, 19.00).", "Saat jadwal tiba, putar stepper 1/7 putaran dan bunyikan buzzer.", "Uji 3 hari dan catat ketepatan waktu."],
  "Dispenser yang membuka slot tepat waktu dengan pengingat suara.",
  "Gunakan permen sebagai pengganti obat saat uji.",
  ["rtc"])
P("pill-dispenser", 2, ["notifikasi", "iot"], "Notifikasi keluarga bila obat tidak diambil", "Menengah", "1 minggu",
  ["Informatika", "Elektrikal"], ["iot", "mobile", "tek-keperawatan"],
  "Menutup lingkaran kepatuhan: sensor memastikan obat diambil, bila tidak keluarga diberi tahu.",
  [ESP32, ("Sensor IR obstacle", 8000), ("Broker MQTT gratis atau lokal", 0)],
  ["Pasang sensor IR di slot keluar.", "Bila 30 menit setelah jadwal obat belum diambil, kirim pesan MQTT.", "Tampilkan notifikasi di aplikasi MQTT di ponsel.", "Catat riwayat kepatuhan per hari."],
  "Dispenser terhubung dengan log kepatuhan dan notifikasi.",
  "Jangan mengandalkan purwarupa untuk obat sungguhan.",
  ["mqtt"])

# ---------- Patient monitor ----------
P("patient-monitor", 1, ["modul", "frontend", "tampilan"], "Monitor dua parameter: EKG dan SpO₂", "Menengah", "2 minggu",
  ["Elektrikal", "Informatika"], ["instrumen", "elektronika-medis", "sistem-tertanam"],
  "Menggabungkan dua modul akuisisi dalam satu layar seperti monitor pasien.",
  [ESP32, ("Modul AD8232 + elektroda", 85000), ("Modul MAX30102", 45000), ("LCD TFT 2,4 inci SPI", 90000), PB],
  ["Baca EKG 250 Hz dan PPG 100 Hz secara bergantian dengan timer.", "Tampilkan dua gelombang dan angka HR serta SpO₂.", "Samakan basis waktu kedua sinyal.", "Bandingkan HR dari EKG dan dari PPG."],
  "Layar monitor mini dengan dua gelombang dan angka.",
  "Hanya pakai power bank; laptop tidak terhubung charger saat elektroda menempel.",
  ["ad8232", "max30102"])
P("patient-monitor", 2, ["prosesor", "jaringan"], "Alarm berprioritas dan central station", "Lanjut", "1–2 minggu",
  ["Informatika"], ["iot", "kdm", "dtk", "tek-keperawatan"],
  "Merancang alarm tiga tingkat dan mengirim data ke central station lewat MQTT, sambil menekan alarm palsu.",
  [ESP32, LAPTOP],
  ["Tentukan batas alarm HR, SpO₂, dan prioritasnya (tinggi, sedang, rendah).", "Tambahkan tunda 10 detik untuk alarm sedang agar artefak singkat tidak memicu.", "Kirim data dan status alarm ke dasbor central station.", "Hitung berapa alarm palsu yang berkurang."],
  "Central station sederhana yang menampilkan banyak bed.",
  "Data fiktif atau dari diri sendiri saja.",
  ["mqtt", "iec60601"])

# ---------- Holter ----------
P("holter", 1, ["elektroda", "frontend", "penyimpan"], "Perekam EKG ke kartu microSD", "Menengah", "1–2 minggu",
  ["Elektrikal"], ["elektronika-medis", "sistem-tertanam", "eldig"],
  "Merekam EKG beberapa jam ke kartu memori seperti Holter.",
  [ESP32, ("Modul AD8232 + elektroda", 85000), ("Modul microSD + kartu 8 GB", 45000), PB],
  ["Sampling EKG 250 Hz dengan timer.", "Tulis ke microSD per blok 512 byte agar efisien.", "Rekam 1 jam sambil beraktivitas ringan.", "Hitung konsumsi daya dan perkirakan lama baterai."],
  "File rekaman EKG 1 jam dan estimasi daya.",
  "Catu baterai saja; lepas elektroda bila kulit iritasi.",
  ["ad8232", "microsd"])
P("holter", 2, ["analisis"], "Analisis Holter: deteksi QRS dan HRV", "Menengah", "1 minggu",
  ["Informatika"], ["sinyal", "statistika", "fisiologi"],
  "Mengolah rekaman panjang: deteksi denyut, ekstrasistol, dan indeks variabilitas denyut.",
  [LAPTOP],
  ["Muat rekaman MIT-BIH atau rekaman tahap 1.", "Deteksi QRS lalu hitung interval RR.", "Hitung SDNN, RMSSD, dan spektrum LF/HF.", "Tandai denyut prematur dari RR yang memendek mendadak."],
  "Laporan Holter mini: rata-rata HR, HRV, jumlah denyut prematur.",
  "Hanya untuk belajar.",
  ["mitdb"])

# ---------- EMG ----------
P("emg", 1, ["elektroda", "penguat", "filter"], "Merekam sinyal otot lengan", "Pemula", "1 minggu",
  ["Elektrikal"], ["elektronika-medis", "fisiologi", "anatomi"],
  "Melihat sinyal EMG mentah dan envelope saat otot dikontraksikan dengan beban berbeda.",
  [NANO, ("Modul Muscle BioAmp atau sensor EMG + elektroda", 150000), PB],
  ["Tempel elektroda di otot biseps sejajar serabut.", "Rekam saat istirahat, kontraksi ringan, dan kuat.", "Hitung RMS per 100 ms.", "Bandingkan RMS dengan beban yang diangkat."],
  "Grafik EMG mentah, envelope, dan hubungan RMS dengan beban.",
  "Catu baterai saja; jangan pasang elektroda melintasi dada.",
  ["bioamp_emg", "muscleshield"])
P("emg", 2, ["analisis", "tampilan"], "Kelelahan otot dari frekuensi median", "Menengah", "1 minggu",
  ["Informatika"], ["sinyal", "biomekanik", "ml-medis"],
  "Mengukur penurunan frekuensi median saat otot lelah dan mengklasifikasi gerakan.",
  [LAPTOP],
  ["Rekam kontraksi statis 60 detik.", "Hitung spektrum per jendela 1 detik dan frekuensi mediannya.", "Plot tren frekuensi median terhadap waktu.", "Latih classifier tiga gerakan (genggam, buka, istirahat) dari fitur RMS dan zero crossing."],
  "Grafik kelelahan otot dan akurasi klasifikasi gerakan.",
  "Istirahatkan otot bila nyeri.",
  ["emgdb"])

# ---------- Audiometer ----------
P("audiometer", 1, ["osilator", "atenuator", "transduser"], "Audiometer nada murni sederhana", "Pemula", "1 minggu",
  ["Informatika", "Dasar"], ["telinga", "fismed", "pemrograman"],
  "Membangkitkan nada 250–8000 Hz dengan intensitas bertahap 5 dB dan mencari ambang dengar.",
  [LAPTOP, ("Headphone tertutup", 150000)],
  ["Buat nada sinus per frekuensi dengan amplitudo turun 5 dB per langkah.", "Terapkan metode Hughson-Westlake: turun 10 dB saat terdengar, naik 5 dB saat tidak.", "Simpan ambang per frekuensi per telinga.", "Gambar audiogram dengan simbol O (kanan) dan X (kiri)."],
  "Aplikasi audiometer dan audiogram diri sendiri (relatif, belum terkalibrasi).",
  "Mulai dari volume kecil; jangan pernah memutar nada keras.",
  ["webster"])
P("audiometer", 2, ["atenuator", "audiogram"], "Kalibrasi relatif dan klasifikasi gangguan dengar", "Menengah", "1 minggu",
  ["Informatika", "Dasar"], ["kalibrasi", "telinga", "statistika"],
  "Memahami beda dB SPL dan dB HL, lalu menggolongkan derajat gangguan dengar.",
  [LAPTOP, ("Aplikasi sound level meter di ponsel", 0)],
  ["Ukur keluaran headphone dengan sound level meter untuk tiap frekuensi.", "Buat tabel koreksi ke dB HL memakai nilai referensi.", "Hitung rata-rata ambang 500, 1000, 2000, 4000 Hz.", "Golongkan normal, ringan, sedang, berat, sangat berat."],
  "Tabel koreksi dan laporan klasifikasi.",
  "Batasi keluaran maksimum 80 dB.",
  ["webster"])

# ---------- Alat bantu dengar ----------
P("alat-bantu-dengar", 1, ["mikrofon", "dsp", "receiver"], "Penguat suara multikanal di laptop", "Menengah", "1 minggu",
  ["Informatika"], ["sinyal", "telinga", "pemrograman"],
  "Membuat filter bank dan memberi penguatan berbeda per pita sesuai audiogram.",
  [LAPTOP, ("Headset dengan mikrofon", 100000)],
  ["Bagi sinyal ke 4–8 pita dengan filter bandpass.", "Hitung penguatan tiap pita dari audiogram (aturan setengah gain).", "Gabungkan kembali dan dengarkan.", "Ukur latensi; usahakan di bawah 10 ms."],
  "Program penguat suara real-time dengan pengaturan per pita.",
  "Batasi output agar tidak keras.",
  ["openmha"])
P("alat-bantu-dengar", 2, ["dsp"], "Kompresi dinamik WDRC dan peredam derau", "Lanjut", "1–2 minggu",
  ["Informatika"], ["sinyal", "ml-medis"],
  "Membuat suara pelan terdengar tanpa membuat suara keras menyakitkan.",
  [LAPTOP],
  ["Hitung level tiap pita dengan attack 5 ms dan release 50 ms.", "Terapkan kurva kompresi 2:1 di atas ambang lutut.", "Tambahkan peredam derau spektral sederhana.", "Bandingkan kejelasan bicara di ruang ramai."],
  "Modul WDRC dan peredam derau beserta grafik input-output.",
  "Uji dengan volume rendah.",
  ["openmha"])

# ---------- Implan koklea ----------
P("implan-koklea", 1, ["prosesor"], "Vokoder: mendengar seperti pengguna implan koklea", "Menengah", "1 minggu",
  ["Informatika", "Dasar"], ["sinyal", "telinga"],
  "Mensimulasikan strategi CIS dengan vokoder noise sehingga terdengar efek jumlah kanal.",
  [LAPTOP],
  ["Bagi suara bicara ke N pita logaritmik (4, 8, 16).", "Ambil envelope tiap pita dengan penyearah dan lowpass 160 Hz.", "Modulasikan derau pita sempit dengan envelope.", "Dengarkan dan catat jumlah kanal minimal agar kalimat dipahami."],
  "File suara vokoder 4, 8, 16 kanal dan catatan pemahaman bicara.",
  "Simulasi perangkat lunak.",
  ["loizou"])
P("implan-koklea", 2, ["transmisi", "stimulator"], "Transfer daya induktif melalui 'kulit'", "Menengah", "1 minggu",
  ["Elektrikal"], ["fisika-listrik-magnet", "elektronika-medis"],
  "Membuktikan pengiriman daya dan data lewat dua kumparan tanpa kabel seperti implan koklea.",
  [("Modul wireless charging 5 V (pemancar dan penerima)", 45000), ("LED + resistor", 3000), ("Lembar plastik atau karton 1–6 mm", 0), ("Multimeter", 0)],
  ["Nyalakan LED di sisi penerima.", "Selipkan penghalang 1–6 mm dan ukur tegangan terima.", "Geser kumparan dan catat pengaruh ketidaksejajaran.", "Hubungkan hasil dengan jarak kulit di atas implan (3–6 mm)."],
  "Grafik tegangan terima terhadap jarak dan pergeseran.",
  "Gunakan modul 5 V; jangan dekatkan ke alat implan sungguhan.",
  ["loizou"])

# ---------- Endoskop ----------
P("endoskop", 1, ["optik", "cahaya"], "Kamera endoskop USB dan pencahayaan", "Pemula", "3 hari",
  ["Elektrikal", "Informatika"], ["fismed", "pencitraan"],
  "Memahami kebutuhan cahaya dan fokus dekat pada kamera endoskop.",
  [("Kamera endoskop USB 5,5 mm dengan LED", 85000), LAPTOP, ("Model saluran dari pipa dan kertas bermotif", 0)],
  ["Tampilkan video endoskop di laptop dengan OpenCV.", "Ukur jarak fokus terbaik dan sudut pandang.", "Ubah kecerahan LED dan catat derau serta silau.", "Masukkan ke pipa berliku dan amati kesulitan navigasi."],
  "Catatan karakteristik kamera dan contoh tangkapan.",
  "Jangan memasukkan kamera ke tubuh.",
  ["kvasir"])
P("endoskop", 2, ["prosesor"], "Deteksi polip pada citra endoskopi", "Lanjut", "2 minggu",
  ["Informatika"], ["citra", "ml-medis"],
  "Melatih model klasifikasi atau segmentasi polip dari dataset endoskopi terbuka.",
  [LAPTOP],
  ["Unduh dataset Kvasir.", "Latih classifier transfer learning (normal vs polip).", "Ukur akurasi, sensitivitas, spesifisitas.", "Tampilkan peta aktivasi untuk melihat area yang dilihat model."],
  "Model dan laporan evaluasi.",
  "Model riset, bukan alat diagnosis.",
  ["kvasir"])

# ---------- CTG ----------
P("ctg", 1, ["toko"], "Sensor kontraksi dengan strain gauge", "Pemula", "1 minggu",
  ["Elektrikal"], ["sensor", "elektronika-medis"],
  "Membuat transduser toko sederhana dengan load cell dan HX711.",
  [NANO, ("Load cell 1 kg + modul HX711", 35000), ("Sabuk elastis", 15000)],
  ["Rakit load cell dengan HX711.", "Kalibrasi dengan beban 100 g dan 500 g.", "Pasang di sabuk dan tekan perlahan meniru kontraksi.", "Plot sinyal dan hitung durasi tiap kontraksi."],
  "Grafik kontraksi tiruan dengan durasi dan amplitudo.",
  "Tidak untuk dipasang pada ibu hamil.",
  ["webster"])
P("ctg", 2, ["autokorelasi", "tampilan"], "Analisis denyut jantung janin dari data CTG", "Menengah", "1–2 minggu",
  ["Informatika"], ["sinyal", "ilmu-data", "ml-medis"],
  "Menghitung baseline, variabilitas, akselerasi, dan deselerasi dari rekaman CTG terbuka.",
  [LAPTOP],
  ["Muat rekaman CTU-UHB.", "Bersihkan nilai hilang dan artefak.", "Hitung baseline dan variabilitas per 10 menit.", "Tandai akselerasi dan deselerasi lalu bandingkan dengan pH tali pusat."],
  "Notebook analisis CTG dengan grafik ala kertas CTG.",
  "Untuk belajar.",
  ["ctgdb"])

# ---------- PET ----------
P("pet", 1, ["koinsidensi", "rekonstruksi"], "Simulasi koinsidensi dan sinogram PET", "Menengah", "1 minggu",
  ["Informatika", "Dasar"], ["radiasi", "statistika", "pencitraan"],
  "Mensimulasikan anihilasi, pasangan foton, dan pembentukan sinogram.",
  [LAPTOP],
  ["Buat fantom aktivitas 2D dengan dua 'tumor'.", "Bangkitkan peluruhan acak (Poisson) dan arah foton berlawanan.", "Catat pasangan yang mengenai cincin detektor sebagai garis respons.", "Susun sinogram dan bandingkan dengan sinogram CT."],
  "Sinogram hasil simulasi dan penjelasan koinsidensi.",
  "Simulasi perangkat lunak.",
  ["radon"])
P("pet", 2, ["rekonstruksi", "fusi"], "Rekonstruksi FBP vs iteratif dan fusi warna", "Lanjut", "1–2 minggu",
  ["Informatika"], ["pencitraan", "citra", "visualisasi"],
  "Membandingkan FBP dan rekonstruksi iteratif pada data berderau, lalu menumpuk citra fungsional di atas anatomi.",
  [LAPTOP],
  ["Rekonstruksi sinogram tahap 1 dengan iradon (FBP).", "Rekonstruksi dengan SART iteratif.", "Bandingkan derau dan kontras lesi.", "Tumpangkan hasil sebagai peta warna di atas citra anatomi."],
  "Panel FBP vs iteratif dan citra fusi.",
  "Simulasi perangkat lunak.",
  ["radon"])

# ---------- Prostesis tangan ----------
P("prostesis-tangan", 1, ["pemindaian", "desain", "cetak", "aktuasi"], "Tangan body-powered cetak 3D", "Menengah", "2 minggu",
  ["Desain"], ["cad-medis", "purwarupa", "biomekanik", "difabel"],
  "Membuat tangan mekanis yang jari-jarinya menekuk saat pergelangan ditekuk, seperti desain e-NABLE.",
  [("Filamen PLA 1 kg", 180000), ("Akses printer 3D (lab kampus)", 0), ("Tali nilon, elastis, sekrup M3", 30000), ("Velcro dan busa", 25000)],
  ["Ukur lebar telapak dan panjang lengan bawah, skalakan model.", "Cetak jari, telapak, dan gauntlet.", "Rakit tali fleksor dan elastis ekstensor.", "Uji genggam benda ringan dan catat gaya serta sudut pergelangan."],
  "Tangan prostetik mekanis yang bisa menggenggam botol kecil.",
  "Haluskan tepi cetakan agar tidak melukai kulit.",
  ["enable"])
P("prostesis-tangan", 2, ["kontrol", "aktuasi"], "Kendali mioelektrik jari dengan servo", "Lanjut", "2 minggu",
  ["Elektrikal", "Informatika"], ["robotika", "sistem-tertanam", "ml-medis"],
  "Menggerakkan jari prostesis dari sinyal EMG lengan bawah.",
  [NANO, ("Sensor EMG + elektroda", 150000), ("Servo MG996R", 60000), ("Catu 6 V terpisah untuk servo", 50000), PB],
  ["Rekam EMG fleksor lengan bawah.", "Hitung envelope dan ambang buka-tutup dengan histeresis.", "Gerakkan servo yang menarik tali jari.", "Tambahkan batas arus atau waktu agar genggaman tidak terlalu kuat."],
  "Prostesis yang menutup saat otot dikontraksikan.",
  "EMG memakai catu baterai terpisah dari catu servo.",
  ["muscleshield", "enable"])

# ---------- ESU ----------
P("esu", 1, ["netral", "monitor"], "Simulasi densitas arus elektroda aktif dan pad netral", "Pemula", "3 hari",
  ["Dasar", "Informatika"], ["fisika-listrik-magnet", "k3"],
  "Memahami mengapa jaringan terpotong di elektroda aktif tetapi kulit di pad netral aman, dan kapan pad bisa membakar.",
  [LAPTOP],
  ["Hitung densitas arus J = I/A untuk ujung 1 mm² dan pad 100 cm².", "Hitung pemanasan sebanding J².", "Simulasikan pad yang setengah terlepas dan lihat kenaikan pemanasan.", "Jelaskan cara kerja pemantau kontak REM."],
  "Tabel dan grafik densitas arus serta risiko luka bakar.",
  "Jangan membuat generator RF berdaya tinggi sendiri.",
  ["webster", "iec60601"])
P("esu", 2, ["generator", "mode"], "Membangkitkan dan menganalisis gelombang cut dan coag", "Menengah", "1 minggu",
  ["Informatika", "Elektrikal"], ["sinyal", "elektronika-medis"],
  "Membandingkan gelombang potong (sinus kontinu) dan koagulasi (burst) dari sisi daya rata-rata dan crest factor.",
  [LAPTOP],
  ["Bangkitkan sinus 500 kHz kontinu dan burst dengan duty cycle 6%.", "Hitung daya rata-rata dan crest factor.", "Gambar spektrum keduanya.", "Hubungkan hasil dengan efek penguapan dan pengeringan jaringan."],
  "Notebook perbandingan bentuk gelombang ESU.",
  "Simulasi perangkat lunak.",
  ["webster"])

# ---------- Autoklaf ----------
P("autoklaf", 1, ["sensor", "kontrol"], "Logger suhu siklus sterilisasi", "Pemula", "1 minggu",
  ["Elektrikal"], ["sensor", "sistem-tertanam", "kalibrasi"],
  "Merekam profil suhu dan memeriksa apakah fase paparan tercapai.",
  [ESP32, ("Termokopel tipe K + MAX6675", 45000), ("Modul microSD", 25000), OLED],
  ["Rangkai termokopel dan uji di air mendidih (sekitar 100 °C).", "Rekam suhu tiap detik ke microSD.", "Uji pada panci presto di bawah pengawasan (sekitar 115–120 °C).", "Hitung lama suhu di atas 121 °C (atau 115 °C) dan nilai F0."],
  "Grafik siklus dan penilaian lulus atau gagal.",
  "Panci presto hanya dioperasikan sesuai petunjuk pabrik dan diawasi; jangan membuka saat bertekanan.",
  ["max6675"])
P("autoklaf", 2, ["kontrol", "katup"], "Kendali suhu dan urutan siklus (simulasi PID)", "Menengah", "1 minggu",
  ["Elektrikal", "Informatika"], ["kendali", "kimia"],
  "Merancang state machine siklus autoklaf dan kendali PID pemanas.",
  [LAPTOP],
  ["Modelkan ruang sebagai sistem orde satu dengan pemanas.", "Rancang PID agar suhu stabil 121 °C ±1 °C.", "Buat state machine: buang udara, naik suhu, paparan, buang uap, kering.", "Tambahkan interlock pintu dan katup pengaman."],
  "Simulasi siklus lengkap dengan grafik suhu-tekanan.",
  "Simulasi perangkat lunak.",
  ["webster"])

# ---------- Fototerapi ----------
P("fototerapi", 1, ["led", "driver", "pendingin"], "Panel LED biru dengan driver arus konstan", "Menengah", "1 minggu",
  ["Elektrikal"], ["elektronika-medis", "fismed"],
  "Membuat panel LED 460 nm dengan arus stabil dan memantau suhu LED.",
  [("LED biru 460 nm 1 W × 6 + heatsink", 60000), ("Driver arus konstan 350 mA", 25000), ("Catu 12 V 2 A", 50000), ("Termistor NTC", 3000), NANO],
  ["Rakit LED seri dengan driver arus konstan.", "Ukur arus dan tegangan tiap LED.", "Pantau suhu heatsink selama 30 menit.", "Hitung efisiensi dan kebutuhan pendingin."],
  "Panel LED biru dengan catatan suhu dan arus.",
  "Jangan menatap LED langsung; pakai kacamata pelindung cahaya biru. Bukan untuk bayi.",
  ["aap"])
P("fototerapi", 2, ["radiometer", "timer"], "Radiometer sederhana dan peta irradiansi", "Menengah", "1 minggu",
  ["Elektrikal", "Informatika"], ["sensor", "kalibrasi", "visualisasi"],
  "Mengukur sebaran intensitas cahaya di area tidur bayi dan menilai keseragaman.",
  [NANO, ("Sensor cahaya TSL2591 atau AS7341 spektral", 120000), ("Kertas grid 5 cm", 0)],
  ["Ukur intensitas di titik grid pada jarak 30 cm dari panel.", "Buat peta panas intensitas.", "Hitung rasio minimum dan maksimum.", "Tambahkan timer paparan dan pencatat jam pakai LED."],
  "Peta irradiansi dan rekomendasi jarak panel.",
  "Lindungi mata saat mengukur.",
  ["aap"])

# ---------- Mesin anestesi ----------
P("mesin-anestesi", 1, ["flowmeter", "vaporizer"], "Kalkulator aliran gas dan konsumsi agen anestesi", "Pemula", "3 hari",
  ["Dasar", "Informatika"], ["kimia", "fluida", "fisiologi"],
  "Menghitung konsumsi agen anestesi cair dari aliran gas segar dan persen vaporizer.",
  [LAPTOP],
  ["Gunakan rumus mL cair per jam = 3 × aliran gas segar (L/menit) × persen agen.", "Bandingkan aliran rendah (1 L/menit) dan tinggi (4 L/menit).", "Hitung biaya per jam untuk sevofluran.", "Diskusikan mengapa circle system dengan soda lime menghemat gas."],
  "Tabel konsumsi dan biaya per skenario.",
  "Kalkulator edukasi.",
  ["vam"])
P("mesin-anestesi", 2, ["sirkuit", "monitor"], "Menjelajah Virtual Anesthesia Machine", "Pemula", "3 hari",
  ["Dasar"], ["fisiologi", "k3", "tek-bedah"],
  "Melihat aliran gas di dalam mesin dan mencoba kegagalan umum secara aman di simulator.",
  [LAPTOP],
  ["Buka simulator mesin anestesi virtual.", "Telusuri jalur O₂ dari pipa sampai pasien.", "Coba skenario: O₂ habis, katup ekspirasi macet, soda lime jenuh.", "Catat alarm dan monitor yang pertama kali menunjukkan masalah."],
  "Laporan skenario kegagalan dan tanda yang muncul.",
  "Simulasi daring.",
  ["vam"])
