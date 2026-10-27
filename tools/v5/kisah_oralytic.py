"""Kisah Deep Learning dari kode Oralytic (D:\\VScode\\Neural Network Club\\Oralytic).

Seluruh kode Oralytic (oralai/stage00..stage11, cam.py, fdi.py, onnx_infer.py,
configs/*.yaml, tests/, .vscode/, requirements.txt) diartikan menjadi cerita
dengan pola yang diminta Tuan Raihan:
  1. "Deep learning adalah ..."
  2. "Jika kita ingin membentuk ini, maka kita harus membuat ..."
  3. "Bayangkan jika Anda ingin membuat program seperti ini, pastinya Anda membutuhkan ..."
  4. "Bayangkan Anda seperti membuat kue ..."
Angka diambil dari docs/STATUS_RISET.md dan configs/experiment.yaml.
Folder Oralytic hanya dibaca; tidak ada file di sana yang diubah.
"""

SUMBER = "D:\\VScode\\Neural Network Club\\Oralytic"

RESEP = [
    # (bahan kue, padanan deep learning, file Oralytic)
    ("Dapur, oven, dan timbangan", "Lingkungan koding: Python .venv, PyTorch + CUDA, GPU RTX 4050, VS Code", ".venv, requirements.txt, .vscode/"),
    ("Buku resep", "File konfigurasi YAML: semua angka eksperimen ditulis di satu tempat", "configs/experiment.yaml"),
    ("Tepung, telur, gula", "Data: foto intraoral beserta label kotak gigi dan karies", "stage01_acquire.py, configs/sources.yaml"),
    ("Mengayak dan menakar", "Pra-pemrosesan dan augmentasi gambar", "stage02_preprocess.py"),
    ("Takaran yang seimbang", "Penyeimbangan kelas: karies lebih jarang daripada gigi sehat", "stage03_balance.py"),
    ("Adonan cicip disisihkan", "Pemisahan train/val/test per pasien", "stage04_split.py"),
    ("Loyang dan cetakan", "Arsitektur jaringan saraf: CNN ResNet50, EfficientNet-B0, YOLO", "stage05_architecture.py"),
    ("Memanggang lapis pertama", "Melatih detektor gigi (YOLO)", "stage06_tooth_detect.py"),
    ("Memanggang lapis kedua", "Melatih classifier karies per gigi (backpropagation)", "stage07_identify.py"),
    ("Memanggang tiga kali", "Eksperimen berulang dengan seed 0, 1, 2", "stage08_train.py"),
    ("Mencicipi", "Evaluasi: sensitivitas, spesifisitas, AUC, interval kepercayaan", "stage09_evaluate.py"),
    ("Menumpuk kue lapis", "Pipeline dua tahap: deteksi lalu klasifikasi", "stage10_pipeline.py"),
    ("Menulis nama di kue", "Penomoran gigi FDI dan odontogram", "fdi.py, orientation.py"),
    ("Membelah kue untuk melihat isinya", "Heatmap Grad-CAM: bagian gambar yang membuat model yakin", "cam.py"),
    ("Juri pencicip", "Tinjauan buta oleh dokter gigi, Cohen kappa", "stage11_review.py"),
    ("Dus kue untuk dijual", "Ekspor ONNX dan pemasangan di aplikasi Health Hub", "onnx_infer.py, scripts/ekspor_onnx.py"),
    ("Uji rasa sebelum dijual", "Unit test otomatis dengan pytest", "tests/"),
]

BAB = []


def B(bid, judul, tahap, file, adalah, bentuk, bayangkan, kue, langkah, kode, angka, istilah, materi, catatan=""):
    BAB.append({
        "id": bid, "judul": judul, "tahap": tahap, "file": list(file),
        "adalah": adalah, "bentuk": bentuk, "bayangkan": bayangkan, "kue": kue,
        "langkah": list(langkah),
        "kode": {"file": kode[0], "isi": kode[1].strip("\n"), "ket": kode[2]} if kode else None,
        "angka": [{"label": a, "nilai": b} for a, b in angka],
        "istilah": [{"nama": a, "arti": b} for a, b in istilah],
        "materi": list(materi), "catatan": catatan,
    })


# ---------------------------------------------------------------- 0
B("pembuka", "Apa itu deep learning, dan kue apa yang sedang kita buat", "Pembuka",
  ["README.md", "CLAUDE.md", "docs/STATUS_RISET.md"],
  "Deep learning adalah cara membuat komputer belajar dari banyak contoh, bukan dari aturan yang kita tulis satu per satu. "
  "Komputer diberi ribuan foto beserta jawabannya (gigi ini sehat, gigi itu karies), lalu sebuah jaringan saraf tiruan berlapis-lapis "
  "mengatur jutaan angka di dalamnya (disebut bobot) sampai tebakannya cocok dengan jawaban. Disebut \"deep\" karena lapisannya banyak: "
  "lapisan awal mengenali garis dan warna, lapisan tengah mengenali bentuk tonjolan gigi, lapisan akhir mengenali pola lubang karies.",
  "Jika kita ingin membentuk sebuah sistem yang bisa melihat foto mulut lalu menunjuk gigi mana yang berlubang, seperti Oralytic, "
  "maka kita harus membuat lima hal: (1) dapur kerja berupa lingkungan Python dengan GPU, (2) kumpulan data foto yang sudah dilabeli, "
  "(3) model jaringan saraf yang cocok untuk gambar, (4) proses pelatihan yang mengubah bobot model sedikit demi sedikit, dan "
  "(5) cara menguji dengan jujur apakah model benar-benar pintar atau hanya menghafal. Oralytic menyusun kelimanya menjadi 12 tahap, "
  "stage00 sampai stage11, yang semuanya dijalankan lewat satu pintu: python -m oralai.cli.",
  "Bayangkan jika Anda ingin membuat program seperti ini: pengguna memotret gigi dengan HP, lalu aplikasi Health Hub menampilkan "
  "gigi nomor berapa yang dicurigai karies dan seberapa yakin. Pastinya Anda membutuhkan detektor yang menemukan setiap gigi di foto, "
  "classifier yang memeriksa tiap gigi satu per satu, penomoran gigi FDI agar dokter paham gigi mana yang dimaksud, heatmap agar "
  "keputusan model bisa dijelaskan, dan file model ringan (ONNX) yang bisa jalan di aplikasi tanpa PyTorch.",
  "Bayangkan Anda seperti membuat kue lapis. Anda butuh dapur dan oven (komputer dan GPU), buku resep (file konfigurasi), "
  "bahan seperti tepung dan telur (data foto), cetakan (arsitektur model), waktu memanggang (training), dan yang paling penting: "
  "mencicipi dengan jujur sebelum dijual (evaluasi). Kue Oralytic punya dua lapis: lapis bawah mencari gigi, lapis atas memeriksa karies. "
  "Di bab-bab berikut, setiap file kode Oralytic akan kita baca sebagai satu langkah membuat kue.",
  ["Masalah: karies sering tidak disadari sampai nyeri; foto HP bisa jadi skrining awal.",
   "Solusi: AI dua tahap, deteksi gigi lalu klasifikasi karies per gigi, dibandingkan dengan YOLO satu tahap.",
   "Pengembangan: penomoran gigi FDI dan odontogram, heatmap penjelas, ekspor ONNX ke aplikasi Health Hub.",
   "Setiap tahap punya file sendiri (stage00 sampai stage11) supaya bisa diuji dan diulang terpisah."],
  ("oralai/cli.py", """
python -m oralai.cli stage00                    # cek konfigurasi & GPU
python -m oralai.cli stage01 download aku       # unduh dataset
python -m oralai.cli stage04 caries_v1          # bangun dataset + split per pasien
python -m oralai.cli stage06 train tooth_v1     # latih detektor gigi
python -m oralai.cli stage07 train teeth_lesions_v1 --backbone resnet50
python -m oralai.cli stage09 compare runs/A/seed0 runs/B/seed0
python -m oralai.cli stage10 run GIGI.pt PENYAKIT.pt FOTO.jpg
""", "Satu pintu untuk semua tahap. Urutan perintah ini adalah urutan resep kue dari awal sampai jadi."),
  [("Tahap pipeline", "12 (stage00–stage11)"), ("Foto dataset AKU", "6.313 foto HP"), ("Model di aplikasi", "oralytic_twostage_v4 (ONNX)")],
  [("Jaringan saraf tiruan", "Susunan fungsi matematika berlapis yang meniru cara neuron menyambung; tiap sambungan punya bobot."),
   ("Bobot (weight)", "Angka yang diubah-ubah selama training; pengetahuan model tersimpan di sini."),
   ("Pipeline", "Urutan tahap kerja dari data mentah sampai hasil akhir.")],
  ["ml-medis", "citra", "pemrograman", "ilmu-data"])

# ---------------------------------------------------------------- 1
B("dapur", "Menyiapkan dapur: lingkungan koding", "Persiapan",
  [".venv/", "requirements.txt", ".vscode/settings.json", ".vscode/launch.json", "oralai/stage00_config.py"],
  "Deep learning adalah pekerjaan hitung yang sangat berat: satu kali training classifier bisa berisi miliaran perkalian. "
  "Karena itu deep learning hampir selalu butuh kartu grafis (GPU) yang mampu menghitung ribuan perkalian sekaligus, "
  "dan pustaka seperti PyTorch yang tahu cara menyuruh GPU bekerja.",
  "Jika kita ingin membentuk proyek deep learning yang bisa diulang hasilnya, maka kita harus membuat lingkungan yang terkunci: "
  "folder .venv berisi Python dan pustaka dengan versi tertentu (numpy, pillow, pyyaml, scipy, pytest, ultralytics, dan torch versi CUDA), "
  "pengaturan VS Code agar folder data dan runs yang besar tidak ikut diindeks, dan fungsi set_seed agar angka acak selalu sama setiap kali dijalankan.",
  "Bayangkan jika Anda ingin membuat program seperti ini di laptop sendiri (RTX 4050 6 GB, RAM 31 GB). Pastinya Anda membutuhkan "
  "satu perintah untuk mengecek apakah GPU terbaca (stage00), satu daftar pustaka yang bisa dipasang ulang di laptop lain (requirements.txt), "
  "dan tombol F5 di VS Code yang langsung menjalankan tahap tertentu (launch.json). Tanpa itu, hasil yang bagus hari ini bisa tidak bisa diulang besok.",
  "Bayangkan Anda seperti membuat kue: sebelum menyentuh tepung, Anda menyiapkan dapur. Oven harus dipanaskan (GPU dan CUDA), "
  "timbangan harus dikalibrasi (versi pustaka dikunci), dan buku resep diletakkan di meja (configs/experiment.yaml). "
  "set_seed itu seperti memakai timer yang sama setiap kali memanggang, supaya kue hari ini dan kue minggu depan rasanya sama.",
  ["Buat virtual environment: python -m venv .venv, lalu aktifkan.",
   "Pasang torch versi CUDA lebih dulu, baru pip install -r requirements.txt (ultralytics ikut memasang torchvision).",
   "Jalankan python -m oralai.cli stage00 untuk mencetak versi Python, torch, CUDA, dan nama GPU.",
   "Kecualikan data/, runs/, .venv/ dari pencarian VS Code agar editor tetap ringan.",
   "Semua angka eksperimen (epoch, batch, learning rate) dibaca dari YAML, bukan ditulis di kode."],
  ("oralai/stage00_config.py", """
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass
""", "Mengunci semua sumber angka acak (Python, NumPy, PyTorch CPU dan GPU). Inilah alasan eksperimen Oralytic bisa diulang."),
  [("GPU", "RTX 4050 Laptop, 6 GB VRAM"), ("RAM", "31 GB"), ("Seed eksperimen", "0, 1, 2"), ("Ultralytics", "8.4")],
  [("Virtual environment (.venv)", "Folder Python terpisah per proyek agar versi pustaka tidak bentrok."),
   ("CUDA", "Platform NVIDIA agar PyTorch bisa menghitung di GPU."),
   ("Seed", "Angka awal pembangkit bilangan acak; seed sama berarti urutan acak sama.")],
  ["pemrograman", "ml-medis", "sistem-tertanam"])

