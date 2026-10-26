# -*- coding: utf-8 -*-
"""Proyek hands-on bertahap per alat (v1.2).

Setiap alat dipecah menjadi beberapa proyek kecil yang mengikuti blok alat:
biasanya tahap 1 = bagian sensor/elektrikal, tahap 2 = pengolahan data/informatika,
tahap 3 = integrasi, antarmuka, atau desain casing. Harga bahan = perkiraan
marketplace Indonesia (Tokopedia/Shopee) akhir 2026, bisa berbeda.
"""

LV = {1: "Pemula", 2: "Menengah", 3: "Lanjut"}

R = {
    "ad8232": "SparkFun AD8232 Heart Rate Monitor Hookup Guide: https://learn.sparkfun.com/tutorials/ad8232-heart-rate-monitor-hookup-guide/all",
    "ad8232b": "Last Minute Engineers, ECG monitor AD8232 + Arduino: https://lastminuteengineers.com/ad8232-ecg-monitor-arduino-tutorial/",
    "pantompkins": "Algoritma Pan–Tompkins (ringkasan): https://en.wikipedia.org/wiki/Pan%E2%80%93Tompkins_algorithm",
    "ecgdetectors": "py-ecg-detectors (implementasi Python detektor QRS): https://pypi.org/project/py-ecg-detectors/1.1.0/",
    "max30102": "MAX30102 + ESP32 (Microcontrollers Lab): https://microcontrollerslab.com/esp32-heart-rate-pulse-oximeter-max30102/",
    "max30102b": "MAX30102 + Arduino (How2Electronics): https://how2electronics.com/max30102-arduino-heart-rate-blood-oxygen-monitoring/",
    "mps20": "Kalibrasi sensor tekanan MPS20N0040D (Maker Portal): https://makersportal.com/blog/2020/6/4/mps20n0040d-pressure-sensor-calibration-with-arduino",
    "nibpunad": "Contoh tugas akhir tensimeter osilometrik berbasis Arduino (UNAD): https://repository.unad.edu.co/handle/10596/61953",
    "bioamp": "BioAmp EXG Pill, penguat biopotensial terbuka (OSH Park blog): https://blog.oshpark.com/2021/08/28/universal-bio-electrical-signal-amplifier-makes-reading-body-signals-easy/",
    "bioamp_emg": "Upside Down Labs, visualisasi EMG 2 kanal: https://www.hackster.io/upsidedownlabs/visualizing-2-channel-emg-on-lcd-display-module-d094cf",
    "muscleshield": "DIY Muscle BioAmp Shield (GitHub): https://github.com/upsidedownlabs/DIY-Muscle-BioAmp-Shield",
    "syringe": "Wijnen, Hunt, Anzalone, Pearce (2014), Open-Source Syringe Pump Library, PLOS ONE: https://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0107216",
    "syringe2": "Ulasan pompa suntik open source (3DPrint.com): https://3dprint.com/31738/open-source-syringe-pump/",
    "event": "Inside MIT's low-cost ventilator project (MIT Technology Review): https://www.technologyreview.com/2020/06/16/1002980/inside-mits-low-cost-ventilator-project",
    "event2": "MIT E-Vent siap dibuka untuk umum (VoxelMatters): https://www.voxelmatters.com/mit-emergency-ventilator-e-vent-project-is-ready/",
    "murgen": "Murgen, proyek USG open source (BeagleBoard): https://www.beagleboard.org/blog/2016-09-03-murgen-open-source-ultrasound-imaging",
    "murgen2": "Murgen: ultrasound imaging open source (Meccanismo Complesso): https://www.meccanismocomplesso.org/en/murgen-an-opensource-project-for-ultrasound-imaging/",
    "radar": "Ultrasonic radar Arduino + Processing (Arduino Project Hub): https://projecthub.arduino.cc/diegogalvan_1294/building-an-ultrasonic-radar-using-arduino-and-processing-59053e",
    "openflexure": "OpenFlexure Microscope: https://openflexure.org/",
    "openflexure2": "OpenFlexure, mikroskop cetak 3D open source (FocalPlane): https://focalplane.biologists.com/2021/10/19/openflexure-an-open-source-3d-printed-microscope/",
    "inkubator": "Low-cost and open-source neonatal incubator operated by an Arduino (HardwareX): https://doaj.org/article/9b930d1deb784c19a30e46b8a05e6f37",
    "inkubator2": "Data dan desain inkubator open source (Mendeley Data): https://data.mendeley.com/datasets/k59v85zjr5",
    "colorimeter": "Open-source colorimeter (Hackster/MOST): https://www.hackster.io/MOST/open-source-colorimeter-cd0a76",
    "colorimeter2": "Open-source colorimeter (RepRap wiki): https://reprap.org/wiki/Open-source_colorimeter",
    "paperfuge": "Paperfuge, sentrifus kertas 20 sen (Technology Networks): https://www.technologynetworks.com/diagnostics/news/paperfuge-a-20-cent-blood-centrifuge-279067",
    "paperfuge2": "Building a centrifuge on a shoestring (QEPrize): https://qeprize.org/news/building-centrifuge-shoestring",
    "osii": "OSI² ONE, MRI open source 50 mT: https://letsdatascience.com/news/osi2-one-brings-open-source-portable-mri-34fec67a",
    "ctedu": "An Educational CT Scanner Prototype of a 3rd Generation CT Scanner (IJIE): https://penerbit.uthm.edu.my/ojs/index.php/ijie/article/view/19123",
    "ctedu2": "An Educational CT Scanner Prototype Using Optical Scanning (MMU): https://shdl.mmu.edu.my/13360/",
    "slicer": "3D Slicer Training Compendium: https://training.slicer.org/",
    "mlx": "Termometer inframerah MLX90614 + Arduino (Circuit Digest): https://circuitdigest.com/microcontroller-projects/ir-thermometer-using-arduino-and-ir-temperature-sensor",
    "tcs": "Adafruit TCS34725 color sensor, kode Arduino: https://learn.adafruit.com/adafruit-color-sensors/arduino-code",
    "tcs2": "DFRobot TCS34725 wiki: https://wiki.dfrobot.com/TCS34725_I2C_Color_Sensor_For_Arduino_SKU__SEN0212",
    "drip": "Design, Fabrication, and Testing of an Internet Connected IV Drip Monitoring Device (MDPI JSAN): https://www2.mdpi.com/2224-2708/8/1/2",
    "drip2": "Alat monitoring infus berbasis web ESP8266 (UNY): https://journal.student.uny.ac.id/index.php/elektronika/article/view/9225",
    "mne": "Topomap EEG rasio alpha/theta dengan MNE (naplib): https://naplib-python.readthedocs.io/en/latest/auto_examples/integrating_naplib/plot_eeg_topomap.html",
    "mne2": "Getting started EEG analysis with MNE-Python: https://medium.com/@manishthilagar/getting-started-with-eeg-analysis-using-mne-python-a-beginners-guide-89dc753c76eb",
    "simnibs": "SimNIBS, simulasi medan listrik TMS/tES: https://simnibs.drcmr.dk/",
    "mcflirt": "FSL MCFLIRT, koreksi gerak fMRI: https://FSL.fmrib.ox.ac.uk/fsl/fslwiki/MCFLIRT",
    "nipype": "Nipype contoh alur fMRI dengan FSL: https://nipype.readthedocs.io/en/1.1.8/users/examples/fmri_fsl.html",
    "lfa": "Open-source smartphone reader untuk tes point-of-care (Diagnostics 2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC8947044",
    "brace": "Brace skoliosis cetak 3D dan pemindaian (Frontiers Rehab Sci 2022): https://www.frontiersin.org/journals/rehabilitation-sciences/articles/10.3389/fresc.2022.840286/pdf",
    "brace2": "Ulasan desain brace CAD/CAM (PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC9397992",
    "cellcount": "Identifikasi sel darah dengan image processing (GeeksforGeeks): https://www.geeksforgeeks.org/python-blood-cell-identification-using-image-processing/",
    "cellcount2": "Menghitung objek dengan connected components: https://medium.com/@enplim/image-processing-object-counting-using-connected-components-10c38f9c9ee2",
    "nfb": "Build your own neurofeedback game with OpenBCI: https://openbci.com/community/build-your-own-neurofeedback-game-with-openbci/",
    "brainflow": "BrainFlow (Python, akuisisi data biosensor): https://pypi.org/project/brainflow/",
    "cheapstat": "CheapStat: potensiostat DIY untuk edukasi (PLOS ONE 2011): https://pmc.ncbi.nlm.nih.gov/articles/PMC3172209",
    "ec": "DFRobot analog EC (konduktivitas) sensor: https://wiki.dfrobot.com/dfr0300/docs/19240",
    "ptsensor": "Fully printed prothrombin time sensor for point-of-care testing: https://agris.fao.org/search/en/records/65ded2c30f3e94b9e5d1cda5",
    "tens": "TENS circuit on breadboard (Hackaday.io): https://hackaday.io/project/165363-tens-circuit-on-breadboard",
    "iec60601": "Panduan ringkas IEC 60601-1: https://meddeviceguide.com/blog/iec-60601-1-medical-electrical-equipment-safety-guide",
    "essperf": "Essential performance alat medis (Johner Institute): https://blog.johner-institute.com/regulatory-affairs/essential-performance-of-medical-devices/",
    "webster": "Webster, Medical Instrumentation: Application and Design, ed. 5 (Wiley): https://search.worldcat.org/oclc/1131895650",
}

# Bahan yang sering dipakai, dengan perkiraan harga (Rp).
B = {
    "nano": ("Arduino Nano (klon) + kabel USB", 55000),
    "uno": ("Arduino Uno R3 (klon)", 85000),
    "esp32": ("ESP32 DevKit V1", 75000),
    "oled": ("OLED 0,96\" I2C SSD1306", 35000),
    "tft": ("LCD TFT 2,4\" SPI ILI9341", 110000),
    "bb": ("Breadboard 830 titik + kabel jumper", 35000),
    "batt": ("Baterai Li-ion 18650 + holder + modul TP4056", 45000),
    "powerbank": ("Power bank (catu terisolasi dari jala-jala, wajib untuk biopotensial)", 0),
    "res": ("Paket resistor & kapasitor", 30000),
    "laptop": ("Laptop dengan Python 3 (sudah ada)", 0),
    "print3d": ("Cetak 3D casing PLA (jasa cetak per jam / filamen)", 75000),
    "servo": ("Servo SG90", 15000),
    "stepper": ("Motor stepper NEMA17 + driver A4988", 110000),
    "relay": ("Modul relay 5 V / MOSFET IRF520", 15000),
    "buzzer": ("Buzzer aktif + LED indikator", 8000),
    "ds18": ("Sensor suhu DS18B20 waterproof", 18000),
    "dht": ("Sensor suhu-kelembapan DHT22/AM2302", 45000),
    "multimeter": ("Multimeter digital (pinjam lab bila ada)", 90000),
    "osilo": ("Osiloskop (pinjam lab) atau osiloskop mini DSO138", 250000),
}


def b(*keys, extra=()):
    out = [list(B[k]) for k in keys]
    out += [list(x) for x in extra]
    return out


