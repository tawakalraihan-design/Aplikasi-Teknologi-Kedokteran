# -*- coding: utf-8 -*-
"""Bank soal penerapan alat (v1.2).

Tipe: pg (pilihan ganda, jawab = indeks opsi), bs (benar/salah), kasus (pilihan
ganda berbentuk skenario klinis/teknis), cocok (pasangan kiri-kanan), urut
(urutan benar). Soal otomatis tambahan (urutan blok, fungsi blok, mata kuliah
per blok) dibuat aplikasi dari data alat, jadi tidak ditulis di sini.
"""

S = []


def pg(alat, tanya, opsi, jawab, bahas, tipe="pg"):
    S.append({"alat": alat, "tipe": tipe, "tanya": tanya, "opsi": opsi, "jawab": jawab, "bahas": bahas})


def kasus(alat, tanya, opsi, jawab, bahas):
    pg(alat, tanya, opsi, jawab, bahas, "kasus")


def bs(alat, tanya, jawab, bahas):
    S.append({"alat": alat, "tipe": "bs", "tanya": tanya, "jawab": jawab, "bahas": bahas})


def cocok(alat, tanya, pasangan, bahas):
    S.append({"alat": alat, "tipe": "cocok", "tanya": tanya, "pasangan": pasangan, "bahas": bahas})


def urut(alat, tanya, item, bahas):
    S.append({"alat": alat, "tipe": "urut", "tanya": tanya, "item": item, "bahas": bahas})


# ---------------- EKG ----------------
kasus("ekg", "Rekaman EKG pasien menunjukkan getaran halus teratur yang menumpang di seluruh sinyal. Frekuensinya 50 Hz. Penyebab paling mungkin?",
      ["Interferensi jala-jala listrik", "Artefak gerak pernapasan", "Elektroda kehabisan gel", "Fibrilasi atrium"], 0,
      "50 Hz adalah frekuensi jala-jala PLN. Solusinya: penguat dengan CMRR tinggi, elektroda RL (driven right leg), dan filter notch 50 Hz.")
pg("ekg", "Kenapa EKG memakai penguat instrumentasi, bukan penguat biasa?",
   ["Karena CMRR tinggi menolak sinyal bersama (derau) dan menguatkan beda potensial", "Karena penguat instrumentasi lebih murah",
    "Karena sinyal EKG berupa arus besar", "Karena penguat biasa tidak bisa memakai baterai"], 0,
   "Sinyal jantung adalah beda potensial kecil antar-elektroda, sedangkan derau muncul sama di semua elektroda. Penguat instrumentasi menguatkan selisih dan menolak sinyal bersama.")
pg("ekg", "Rentang frekuensi yang umum dipakai filter EKG monitoring adalah…",
   ["0,5–40 Hz", "100–500 Hz", "1–3 MHz", "8–12 Hz"], 0,
   "Mode monitoring memakai 0,5–40 Hz agar garis dasar stabil dan derau otot berkurang. Mode diagnostik memakai rentang lebih lebar (0,05–150 Hz).")
bs("ekg", "Garis dasar EKG yang naik-turun pelan (baseline wander) biasanya disebabkan pernapasan dan bisa dikurangi dengan high-pass filter.", True,
   "Pernapasan menggeser garis dasar pada frekuensi < 0,5 Hz, sehingga high-pass 0,5 Hz membuangnya.")
cocok("ekg", "Cocokkan gelombang EKG dengan kejadian listrik di jantung.",
      [["Gelombang P", "Depolarisasi atrium"], ["Kompleks QRS", "Depolarisasi ventrikel"], ["Gelombang T", "Repolarisasi ventrikel"], ["Interval PR", "Konduksi melalui nodus AV"]],
      "Bentuk gelombang EKG adalah gambaran urutan aktivasi listrik jantung, yang dipelajari di Fisiologi Kedokteran.")
kasus("ekg", "Detak dihitung dari jarak R ke R. Jika jarak RR rata-rata 0,75 detik, berapa detak jantungnya?",
      ["80 bpm", "75 bpm", "60 bpm", "133 bpm"], 0, "BPM = 60 / RR = 60 / 0,75 = 80.")

# ---------------- Oksimeter ----------------
pg("oksimeter", "Kenapa pulse oximeter memakai dua panjang gelombang (merah dan inframerah)?",
   ["Hemoglobin beroksigen dan tidak beroksigen menyerap kedua cahaya secara berbeda", "Satu untuk siang, satu untuk malam",
    "Inframerah mengukur suhu", "Agar baterai lebih awet"], 0,
   "HbO₂ menyerap lebih banyak IR, Hb lebih banyak merah. Rasio penyerapan keduanya menentukan saturasi.")
kasus("oksimeter", "Pasien dengan tangan sangat dingin memperoleh bacaan SpO₂ tidak stabil. Penyebab paling mungkin?",
      ["Perfusi perifer rendah sehingga komponen AC lemah", "Kadar gula darah tinggi", "Baterai terlalu penuh", "LED terlalu terang"], 0,
      "SpO₂ dihitung dari komponen pulsatil (AC). Vasokonstriksi membuat AC kecil sehingga rasio R tidak andal.")
bs("oksimeter", "Kuku cat gelap dan cahaya ruangan kuat dapat mengganggu pembacaan pulse oximeter.", True,
   "Cat menyerap cahaya dan cahaya ambien menambah derau di fotodioda. Klip yang tertutup rapat membantu.")
pg("oksimeter", "Blok TIA (transimpedance amplifier) pada oksimeter berfungsi…",
   ["Mengubah arus fotodioda menjadi tegangan", "Menyalakan LED bergantian", "Menghitung SpO₂", "Mengisi baterai"], 0,
   "Fotodioda menghasilkan arus kecil sebanding cahaya. TIA mengubahnya menjadi tegangan agar bisa dibaca ADC.")
urut("oksimeter", "Urutkan alur sinyal pulse oximeter.",
     ["LED merah/IR", "Jaringan jari", "Fotodioda", "Penguat TIA", "ADC", "Algoritma rasio R", "Tampilan SpO₂"],
     "Cahaya melewati jaringan, diterima fotodioda, dikuatkan, didigitalkan, lalu dihitung.")