# ---------------------------------------------------------------- 2
B("resep", "Buku resep: file konfigurasi YAML", "Persiapan",
  ["configs/experiment.yaml", "configs/builds.yaml", "configs/labels.yaml", "configs/sources.yaml"],
  "Deep learning adalah proses yang punya banyak kenop pengatur, disebut hyperparameter: berapa kali data diputar (epoch), "
  "berapa foto sekali proses (batch), seberapa besar langkah belajar (learning rate), sampai kapan berhenti bila tidak membaik (patience). "
  "Hasil model sangat bergantung pada kenop ini.",
  "Jika kita ingin membentuk eksperimen yang adil, maka kita harus membuat buku resep yang tertulis rapi: experiment.yaml berisi "
  "nilai bawaan (imgsz 640, epochs 100, patience 30, batch 16, lr 0,0003 dengan AdamW dan jadwal cosine) dan daftar eksperimen yang "
  "hanya mengubah satu hal dari bawaan. builds.yaml berisi resep dataset, labels.yaml berisi kamus label, sources.yaml berisi asal dataset.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan ingin membandingkan model tanpa augmentasi dengan model yang memakai augmentasi. "
  "Pastinya Anda membutuhkan dua eksperimen yang semua kenopnya sama kecuali satu (augment: none vs dental). Kalau kenopnya ditulis "
  "tersebar di kode, Anda tidak akan pernah yakin perbandingannya adil.",
  "Bayangkan Anda seperti membuat kue dan ingin tahu apakah tambahan mentega membuat kue lebih lembut. Anda harus memanggang dua kue "
  "dengan resep yang sama persis, beda hanya di mentega. experiment.yaml adalah buku resep itu: ss_baseline dan ss_augmented sama-sama "
  "YOLO11s 30 epoch, bedanya hanya ada augmentasi gigi atau tidak.",
  ["defaults: seeds [0,1,2], imgsz 640, epochs 100, patience 30, batch 16, det_conf 0,25.",
   "Classifier: cls_imgsz 224, cls_epochs 15, cls_batch 32, cls_patience 5, lr 3e-4, weight_decay 1e-4.",
   "Eksperimen satu tahap: ss_baseline, ss_augmented, ss_dentalai. Detektor: tooth_detector, fdi_yolo32 (imgsz 1024).",
   "Classifier: id_baseline_resnet50, id_augmented_resnet50, id_augmented_efficientnet_b0, id_mix_resnet50.",
   "labels.yaml menyatukan sinonim: 'caries', 'karies', 'decay' menjadi satu label; tooth_11 sampai tooth_48 untuk FDI."],
  ("configs/experiment.yaml", """
defaults:
  seeds: [0, 1, 2]
  imgsz: 640
  epochs: 100
  patience: 30
  batch: 16
  lr: 0.0003          # AdamW, jadwal cosine
  weight_decay: 0.0001
  balance: weighted_loss
  bootstrap: 1000
""", "Kenop bersama semua eksperimen. Eksperimen hanya menimpa kenop yang ingin diuji."),
  [("Learning rate", "0,0003"), ("Epoch detektor", "100 (patience 30)"), ("Epoch classifier", "15 (patience 5)"), ("Bootstrap CI", "1.000 kali")],
  [("Hyperparameter", "Pengaturan yang dipilih manusia sebelum training, bukan dipelajari model."),
   ("Epoch", "Satu putaran penuh model melihat semua data training."),
   ("Batch", "Sekelompok foto yang diproses bersama sebelum bobot diperbarui.")],
  ["ml-medis", "metopen", "pemrograman"])

# ---------------------------------------------------------------- 3
B("bahan", "Mengumpulkan bahan: data dan label", "Bahan",
  ["oralai/stage01_acquire.py", "oralai/formats.py", "configs/sources.yaml", "configs/labels.yaml"],
  "Deep learning adalah murid yang hanya sepintar contoh yang diberikan kepadanya. Model tidak tahu apa itu karies; ia hanya tahu "
  "pola yang muncul berulang di foto yang dilabeli karies. Karena itu data dan label adalah bahan terpenting, lebih penting dari model.",
  "Jika kita ingin membentuk detektor karies yang tangguh, maka kita harus membuat kumpulan data dari beberapa sumber, lalu "
  "menyeragamkannya. Oralytic memakai dataset AKU (6.313 foto HP, Zenodo), DentalAI (anotasi poligon Supervisely), IOP-Compass "
  "(nomor gigi FDI), dan AlphaDent (uji eksternal). Tiap sumber punya format berbeda (COCO, VOC, LabelMe, Supervisely, YOLO, folder), "
  "jadi stage01 mengubah semuanya menjadi satu format kanonik JSONL dengan label yang sudah disatukan lewat labels.yaml.",
  "Bayangkan jika Anda ingin membuat program seperti ini dari foto yang dikirim pengguna. Pastinya Anda membutuhkan contoh foto yang "
  "mirip foto pengguna (foto HP, bukan hanya foto klinik), kotak penanda tiap gigi dan lesi, kamus yang menyamakan nama label, dan "
  "sidik jari gambar (dhash) untuk menemukan foto kembar yang tidak boleh terhitung dua kali.",
  "Bayangkan Anda seperti membuat kue: tepung dari empat toko berbeda dikemas dalam kantong dengan satuan berbeda (gram, ons, cangkir). "
  "Sebelum dipakai, semuanya dituang ke wadah yang sama dan ditimbang dengan satuan yang sama. stage01 adalah proses menuang ulang itu, "
  "dan labels.yaml adalah tabel konversi satuannya.",
  ["Unduh dataset dari Zenodo (stage01 download aku) atau taruh di data/raw/.",
   "Baca format apa pun lewat formats.py: COCO, Pascal VOC, LabelMe, Supervisely, YOLO txt, atau folder per kelas.",
   "Tulis ulang ke JSONL kanonik: satu baris per foto berisi path, ukuran, kotak, dan label.",
   "Satukan label lewat ontologi: sinonim dipetakan ke satu nama, anak label (misal karies dentin) bisa diangkat ke induknya.",
   "Hitung dhash tiap foto untuk menemukan duplikat."],
  None,
  [("Dataset AKU", "6.313 foto HP"), ("Sumber data", "4 (AKU, DentalAI, IOP-Compass, AlphaDent)"), ("Format yang dibaca", "6 jenis anotasi")],
  [("Label / anotasi", "Jawaban yang ditempel manusia pada data, misal kotak di sekitar gigi berlubang."),
   ("Ontologi label", "Kamus resmi nama label beserta sinonim dan hubungan induk-anak."),
   ("dhash", "Sidik jari gambar 64-bit; dua foto mirip punya dhash yang bedanya sedikit.")],
  ["ilmu-data", "manajemen-data", "citra", "ml-medis"],
  "Lisensi dataset dicatat di sources.yaml. IOP-Compass berlisensi CC BY-NC-SA, jadi tidak boleh dipakai komersial.")

# ---------------------------------------------------------------- 4
B("ayak", "Mengayak dan menakar: pra-pemrosesan dan augmentasi", "Bahan",
  ["oralai/stage02_preprocess.py"],
  "Deep learning adalah metode yang mudah tertipu oleh hal sepele: foto yang sedikit lebih gelap atau sedikit miring bisa membuat model ragu. "
  "Augmentasi adalah cara melatih model agar kebal terhadap variasi itu, dengan memberi versi foto yang sengaja diubah-ubah sedikit.",
  "Jika kita ingin membentuk model yang tetap benar walau foto pengguna gelap, miring, atau tidak di tengah, maka kita harus membuat "
  "preset augmentasi khusus gigi. Preset 'dental' di Oralytic mengubah warna sedikit (hue 0,005; saturasi 0,4; kecerahan 0,3), memutar "
  "sampai 10 derajat, menggeser 10%, memperbesar-perkecil 30%, membalik kiri-kanan 50%, dan menggabung empat foto jadi satu (mosaic).",
  "Bayangkan jika Anda ingin membuat program seperti ini yang juga menomori gigi. Pastinya Anda membutuhkan preset terpisah, 'dental_fdi', "
  "yang mematikan flip kiri-kanan. Alasannya: kalau foto dibalik, gigi 11 pindah ke posisi gigi 21 tetapi labelnya tetap 11, sehingga model "
  "diajari jawaban yang salah. Untuk classifier per gigi, transformasinya RandomResizedCrop 0,8–1, flip, rotasi 10°, ColorJitter 0,2, lalu "
  "dinormalisasi dengan rata-rata dan simpangan baku ImageNet.",
  "Bayangkan Anda seperti membuat kue: tepung diayak supaya tidak menggumpal, dan Anda berlatih membuat adonan dengan tepung dari "
  "berbagai merek supaya tangan Anda terbiasa. Augmentasi adalah latihan dengan 'merek tepung' berbeda: foto yang sama dibuat lebih terang, "
  "lebih miring, atau digeser, sehingga model tidak bergantung pada satu kondisi foto saja. Tapi jangan sampai mengubah resep: membalik "
  "foto saat menomori gigi itu seperti menukar gula dengan garam.",
  ["Preset none: semua augmentasi nol (pembanding).",
   "Preset dental: hsv_h 0,005, hsv_s 0,4, hsv_v 0,3, degrees 10, translate 0,1, scale 0,3, fliplr 0,5, mosaic 1, close_mosaic 10.",
   "Preset dental_fdi: sama dengan dental tetapi fliplr 0.",
   "Classifier: augmentasi hanya saat train; saat val/test hanya resize + normalisasi.",
   "close_mosaic 10: mosaic dimatikan di 10 epoch terakhir agar model sempat melihat foto utuh."],
  ("oralai/stage02_preprocess.py", """
DETECTOR_AUG = {
    "dental": dict(hsv_h=0.005, hsv_s=0.4, hsv_v=0.3, degrees=10.0,
                   translate=0.1, scale=0.3, fliplr=0.5, mosaic=1.0,
                   close_mosaic=10),
}
# Nomor FDI: flip kiri-kanan menukar sisi (11 <-> 21) tanpa
# menukar labelnya -> label salah.
DETECTOR_AUG["dental_fdi"] = {**DETECTOR_AUG["dental"], "fliplr": 0.0}
""", "Dua preset augmentasi. Komentar di kode menjelaskan alasan flip dimatikan untuk penomoran gigi."),
  [("Rotasi maksimum", "10°"), ("Peluang flip", "50% (0% untuk FDI)"), ("ΔAUC karena augmentasi", "+0,020 (McNemar p = 0,034)")],
  [("Augmentasi", "Membuat variasi data training secara acak agar model lebih tahan banting."),
   ("Normalisasi ImageNet", "Mengurangi rata-rata (0,485; 0,456; 0,406) dan membagi simpangan baku tiap kanal warna."),
   ("Mosaic", "Empat foto ditempel jadi satu agar model melihat banyak objek dan latar sekaligus.")],
  ["citra", "ml-medis", "statistika"])