P = []


def proj(alat, tahap, blok, judul, level, durasi, bidang, materi, tujuan, bahan, langkah, hasil, aman, refs):
    P.append({
        "id": f"{alat}-{tahap}", "alat": alat, "tahap": tahap, "blok": blok,
        "judul": judul, "level": LV[level], "durasi": durasi, "bidang": bidang,
        "materi": materi, "tujuan": tujuan, "bahan": bahan, "langkah": langkah,
        "hasil": hasil, "keselamatan": aman, "referensi": [R[r] for r in refs],
    })


BIO_SAFE = "Hanya pakai catu baterai/power bank, laptop dicabut dari charger saat elektroda menempel di tubuh. Jangan pernah menyambung rangkaian ini ke jala-jala PLN."
LOAD_SAFE = "Uji keluaran HANYA ke beban dummy (resistor 500 Ω–1 kΩ) dan osiloskop. Jangan ditempel ke tubuh: ini alat belajar, bukan alat terapi bersertifikat."

# ---------------- EKG ----------------
proj("ekg", 1, ["elektroda", "penguat", "filter"], "Menangkap sinyal jantung dengan AD8232", 1, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "fisiologi", "sensor", "elda"],
     "Melihat langsung bagaimana biopotensial jantung (±1 mV) diperkuat oleh penguat instrumentasi dan difilter.",
     b("nano", "bb", "powerbank", extra=[("Modul AD8232 + kabel 3 lead + 10 elektroda Ag/AgCl", 85000)]),
     ["Rakit AD8232 ke Arduino (OUTPUT→A0, LO+/LO−→D10/D11).", "Pasang elektroda RA, LA, RL sesuai panduan SparkFun.",
      "Tampilkan sinyal di Serial Plotter, lalu catat bentuk P-QRS-T.", "Coba gerakkan lengan: amati artefak gerak dan lead-off."],
     "Grafik EKG real-time di laptop dan catatan perbandingan sinyal diam vs bergerak.",
     BIO_SAFE, ["ad8232", "ad8232b"])
proj("ekg", 2, ["filter", "prosesor"], "Filter digital dan deteksi detak (Pan–Tompkins)", 2, "1–2 minggu", ["Informatika"],
     ["sinyal", "pemrograman", "kalkulus"],
     "Mengubah sinyal mentah menjadi detak jantung (BPM) dengan filter bandpass 0,5–40 Hz, notch 50 Hz, dan algoritma Pan–Tompkins.",
     b("laptop"),
     ["Rekam 60 detik data dari tahap 1 ke file CSV (atau unduh rekaman MIT-BIH dari PhysioNet).",
      "Di Python (numpy/scipy) buat filter Butterworth bandpass dan notch 50 Hz, bandingkan spektrum sebelum/sesudah.",
      "Implementasikan tahap Pan–Tompkins: turunan, kuadrat, moving window integration, ambang adaptif.",
      "Hitung BPM dan interval RR, lalu bandingkan dengan py-ecg-detectors."],
     "Notebook Python yang menampilkan sinyal terfilter, titik R, dan BPM.",
     "Aman (hanya pengolahan data).", ["pantompkins", "ecgdetectors"])
proj("ekg", 3, ["prosesor", "tampilan"], "Monitor EKG portabel dengan layar dan IoT", 2, "2 minggu", ["Informatika", "Desain"],
     ["sistem-tertanam", "iot", "cad-medis", "purwarupa"],
     "Memindahkan deteksi detak ke mikrokontroler, menampilkan gelombang di layar, mengirim BPM ke ponsel, lalu membuat casing.",
     b("esp32", "tft", "batt", "print3d"),
     ["Port deteksi QRS sederhana ke ESP32 (ambang + periode refraktori 200 ms).", "Gambar gelombang bergulir di TFT dan BPM di pojok.",
      "Kirim BPM lewat Bluetooth/Wi-Fi ke dasbor sederhana.", "Desain casing di Fusion 360/Onshape dengan lubang konektor lead dan baterai."],
     "Prototipe monitor EKG genggam bertenaga baterai.",
     BIO_SAFE, ["ad8232", "iec60601"])
proj("ekg", 4, ["isolasi"], "Mengukur keselamatan: arus bocor dan isolasi", 3, "1 minggu", ["Elektrikal"],
     ["k3", "instrumen", "elektronika-medis"],
     "Memahami kenapa bagian pasien harus terisolasi (tipe BF/CF) dan bagaimana arus bocor diukur menurut IEC 60601-1.",
     b("multimeter", "res"),
     ["Baca ringkasan IEC 60601-1 tentang applied part tipe B, BF, CF.", "Buat rangkaian ukur arus bocor (jaringan 1 kΩ ∥ 10 nF + 10 kΩ) di breadboard dengan sumber tegangan rendah.",
      "Hitung batas arus bocor pasien untuk tipe CF dan bandingkan dengan simulasi.", "Tulis rekomendasi isolasi (optocoupler/isolator digital) untuk prototipe tahap 3."],
     "Laporan singkat analisis isolasi dan diagram blok prototipe yang lebih aman.",
     "Gunakan sumber tegangan rendah (≤12 V). Jangan bereksperimen dengan tegangan jala-jala.", ["iec60601", "essperf"])

# ---------------- Pulse oximeter ----------------
proj("oksimeter", 1, ["led", "fotodioda", "tia"], "Membaca PPG merah dan inframerah", 1, "1 minggu", ["Elektrikal"],
     ["fisiologi", "elektronika-medis", "fisika-listrik-magnet", "sensor"],
     "Memahami fotopletismografi: cahaya merah (660 nm) dan IR (880 nm) diserap berbeda oleh hemoglobin beroksigen.",
     b("esp32", "bb", "oled", extra=[("Modul MAX30102", 35000)]),
     ["Sambungkan MAX30102 lewat I2C ke ESP32.", "Tampilkan nilai mentah RED dan IR di Serial Plotter.",
      "Bandingkan sinyal saat jari diam, ditekan kuat, dan bergerak.", "Catat komponen AC (denyut) dan DC (jaringan) tiap kanal."],
     "Grafik PPG dua kanal dan tabel AC/DC.", "Aman. Hindari menatap LED IR dari dekat.", ["max30102", "max30102b"])
proj("oksimeter", 2, ["algoritma"], "Menghitung SpO₂ dengan rasio R", 2, "1 minggu", ["Informatika"],
     ["sinyal", "pemrograman", "statistika", "kalkulus"],
     "Menurunkan SpO₂ dari R = (AC_red/DC_red)/(AC_ir/DC_ir) dan memahami kenapa perlu kurva kalibrasi.",
     b("laptop"),
     ["Simpan data RED/IR ke CSV.", "Filter bandpass 0,5–5 Hz, cari puncak-lembah untuk AC, rata-rata untuk DC.",
      "Hitung R per denyut lalu SpO₂ ≈ 110 − 25·R (kurva empiris umum) dan detak dari jarak puncak.",
      "Bandingkan dengan oksimeter komersial pada 5 orang, hitung bias dan limits of agreement (Bland–Altman)."],
     "Notebook perhitungan SpO₂ + grafik Bland–Altman.", "Aman. Ini bukan alat diagnosis.", ["max30102b"])
proj("oksimeter", 3, ["tampilan"], "Oksimeter jepit jari dengan casing sendiri", 2, "2 minggu", ["Desain", "Informatika"],
     ["cad-medis", "purwarupa", "dtk", "mobile"],
     "Mendesain klip jari yang menutup cahaya luar dan menampilkan SpO₂ + BPM di OLED atau aplikasi ponsel.",
     b("esp32", "oled", "batt", "print3d"),
     ["Ukur lebar jari (dewasa ±14–20 mm) dan buat klip berpegas di CAD.", "Cetak 3D, uji kebocoran cahaya ambien.",
      "Tampilkan SpO₂/BPM dan indikator kualitas sinyal.", "Opsional: kirim ke aplikasi ponsel lewat BLE."],
     "Prototipe oksimeter genggam dan catatan uji pengguna.", "Aman.", ["max30102"])

# ---------------- Tensimeter ----------------
proj("tensimeter", 1, ["manset", "sensor", "pengondisi"], "Sensor tekanan manset dan kalibrasi", 1, "1 minggu", ["Elektrikal"],
     ["fisika-mekanika", "sensor", "elektronika-medis"],
     "Mengubah tekanan udara manset menjadi angka mmHg yang terkalibrasi.",
     b("nano", "bb", extra=[("Sensor tekanan MPS20N0040D + modul HX710B", 30000), ("Manset + bulb tensimeter cadangan", 60000), ("Selang silikon 4 mm + konektor T", 15000)]),
     ["Sambungkan sensor ke manset lewat konektor T.", "Baca nilai HX710B, lalu kalibrasi dengan tensimeter aneroid/raksa pembanding (regresi linear).",
      "Konversi kPa→mmHg (1 kPa = 7,50 mmHg)."], "Persamaan kalibrasi dan grafik tekanan vs waktu.",
     "Jangan pompa manset di atas 200 mmHg dan jangan lebih dari 2 menit di lengan.", ["mps20"])
proj("tensimeter", 2, ["kontrol", "algoritma"], "Pompa otomatis dan algoritma osilometrik", 2, "2 minggu", ["Elektrikal", "Informatika"],
     ["sistem-tertanam", "sinyal", "kendali", "fisiologi"],
     "Memompa manset otomatis, mengempiskan perlahan, lalu mencari sistolik/diastolik dari amplitudo osilasi.",
     b("nano", "relay", extra=[("Pompa udara mini 3–6 V", 18000), ("Katup solenoid 6 V normally open", 25000)]),
     ["Kendalikan pompa hingga 180 mmHg lalu buka katup secara bertahap (laju turun 2–3 mmHg/detik).",
      "Pisahkan osilasi dengan high-pass 0,5 Hz.", "Cari MAP pada osilasi maksimum; sistolik ≈ 0,5·Amax, diastolik ≈ 0,8·Amax (rasio karakteristik).",
      "Bandingkan dengan tensimeter digital komersial pada 10 pengukuran."],
     "Tensimeter otomatis sederhana + tabel perbandingan.",
     "Pasang batas aman: katup terbuka otomatis bila tekanan > 200 mmHg atau waktu > 120 detik.", ["nibpunad", "mps20"])
proj("tensimeter", 3, ["kontrol"], "Desain antarmuka pengguna tensimeter rumah", 1, "1 minggu", ["Desain"],
     ["design-thinking", "interaksi-pasien", "dtk"],
     "Merancang tampilan dan alur pemakaian yang mudah untuk lansia (tombol besar, angka jelas, kategori tekanan darah).",
     b("print3d"),
     ["Wawancara 3 calon pengguna lansia (empati).", "Buat 2 sketsa layar dan casing, uji dengan prototipe kertas.",
      "Pilih desain, buat model CAD, dan catat masukan pengguna."], "Prototipe casing dan laporan design thinking.", "Aman.", ["iec60601"])

