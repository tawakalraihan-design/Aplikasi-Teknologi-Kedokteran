# CLAUDE.md: cara kerja di proyek Teknologi Kedokteran

File ini dibaca otomatis oleh Claude Code. Isinya cara kerja yang sudah dipakai sejak v1.0 sampai v1.4, supaya Claude dari akun mana pun bekerja dengan cara yang sama.

## Pemilik dan gaya komunikasi

- Pemilik: Raihan, mahasiswa Teknologi Kedokteran ITS. Di aplikasi ia disapa **"Tuan Raihan"**.
- Selalu pakai **bahasa Indonesia** dan **jelaskan alasan** setiap keputusan.
- Laporan akhir dibuat singkat: apa yang berubah, di mana filenya, dan apa yang perlu ia cek. Rincian panjang ditulis di file (PANDUAN.md, Referensi-vX.Y.md), bukan di chat.
- Kalau permintaan bisa dibaca dua cara, kerjakan tafsiran yang paling mungkin, lalu sebutkan tafsiran itu. Tanya hanya untuk langkah yang tidak bisa dibatalkan.

## Aturan yang tidak boleh dilanggar

1. **Jangan pernah menimpa folder `data\`** milik pengguna. Perubahan isi atau skema dilakukan lewat migrasi di `web/app.js` (`migrateContent`) yang **hanya menambah** (cadangan dulu lewat `api/backup`, tambah item yang id-nya belum ada, lalu naikkan `VERSI_KONTEN`).
2. **Jangan hapus file atau materi.** Setiap update hanya MENAMBAH konten; materi lama tetap ada.
3. Folder sumber milik pengguna (misal `D:\VScode\Neural Network Club\Oralytic`, `D:\Semester N`, vault Obsidian) **hanya dibaca**. Di Oralytic: bobot di `runs/` tidak boleh dipindah atau diubah, dan `runs/tinjauan_fp/KUNCI_jangan_dikirim.csv` tidak boleh dikirim ke mana pun.
4. Lokasi pasang tetap di laptop: `D:\Project ITS\1_aplikasi Teknologi Kedokteran`. Saat update, yang boleh ditimpa hanya `TeknologiKedokteran.exe`, `PANDUAN.md`, dan `kode-sumber.zip`. Yang ditambahkan: `Referensi-vX.Y.md` baru (dan file .md baru lain bila ada). Kalau exe terkunci karena aplikasi sedang terbuka, tulis sebagai `TeknologiKedokteran-vX.Y.exe`.
5. Jangan menulis nama model AI di commit, kode, atau dokumen.

## Arsitektur singkat

- Go + WebView2 (`github.com/jchv/go-webview2`). UI HTML/CSS/JS vanilla di `web/`, konten bawaan di `defaultdata/*.json`, keduanya di-embed ke satu exe (`//go:embed`). Tanpa installer, tanpa internet.
- Data pengguna: `data\*.json` di samping exe (`materi, alat, progres, proyek, soal, lanjutan, modul, referensi, kisah`). Server lokal 127.0.0.1:8765 melayani `api/data`, `api/save/<nama>`, `api/defaults`, `api/backup`, `api/cek-file`, `api/open-file`, dan lainnya (`server.go`).
- Versi iPhone = PWA di `docs/` (GitHub Pages dari branch `main`, folder `/docs`). `web/lokal.js` menjawab `api/*` dari IndexedDB bila hostname bukan 127.0.0.1.
- Saat menambah file data baru, daftarkan namanya di **empat tempat**: `dataFiles` dan daftar `api/defaults` di `server.go`, `NAMA_DATA` dan daftar `defaults` di `web/lokal.js`, `load()` di `web/app.js`, dan `KONTEN` di `migrateContent`.
- File web per fitur: `app.js` (inti, beranda, alat, materi, migrasi), `modul.js` (modul dan Referensi), `kisah.js` (Kisah Deep Learning dan buku), `latihan.js`, `proyek.js`, `lanjutan.js`, `breakdown.js`, `grafik.js`, `ilustrasi.js`, `anatomi.js`.

## Gaya UI

Meniru Lovable: latar krem, tombol pil hitam, kartu datar, gradasi hanya di hero. Warna bidang: Elektrikal oranye, Informatika biru, Desain merah muda, Dasar abu. Target layar ASUS TUF A14 (2560×1600, skala 150%, sekitar 1707×1067). Pastikan tetap rapi di lebar HP 390 px dan di mode gelap. Animasi harus bisa dimatikan (Pengaturan).

## Konten dan pipeline

- Konten ditulis sebagai data Python di `tools/vN/`, lalu dibangun ke `defaultdata/` oleh `build_vN.py` yang **memvalidasi dulu** (id alat, materi, blok, jawaban soal) dan keluar dengan kode 1 bila ada kesalahan. Skrip aman dijalankan ulang: hanya entri buatannya yang diganti.
- Versi terbaru: `python3 tools/v5/build_v5.py` lalu `python3 tools/v5/tulis_md.py` (menulis `Referensi-v1.4.md` dan `Kisah-Deep-Learning-Oralytic.md`). Versi lama tetap di `tools/v4/` dan seterusnya; untuk versi berikutnya buat `tools/v6/`.
- Format soal: `{id, tipe, tanya, bahas, materi, alat?, ...}`; tipe `pg, bs, kasus, cocok, urut, isian, hitung, multi, kategori, celah` (contoh lengkap di `defaultdata/soal.json`).
- Alat memakai DSL `A(id, nama, singkatan, kategori, ikon, ilustrasi, ringkasan, prinsip, keselamatan, blok[(id,nama,fungsi)], kontribusi[(materi, tingkat 1–3, [blok], peran)])`. Ilustrasi memakai arketipe yang sudah ada di `web/ilustrasi.js`.
- Isi konten harus akurat dan berasal dari sumber Raihan (PDF materi, bahan kuliah di `D:\Semester N`, vault Obsidian, folder `Referensi`, kode proyeknya). Tandai bila ada yang berupa perkiraan.

## Langkah rilis (urutan tetap)

1. Naikkan `VERSI_APP` dan `VERSI_KONTEN` di `web/app.js`, versi di `winres/winres.json`, lalu tambahkan cabang migrasi yang hanya menambah.
2. Bangun konten (`tools/vN/build_vN.py`) dan perbarui `PANDUAN.md` (bagian "Yang baru di vX.Y" dan langkah migrasinya) serta `README.md`.
3. Uji di server dev:
   - `go build -o /tmp/tekkes-dev . && /tmp/tekkes-dev <folder-data-uji>` dijalankan di latar belakang, port 8765.
   - Uji migrasi dengan **salinan data versi sebelumnya** (`git show HEAD:defaultdata/x.json` dengan `progres.versiKonten` lama) dan pastikan toast "+N …" muncul serta data lama utuh.
   - Pakai Playwright (sudah terpasang) untuk membuka halaman baru, cek tidak ada error konsol, dan ambil tangkapan layar di 1440 px dan 390 px.
   - Matikan server dengan `kill $(pgrep -x tekkes-dev)`. **Jangan pakai `pkill -f`**, karena itu ikut mematikan shell.
4. Build Windows: `~/go/bin/go-winres make --arch amd64` lalu `GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -trimpath -ldflags "-H windowsgui -s -w" -o build/TeknologiKedokteran.exe .`
5. Build PWA: `python3 tools/build_pwa.py`. Uji lewat `http://localhost:8790` (`python3 -m http.server 8790` di `docs/`); jangan lewat 127.0.0.1, karena alamat itu dianggap mode desktop.
6. Commit dan push ke `main`. Push ini sekaligus memperbarui versi iPhone.
7. Siapkan paket rilis: exe, PANDUAN.md, Referensi-vX.Y.md, dan `git archive --format=zip -o kode-sumber.zip HEAD`. Salin ke folder aplikasi di laptop sesuai aturan nomor 4.
8. Laporkan ke Raihan dengan singkat dan lampirkan file .md barunya.

## Status terakhir

v1.4 (VERSI_KONTEN 5): 66 alat, 58 mata kuliah, 155 proyek, 568 soal, 338 referensi (termasuk 12 buku folder `Referensi` dengan 187 bab), Kisah Deep Learning 20 bab dari kode Oralytic.

Masih terbuka:
- Big Data, SIMRS, dan Monitoring belum punya sub-materi.
- Mata kuliah tanpa folder di drive D masih memakai semester perkiraan.
- Harga bahan proyek masih perkiraan.
- Usulan yang belum dikerjakan: ekspor/impor progres untuk menyamakan HP dan laptop.