# ---------------- Tensimeter ----------------
pg("tensimeter", "Pada metode osilometrik, tekanan arteri rata-rata (MAP) ditentukan pada saat…",
   ["Amplitudo osilasi manset maksimum", "Bunyi Korotkoff pertama terdengar", "Manset dipompa penuh", "Osilasi hilang"], 0,
   "Osilasi terbesar terjadi pada MAP; sistolik dan diastolik diperkirakan dengan rasio amplitudo karakteristik.")
kasus("tensimeter", "Hasil tensi seorang pasien bertubuh besar selalu terlalu tinggi. Apa yang paling perlu diperiksa?",
      ["Ukuran manset terlalu kecil untuk lingkar lengannya", "Kadar oksigen darah", "Suhu ruangan", "Baterai alat terlalu baru"], 0,
      "Manset yang terlalu kecil memerlukan tekanan lebih tinggi untuk menutup arteri sehingga hasil terbaca lebih tinggi.")
bs("tensimeter", "1 kPa kira-kira sama dengan 7,5 mmHg.", True, "1 kPa = 7,50062 mmHg.")
pg("tensimeter", "Fitur keselamatan wajib pada tensimeter otomatis adalah…",
   ["Pembatas tekanan maksimum dan katup buang otomatis", "Lampu kilat", "Koneksi Wi-Fi", "Speaker stereo"], 0,
   "Tekanan berlebih atau terlalu lama bisa melukai lengan, jadi harus ada pembatas tekanan dan waktu.")

# ---------------- USG ----------------
pg("usg", "Kedalaman pantulan dihitung dengan d = c·t/2. Kenapa dibagi 2?",
   ["Gelombang menempuh jalan pergi dan pulang", "Karena ada dua kristal piezo", "Agar satuan menjadi cm", "Karena kecepatan suara berkurang setengah"], 0,
   "Waktu t adalah waktu bolak-balik, jadi jarak satu arah adalah setengahnya.")
kasus("usg", "Sonografer menaikkan frekuensi probe dari 3,5 MHz ke 10 MHz. Apa akibatnya?",
      ["Resolusi lebih tajam tetapi penetrasi lebih dangkal", "Penetrasi lebih dalam dan resolusi lebih buruk", "Tidak ada perubahan", "Citra menjadi berwarna"], 0,
      "Frekuensi tinggi memberi panjang gelombang pendek (resolusi baik) tetapi atenuasi lebih besar.")
bs("usg", "Gel USG dipakai untuk menghilangkan udara antara probe dan kulit karena udara memantulkan hampir semua gelombang ultrasonik.", True,
   "Beda impedansi akustik udara-jaringan sangat besar, sehingga hampir semua energi terpantul tanpa gel.")
pg("usg", "Fungsi time gain compensation (TGC) adalah…",
   ["Menguatkan gema dari kedalaman lebih besar untuk mengimbangi atenuasi", "Mengatur waktu pemeriksaan", "Mengubah frekuensi probe", "Menyimpan citra"], 0,
   "Gema dari dalam lebih lemah, jadi penguatan dinaikkan seiring waktu tiba gema.")
cocok("usg", "Cocokkan mode USG dengan tampilannya.",
      [["A-mode", "Amplitudo gema vs kedalaman"], ["B-mode", "Citra 2D skala abu-abu"], ["M-mode", "Gerak struktur terhadap waktu"], ["Doppler", "Kecepatan aliran darah"]],
      "Mode-mode ini memakai sinyal gema yang sama dengan cara penyajian berbeda.")

# ---------------- X-ray ----------------
pg("xray", "Menaikkan kVp pada tabung sinar-X terutama akan…",
   ["Meningkatkan energi foton dan daya tembus", "Menambah jumlah foton tanpa mengubah energi", "Mendinginkan tabung", "Memperbesar ukuran detektor"], 0,
   "kVp menentukan energi maksimum foton; mAs menentukan jumlah foton.")
bs("xray", "Prinsip proteksi radiasi adalah waktu sesingkat mungkin, jarak sejauh mungkin, dan perisai.", True,
   "Dosis berbanding lurus dengan waktu, turun dengan kuadrat jarak, dan dilemahkan perisai.")
kasus("xray", "Petugas berdiri 1 m dari sumber dan menerima laju dosis D. Jika mundur ke 2 m, laju dosisnya menjadi…",
      ["D/4", "D/2", "2D", "D"], 0, "Hukum kuadrat terbalik: (1/2)² = 1/4.")
pg("xray", "Kolimator pada pesawat sinar-X berfungsi…",
   ["Membatasi luas berkas agar hanya area yang diperiksa terpapar", "Menghasilkan elektron", "Mengubah sinar-X menjadi cahaya", "Menyimpan citra"], 0,
   "Kolimasi mengurangi dosis pasien dan hamburan yang menurunkan kontras.")

# ---------------- CT ----------------
pg("ct", "Satuan Hounsfield (HU) untuk air adalah…", ["0", "−1000", "+1000", "100"], 0, "Skala HU: air 0, udara −1000, tulang padat sekitar +1000 atau lebih.")
pg("ct", "Algoritma klasik untuk membangun irisan CT dari proyeksi adalah…",
   ["Filtered back projection", "Fast Fourier wavelet", "Pan–Tompkins", "K-means"], 0,
   "Back projection dengan filter ramp mengembalikan detail yang kabur pada back projection biasa.")
kasus("ct", "Citra CT menampilkan garis-garis terang memancar dari tambalan gigi logam. Ini adalah…",
      ["Artefak logam/streak akibat beam hardening dan foton kurang", "Tumor", "Gangguan Wi-Fi", "Kesalahan monitor"], 0,
      "Logam menyerap hampir semua foton sehingga data proyeksi rusak dan muncul streak.")
cocok("ct", "Cocokkan jaringan dengan perkiraan nilai HU.",
      [["Udara", "−1000"], ["Lemak", "sekitar −100"], ["Air", "0"], ["Tulang kortikal", "lebih dari +700"]],
      "Nilai HU dipakai untuk windowing dan segmentasi, misalnya segmentasi tulang di 3D Slicer.")

# ---------------- MRI ----------------
pg("mri", "Frekuensi Larmor proton berbanding lurus dengan…", ["Kuat medan magnet B₀", "Suhu ruangan", "Jumlah kumparan gradien", "Lama pemeriksaan"], 0,
   "ω = γ·B₀; pada 1,5 T frekuensi proton sekitar 63,9 MHz.")
bs("mri", "Data MRI diukur dalam k-space dan citra diperoleh dengan transformasi Fourier terbalik.", True,
   "Gradien mengkodekan posisi sebagai frekuensi dan fase, sehingga FFT 2D/3D mengubahnya menjadi citra.")