# ---------------- USG ----------------
proj("usg", 1, ["transduser", "pemancar", "penerima"], "Prinsip pulsa-gema dengan sensor ultrasonik", 1, "1 minggu", ["Elektrikal"],
     ["fisika-mekanika", "pencitraan", "sensor"],
     "Memahami waktu tempuh gema (d = c·t/2) memakai sensor ultrasonik 40 kHz di udara, sebagai analogi transduser USG MHz di jaringan.",
     b("uno", "bb", extra=[("Sensor HC-SR04", 12000)]),
     ["Ukur waktu gema ke benda pada jarak 10–100 cm.", "Hitung kecepatan suara dari data dan bandingkan 343 m/s.",
      "Hitung: jika c jaringan 1540 m/s, berapa waktu gema dari kedalaman 5 cm?"], "Tabel jarak-waktu dan perhitungan.", "Aman.", ["radar"])
proj("usg", 2, ["beamformer", "pengolah"], "Mode-B mini: memindai dengan servo", 2, "1–2 minggu", ["Informatika", "Elektrikal"],
     ["pemrograman", "pencitraan", "visualisasi"],
     "Membentuk citra 2D dari banyak garis A-mode, seperti probe sektor USG.",
     b("uno", "servo", extra=[("Sensor HC-SR04", 12000)]),
     ["Pasang HC-SR04 di atas servo, sapu 0–180°.", "Kirim sudut dan jarak ke laptop, gambar sebagai kipas (koordinat polar→kartesian) di Python/Processing.",
      "Tambahkan pemetaan intensitas (grayscale) dan bandingkan dengan citra USG mode-B sungguhan."],
     "Visualisasi 'radar' yang menjelaskan scan converter USG.", "Aman.", ["radar", "murgen"])
proj("usg", 3, ["penerima", "pengolah"], "Pengolahan sinyal RF ultrasound: envelope dan kompresi log", 3, "2 minggu", ["Informatika"],
     ["sinyal", "pencitraan", "pemrograman"],
     "Mengolah data RF (dari proyek Murgen atau data contoh) menjadi citra: filter bandpass, deteksi envelope (Hilbert), kompresi logaritmik.",
     b("laptop"),
     ["Unduh contoh data RF dari repositori Murgen.", "Terapkan filter bandpass di sekitar frekuensi transduser.",
      "Hitung envelope dengan transformasi Hilbert dan kompres 20·log10.", "Susun garis-garis menjadi citra dan atur time gain compensation (TGC)."],
     "Citra mode-B hasil olahan sendiri.", "Aman.", ["murgen", "murgen2"])

# ---------------- X-ray ----------------
proj("xray", 1, ["tabung", "detektor"], "Simulasi atenuasi dengan cahaya", 1, "1 minggu", ["Elektrikal"],
     ["fismed", "pencitraan", "sensor", "kalkulus"],
     "Memahami hukum Beer–Lambert I = I₀·e^(−μx) memakai LED dan LDR/fotodioda sebagai pengganti sinar-X (tanpa radiasi pengion).",
     b("nano", "bb", "res", extra=[("LED putih terang + LDR/fotodioda BPW34", 15000), ("Lembaran plastik/kertas sebagai 'jaringan'", 10000)]),
     ["Ukur intensitas cahaya tembus untuk 0–10 lapis bahan.", "Plot ln(I/I₀) terhadap tebal, hitung μ dari kemiringan.",
      "Bandingkan dua bahan (kertas vs plastik) seperti jaringan lunak vs tulang."], "Grafik atenuasi dan nilai μ.", "Aman (tidak memakai sinar-X).", ["webster"])
proj("xray", 2, ["konsol"], "Penampil DICOM dengan windowing", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "pencitraan", "manajemen-data", "citra"],
     "Membaca citra radiografi DICOM, menampilkan metadata, dan mengatur window level/width seperti konsol radiologi.",
     b("laptop"),
     ["Pasang pydicom dan matplotlib.", "Buka contoh DICOM, tampilkan tag penting (kVp, mAs, ukuran piksel).",
      "Buat slider window level/width, lalu simpan sebagai PNG."], "Aplikasi kecil penampil DICOM.", "Aman. Anonimkan data pasien bila memakai citra asli.", ["slicer"])
proj("xray", 3, ["kolimator"], "Perhitungan proteksi radiasi ruang X-ray", 2, "1 minggu", ["Desain"],
     ["radiasi", "dtk", "k3"],
     "Mendesain denah ruang radiografi: jarak, perisai timbal, dan area kendali memakai prinsip waktu-jarak-perisai.",
     b("laptop"),
     ["Pelajari hukum kuadrat terbalik dan nilai HVL timbal.", "Hitung dosis di balik dinding untuk beberapa ketebalan.",
      "Gambar denah ruang dengan zona kendali di CAD."], "Denah ruang dan tabel perhitungan perisai.", "Aman (perhitungan).", ["webster"])

# ---------------- CT ----------------
proj("ct", 1, ["tabung", "gantry", "detektor"], "CT optik mini dengan laser dan meja putar", 2, "2 minggu", ["Elektrikal", "Desain"],
     ["fismed", "sistem-tertanam", "cad-medis", "pencitraan"],
     "Meniru CT generasi 1: sumber cahaya dan detektor bergeser lalu objek diputar, menghasilkan sinogram.",
     b("uno", "stepper", "servo", "print3d", extra=[("Modul laser merah 5 mW + fotodioda/LDR", 20000), ("Rel linier/rak gigi cetak 3D", 30000)]),
     ["Buat dudukan objek berputar (stepper) dan rel geser sumber-detektor.", "Ambil proyeksi intensitas tiap 1–2° untuk 180°.",
      "Simpan data sebagai matriks sinogram."], "Data sinogram dari objek tembus cahaya (botol, lilin).",
     "Jangan menatap sinar laser.", ["ctedu", "ctedu2"])
proj("ct", 2, ["rekonstruksi"], "Rekonstruksi filtered back projection", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "sinyal", "kalkulus", "citra"],
     "Membangun ulang irisan dari sinogram dengan transformasi Radon terbalik.",
     b("laptop"),
     ["Pakai phantom Shepp–Logan (scikit-image) untuk membuat sinogram.", "Rekonstruksi dengan back projection biasa lalu dengan filter ramp.",
      "Bandingkan jumlah sudut (30, 90, 180) terhadap artefak streak.", "Rekonstruksi data dari tahap 1."], "Notebook rekonstruksi CT.", "Aman.", ["ctedu"])
proj("ct", 3, ["tampilan"], "Visualisasi 3D dari irisan CT dengan 3D Slicer", 1, "1 minggu", ["Informatika", "Desain"],
     ["visualisasi", "cad-medis", "anatomi"],
     "Mengubah tumpukan DICOM menjadi model 3D tulang dan mencetaknya.",
     b("laptop", "print3d"),
     ["Ikuti modul Data Loading & Visualization di 3D Slicer.", "Segmentasi tulang dengan threshold HU.", "Ekspor STL dan cetak 3D."],
     "Model 3D anatomi dari data CT.", "Aman.", ["slicer"])

# ---------------- MRI ----------------
proj("mri", 1, ["magnet", "gradien"], "Memetakan medan magnet dengan sensor Hall", 1, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "sensor", "pencitraan"],
     "Mengukur medan dari kumparan Helmholtz dan magnet permanen, untuk memahami homogenitas dan gradien medan.",
     b("nano", "bb", extra=[("Sensor Hall linear SS49E/A1302", 10000), ("Kawat email 0,5 mm 100 m", 60000), ("Catu daya DC 12 V 2 A", 60000)]),
     ["Gulung dua kumparan Helmholtz (jari-jari = jarak).", "Ukur medan di grid 1 cm, plot peta warna.",
      "Ubah arus satu kumparan untuk membuat gradien, lalu amati perubahan peta."], "Peta medan dan perbandingan dengan rumus.",
     "Kumparan bisa panas; batasi arus dan waktu.", ["osii"])
proj("mri", 2, ["rf", "akuisisi"], "Simulasi presesi dan sinyal FID", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "fisika-listrik-magnet", "kalkulus"],
     "Mensimulasikan persamaan Bloch: presesi Larmor, T1/T2, dan sinyal free induction decay.",
     b("laptop"),
     ["Tulis simulasi vektor magnetisasi di Python.", "Variasikan T1/T2 untuk lemak, air, otot.", "Animasikan spin echo (90°–180°)."],
     "Animasi Bloch dan grafik FID.", "Aman.", ["osii"])
proj("mri", 3, ["rekonstruksi"], "Rekonstruksi citra dari k-space", 2, "1 minggu", ["Informatika"],
     ["sinyal", "citra", "pemrograman"],
     "Memahami bahwa MRI mengukur ruang frekuensi (k-space) dan citra didapat dengan FFT 2D terbalik.",
     b("laptop"),
     ["Ambil citra otak contoh, ubah ke k-space dengan FFT 2D.", "Hapus bagian tepi/tengah k-space dan lihat efeknya (resolusi vs kontras).",
      "Simulasikan undersampling dan artefak aliasing."], "Notebook k-space interaktif.", "Aman.", ["osii"])

# ---------------- Ventilator ----------------
proj("ventilator", 1, ["sensor"], "Sensor tekanan dan aliran napas", 2, "1 minggu", ["Elektrikal"],
     ["fluida", "sensor", "fisiologi"],
     "Mengukur tekanan jalan napas dan aliran memakai sensor tekanan diferensial pada orifis/venturi.",
     b("esp32", "bb", "print3d", extra=[("Sensor tekanan BMP280/MPX5010DP", 60000), ("Venturi/orifis cetak 3D + selang", 20000), ("Balon/kantong uji paru (test lung)", 30000)]),
     ["Cetak venturi, pasang sensor tekanan diferensial.", "Kalibrasi aliran dengan volume diketahui (botol/spirometer).",
      "Tampilkan kurva tekanan, aliran, dan volume (integral aliran)."], "Grafik P–Q–V dari kantong uji.", "Uji hanya ke kantong/balon uji, jangan ke manusia.", ["event"])
proj("ventilator", 2, ["aktuator", "kontrol"], "Penekan kantong ambu dengan servo (gaya E-Vent)", 3, "2–3 minggu", ["Elektrikal", "Desain"],
     ["kendali", "sistem-tertanam", "purwarupa", "biomekanik"],
     "Membuat mekanisme penekan kantong resusitasi dengan pengaturan laju napas (RR), volume tidal, dan rasio I:E.",
     b("esp32", "stepper", "print3d", extra=[("Kantong resusitasi (ambu bag) dewasa", 150000), ("Potensiometer 3 buah + rangka akrilik/aluminium", 60000)]),
     ["Pelajari desain mekanik MIT E-Vent.", "Buat lengan penekan dan atur sudut tekan untuk volume tidal tertentu.",
      "Atur RR 10–30/menit dan I:E 1:2 lewat potensiometer.", "Gunakan sensor tahap 1 untuk loop tertutup tekanan puncak."],
     "Prototipe mekanik yang memompa test lung.", "Ini prototipe belajar, bukan ventilator klinis.", ["event", "event2"])
