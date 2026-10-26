# Teknologi Kedokteran — Panduan Pemakaian (v1.2)

Aplikasi desktop Windows untuk belajar alat Teknologi Kedokteran dan melihat mata kuliah serta sub-materi apa saja yang membangun tiap alat. Semua data tersimpan di laptopmu, tanpa internet.

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

Pembaruan ini hanya berjalan sekali (dicatat sebagai `versiKonten` di `progres.json`).

## 3. Isi aplikasi

| Halaman | Isi |
|---|---|
| **Beranda** | Kotak pencarian besar, ringkasan (alat, mata kuliah, sub-materi dikuasai), kartu alat yang paling siap kamu pahami, dan mata kuliah yang sedang dipelajari. |
| **Alat Medis** | Katalog alat dengan filter kategori, tampilan kartu atau tabel. |
| **Detail alat** | Anatomi alat (gambar dipecah + garis ke mata kuliah), kesiapan, tombol Latihan soal, diagram blok, breakdown mata kuliah beserta sub-materi, proyek hands-on, prinsip kerja, keselamatan, sebaran per semester, dan referensi. |
| **Materi Kuliah** | Mata kuliah per semester. Saring menurut sumber (Silabus ITS / Pelengkap), status, dan kategori. |
| **Detail materi** | Daftar sub-materi yang bisa dicentang, label alat yang memakai tiap sub-materi, catatan pribadi. |
| **Peta Keterkaitan** | Matriks mata kuliah × alat. |
| **Proyek Hands-on** | Semua proyek per alat, filter bidang (Elektrikal/Informatika/Desain) dan level (Pemula/Menengah/Lanjut). Status Belum mulai / Sedang dikerjakan / Selesai mengikuti langkah yang kamu centang. |
| **Latihan Soal** | Mode Latihan cepat, Match kilat, Urutkan alur sinyal, Studi kasus, Ulangi yang salah, latihan per alat, dan latihan per topik studi lanjutan. |
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

`jawab` pada pg/kasus = urutan opsi yang benar, mulai dari 0 (opsi diacak saat tampil). Untuk soal studi lanjutan, isi `alat` dengan `hta`, `he`, atau `ph`. Soal otomatis dari diagram blok tidak perlu ditulis; jumlahnya bertambah sendiri saat kamu menambah alat atau blok.

## 6b. Latihan soal

- Satu soal per layar. Pilih jawaban (bisa dengan tombol `1` sampai `4`), lalu **Periksa** (`Enter`). Pembahasan langsung muncul di bawah.
- Jawaban benar memberi 10 XP, ditambah bonus combo untuk jawaban benar berturut-turut.
- Soal yang salah masuk ke **Ulangi yang salah** dan keluar setelah kamu menjawabnya dengan benar. Pola ini meniru retrieval practice: mengingat kembali lebih melekat daripada membaca ulang.
- **Match kilat**: cocokkan 6 pasangan secepat mungkin, salah pasang menambah 1 detik. Rekor waktumu disimpan.
- Riwayat latihan (XP, hari beruntun, skor per alat) tersimpan di `progres.json` bagian `latihan`.

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

Tampilan ada di folder `web`, konten bawaan di `defaultdata`, dan keduanya tertanam di exe. Konten bawaan dibangun dari PDF dan catatan Obsidian dengan `tools\parse_silabus.py` lalu `tools\build_v2.py`. Konten v1.2 (bidang, ilustrasi, proyek, soal, studi lanjutan) dibangun dengan `tools\build_v3.py`, yang membaca `proyek_v3.py`, `soal_v3.py`, dan `lanjutan_v3.py`. Daftar referensi lengkap ada di `Referensi-v1.2.md`.