kasus("mri", "Sebelum masuk ruang MRI, pasien ditanya soal alat pacu jantung dan logam di tubuh. Kenapa?",
      ["Medan magnet kuat dan RF dapat menarik, memanaskan, atau mengganggu benda logam/implan", "Agar citra berwarna", "Karena MRI memakai sinar-X", "Untuk menentukan tarif"], 0,
      "Skrining keselamatan MRI wajib karena gaya magnet dan pemanasan RF pada benda feromagnetik.")
cocok("mri", "Cocokkan komponen MRI dengan fungsinya.",
      [["Magnet utama", "Menyelaraskan spin proton"], ["Kumparan gradien", "Mengkodekan posisi"], ["Kumparan RF", "Mengeksitasi dan menerima sinyal"], ["Rekonstruksi", "Mengubah k-space menjadi citra"]],
      "Masing-masing komponen terkait mata kuliah Fisika Listrik dan Magnet serta pengolahan sinyal.")

# ---------------- Ventilator ----------------
pg("ventilator", "Rasio I:E 1:2 berarti…", ["Waktu ekspirasi dua kali waktu inspirasi", "Inspirasi dua kali ekspirasi", "Dua napas per detik", "Volume tidal 1:2 liter"], 0,
   "I:E menyatakan perbandingan waktu inspirasi terhadap ekspirasi.")
kasus("ventilator", "Alarm tekanan jalan napas tinggi berbunyi tiba-tiba. Kemungkinan penyebab?",
      ["Selang tertekuk atau sekret menyumbat", "Selang terlepas", "Baterai penuh", "Oksigen terlalu rendah"], 0,
      "Sumbatan menaikkan tekanan; selang lepas justru memicu alarm tekanan rendah/diskoneksi.")
bs("ventilator", "Volume tidal dapat dihitung dengan mengintegralkan aliran udara terhadap waktu.", True, "V = ∫Q dt, materi kalkulus yang dipakai langsung di ventilator.")
pg("ventilator", "Humidifier pada ventilator diperlukan karena…",
   ["Udara medis kering dapat mengeringkan dan merusak saluran napas", "Agar alat tidak panas", "Untuk mengukur tekanan", "Agar alarm berbunyi"], 0,
   "Saat diintubasi, hidung yang biasanya melembapkan udara dilewati, sehingga gas harus dilembapkan.")

# ---------------- Infus ----------------
kasus("infus", "Dokter meresepkan 500 mL dalam 4 jam memakai set makro (20 tetes/mL). Berapa tetes per menit?",
      ["±42 tetes/menit", "±125 tetes/menit", "±21 tetes/menit", "±83 tetes/menit"], 0,
      "500 × 20 / 240 menit ≈ 41,7 tetes/menit.")
pg("infus", "Sensor oklusi pada pompa infus mendeteksi…", ["Kenaikan tekanan karena selang tersumbat", "Warna cairan", "Suhu pasien", "Detak jantung"], 0,
   "Sumbatan membuat tekanan di selang naik; pompa harus berhenti dan memberi alarm.")
bs("infus", "Pompa peristaltik mendorong cairan dengan menekan selang secara berurutan tanpa menyentuh cairan langsung.", True,
   "Karena itu jalur cairan tetap steril dan set infus bisa sekali pakai.")
pg("infus", "Pada pompa suntik, laju aliran ditentukan oleh…", ["Kecepatan dorong ulir dan diameter spuit", "Warna spuit", "Tinggi botol", "Tegangan baterai saja"], 0,
   "Q = A·v; luas penampang spuit dikali kecepatan plunger.")

# ---------------- Defibrilator ----------------
pg("defibrilator", "Energi yang tersimpan di kapasitor defibrilator dihitung dengan…", ["E = ½CV²", "E = mc²", "E = IR", "E = ½mv"], 0,
   "Energi kapasitor sebanding kuadrat tegangan.")
kasus("defibrilator", "AED menganalisis ritme dan menyatakan 'no shock advised' pada pasien asistol. Kenapa?",
      ["Asistol bukan ritme shockable; yang dibutuhkan RJP dan obat", "Baterai habis", "Elektroda terbalik", "AED rusak"], 0,
      "Defibrilasi hanya untuk VF dan VT tanpa nadi. Asistol tidak punya aktivitas listrik untuk disinkronkan ulang.")
bs("defibrilator", "Gelombang bifasik umumnya membutuhkan energi lebih rendah daripada monofasik untuk efektivitas serupa.", True,
   "Defibrilator modern bifasik biasanya 120–200 J.")
urut("defibrilator", "Urutkan langkah penggunaan AED.",
     ["Nyalakan AED", "Pasang pad di dada pasien", "Biarkan AED menganalisis (jangan sentuh pasien)", "Tekan tombol kejut bila diminta", "Lanjutkan RJP"],
     "Urutan ini juga dipakai untuk merancang alur suara AED trainer di proyek.")

# ---------------- Inkubator ----------------
pg("inkubator", "Kenapa inkubator bayi memakai kendali umpan balik (closed loop)?",
   ["Agar suhu tetap stabil meski kondisi luar berubah", "Agar murah", "Agar bayi tidak menangis", "Untuk menghemat oksigen saja"], 0,
   "Sensor suhu terus membandingkan nilai aktual dengan setpoint, lalu pengendali menyesuaikan pemanas.")
kasus("inkubator", "Suhu inkubator berosilasi naik-turun ±1 °C di sekitar setpoint. Perbaikan pertama yang tepat?",
      ["Mengganti kendali on-off dengan PID atau menala ulang parameter", "Menambah kipas lebih kencang tanpa kontrol", "Mematikan alarm", "Memindahkan sensor ke luar kotak"], 0,
      "Kendali on-off menyebabkan osilasi; PID memberi respons lebih halus.")
bs("inkubator", "Mode skin servo mengatur pemanas berdasarkan suhu kulit bayi, bukan suhu udara.", True, "Sensor kulit ditempel di bayi untuk menjaga suhu tubuh target.")
pg("inkubator", "Kelembapan dalam inkubator penting terutama untuk…", ["Mengurangi kehilangan air lewat penguapan kulit bayi prematur", "Membersihkan udara", "Menambah oksigen", "Mengurangi kebisingan"], 0,
   "Kulit prematur tipis sehingga penguapan tinggi; kelembapan membantu mencegah dehidrasi dan hipotermia.")