# ---------------------------------------------------------------- 5
B("takar", "Menakar dengan adil: menyeimbangkan kelas", "Bahan",
  ["oralai/stage03_balance.py"],
  "Deep learning adalah proses meminimalkan kesalahan rata-rata. Masalahnya, kalau 90% gigi sehat dan hanya 10% karies, model bisa "
  "mendapat akurasi 90% hanya dengan menjawab 'sehat' untuk semua gigi, dan tidak pernah belajar mengenali karies.",
  "Jika kita ingin membentuk model yang peduli pada kelas yang jarang, maka kita harus membuat penimbang. stage03 menyediakan tiga cara: "
  "bobot kelas di fungsi loss (w_c = N / (K × n_c), kelas jarang diberi bobot besar), oversampling (foto kelas jarang diambil lebih sering), "
  "dan repeat factor untuk detektor. Oralytic memakai weighted_loss sebagai bawaan.",
  "Bayangkan jika Anda ingin membuat program seperti ini untuk skrining. Pastinya Anda membutuhkan model yang lebih takut melewatkan "
  "karies daripada salah menuduh gigi sehat, karena karies yang terlewat akan memburuk. Bobot kelas membuat satu kesalahan pada gigi karies "
  "terasa lebih 'mahal' bagi model.",
  "Bayangkan Anda seperti membuat kue cokelat-keju, tetapi stok keju Anda sedikit sekali. Kalau Anda mencicip adonan secara acak, "
  "rasa keju hampir tidak pernah terasa. Supaya keju tetap terasa, setiap gigitan keju Anda beri perhatian lebih besar. "
  "Itulah bobot kelas: gigi karies yang langka diberi bobot lebih berat saat menghitung kesalahan.",
  ["Hitung jumlah sampel per kelas n_c dan jumlah total N.",
   "Bobot kelas w_c = N / (K × n_c); K = banyak kelas.",
   "Pakai bobot itu di CrossEntropyLoss(weight=w) saat training.",
   "Alternatif: WeightedRandomSampler dengan bobot 1/n_c per sampel (oversample).",
   "Laporkan imbalance ratio di stage03 sebelum training."],
  ("oralai/stage03_balance.py", """
def class_weights(labels, k):
    n, c = len(labels), Counter(labels)
    return [n / (k * c[i]) if c[i] else 0.0 for i in range(k)]


def sample_weights(labels):
    c = Counter(labels)
    return [1.0 / c[y] for y in labels]
""", "Dua baris rumus yang menentukan seberapa 'penting' tiap kelas saat model dihukum karena salah."),
  [("Rumus bobot", "w_c = N / (K · n_c)"), ("Mode bawaan", "weighted_loss")],
  [("Ketidakseimbangan kelas", "Satu kelas jauh lebih banyak daripada kelas lain."),
   ("Weighted loss", "Fungsi kesalahan yang memberi bobot berbeda per kelas."),
   ("Oversampling", "Mengambil sampel kelas langka lebih sering saat training.")],
  ["statistika", "ml-medis", "data-mining"])

# ---------------------------------------------------------------- 6
B("sisih", "Menyisihkan adonan cicip: split per pasien", "Bahan",
  ["oralai/stage04_split.py", "configs/builds.yaml"],
  "Deep learning adalah murid yang sangat pandai menghafal. Kalau soal ujian sama dengan soal latihan, nilainya pasti tinggi, padahal "
  "belum tentu ia paham. Karena itu data harus dibagi tiga: train untuk belajar, validation untuk memilih model terbaik, test untuk ujian akhir "
  "yang tidak pernah dilihat sebelumnya.",
  "Jika kita ingin membentuk ujian yang jujur untuk data medis, maka kita harus membuat pemisahan per pasien, bukan per foto. Satu pasien "
  "bisa punya beberapa foto dari sudut berbeda; kalau satu foto masuk train dan foto lain pasien yang sama masuk test, model hanya mengenali "
  "pasien itu. Oralytic menemukan masalah ini: 87% foto test punya pasien yang juga ada di train. stage04 memperbaikinya dengan hash_split "
  "(MD5 dari ID pasien) dan membuang foto kembar dengan dhash (jarak Hamming ≤ 8).",
  "Bayangkan jika Anda ingin membuat program seperti ini dan melaporkan AUC di skripsi. Pastinya Anda membutuhkan bukti bahwa angka itu "
  "berlaku untuk pasien baru. Split per pasien yang deterministik juga berarti: menambah data baru tidak mengacak ulang pembagian data lama, "
  "jadi hasil eksperimen lama tetap bisa dibandingkan.",
  "Bayangkan Anda seperti membuat kue untuk lomba. Sebelum memanggang, Anda menyisihkan satu mangkuk adonan untuk dicicipi juri. "
  "Kalau mangkuk juri diambil dari adonan yang sudah Anda cicipi berkali-kali saat mengaduk, Anda akan tertipu oleh lidah sendiri. "
  "Mangkuk juri harus dari adonan yang benar-benar terpisah, dan untuk data medis, 'adonan terpisah' berarti pasien yang berbeda.",
  ["Angkat label anak ke induk bila diminta resep build (lift to parent).",
   "Buang duplikat: dua foto dengan dhash berbeda ≤ 8 bit dianggap sama.",
   "Bagi per pasien dengan hash_split: MD5(ID pasien) dipetakan ke train/val/test sesuai rasio.",
   "Tempatkan file (hardlink bila aman, simpan ulang JPEG bila perlu diputar atau dibalik).",
   "Tulis label format YOLO (kelas, x_tengah, y_tengah, lebar, tinggi; dinormalisasi 0–1) dan pratinjau."],
  ("oralai/stage04_split.py", """
def hash_split(group, ratios):
    \"\"\"Split deterministik per grup: menambah data baru tidak
    mengacak ulang data lama.\"\"\"
    x = int(hashlib.md5(group.encode()).hexdigest(), 16) / 16 ** 32
    total, acc = sum(ratios.values()), 0.0
    for name, r in ratios.items():
        acc += r / total
        if x < acc:
            return name
    return name
""", "ID pasien diubah menjadi angka 0–1 yang selalu sama, lalu dipetakan ke train, val, atau test."),
  [("Kebocoran sebelum diperbaiki", "87% foto test berbagi pasien dengan train"), ("Ambang duplikat", "Hamming ≤ 8 bit")],
  [("Data leakage", "Informasi dari data uji bocor ke training sehingga skor terlihat lebih baik dari kenyataan."),
   ("Train / validation / test", "Data belajar, data pemilih model, dan data ujian akhir."),
   ("Hash", "Fungsi yang mengubah teks menjadi angka acak tetapi selalu sama untuk teks yang sama.")],
  ["ml-medis", "metopen", "statistika", "ilmu-data"])

# ---------------------------------------------------------------- 7
B("cetakan", "Memilih cetakan: arsitektur jaringan saraf", "Model",
  ["oralai/stage05_architecture.py"],
  "Deep learning adalah tumpukan lapisan. Untuk gambar, lapisan utamanya adalah konvolusi: jendela kecil (misal 3×3) yang digeser di "
  "seluruh gambar untuk mencari pola. Puluhan lapis konvolusi bertumpuk menjadi Convolutional Neural Network (CNN) seperti ResNet50 "
  "(50 lapis, sekitar 25 juta bobot) atau EfficientNet-B0 (lebih kecil dan hemat).",
  "Jika kita ingin membentuk classifier karies tanpa jutaan foto, maka kita harus membuat model dari CNN yang sudah dilatih di ImageNet "
  "(transfer learning), lalu mengganti kepala terakhirnya. build_classifier mengambil ResNet50 atau EfficientNet-B0 bawaan torchvision, "
  "mencari lapisan Linear terakhir, dan menggantinya dengan Linear baru yang keluarannya sebanyak kelas kita (misal sehat dan karies).",
  "Bayangkan jika Anda ingin membuat program seperti ini yang harus jalan cepat di aplikasi. Pastinya Anda membutuhkan tabel pembanding "
  "arsitektur: jumlah parameter, jumlah perkalian (MACs) per gambar, latensi, dan FPS. stage05 menghitung semuanya sehingga Anda bisa memilih "
  "model yang cukup akurat tetapi tidak terlalu berat.",
  "Bayangkan Anda seperti membuat kue dan tidak perlu menempa loyang sendiri. Anda membeli loyang bagus yang sudah teruji (ResNet50 yang "
  "sudah belajar dari 1,2 juta foto ImageNet), lalu hanya mengganti tutupnya agar pas dengan kue Anda (kepala Linear 2 kelas). "
  "Loyang besar membuat kue tinggi tapi lama matang; loyang kecil cepat matang tapi kuenya tipis. Pilih sesuai kebutuhan.",
  ["Daftar backbone di experiment.yaml (architectures): ResNet50, EfficientNet-B0, dan lainnya.",
   "Muat bobot pralatih: get_model(name, weights='DEFAULT').",
   "Ganti lapisan Linear terakhir dengan Linear(in_features, n_kelas).",
   "Hitung layer_stats: jumlah lapis konvolusi, ukuran filter, stride, parameter (juta).",
   "Hitung MACs dan ukur latensi untuk memilih model."],
  ("oralai/stage05_architecture.py", """
def _replace_head(model, n_classes):
    \"\"\"Ganti lapisan Linear TERAKHIR dengan Linear(in, n_classes).\"\"\"
    name, last = [(n, m) for n, m in model.named_modules()
                  if isinstance(m, nn.Linear)][-1]
    parent = model
    *path, attr = name.split(".")
    for p in path:
        parent = getattr(parent, p)
    setattr(parent, attr, nn.Linear(last.in_features, n_classes))
    return model
""", "Transfer learning dalam sembilan baris: badan model dipertahankan, hanya 'kepala' yang diganti."),
  [("Input classifier", "224 × 224 piksel"), ("Pilihan backbone", "ResNet50, EfficientNet-B0"), ("Input detektor", "640 px (FDI 1024 px)")],
  [("Konvolusi", "Operasi jendela geser yang mengalikan filter kecil dengan potongan gambar."),
   ("Transfer learning", "Memakai model yang sudah dilatih pada data besar sebagai titik awal."),
   ("MACs", "Multiply-accumulate: banyak perkalian-penjumlahan untuk satu gambar; ukuran beban hitung.")],
  ["ml-medis", "citra", "matek", "pemrograman"])

# ---------------------------------------------------------------- 8
B("lapis1", "Lapis pertama: detektor gigi dengan YOLO", "Memanggang",
  ["oralai/stage06_tooth_detect.py", "yolo11s.pt", "weights/yolo26n.pt"],
  "Deep learning adalah cara menemukan letak benda, bukan hanya menamai gambar. Detektor seperti YOLO (You Only Look Once) melihat "
  "seluruh foto sekali jalan lalu mengeluarkan banyak kotak beserta kelas dan tingkat keyakinannya.",
  "Jika kita ingin membentuk lapis pertama Oralytic, yaitu menemukan setiap gigi di foto, maka kita harus membuat detektor YOLO yang dilatih "
  "dengan kotak gigi. Di dalam YOLO ada backbone (pengekstrak fitur), neck (menggabung fitur berbagai ukuran), head (memprediksi kotak), dan "
  "NMS (membuang kotak ganda). Loss-nya gabungan CIoU (seberapa pas kotak), BCE (kelas benar atau tidak), dan DFL (ketajaman tepi kotak).",
  "Bayangkan jika Anda ingin membuat program seperti ini dan training-nya berhenti di tengah karena laptop panas. Pastinya Anda membutuhkan "
  "fitur resume: stage06 menyimpan last.pt setiap epoch dan bisa melanjutkan dari situ. Kode Oralytic bahkan mencatat jebakan nyata: "
  "device harus disebut saat resume, kalau tidak training jatuh ke CPU dan memakan RAM sekitar 10 GB.",
  "Bayangkan Anda seperti membuat kue lapis: lapis pertama harus matang sempurna, karena lapis kedua diletakkan di atasnya. "
  "Kalau detektor melewatkan satu gigi, classifier tidak akan pernah memeriksa gigi itu. Itulah sebabnya detektor gigi Oralytic "
  "dilatih sampai mAP@0,5 = 0,952 sebelum lapis kedua dibuat.",
  ["Siapkan build tooth_v1 di stage04 (satu kelas: tooth).",
   "Latih: YOLO('yolo11s.pt').train(data, seed, deterministic=True, augmentasi dental).",
   "Simpan best.pt (mAP terbaik di val) dan last.pt (untuk resume).",
   "Prediksi: kotak dengan keyakinan ≥ det_conf 0,25 dipakai ke tahap berikutnya.",
   "Pembanding: YOLO satu tahap yang langsung mendeteksi karies (ss_baseline, ss_augmented)."],
  ("oralai/stage06_tooth_detect.py", """
YOLO(model).train(
    data=str(data_yaml), project=str(out.parent), name=out.name,
    seed=seed, deterministic=True, device=yolo_device(hp),
    **{k: hp[k] for k in HP_KEYS if k in hp},
    **detector_augmentation(augment),
)
best = out / "weights" / "best.pt"
""", "Training detektor memakai Ultralytics. Semua kenop datang dari experiment.yaml dan preset augmentasi stage02."),
  [("mAP@0,5 detektor gigi", "0,952"), ("YOLO satu tahap (AKU) AUC", "0,981"), ("Ambang deteksi", "0,25")],
  [("Bounding box", "Kotak (x1, y1, x2, y2) yang membungkus objek."),
   ("IoU", "Luas irisan dibagi luas gabungan dua kotak; 1 berarti kotak sama persis."),
   ("mAP@0,5", "Rata-rata presisi semua kelas bila deteksi dianggap benar saat IoU ≥ 0,5."),
   ("NMS", "Non-Maximum Suppression: membuang kotak yang tumpang tindih dengan kotak lebih yakin.")],
  ["ml-medis", "citra", "pencitraan"])

