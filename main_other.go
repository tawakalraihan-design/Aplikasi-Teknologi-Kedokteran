//go:build !windows

package main

import (
	"fmt"
	"os"
)

// Mode pratinjau untuk non-Windows: jalankan server lalu buka URL di browser.
func main() {
	dataDir := resolveDataDir()
	if len(os.Args) > 1 {
		dataDir = os.Args[1]
		os.MkdirAll(dataDir, 0o755)
	}
	ensureDefaults(dataDir)
	url, err := startServer("127.0.0.1:8765", dataDir, nil)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println("Buka di browser:", url, "data:", dataDir)
	select {}
}