# ---------------- Hemodialisis ----------------
pg("hemodialisis", "Prinsip utama pembuangan zat sisa pada dialiser adalah…", ["Difusi melalui membran semipermeabel", "Penguapan", "Filtrasi oleh pasir", "Pemanasan darah"], 0,
   "Ureum dan kreatinin berdifusi dari darah ke dialisat karena beda konsentrasi.")
kasus("hemodialisis", "Detektor udara di jalur vena berbunyi. Tindakan otomatis yang benar dari mesin?",
      ["Menghentikan pompa darah dan menjepit jalur vena", "Mempercepat pompa", "Mengabaikan karena gelembung kecil", "Menambah dialisat"], 0,
      "Emboli udara berbahaya, jadi mesin harus berhenti dan mengklem jalur.")
bs("hemodialisis", "Konduktivitas dialisat dipantau karena mencerminkan konsentrasi elektrolitnya.", True, "Ion dalam larutan menghantarkan listrik; konduktivitas menjadi indikator komposisi.")
pg("hemodialisis", "Ultrafiltrasi (UF) pada hemodialisis bertujuan…", ["Menarik kelebihan cairan dari tubuh dengan beda tekanan", "Menambah darah", "Menurunkan suhu", "Mengukur EKG"], 0,
   "Tekanan transmembran menarik air keluar dari darah.")

# ---------------- EEG ----------------
cocok("eeg", "Cocokkan pita gelombang EEG dengan frekuensinya.",
      [["Delta", "0,5–4 Hz"], ["Theta", "4–8 Hz"], ["Alfa", "8–12 Hz"], ["Beta", "13–30 Hz"]],
      "Pita ini dipakai dalam analisis spektrum, qEEG, dan neurofeedback.")
pg("eeg", "Kenapa sinyal EEG lebih sulit direkam daripada EKG?", ["Amplitudonya jauh lebih kecil (mikrovolt) sehingga mudah tertutup derau", "Frekuensinya MHz", "EEG memakai sinar-X", "Karena memakai satu elektroda"], 0,
   "EEG puluhan µV, sedangkan EKG sekitar 1 mV.")
kasus("eeg", "Pada rekaman EEG muncul lonjakan besar lambat di kanal frontal setiap beberapa detik. Kemungkinan terbesar?",
      ["Artefak kedipan mata", "Kejang umum", "Interferensi 50 Hz", "Elektroda referensi putus"], 0,
      "Kedip mata menghasilkan potensial besar di elektroda frontal; bisa dibuang dengan ICA.")
bs("eeg", "Sistem penempatan elektroda 10–20 memakai jarak 10% dan 20% dari ukuran kepala.", True, "Angka 10–20 merujuk persentase jarak antar-titik anatomi (nasion, inion, preaurikular).")

# ---------------- qEEG ----------------
pg("brainmapping", "Peta topografi qEEG dibuat dengan…", ["Interpolasi nilai tiap elektroda ke permukaan kepala", "Memotret kepala", "Sinar-X kepala", "Menghitung detak jantung"], 0,
   "Nilai di antara elektroda diperkirakan dengan interpolasi (misalnya spline).")
bs("brainmapping", "Z-score qEEG membandingkan nilai individu dengan database normatif seusia.", True, "Z = (x − rerata normatif)/SD; menunjukkan seberapa jauh dari normal.")
kasus("brainmapping", "Hasil qEEG menunjukkan Z-score tinggi di semua kanal frontal pada pita delta. Hal pertama yang perlu dicek?",
      ["Kualitas data: artefak gerak mata/kedip belum dibersihkan", "Langsung mendiagnosis tumor", "Mengganti monitor", "Menambah frekuensi sampling"], 0,
      "Artefak okular dominan di frontal dan pita lambat. Pra-proses menentukan kualitas peta.")

# ---------------- Neurofeedback ----------------
pg("neurofeedback", "Inti neurofeedback adalah…", ["Memberi umpan balik real-time agar pengguna belajar mengubah pola gelombang otaknya", "Menstimulasi otak dengan listrik", "Memotret otak", "Mengukur gula darah"], 0,
   "Ini bentuk operant conditioning: perubahan yang diinginkan diberi 'hadiah' visual/suara.")
bs("neurofeedback", "Latensi pemrosesan yang terlalu besar membuat umpan balik neurofeedback kurang efektif.", True, "Umpan balik harus cukup cepat (ratusan ms) agar otak mengaitkannya dengan keadaan saat itu.")
kasus("neurofeedback", "Untuk menguji apakah efek neurofeedback nyata, desain penelitian yang paling kuat adalah…",
      ["Uji acak dengan kelompok sham feedback", "Testimoni pengguna", "Satu sesi tanpa pembanding", "Survei kepuasan"], 0,
      "Sham feedback mengontrol efek plasebo dan motivasi.")

# ---------------- TMS ----------------
pg("tms", "TMS menstimulasi neuron dengan…", ["Medan magnet berubah cepat yang menginduksi arus listrik di korteks", "Arus listrik langsung lewat elektroda", "Sinar laser", "Gelombang ultrasonik"], 0,
   "Hukum induksi Faraday: dB/dt yang besar menginduksi medan listrik di jaringan.")
bs("tms", "Kumparan figure-8 memberi stimulasi lebih fokus daripada kumparan bulat.", True, "Medan dua sayap bertemu di titik tengah, menghasilkan fokus.")
kasus("tms", "Koil TMS menjadi panas setelah sesi repetitif panjang. Blok apa yang bertugas mengatasinya?",
      ["Sistem pendingin koil", "Navigasi", "Kapasitor", "Tampilan"], 0, "Arus ribuan ampere memanaskan koil, sehingga perlu pendingin dan sensor suhu.")

# ---------------- ECT ----------------
pg("ect", "Parameter dosis ECT modern biasanya dinyatakan dalam…", ["Muatan listrik (milicoulomb)", "Tekanan (mmHg)", "Suhu (°C)", "Intensitas cahaya"], 0,
   "Muatan = arus × lebar pulsa × frekuensi × durasi × 2 (bifasik).")