# ---------------------------------------------------------------- 9
B("lapis2", "Lapis kedua: classifier karies dan backpropagation", "Memanggang",
  ["oralai/stage07_identify.py"],
  "Deep learning adalah siklus tebak, hitung salah, perbaiki. Model menebak (forward), fungsi loss mengukur seberapa salah tebakannya, "
  "backpropagation menghitung arah perbaikan untuk setiap bobot memakai aturan rantai turunan, lalu optimizer menggeser bobot sedikit "
  "ke arah itu: W_baru = W_lama − learning_rate × gradien. Siklus ini diulang ribuan kali.",
  "Jika kita ingin membentuk lapis kedua Oralytic, yaitu memeriksa tiap gigi, maka kita harus membuat potongan foto per gigi lebih dulu "
  "(crop dengan margin 10% di sekitar kotak gigi), memberi label tiap potongan (sehat atau karies; tambalan dianggap sehat), lalu melatih "
  "CNN dengan AdamW, jadwal learning rate cosine, dan early stopping berdasarkan macro-F1 di data validasi.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan bertanya: kapan training harus berhenti? Pastinya Anda membutuhkan aturan: "
  "simpan model setiap kali macro-F1 validasi membaik, dan berhenti bila 5 epoch berturut-turut tidak membaik (cls_patience 5). "
  "Dengan begitu yang dipakai adalah model terbaik, bukan model terakhir yang mungkin sudah mulai menghafal (overfitting).",
  "Bayangkan Anda seperti membuat kue dan memanggangnya sambil terus mengintip. Setiap beberapa menit Anda tusuk dengan lidi (validasi). "
  "Kalau masih basah, panggang lagi dan sesuaikan suhu (optimizer mengubah bobot). Suhu oven diturunkan pelan-pelan menjelang akhir "
  "(jadwal cosine). Begitu tusukan lidi tidak membaik lagi beberapa kali, keluarkan kue sebelum gosong (early stopping).",
  ["make_crops: potong setiap kotak gigi dengan margin 10%; gigi yang tumpang tindih lesi ≥ 50% diberi label lesi.",
   "CropDataset: baca potongan, terapkan transformasi stage02.",
   "Model: build_classifier(backbone, n_kelas); loss CrossEntropy berbobot kelas.",
   "Optimizer AdamW (lr 3e-4, weight_decay 1e-4) dan CosineAnnealingLR.",
   "Tiap epoch: _run_epoch train lalu val; simpan best.pt bila macro-F1 naik; berhenti bila 5 epoch tanpa perbaikan."],
  ("oralai/stage07_identify.py", """
def _run_epoch(model, loader, loss_fn, device, opt=None):
    model.train(opt is not None)
    with torch.set_grad_enabled(opt is not None):
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            logits = model(x)                # forward: menebak
            loss = loss_fn(logits, y)        # seberapa salah
            if opt is not None:
                opt.zero_grad()
                loss.backward()  # backpropagation (chain rule)
                opt.step()       # W_baru = W_lama - lr * gradien
""", "Jantung deep learning. Semua model di Oralytic, dan hampir semua deep learning di dunia, belajar dengan empat baris ini."),
  [("AUC id_augmented_resnet50", "0,964"), ("Margin crop", "10%"), ("Early stopping", "5 epoch tanpa perbaikan")],
  [("Loss", "Angka yang mengukur seberapa salah tebakan model; makin kecil makin baik."),
   ("Backpropagation", "Menghitung gradien loss terhadap setiap bobot dari lapisan akhir mundur ke awal."),
   ("Optimizer AdamW", "Aturan menggeser bobot memakai gradien, dengan momentum dan peluruhan bobot."),
   ("Overfitting", "Model hafal data training tetapi buruk di data baru.")],
  ["ml-medis", "kalkulus", "matek", "citra"])

# ---------------------------------------------------------------- 10
B("tiga-kali", "Memanggang tiga kali: eksperimen dan seed", "Memanggang",
  ["oralai/stage08_train.py", "runs/"],
  "Deep learning adalah proses yang mengandung keacakan: urutan data, augmentasi, dan bobot awal kepala model semuanya acak. "
  "Satu kali training bisa kebetulan beruntung. Hasil yang bisa dipercaya adalah rata-rata dari beberapa kali training dengan seed berbeda.",
  "Jika kita ingin membentuk klaim ilmiah seperti 'augmentasi meningkatkan AUC', maka kita harus membuat setiap eksperimen dijalankan "
  "dengan seed 0, 1, dan 2, lalu dilaporkan sebagai rata-rata ± simpangan baku. stage08 menjalankan semua eksperimen di experiment.yaml, "
  "menyimpan hasil per seed di runs/<eksperimen>/seed<N>/, membuat ringkasan, dan membandingkan pasangan eksperimen.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan dosen bertanya: apakah selisih 0,02 itu nyata atau kebetulan? "
  "Pastinya Anda membutuhkan beberapa ulangan dan uji statistik. Tanpa itu, Anda tidak bisa membedakan perbaikan sungguhan dari keberuntungan.",
  "Bayangkan Anda seperti membuat kue untuk menguji resep baru. Satu kue enak bisa karena kebetulan oven sedang pas. Anda memanggang tiga "
  "kali dengan resep yang sama, lalu mencatat rata-rata dan seberapa beda hasilnya. Kalau resep baru selalu lebih enak di ketiga percobaan, "
  "barulah Anda yakin.",
  ["Baca daftar eksperimen dari experiment.yaml.",
   "run_one: untuk tiap seed, latih detektor atau classifier dan simpan metrik.",
   "summarize: rata-rata ± SD semua metrik lintas seed.",
   "compare: pasangan eksperimen (misal baseline vs augmented) diuji dengan McNemar dan selisih AUC.",
   "Bobot di runs/ tidak dipindah atau diubah setelah jadi; itu arsip hasil penelitian."],
  None,
  [("Seed per eksperimen", "3"), ("Contoh hasil", "ss_augmented AUC 0,981 (AKU)"), ("Augmentasi vs tanpa", "ΔAUC +0,020, p = 0,034")],
  [("Rata-rata ± SD", "Ringkasan hasil beberapa ulangan dan seberapa besar variasinya."),
   ("Reproducibility", "Orang lain bisa mendapat hasil yang sama dengan kode dan data yang sama.")],
  ["metopen", "statistika", "ml-medis"])

# ---------------------------------------------------------------- 11
B("cicip", "Mencicipi dengan jujur: evaluasi medis", "Menguji",
  ["oralai/stage09_evaluate.py"],
  "Deep learning adalah alat bantu yang harus dinilai dengan ukuran dunia medis, bukan hanya akurasi. Dokter ingin tahu: dari semua gigi karies, "
  "berapa yang tertangkap (sensitivitas)? Dari semua gigi sehat, berapa yang benar dinyatakan sehat (spesifisitas)? Seberapa baik model "
  "memisahkan keduanya di semua ambang (AUC)?",
  "Jika kita ingin membentuk evaluasi yang bisa dipertanggungjawabkan, maka kita harus membuat matriks konfusi (TP, FP, TN, FN), lalu "
  "menghitung Se, Sp, PPV, NPV, F1, diagnostic odds ratio, AUC (lewat uji Mann-Whitney), interval kepercayaan Wilson, bootstrap per pasien "
  "1.000 kali, kalibrasi (Brier dan ECE), ambang Youden, uji McNemar untuk membandingkan dua model, dan Cohen kappa untuk kesepakatan.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan memasangnya di aplikasi publik. Pastinya Anda membutuhkan ambang keputusan "
  "yang dipilih dengan sadar. Ambang rendah menangkap banyak karies tapi banyak alarm palsu; ambang tinggi sebaliknya. Model di aplikasi "
  "Health Hub memakai ambang 0,971 setelah meninjau positif palsu bersama dokter gigi.",
  "Bayangkan Anda seperti membuat kue lalu mengundang juri. Anda tidak cukup bertanya 'enak atau tidak'. Anda ingin tahu: berapa juri yang "
  "suka (sensitivitas), apakah juri yang tidak suka memang alasannya kuat (spesifisitas), dan seberapa yakin Anda bahwa hasilnya tidak berubah "
  "kalau jurinya diganti (interval kepercayaan dan bootstrap).",
  ["Hitung TP, FP, TN, FN pada ambang tertentu.",
   "Se = TP/(TP+FN); Sp = TN/(TN+FP); PPV = TP/(TP+FP); NPV = TN/(TN+FN).",
   "AUC dari peringkat skor (setara uji Mann-Whitney U).",
   "Interval kepercayaan Wilson untuk proporsi; bootstrap per pasien untuk AUC.",
   "Kalibrasi: Brier score dan ECE; ambang Youden J = Se + Sp − 1 maksimum."],
  ("oralai/stage09_evaluate.py", """
def auc(y, s):
    from scipy.stats import rankdata
    y, s = np.asarray(y, bool), np.asarray(s, float)
    npos, nneg = int(y.sum()), int((~y).sum())
    if npos == 0 or nneg == 0:
        return None
    r = rankdata(s)
    return float((r[y].sum() - npos * (npos + 1) / 2) / (npos * nneg))
""", "AUC dihitung dari peringkat: peluang skor gigi karies lebih tinggi daripada skor gigi sehat yang dipilih acak."),
  [("Dua tahap end-to-end (DentalAI)", "AUC 0,923; Se 0,966; Sp 0,734"), ("Ambang di aplikasi", "0,971"), ("Bootstrap", "1.000 kali per pasien")],
  [("Sensitivitas", "Proporsi kasus sakit yang terdeteksi positif."),
   ("Spesifisitas", "Proporsi kasus sehat yang terdeteksi negatif."),
   ("AUC", "Luas di bawah kurva ROC; 0,5 = tebak koin, 1 = sempurna."),
   ("Kalibrasi", "Kesesuaian probabilitas model dengan frekuensi nyata.")],
  ["statistika", "metopen", "ml-medis", "ilmu-data"])

# ---------------------------------------------------------------- 12
B("susun", "Menyusun kue lapis: pipeline dua tahap", "Menyajikan",
  ["oralai/stage10_pipeline.py", "scripts/latency_e2e.py"],
  "Deep learning adalah komponen, bukan selalu seluruh sistem. Oralytic menggabungkan dua model: detektor gigi dan classifier karies. "
  "Gabungan ini disebut pipeline dua tahap, dan hasilnya dibandingkan dengan YOLO satu tahap yang langsung mendeteksi karies.",
  "Jika kita ingin membentuk laporan per gigi, maka kita harus membuat kelas TwoStage dengan metode analyze: buka foto dan koreksi rotasi "
  "EXIF, deteksi gigi, potong tiap gigi, klasifikasikan semua potongan, hitung peluang penyakit = 1 − peluang sehat, lalu ringkas gigi mana "
  "yang melewati ambang. Metode draw menggambar kotak dan label di foto.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan memilih antara dua tahap atau satu tahap. Pastinya Anda membutuhkan "
  "perbandingan yang adil: dua tahap lebih bisa dijelaskan per gigi, tetapi lebih lambat (152 ms per foto) dibanding satu tahap (78 ms). "
  "Keputusan arsitektur selalu tukar-menukar antara akurasi, kecepatan, dan kemudahan dijelaskan.",
  "Bayangkan Anda seperti membuat kue lapis: lapis bawah (detektor) dipanggang, lalu setiap potong diberi lapis atas (classifier). "
  "Kue lapis lebih indah dan setiap potong bisa diberi hiasan berbeda, tetapi butuh waktu lebih lama daripada bolu satu loyang. "
  "Pilihan tergantung siapa yang menunggu.",
  ["Buka foto, ImageOps.exif_transpose agar orientasi benar, ubah ke RGB.",
   "detect_teeth: kotak gigi dengan keyakinan ≥ ambang.",
   "crop_box tiap gigi, classify sekaligus satu batch.",
   "disease_prob = 1 − p(sehat); gigi dengan disease_prob ≥ ambang masuk temuan.",
   "evaluate_two_stage: bandingkan dengan label asli di tingkat gigi dan foto."],
  ("oralai/stage10_pipeline.py", """
def analyze(self, image):
    im = ImageOps.exif_transpose(Image.open(image)).convert("RGB")
    teeth = detect_teeth(self.det, im, self.conf)
    probs = classify(self.cls, [crop_box(im, t, self.margin) for t in teeth])
    for i, (t, p) in enumerate(zip(teeth, probs), 1):
        j = int(p.argmax())
        out.append({"index": i, "label": classes[j],
                    "disease_prob": round(float(1 - p[0]), 3)})
""", "Dua model disambung: keluaran detektor menjadi masukan classifier."),
  [("Latensi dua tahap", "152 ms/foto"), ("Latensi satu tahap", "78 ms/foto"), ("AUC satu tahap DentalAI", "0,950")],
  [("Two-stage pipeline", "Deteksi objek lalu klasifikasi per objek."),
   ("Latensi", "Waktu dari foto masuk sampai hasil keluar.")],
  ["ml-medis", "citra", "pemrograman", "sistem-tertanam"])

