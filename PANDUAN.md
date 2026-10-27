# Teknologi Kedokteran — Panduan Pemakaian (v1.3)

Aplikasi desktop Windows untuk belajar alat Teknologi Kedokteran dan melihat mata kuliah serta sub-materi apa saja yang membangun tiap alat. Semua data tersimpan di laptopmu, tanpa internet.

## Yang baru di v1.3

- **Bahan kuliah Semester 1 sampai 5 masuk aplikasi.** Isi folder `D:\Semester 1` sampai `D:\Semester 5` (215 berkas dari 26 mata kuliah: PDF, PPTX, DOCX, notebook) dibaca dan dirangkum. Di halaman mata kuliah ada panel **Bahan kuliah** berisi judul tiap berkas, jumlah halaman/slide, dan poin isinya. Di versi laptop tombol **Buka** membuka berkas aslinya. Berkasnya tidak disalin; aplikasi hanya menyimpan ringkasan, jadi kalau folder dipindah tombol Buka akan disembunyikan.
- **Semester sudah pasti** untuk 26 mata kuliah yang foldernya ada di drive D. Tanda "perkiraan" hilang untuk mata kuliah itu.
- **Modul tiap mata kuliah (58 modul).** Halaman mata kuliah sekarang dibuka dengan **Apa yang dipelajari**: ringkasan, lalu 254 topik inti yang bisa dibuka-tutup, lengkap dengan poin dan nomor sub-materinya.
- **Studi kasus alat (171 kasus).** Contoh: Anatomi → EKG → anatomi jantung dan dada untuk EKG 12 sadapan. Tiap kasus menjelaskan apa yang dideteksi alat, daftar hal yang harus dipelajari (bisa dicentang, tersimpan di progres), dan penerapannya di alat.
- **Latihan soal per mata kuliah.** 331 soal baru yang ditulis per mata kuliah. Tombol **Latihan** ada di kepala halaman mata kuliah, dan halaman Latihan Soal punya bagian **Per mata kuliah** dengan saringan semester.
- **6 tipe soal baru:** isian singkat, hitungan (dengan toleransi dan satuan), pilih semua yang benar, kelompokkan, lengkapi kalimat dari bank kata, dan lengkapi diagram blok (dibuat otomatis dari tiap alat). Mode baru di Latihan Soal: Lengkapi diagram blok, Soal hitungan, Kelompokkan, Lengkapi kalimat, dan Campuran tipe baru.
- **Menu Referensi** di sidebar: 326 referensi (buku teks, standar IEC/ISO dan Permenkes, jurnal dan pedoman, dataset, sumber proyek, bahan kuliah). Tiap referensi menyebut **alat yang memakainya** dan mata kuliahnya. Bisa dicari dan disaring per jenis atau per alat; dari halaman alat, tombol **Semua referensi** langsung membuka saringan alat itu.
- **23 alat baru** (total 59): Spirometer, Kapnograf, Mammografi, Fluoroskopi C-arm, Platform Telemedisin, Rekam Medis Elektronik, Jam Tangan Pintar Kesehatan, Robot Bedah, Dispenser Obat Pintar, Monitor Pasien Multiparameter, Holter, Elektromiograf, Audiometer, Alat Bantu Dengar, Implan Koklea, Endoskop, Kardiotokograf, PET Scan, Prostesis Tangan Cetak 3D, Electrosurgical Unit, Autoklaf, Fototerapi Neonatus, dan Mesin Anestesi. Ada kategori baru **Bedah**, 7 ilustrasi baru, dan 46 proyek hands-on baru (total 155). Untuk alat berbahaya (sinar-X, PET, ESU, gas anestesi) proyeknya berupa simulasi atau perangkat lunak.
- **Animasi breakdown komponen** di halaman alat. Sinyal "berjalan" dari blok ke blok: komponen yang aktif menyala di gambar, osiloskop mini menunjukkan bentuk sinyal di tahap itu (mentah berderau → diperkuat → difilter → disampling → diolah → ditampilkan; untuk alat pencitraan: data detektor → rekonstruksi → citra), dan mata kuliah yang dipakai di tahap itu muncul sebagai chip. Bisa diputar, dijeda, atau dilangkahi dengan tombol ◀ ▶.
- **Grafik progres di beranda:** cincin per bidang, kolom per semester, dan garis jumlah soal 14 hari terakhir. Arahkan kursor untuk melihat angkanya; ada juga tampilan tabel. Garis EKG berjalan di kiri-kanan sapaan.
- **Penyegaran UI:** bagian halaman muncul halus saat digulir, navigasi cepat di halaman mata kuliah (Penjelasan, Studi kasus, Latihan, Sub-materi, Bahan kuliah), tombol dan chip bereaksi saat ditekan. Semua animasi tetap bisa dimatikan di Pengaturan.

