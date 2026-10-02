# Panduan Penulisan Skripsi Takar (kontrak bersama semua penulis bab)

## 0. Sumber fakta (urutan otoritas)
1. `D:\barista\skripsi\tools\BRIEF.md` — fakta final proyek (dibuat setelah implementasi & evaluasi selesai; bila
   bertentangan dengan sumber lain, BRIEF yang benar).
2. `D:\barista\app\SPEC.md` — rancangan sistem (arsitektur, skema, algoritma, protokol evaluasi, §11 validasi data nyata).
3. Berkas hasil di `D:\barista\app\results\` (JSON/CSV/gambar). **Angka hanya boleh disalin dari berkas ini**, beserta
   nama berkasnya di komentar LaTeX (`% sumber: results/forecast_eval.json`).
4. `D:\barista\Skripsi Arahan Pak Budi.pdf` — arahan pembimbing (judul awal, latar belakang, rumusan masalah, batasan,
   metodologi Agile/Scrum, basis pengetahuan resep). Isi resep harus sama persis.
5. `D:\barista\skripsi\referensi_terverifikasi.json` — satu-satunya sumber kunci sitasi (211 entri terverifikasi
   Crossref/OpenAlex; gunakan `abstract_evidence` untuk memastikan klaim sesuai isi sumber).
6. `D:\barista\skripsi\rumus_terverifikasi.json` — satu-satunya sumber persamaan (status `confirmed`).
7. Gaya penulisan contoh: skripsi sebelumnya di
   `C:\Users\Lenovo\AppData\Local\Temp\claude\d--barista\6906ce7c-499f-41ab-b91b-a9fc37e25f63\scratchpad\skripsi_lama\`
   (bab1–bab5.tex) — tiru gaya, **jangan** menyalin isinya (topik berbeda).

Perubahan dari arahan (wajib dijelaskan jujur di Bab 1/3): Laravel+PWA → FastAPI (Python) + Vue.js berbasis web
responsif (keputusan 30 September 2026, alasan: kebutuhan pengolahan data dan AI); ditambah modul rekomendasi AI.

## 1. Kerangka dan label (pakai label ini persis agar rujukan silang antarbab konsisten)
- `bab:pendahuluan` — Bab 1: `sec:latar-belakang`, `sec:rumusan-masalah`, `sec:hipotesis`, `sec:ruang-lingkup`,
  `sec:tujuan-manfaat` (Tujuan, Manfaat), `sec:metode-ringkas`, `sec:sistematika`.
- `bab:tinjauan` — Bab 2: `sec:landasan-teori` dengan subbab
  `subsec:kedai-kopi` (industri kedai kopi, konsistensi, resep standar, SOP, pelatihan barista, konteks Indonesia),
  `subsec:penyeduhan` (TDS, EY, rasio seduh, *brewing control chart*/Golden Cup, espreso, *pour over* V60, susu),
  `subsec:penskalaan` (faktor konversi resep, *yield*, masalah penskalaan),
  `subsec:persediaan` (buku besar stok, BOM, *reorder point*, *safety stock*, *order-up-to*, tingkat layanan, *fill rate*),
  `subsec:sistem-web` (klien–server, REST API, SPA, FastAPI, Vue.js, basis data relasional, ERD, ORM/SQLite,
  keamanan: JWT, RBAC, Argon2),
  `subsec:kecerdasan-buatan` (definisi AI, sistem rekomendasi, rekomendasi makanan),
  `subsec:aturan-asosiasi` (*support*, *confidence*, *lift*, *leverage*, *conviction*, Apriori, FP-Growth),
  `subsec:peramalan` (naive, *seasonal naive*, rata-rata bergerak, SES, Holt-Winters, *gradient boosting*;
  MAE, RMSE, WAPE, MASE; *rolling origin*),
  `subsec:sistem-pakar` (komponen, *forward chaining*, fasilitas penjelasan),
  `subsec:llm-rag` (model bahasa besar, LLM lokal/Gemma, RAG, BM25, *tool calling*, halusinasi, evaluasi RAG),
  `subsec:evaluasi-rekomendasi` (HR@K, Precision@K, MRR, cakupan; *temporal split*; kebocoran data; *bootstrap*),
  `subsec:scrum`, `subsec:uml`, `subsec:pengujian` (*black-box*: EP & BVA, pengujian otomatis/E2E, UAT, SUS);
  `sec:penelitian-terkait` (narasi + `tab:penelitian-terkait`), `sec:kerangka-pemikiran` (`fig:kerangka-pemikiran`).
- `bab:metode` — Bab 3: `sec:desain-penelitian`, `sec:tahapan` (`fig:tahapan-penelitian`), `sec:analisis-kebutuhan`,
  `sec:perancangan-sistem` (`fig:arsitektur`, `fig:use-case`, `fig:activity-*`, `fig:sequence-*`, `fig:erd`,
  `fig:peta-situs`, `tab:endpoint`), `sec:perancangan-algoritma` (`alg:penskalaan`, `alg:restock`, `tab:aturan-pakar`),
  `sec:dataset` (`tab:dataset`, `tab:pemetaan-produk`), `sec:rancangan-eksperimen`, `sec:rancangan-pengujian`,
  `sec:jadwal`.
- `bab:hasil` — Bab 4: `sec:lingkungan-implementasi`, `sec:implementasi`, `sec:hasil-fungsional`,
  `sec:hasil-penskalaan`, `sec:hasil-pasangan`, `sec:hasil-peramalan`, `sec:hasil-restock`, `sec:hasil-sistem-pakar`,
  `sec:hasil-asisten` (tolok ukur tanya-jawab LLM lokal), `sec:hasil-kinerja`, `sec:hasil-uat`, `sec:pembahasan`.
  Bab 3 menambah `subsec:perancangan-asisten` di dalam `sec:perancangan-algoritma` dan `fig:alur-penskalaan`.
- `bab:simpulan` — Bab 5: `sec:simpulan`, `sec:saran`.
Persamaan: `eq:<nama>`; gambar `fig:<nama>`; tabel `tab:<nama>`; algoritma `alg:<nama>`.

## 2. Rumusan masalah dan hipotesis (tetap; Bab 1 menulisnya, bab lain merujuknya)
- RM1: Bagaimana merancang dan membangun aplikasi web manajemen resep dan standardisasi operasional kedai kopi yang
  mendokumentasikan takaran (rasio seduh, gramasi, waktu ekstraksi), SOP, dan inventaris bahan baku secara terintegrasi?
- RM2: Bagaimana merancang kalkulator takaran dinamis yang menghitung ulang kebutuhan bahan baku untuk variasi pesanan
  dengan tetap memenuhi batasan praktis (shot utuh, kapasitas cangkir, rasio seduh), dan bagaimana hasilnya dibandingkan
  dengan penskalaan linier?
- RM3: Bagaimana menerapkan kecerdasan buatan untuk rekomendasi pasangan menu, rekomendasi pengadaan (*restock*) bahan
  baku berbasis peramalan permintaan, koreksi parameter seduh, dan asisten tanya-jawab barista berbasis model bahasa
  lokal (LLM lokal dengan RAG dan *tool calling*, SPEC §12), serta seberapa baik kinerjanya pada data sampel fiktif,
  data nyata, dan tolok ukur tanya-jawab?
- RM4: Bagaimana kelayakan aplikasi ditinjau dari pengujian fungsional *black-box*, kinerja, dan penerimaan pengguna?
- H1 (penskalaan): algoritma berbasis batasan tidak menghasilkan pelanggaran batasan praktis (shot pecahan, luapan
  cangkir > 5%, penyimpangan rasio > 0,2) pada seluruh skenario uji, sedangkan penskalaan linier menghasilkan pelanggaran.
- H2 (pasangan menu): HR@5 FP-Growth lebih tinggi daripada baseline popularitas pada data uji (IBM dan Bread Basket),
  dengan interval kepercayaan *bootstrap* 95% dari selisih berpasangan di atas nol.
- H3 (peramalan): model terpilih menghasilkan WAPE lebih rendah daripada *seasonal naive* pada evaluasi *rolling origin*
  (Maven dan ihelon).
- H4 (*restock*): kebijakan berbasis peramalan menghasilkan *fill rate* lebih tinggi daripada ROP statis pada simulasi.
- H5 (asisten LLM lokal): pada tolok ukur tanya-jawab, kondisi LLM + RAG + *tools* menghasilkan akurasi jawaban lebih
  tinggi dan tingkat halusinasi angka lebih rendah daripada LLM tanpa konteks (*closed-book*).
Hasil boleh tidak mendukung hipotesis; laporkan apa adanya. Keputusan: H2 diuji dengan metode FP-Growth yang dipakai
aplikasi (hanya aturan *lift* > 1); varian semua aturan dilaporkan sebagai ablasi. "Model terpilih" pada H3 = WAPE
keseluruhan terendah pada Maven (aturan seleksi `results/forecast_eval.json`), diperiksa ulang pada ihelon.

Konvensi rumus hasil verifikasi (`rumus_terverifikasi.json`): bias dilaporkan sebagai rerata (ŷ − y) — positif berarti
ramalan terlalu tinggi — dan konvensi ini dinyatakan eksplisit; MASE musiman disitasi ke FPP3 (bukan Hyndman & Koehler
2006); *safety stock* untuk level *order-up-to* memakai √L sebagai penyederhanaan (varian √(L+R) dilaporkan bila ada);
rasio seduh espreso ditulis sesuai arah sumber; leverage memakai definisi supp(X∪Y) − supp(X)·supp(Y); rata-rata bergerak
sebagai ramalan datar ditandai "dirumuskan penulis".

## 3. Bahasa dan format
- Bahasa Indonesia baku (KBBI/PUEBI), kalimat efektif, formal, tanpa "kita"; gunakan "penelitian ini", "sistem",
  sesekali "penulis". Paragraf 4–8 kalimat, satu gagasan utama. Hindari klaim berlebihan ("selalu", "terbukti sempurna").
- Istilah asing yang tidak ada padanan baku dicetak miring `\textit{...}`: *coffee shop*, *brew ratio*, *pour over*,
  *latte art*, *framework*, *backend*, *frontend*, *dataset*, *machine learning*, *support*, *confidence*, *lift*,
  *restock*, *safety stock*, *reorder point*, *black-box*, *user acceptance testing*, *endpoint*, *single-page
  application*. Tidak miring: kopi, barista, resep, takaran, espreso (KBBI; boleh *espresso* miring bila merujuk nama
  menu), basis data, aplikasi web, sistem pakar, peramalan, inventaris, kecerdasan buatan. Nama produk/perangkat lunak
  (FastAPI, Vue.js, Python, SQLite) tidak miring. Dalam judul bagian gunakan `\texorpdfstring{\textit{X}}{X}`.
- Angka Indonesia: desimal koma (0,396; 39,6%), ribuan titik (49.894), rentang dengan `--` (90--92~$^\circ$C),
  satuan dipisah spasi tak-putus (`15~g`, `225~ml`, `30~detik`). Persen tanpa spasi (`24,4\%`).
- Keterangan tabel di atas tabel, gambar di bawah gambar, huruf awal tiap kata kapital (Title Case Indonesia), tanpa
  titik akhir. Tabel memakai `booktabs`; tabel panjang `longtable`. Setiap gambar/tabel dirujuk di teks sebelum muncul.
- Pseudocode: lingkungan `algorithm` + `algpseudocode` (`\Require`, `\Ensure`, `\State`, `\If`, `\For`).
- Persamaan bernomor dengan label, variabel dijelaskan tepat setelahnya, sumber disitasi di kalimat pengantar.
  Hanya persamaan berstatus `confirmed` di `rumus_terverifikasi.json`; rumus turunan sendiri ditandai "dirumuskan
  penulis berdasarkan ...".
- Gambar di `pic/` (PNG 300 dpi); diagram UML dari `pic/uml/*.puml`.

## 4. Sitasi (aturan BINUS, diperiksa `python tools/check_citations.py`)
- Hanya kunci dari `referensi_terverifikasi.json`. Sumber 1–5 penulis: `\citet*{}` / `\citep*{}`; ≥ 6 penulis:
  `\citet{}` / `\citep{}` (tercetak "dkk."). Jangan pakai `\cite{}`; jangan menulis "et al." sendiri.
- Klaim harus didukung `abstract_evidence` sumber; jangan mengklaim isi yang tidak tercatat di sana.
- Seluruh skripsi mensitasi ≥ 30 sumber berbeda terbitan 2021–2026; utamakan jurnal/konferensi bereputasi, sumber
  lokal Indonesia untuk konteks dan penelitian terkait.
- Dataset dan perangkat lunak juga disitasi (mis. `mavenanalytics2023coffee`, `pedregosa2011scikitlearn`).

## 5. Kejujuran data
- Data IBM dan Maven adalah **data sampel fiktif**; Bread Basket (lisensi tidak jelas — diungkapkan), ihelon (CC0,
  nyata), UC Davis/Cotter (CC0, nyata) dipakai sebagai validasi eksternal. Sebutkan ini setiap kali hasil dilaporkan.
- UAT/SUS belum dilaksanakan: tulis instrumen dan prosedurnya; hasil diberi penanda `[ISI SETELAH UAT]`.
- Nama orang/instansi: placeholder `[Nama Mahasiswa]`, `[NIM]`, `[Nama Dosen Pembimbing, Gelar]`, `[Nama Kedai Mitra]`.
- Jangan menulis hasil yang tidak ada di berkas `results/`. Bila suatu angka belum tersedia, tulis `[DIISI: ...]`.