# ---------------------------------------------------------------- 13
B("nama", "Menulis nama di kue: penomoran gigi FDI", "Menyajikan",
  ["oralai/fdi.py", "oralai/orientation.py", "configs/experiment.yaml (fdi_yolo32)"],
  "Deep learning adalah kuat menebak setiap objek, tetapi tidak otomatis tahu aturan dunia nyata. Model bisa menebak dua gigi sama-sama "
  "'11', padahal di mulut hanya ada satu gigi 11. Aturan seperti ini harus ditambahkan di luar jaringan saraf.",
  "Jika kita ingin membentuk odontogram, yaitu peta gigi bernomor FDI (11–18, 21–28, 31–38, 41–48), maka kita harus membuat dua hal: "
  "detektor 32 kelas (fdi_yolo32, gambar 1024 px, tanpa flip) dan algoritma penyelaras (align) dengan pemrograman dinamis. align mengurutkan "
  "gigi sepanjang lengkung dari kanan ke kiri pasien, lalu mencari susunan nomor dengan skor total tertinggi yang naik ketat, sehingga "
  "setiap nomor dipakai sekali dan gigi yang hilang dilewati.",
  "Bayangkan jika Anda ingin membuat program seperti ini untuk foto yang diambil dari depan, samping, atau lewat cermin. Pastinya Anda "
  "membutuhkan konvensi orientasi: foto cermin harus dibalik dulu, dan nomor gigi ikut ditukar kuadrannya (flip_fdi: 1↔2, 3↔4). "
  "orientation.py menyimpan konvensi foto klinis itu.",
  "Bayangkan Anda seperti membuat kue ulang tahun dan menulis nama di atasnya. Huruf-hurufnya sudah dicetak (deteksi gigi), tetapi harus "
  "disusun dengan urutan yang benar. Satu huruf tidak boleh dipakai dua kali, dan urutannya harus dari kiri ke kanan. Pemrograman dinamis "
  "adalah cara menyusun huruf itu dengan paling sedikit kesalahan.",
  ["Latih detektor 32 kelas (tooth_11 … tooth_48) dengan preset dental_fdi.",
   "Kelompokkan gigi ke lengkung atas dan bawah.",
   "Urutkan sepanjang lengkung; align memilih nomor naik ketat dengan skor maksimum.",
   "Untuk foto cermin: flip_fdi menukar kuadran 1↔2 dan 3↔4.",
   "assign: cocokkan nomor ke kotak gigi pipeline dengan IoU ≥ 0,5."],
  ("oralai/fdi.py", """
def flip_fdi(f):
    \"\"\"Nomor gigi setelah foto dibalik kiri-kanan:
    kuadran 1<->2, 3<->4.\"\"\"
    q, p = divmod(f, 10)
    return {1: 2, 2: 1, 3: 4, 4: 3, 5: 6, 6: 5, 7: 8, 8: 7}[q] * 10 + p
""", "Aturan anatomi gigi ditulis sebagai kode, karena jaringan saraf tidak tahu konvensi FDI dengan sendirinya."),
  [("Nomor gigi benar", "95,4%"), ("Kesalahan bergeser satu posisi", "92% dari semua kesalahan"), ("Ukuran input FDI", "1024 px")],
  [("FDI", "Sistem penomoran gigi dua digit: digit pertama kuadran, digit kedua posisi dari tengah."),
   ("Pemrograman dinamis", "Memecah masalah jadi submasalah dan menyimpan hasil terbaik tiap langkah."),
   ("Odontogram", "Diagram gigi pasien beserta temuan per gigi.")],
  ["anatomi", "pemrograman", "ml-medis", "citra"])

# ---------------------------------------------------------------- 14
B("belah", "Membelah kue: heatmap Grad-CAM", "Menyajikan",
  ["oralai/cam.py", "scripts/validasi_heatmap.py"],
  "Deep learning adalah model yang sering disebut kotak hitam: model memberi jawaban tanpa alasan. Di dunia medis, jawaban tanpa alasan sulit dipercaya. "
  "Grad-CAM membuka kotak itu dengan peta panas yang menunjukkan bagian gambar mana yang paling mendorong keputusan model.",
  "Jika kita ingin membentuk penjelasan visual untuk setiap gigi, maka kita harus membuat peta aktivasi dari lapisan konvolusi terakhir "
  "(layer4 ResNet, 7×7), dibobot oleh bobot kepala Linear untuk selisih logit karies − sehat. Karena kepala ResNet adalah GAP lalu satu Linear, "
  "Grad-CAM di sini sama persis dengan CAM, sehingga peta bisa dihitung di dalam file ONNX tanpa gradien.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan dokter gigi bertanya 'kenapa gigi ini dianggap karies?'. Pastinya Anda "
  "membutuhkan heatmap yang benar-benar menunjuk lesi, bukan sekadar bagian tengah gambar. Oralytic mengujinya dengan pointing game: "
  "titik terpanas jatuh di lesi 66,9% kasus, jauh di atas tebakan tengah crop (32,7%).",
  "Bayangkan Anda seperti membuat kue lalu membelahnya di depan pembeli untuk menunjukkan lapisan cokelatnya. Pembeli lebih percaya "
  "setelah melihat isinya. Heatmap adalah belahan kue itu: menunjukkan bagian foto yang membuat model berkata 'karies'.",
  ["Ambil aktivasi layer4 (N × 2048 × 7 × 7).",
   "Bobot w = fc.weight[karies] − fc.weight[sehat].",
   "Peta = jumlah aktivasi × w per kanal (einsum), lalu ReLU.",
   "Perbesar ke ukuran crop (bilinear) dan normalisasi 0–1.",
   "Cek paritas ONNX vs Grad-CAM PyTorch, lalu uji stabilitas peta terhadap gangguan kecil."],
  ("oralai/cam.py", """
class _Cam(nn.Module):
    def __init__(self):
        super().__init__()
        self.m = model
        self.register_buffer("w", (fc.weight[target] - fc.weight[ref]))

    def forward(self, x):
        a = _features(self.m, x)
        logit = self.m.fc(torch.flatten(self.m.avgpool(a), 1))
        return logit, torch.einsum("nkhw,k->nhw", a, self.w)
""", "Satu model mengeluarkan dua hal sekaligus: logit (jawaban) dan cam (alasan visual)."),
  [("Pointing game heatmap", "0,669"), ("Pembanding tengah crop", "0,327"), ("Ukuran peta mentah", "7 × 7")],
  [("Grad-CAM", "Peta panas dari gradien skor kelas terhadap aktivasi lapisan konvolusi."),
   ("Explainable AI (XAI)", "Metode yang membuat keputusan model bisa dipahami manusia."),
   ("Pointing game", "Uji apakah titik terpanas heatmap jatuh di dalam area lesi yang benar.")],
  ["ml-medis", "citra", "visualisasi", "interaksi-pasien"])

# ---------------------------------------------------------------- 15
B("juri", "Juri pencicip: tinjauan dokter gigi", "Menguji",
  ["oralai/stage11_review.py", "docs/Pertanyaan_untuk_Dokter_Gigi.md", "scripts/fp_review.py"],
  "Deep learning adalah murid yang belajar dari label manusia, jadi kualitasnya dibatasi kualitas label. Kalau label dataset keliru atau "
  "definisi karies berbeda antar-sumber, model akan ikut keliru. Pemeriksa akhir tetaplah ahli manusia.",
  "Jika kita ingin membentuk bukti bahwa model berguna secara klinis, maka kita harus membuat formulir tinjauan buta: stage11 export "
  "mengambil contoh benar dan salah, mengacak urutannya, menyembunyikan jawaban model, lalu dokter gigi menilai. stage11 score menghitung "
  "Cohen kappa (kesepakatan di luar kebetulan) dan menganalisis jenis kesalahan.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan menemukan banyak positif palsu. Pastinya Anda membutuhkan dokter yang melihat "
  "langsung: apakah itu benar-benar salah model, atau label dataset yang kurang lengkap? File kunci jawaban tinjauan disimpan terpisah dan "
  "tidak boleh dikirim ke penilai, supaya tinjauan tetap buta.",
  "Bayangkan Anda seperti membuat kue untuk lomba: juri mencicip tanpa tahu kue mana buatan siapa. Kalau juri tahu, penilaiannya bisa "
  "condong. Kunci nama pembuat kue disimpan di amplop tertutup sampai penilaian selesai.",
  ["export: pilih contoh positif palsu, negatif palsu, dan sejumlah contoh benar (default 20), acak dengan seed.",
   "Tulis formulir tanpa jawaban model; kunci disimpan terpisah (KUNCI_jangan_dikirim.csv).",
   "Dokter gigi mengisi penilaian.",
   "score: hitung Cohen kappa dan tabel kesalahan.",
   "Hasil dipakai untuk memperbaiki definisi label dan memilih ambang."],
  None,
  [("Ukuran kesepakatan", "Cohen kappa"), ("Contoh benar ikut ditinjau", "20 (bawaan)")],
  [("Tinjauan buta", "Penilai tidak tahu jawaban model atau kunci, untuk menghindari bias."),
   ("Cohen kappa", "Kesepakatan dua penilai dikoreksi kesepakatan karena kebetulan; 1 = sepakat sempurna.")],
  ["metopen", "statistika", "interaksi-pasien", "tek-medik"],
  "Aturan Oralytic: file runs/tinjauan_fp/KUNCI_jangan_dikirim.csv tidak boleh dikirim ke mana pun.")

# ---------------------------------------------------------------- 16
B("kemas", "Mengemas kue: ekspor ONNX ke aplikasi Health Hub", "Menyajikan",
  ["oralai/onnx_infer.py", "scripts/ekspor_onnx.py", "scripts/snapshot_model.py"],
  "Deep learning adalah dua dunia: dunia training yang berat (PyTorch, GPU, gigabyte pustaka) dan dunia pemakaian (inference) yang harus "
  "ringan dan cepat. Model yang sudah jadi diekspor ke format netral ONNX agar bisa dijalankan onnxruntime tanpa PyTorch.",
  "Jika kita ingin membentuk fitur deteksi karies di aplikasi Health Hub, maka kita harus membuat paket model: detektor dan classifier "
  "dalam ONNX, file konfigurasi berisi kelas, ukuran input, dan ambang (0,971), lalu kelas OralyticONNX yang menyediakan analyze "
  "(temuan per gigi), explain (heatmap plus uji stabilitas terhadap gangguan kecil), dan fdi (nomor gigi).",
  "Bayangkan jika Anda ingin membuat program seperti ini berjalan di laptop pengguna biasa. Pastinya Anda membutuhkan letterbox (mengubah "
  "ukuran foto tanpa merusak rasio), batch inference, dan snapshot model dengan nama versi (oralytic_twostage_v4) supaya aplikasi tahu "
  "model mana yang sedang dipakai dan bisa kembali ke versi lama bila perlu.",
  "Bayangkan Anda seperti membuat kue yang akan dijual. Dapur dan oven tidak ikut dikirim ke pembeli; yang dikirim hanya kue di dalam dus "
  "dengan label tanggal dan cara penyimpanan. ONNX adalah dus itu, dan file konfigurasi adalah labelnya.",
  ["scripts/ekspor_onnx.py: ekspor detektor (Ultralytics) dan classifier+CAM (torch.onnx, opset 17).",
   "Uji paritas: keluaran ONNX harus sama dengan PyTorch (cam.paritas).",
   "snapshot_model.py: salin model + konfigurasi ke folder versi.",
   "OralyticONNX.analyze(foto, thr): letterbox → deteksi → crop → klasifikasi.",
   "Pasang di Health Hub (Project Patriot / Prototype_MVP)."],
  ("oralai/onnx_infer.py", """
class OralyticONNX:
    def analyze(self, image, thr=0.5): ...   # temuan per gigi
    def explain(self, image, thr=0.5):  ...   # heatmap + stabilitas
    def fdi(self, im, view, src_mirrored, convention): ...  # nomor gigi
""", "Antarmuka yang dipakai aplikasi. Aplikasi tidak perlu tahu PyTorch sama sekali."),
  [("Model terpasang", "oralytic_twostage_v4"), ("Ambang aplikasi", "0,971"), ("Opset ONNX", "17")],
  [("Inference", "Memakai model yang sudah dilatih untuk menebak data baru."),
   ("ONNX", "Open Neural Network Exchange: format file model yang bisa dibaca banyak runtime."),
   ("Letterbox", "Mengubah ukuran gambar dengan menambah pinggiran agar rasio aspek tetap.")],
  ["mobile", "pemrograman", "sistem-tertanam", "ml-medis"])