## Yang baru di v1.2

- **Sapaan baru di beranda:** "Selamat Datang Tuan Raihan, Selamat Belajar". Nama sapaan bisa diganti di Pengaturan.
- **Anatomi alat.** Saat membuka alat, bagian paling atas menampilkan gambar alat yang kemudian dipecah per komponen (exploded view). Tiap komponen ditarik garis ke mata kuliah yang membangunnya, seperti mindmap. Warna garis mengikuti bidang kuliah: **Elektrikal** oranye, **Informatika** biru, **Desain** merah muda, **Dasar** abu. Tebal garis = tingkat peran. Arahkan kursor ke komponen atau mata kuliah untuk menyorot jalurnya, klik chip bidang untuk menyembunyikan bidang tertentu, dan tombol **Rakit ulang / Pecah komponen** untuk mengulang animasi.
- **Bidang kuliah.** Tiap mata kuliah sekarang punya bidang: Informatika, Elektrikal, Desain, atau Dasar (sains dan kedokteran). Halaman Materi Kuliah bisa disaring per bidang.
- **Proyek Hands-on (109 proyek).** Tiap alat dipecah jadi 3 sampai 4 proyek kecil per komponen, dari tahap 1 (pemula) sampai prototipe. Tiap proyek berisi tujuan, langkah kerja yang bisa dicentang, daftar bahan dengan perkiraan harga, mata kuliah yang dipakai, catatan keselamatan, dan referensi tutorial.
- **Latihan Soal.** 145 soal tulisan tangan ditambah soal otomatis dari diagram blok tiap alat. Tipe: pilihan ganda, benar/salah, studi kasus, cocokkan pasangan, urutkan alur sinyal, dan permainan **Match kilat**. Ada XP, combo, hari beruntun, dan daftar soal yang perlu diulang.
- **Studi Lanjutan:** Health Technology Assessment, Health Economics, dan Public Health. Masing-masing berisi modul, kaitan dengan Teknologi Kedokteran, referensi, latihan soal, dan alat interaktif: lembar kerja 9 domain HTA, kalkulator ICER dengan bidang efektivitas-biaya, dan simulator akurasi alat diagnostik (PPV/NPV).
- **Tombol Kembali** di kiri atas setiap halaman (juga `Alt` + `←`). Kalau tidak ada halaman sebelumnya, tombol ini membawa ke halaman induk.
- **Foto alat sendiri.** Di Edit alat, pilih ilustrasi bawaan atau unggah foto. Foto tampil lebih dulu di halaman alat lalu berganti ke ilustrasi saat komponennya dipecah.
- **Animasi:** transisi halaman, kartu yang muncul berurutan, angka yang naik, cincin kesiapan, konfeti saat proyek selesai. Bisa dimatikan di **Pengaturan › Animasi**.
- Pencarian sekarang juga menemukan proyek.

## Yang baru di v1.1

- **Tampilan bergaya Lovable.** Latar krem hangat, tombol pil hitam, kartu datar berbingkai tipis, dan gradasi warna hanya di bagian hero. Beranda dibuka dengan kotak pencarian besar seperti kotak chat, jadi langkah pertama selalu "cari alat atau materi".
- **Materi mengikuti file `Materi Teknologi Kedokteran.pdf`.** Judul tanpa nomor = mata kuliah, baris bernomor di bawahnya = sub-materi. Ada 42 mata kuliah silabus dengan 280 sub-materi.
- **Sub-materi bisa dicentang.** Kesiapan tiap alat sekarang dihitung dari sub-materi yang benar-benar dipakai alat itu, bukan hanya dari status mata kuliah.
- **24 alat baru** dari catatan Obsidian `Teknologi Kedokteran\Hardware` dan `Software`: EEG, qEEG, neurofeedback, TMS, ECT, TENS, elektroterapi, diatermi gelombang pendek dan mikro, terapi ultrasound, brace skoliosis, termometer, glukometer, 9 alat laboratorium, BrainWave dan motion correction fMRI. Total 36 alat.
- **Referensi bisa diklik** dan terbuka di browser.