bs("ect", "Pengukuran impedansi sebelum stimulus dilakukan untuk memastikan kontak elektroda baik dan mencegah luka bakar.", True, "Impedansi terlalu tinggi menandakan kontak buruk.")
kasus("ect", "Mengapa ECT memantau EEG selama prosedur?", ["Untuk memastikan dan mengukur durasi kejang terapeutik", "Untuk mengukur gula darah", "Untuk memotret otak", "Untuk menentukan golongan darah"], 0,
      "Efektivitas ECT berkaitan dengan kejang yang adekuat; EEG dipakai memantaunya.")

# ---------------- TENS ----------------
pg("tens", "Teori yang paling sering dipakai menjelaskan efek TENS frekuensi tinggi adalah…", ["Gate control theory", "Hukum Ohm", "Efek Doppler", "Hukum Beer–Lambert"], 0,
   "Stimulasi serabut Aβ 'menutup gerbang' transmisi nyeri di medula spinalis.")
bs("tens", "Pulsa bifasik pada TENS membantu mencegah penumpukan muatan dan iritasi kulit.", True, "Muatan bersih nol mengurangi reaksi elektrokimia di bawah elektroda.")
kasus("tens", "Pasien dengan alat pacu jantung meminta terapi TENS di dada. Sikap yang tepat?",
      ["Tidak memasang di area dada karena merupakan kontraindikasi", "Langsung pasang intensitas maksimum", "Pasang di kepala saja", "Abaikan alat pacu"], 0,
      "Stimulasi listrik dekat alat pacu jantung bisa mengganggu kerjanya.")

# ---------------- EMS ----------------
pg("stimulasi-listrik", "Perbedaan utama NMES dengan TENS adalah…", ["NMES bertujuan membuat kontraksi otot, TENS untuk mengurangi nyeri", "NMES memakai sinar-X", "TENS untuk mengukur EMG", "Tidak ada bedanya"], 0,
   "Parameter NMES (intensitas lebih tinggi, pola on/off) dirancang untuk kontraksi.")
bs("stimulasi-listrik", "Ramp up dan ramp down pada stimulasi otot membuat kontraksi lebih nyaman.", True, "Kenaikan bertahap menghindari kontraksi mendadak.")
cocok("stimulasi-listrik", "Cocokkan parameter stimulasi dengan efeknya.",
      [["Frekuensi", "Kehalusan kontraksi (tetani)"], ["Lebar pulsa", "Jumlah serabut yang terekrut"], ["Duty cycle on/off", "Mencegah kelelahan otot"], ["Intensitas", "Kekuatan kontraksi"]],
      "Parameter ini diatur di blok kontrol dan generator.")

# ---------------- Diatermi SW ----------------
pg("diatermi-sw", "Frekuensi diatermi gelombang pendek yang umum dipakai adalah…", ["27,12 MHz", "50 Hz", "2,45 GHz", "1 MHz"], 0,
   "27,12 MHz adalah pita ISM yang dialokasikan untuk keperluan medis.")
bs("diatermi-sw", "Tuning pada SWD bertujuan menyamakan resonansi rangkaian pasien dengan osilator agar transfer energi maksimum.", True, "Rangkaian pasien berubah dengan posisi dan jaringan, jadi perlu tuning.")
kasus("diatermi-sw", "Pasien memakai implan logam di lutut dan akan diterapi SWD di lutut. Keputusan yang benar?",
      ["Tidak dilakukan di area itu karena logam dapat memanas berlebihan", "Dilakukan dengan intensitas tinggi", "Dilakukan tanpa handuk", "Implan tidak berpengaruh"], 0,
      "Logam memusatkan medan dan bisa menyebabkan luka bakar.")

# ---------------- Diatermi MW ----------------
pg("diatermi-mw", "Sumber gelombang mikro pada diatermi MWD adalah…", ["Magnetron", "Tabung sinar-X", "Kristal piezo", "LED"], 0, "Magnetron membangkitkan gelombang 2,45 GHz.")
bs("diatermi-mw", "Gelombang mikro lebih banyak diserap jaringan yang kaya air seperti otot.", True, "Molekul air polar menyerap energi gelombang mikro.")
kasus("diatermi-mw", "Kenapa mata harus dilindungi atau dihindari saat terapi MWD?", ["Lensa mata sensitif panas dan perfusinya rendah sehingga mudah rusak", "Karena mata memantulkan gelombang", "Agar pasien tidur", "Karena sinar-X"], 0,
      "Jaringan dengan aliran darah rendah sulit membuang panas.")

# ---------------- Terapi US ----------------
pg("terapi-us", "Frekuensi 3 MHz pada terapi ultrasound dipilih untuk…", ["Jaringan superfisial (dangkal)", "Jaringan dalam", "Mengukur tekanan darah", "Mencitrakan janin"], 0,
   "Frekuensi tinggi diserap lebih cepat, jadi efeknya lebih dangkal; 1 MHz untuk jaringan lebih dalam.")
bs("terapi-us", "Mode pulsed (misalnya duty cycle 20%) mengurangi efek termal dibanding mode kontinu.", True, "Energi rata-rata lebih kecil sehingga panas lebih sedikit, efek non-termal dominan.")
kasus("terapi-us", "Transduser terapi ultrasound dinyalakan di udara tanpa kontak. Risikonya?",
      ["Kristal bisa rusak karena energi tidak tersalur (impedansi udara)", "Tidak ada risiko", "Pasien tersengat listrik", "Layar mati"], 0,
      "Energi yang tidak terserap kembali ke transduser dan memanaskan kristal.")

# ---------------- Brace ----------------
pg("brace-skoliosis", "Sudut Cobb diukur antara…", ["Garis endplate vertebra paling miring di atas dan di bawah kurva", "Bahu kiri dan kanan", "Panggul dan lutut", "Dua tulang rusuk"], 0,
   "Sudut Cobb adalah standar menilai derajat skoliosis.")
bs("brace-skoliosis", "Brace skoliosis bekerja dengan memberi gaya koreksi tiga titik pada batang tubuh.", True, "Prinsip biomekanik tiga titik untuk menahan dan memperbaiki kurva.")
kasus("brace-skoliosis", "Pasien remaja jarang memakai brace karena panas dan tidak nyaman. Solusi desain yang paling relevan?",
      ["Ventilasi, bahan lebih ringan, dan sensor kepatuhan pakai", "Menambah ketebalan brace", "Mewarnai brace", "Mengurangi jam pakai tanpa evaluasi"], 0,
      "Kepatuhan pakai menentukan keberhasilan; desain yang nyaman dan pemantauan membantu.")