# ---------------------------------------------------------------- 17
B("uji-rasa", "Uji rasa sebelum dijual: pytest", "Menguji",
  ["tests/test_pipeline.py", "tests/test_two_stage.py", "tests/test_cam.py", "tests/test_fdi.py", "tests/test_orientation.py", "tests/test_stats.py"],
  "Deep learning adalah perangkat lunak juga. Bug kecil, misalnya kotak yang terbalik koordinatnya atau nomor gigi yang salah ditukar, "
  "bisa merusak hasil tanpa terlihat. Unit test memastikan setiap potongan kode berperilaku benar sebelum model dilatih berjam-jam.",
  "Jika kita ingin membentuk proyek yang aman diubah, maka kita harus membuat tes otomatis untuk bagian yang paling rawan: statistik "
  "(test_stats: Wilson, AUC), penomoran (test_fdi: flip dan align), orientasi foto, CAM (paritas dengan Grad-CAM), dan pipeline. "
  "VS Code sudah diatur agar pytest bisa dijalankan dari panel Testing.",
  "Bayangkan jika Anda ingin membuat program seperti ini lalu enam bulan kemudian mengubah fungsi crop. Pastinya Anda membutuhkan cara "
  "cepat untuk tahu apakah perubahan itu merusak bagian lain. Satu perintah pytest menjawabnya dalam hitungan detik.",
  "Bayangkan Anda seperti membuat kue dan punya daftar periksa sebelum dijual: gula sudah larut, tengah kue matang, label tanggal benar. "
  "Daftar periksa itu tidak membuat kue lebih enak, tetapi mencegah kue gagal sampai ke tangan pembeli.",
  ["Tulis fungsi kecil yang bisa diuji tanpa GPU dan tanpa dataset besar.",
   "Uji kasus tepi: n = 0 pada Wilson, satu kelas kosong pada AUC, gigi lebih banyak dari nomor pada align.",
   "Jalankan pytest dari terminal atau panel Testing VS Code.",
   "Jalankan ulang tes setiap kali mengubah kode inti."],
  ("tests/ (contoh pola)", """
def test_flip_fdi():
    assert flip_fdi(11) == 21
    assert flip_fdi(36) == 46
    assert flip_fdi(flip_fdi(24)) == 24
""", "Contoh pola tes untuk fungsi flip_fdi: membalik dua kali harus kembali ke nomor semula."),
  [("File tes", "6"), ("Penjalankan", "pytest")],
  [("Unit test", "Kode kecil yang memeriksa satu fungsi memberi hasil yang diharapkan."),
   ("Regresi", "Bug baru yang muncul pada fitur yang dulu sudah benar.")],
  ["pemrograman", "sistem-tertanam"],
  "Contoh tes ditulis ulang untuk penjelasan; isi file tes asli di folder tests/ Oralytic.")

# ---------------------------------------------------------------- 18
B("pelajaran", "Pelajaran dari dapur: yang paling menentukan hasil", "Penutup",
  ["docs/STATUS_RISET.md", "docs/bab_hasil_pembahasan.md", "scripts/analisis_*.py"],
  "Deep learning adalah ilmu eksperimen. Banyak pelajaran terpenting Oralytic tidak datang dari memilih model yang lebih besar, tetapi dari "
  "memeriksa data, cara membagi data, dan cara menguji.",
  "Jika kita ingin membentuk model yang tetap bekerja di luar laboratorium, maka kita harus membuat uji lintas domain. Oralytic dilatih "
  "pada satu sumber lalu diuji di sumber lain: AUC turun ke 0,787 lintas domain dan sekitar 0,65 di AlphaDent. Setelah melatih dengan "
  "campuran data (id_mix), AUC AlphaDent naik ke 0,739 dengan AKU tetap 0,914.",
  "Bayangkan jika Anda ingin membuat program seperti ini dan skornya sangat tinggi di awal. Pastinya Anda membutuhkan kecurigaan sehat: "
  "apakah ada kebocoran pasien? apakah model belajar jalan pintas, misalnya sudut pengambilan foto, bukan karies? apakah definisi karies "
  "di dataset sama dengan definisi dokter? Tiga pertanyaan ini mengubah hasil Oralytic lebih besar daripada mengganti arsitektur.",
  "Bayangkan Anda seperti membuat kue yang menang lomba di kampung sendiri, lalu dibawa ke kota lain dan rasanya dianggap biasa saja. "
  "Ternyata tepung di kota itu berbeda. Kue yang hebat adalah kue yang tetap enak dengan tepung dari mana pun, dan itu didapat dengan "
  "berlatih memakai tepung dari banyak tempat.",
  ["Split per pasien wajib untuk data medis; kebocoran membuat skor terlalu optimis.",
   "Waspadai shortcut: model bisa belajar sudut foto atau warna latar, bukan penyakit.",
   "Definisi label lebih menentukan daripada arsitektur.",
   "Uji eksternal (data dari sumber lain) adalah ujian yang sesungguhnya.",
   "Laporkan interval kepercayaan, bukan satu angka saja."],
  None,
  [("Lintas domain", "AUC 0,787"), ("AlphaDent awal", "≈ 0,65"), ("AlphaDent setelah id_mix", "0,739"), ("AKU setelah id_mix", "0,914")],
  [("Domain shift", "Perbedaan sifat data latih dan data pemakaian (kamera, populasi, cara memotret)."),
   ("Shortcut learning", "Model memakai petunjuk palsu yang kebetulan berkorelasi dengan label.")],
  ["metopen", "ml-medis", "ilmu-data", "big-data"])

# ---------------------------------------------------------------- 19
B("bonus", "Bonus: kue tanpa oven, machine learning klasik", "Penutup",
  ["loan2.py", "loan.py"],
  "Deep learning adalah salah satu cabang machine learning, bukan satu-satunya. Untuk data tabel kecil, metode klasik seperti KMeans, "
  "regresi, atau pohon keputusan sering cukup, lebih cepat, dan lebih mudah dijelaskan.",
  "Jika kita ingin membentuk kelompok-kelompok data tanpa label, maka kita harus membuat clustering. loan2.py mengambil dua kolom "
  "(installment dan fico) dari loan_data.csv, menstandarkan skalanya dengan StandardScaler, lalu mencoba KMeans k = 1 sampai 5 dan "
  "menggambar kurva elbow untuk memilih k.",
  "Bayangkan jika Anda ingin membuat program seperti ini untuk mengelompokkan pasien berdasarkan dua angka lab. Pastinya Anda tidak "
  "membutuhkan GPU atau jaringan berlapis; Anda butuh standardisasi (agar satuan yang besar tidak mendominasi) dan cara memilih jumlah kelompok.",
  "Bayangkan Anda seperti membuat kue: tidak semua kue perlu oven. Puding dan es buah cukup dicampur dan didinginkan. Deep learning adalah "
  "oven besar untuk bahan rumit seperti foto; machine learning klasik adalah resep tanpa oven untuk bahan sederhana seperti tabel angka.",
  ["Pilih fitur: installment dan fico.",
   "StandardScaler: ubah tiap kolom menjadi rata-rata 0, simpangan baku 1.",
   "KMeans(n_clusters=k, n_init=10, random_state=42) untuk k = 1…5.",
   "Plot inertia terhadap k; pilih k di 'siku' kurva."],
  ("loan2.py", """
X = df[['installment', 'fico']]
X_scaled = StandardScaler().fit_transform(X)
inertia = []
for k in range(1, 6):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(X_scaled)
    inertia.append(km.inertia_)
""", "Machine learning klasik tanpa jaringan saraf: tiga baris inti, jalan dalam hitungan detik di CPU."),
  [("Rentang k", "1–5"), ("Fitur", "2 (installment, fico)")],
  [("Clustering", "Mengelompokkan data tanpa label berdasarkan kemiripan."),
   ("Inertia", "Jumlah kuadrat jarak titik ke pusat kelompoknya; makin kecil makin rapat."),
   ("Metode elbow", "Memilih k pada titik di mana penurunan inertia mulai melandai.")],
  ["data-mining", "statistika", "ilmu-data"])


KISAH = {
    "id": "oralytic",
    "judul": "Kisah Deep Learning: membuat Oralytic seperti membuat kue",
    "singkat": "Kisah Deep Learning",
    "sumber": SUMBER,
    "ikon": "🦷",
    "alat": "oralytic",
    "ringkasan": "Seluruh environment dan kode proyek Oralytic (deteksi karies dua tahap dari foto intraoral) diartikan menjadi cerita "
                 "langkah demi langkah membentuk deep learning, dengan perumpamaan membuat kue. Setiap bab menyebut file kode aslinya, "
                 "potongan kode, angka hasil riset, dan istilah penting.",
    "pola": ["Deep learning adalah …", "Jika kita ingin membentuk ini, maka harus membuat …",
             "Bayangkan jika Anda ingin membuat program seperti ini, pastinya Anda membutuhkan …",
             "Bayangkan Anda seperti membuat kue …"],
    "resep": [{"kue": a, "dl": b, "file": c} for a, b, c in RESEP],
    "bab": BAB,
}


# ---------------------------------------------------------------- soal
SOAL = []


def Q(bab, materi, tipe, tanya, bahas, **kw):
    q = {"id": "k-oralytic-%02d" % (len(SOAL) + 1), "tipe": tipe, "tanya": tanya, "bahas": bahas,
         "materi": materi, "alat": "oralytic", "kisah": "oralytic", "bab": bab}
    q.update(kw)
    SOAL.append(q)


Q("pembuka", "ml-medis", "pg", "Mengapa disebut deep learning?",
  "Disebut deep karena jaringan saraf punya banyak lapisan bertumpuk: lapisan awal mengenali garis, lapisan akhir mengenali pola rumit seperti lesi karies.",
  opsi=["Karena jaringan sarafnya punya banyak lapisan bertumpuk", "Karena datanya disimpan di server yang dalam", "Karena hanya bisa dipakai untuk citra kedokteran", "Karena modelnya ditulis dengan bahasa pemrograman tingkat rendah"], jawab=0)
Q("pembuka", "ml-medis", "urut", "Urutkan tahap pipeline Oralytic dari awal sampai model dipakai.",
  "Urutan resepnya: data → split per pasien → latih detektor → latih classifier → evaluasi → ekspor ONNX.",
  item=["Akuisisi data (stage01)", "Split per pasien (stage04)", "Latih detektor gigi (stage06)", "Latih classifier karies (stage07)", "Evaluasi (stage09)", "Ekspor ONNX ke aplikasi"])
Q("dapur", "pemrograman", "pg", "Apa fungsi set_seed(seed) di stage00_config.py?",
  "set_seed mengunci pembangkit angka acak Python, NumPy, dan PyTorch (CPU dan GPU) sehingga training bisa diulang dengan hasil sama.",
  opsi=["Mengunci semua pembangkit angka acak agar hasil bisa diulang", "Mempercepat GPU", "Memilih model terbaik", "Mengunduh dataset dari Zenodo"], jawab=0)
