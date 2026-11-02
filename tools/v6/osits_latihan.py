# -*- coding: utf-8 -*-
"""Soal latihan cepat OSITS (masuk ke soal.json, dipakai mesin Latihan).
Setiap soal punya field "osits": id bidang. Rumus sederhana memakai Unicode, sebagian memakai $...$ (KaTeX)."""


def pg(i, b, tanya, opsi, bahas):
    return {"id": "osits-%02d" % i, "osits": b, "tipe": "pg", "tanya": tanya, "opsi": opsi, "jawab": 0, "bahas": bahas}


def bs(i, b, tanya, jawab, bahas):
    return {"id": "osits-%02d" % i, "osits": b, "tipe": "bs", "tanya": tanya, "jawab": jawab, "bahas": bahas}


def hit(i, b, tanya, angka, tol, satuan, bahas):
    return {"id": "osits-%02d" % i, "osits": b, "tipe": "hitung", "tanya": tanya, "angka": angka, "tol": tol, "satuan": satuan, "bahas": bahas}


def cocok(i, b, tanya, pasangan, bahas):
    return {"id": "osits-%02d" % i, "osits": b, "tipe": "cocok", "tanya": tanya, "pasangan": pasangan, "bahas": bahas}


SOAL = [
    # Mekanika
    pg(1, "mekanika", "Benda bergerak dengan v < 0 dan a < 0. Keadaannya…",
       ["Bergerak ke arah negatif dan makin cepat", "Bergerak ke arah negatif dan makin lambat", "Bergerak ke arah positif dan makin lambat", "Diam sesaat"],
       "Kecepatan dan percepatan searah, jadi besar kecepatan bertambah."),
    hit(2, "mekanika", "Pergi 10 km/jam, pulang lewat jalan sama 20 km/jam. Laju rata-ratanya (km/jam)?", 13.33, 0.1, "km/jam",
        "Rata-rata harmonik: 2·10·20/(10+20) = 40/3 ≈ 13,3 km/jam."),
    pg(3, "mekanika", "Bola pejal (I = ⅖mR²) menggelinding tanpa slip di bidang miring bersudut θ. Percepatannya…",
       ["$\\tfrac57 g\\sin\\theta$", "$g\\sin\\theta$", "$\\tfrac23 g\\sin\\theta$", "$\\tfrac12 g\\sin\\theta$"],
       "a = g sinθ /(1 + I/mR²) = g sinθ/(1 + 2/5) = 5/7 g sinθ. Silinder pejal memberi 2/3, cincin 1/2."),
    pg(4, "mekanika", "Untuk osilasi kecil di sekitar minimum potensial U(x), kuadrat frekuensi sudutnya…",
       ["$U''(x_0)/m$", "$U'(x_0)/m$", "$U(x_0)/m$", "$m\\,U''(x_0)$"],
       "Kembangkan U di sekitar x₀: U ≈ U₀ + ½U″(x₀)(x−x₀)², sehingga ω² = U″/m."),
    hit(5, "mekanika", "U(x) = 4/x³ − 1/x². Di mana titik setimbangnya (x₀)?", 6, 0.01, "",
        "U′ = −12/x⁴ + 2/x³ = 0, sehingga x₀ = 6."),
    bs(6, "mekanika", "Pada sistem katrol tak bermassa, tegangan tali di kedua sisi katrol selalu sama besar.", True,
       "Benar bila katrol tak bermassa dan licin: torsi total harus nol, jadi tegangan kedua sisi sama."),
    pg(7, "mekanika", "Persamaan Hamilton untuk H(q, p) adalah…",
       ["$\\dot q=\\partial H/\\partial p,\\ \\dot p=-\\partial H/\\partial q$", "$\\dot q=-\\partial H/\\partial p,\\ \\dot p=\\partial H/\\partial q$", "$\\dot q=\\partial H/\\partial q,\\ \\dot p=\\partial H/\\partial p$", "$\\dot p=\\partial H/\\partial t$"],
       "Tanda minus ada pada persamaan untuk ṗ."),
    cocok(8, "mekanika", "Cocokkan benda dengan momen inersianya terhadap pusat massa.",
          [["Batang tipis (panjang l)", "1/12 ml²"], ["Silinder pejal", "½ mr²"], ["Bola pejal", "⅖ mr²"], ["Cincin tipis", "mr²"]],
          "Nilai standar yang sering muncul pada soal menggelinding dan Lagrangian."),
    # Elektro
    pg(9, "elektro", "Persamaan Maxwell yang menyatakan tidak ada monopol magnet adalah…",
       ["$\\nabla\\cdot\\vec B=0$", "$\\nabla\\cdot\\vec E=\\rho/\\varepsilon_0$", "$\\nabla\\times\\vec E=-\\partial_t\\vec B$", "$\\nabla\\times\\vec B=\\mu_0\\vec J$"],
       "Divergensi B nol: garis medan magnet selalu tertutup."),
    hit(10, "elektro", "Agar F = (9xy² − y) î − (4y + 3y³) ĵ + a z k̂ bisa menjadi medan magnet, nilai a = …", 4, 0.01, "",
        "∇·F = 9y² − 4 − 9y² + a = 0, sehingga a = 4."),
    hit(11, "elektro", "Potensial 600 V dan medan 400 N/C di titik yang sama dari satu muatan titik. Jaraknya (m)?", 1.5, 0.01, "m",
        "V/E = (kQ/r)/(kQ/r²) = r = 1,5 m."),
    pg(12, "elektro", "Medan listrik di dekat pelat tak hingga dengan rapat muatan σ adalah…",
       ["$\\sigma/2\\varepsilon_0$", "$\\sigma/\\varepsilon_0$", "$2\\sigma/\\varepsilon_0$", "$\\sigma/4\\pi\\varepsilon_0$"],
       "Permukaan Gauss silinder pil: fluks keluar dari dua tutup, 2EA = σA/ε₀."),
    pg(13, "elektro", "Di dalam selubung silinder panjang yang arusnya hanya di permukaan, medan magnetnya…",
       ["Nol", "μ₀I/2πr", "μ₀I/2πa", "μ₀Ir/2πa²"], "Lingkaran Ampère di dalam tidak melingkupi arus."),
    pg(14, "elektro", "Untuk gelombang bidang E₀ cos(k·r − ωt), medan magnetnya…",
       ["$\\vec B=\\tfrac1\\omega\\vec k\\times\\vec E$", "$\\vec B=\\omega\\,\\vec k\\times\\vec E$", "$\\vec B=\\tfrac1\\omega\\vec E\\times\\vec k$", "$\\vec B=c\\,\\vec E$"],
       "Dari ∇×E = −∂B/∂t: i k × E = iωB. Arah B mengikuti k × E."),
    hit(15, "elektro", "Dua gumpal masing-masing massa diam m bergerak 4c/5 berlawanan arah lalu melekat. Massa akhirnya berapa kali m?", 3.333, 0.01, "× m",
        "γ = 5/3, M = 2γm = 10m/3."),
    bs(16, "elektro", "Pada bahan paramagnet, H berlawanan arah dengan M.", False,
       "Paramagnet: χ > 0, jadi M = χH searah H. Yang berlawanan adalah bahan diamagnet (χ < 0)."),
    # Termo
    pg(17, "termo", "Kapasitas kalor molar gas diatomik kaku pada volume tetap adalah…",
       ["5R/2", "3R/2", "7R/2", "3R"], "3 derajat translasi + 2 rotasi = 5, jadi Cv = 5R/2 dan Cp = 7R/2."),
    hit(18, "termo", "Dua benda: T₁ dan T₂ = 2T₁, C₂ = 1,5C₁. Suhu akhirnya berapa kali T₁?", 1.6, 0.01, "× T₁",
        "Tf = (C₁T₁ + 1,5C₁·2T₁)/(2,5C₁) = 1,6T₁."),
    hit(19, "termo", "Gas ideal T = T₀ + aV² (1 mol). Tekanan minimumnya berapa kali R√(aT₀)?", 2, 0.01, "",
        "p = R(T₀/V + aV), minimum di V = √(T₀/a): p = 2R√(aT₀)."),
    pg(20, "termo", "Entropi dalam fisika statistik (Boltzmann) adalah…",
       ["$S=k_B\\ln\\Omega$", "$S=k_B\\Omega$", "$S=\\Omega/k_B$", "$S=-k_B\\Omega\\ln\\Omega$"], "Hubungan Boltzmann antara entropi dan jumlah keadaan mikro."),
    pg(21, "termo", "Paramagnet klasik pada suhu tinggi memenuhi…",
       ["Hukum Curie: M ∝ H/T", "M jenuh = Nμ₀", "M ∝ T", "M tidak bergantung T"], "L(ξ) ≈ ξ/3 untuk ξ = μ₀H/kT ≪ 1, sehingga M = Nμ₀²H/(3kT)."),
    hit(22, "termo", "Dua partikel, masing-masing 10 keadaan, suhu sangat tinggi. Berapa Z_FD?", 45, 0.01, "",
        "Pasangan keadaan berbeda tanpa urutan: C(10,2) = 45. Z_BE = 55, Z_MB = 100."),
    bs(23, "termo", "Untuk gas van der Waals, C_V bergantung pada volume.", False,
       "p linear dalam T, jadi (∂²p/∂T²)_V = 0 dan (∂C_V/∂V)_T = 0."),
    hit(24, "termo", "Termometer X: 10 °F = 40 °X, 55 °F = 70 °X (linear). Pada angka berapa keduanya sama?", 100, 0.5, "",
        "X = (2/3)F + 100/3. Samakan X = F, sehingga F = 100."),
    # Modern
    hit(25, "modern", "Energi foton cahaya 450 nm (eV)?", 2.76, 0.02, "eV", "E = 1240/450 ≈ 2,76 eV."),
    pg(26, "modern", "Transisi hidrogen n = 2 → n = 4…",
       ["Menyerap foton ±486 nm (biru)", "Memancarkan foton ±486 nm", "Menyerap foton ±656 nm (merah)", "Memancarkan foton ±122 nm"],
       "Naik level berarti menyerap. 1/λ = R(1/4 − 1/16), sehingga λ ≈ 486 nm (H-β)."),
    pg(27, "modern", "Dalam model Bohr-Sommerfeld, perbandingan sumbu b/a orbit elips adalah…",
       ["$n_\\phi/(n_r+n_\\phi)$", "$n_r/n_\\phi$", "$n_\\phi/n_r$", "$(n_r+n_\\phi)/n_\\phi$"], "√(1 − ε²) = n_φ/(n_r + n_φ); energi bergantung pada n = n_r + n_φ."),
    bs(28, "modern", "Menambah intensitas cahaya merah 700 nm akan membuat cesium (φ = 2,14 eV) memancarkan elektron.", False,
       "Energi foton 1,77 eV < 2,14 eV. Intensitas hanya menambah jumlah foton, bukan energi per foton."),
    hit(29, "modern", "Massa efektif elektron bebas berapa kali m_e?", 1, 0.001, "× m_e", "E = ħ²k²/2m_e, sehingga d²E/dk² = ħ²/m_e dan m_ef = m_e."),
    # Kuantum
    pg(30, "kuantum", "Komutator posisi dan momentum adalah…", ["$i\\hbar$", "$-i\\hbar$", "$\\hbar$", "0"], "[x̂, p̂]f = iħf."),
    hit(31, "kuantum", "⟨V⟩ elektron hidrogen keadaan dasar (eV)?", -27.2, 0.2, "eV", "⟨1/r⟩ = 1/a₀, sehingga ⟨V⟩ = −e²/(4πε₀a₀) = 2E₁ = −27,2 eV."),
    hit(32, "kuantum", "A = [[3, −i],[2i, 4]], ψ = (1, i). Berapakah ⟨A⟩?", 5, 0.01, "", "ψ†Aψ = 10, ψ†ψ = 2, jadi ⟨A⟩ = 5."),
    pg(33, "kuantum", "Agar operator Â membangkitkan simetri bagi Ĥ, syaratnya…",
       ["Â hermitian dan [Â, Ĥ] = 0", "Â uniter dan [Â, Ĥ] ≠ 0", "Â = Ĥ²", "Â komut dengan x̂"], "Pembangkit simetri harus hermitian (observabel) dan komut dengan Ĥ, sehingga ⟨A⟩ kekal."),
    pg(34, "kuantum", "Osilator harmonik ditambah medan listrik −qℰx. Energi eigennya…",
       ["$\\hbar\\omega(n+\\tfrac12)-q^2\\mathcal E^2/2m\\omega^2$", "$\\hbar\\omega(n+\\tfrac12)$", "$\\hbar\\omega(n+\\tfrac12)+q\\mathcal E$", "$\\hbar\\omega n$"],
       "Lengkapkan kuadrat: osilator tergeser x₀ = qℰ/mω² dan energi turun sebesar q²ℰ²/2mω²."),
    bs(35, "kuantum", "Untuk fungsi gelombang keadaan terikat yang riil, ⟨p⟩ selalu nol.", True,
       "⟨p⟩ = −iħ∫ψψ′dx harus riil, padahal integralnya riil dan dikali −i; satu-satunya kemungkinan adalah nol."),
    pg(36, "kuantum", "Pusat paket gelombang Gauss partikel bebas bergerak dengan kecepatan…",
       ["$\\hbar k_0/m$", "$\\hbar k_0/2m$", "c", "0 (paket hanya melebar)"], "⟨x⟩_t = ħk₀t/m, kecepatan grup dω/dk = ħk/m."),
]