# ---------------- Termometer ----------------
pg("termometer", "Termometer inframerah dahi mengukur suhu dengan…", ["Radiasi inframerah yang dipancarkan permukaan kulit", "Kontak logam", "Gelombang suara", "Tekanan"], 0,
   "Semua benda memancarkan radiasi IR sesuai suhunya (hukum Stefan–Boltzmann).")
bs("termometer", "Termistor NTC memiliki resistansi yang turun ketika suhu naik.", True, "NTC = negative temperature coefficient.")
kasus("termometer", "Hasil termometer IR selalu lebih rendah saat pasien baru masuk dari luar yang dingin. Kenapa?",
      ["Suhu kulit permukaan belum seimbang dengan suhu inti tubuh", "Baterai lemah", "Termometer terlalu baru", "Pasien demam"], 0,
      "Termometer IR membaca permukaan, jadi pasien perlu beradaptasi beberapa menit.")

# ---------------- Glukometer ----------------
pg("glukometer", "Prinsip pengukuran glukometer strip elektrokimia adalah…", ["Arus dari reaksi enzim glukosa oksidase/dehidrogenase sebanding kadar glukosa", "Warna kulit", "Suhu darah", "Tekanan darah"], 0,
   "Ini metode amperometri yang memakai potensiostat.")
bs("glukometer", "Hematokrit yang sangat tinggi atau rendah dapat memengaruhi akurasi glukometer.", True, "Hematokrit mengubah difusi plasma ke elektroda.")
kasus("glukometer", "Sebuah glukometer membaca 130 mg/dL saat nilai laboratorium 100 mg/dL. Berapa galat relatifnya?",
      ["30%", "13%", "3%", "77%"], 0, "(130 − 100)/100 = 30%. Standar ISO 15197 menuntut sebagian besar hasil dalam ±15%.")

# ---------------- Kimia klinik ----------------
pg("kimia-klinik", "Hukum yang dipakai fotometer chemistry analyzer adalah…", ["Beer–Lambert (A = ε·l·c)", "Hukum Ohm", "Hukum Boyle", "Hukum Faraday"], 0,
   "Absorbansi sebanding konsentrasi dan panjang lintasan.")
bs("kimia-klinik", "Inkubasi pada 37 °C dipakai karena laju reaksi enzim dipengaruhi suhu.", True, "Suhu dikendalikan agar hasil kinetik dapat dibandingkan.")
kasus("kimia-klinik", "Hasil kontrol mutu harian berada di luar ±3 SD. Langkah yang tepat?",
      ["Hentikan pelaporan, cari penyebab (reagen, kalibrasi), ulangi kontrol", "Tetap laporkan hasil pasien", "Hapus data kontrol", "Ganti nama pasien"], 0,
      "Aturan Westgard 1-3s menandakan kesalahan yang harus diselidiki.")

# ---------------- Koagulasi ----------------
pg("koagulasi", "INR dihitung dengan…", ["(PT pasien / PT normal)^ISI", "PT pasien × 2", "APTT − PT", "PT / 37"], 0,
   "ISI (international sensitivity index) menstandarkan reagen tromboplastin yang berbeda.")
bs("koagulasi", "Deteksi optik pada analyzer koagulasi memanfaatkan perubahan kekeruhan saat fibrin terbentuk.", True, "Fibrin membuat sampel lebih keruh sehingga transmisi cahaya berubah.")
kasus("koagulasi", "Pasien yang memakai warfarin dipantau dengan parameter…", ["PT/INR", "Hemoglobin", "Glukosa", "Kolesterol"], 0, "INR target untuk pasien warfarin umumnya 2–3.")

# ---------------- CAT ----------------
pg("cat", "Pada column agglutination test, sel yang beraglutinasi akan…", ["Tertahan di atas atau di dalam gel", "Turun ke dasar kolom", "Larut", "Berubah warna menjadi biru"], 0,
   "Gumpalan sel tidak bisa melewati matriks gel; sel tidak beraglutinasi turun ke dasar.")
bs("cat", "Sentrifugasi kartu gel dibutuhkan agar sel bergerak melewati gel dengan gaya terkendali.", True, "RCF yang tepat memisahkan sel yang menggumpal dan tidak.")
kasus("cat", "Kesalahan paling berbahaya dalam uji golongan darah adalah…", ["Salah identifikasi sampel/pasien", "Kartu terlalu dingin", "Layar redup", "Baterai lemah"], 0,
      "Salah identifikasi dapat menyebabkan reaksi transfusi fatal; barcode dan alur kerja membantu.")

# ---------------- Elektrolit ----------------
pg("elektrolit", "Elektroda ion selektif (ISE) menghasilkan potensial yang sebanding dengan…", ["Logaritma aktivitas ion", "Kuadrat konsentrasi", "Suhu saja", "Tekanan"], 0,
   "Persamaan Nernst: E = E₀ + (RT/zF)·ln(a).")
bs("elektrolit", "Kemiringan ideal elektroda untuk ion bervalensi 1 pada 25 °C kira-kira 59 mV per dekade.", True, "2,303·RT/F ≈ 59,16 mV.")
kasus("elektrolit", "Sampel darah hemolisis menunjukkan kalium tinggi palsu. Penyebabnya?", ["Kalium keluar dari sel darah merah yang pecah", "Elektroda rusak", "Suhu tinggi", "Natrium rendah"], 0,
      "Kalium intrasel jauh lebih tinggi dari plasma.")

# ---------------- Hematologi ----------------
pg("hematologi", "Prinsip Coulter menghitung sel berdasarkan…", ["Perubahan impedansi saat sel melewati celah kecil", "Warna sel", "Bau sampel", "Suhu"], 0,
   "Setiap sel mengganggu aliran arus dan menghasilkan pulsa sebanding volumenya.")
bs("hematologi", "Hemoglobin pada analyzer hematologi umumnya diukur secara fotometri.", True, "Hb diubah menjadi kompleks berwarna lalu diukur absorbansinya (sekitar 540–555 nm).")
cocok("hematologi", "Cocokkan parameter dengan metode pengukuran umumnya.",
      [["Jumlah RBC", "Impedansi"], ["Hemoglobin", "Fotometri"], ["Diferensial WBC", "Flow cytometry/hamburan laser"], ["MCV", "Tinggi pulsa impedansi"]],
      "Satu analyzer menggabungkan beberapa prinsip fisika.")