Q("dapur", "pemrograman", "bs", "Torch versi CUDA sebaiknya dipasang sebelum pip install -r requirements.txt, karena ultralytics akan memasang torch sendiri bila belum ada.",
  "Benar. Komentar di requirements.txt Oralytic meminta torch CUDA dipasang dulu; kalau tidak, ultralytics memasang torch versi CPU.", jawab=True)
Q("resep", "ml-medis", "cocok", "Cocokkan hyperparameter dengan artinya.",
  "Epoch = putaran penuh data; batch = jumlah foto per pembaruan bobot; learning rate = besar langkah; patience = batas epoch tanpa perbaikan.",
  pasangan=[["Epoch", "Satu putaran penuh melihat semua data training"], ["Batch", "Jumlah foto yang diproses sebelum bobot diperbarui"],
            ["Learning rate", "Besar langkah perubahan bobot"], ["Patience", "Batas epoch tanpa perbaikan sebelum berhenti"]])
Q("resep", "metopen", "pg", "Mengapa ss_baseline dan ss_augmented memakai resep yang sama kecuali augmentasi?",
  "Perbandingan hanya adil bila satu variabel yang diubah. Itu prinsip eksperimen terkontrol.",
  opsi=["Agar perbedaan hasil hanya disebabkan augmentasi", "Agar training lebih cepat", "Karena YOLO tidak bisa diubah", "Agar jumlah data bertambah"], jawab=0)
Q("bahan", "ilmu-data", "pg", "Apa tujuan stage01 mengubah semua dataset ke satu format JSONL kanonik?",
  "Dataset datang dalam format COCO, VOC, LabelMe, Supervisely, YOLO, dan folder. Format kanonik membuat tahap berikutnya cukup membaca satu format.",
  opsi=["Agar tahap berikutnya cukup membaca satu format seragam", "Agar ukuran foto mengecil", "Agar model langsung terlatih", "Agar foto tidak bisa dibuka orang lain"], jawab=0)
Q("bahan", "ilmu-data", "isian", "Sidik jari gambar 64-bit yang dipakai Oralytic untuk menemukan foto kembar disebut …",
  "dhash (difference hash) membandingkan kecerahan piksel bertetangga; foto yang mirip punya dhash yang hanya beda sedikit bit.",
  jawab=["dhash", "d-hash", "difference hash"])
Q("ayak", "citra", "pg", "Mengapa preset dental_fdi mematikan flip kiri-kanan?",
  "Membalik foto memindahkan gigi 11 ke posisi 21, tetapi labelnya tetap 11, sehingga model diajari jawaban salah.",
  opsi=["Flip menukar sisi gigi tanpa menukar nomornya, sehingga label menjadi salah", "Flip membuat foto terlalu gelap", "Flip memperlambat GPU", "Flip tidak didukung YOLO"], jawab=0)
Q("ayak", "citra", "multi", "Pilih semua augmentasi yang ada di preset dental Oralytic.",
  "Preset dental: perubahan HSV, rotasi 10°, geser 10%, skala 30%, flip kiri-kanan 50%, dan mosaic. flipud dan mixup bernilai 0.",
  opsi=["Rotasi sampai 10°", "Flip kiri-kanan 50%", "Mosaic", "Perubahan kecerahan (hsv_v)", "Flip atas-bawah", "Mixup"], benar=[0, 1, 2, 3])
Q("ayak", "statistika", "pg", "Augmentasi menaikkan AUC YOLO satu tahap sebesar 0,020 dengan McNemar p = 0,034. Artinya…",
  "p < 0,05 berarti perbedaan kesalahan kedua model kecil kemungkinannya terjadi karena kebetulan saja.",
  opsi=["Perbedaannya signifikan secara statistik pada α = 0,05", "Augmentasi membuat model lebih buruk", "Perbedaannya pasti karena kebetulan", "AUC model menjadi 0,034"], jawab=0)
Q("takar", "statistika", "hitung", "Ada 1.000 crop: 800 sehat dan 200 karies (K = 2 kelas). Berapa bobot kelas karies menurut w_c = N / (K · n_c)?",
  "w_karies = 1000 / (2 × 200) = 2,5. Bobot sehat = 1000 / (2 × 800) = 0,625. Kesalahan pada karies dihitung 4 kali lebih berat.",
  angka=2.5, tol=0.01, satuan="")
Q("takar", "ml-medis", "bs", "Pada data 90% sehat, model yang selalu menjawab 'sehat' mendapat akurasi 90% tetapi sensitivitasnya 0.",
  "Benar. Itulah sebabnya akurasi menyesatkan pada data tidak seimbang, dan Oralytic memakai bobot kelas serta melaporkan sensitivitas.", jawab=True)
Q("sisih", "metopen", "kasus", "Seorang mahasiswa membagi foto gigi secara acak per foto. AUC test 0,99, tetapi turun drastis di pasien baru. Penyebab paling mungkin?",
  "Satu pasien punya beberapa foto; pembagian per foto membuat foto pasien yang sama ada di train dan test (kebocoran). Oralytic menemukan 87% foto test berbagi pasien dengan train.",
  opsi=["Kebocoran data: foto pasien yang sama ada di train dan test", "Learning rate terlalu kecil", "GPU kurang memori", "Augmentasi terlalu sedikit"], jawab=0)
Q("sisih", "pemrograman", "pg", "Apa keunggulan hash_split (MD5 dari ID pasien) dibanding pengacakan biasa?",
  "Hash selalu sama untuk ID yang sama, jadi menambah data baru tidak mengubah pembagian data lama.",
  opsi=["Pembagian deterministik: data lama tidak teracak ulang saat data baru ditambah", "Lebih cepat dilatih", "Membuat foto lebih tajam", "Menghapus foto yang buram"], jawab=0)
Q("sisih", "ml-medis", "kategori", "Kelompokkan kegunaan tiap bagian data.",
  "Train untuk mengubah bobot, validation untuk memilih model dan early stopping, test untuk ujian akhir sekali saja.",
  kelompok=["Train", "Validation", "Test"],
  item=[["Menghitung gradien dan mengubah bobot", 0], ["Augmentasi diterapkan", 0], ["Memilih best.pt dengan macro-F1", 1], ["Menentukan kapan early stopping", 1], ["Melaporkan AUC akhir di skripsi", 2], ["Tidak boleh dilihat selama tuning", 2]])
Q("cetakan", "ml-medis", "pg", "Apa yang dilakukan _replace_head pada ResNet50 pralatih?",
  "Lapisan Linear terakhir (1.000 kelas ImageNet) diganti dengan Linear baru sebanyak kelas kita; badan konvolusi dipertahankan. Itu inti transfer learning.",
  opsi=["Mengganti lapisan Linear terakhir agar keluarannya sebanyak kelas kita", "Menghapus semua lapisan konvolusi", "Menambah 50 lapisan baru", "Mengubah gambar menjadi hitam putih"], jawab=0)
Q("cetakan", "matek", "celah", "Lengkapi kalimat berikut.",
  "Konvolusi menggeser filter kecil di seluruh gambar; transfer learning memakai bobot pralatih ImageNet.",
  teks="CNN memakai operasi [[0]] yang menggeser filter kecil di seluruh gambar. Model yang sudah dilatih pada [[1]] lalu dipakai untuk tugas baru disebut [[2]] learning.",
  isi=["konvolusi", "ImageNet", "transfer"], pengecoh=["integral", "Excel", "reinforcement"])
Q("lapis1", "citra", "cocok", "Cocokkan bagian YOLO dengan tugasnya.",
  "Backbone mengekstrak fitur, neck menggabung fitur berbagai skala, head memprediksi kotak dan kelas, NMS membuang kotak ganda.",
  pasangan=[["Backbone", "Mengekstrak fitur dari gambar"], ["Neck", "Menggabungkan fitur berbagai ukuran"], ["Head", "Memprediksi kotak, kelas, dan keyakinan"], ["NMS", "Membuang kotak yang tumpang tindih"]])
Q("lapis1", "citra", "hitung", "Kotak prediksi dan kotak asli beririsan 60 px² dan gabungannya 100 px². Berapa IoU-nya?",
  "IoU = irisan / gabungan = 60 / 100 = 0,6. Karena ≥ 0,5, deteksi ini dihitung benar pada mAP@0,5.", angka=0.6, tol=0.01, satuan="")
Q("lapis1", "ml-medis", "pg", "Mengapa detektor gigi harus sangat baik sebelum classifier dilatih?",
  "Pada pipeline dua tahap, gigi yang terlewat detektor tidak pernah diperiksa classifier. Detektor Oralytic mencapai mAP@0,5 0,952.",
  opsi=["Gigi yang terlewat detektor tidak akan pernah diperiksa classifier", "Classifier memakai bobot detektor", "Detektor menentukan learning rate classifier", "Classifier hanya bisa dilatih di CPU"], jawab=0)
Q("lapis2", "kalkulus", "urut", "Urutkan satu langkah training di _run_epoch.",
  "Forward (menebak) → hitung loss → zero_grad → backward (gradien lewat chain rule) → step (W − lr·gradien).",
  item=["logits = model(x)", "loss = loss_fn(logits, y)", "opt.zero_grad()", "loss.backward()", "opt.step()"])
Q("lapis2", "kalkulus", "pg", "loss.backward() menghitung gradien untuk setiap bobot memakai…",
  "Backpropagation menerapkan aturan rantai turunan dari lapisan akhir mundur ke lapisan awal.",
  opsi=["Aturan rantai (chain rule) turunan", "Integral tak tentu", "Transformasi Fourier", "Regresi linear"], jawab=0)
Q("lapis2", "kalkulus", "hitung", "Sebuah bobot bernilai 0,50, gradiennya 2,0, dan learning rate 0,01. Berapa bobot setelah satu langkah gradient descent sederhana?",
  "W_baru = W_lama − lr × gradien = 0,50 − 0,01 × 2,0 = 0,48.", angka=0.48, tol=0.001, satuan="")
Q("lapis2", "ml-medis", "pg", "Kapan train_classifier berhenti lebih awal (early stopping)?",
  "Model disimpan saat macro-F1 validasi membaik dan training berhenti bila cls_patience (5) epoch berturut-turut tidak membaik.",
  opsi=["Saat macro-F1 validasi tidak membaik selama 5 epoch berturut-turut", "Saat loss training mencapai 0", "Setelah tepat 1 epoch", "Saat GPU panas"], jawab=0)
Q("tiga-kali", "statistika", "bs", "Hasil satu kali training sudah cukup untuk menyimpulkan bahwa satu metode lebih baik dari metode lain.",
  "Salah. Training mengandung keacakan; Oralytic memakai tiga seed dan melaporkan rata-rata ± SD serta uji statistik.", jawab=False)
Q("cicip", "statistika", "hitung", "Dari 100 gigi karies, model mendeteksi 90. Dari 200 gigi sehat, 170 dinyatakan sehat. Berapa sensitivitasnya (desimal)?",
  "Se = TP / (TP + FN) = 90 / 100 = 0,9. Spesifisitasnya 170/200 = 0,85.", angka=0.9, tol=0.001, satuan="")
Q("cicip", "statistika", "cocok", "Cocokkan ukuran evaluasi dengan artinya.",
  "Se dan Sp menilai deteksi; PPV menilai seberapa bisa dipercaya hasil positif; AUC merangkum semua ambang.",
  pasangan=[["Sensitivitas", "Proporsi gigi karies yang terdeteksi"], ["Spesifisitas", "Proporsi gigi sehat yang dinyatakan sehat"],
            ["PPV", "Proporsi hasil positif yang benar-benar karies"], ["AUC", "Kemampuan memisahkan kelas di semua ambang"]])
Q("cicip", "statistika", "pg", "Model di Health Hub memakai ambang 0,971, jauh di atas 0,5. Konsekuensinya?",
  "Ambang tinggi mengurangi alarm palsu (spesifisitas naik) tetapi sebagian karies ringan bisa terlewat (sensitivitas turun).",
  opsi=["Positif palsu berkurang, tetapi sebagian karies bisa terlewat", "Sensitivitas pasti naik", "AUC berubah menjadi 0,971", "Model menjadi lebih lambat"], jawab=0)