proj("ventilator", 3, ["alarm"], "Logika alarm dan antarmuka klinis", 2, "1 minggu", ["Informatika", "Desain"],
     ["pemrograman", "interaksi-pasien", "tek-keperawatan"],
     "Merancang alarm tekanan tinggi/rendah, apnea, dan diskoneksi dengan prioritas sesuai standar alarm alat medis.",
     b("esp32", "tft", "buzzer"),
     ["Definisikan ambang alarm dari data tahap 1.", "Buat mesin status alarm (normal/peringatan/kritis) dengan bunyi berbeda.",
      "Uji dengan skenario: selang lepas, tersumbat."], "Layar status ventilator dan uji skenario alarm.", "Aman.", ["event"])

# ---------------- Infus ----------------
proj("infus", 1, ["sensor"], "Penghitung tetes infus inframerah", 1, "1 minggu", ["Elektrikal"],
     ["sensor", "elektronika-medis", "tek-keperawatan"],
     "Menghitung tetes di drip chamber dengan pasangan LED IR–fototransistor untuk memantau laju infus.",
     b("esp32", "oled", "bb", extra=[("Sensor IR obstacle/optocoupler celah", 10000), ("Set infus + botol air (simulasi)", 25000)]),
     ["Jepit sensor di drip chamber.", "Hitung tetes dengan interrupt dan laju tetes/menit.",
      "Konversi ke mL/jam (faktor tetes 20 tetes/mL makro atau 60 tetes/mL mikro)."], "Monitor laju tetes.", "Pakai air, bukan cairan medis.", ["drip", "drip2"])
proj("infus", 2, ["motor", "peristaltik", "kontrol"], "Pompa suntik open source dengan stepper", 2, "2 minggu", ["Elektrikal", "Desain"],
     ["kendali", "fisika-mekanika", "cad-medis", "purwarupa"],
     "Membangun syringe pump dari pustaka desain open source dan mengkalibrasi laju aliran.",
     b("uno", "stepper", "print3d", extra=[("Batang ulir M8 + mur + bearing", 40000), ("Spuit 10/20 mL", 5000)]),
     ["Cetak bagian dari Open-Source Syringe Pump Library.", "Hitung langkah/mL dari pitch ulir dan diameter spuit.",
      "Uji laju 1–20 mL/jam dengan menimbang air (gravimetri)."], "Pompa suntik terkalibrasi dan grafik akurasi.", "Hanya air.", ["syringe", "syringe2"])
proj("infus", 3, ["antarmuka"], "Notifikasi infus habis/tersumbat ke perawat", 2, "1 minggu", ["Informatika"],
     ["iot", "mobile", "tek-keperawatan", "interaksi-pasien"],
     "Mengirim peringatan ke ponsel saat tetes berhenti atau botol hampir habis.",
     b("esp32"),
     ["Gabungkan tahap 1 dengan Wi-Fi (MQTT/Telegram bot).", "Tetapkan logika: tidak ada tetes 60 detik = tersumbat/habis.",
      "Buat dasbor beberapa bed."], "Sistem notifikasi infus multi-bed.", "Aman.", ["drip"])

# ---------------- Defibrilator ----------------
proj("defibrilator", 1, ["pengisi", "kapasitor", "saklar"], "Pengisian dan pelepasan kapasitor bertegangan rendah", 1, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "elektronika-medis", "rangkaian"],
     "Memahami energi defibrilasi E = ½CV² dan bentuk gelombang pelepasan RC memakai kapasitor bertegangan rendah.",
     b("nano", "bb", "osilo", extra=[("Kapasitor elektrolit 1000–4700 µF 25 V", 15000), ("Resistor daya 50 Ω 5 W (beban 'pasien')", 8000)]),
     ["Isi kapasitor ke 12 V, ukur waktu pengisian.", "Lepaskan ke resistor 50 Ω, rekam kurva peluruhan.",
      "Hitung τ = RC dan energi; skalakan ke defibrilator nyata (150–200 J)."], "Kurva RC dan perhitungan energi.",
     "JANGAN pakai rangkaian tegangan tinggi atau kapasitor dari kamera flash. Hanya ≤ 25 V.", ["webster"])
proj("defibrilator", 2, ["analisis"], "Klasifikasi ritme shockable (VF/VT)", 3, "2 minggu", ["Informatika"],
     ["sinyal", "ml-medis", "ilmu-data"],
     "Membuat pengklasifikasi ritme yang memutuskan perlu kejut atau tidak, seperti AED.",
     b("laptop"),
     ["Unduh database aritmia PhysioNet (mis. CU Ventricular Tachyarrhythmia).", "Ekstrak fitur (frekuensi dominan, kemiringan, jumlah persilangan nol).",
      "Latih model sederhana (logistic regression/random forest) dan ukur sensitivitas–spesifisitas."], "Model klasifikasi dan matriks konfusi.", "Aman.", ["pantompkins"])
proj("defibrilator", 3, ["elektroda"], "AED trainer dengan panduan suara", 1, "1 minggu", ["Desain", "Informatika"],
     ["dtk", "interaksi-pasien", "design-thinking"],
     "Membuat alat latih AED tanpa listrik kejut yang memandu langkah pertolongan dengan suara dan lampu.",
     b("nano", "buzzer", "print3d", extra=[("Modul MP3 DFPlayer Mini + speaker", 35000)]),
     ["Rekam suara panduan (pasang pad, menjauh, tekan tombol).", "Deteksi pad terpasang dengan saklar.", "Uji dengan teman dan perbaiki alurnya."],
     "AED trainer untuk edukasi masyarakat.", "Tidak ada keluaran listrik ke tubuh.", ["webster"])

# ---------------- Inkubator ----------------
proj("inkubator", 1, ["sensor", "pemanas"], "Ruang hangat dengan sensor suhu dan kelembapan", 1, "1 minggu", ["Elektrikal"],
     ["sensor", "fluida", "fisiologi"],
     "Mengukur suhu udara dan kelembapan di kotak tertutup serta memahami perpindahan panas.",
     b("nano", "dht", "ds18", "relay", extra=[("Kotak akrilik/styrofoam", 50000), ("Pemanas PTC 12 V 50 W + kipas 12 V", 45000), ("Catu daya 12 V 5 A", 75000)]),
     ["Pasang sensor di tengah dan sudut kotak.", "Nyalakan pemanas, rekam kenaikan suhu.", "Hitung waktu naik dan sebaran suhu."],
     "Data karakteristik termal kotak.", "Pakai catu 12 V; jangan tinggalkan pemanas tanpa pengawasan.", ["inkubator"])
proj("inkubator", 2, ["kontrol"], "Kendali PID suhu 36,5 °C", 2, "2 minggu", ["Elektrikal", "Informatika"],
     ["kendali", "sistem-tertanam", "kalkulus"],
     "Menjaga suhu tetap stabil dengan PID dan PWM, lalu menala parameter Kp, Ki, Kd.",
     b("nano", "relay"),
     ["Ganti relay ke MOSFET agar bisa PWM.", "Implementasi PID, mulai dari P saja lalu tambah I dan D.",
      "Ukur overshoot, waktu naik, dan error steady-state; bandingkan dengan on-off."], "Grafik respons PID vs on-off.", "Batasi suhu maksimum 38 °C di perangkat lunak.", ["inkubator", "inkubator2"])
proj("inkubator", 3, ["alarm"], "Pemantauan jarak jauh dan alarm", 2, "1 minggu", ["Informatika", "Desain"],
     ["iot", "tek-keperawatan", "dtk"],
     "Mengirim suhu/kelembapan ke dasbor dan memberi alarm bila keluar rentang aman.",
     b("esp32", "buzzer"),
     ["Kirim data ke dasbor (MQTT/Google Sheets).", "Buat alarm suhu tinggi/rendah dan sensor lepas.", "Rancang tata letak panel depan yang mudah dibaca perawat."],
     "Dasbor inkubator.", "Aman.", ["inkubator"])

# ---------------- Hemodialisis ----------------
proj("hemodialisis", 1, ["dialisat"], "Monitor konduktivitas dan suhu dialisat", 2, "1 minggu", ["Elektrikal"],
     ["kimia", "sensor", "fisiologi"],
     "Memahami kenapa konsentrasi elektrolit dialisat dipantau lewat konduktivitas dan suhu.",
     b("nano", "ds18", "oled", extra=[("Sensor EC analog (DFRobot/klon)", 120000), ("Garam dapur + gelas ukur", 15000)]),
     ["Buat larutan NaCl beberapa konsentrasi.", "Kalibrasi EC dan kompensasi suhu.", "Plot konduktivitas vs konsentrasi, cari rentang linear."],
     "Kurva kalibrasi konduktivitas.", "Aman.", ["ec"])
proj("hemodialisis", 2, ["pompadarah", "uf"], "Pompa peristaltik dengan kendali laju", 2, "1–2 minggu", ["Elektrikal"],
     ["kendali", "fluida", "sistem-tertanam"],
     "Mengatur laju aliran pompa peristaltik (analogi pompa darah) dan menghitung volume ultrafiltrasi.",
     b("nano", "relay", "oled", extra=[("Pompa peristaltik 12 V", 75000), ("Timbangan digital dapur", 60000)]),
     ["Kalibrasi laju (mL/menit) terhadap PWM.", "Ukur akurasi dengan timbangan.", "Buat mode laju konstan dan hitung volume total."],
     "Pompa terkalibrasi.", "Hanya air.", ["syringe"])
proj("hemodialisis", 3, ["pengaman"], "Detektor gelembung udara dan kebocoran", 2, "1 minggu", ["Elektrikal", "Informatika"],
     ["sensor", "k3", "pemrograman"],
     "Membuat detektor gelembung pada selang (optik/ultrasonik) yang menghentikan pompa, seperti air detector mesin HD.",
     b("nano", "buzzer", extra=[("Sensor IR celah/optocoupler", 10000)]),
     ["Pasang sensor di selang transparan.", "Bedakan sinyal cairan vs gelembung.", "Hubungkan ke pompa tahap 2: berhenti + alarm."],
     "Sistem pengaman gelembung.", "Aman.", ["ec"])

# ---------------- EEG ----------------
proj("eeg", 1, ["elektroda", "frontend", "penguat"], "Merekam gelombang alfa dengan BioAmp EXG Pill", 2, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "fisiologi", "anatomi", "sensor"],
     "Melihat ritme alfa (8–12 Hz) yang muncul saat mata terpejam.",
     b("nano", "bb", "powerbank", extra=[("BioAmp EXG Pill + kabel + elektroda gel", 220000), ("Pasta konduktif/gel EEG", 50000)]),
     ["Pasang elektroda di Fp1/O1 dengan referensi di mastoid/telinga.", "Rekam 30 detik mata terbuka dan 30 detik mata tertutup.",
      "Bandingkan amplitudo; EEG ±10–100 µV jauh lebih kecil dari EKG."], "Rekaman EEG dua kondisi.", BIO_SAFE, ["bioamp"])
proj("eeg", 2, ["filter", "komputer"], "Analisis spektrum dan pita EEG", 2, "1 minggu", ["Informatika"],
     ["sinyal", "pemrograman", "statistika"],
     "Menghitung daya pita delta, theta, alfa, beta dengan metode Welch.",
     b("laptop"),
     ["Filter 1–40 Hz dan notch 50 Hz.", "Hitung PSD (scipy.signal.welch).", "Bandingkan daya alfa mata terbuka vs tertutup, uji statistik sederhana."],
     "Grafik PSD dan tabel daya pita.", "Aman.", ["mne2"])
