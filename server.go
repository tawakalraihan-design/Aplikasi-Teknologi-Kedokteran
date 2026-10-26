package main

import (
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"io"
	"io/fs"
	"net"
	"net/http"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"time"
)

//go:embed web
var webFS embed.FS

//go:embed defaultdata/*.json
var defaultFS embed.FS

// Nama file konten yang boleh dibaca/ditulis lewat API.
var dataFiles = []string{"materi", "alat", "progres", "proyek", "soal", "lanjutan"}

var writeMu sync.Mutex

// openExternal membuka URL di browser bawaan (diisi oleh main_windows.go).
var openExternal func(string)

// resolveDataDir memilih folder "data" di samping program. Jika folder itu
// tidak bisa ditulis (misalnya di Program Files), pakai folder AppData.
func resolveDataDir() string {
	if exe, err := os.Executable(); err == nil {
		dir := filepath.Join(filepath.Dir(exe), "data")
		if canWrite(dir) {
			return dir
		}
	}
	if cfg, err := os.UserConfigDir(); err == nil {
		dir := filepath.Join(cfg, "TeknologiKedokteran", "data")
		if canWrite(dir) {
			return dir
		}
	}
	return "data"
}

func canWrite(dir string) bool {
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return false
	}
	probe := filepath.Join(dir, ".tulis-uji")
	if err := os.WriteFile(probe, []byte("ok"), 0o644); err != nil {
		return false
	}
	os.Remove(probe)
	return true
}

// ensureDefaults menyalin konten contoh bila file data belum ada.
func ensureDefaults(dir string) {
	for _, name := range dataFiles {
		target := filepath.Join(dir, name+".json")
		if _, err := os.Stat(target); err == nil {
			continue
		}
		b, err := defaultFS.ReadFile("defaultdata/" + name + ".json")
		if err != nil {
			continue
		}
		os.WriteFile(target, b, 0o644)
	}
}

func validName(name string) bool {
	for _, n := range dataFiles {
		if n == name {
			return true
		}
	}
	return false
}