# ---------------- Immunoassay ----------------
pg("immunoassay", "Pada immunoassay fluoresensi, filter emisi berfungsi…", ["Meloloskan cahaya fluoresensi dan menghalangi cahaya eksitasi", "Menambah cahaya eksitasi", "Memanaskan kartrid", "Mengukur suhu"], 0,
   "Cahaya eksitasi jauh lebih kuat; tanpa filter, sinyal fluoresensi tertutup.")
bs("immunoassay", "Garis kontrol pada strip lateral flow harus muncul agar hasil dianggap valid.", True, "Garis kontrol menunjukkan cairan mengalir dan reagen bekerja.")
kasus("immunoassay", "Pembaca strip memberi hasil berbeda pada pencahayaan berbeda. Solusi desain?", ["Kotak baca dengan pencahayaan internal seragam", "Memakai lampu disko", "Menambah filter Instagram", "Membaca di bawah matahari"], 0,
      "Kondisi optik yang konsisten membuat rasio T/C dapat diandalkan.")

# ---------------- Sentrifus ----------------
pg("sentrifus", "RCF (gaya sentrifugal relatif) bergantung pada…", ["Kuadrat RPM dan jari-jari rotor", "Warna tabung", "Suhu ruang saja", "Volume sampel saja"], 0,
   "RCF = 1,118×10⁻⁵ × r(cm) × RPM².")
bs("sentrifus", "Tabung di rotor harus seimbang berat dan posisinya untuk mencegah getaran berbahaya.", True, "Ketidakseimbangan merusak motor dan bisa memecahkan tabung.")
kasus("sentrifus", "Sentrifus bergetar keras saat mulai berputar. Tindakan pertama?", ["Hentikan, periksa keseimbangan tabung", "Naikkan kecepatan", "Buka tutup saat berputar", "Abaikan"], 0,
      "Getaran menandakan ketidakseimbangan; tutup harus tetap terkunci sampai rotor berhenti.")

# ---------------- Mikroskop ----------------
pg("mikroskop", "Perbesaran total mikroskop dengan objektif 40× dan okuler 10× adalah…", ["400×", "50×", "4000×", "30×"], 0, "Perbesaran total = objektif × okuler.")
bs("mikroskop", "Minyak imersi pada objektif 100× meningkatkan aperture numerik sehingga resolusi lebih baik.", True, "Indeks bias minyak mirip kaca sehingga lebih banyak cahaya masuk ke objektif.")
cocok("mikroskop", "Cocokkan bagian mikroskop dengan fungsinya.",
      [["Kondensor", "Memfokuskan cahaya ke preparat"], ["Objektif", "Perbesaran utama dan resolusi"], ["Okuler", "Perbesaran akhir ke mata"], ["Makrometer/mikrometer", "Mengatur fokus"]],
      "Blok optik dan mekanik ini juga ditiru di mikroskop OpenFlexure.")

# ---------------- Urin ----------------
pg("urin-analyzer", "Urine analyzer strip membaca hasil dengan…", ["Reflektometri warna pad", "Sinar-X", "Ultrasonik", "Tekanan"], 0,
   "LED menyinari pad, detektor membaca cahaya pantul untuk menentukan warna.")
bs("urin-analyzer", "Waktu baca strip penting karena warna pad terus berubah setelah dicelup.", True, "Reaksi kimia berlanjut, jadi pembacaan harus pada waktu yang ditentukan.")
kasus("urin-analyzer", "Strip menunjukkan glukosa positif pada urin. Pemeriksaan lanjutan yang relevan?", ["Kadar glukosa darah", "Rontgen dada", "EEG", "Tes golongan darah"], 0,
      "Glukosuria muncul bila glukosa darah melampaui ambang ginjal.")

# ---------------- BrainWave ----------------
pg("brainwave", "Sinyal BOLD pada fMRI mencerminkan…", ["Perubahan oksigenasi darah akibat aktivitas neuron", "Aktivitas listrik langsung", "Kepadatan tulang", "Detak jantung"], 0,
   "Aktivitas neuron meningkatkan aliran darah lokal sehingga rasio oksi/deoksi-Hb berubah.")
bs("brainwave", "General linear model (GLM) dipakai untuk menguji voxel mana yang mengikuti pola tugas.", True, "Regressor tugas dikonvolusi HRF lalu difit per voxel.")
kasus("brainwave", "Peta aktivasi tampak di luar otak, di tepi tengkorak. Penyebab yang mungkin?", ["Artefak gerak kepala atau registrasi yang buruk", "Otak sangat aktif", "Pasien berbicara", "Monitor rusak"], 0,
      "Gerak menghasilkan korelasi palsu di tepi; koreksi gerak dan registrasi harus diperiksa.")

# ---------------- Motion correction ----------------
pg("motion-correction", "Koreksi gerak rigid pada fMRI memperkirakan berapa parameter?", ["6 (3 translasi + 3 rotasi)", "2", "12", "1"], 0,
   "Rigid body: x, y, z, pitch, roll, yaw.")
bs("motion-correction", "Framewise displacement dipakai untuk menandai volume dengan gerak berlebih.", True, "Volume dengan FD tinggi bisa dibuang (scrubbing).")
kasus("motion-correction", "Setelah resampling, citra tampak lebih kabur. Penyebabnya?", ["Interpolasi saat resampling", "Pasien tertidur", "Koil RF rusak", "Kontras terlalu tinggi"], 0,
      "Interpolasi (misalnya trilinear) menghaluskan citra; sinc/spline mengurangi efek ini.")

# ---------------- Lanjutan: HTA ----------------
pg("hta", "Health Technology Assessment (HTA) paling tepat didefinisikan sebagai…",
   ["Evaluasi multidisiplin tentang nilai teknologi kesehatan untuk mendukung keputusan", "Uji kalibrasi alat", "Pemasaran alat kesehatan", "Desain casing alat"], 0,
   "HTA menilai efektivitas klinis, keamanan, biaya, dan aspek sosial-etis untuk membantu pengambil kebijakan.")
cocok("hta", "Cocokkan domain HTA Core Model dengan pertanyaannya.",
      [["Keamanan", "Apa efek merugikan teknologi ini?"], ["Efektivitas klinis", "Apakah hasil kesehatan pasien membaik?"], ["Biaya dan evaluasi ekonomi", "Apakah sepadan dengan biayanya?"], ["Organisasi", "Apa yang berubah pada alur kerja RS?"]],
      "HTA Core Model EUnetHTA memiliki 9 domain, termasuk etika, sosial, dan hukum.")