proj("eeg", 3, ["komputer"], "Headband EEG yang nyaman", 2, "1–2 minggu", ["Desain"],
     ["cad-medis", "purwarupa", "difabel", "biomaterial"],
     "Mendesain ikat kepala yang menahan elektroda kering dengan tekanan cukup tanpa sakit.",
     b("print3d", extra=[("Elastis/strap kain + velcro", 25000), ("Elektroda kering/finger electrode", 80000)]),
     ["Ukur lingkar kepala 3 orang.", "Desain dudukan elektroda yang bisa disetel.", "Uji kenyamanan 15 menit dan kualitas sinyal."],
     "Prototipe headband dan catatan uji.", BIO_SAFE, ["bioamp"])

# ---------------- qEEG / brain mapping ----------------
proj("brainmapping", 1, ["rekam", "praproses"], "Pra-proses EEG multikanal dengan MNE-Python", 2, "1 minggu", ["Informatika"],
     ["sinyal", "pemrograman", "manajemen-data"],
     "Membersihkan EEG dari kedip dan derau dengan filter dan ICA.",
     b("laptop"),
     ["Muat dataset contoh MNE (sample/eegbci).", "Filter, re-referensi rata-rata, tandai kanal buruk.", "Jalankan ICA dan buang komponen kedip."],
     "Notebook pra-proses EEG.", "Aman.", ["mne2"])
proj("brainmapping", 2, ["spektral", "topografi"], "Peta topografi daya alfa/theta", 2, "1 minggu", ["Informatika"],
     ["sinyal", "visualisasi", "anatomi"],
     "Membuat peta warna permukaan kepala dari daya pita tiap elektroda.",
     b("laptop"),
     ["Hitung daya pita tiap kanal.", "Gambar topomap dengan montase 10–20.", "Buat peta rasio theta/alfa seperti contoh naplib."],
     "Peta topografi qEEG.", "Aman.", ["mne", "mne2"])
proj("brainmapping", 3, ["laporan"], "Z-score terhadap data normatif", 3, "1–2 minggu", ["Informatika"],
     ["statistika", "ilmu-data", "metopen"],
     "Membandingkan satu subjek dengan kelompok referensi memakai Z-score dan membahas keterbatasannya.",
     b("laptop"),
     ["Gunakan beberapa subjek dataset sebagai kelompok normatif.", "Hitung rerata/simpangan per kanal-pita, lalu Z-score subjek uji.",
      "Tulis laporan otomatis (PDF/HTML) dengan peta Z."], "Laporan qEEG otomatis.", "Aman. Bukan untuk diagnosis.", ["mne"])

# ---------------- Neurofeedback ----------------
proj("neurofeedback", 1, ["sensor", "akuisisi"], "Streaming EEG real-time ke Python", 2, "1 minggu", ["Informatika", "Elektrikal"],
     ["sistem-tertanam", "pemrograman", "kdm"],
     "Mengirim data EEG dari mikrokontroler ke Python secara real-time dengan buffer dan timestamp.",
     b("nano", "powerbank", extra=[("BioAmp EXG Pill + elektroda", 220000)]),
     ["Kirim sampel 250 Hz lewat serial dengan format biner.", "Terima di Python dengan buffer cincin.", "Ukur latensi dan sampel yang hilang."],
     "Pipeline streaming EEG.", BIO_SAFE, ["brainflow", "bioamp"])
proj("neurofeedback", 2, ["ekstraksi", "umpan"], "Game neurofeedback alfa", 2, "1–2 minggu", ["Informatika", "Desain"],
     ["sinyal", "pemrograman", "interaksi-pasien"],
     "Membuat permainan sederhana yang bergerak saat daya alfa naik (relaksasi).",
     b("laptop"),
     ["Hitung daya alfa jendela 1 detik dengan overlap.", "Normalisasi terhadap baseline 1 menit.", "Gerakkan objek di pygame sesuai skor, uji 5 sesi."],
     "Game neurofeedback dan grafik skor per sesi.", BIO_SAFE, ["nfb", "brainflow"])
proj("neurofeedback", 3, ["protokol"], "Merancang protokol sesi dan evaluasi", 2, "1 minggu", ["Desain"],
     ["metopen", "statistika", "interaksi-pasien"],
     "Menyusun protokol (durasi, ambang, jumlah sesi) dan cara mengevaluasi efeknya secara ilmiah.",
     b("laptop"),
     ["Tinjau 3 artikel protokol alfa/SMR.", "Tulis protokol dengan kelompok kontrol (sham).", "Tentukan ukuran hasil dan analisis statistik."],
     "Dokumen protokol penelitian mini.", "Aman.", ["nfb"])

# ---------------- TMS ----------------
proj("tms", 1, ["koil"], "Kumparan figure-8 dan pengukuran medan", 2, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "sensor"],
     "Membuat kumparan angka-8 arus rendah dan mengukur fokus medan magnetnya dengan sensor Hall.",
     b("nano", extra=[("Kawat email 1 mm", 60000), ("Sensor Hall SS49E", 10000), ("Catu DC 12 V terbatas arus", 60000)]),
     ["Gulung dua kumparan bersebelahan dengan arah arus berlawanan.", "Ukur medan pada grid di bawah kumparan.", "Bandingkan dengan satu kumparan bulat."],
     "Peta medan kumparan figure-8 vs bulat.", "Arus DC rendah saja. TMS sungguhan memakai ribuan volt; jangan ditiru.", ["simnibs"])
proj("tms", 2, ["navigasi"], "Simulasi medan listrik di otak dengan SimNIBS", 3, "1–2 minggu", ["Informatika"],
     ["pemrograman", "anatomi", "pencitraan"],
     "Melihat bagaimana posisi dan orientasi koil mengubah medan listrik di korteks.",
     b("laptop"),
     ["Pasang SimNIBS dan jalankan contoh head model.", "Simulasikan koil di atas korteks motorik dengan 3 orientasi.", "Bandingkan medan maksimum dan fokus."],
     "Gambar distribusi medan dan analisis.", "Aman.", ["simnibs"])
proj("tms", 3, ["kapasitor", "saklar", "kontrol"], "Simulasi rangkaian pulsa RLC TMS", 2, "1 minggu", ["Elektrikal", "Informatika"],
     ["rangkaian", "fisika-listrik-magnet", "pemrograman"],
     "Mensimulasikan pulsa bifasik dari pelepasan kapasitor ke koil (RLC) di LTspice/Python.",
     b("laptop"),
     ["Modelkan C ≈ 200 µF, L ≈ 16 µH, R kecil.", "Hitung frekuensi resonansi dan durasi pulsa.", "Bandingkan pulsa monofasik dan bifasik."],
     "Simulasi dan grafik arus koil.", "Aman (simulasi).", ["simnibs"])

# ---------------- ECT ----------------
proj("ect", 1, ["generator", "dosis"], "Generator pulsa singkat ke beban dummy", 2, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "sistem-tertanam", "rangkaian"],
     "Memahami parameter stimulus ECT (lebar pulsa, frekuensi, durasi, muatan) dengan pulsa tegangan rendah.",
     b("nano", "osilo", "res"),
     ["Bangkitkan pulsa 0,5–1 ms, 20–60 Hz dengan timer mikrokontroler.", "Ukur di beban 220 Ω dengan osiloskop.", "Hitung muatan total (mC) untuk berbagai setelan."],
     "Tabel parameter dosis.", LOAD_SAFE, ["iec60601"])
proj("ect", 2, ["impedansi"], "Pengukur impedansi elektroda", 2, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "sensor", "k3"],
     "Mengukur impedansi kontak dengan arus uji kecil sebelum stimulus, seperti uji impedansi alat ECT.",
     b("nano", "res", "oled"),
     ["Buat pembagi tegangan dengan sumber AC kecil (1 kHz).", "Ukur impedansi beberapa resistor dan elektroda gel di kulit buah.", "Tentukan batas aman impedansi."],
     "Alat uji impedansi sederhana.", LOAD_SAFE, ["iec60601"])
proj("ect", 3, ["monitor"], "Analisis durasi kejang dari EEG", 3, "1 minggu", ["Informatika"],
     ["sinyal", "ml-medis", "pemrograman"],
     "Mendeteksi awal dan akhir aktivitas kejang pada rekaman EEG publik.",
     b("laptop"),
     ["Pakai dataset EEG kejang publik (CHB-MIT di PhysioNet).", "Hitung fitur line length dan energi.", "Tentukan durasi kejang otomatis dan bandingkan anotasi."],
     "Detektor durasi kejang.", "Aman.", ["mne2"])

# ---------------- TENS ----------------
proj("tens", 1, ["osilator", "output"], "Osilator pulsa TENS di breadboard", 1, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "rangkaian", "eldig"],
     "Membangkitkan pulsa bifasik 2–100 Hz, lebar 50–250 µs, dan melihat bentuknya.",
     b("bb", "osilo", "res", extra=[("IC NE555 + transistor + trafo kecil", 25000)]),
     ["Rakit astable 555, atur frekuensi dengan potensiometer.", "Buat tahap keluaran bifasik.", "Ukur di beban 1 kΩ."],
     "Bentuk gelombang terukur.", LOAD_SAFE, ["tens"])
proj("tens", 2, ["kontrol"], "Mode TENS terprogram", 2, "1 minggu", ["Informatika", "Elektrikal"],
     ["sistem-tertanam", "pemrograman"],
     "Membuat mode konvensional, burst, dan modulasi dengan mikrokontroler dan timer otomatis 20 menit.",
     b("nano", "oled", "osilo"),
     ["Program tiga mode pulsa.", "Tampilkan mode/timer di OLED.", "Validasi tiap mode di osiloskop."],
     "Firmware TENS multi-mode.", LOAD_SAFE, ["tens"])
proj("tens", 3, ["elektroda"], "Desain unit TENS genggam", 1, "1 minggu", ["Desain"],
     ["dtk", "difabel", "interaksi-pasien"],
     "Merancang casing dengan tombol intensitas yang aman (mulai dari nol) dan panduan penempatan elektroda.",
     b("print3d"),
     ["Pelajari ergonomi tombol untuk pengguna lansia/nyeri kronis.", "Buat model CAD + label.", "Buat kartu panduan penempatan elektroda."],
     "Prototipe casing dan panduan.", "Aman.", ["iec60601"])

# ---------------- Elektroterapi ----------------
proj("stimulasi-listrik", 1, ["generator"], "Membaca EMG otot", 1, "1 minggu", ["Elektrikal"],
     ["biomekanik", "fisiologi", "elektronika-medis"],
     "Memahami sinyal otot sebelum menstimulasinya: rekam EMG saat kontraksi ringan sampai kuat.",
     b("nano", "powerbank", extra=[("Muscle BioAmp Candy/Patchy + elektroda", 180000)]),
     ["Pasang elektroda di biseps.", "Rekam EMG pada beban 0, 1, 2 kg.", "Hitung RMS dan envelope."],
     "Grafik EMG vs beban.", BIO_SAFE, ["bioamp_emg", "muscleshield"])