Q("susun", "ml-medis", "pg", "Apa kelebihan pipeline dua tahap dibanding YOLO satu tahap pada Oralytic?",
  "Dua tahap memberi temuan per gigi yang bisa dijelaskan dan dinomori, tetapi lebih lambat (152 ms vs 78 ms).",
  opsi=["Temuan per gigi lebih mudah dijelaskan dan dinomori", "Selalu lebih cepat", "Tidak perlu data berlabel", "Tidak memerlukan GPU saat training"], jawab=0)
Q("susun", "pemrograman", "isian", "Fungsi PIL yang dipakai analyze agar foto HP tidak terbaca miring adalah ImageOps.…",
  "ImageOps.exif_transpose memutar foto sesuai tag orientasi EXIF dari kamera.", jawab=["exif_transpose", "exif transpose"])
Q("nama", "anatomi", "pg", "Pada sistem FDI, gigi 36 adalah…",
  "Digit pertama 3 = kuadran kiri bawah, digit kedua 6 = gigi keenam dari tengah, yaitu molar pertama.",
  opsi=["Molar pertama kiri bawah", "Kaninus kanan atas", "Insisivus sentral kiri atas", "Premolar kedua kanan bawah"], jawab=0)
Q("nama", "anatomi", "hitung", "Foto cermin dibalik kiri-kanan. Gigi yang terbaca 14 sebenarnya bernomor berapa (flip_fdi)?",
  "Kuadran 1 ditukar dengan 2, posisi tetap: 14 → 24.", angka=24, tol=0, satuan="")
Q("nama", "pemrograman", "pg", "Apa tugas fungsi align di fdi.py?",
  "align memakai pemrograman dinamis untuk memilih susunan nomor yang naik ketat sepanjang lengkung dengan skor total maksimum.",
  opsi=["Memilih susunan nomor gigi sepanjang lengkung dengan skor total maksimum", "Meluruskan foto yang miring", "Menghitung AUC", "Mengubah ukuran foto"], jawab=0)
Q("belah", "ml-medis", "pg", "Mengapa heatmap Oralytic bisa dihitung di dalam file ONNX tanpa gradien?",
  "Kepala ResNet adalah GAP lalu satu Linear, sehingga bobot Grad-CAM konstan dan sama dengan bobot Linear (CAM).",
  opsi=["Karena kepala ResNet GAP→Linear membuat Grad-CAM sama dengan CAM", "Karena ONNX otomatis menghitung gradien", "Karena heatmap diambil dari detektor YOLO", "Karena gambar diubah menjadi hitam putih"], jawab=0)
Q("belah", "visualisasi", "bs", "Pointing game heatmap Oralytic 0,669 lebih baik daripada menebak tengah crop (0,327), sehingga heatmap memang menunjuk lesi lebih sering dari kebetulan.",
  "Benar. Titik terpanas jatuh di lesi pada 66,9% kasus, dua kali lipat pembanding naif.", jawab=True)
Q("juri", "statistika", "pg", "Cohen kappa dipakai di stage11 untuk mengukur…",
  "Kappa mengukur kesepakatan dua penilai setelah dikoreksi kesepakatan yang terjadi karena kebetulan.",
  opsi=["Kesepakatan penilai yang dikoreksi faktor kebetulan", "Kecepatan model", "Jumlah gigi per foto", "Ukuran file ONNX"], jawab=0)
Q("juri", "metopen", "bs", "Formulir tinjauan dokter gigi sebaiknya menampilkan jawaban model agar dokter bisa menilai lebih cepat.",
  "Salah. Tinjauan harus buta; kunci disimpan terpisah agar penilaian dokter tidak bias.", jawab=False)
Q("kemas", "mobile", "pg", "Mengapa model Oralytic diekspor ke ONNX untuk aplikasi Health Hub?",
  "ONNX bisa dijalankan onnxruntime tanpa PyTorch dan GPU, sehingga aplikasi jauh lebih ringan.",
  opsi=["Agar bisa dijalankan tanpa PyTorch dan GPU", "Agar akurasi naik otomatis", "Agar bisa dilatih ulang di HP", "Agar data pasien terenkripsi"], jawab=0)
Q("kemas", "pemrograman", "cocok", "Cocokkan metode OralyticONNX dengan hasilnya.",
  "analyze untuk temuan per gigi, explain untuk heatmap dan stabilitas, fdi untuk nomor gigi.",
  pasangan=[["analyze", "Temuan karies per gigi"], ["explain", "Heatmap dan uji stabilitas"], ["fdi", "Nomor gigi FDI"], ["letterbox", "Mengubah ukuran tanpa merusak rasio"]])
Q("uji-rasa", "pemrograman", "pg", "Apa manfaat utama unit test (pytest) di proyek deep learning?",
  "Tes cepat menangkap bug pada fungsi kecil (statistik, penomoran, crop) sebelum training berjam-jam atau sebelum model dipasang.",
  opsi=["Menangkap bug di fungsi kecil sebelum training lama atau pemasangan", "Menaikkan AUC", "Mengganti data validasi", "Mempercepat GPU"], jawab=0)
Q("pelajaran", "metopen", "multi", "Pilih semua pelajaran utama dari riset Oralytic.",
  "Split per pasien, waspada shortcut, definisi label, dan uji eksternal lebih menentukan daripada arsitektur yang lebih besar.",
  opsi=["Split per pasien mencegah skor terlalu optimis", "Model bisa belajar jalan pintas seperti sudut foto", "Definisi label lebih menentukan daripada arsitektur", "Uji eksternal adalah ujian sesungguhnya", "Model terbesar selalu terbaik", "Akurasi cukup sebagai satu-satunya ukuran"], benar=[0, 1, 2, 3])
Q("pelajaran", "ml-medis", "kasus", "Model dilatih di dataset AKU (AUC 0,914) lalu diuji di AlphaDent dan AUC turun ke sekitar 0,65. Langkah yang dilakukan Oralytic?",
  "Melatih dengan campuran data dari beberapa sumber (id_mix) menaikkan AUC AlphaDent ke 0,739 tanpa merusak AKU.",
  opsi=["Melatih dengan campuran data dari beberapa sumber (id_mix)", "Menurunkan ambang ke 0", "Menghapus data AlphaDent", "Mengganti GPU"], jawab=0)
Q("bonus", "data-mining", "pg", "Mengapa loan2.py memakai StandardScaler sebelum KMeans?",
  "KMeans memakai jarak. Tanpa standardisasi, kolom bernilai besar (fico ratusan) mendominasi kolom lain.",
  opsi=["Agar fitur dengan satuan besar tidak mendominasi perhitungan jarak", "Agar KMeans memakai GPU", "Agar data berlabel", "Agar jumlah cluster bertambah"], jawab=0)
Q("bonus", "data-mining", "kategori", "Kelompokkan metode berikut.",
  "Deep learning memakai jaringan saraf berlapis; metode klasik tidak.",
  kelompok=["Deep learning", "Machine learning klasik"],
  item=[["ResNet50", 0], ["YOLO", 0], ["EfficientNet-B0", 0], ["KMeans", 1], ["Regresi logistik", 1], ["Pohon keputusan", 1]])


# ---------------------------------------------------------------- alat Oralytic
ALAT = {
    "id": "oralytic", "nama": "Oralytic: Deteksi Karies AI dari Foto Gigi", "singkatan": "Oralytic",
    "kategori": "Perangkat Lunak", "ikon": "🦷", "ilustrasi": "laptop",
    "ringkasan": "Perangkat lunak deep learning karya sendiri yang menemukan setiap gigi di foto intraoral, memeriksa karies per gigi, "
                 "menomori gigi dengan sistem FDI, dan menampilkan heatmap alasan keputusan. Dipasang di aplikasi Health Hub.",
    "prinsipKerja": "Foto HP dikoreksi orientasinya (EXIF), lalu detektor YOLO menemukan kotak setiap gigi. Tiap kotak dipotong dengan margin 10% "
                    "dan diklasifikasikan CNN ResNet50 (transfer learning dari ImageNet) menjadi sehat atau karies. Gigi dengan peluang penyakit di atas "
                    "ambang 0,971 dilaporkan, lengkap dengan nomor FDI hasil penyelarasan pemrograman dinamis dan heatmap CAM dari lapisan konvolusi terakhir. "
                    "Model berjalan sebagai file ONNX lewat onnxruntime.",
    "keselamatan": "Alat skrining, bukan diagnosis: hasil harus dikonfirmasi dokter gigi. Foto pasien adalah data pribadi; simpan dan kirim sesuai aturan "
                   "privasi. Performa turun pada data dari sumber berbeda (AUC lintas domain 0,787), jadi validasi ulang sebelum dipakai di populasi baru. "
                   "Perangkat lunak yang memberi informasi diagnosis termasuk Software as a Medical Device dan perlu jalur regulasi.",
    "blok": [
        {"id": "foto", "nama": "Foto intraoral", "fungsi": "Foto HP atau kamera intraoral, dikoreksi orientasi EXIF"},
        {"id": "deteksi", "nama": "Detektor gigi YOLO", "fungsi": "Menemukan kotak setiap gigi (mAP@0,5 0,952)"},
        {"id": "crop", "nama": "Potong per gigi", "fungsi": "Memotong tiap gigi dengan margin 10% dan resize 224 px"},
        {"id": "klasifikasi", "nama": "Classifier karies CNN", "fungsi": "ResNet50 menilai peluang karies tiap gigi"},
        {"id": "fdi", "nama": "Penomoran FDI", "fungsi": "Menyelaraskan nomor gigi sepanjang lengkung (95,4% benar)"},
        {"id": "heatmap", "nama": "Heatmap CAM", "fungsi": "Menunjukkan bagian gigi yang membuat model yakin"},
        {"id": "laporan", "nama": "Laporan odontogram", "fungsi": "Ringkasan temuan per gigi di aplikasi Health Hub"},
    ],
    "kontribusi": [
        {"materi": "ml-medis", "tingkat": 3, "blok": ["deteksi", "klasifikasi"], "peran": "Deep learning: CNN, transfer learning, training dengan backpropagation, early stopping.", "sub": []},
        {"materi": "citra", "tingkat": 3, "blok": ["foto", "crop", "heatmap"], "peran": "Pra-pemrosesan, augmentasi, normalisasi, dan peta aktivasi citra.", "sub": []},
        {"materi": "statistika", "tingkat": 3, "blok": ["klasifikasi", "laporan"], "peran": "Sensitivitas, spesifisitas, AUC, interval kepercayaan Wilson, bootstrap, McNemar, kappa.", "sub": []},
        {"materi": "pemrograman", "tingkat": 3, "blok": ["deteksi", "fdi", "laporan"], "peran": "Python, pipeline modular stage00–11, pemrograman dinamis untuk FDI, unit test.", "sub": []},
        {"materi": "ilmu-data", "tingkat": 2, "blok": ["foto"], "peran": "Akuisisi dan penyeragaman dataset, deduplikasi, split per pasien.", "sub": []},
        {"materi": "metopen", "tingkat": 2, "blok": ["laporan"], "peran": "Desain eksperimen terkontrol, seed berulang, tinjauan buta dokter gigi.", "sub": []},
        {"materi": "anatomi", "tingkat": 2, "blok": ["fdi"], "peran": "Anatomi gigi dan sistem penomoran FDI.", "sub": []},
        {"materi": "visualisasi", "tingkat": 2, "blok": ["heatmap", "laporan"], "peran": "Heatmap dan odontogram yang mudah dibaca.", "sub": []},
        {"materi": "mobile", "tingkat": 2, "blok": ["laporan"], "peran": "Integrasi model ONNX ke aplikasi Health Hub.", "sub": []},
        {"materi": "kalkulus", "tingkat": 1, "blok": ["klasifikasi"], "peran": "Turunan dan aturan rantai di balik backpropagation.", "sub": []},
        {"materi": "interaksi-pasien", "tingkat": 1, "blok": ["laporan"], "peran": "Menyampaikan hasil skrining kepada pasien tanpa menakut-nakuti.", "sub": []},
    ],
    "catatan": "", "umpanBalik": False, "referensi": [], "model": "", "sumber": SUMBER,
}