## 1. Menjalankan

1. Klik dua kali `TeknologiKedokteran.exe` di `D:\Project ITS\1_aplikasi Teknologi Kedokteran`.
2. Data ada di folder `data` di sebelah exe.

Kalau muncul pesan "Microsoft Edge WebView2 Runtime tidak ditemukan", pasang **Microsoft Edge WebView2 Runtime (Evergreen Standalone Installer x64)** dari situs Microsoft. Windows 11 biasanya sudah punya runtime ini.

Windows SmartScreen bisa menahan file karena belum bertanda tangan digital: klik **More info › Run anyway**.

## 2. Pembaruan konten otomatis (hanya menambah)

Saat versi baru pertama kali dibuka, aplikasi membandingkan data kamu dengan konten bawaan terbaru lalu **menambahkan** yang belum ada. Tidak ada yang dihapus.

1. Sebelum mengubah apa pun, semua data disalin ke `data\cadangan\<tanggal_jam>\`.
2. Mata kuliah dan sub-materi baru ditambahkan.
3. Mata kuliah lama yang sama dengan silabus diganti ke nama resminya, dan nama lama disimpan sebagai "dulu: …". Ini hanya terjadi kalau kamu belum mengganti namanya sendiri.
4. Mata kuliah lama yang tidak ada di PDF tetap ada dan diberi label **pelengkap**.
5. Alat baru, keterkaitan mata kuliah, dan referensi baru ditambahkan ke alat yang sudah ada.
6. Status belajar, centang, dan catatan pribadimu tidak disentuh.
7. v1.2 menambahkan `bidang` pada mata kuliah dan `ilustrasi` pada alat (hanya bila belum ada), lalu membuat file baru `proyek.json`, `soal.json`, dan `lanjutan.json`. Kalau file itu sudah ada, hanya proyek/soal yang id-nya belum ada yang ditambahkan.

8. v1.3 membuat file baru `modul.json` (penjelasan, topik, studi kasus, daftar bahan kuliah) dan `referensi.json`, menambah alat dan proyek yang id-nya belum ada, menambah soal per mata kuliah (id `m-…`), menambah sub-materi baru, dan menambah keterkaitan mata kuliah ke alat lama hanya bila mata kuliah itu belum terhubung. Semester ditandai pasti hanya bila nilainya masih sama dengan bawaan; semester yang sudah kamu ubah sendiri tidak disentuh.

Pembaruan ini hanya berjalan sekali (dicatat sebagai `versiKonten` di `progres.json`).

## 3. Isi aplikasi

| Halaman | Isi |
|---|---|
| **Beranda** | Kotak pencarian besar, ringkasan (alat, mata kuliah, sub-materi dikuasai), grafik progres per bidang, per semester, dan latihan 14 hari (v1.3), kartu alat yang paling siap kamu pahami, dan mata kuliah yang sedang dipelajari. |
| **Alat Medis** | Katalog alat dengan filter kategori, tampilan kartu atau tabel. |
| **Detail alat** | Anatomi alat (gambar dipecah + garis ke mata kuliah), animasi breakdown komponen (v1.3), kesiapan, tombol Latihan soal, diagram blok, breakdown mata kuliah beserta sub-materi, proyek hands-on, prinsip kerja, keselamatan, sebaran per semester, dan referensi. |
| **Materi Kuliah** | Mata kuliah per semester. Saring menurut sumber (Silabus ITS / Pelengkap), status, dan kategori. |
| **Detail materi** | Navigasi cepat, penjelasan dan topik inti, studi kasus alat yang bisa dicentang, ajakan latihan soal, daftar sub-materi yang bisa dicentang, label alat yang memakai tiap sub-materi, bahan kuliah dari drive D, referensi, catatan pribadi. |
| **Peta Keterkaitan** | Matriks mata kuliah × alat. |
| **Referensi** | Semua referensi per jenis, dengan keterangan alat dan mata kuliah yang memakainya. Cari, saring per jenis atau per alat, buka tautan atau berkas kuliah. |
| **Proyek Hands-on** | Semua proyek per alat, filter bidang (Elektrikal/Informatika/Desain) dan level (Pemula/Menengah/Lanjut). Status Belum mulai / Sedang dikerjakan / Selesai mengikuti langkah yang kamu centang. |
| **Latihan Soal** | Mode Latihan cepat, Match kilat, Urutkan alur sinyal, Studi kasus, Lengkapi diagram blok, Soal hitungan, Kelompokkan, Lengkapi kalimat, Campuran tipe baru, Ulangi yang salah, latihan per mata kuliah, per alat, dan per topik studi lanjutan. |
| **Studi Lanjutan** | HTA, Health Economics, Public Health: modul yang bisa ditandai "Sudah", alat interaktif, referensi, catatan. |
| **Kelola Konten** | Tambah, ubah, hapus alat dan mata kuliah. |
| **Pengaturan** | Tema, ukuran huruf, animasi, nama sapaan, folder data, cadangan. |

## 4. Status belajar dan kesiapan

- **Centang sub-materi** yang sudah kamu kuasai, di halaman detail materi atau langsung di breakdown alat. Status mata kuliah ikut berubah otomatis: belum ada centang = Belum, sebagian = Sedang, semua = Sudah.
- Kamu tetap bisa memilih status mata kuliah secara manual dengan tombol Belum / Sedang / Sudah. Pilihan manual "Sudah" dihitung penuh.
- **Kesiapan kamu** pada tiap alat = rata-rata berbobot dari mata kuliah penyusunnya. Bobotnya: Inti 3, Penting 2, Pendukung 1. Untuk tiap mata kuliah, yang dihitung adalah bagian sub-materi yang dipakai alat itu dan sudah kamu centang.
- Warna titik: **biru = Inti**, **merah muda = Penting**, **abu = Pendukung**.

## 5. Tentang semester "perkiraan"

PDF materi tidak mencantumkan semester. Semester 5 sudah pasti dari jadwalmu (Pengolahan Sinyal Biomedik, Kecerdasan Buatan dan Machine Learning Medis, Interaksi Pasien, Purwarupa, Visualisasi, KDM, DTK). Semester mata kuliah lain adalah perkiraan dan ditandai "(perkiraan)" atau "≈S3". Koreksi lewat **Kelola Konten › Mata kuliah › Edit › Semester**; tanda perkiraan hilang begitu kamu menyimpannya.

Lima mata kuliah belum punya sub-materi karena di PDF juga belum ada rinciannya: KDM, Visualisasi, Big Data, SIMRS, dan Monitoring. Tambahkan sub-materinya saat sudah ada.

**Pembaruan v1.3:** semester 26 mata kuliah sekarang dipastikan dari nama folder `D:\Semester 1` sampai `D:\Semester 5`. KDM dan Visualisasi sudah mendapat sub-materi dari bahan kuliahnya. Yang masih tanpa sub-materi: Big Data, SIMRS, dan Monitoring. Mata kuliah yang foldernya tidak ada di drive D tetap bertanda perkiraan.

## 6. Menambah konten tiap semester

### a. Lewat aplikasi (disarankan)

**Kelola Konten › Tambah mata kuliah.** Isi nama, semester, kategori, sumber, ringkasan, lalu sub-materi satu per baris dengan format:

```
nomor. Nama sub-materi: rincian
```

Contoh:

```
218. Protokol HL7: struktur pesan, segmen
219. DICOM
```

Rincian setelah titik dua boleh dikosongkan. **Jangan ubah nomor yang sudah ada**, karena nomor dipakai untuk menghubungkan sub-materi ke alat. Untuk sub-materi baru, pakai nomor lanjutan dari PDF.

**Kelola Konten › Tambah alat.**
1. Isi informasi alat: nama, singkatan, kategori, ikon emoji (`Win` + `.`), model/merek, ringkasan, prinsip kerja, keselamatan, referensi (satu per baris).
2. Tambah blok satu per satu, urut dari input ke output.
3. Hubungkan mata kuliah: pilih mata kuliah, tingkat peran, tulis perannya, centang blok yang didukung, lalu centang sub-materi yang dipakai.

### b. Lewat file JSON

Struktur satu mata kuliah di `data\materi.json`:

```json
{
  "id": "sinyal",
  "nama": "Pengolahan Sinyal Biomedik",
  "alias": "Pengolahan Sinyal Biomedis",
  "semester": 5,
  "semesterPasti": true,
  "kategori": "Komputasi",
  "sumber": "Silabus ITS",
  "ringkasan": "…",
  "sub": [
    { "no": "116", "nama": "Perencanaan filter digital untuk sinyal biomedik", "rincian": "" }
  ],
  "topik": [],
  "referensi": [],
  "catatan": ""
}
```

Kontribusi di `data\alat.json` sekarang bisa menyebut sub-materi:

```json
{ "materi": "sinyal", "tingkat": 3, "blok": ["filter"], "peran": "Filter digital dan deteksi QRS", "sub": ["116", "119"] }
```

Aturan singkat:
- `id` dan `no` harus unik dan tidak diubah setelah dipakai.
- `kontribusi[].materi` harus sama dengan `id` di `materi.json`, dan `kontribusi[].sub` berisi `no` sub-materi dari mata kuliah itu.
- `tingkat`: 3 Inti, 2 Penting, 1 Pendukung.

Setelah mengedit file, buka **Pengaturan › Muat ulang**. Kalau JSON-nya salah ketik, aplikasi tetap jalan dan menampilkan peringatan.

### c. Menambah proyek dan soal

Proyek ada di `data\proyek.json`. Satu proyek:

```json
{
  "id": "ekg-5",
  "alat": "ekg",
  "tahap": 5,
  "blok": ["filter"],
  "judul": "Filter notch 50 Hz analog",
  "level": "Menengah",
  "durasi": "1 minggu",
  "bidang": ["Elektrikal"],
  "materi": ["elektronika-medis", "elda"],
  "tujuan": "…",
  "bahan": [["Op-amp TL072", 8000], ["Resistor dan kapasitor", 15000]],
  "langkah": ["…", "…"],
  "hasil": "…",
  "keselamatan": "…",
  "referensi": ["Judul: https://…"]
}
```

`alat` = id alat, `blok` = id blok alat itu, `materi` = id mata kuliah, `bahan` = pasangan nama dan harga (0 = sudah punya atau pinjam lab).

Soal ada di `data\soal.json`. Bentuk tiap tipe:

```json
{ "id": "u001", "alat": "ekg", "tipe": "pg", "tanya": "…", "opsi": ["benar", "salah 1", "salah 2", "salah 3"], "jawab": 0, "bahas": "…" }
{ "id": "u002", "alat": "ekg", "tipe": "kasus", "tanya": "Skenario…", "opsi": ["…", "…", "…", "…"], "jawab": 0, "bahas": "…" }
{ "id": "u003", "alat": "ekg", "tipe": "bs", "tanya": "Pernyataan…", "jawab": true, "bahas": "…" }
{ "id": "u004", "alat": "ekg", "tipe": "cocok", "tanya": "Cocokkan…", "pasangan": [["kiri", "kanan"], ["kiri", "kanan"]], "bahas": "…" }
{ "id": "u005", "alat": "ekg", "tipe": "urut", "tanya": "Urutkan…", "item": ["pertama", "kedua", "ketiga"], "bahas": "…" }
```

Tipe baru v1.3 (isi `materi` dengan id mata kuliah agar soal masuk latihan per mata kuliah):

```json
{ "id": "u006", "materi": "kalkulus", "tipe": "isian", "tanya": "…", "jawab": ["jawaban utama", "ejaan lain yang diterima"], "bahas": "…" }
{ "id": "u007", "materi": "eldig", "tipe": "hitung", "tanya": "…", "angka": 2.5, "tol": 0.05, "satuan": "kHz", "bahas": "…" }
{ "id": "u008", "materi": "anatomi", "tipe": "multi", "tanya": "…", "opsi": ["…", "…", "…", "…"], "benar": [0, 2], "bahas": "…" }
{ "id": "u009", "materi": "anatomi", "tipe": "kategori", "tanya": "…", "kelompok": ["Kepala", "Ekstremitas atas"], "item": [["Frontal", 0], ["Ulna", 1]], "bahas": "…" }
{ "id": "u010", "materi": "kalkulus", "tipe": "celah", "tanya": "Lengkapi kalimat berikut.", "teks": "Turunan dari [[0]] adalah [[1]].", "isi": ["sin x", "cos x"], "pengecoh": ["tan x"], "bahas": "…" }
```

`jawab` pada pg/kasus = urutan opsi yang benar, mulai dari 0 (opsi diacak saat tampil). Untuk soal studi lanjutan, isi `alat` dengan `hta`, `he`, atau `ph`. Soal otomatis dari diagram blok tidak perlu ditulis; jumlahnya bertambah sendiri saat kamu menambah alat atau blok.

## 6b. Latihan soal

- Satu soal per layar. Pilih jawaban (bisa dengan tombol `1` sampai `4`), lalu **Periksa** (`Enter`). Pembahasan langsung muncul di bawah.
- Jawaban benar memberi 10 XP, ditambah bonus combo untuk jawaban benar berturut-turut.
- Soal yang salah masuk ke **Ulangi yang salah** dan keluar setelah kamu menjawabnya dengan benar. Pola ini meniru retrieval practice: mengingat kembali lebih melekat daripada membaca ulang.
- **Match kilat**: cocokkan 6 pasangan secepat mungkin, salah pasang menambah 1 detik. Rekor waktumu disimpan.
- Isian singkat tidak membedakan huruf besar dan tanda baca. Hitungan menerima koma atau titik desimal dalam batas toleransi yang tertulis.
- **Kelompokkan:** ketuk istilah, lalu ketuk kelompoknya. **Lengkapi kalimat:** ketuk kata di bank kata untuk mengisi celah yang menyala; ketuk celah untuk mengosongkannya.
- Riwayat latihan (XP, hari beruntun, skor per alat dan per mata kuliah) tersimpan di `progres.json` bagian `latihan`.

## 6c. Foto alat

**Kelola Konten › Edit alat › Pilih foto…** lalu **Simpan alat**. Foto disalin ke `data\gambar\`. Tombol **Pakai ilustrasi saja** melepas foto tanpa menghapus filenya.

## 7. Cadangan dan keamanan data

- Setiap menyimpan, file sebelumnya disalin sebagai `*.json.bak`.
- **Pengaturan › Buat cadangan sekarang** menyalin semua data ke `data\cadangan\<tanggal_jam>\`.
- Untuk pindah laptop, salin seluruh folder `data`.

## 8. Pintasan keyboard

| Pintasan | Fungsi |
|---|---|
| `Ctrl` + `K` | Fokus ke kotak pencarian |
| `↑` `↓` lalu `Enter` | Pilih hasil pencarian |
| `Esc` | Tutup hasil pencarian |
| `Alt` + `←` | Kembali ke halaman sebelumnya (sama dengan tombol Kembali) |
| `1` – `4`, `Enter` | Memilih jawaban dan memeriksa/lanjut saat latihan soal |

## 9. Catatan untuk layar ASUS TUF Gaming A14

Layar 14 inci 2560×1600 pada skala 150% memberi area kerja sekitar 1707×1067 piksel logis.

- Jendela terbuka 1480×940 piksel logis dan otomatis menyesuaikan skala Windows.
- Tiga kolom (menu, konten, panel samping) dipakai di atas 1366 px; di bawahnya panel samping turun, dan di bawah 1007 px menu menyusut jadi ikon.
- Ukuran huruf bisa diubah di Pengaturan. Tema mengikuti Windows dan bisa dipaksa terang atau gelap.

## 10. Membangun ulang dari kode sumber

Butuh Go 1.21 atau lebih baru.

```bat
go-winres make --arch amd64
go build -trimpath -ldflags "-H windowsgui -s -w" -o TeknologiKedokteran.exe .
```

Tampilan ada di folder `web`, konten bawaan di `defaultdata`, dan keduanya tertanam di exe. Konten bawaan dibangun dari PDF dan catatan Obsidian dengan `tools\parse_silabus.py` lalu `tools\build_v2.py`. Konten v1.2 (bidang, ilustrasi, proyek, soal, studi lanjutan) dibangun dengan `tools\build_v3.py`, yang membaca `proyek_v3.py`, `soal_v3.py`, dan `lanjutan_v3.py`. Daftar referensi lengkap ada di `Referensi-v1.2.md`. Konten v1.3 (modul, studi kasus, soal per mata kuliah, 23 alat baru, referensi) dibangun dengan `tools\v4\build_v4.py`; daftar referensinya ditulis `tools\v4\referensi_md.py` ke `Referensi-v1.3.md`.
