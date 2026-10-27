//go:build windows

package main

import (
	"os/exec"
	"path/filepath"
	"syscall"
	"unsafe"

	webview2 "github.com/jchv/go-webview2"
)

var (
	user32                        = syscall.NewLazyDLL("user32.dll")
	procSetProcessDpiAwarenessCtx = user32.NewProc("SetProcessDpiAwarenessContext")
	procGetDpiForSystem           = user32.NewProc("GetDpiForSystem")
	procMessageBoxW               = user32.NewProc("MessageBoxW")
)

// Ukuran jendela awal dalam piksel logis (sebelum skala Windows).
// Pada ASUS TUF A14 (2560x1600, skala 150%) area kerja ±1706x1018,
// jadi 1480x940 terasa lega tanpa menutupi taskbar.
const (
	logicalWidth  = 1480
	logicalHeight = 940
	minWidth      = 1100
	minHeight     = 700
)

func makeDpiAware() uint {
	if procSetProcessDpiAwarenessCtx.Find() == nil {
		// DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4
		procSetProcessDpiAwarenessCtx.Call(uintptr(^uintptr(3)))
	}
	dpi := uint(96)
	if procGetDpiForSystem.Find() == nil {
		if v, _, _ := procGetDpiForSystem.Call(); v != 0 {
			dpi = uint(v)
		}
	}
	return dpi
}

func showError(msg string) {
	t, _ := syscall.UTF16PtrFromString("Teknologi Kedokteran")
	m, _ := syscall.UTF16PtrFromString(msg)
	procMessageBoxW.Call(0, uintptr(unsafe.Pointer(m)), uintptr(unsafe.Pointer(t)), 0x10)
}

func openFolder(dir string) {
	exec.Command("explorer.exe", dir).Start()
}

func init() {
	openExternal = func(u string) {
		exec.Command("rundll32", "url.dll,FileProtocolHandler", u).Start()
	}
	openFile = func(p string) {
		exec.Command("rundll32", "url.dll,FileProtocolHandler", p).Start()
	}
}

func main() {
	dpi := makeDpiAware()
	scale := func(v uint) uint { return v * dpi / 96 }

	dataDir := resolveDataDir()
	ensureDefaults(dataDir)

	// Port tetap agar pengaturan tampilan (tema) tetap tersimpan; cadangan port acak.
	url, err := startServer("127.0.0.1:47321", dataDir, openFolder)
	if err != nil {
		url, err = startServer("127.0.0.1:0", dataDir, openFolder)
	}
	if err != nil {
		showError("Gagal menjalankan server lokal: " + err.Error())
		return
	}

	w := webview2.NewWithOptions(webview2.WebViewOptions{
		Debug:     false,
		AutoFocus: true,
		DataPath:  filepath.Join(filepath.Dir(dataDir), "WebView2Cache"),
		WindowOptions: webview2.WindowOptions{
			Title:  "Teknologi Kedokteran",
			Width:  scale(logicalWidth),
			Height: scale(logicalHeight),
			IconId: 1,
			Center: true,
		},
	})
	if w == nil {
		// WebView2 Runtime belum terpasang: buka di browser bawaan sebagai cadangan.
		// Aplikasi berhenti saat kotak pesan ini ditutup.
		exec.Command("rundll32", "url.dll,FileProtocolHandler", url).Start()
		showError("Microsoft Edge WebView2 Runtime tidak ditemukan, jadi aplikasi dibuka di browser.\n\nPasang WebView2 Runtime dari situs Microsoft agar tampil sebagai jendela aplikasi sendiri.\n\nJangan tutup kotak pesan ini selama masih memakai aplikasi di browser.")
		return
	}
	defer w.Destroy()
	w.SetSize(int(scale(minWidth)), int(scale(minHeight)), webview2.HintMin)
	w.Navigate(url)
	w.Run()
}