proj("stimulasi-listrik", 2, ["output", "kontrol"], "Pola stimulasi NMES pada beban dummy", 2, "1 minggu", ["Elektrikal", "Informatika"],
     ["sistem-tertanam", "kendali"],
     "Membuat pola on/off ramp untuk stimulasi otot (NMES) dan memverifikasinya.",
     b("nano", "osilo", "res"),
     ["Program ramp-up, on 5 s, ramp-down, off 10 s.", "Tampilkan amplitudo relatif.", "Verifikasi di osiloskop."],
     "Firmware pola NMES.", LOAD_SAFE, ["muscleshield"])
proj("stimulasi-listrik", 3, ["kontrol"], "Rehabilitasi berbasis EMG (biofeedback)", 2, "1–2 minggu", ["Informatika", "Desain"],
     ["ml-medis", "difabel", "interaksi-pasien"],
     "Membuat game latihan otot yang dikendalikan EMG untuk motivasi pasien rehabilitasi.",
     b("laptop"),
     ["Gunakan envelope EMG tahap 1 sebagai input game.", "Buat level latihan dengan target kontraksi.", "Uji kegunaan dengan 3 teman."],
     "Game rehabilitasi EMG.", BIO_SAFE, ["bioamp_emg"])

# ---------------- Diatermi SW ----------------
proj("diatermi-sw", 1, ["osilator", "tuning"], "Resonansi LC dan tuning", 2, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "rangkaian", "elektronika-medis"],
     "Memahami kenapa diatermi gelombang pendek harus di-tuning ke resonansi (27,12 MHz) memakai rangkaian LC daya rendah.",
     b("bb", "osilo", "res", extra=[("Induktor dan kapasitor variabel (trimmer)", 20000), ("Generator fungsi (pinjam lab)", 0)]),
     ["Bangun rangkaian LC seri, sapu frekuensi dari generator.", "Ukur amplitudo dan temukan frekuensi resonansi.", "Ubah C dan bandingkan dengan f = 1/(2π√LC)."],
     "Kurva resonansi.", "Daya rendah saja; jangan membangun pemancar RF daya tinggi.", ["webster"])
proj("diatermi-sw", 2, ["aplikator"], "Simulasi pemanasan jaringan", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "fluida", "biomekanik"],
     "Mensimulasikan kenaikan suhu jaringan (persamaan biopanas Pennes sederhana) untuk dosis diatermi.",
     b("laptop"),
     ["Tulis simulasi 1D lemak–otot.", "Variasikan SAR dan durasi.", "Bandingkan pemanasan kapasitif vs induktif secara kualitatif."], "Grafik profil suhu.", "Aman.", ["webster"])
proj("diatermi-sw", 3, ["kontrol"], "Timer dosis dan pengaman", 1, "1 minggu", ["Elektrikal", "Desain"],
     ["sistem-tertanam", "k3", "dtk"],
     "Membuat panel kontrol dengan timer, tombol stop darurat, dan indikator daya (beban lampu).",
     b("nano", "relay", "oled", "buzzer"),
     ["Timer 5–20 menit dengan relay ke lampu (simulasi daya).", "Tombol stop darurat yang memutus langsung.", "Desain label dan tata letak panel."],
     "Panel kontrol prototipe.", "Beban lampu 12 V saja.", ["iec60601"])

# ---------------- Diatermi MW ----------------
proj("diatermi-mw", 1, ["magnetron", "pemandu"], "Perilaku gelombang mikro dan penyerapan air", 1, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "fismed"],
     "Memahami panjang gelombang 2,45 GHz (±12 cm) dan penyerapan air dengan eksperimen aman berbasis perhitungan dan bahan ajar.",
     b("laptop"),
     ["Hitung panjang gelombang di udara dan jaringan (permitivitas).", "Pelajari cara kerja magnetron dan pemandu gelombang.", "Buat infografis perbandingan SWD vs MWD."],
     "Ringkasan visual dan perhitungan.", "Jangan membongkar magnetron/microwave oven: kapasitornya mematikan.", ["webster"])
proj("diatermi-mw", 2, ["aplikator"], "Simulasi distribusi SAR", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "kalkulus"],
     "Mensimulasikan peluruhan daya terhadap kedalaman dan membandingkan jaringan lemak/otot.",
     b("laptop"),
     ["Model P(z) = P₀·e^(−2αz).", "Gunakan nilai α untuk lemak dan otot.", "Plot kedalaman penetrasi efektif."], "Grafik SAR.", "Aman.", ["webster"])
proj("diatermi-mw", 3, ["kontrol"], "Desain panel dan alur terapi", 1, "1 minggu", ["Desain"],
     ["dtk", "interaksi-pasien", "design-thinking"],
     "Merancang alur kerja terapis: pilih area, daya, durasi, dan checklist kontraindikasi (logam, alat pacu jantung).",
     b("laptop"),
     ["Wawancara fisioterapis bila memungkinkan.", "Buat wireframe layar.", "Uji dengan skenario kontraindikasi."], "Wireframe dan checklist.", "Aman.", ["iec60601"])

# ---------------- Terapi ultrasound ----------------
proj("terapi-us", 1, ["generator", "transduser"], "Driver transduser piezo", 2, "1 minggu", ["Elektrikal"],
     ["elektronika-medis", "fisika-mekanika", "sensor"],
     "Menggerakkan transduser piezo pada frekuensi resonansinya, sebagai analogi transduser 1–3 MHz terapi.",
     b("nano", "osilo", "relay", extra=[("Modul mist maker/atomizer 1,7 MHz", 35000), ("Transduser piezo 40 kHz", 15000)]),
     ["Bangkitkan PWM 40 kHz dengan MOSFET ke piezo.", "Amati resonansi dengan mengubah frekuensi.", "Coba modul atomizer di air untuk melihat efek energi akustik."],
     "Catatan resonansi dan duty cycle.", "Jangan menempelkan transduser bertenaga ke kulit.", ["webster"])
proj("terapi-us", 2, ["kontrol"], "Mode kontinu dan pulsed dengan timer", 1, "1 minggu", ["Informatika"],
     ["sistem-tertanam", "pemrograman"],
     "Membuat mode terapi kontinu dan pulsed (duty 20/50%) serta menghitung intensitas rata-rata.",
     b("nano", "oled"),
     ["Program duty cycle dan timer.", "Hitung intensitas temporal average dari intensitas puncak.", "Tampilkan sisa waktu dan mode."], "Firmware mode terapi.", "Aman.", ["webster"])
proj("terapi-us", 3, ["aplikasi"], "Desain applicator head yang ergonomis", 1, "1 minggu", ["Desain"],
     ["cad-medis", "biomekanik", "purwarupa"],
     "Merancang gagang aplikator yang nyaman digenggam terapis selama 10 menit.",
     b("print3d"),
     ["Ukur genggaman tangan beberapa orang.", "Buat 2 varian gagang di CAD.", "Uji kenyamanan dan pilih desain."], "Prototipe gagang.", "Aman.", ["brace2"])

# ---------------- Brace ----------------
proj("brace-skoliosis", 1, ["ukur"], "Mengukur sudut Cobb dari citra", 1, "1 minggu", ["Informatika"],
     ["anatomi", "biomekanik", "citra", "pemrograman"],
     "Menghitung sudut Cobb dari radiograf tulang belakang secara semi-otomatis.",
     b("laptop"),
     ["Ambil contoh citra skoliosis dari literatur terbuka.", "Buat alat klik 4 titik untuk menggambar garis endplate.", "Hitung sudut Cobb dan bandingkan antar-pengamat."],
     "Alat ukur sudut Cobb.", "Aman.", ["brace"])
proj("brace-skoliosis", 2, ["desain", "fabrikasi"], "Brace dari pindaian 3D tubuh", 2, "2 minggu", ["Desain"],
     ["cad-medis", "purwarupa", "difabel", "biomaterial"],
     "Memindai torso (manekin) dengan fotogrametri ponsel, lalu mendesain shell brace dan mencetak versi skala kecil.",
     b("laptop", "print3d"),
     ["Pindai manekin dengan aplikasi fotogrametri.", "Bersihkan mesh di Meshmixer/Blender.", "Buat shell offset 3–4 mm, tambahkan ventilasi, cetak skala 1:4."],
     "Model brace skala.", "Aman.", ["brace", "brace2"])
proj("brace-skoliosis", 3, ["bantalan", "evaluasi"], "Sensor tekanan bantalan brace", 2, "1 minggu", ["Elektrikal", "Informatika"],
     ["sensor", "iot", "biomekanik"],
     "Memantau gaya koreksi dan lama pemakaian brace dengan sensor FSR.",
     b("esp32", extra=[("Sensor gaya FSR402 ×3", 60000)]),
     ["Kalibrasi FSR dengan beban.", "Catat tekanan dan durasi pakai per hari.", "Kirim ringkasan ke ponsel."], "Logger kepatuhan pakai brace.", "Aman.", ["brace"])

# ---------------- Termometer ----------------
proj("termometer", 1, ["sensor", "pengondisi", "adc"], "Termometer termistor dan kalibrasi", 1, "3 hari", ["Elektrikal"],
     ["sensor", "elektronika-medis", "fisika-mekanika"],
     "Mengubah resistansi NTC menjadi suhu dengan persamaan Steinhart–Hart dan mengkalibrasinya.",
     b("nano", "bb", "oled", extra=[("Termistor NTC 10 kΩ", 5000), ("Termometer acuan", 30000)]),
     ["Rangkai pembagi tegangan NTC.", "Kalibrasi di air es, suhu ruang, dan air hangat.", "Hitung koefisien dan galat."],
     "Termometer terkalibrasi.", "Aman.", ["mlx"])
proj("termometer", 2, ["sensor", "mcu", "tampilan"], "Termometer dahi inframerah", 1, "1 minggu", ["Elektrikal", "Desain"],
     ["sensor", "sistem-tertanam", "cad-medis"],
     "Membuat termometer non-kontak dengan MLX90614 dan casing pistol.",
     b("nano", "oled", "batt", "print3d", extra=[("Sensor MLX90614", 90000)]),
     ["Baca suhu objek dan ambien.", "Uji pengaruh jarak 1–10 cm.", "Desain casing pistol dengan tombol picu."],
     "Termometer IR genggam.", "Aman.", ["mlx"])
proj("termometer", 3, ["mcu"], "Pencatat demam ke aplikasi", 1, "1 minggu", ["Informatika"],
     ["mobile", "manajemen-data", "iot"],
     "Mencatat suhu beberapa orang dan menandai demam (≥ 37,5 °C).",
     b("esp32"),
     ["Kirim hasil ke Google Sheets/Firebase.", "Tampilkan riwayat per orang.", "Hitung statistik sederhana."], "Aplikasi log suhu.", "Aman.", ["mlx"])