func newHandler(dataDir string, openFolder func(string)) http.Handler {
	mux := http.NewServeMux()
	static, _ := fs.Sub(webFS, "web")
	mux.Handle("/", http.FileServer(http.FS(static)))

	mux.HandleFunc("/api/data", func(w http.ResponseWriter, r *http.Request) {
		out := map[string]json.RawMessage{}
		errs := map[string]string{}
		for _, name := range dataFiles {
			b, err := os.ReadFile(filepath.Join(dataDir, name+".json"))
			if err != nil {
				b, _ = defaultFS.ReadFile("defaultdata/" + name + ".json")
			}
			if !json.Valid(b) {
				errs[name] = "File " + name + ".json tidak valid (cek koma/tanda kutip). Memakai data kosong."
				if name == "progres" {
					b = []byte("{}")
				} else {
					b = []byte("[]")
				}
			}
			out[name] = b
		}
		eb, _ := json.Marshal(errs)
		out["errors"] = eb
		db, _ := json.Marshal(dataDir)
		out["dataDir"] = db
		w.Header().Set("Content-Type", "application/json; charset=utf-8")
		w.Header().Set("Cache-Control", "no-store")
		json.NewEncoder(w).Encode(out)
	})

	mux.HandleFunc("/api/save/", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "metode tidak didukung", http.StatusMethodNotAllowed)
			return
		}
		name := strings.TrimPrefix(r.URL.Path, "/api/save/")
		if !validName(name) {
			http.Error(w, "nama data tidak dikenal", http.StatusBadRequest)
			return
		}
		body, err := io.ReadAll(io.LimitReader(r.Body, 20<<20))
		if err != nil || !json.Valid(body) {
			http.Error(w, "isi bukan JSON yang valid", http.StatusBadRequest)
			return
		}
		// json.Indent menjaga urutan field agar file tetap enak dibaca/diedit.
		var buf bytes.Buffer
		json.Indent(&buf, body, "", "  ")
		formatted := buf.Bytes()

		writeMu.Lock()
		defer writeMu.Unlock()
		target := filepath.Join(dataDir, name+".json")
		if old, err := os.ReadFile(target); err == nil {
			os.WriteFile(target+".bak", old, 0o644)
		}
		tmp := target + ".tmp"
		if err := os.WriteFile(tmp, formatted, 0o644); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		if err := os.Rename(tmp, target); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		w.Write([]byte(`{"ok":true}`))
	})

	mux.HandleFunc("/api/backup", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "metode tidak didukung", http.StatusMethodNotAllowed)
			return
		}
		stamp := time.Now().Format("2006-01-02_150405")
		dir := filepath.Join(dataDir, "cadangan", stamp)
		if err := os.MkdirAll(dir, 0o755); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		for _, name := range dataFiles {
			if b, err := os.ReadFile(filepath.Join(dataDir, name+".json")); err == nil {
				os.WriteFile(filepath.Join(dir, name+".json"), b, 0o644)
			}
		}
		json.NewEncoder(w).Encode(map[string]string{"folder": dir})
	})

	mux.HandleFunc("/api/open-folder", func(w http.ResponseWriter, r *http.Request) {
		if openFolder != nil {
			openFolder(dataDir)
		}
		w.Write([]byte(`{"ok":true}`))
	})

	// Ekspor progres: file JSON ditulis di samping folder data (di samping exe), lalu foldernya dibuka.
	mux.HandleFunc("/api/ekspor", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "metode tidak didukung", http.StatusMethodNotAllowed)
			return
		}
		body, err := io.ReadAll(io.LimitReader(r.Body, 64<<20))
		if err != nil || !json.Valid(body) {
			http.Error(w, "isi ekspor tidak valid", http.StatusBadRequest)
			return
		}
		dir := filepath.Dir(dataDir)
		file := filepath.Join(dir, "ekspor-progres-"+time.Now().Format("2006-01-02_150405")+".json")
		if err := os.WriteFile(file, body, 0o644); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		if openFolder != nil {
			openFolder(dir)
		}
		json.NewEncoder(w).Encode(map[string]string{"file": file})
	})

	// Konten bawaan versi terbaru, dipakai aplikasi untuk menambahkan materi/alat baru ke data pengguna.
	mux.HandleFunc("/api/defaults", func(w http.ResponseWriter, r *http.Request) {
		out := map[string]json.RawMessage{}
		for _, name := range []string{"materi", "alat", "proyek", "soal", "lanjutan"} {
			b, _ := defaultFS.ReadFile("defaultdata/" + name + ".json")
			out[name] = b
		}
		w.Header().Set("Content-Type", "application/json; charset=utf-8")
		json.NewEncoder(w).Encode(out)
	})

	// Foto alat milik pengguna disimpan di data/gambar/.
	gambarDir := filepath.Join(dataDir, "gambar")
	mux.Handle("/gambar/", http.StripPrefix("/gambar/", http.FileServer(http.Dir(gambarDir))))
	mux.HandleFunc("/api/upload-gambar", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "metode tidak didukung", http.StatusMethodNotAllowed)
			return
		}
		ext := strings.ToLower(r.URL.Query().Get("ext"))
		name := filepath.Base(r.URL.Query().Get("nama"))
		if !map[string]bool{"jpg": true, "jpeg": true, "png": true, "webp": true, "gif": true}[ext] || name == "" || name == "." || strings.ContainsAny(name, `/\:`) {
			http.Error(w, "nama atau jenis file tidak valid", http.StatusBadRequest)
			return
		}
		body, err := io.ReadAll(io.LimitReader(r.Body, 15<<20))
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		os.MkdirAll(gambarDir, 0o755)
		file := name + "." + ext
		if err := os.WriteFile(filepath.Join(gambarDir, file), body, 0o644); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		json.NewEncoder(w).Encode(map[string]string{"file": file})
	})

	// Link referensi dibuka di browser bawaan, bukan di dalam jendela aplikasi.
	mux.HandleFunc("/api/open-url", func(w http.ResponseWriter, r *http.Request) {
		u := r.URL.Query().Get("u")
		if openExternal != nil && (strings.HasPrefix(u, "https://") || strings.HasPrefix(u, "http://")) {
			openExternal(u)
		}
		w.Write([]byte(`{"ok":true}`))
	})

	return mux
}

// startServer menjalankan server lokal (hanya 127.0.0.1) dan mengembalikan URL-nya.
func startServer(addr string, dataDir string, openFolder func(string)) (string, error) {
	ln, err := net.Listen("tcp", addr)
	if err != nil {
		return "", err
	}
	go http.Serve(ln, newHandler(dataDir, openFolder))
	return fmt.Sprintf("http://%s/", ln.Addr().String()), nil
}