bs("hta", "Di Indonesia, penilaian teknologi kesehatan untuk program JKN dikoordinasikan oleh Komite PTK (InaHTAC).", True, "InaHTAC memberi rekomendasi berbasis bukti untuk paket manfaat JKN.")
pg("hta", "Format PICO dipakai pada tahap scoping HTA untuk merumuskan…", ["Population, Intervention, Comparator, Outcome", "Price, Income, Cost, Output", "Plan, Implement, Check, Optimize", "Patient, Insurance, Clinic, Obat"], 0,
   "PICO memastikan pertanyaan kajian jelas dan dapat dijawab bukti.")
kasus("hta", "Sebuah RS ingin membeli MRI kedua. Dalam HTA, pembanding (comparator) yang paling tepat adalah…",
      ["Praktik saat ini: satu MRI dengan antrean, atau rujukan ke RS lain", "Tidak ada pembanding", "Harga mobil", "Alat USG di RS lain negara"], 0,
      "Comparator adalah alternatif realistis yang akan digantikan atau dilengkapi.")
bs("hta", "Alat kesehatan berbeda dari obat dalam HTA karena hasilnya bergantung pada kurva belajar operator dan pembaruan desain yang cepat.", True,
   "WHO menekankan karakteristik khusus alat: operator, inovasi bertahap, dan kebutuhan infrastruktur.")

# ---------------- Lanjutan: Health Economics ----------------
pg("he", "ICER dihitung dengan…", ["(Biaya baru − biaya lama) / (Efek baru − efek lama)", "Biaya / jumlah pasien", "Efek × biaya", "Biaya baru − biaya lama"], 0,
   "Incremental cost-effectiveness ratio = ΔC/ΔE, misalnya rupiah per QALY.")
kasus("he", "Alat baru menambah biaya Rp30 juta dan menambah 0,5 QALY per pasien. ICER-nya?", ["Rp60 juta/QALY", "Rp15 juta/QALY", "Rp30 juta/QALY", "Rp0,5 juta/QALY"], 0,
      "30 juta / 0,5 = 60 juta per QALY. Lalu bandingkan dengan ambang willingness-to-pay.")
cocok("he", "Cocokkan jenis evaluasi ekonomi dengan ukuran hasilnya.",
      [["Cost-minimization", "Hasil dianggap setara, bandingkan biaya"], ["Cost-effectiveness", "Unit alami (misal kasus terdeteksi)"], ["Cost-utility", "QALY atau DALY"], ["Cost-benefit", "Semua dinilai dalam uang"]],
      "Pembagian ini mengikuti Drummond dkk., Methods for the Economic Evaluation of Health Care Programmes.")
bs("he", "QALY menggabungkan lama hidup dan kualitas hidup dalam satu ukuran.", True, "1 QALY = 1 tahun dalam kesehatan sempurna; nilai utilitas diambil dari instrumen seperti EQ-5D.")
pg("he", "Budget impact analysis menjawab pertanyaan…", ["Berapa tambahan anggaran yang dibutuhkan bila teknologi diadopsi", "Apakah alat aman", "Berapa QALY per pasien", "Bagaimana desain casing"], 0,
   "BIA melengkapi analisis efektivitas biaya dengan sudut pandang keterjangkauan anggaran.")
kasus("he", "Hasil ICER berubah dari 'cost-effective' menjadi tidak saat harga alat dinaikkan 20%. Analisis apa yang menunjukkan ini?", ["Analisis sensitivitas", "Uji klinis fase 1", "Kalibrasi", "Survei kepuasan"], 0,
      "Analisis sensitivitas menguji seberapa kuat kesimpulan terhadap ketidakpastian parameter.")
bs("he", "Diskonto dipakai karena biaya dan manfaat di masa depan dinilai lebih rendah daripada saat ini.", True, "Rumus nilai kini: PV = FV/(1+r)^t.")

# ---------------- Lanjutan: Public Health ----------------
kasus("ph", "Sebuah tes skrining memiliki sensitivitas 90% dan spesifisitas 90%. Pada populasi dengan prevalensi 1%, PPV-nya sekitar…",
      ["8%", "90%", "50%", "99%"], 0, "Dari 1000 orang: 9 positif benar, 99 positif palsu. PPV = 9/108 ≈ 8%. Prevalensi rendah menurunkan PPV.")
pg("ph", "Sensitivitas alat skrining adalah…", ["Proporsi orang sakit yang terdeteksi positif", "Proporsi orang sehat yang negatif", "Proporsi hasil positif yang benar sakit", "Jumlah alat per puskesmas"], 0,
   "Sensitivitas = TP/(TP+FN).")
cocok("ph", "Cocokkan ukuran epidemiologi dengan definisinya.",
      [["Insidensi", "Kasus baru dalam periode tertentu"], ["Prevalensi", "Semua kasus yang ada pada satu waktu"], ["Spesifisitas", "Proporsi orang sehat yang dites negatif"], ["NPV", "Peluang benar sehat bila hasil negatif"]],
      "Ukuran ini menentukan apakah alat diagnostik berguna di populasi tertentu.")
bs("ph", "WHO building blocks sistem kesehatan mencakup 'produk medis, vaksin, dan teknologi' sebagai salah satu blok.", True,
   "Enam blok: layanan, tenaga kesehatan, informasi, produk/teknologi medis, pembiayaan, serta kepemimpinan/tata kelola.")
pg("ph", "Kriteria Wilson–Jungner dipakai untuk menilai…", ["Kelayakan program skrining", "Kalibrasi alat", "Harga alat", "Kualitas citra"], 0,
   "Misalnya penyakit harus penting, ada tes yang dapat diterima, dan ada pengobatan efektif.")
kasus("ph", "Puskesmas di daerah terpencil ingin skrining hipertensi massal. Alat yang paling sesuai?", ["Tensimeter digital tervalidasi dengan manset beberapa ukuran", "MRI", "CT scan", "Analyzer hematologi"], 0,
      "Teknologi tepat guna untuk layanan primer harus terjangkau, mudah dipakai, dan tervalidasi.")
bs("ph", "Transformasi sistem kesehatan Indonesia mencakup pilar ketahanan kesehatan, termasuk kemandirian produksi alat kesehatan dalam negeri.", True,
   "Pilar ketahanan kesehatan menargetkan industri farmasi dan alat kesehatan dalam negeri.")


def get():
    return S