# ---------------- Glukometer ----------------
proj("glukometer", 1, ["strip", "potensiostat"], "Potensiostat sederhana", 3, "2 minggu", ["Elektrikal"],
     ["kimia", "elektronika-medis", "elda"],
     "Memahami prinsip amperometri: menjaga beda potensial dan mengukur arus dari reaksi enzim glukosa oksidase.",
     b("nano", "bb", "res", extra=[("Op-amp rail-to-rail (MCP6002) ×2", 15000), ("Elektroda/strip uji atau elektroda grafit pensil", 20000)]),
     ["Pelajari rangkaian CheapStat.", "Rakit potensiostat 2 elektroda + penguat transimpedansi.", "Uji dengan larutan kalium ferisianida/vitamin C berbagai konsentrasi."],
     "Kurva arus vs konsentrasi.", "Gunakan bahan kimia rumah tangga yang aman; pakai sarung tangan.", ["cheapstat"])
proj("glukometer", 2, ["algoritma", "adc"], "Kurva kalibrasi dan akurasi (Clarke error grid)", 2, "1 minggu", ["Informatika"],
     ["statistika", "pemrograman", "kimia"],
     "Mengubah arus menjadi mg/dL dan mengevaluasi akurasi dengan Clarke error grid.",
     b("laptop"),
     ["Buat regresi arus–konsentrasi.", "Hitung MARD (mean absolute relative difference).", "Plot Clarke error grid dari data contoh."],
     "Notebook evaluasi akurasi.", "Aman.", ["cheapstat"])
proj("glukometer", 3, ["tampilan"], "Aplikasi diabetes log", 1, "1 minggu", ["Informatika", "Desain"],
     ["mobile", "interaksi-pasien", "dtk"],
     "Merancang aplikasi pencatat gula darah yang memudahkan pasien melihat tren.",
     b("laptop"),
     ["Buat persona pasien diabetes.", "Wireframe dan prototipe (Figma/Flutter).", "Uji 3 pengguna."], "Prototipe aplikasi.", "Aman.", ["cheapstat"])

# ---------------- Kimia klinik ----------------
proj("kimia-klinik", 1, ["fotometer"], "Fotometer LED (hukum Beer–Lambert)", 1, "1 minggu", ["Elektrikal"],
     ["kimia", "sensor", "fisika-listrik-magnet"],
     "Membangun kolorimeter untuk mengukur absorbansi larutan berwarna.",
     b("nano", "bb", "oled", "print3d", extra=[("LED RGB + fotodioda/TSL2561", 40000), ("Kuvet plastik 10 mm", 20000)]),
     ["Cetak dudukan kuvet kedap cahaya.", "Ukur intensitas blanko dan sampel.", "Hitung A = log10(I₀/I) untuk seri pewarna makanan."],
     "Kolorimeter dan kurva standar.", "Aman.", ["colorimeter", "colorimeter2"])
proj("kimia-klinik", 2, ["kuvet"], "Inkubasi 37 °C dan kinetika reaksi", 2, "1 minggu", ["Elektrikal", "Informatika"],
     ["kendali", "kimia", "pemrograman"],
     "Menjaga kuvet di 37 °C dan merekam perubahan absorbansi terhadap waktu (pengukuran kinetik).",
     b("nano", "ds18", "relay", extra=[("Blok aluminium + resistor pemanas", 25000)]),
     ["Pasang pemanas + PID di blok kuvet.", "Rekam absorbansi tiap 5 detik.", "Hitung laju ΔA/menit."], "Grafik kinetik.", "Aman.", ["colorimeter"])
proj("kimia-klinik", 3, ["lis"], "Kirim hasil ke sistem informasi lab", 2, "1 minggu", ["Informatika"],
     ["manajemen-data", "kdm", "simrs"],
     "Membuat format hasil (ID sampel, parameter, nilai, satuan, flag) dan mengirimnya ke basis data.",
     b("esp32"),
     ["Rancang skema tabel hasil lab.", "Kirim JSON ke server lokal (Flask/SQLite).", "Beri flag nilai di luar rentang rujukan."], "Mini LIS.", "Aman.", ["lfa"])

# ---------------- Koagulasi ----------------
proj("koagulasi", 1, ["deteksi"], "Deteksi perubahan kekeruhan (turbidimetri)", 2, "1 minggu", ["Elektrikal"],
     ["sensor", "kimia", "biologi-kedokteran"],
     "Mendeteksi titik pembekuan dari perubahan kekeruhan, memakai analogi gelatin/susu + cuka.",
     b("nano", "oled", extra=[("LED IR + fotodioda", 15000), ("Kuvet + bahan simulasi", 20000)]),
     ["Rekam transmisi cahaya saat larutan mulai menggumpal.", "Tentukan waktu ambang perubahan.", "Ulangi 5× dan hitung CV."],
     "Pengukur waktu 'beku' optik.", "Aman.", ["ptsensor"])
proj("koagulasi", 2, ["inkubasi"], "Pemanas 37 °C dan timer otomatis", 1, "1 minggu", ["Elektrikal"],
     ["kendali", "sistem-tertanam"],
     "Membuat blok inkubasi dan timer yang mulai saat reagen ditambahkan.",
     b("nano", "ds18", "relay", "buzzer"), ["PID suhu blok.", "Tombol start = penambahan reagen.", "Timer berhenti otomatis dari tahap 1."],
     "Blok inkubasi bertimer.", "Aman.", ["ptsensor"])
proj("koagulasi", 3, ["hasil"], "Menghitung INR dan kontrol mutu", 1, "3 hari", ["Informatika"],
     ["statistika", "pemrograman"],
     "Menghitung INR = (PT pasien / PT normal)^ISI dan membuat grafik Levey–Jennings untuk kontrol mutu.",
     b("laptop"), ["Buat fungsi INR.", "Simulasikan data kontrol harian.", "Tandai pelanggaran aturan Westgard."], "Notebook INR + QC.", "Aman.", ["ptsensor"])

# ---------------- CAT ----------------
proj("cat", 1, ["sentrifus"], "Sentrifus kartu dengan motor", 2, "1 minggu", ["Elektrikal", "Desain"],
     ["fisika-mekanika", "kendali", "cad-medis"],
     "Membuat dudukan kartu gel yang diputar dengan kecepatan terkendali dan mengukur RPM.",
     b("nano", "print3d", extra=[("Motor DC brushless/kipas + ESC", 90000), ("Sensor Hall/IR untuk RPM", 10000)]),
     ["Desain rotor kartu seimbang.", "Ukur RPM, hitung RCF = 1,118×10⁻⁵·r·RPM².", "Tambah tutup pengaman."], "Sentrifus kartu mini.", "Wajib tutup pengaman dan seimbangkan rotor.", ["paperfuge"])
proj("cat", 2, ["pembaca"], "Pembaca kartu gel dengan kamera", 2, "1–2 minggu", ["Informatika"],
     ["citra", "ml-medis", "pemrograman"],
     "Mengklasifikasi pola aglutinasi (0 sampai 4+) dari foto kolom gel.",
     b("laptop", extra=[("Webcam/kamera ponsel + kotak lampu", 50000)]),
     ["Kumpulkan contoh gambar pola (dari literatur/brosur).", "Ekstrak profil intensitas sepanjang kolom.", "Buat aturan/klasifikasi sederhana."],
     "Pembaca pola gel.", "Aman.", ["lfa"])
proj("cat", 3, ["inkubator"], "Alur kerja golongan darah yang aman", 1, "3 hari", ["Desain"],
     ["tek-medik", "design-thinking"],
     "Memetakan alur uji crossmatch dan titik rawan salah identifikasi, lalu mengusulkan barcode.",
     b("laptop"), ["Gambar alur kerja.", "Identifikasi risiko (FMEA sederhana).", "Usulkan desain label barcode."], "Peta alur + FMEA.", "Aman.", ["lfa"])

# ---------------- Elektrolit ----------------
proj("elektrolit", 1, ["ise", "referensi", "penguat"], "Pengukuran potensial ISE (pH meter)", 2, "1 minggu", ["Elektrikal"],
     ["kimia", "elda", "sensor"],
     "Memahami persamaan Nernst dan penguat impedansi masukan tinggi memakai elektroda pH (sejenis ISE).",
     b("nano", "oled", extra=[("Modul sensor pH + elektroda", 150000), ("Larutan buffer pH 4/7/10", 45000)]),
     ["Kalibrasi 2 titik.", "Hitung kemiringan mV/pH dan bandingkan 59,16 mV pada 25 °C.", "Ukur beberapa larutan rumah tangga."], "Kurva Nernst.", "Aman.", ["ec"])
proj("elektrolit", 2, ["fluida"], "Sistem fluidik: pompa sampel dan bilas", 2, "1 minggu", ["Elektrikal", "Desain"],
     ["fluida", "kendali", "purwarupa"],
     "Mengotomatiskan urutan isap sampel → ukur → bilas dengan pompa peristaltik dan katup.",
     b("nano", "relay", extra=[("Pompa peristaltik 12 V", 75000), ("Selang silikon + konektor", 20000)]),
     ["Rancang urutan langkah.", "Kendalikan pompa dengan waktu terkalibrasi.", "Uji pembilasan antar-sampel (carry-over)."], "Fluidik otomatis.", "Aman.", ["ec"])
proj("elektrolit", 3, ["mcu"], "Kompensasi suhu dan laporan Na/K/Cl", 1, "3 hari", ["Informatika"],
     ["pemrograman", "statistika"],
     "Mengoreksi pembacaan terhadap suhu dan menyusun laporan dengan rentang rujukan.",
     b("laptop"), ["Implementasi koreksi suhu Nernst.", "Simulasikan data Na/K/Cl.", "Tandai hipo/hiper."], "Laporan otomatis.", "Aman.", ["ec"])

# ---------------- Hematologi ----------------
proj("hematologi", 1, ["impedansi"], "Prinsip Coulter: perubahan impedansi", 2, "1 minggu", ["Elektrikal"],
     ["fisika-listrik-magnet", "biologi-kedokteran", "elda"],
     "Memahami penghitungan sel dengan perubahan impedansi saat partikel melewati celah kecil (simulasi dengan pipet dan larutan garam).",
     b("nano", "osilo", "res", extra=[("Pipet + elektroda kawat + larutan garam", 15000)]),
     ["Buat celah kecil di ujung pipet dengan dua elektroda.", "Lewatkan partikel (biji kecil/serbuk) dan amati pulsa.", "Hubungkan tinggi pulsa dengan ukuran partikel."],
     "Demonstrasi prinsip Coulter.", "Tegangan rendah saja.", ["webster"])
proj("hematologi", 2, ["flow", "analisis"], "Menghitung sel darah dari citra mikroskop", 2, "1 minggu", ["Informatika"],
     ["citra", "pemrograman", "biologi-kedokteran"],
     "Menghitung dan mengklasifikasi sel dari citra apusan dengan OpenCV.",
     b("laptop"), ["Gunakan dataset sel darah terbuka.", "Segmentasi (threshold + watershed) dan hitung sel.", "Bedakan WBC dan RBC dari warna/ukuran."],
     "Penghitung sel otomatis.", "Aman.", ["cellcount", "cellcount2"])
