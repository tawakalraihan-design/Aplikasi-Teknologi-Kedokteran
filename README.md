# Teknologi Kedokteran

Aplikasi desktop Windows untuk mahasiswa Teknologi Kedokteran: katalog 36 alat medis dengan anatomi alat (gambar dipecah per komponen dan ditarik ke mata kuliah), 58 mata kuliah (42 dari silabus, 280 sub-materi) yang dikelompokkan per bidang (Informatika, Elektrikal, Desain, Dasar), 109 proyek hands-on, latihan soal bergaya Duolingo/Quizlet, dan studi lanjutan HTA, Health Economics, serta Public Health.

- Satu file `.exe`, tanpa installer dan tanpa internet.
- UI: HTML/CSS/JS yang ditanam ke dalam binary Go, ditampilkan lewat WebView2.
- Konten tersimpan sebagai JSON di folder `data`, bisa diedit lewat aplikasi atau langsung.

Cara pakai dan cara menambah konten ada di [PANDUAN.md](PANDUAN.md).

## Struktur

| Path | Isi |
|---|---|
| `main_windows.go` | Jendela WebView2, DPI awareness, ukuran jendela. |
| `main_other.go` | Mode pratinjau di Linux/macOS lewat browser. |
| `server.go` | Server lokal 127.0.0.1, baca/tulis JSON (materi, alat, progres, proyek, soal, lanjutan), cadangan, konten bawaan (`/api/defaults`) untuk migrasi, unggah foto alat ke `data/gambar`. |
| `web/` | Antarmuka: `index.html`, `styles.css`, `app.js` (inti, navigasi, alat, materi, kelola), `ilustrasi.js` (gambar SVG per komponen), `anatomi.js` (exploded view + mindmap), `proyek.js`, `latihan.js`, `lanjutan.js`, `main.js` (start). |
| `defaultdata/` | Konten bawaan; disalin saat pertama dijalankan dan ditambahkan ke data lama lewat migrasi (`versiKonten`). |
| `tools/` | `parse_silabus.py` (PDF → `silabus.json`), `build_v2.py` (v1 + silabus + Obsidian), `build_v3.py` (bidang, ilustrasi, `proyek_v3.py`, `soal_v3.py`, `lanjutan_v3.py` → `defaultdata`), `referensi_v3.py` (→ `Referensi-v1.2.md`). |
| `winres/` | Ikon dan metadata exe. |

## Build

```bash
go-winres make --arch amd64
GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -trimpath -ldflags "-H windowsgui -s -w" -o build/TeknologiKedokteran.exe .
```

Pratinjau di Linux: `go run . ./data` lalu buka http://127.0.0.1:8765/