proj("hematologi", 3, ["hgb"], "Fotometer hemoglobin", 2, "1 minggu", ["Elektrikal"],
     ["kimia", "sensor"],
     "Mengukur konsentrasi warna merah (analogi Hb) dengan absorbansi pada 540 nm (LED hijau).",
     b("nano", "oled", extra=[("LED hijau + fotodioda + kuvet", 25000)]),
     ["Buat seri larutan pewarna merah.", "Ukur absorbansi dengan LED hijau.", "Buat kurva standar."], "Fotometer Hb mini.", "Aman.", ["colorimeter"])

# ---------------- Immunoassay ----------------
proj("immunoassay", 1, ["cahaya", "detektor"], "Deteksi fluoresensi dengan LED UV", 2, "1 minggu", ["Elektrikal"],
     ["sensor", "kimia", "fisika-listrik-magnet"],
     "Mengukur fluoresensi (eksitasi UV/biru, emisi hijau) memakai filter warna dan fotodioda.",
     b("nano", "oled", extra=[("LED UV 395 nm + fotodioda + filter gel", 35000), ("Stabilo/tonik (bahan berpendar)", 15000)]),
     ["Susun LED dan detektor 90°.", "Tambahkan filter emisi.", "Ukur seri pengenceran bahan berpendar."], "Kurva fluoresensi.", "Jangan menatap LED UV.", ["lfa"])
proj("immunoassay", 2, ["kartrid"], "Pembaca strip lateral flow dengan ponsel", 2, "1 minggu", ["Informatika"],
     ["citra", "pemrograman", "mobile"],
     "Mengukur intensitas garis tes dan kontrol dari foto strip (rasio T/C).",
     b("laptop", extra=[("Strip tes kehamilan/antigen bekas + kotak foto", 25000)]),
     ["Foto strip dengan pencahayaan tetap.", "Ambil profil intensitas sepanjang strip.", "Hitung rasio T/C."], "Pembaca strip.", "Buang strip bekas sebagai limbah medis.", ["lfa"])
proj("immunoassay", 3, ["mcu"], "Kotak baca dengan pencahayaan seragam", 1, "1 minggu", ["Desain"],
     ["cad-medis", "purwarupa"],
     "Mendesain kotak yang memposisikan kartrid dan kamera ponsel dengan cahaya seragam.",
     b("print3d"), ["Desain dudukan kartrid dan ponsel.", "Uji keseragaman cahaya.", "Iterasi 2 versi."], "Kotak baca.", "Aman.", ["lfa"])

# ---------------- Sentrifus ----------------
proj("sentrifus", 1, ["motor", "kendali"], "Kendali kecepatan dan pengukuran RPM", 1, "1 minggu", ["Elektrikal"],
     ["kendali", "fisika-mekanika", "sistem-tertanam"],
     "Mengendalikan motor dan mengukur RPM, lalu menghitung RCF (g).",
     b("nano", "oled", extra=[("Motor DC + driver/ESC", 60000), ("Sensor IR/Hall RPM", 10000)]),
     ["Ukur RPM dengan tachometer optik.", "Buat PID kecepatan.", "Hitung RCF dari jari-jari rotor."], "Pengendali sentrifus.", "Pasang tutup pelindung.", ["paperfuge2"])
proj("sentrifus", 2, ["rotor"], "Paperfuge dan analisis rotor", 1, "3 hari", ["Desain"],
     ["fisika-mekanika", "biomekanik", "purwarupa"],
     "Membuat paperfuge dari kertas dan tali, lalu menganalisis kecepatan yang dicapai dengan video ponsel slow motion.",
     b(extra=[("Karton, tali, tusuk sate", 10000)]),
     ["Buat paperfuge sesuai artikel Stanford.", "Rekam slow motion dan hitung RPM.", "Bandingkan dengan sentrifus lab."], "Laporan paperfuge.", "Aman.", ["paperfuge", "paperfuge2"])
proj("sentrifus", 3, ["pengaman"], "Deteksi ketidakseimbangan dengan akselerometer", 2, "1 minggu", ["Informatika", "Elektrikal"],
     ["sinyal", "sensor", "k3"],
     "Mendeteksi rotor tidak seimbang dari getaran dan menghentikan motor.",
     b("nano", extra=[("Akselerometer MPU6050", 25000)]),
     ["Rekam getaran seimbang vs tidak.", "Hitung RMS/FFT getaran.", "Hentikan motor bila melewati ambang."], "Pengaman getaran.", "Aman.", ["paperfuge2"])

# ---------------- Mikroskop ----------------
proj("mikroskop", 1, ["cahaya", "objektif"], "Mikroskop OpenFlexure", 2, "2–3 minggu", ["Desain", "Elektrikal"],
     ["purwarupa", "cad-medis", "fisika-mekanika"],
     "Merakit mikroskop cetak 3D dengan tahap flexure dan kamera.",
     b("print3d", extra=[("Raspberry Pi 4 + kamera Pi v2", 1100000), ("Lensa objektif/kamera + LED", 80000)]),
     ["Cetak bagian sesuai dokumentasi OpenFlexure.", "Rakit optik dan kamera.", "Ambil citra preparat."], "Mikroskop digital.", "Aman.", ["openflexure", "openflexure2"])
proj("mikroskop", 2, ["mekanik"], "Fokus otomatis berbasis ketajaman", 2, "1 minggu", ["Informatika"],
     ["citra", "pemrograman", "kendali"],
     "Mencari posisi fokus terbaik dengan metrik ketajaman (varian Laplacian).",
     b("laptop"), ["Ambil tumpukan citra pada beberapa posisi z.", "Hitung skor ketajaman.", "Gerakkan motor ke posisi maksimum."], "Algoritma autofokus.", "Aman.", ["openflexure"])
proj("mikroskop", 3, ["okuler"], "Mikroskop ponsel murah", 1, "3 hari", ["Desain"],
     ["dtk", "purwarupa"],
     "Membuat adaptor lensa untuk ponsel agar bisa memotret preparat sederhana.",
     b("print3d", extra=[("Lensa laser pointer/lensa makro", 15000)]),
     ["Desain klip lensa.", "Kalibrasi skala dengan penggaris mikro.", "Foto preparat bawang."], "Adaptor mikroskop ponsel.", "Aman.", ["openflexure2"])

# ---------------- Urin ----------------
proj("urin-analyzer", 1, ["strip", "led", "detektor"], "Pembaca warna strip urin", 1, "1 minggu", ["Elektrikal"],
     ["sensor", "kimia"],
     "Membaca warna tiap pad strip dengan sensor warna RGB.",
     b("nano", "oled", "print3d", extra=[("Sensor warna TCS34725", 50000), ("Strip urin 10 parameter (1 botol)", 60000)]),
     ["Buat dudukan strip yang bergeser per pad.", "Baca RGB tiap pad.", "Bandingkan dengan bagan warna di botol."], "Pembaca strip.", "Gunakan larutan uji, bukan urin orang lain.", ["tcs", "tcs2"])
proj("urin-analyzer", 2, ["mcu"], "Klasifikasi warna ke kategori hasil", 2, "1 minggu", ["Informatika"],
     ["ml-medis", "pemrograman"],
     "Memetakan RGB ke kategori (negatif, +1, +2…) dengan k-nearest neighbors.",
     b("laptop"), ["Kumpulkan data RGB dari bagan referensi.", "Latih KNN.", "Uji dengan larutan buatan."], "Model klasifikasi warna.", "Aman.", ["tcs"])
proj("urin-analyzer", 3, ["output"], "Laporan urinalisis untuk pasien", 1, "3 hari", ["Desain", "Informatika"],
     ["interaksi-pasien", "manajemen-data"],
     "Menyajikan hasil dengan bahasa yang mudah dipahami dan rentang normal.",
     b("laptop"), ["Desain template laporan.", "Generate PDF dari data.", "Uji keterbacaan."], "Template laporan.", "Aman.", ["tcs"])

# ---------------- BrainWave (fMRI) ----------------
proj("brainwave", 1, ["data", "koreksi"], "Membaca dan memeriksa data fMRI", 2, "1 minggu", ["Informatika"],
     ["pemrograman", "manajemen-data", "pencitraan"],
     "Membuka data NIfTI, memahami dimensi 4D (x, y, z, waktu), dan memeriksa kualitas.",
     b("laptop"), ["Pasang nibabel dan nilearn.", "Muat dataset contoh nilearn.", "Plot irisan dan time series satu voxel."], "Notebook eksplorasi fMRI.", "Aman.", ["nipype"])
proj("brainwave", 2, ["statistik", "peta"], "GLM sederhana untuk peta aktivasi", 3, "2 minggu", ["Informatika"],
     ["statistika", "ilmu-data", "sinyal"],
     "Membuat peta aktivasi dari desain blok dengan general linear model.",
     b("laptop"), ["Buat regressor tugas dikonvolusi HRF.", "Fit GLM per voxel (nilearn).", "Threshold peta-z dan tampilkan di atas anatomi."], "Peta aktivasi.", "Aman.", ["nipype"])
proj("brainwave", 3, ["fusi"], "Fusi peta fMRI ke citra anatomi", 2, "1 minggu", ["Informatika", "Desain"],
     ["visualisasi", "citra"],
     "Menampilkan peta fungsional di atas MRI anatomi dan membuat tampilan yang mudah dibaca dokter.",
     b("laptop"), ["Registrasi fungsional–anatomi.", "Overlay dengan colormap.", "Rancang tata letak laporan."], "Tampilan fusi.", "Aman.", ["slicer"])

# ---------------- Motion correction ----------------
proj("motion-correction", 1, ["estimasi", "transformasi"], "Registrasi rigid dua citra", 2, "1 minggu", ["Informatika"],
     ["citra", "kalkulus", "pemrograman"],
     "Mengestimasi translasi dan rotasi antar dua citra dengan optimasi.",
     b("laptop"), ["Buat citra tergeser buatan.", "Implementasi registrasi rigid (scikit-image/SimpleITK).", "Ukur galat parameter."], "Notebook registrasi.", "Aman.", ["mcflirt"])
proj("motion-correction", 2, ["akuisisi", "resampling", "evaluasi"], "Koreksi gerak seri fMRI dengan MCFLIRT", 3, "1–2 minggu", ["Informatika"],
     ["pencitraan", "statistika"],
     "Menjalankan MCFLIRT, membaca 6 parameter gerak, dan menghitung framewise displacement.",
     b("laptop"), ["Jalankan MCFLIRT lewat Nipype.", "Plot parameter gerak.", "Tandai volume dengan FD > 0,5 mm."], "Laporan kualitas gerak.", "Aman.", ["mcflirt", "nipype"])
proj("motion-correction", 3, ["evaluasi"], "Penanda gerak kepala dengan IMU", 2, "1 minggu", ["Elektrikal", "Desain"],
     ["sensor", "sistem-tertanam", "cad-medis"],
     "Merekam gerak kepala selama 'pemindaian' tiruan dengan IMU di ikat kepala untuk membandingkan dengan estimasi citra.",
     b("esp32", "print3d", extra=[("IMU MPU6050", 25000)]),
     ["Pasang IMU di headband.", "Rekam rotasi saat berbaring.", "Bandingkan pola dengan parameter dari tahap 2."], "Logger gerak kepala.", "Aman.", ["mcflirt"])


def get():
    return P
