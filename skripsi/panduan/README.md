# TAKAR: Panduan Belajar Skripsi dan Persiapan Sidang

## 01 · Mulai dari nol

**Untuk siapa:** mahasiswa yang ingin memahami penelitian ini dari dasar, termasuk yang belum mengenal kopi, aplikasi web, atau kecerdasan buatan.

**Inti dalam satu kalimat:** Takar menghubungkan resep, cara membuat minuman, perhitungan variasi pesanan, pemakaian bahan, dan bantuan keputusan dalam satu aplikasi web, lalu menguji bagian-bagian tersebut dengan pembanding dan batas yang jelas.

Panduan ini adalah bahan belajar pendamping skripsi, bukan pengganti naskah resmi. Isinya mengikuti Bab 1–5, abstrak, spesifikasi aplikasi, dan berkas hasil lokal yang tersedia. Contoh yang disusun untuk membantu berhitung selalu disebut **ilustrasi**, sehingga tidak tercampur dengan hasil penelitian.

Rujukan `app/results` dan `dataset` menunjukkan asal bukti pada workspace lengkap. Folder itu tidak disertakan dalam repositori publik yang hanya berisi dokumen skripsi. Pembaca repositori dapat menelusuri pembahasan dan angka melalui Bab 3–5 pada sumber LaTeX dan PDF skripsi; reproduksi eksperimen memerlukan workspace lengkap.

### Cara memakai panduan

1. Baca halaman 2–4 untuk memahami masalah, tujuan, dan bentuk aplikasi.
2. Pelajari halaman 5–14 untuk memahami algoritma dan istilah.
3. Hafalkan makna hasil di halaman 15–19, terutama hasil yang tidak mendukung hipotesis.
4. Latih demo, pertanyaan, dan presentasi di halaman 20–25.

Jangan mulai dengan menghafal nama pustaka perangkat lunak. Mulailah dari pertanyaan: **pesanan masuk, bagaimana sistem menghitung takaran yang bisa dikerjakan, lalu bagaimana takaran tersebut memengaruhi stok?** Setelah alurnya dipahami, istilah teknis akan lebih mudah diingat.

### Empat kalimat yang harus selalu diingat

- IBM dan Maven adalah **data sampel fiktif**, bukan transaksi kedai mitra.
- H2 dan H3 **tidak didukung pada pemeriksaan data nyata** yang dilaporkan.
- Akurasi asisten 95,0% adalah **hasil pipeline pada tolok ukur internal yang memandu perbaikan router**.
- UAT bersama barista dan skor SUS **belum tersedia**.

Nama mahasiswa, NIM, pembimbing, dan mitra pada naskah masih memakai placeholder. Lengkapi dengan identitas yang benar sebelum pengumpulan resmi; jangan menganggap dokumen siap administrasi hanya karena PDF sudah terbentuk.

**Sumber lokal:** `skripsi/abstrak.tex`; `skripsi/bab1.tex`, Ruang Lingkup; `skripsi/bab5.tex`, Simpulan; `skripsi/tools/PANDUAN_PENULISAN.md`.

<!-- PAGEBREAK -->

## 02 · Benang merah: mengapa penelitian ini ada?

Bayangkan barista A dan B membuat latte dengan nama yang sama. A mengingat takaran dari pengalaman, sedangkan B baru belajar. Jika resep hanya ada di ingatan atau kertas terpisah, takaran dapat berbeda. Ketika pelanggan meminta lebih besar, kurang manis, atau tambahan espreso, bahan perlu dihitung ulang. Setelah minuman dibuat, pemakaian susu dan biji juga harus masuk ke catatan stok.

Tiga masalah yang dipakai penelitian adalah ketidakseragaman takaran antarbarista, kebutuhan bantuan belajar staf baru, serta inventaris yang terpisah dari produksi. Takar menyatukan pekerjaan tersebut di sekitar **resep standar**. Resep menjadi satu sumber untuk melihat komposisi, menghitung pesanan, menampilkan langkah, dan menurunkan kebutuhan bahan.

### Alur yang harus bisa diceritakan

**Resep standar → variasi pesanan → kalkulator berbasis batasan → panduan seduh → catat produksi → bahan berkurang pada buku besar stok.**

Di atas alur itu, modul keputusan memberi saran pasangan menu, perkiraan penjualan dan pemesanan bahan, diagnosis seduh, serta tanya-jawab berbasis sumber lokal. Saran AI melengkapi alur operasional; kebenaran takaran dan pencatatan stok tetap ditangani layanan aplikasi.

### Mengapa tidak cukup mengalikan semua bahan?

Susu dapat ditakar 150 ml, tetapi jumlah shot dalam model resep harus utuh. Tambahan shot juga mengambil ruang di cangkir, sehingga susu pengisi perlu menyesuaikan. Pada V60, perubahan dosis harus menjaga rasio kopi dan air serta target tuang kumulatif. Jadi setiap bahan memerlukan aturan sesuai sifatnya.

### Apa kontribusinya?

Kontribusi penelitian terutama berupa integrasi resep, SOP, kalkulator dan stok, beserta evaluasi yang membandingkan algoritma dengan metode sederhana. FP-Growth, gradient boosting, RAG, dan forward chaining sudah merupakan metode yang dikenal; penelitian ini tidak mengklaim menemukan semua algoritma tersebut.

**Cara menjawab sidang:** “Saya membangun sistem yang memakai resep sebagai penghubung antara takaran, prosedur dan kebutuhan bahan. Lalu saya menguji fungsi dan modul keputusan secara terpisah, termasuk pada data eksternal. Manfaat pada rasa, waktu pelatihan dan keuntungan kedai belum diukur melalui pengguna nyata.”

**Sumber lokal:** `skripsi/bab1.tex`, Latar Belakang dan Tujuan; `skripsi/bab2.tex`, Penelitian Terkait dan Kerangka Pemikiran; `skripsi/bab3.tex`, Desain Penelitian.

<!-- PAGEBREAK -->

## 03 · Bab 1 dan Bab 2: masalah, teori, dan pertanyaan penelitian

**Bab 1 menjawab “mengapa dan apa yang diteliti?”** Latar belakang menjelaskan masalah kedai. Rumusan masalah mengubahnya menjadi pertanyaan yang dapat dijawab. Tujuan mengikuti rumusan masalah. Ruang lingkup membatasi fitur, teknologi, data, pengguna, dan bentuk pengujian.

| Rumusan | Pertanyaan sederhana | Cara menjawab |
|---|---|---|
| RM1 | Bisakah resep, SOP dan stok dihubungkan? | Rancangan dan implementasi aplikasi |
| RM2 | Bisakah variasi pesanan dihitung dengan batas praktis? | Pembanding linier dan H1 |
| RM3 | Seberapa baik modul AI dan asisten? | Evaluasi H2–H5 dan sistem pakar |
| RM4 | Apakah fungsi, kinerja dan penerimaan pengguna memadai? | Tes otomatis, latensi, dan UAT yang masih direncanakan |

**Hipotesis** adalah dugaan yang akan diperiksa, bukan kesimpulan awal. H1 membahas pelanggaran takaran; H2 ketepatan pasangan menu; H3 galat prakiraan; H4 pemenuhan permintaan bahan; H5 ketepatan asisten dan angka tanpa dasar. Dugaan yang tidak didukung tetap menjadi hasil ilmiah yang perlu dijelaskan.

**Bab 2 menjawab “konsep apa yang mendasari solusi?”** Teori disusun mengikuti pekerjaan aplikasi: resep dan penyeduhan, penskalaan, persediaan, aplikasi web, AI, evaluasi, pengembangan, dan pengujian. Bagian penelitian terkait menjelaskan posisi Takar dibanding sistem lain. Kerangka pemikiran menghubungkan masalah, solusi, metode, evaluasi, dan hasil.

### Istilah awal yang sering muncul

- **Resep standar:** komposisi dan prosedur yang menjadi acuan kedai.
- **SOP:** urutan kerja yang disepakati, misalnya pembukaan bar atau kalibrasi.
- **BOM:** daftar bahan penyusun produk; diterangkan pada halaman 7.
- **Baseline:** pembanding sederhana agar keunggulan metode dapat dinilai.
- **Validasi eksternal:** pemeriksaan memakai sumber berbeda dari data pengembangan.
- **Ruang lingkup:** batas penelitian; Takar satu outlet, tanpa kasir, sinkronisasi gerai, PWA atau mode luring.

Arahan awal menggunakan Laravel dan PWA. Naskah menjelaskan perubahan menjadi FastAPI dan Vue.js pada 30 September 2026 untuk menyatukan API, pengolahan data, dan AI dalam Python. Tampilan responsif berarti menyesuaikan layar; itu tidak sama dengan menyediakan operasi luring.

**Sumber lokal:** `skripsi/bab1.tex`, Rumusan Masalah, Hipotesis, Ruang Lingkup; `skripsi/bab2.tex`, Landasan Teori; `skripsi/bab3.tex`, Desain Penelitian.

<!-- PAGEBREAK -->

## 04 · Bab 3: aplikasi bekerja melalui apa?

**Bab 3 menjawab “bagaimana penelitian dan sistem dikerjakan?”** Pendekatannya rancang bangun dengan evaluasi komparatif. Aplikasi dibuat bertahap melalui Scrum yang disesuaikan untuk satu mahasiswa, lalu fungsi dan algoritma diperiksa.

### Arsitektur dalam bahasa sederhana

1. **Vue.js di browser** menampilkan resep, formulir, stok dan jawaban. Bagian ini disebut frontend.
2. **FastAPI di server** memeriksa identitas, hak akses dan masukan, lalu menjalankan logika. Bagian ini disebut backend.
3. **SQLite** menyimpan resep, bahan, produksi dan pergerakan stok dalam basis data.
4. **Skrip AI dan evaluasi** membaca dataset, melatih model dan menulis hasil JSON/CSV.
5. **Ollama** menjalankan model bahasa lokal yang dipakai asisten bila tersedia.

**API** adalah jalur komunikasi antarmuka dan server. **Endpoint** adalah alamat suatu layanan, misalnya kalkulator. **JSON** adalah bentuk data yang dikirim. **ORM/SQLAlchemy** membantu kode Python bekerja dengan tabel. **ERD** menunjukkan hubungan data; UML menunjukkan aktor, aktivitas, dan urutan komunikasi.

### Hak akses dan keamanan

Barista dapat membaca standar, memakai kalkulator, mencatat produksi, dan mengerjakan checklist. Kepala barista dan manajer juga dapat mengubah resep dan mengelola bahan. Hanya manajer mengelola pengguna, menonaktifkan resep, dan melatih ulang model. Server memeriksa hak tersebut, sehingga menyembunyikan tombol saja bukan pengamanan utama.

**JWT** membawa identitas sesi; **Argon2** dipakai untuk hash kata sandi; **RBAC** membatasi tindakan berdasarkan peran. Hash kata sandi bukan kata sandi yang disimpan dalam teks biasa. Keamanan tetap membutuhkan pengelolaan server dan log yang baik.

### Unit evaluasi berbeda untuk setiap tugas

Pesanan menjadi unit penskalaan; kueri keranjang menjadi unit rekomendasi; produk–outlet–hari menjadi unit prakiraan; bahan–hari menjadi unit simulasi stok; seduhan menjadi unit sistem pakar; pertanyaan menjadi unit asisten. HR@5 dan fill rate tidak bisa dibandingkan seolah ukuran yang sama.

**Kalimat sidang:** “Browser mengirim masukan, server menghitung dan memvalidasi, basis data menyimpan hasil. Aturan penting dan hak akses diperiksa di server agar konsistensi tidak bergantung pada tampilan.”

**Sumber lokal:** `skripsi/bab3.tex`, Desain Penelitian, Analisis Kebutuhan, Perancangan Sistem; gambar arsitektur/ERD; tabel Kelompok Endpoint API Utama (`tab:endpoint`).

<!-- PAGEBREAK -->

## 05 · Penskalaan: aturan tiap bahan harus berbeda

**Penskalaan** berarti menyesuaikan resep dasar dengan ukuran, dosis atau jumlah pesanan. Faktor ukuran awal adalah volume diminta dibagi volume dasar. Untuk V60, faktor dapat berasal dari dosis baru dibagi dosis dasar.

| Aturan komponen | Makna | Contoh |
|---|---|---|
| Proporsional | Dikalikan faktor | Bahan yang mengikuti ukuran |
| Tetap | Tidak berubah karena ukuran | Komponen dengan takaran tetap |
| Diskret | Harus dalam unit utuh | Shot espreso |
| Rasio / pengisi | Bergantung pada hasil lain | Air V60 / susu top up |

Pemanis mengikuti persentase kemanisan, dengan pengecualian karakter resep yang didokumentasikan. Air berbasis rasio dihitung setelah dosis final. Susu pengisi dihitung setelah ruang yang dipakai bahan lain diketahui. Pembulatan mengikuti ketelitian bahan, bukan sekadar jumlah digit yang sama untuk semua komponen.

### Urutan algoritma yang perlu dipahami

1. Tentukan ukuran cangkir atau faktor dosis, sajian, dan penggantian bahan yang sah.
2. Hitung bahan proporsional, tetap dan diskret; terapkan kemanisan dan tambahan shot.
3. Bulatkan ke ketelitian praktis, kemudian hitung bahan yang bergantung pada rasio.
4. Hitung ruang cangkir; atur bahan pengisi dan es sesuai model volume.
5. Periksa luapan, kurang isi, rasio, dosis dan ketersediaan stok.
6. Skala target langkah, uraikan subresep, lalu kalikan kebutuhan per cangkir dengan jumlah cangkir.

Urutan ini penting. Jika susu dihitung dahulu, tambahan espreso sesudahnya dapat membuat cangkir terlalu penuh. Jika air dihitung sebelum pembulatan dosis, rasio akhir bisa bergeser.

### Tiga metode pembanding

**Linier mentah** mengalikan semua komponen. **Linier dibulatkan** menambahkan pembulatan tetapi belum mengatur ruang cangkir. **Berbasis batasan** menambahkan aturan bahan dan hubungan kapasitas. Pembanding kedua memperlihatkan apakah manfaat hanya berasal dari pembulatan atau juga dari pengelolaan kapasitas.

Luapan untuk H1 berarti volume lebih dari 1,05 kali kapasitas, sedangkan penyimpangan rasio berarti selisih mutlak lebih dari 0,2. Ini ambang evaluasi penelitian, bukan izin praktis untuk sengaja meluapkan minuman 5%.

**Sumber lokal:** `skripsi/bab3.tex`, Penskalaan Resep Berbasis Batasan dan Algoritma `alg:penskalaan`; `skripsi/bab1.tex`, Hipotesis; `app/backend/app/seed/ASSUMPTIONS.md`.

<!-- PAGEBREAK -->

## 06 · Hitung sendiri: V60 dan ruang latte

### Contoh V60 dari aturan skripsi

Resep dasar V60 memakai 15 g kopi dan 225 ml air, sehingga rasio air : kopi adalah 225 / 15 = 15, biasa ditulis **1:15** dari sisi kopi : air. Target tuang kumulatifnya 45, 130 dan 225 ml.

Jika dosis menjadi 20 g, faktor dosis = 20 / 15 = 1,3333. Air menjadi 20 × 15 = **300 ml**. Target tahap menjadi:

| Tahap | Target kumulatif baru | Air tambahan tahap |
|---|---|---|
| Blooming | 45 × 1,3333 = 60 ml | 60 ml |
| Tuang kedua | 130 × 1,3333 ≈ 173,3 ml | 113,3 ml |
| Tuang ketiga | 225 × 1,3333 = 300 ml | 126,7 ml |

Kumulatif berarti “total sampai tahap ini”. Menuang 60 + 173,3 + 300 ml sebagai tiga tambahan terpisah menghasilkan 533,3 ml dan salah. Waktu penanda langkah tidak ikut dikalikan oleh algoritma; kelayakan rasa dan waktu tetap memerlukan pemeriksaan barista.

Jika dua cangkir dibuat dengan resep 20 g tersebut, kebutuhan totalnya 40 g kopi dan 600 ml air. Total berasal dari takaran per cangkir yang sudah final.

### Ilustrasi kapasitas latte, bukan hasil eksperimen

Gunakan cangkir 240 ml, satu unit shot aplikasi = 36 ml, dan faktor ekspansi susu steam 1,2. Abaikan komponen lain pada ilustrasi ini. Ruang susu setelah satu shot adalah 240 − 36 = 204 ml. Susu cair yang ditakar menjadi 204 / 1,2 = **170 ml**.

Jika ditambah satu shot, espreso menjadi 72 ml. Ruang susu tinggal 240 − 72 = 168 ml, sehingga susu cair menjadi 168 / 1,2 = **140 ml**. Menambah shot sambil mempertahankan 170 ml susu menghasilkan 72 + 170 × 1,2 = 276 ml dalam model volume: cangkir terlalu penuh.

Di aplikasi, satu “shot” diinterpretasikan sebagai satu subresep double shot, dengan dosis 18 g dan hasil 36 g. Itu asumsi proyek yang didokumentasikan, bukan definisi universal semua kedai. Volume espreso dan ekspansi susu juga penyederhanaan model.

**Sumber lokal:** `skripsi/bab4.tex`, Hasil Pengujian Fungsional; `skripsi/bab3.tex`, Penskalaan; `app/backend/app/seed/ASSUMPTIONS.md`, A01–A05 dan A14.

<!-- PAGEBREAK -->

## 07 · BOM dan stok: resep berubah menjadi pemakaian bahan

**Bill of materials atau BOM** berarti daftar bahan untuk membuat produk. Resep latte menyimpan susu dan espreso; espreso merupakan subresep yang membutuhkan biji. Untuk stok, sistem menguraikan subresep hingga menjadi bahan dasar.

### Ilustrasi perhitungan, bukan catatan produksi nyata

Anggap satu latte memakai satu unit subresep espreso dengan 18 g biji dan 170 ml susu. Membuat tiga latte membutuhkan 3 × 18 = **54 g biji** dan 3 × 170 = **510 ml susu**. Jika stok awal ilustratif 1.000 g biji dan 2.000 ml susu, setelah produksi saldo menjadi 946 g dan 1.490 ml.

| Pergerakan | Biji | Susu |
|---|---|---|
| Saldo awal ilustrasi | 1.000 g | 2.000 ml |
| Pemakaian tiga latte | −54 g | −510 ml |
| Saldo akhir | 946 g | 1.490 ml |

**Buku besar stok** menyimpan riwayat perubahan, bukan hanya angka saldo terakhir. Penerimaan menambah stok; produksi dan limbah mengurangi stok; stock opname menyesuaikan hasil hitungan fisik. Catatan ini membantu menelusuri mengapa saldo berubah.

### Pratinjau berbeda dari pencatatan produksi

Membuka kalkulator hanya menghitung kebutuhan. Stok baru berubah ketika pengguna memilih **catat produksi**. Tanpa pemisahan ini, mencoba ukuran atau membuka resep dapat salah dianggap pemakaian bahan.

Pencatatan produksi dan pergerakan stok dilakukan **atomik**: perubahan terkait diselesaikan sebagai satu transaksi, atau dibatalkan bila terjadi kegagalan. **Idempoten** berarti pengiriman ulang permintaan yang sama tidak membuat efek kedua. Pengenal permintaan klien digunakan untuk mencegah stok berkurang dua kali saat jaringan atau pengguna mengirim ulang.

### Batas yang harus disebutkan

Saldo tetap bergantung pada produksi yang benar-benar dicatat, resep yang benar, dan satuan yang konsisten. Bahan terbuang dan penerimaan nyata juga harus dicatat. Air dan es dalam demonstrasi tidak dilacak sebagai stok. Sistem tidak otomatis mengetahui minuman yang dibuat tetapi tidak dicatat, dan tidak terhubung ke kasir atau sensor.

**Kalimat sidang:** “Resep menjadi dasar pemakaian bahan. Produksi dicatat sekali, subresep diuraikan, lalu pergerakan stok ditulis dalam transaksi yang konsisten.”

**Sumber lokal:** `skripsi/bab3.tex`, Analisis Kebutuhan dan Perancangan Sistem; `skripsi/bab4.tex`, Implementasi; `app/backend/app/seed/ASSUMPTIONS.md`, A17.

<!-- PAGEBREAK -->

## 08 · FP-Growth: menemukan menu yang sering dibeli bersama

**Keranjang transaksi** adalah kumpulan menu pada satu struk. **Itemset** adalah himpunan menu, misalnya {latte, croissant}. **Aturan asosiasi** X → Y berarti transaksi yang mengandung X cenderung juga mengandung Y. Aturan tersebut menunjukkan pola bersama, bukan sebab-akibat.

FP-Growth menghitung item yang cukup sering, mengurutkannya dan merangkum transaksi dalam **FP-tree**. Jalur bersama dapat memakai bagian pohon yang sama. Dari pola bersyarat dalam pohon, algoritma menemukan itemset sering tanpa membangkitkan kandidat dengan cara Apriori. Itemset kemudian dipakai membentuk aturan asosiasi.

### Ilustrasi 100 struk, bukan dataset penelitian

Misalkan 40 struk memiliki latte, 30 memiliki croissant, dan 20 memiliki keduanya.

- **Support pasangan** = 20 / 100 = **0,20**: 20% seluruh struk memiliki pasangan itu.
- **Confidence latte → croissant** = 20 / 40 = **0,50**: separuh struk dengan latte juga memiliki croissant.
- **Lift** = 0,50 / 0,30 = **1,67**: kemunculan croissant bersama latte lebih tinggi daripada proporsi croissant secara umum.
- **Leverage** = 0,20 − (0,40 × 0,30) = **0,08**: pasangan muncul delapan poin persentase lebih tinggi daripada pola independen.
- **Conviction** = (1 − 0,30) / (1 − 0,50) = **1,40**: ukuran tambahan implikasi aturan melalui kegagalannya. Ini dilaporkan bersama ukuran lain, tetapi aplikasi mengurutkan terutama confidence dan lift.

Confidence yang tinggi belum otomatis menunjukkan hubungan khusus. Item yang memang sangat populer dapat sering menjadi pasangan banyak item. Lift membandingkan confidence dengan popularitas umum konsekuen. Lift di atas satu menunjukkan asosiasi positif menurut ukuran ini, bukan jaminan pelanggan berikutnya akan membeli.

### Apa yang dilakukan aplikasi?

Ukuran produk dinormalisasi menjadi kunci menu. Aplikasi mencocokkan item yang dipilih dengan anteseden, mengurutkan konsekuen menurut confidence lalu lift, menghapus duplikat, dan mengisi tempat kosong dengan item populer yang diberi penanda. Aturan yang ditampilkan harus memiliki **lift > 1**. Produk yang tidak mempunyai padanan persis dapat memakai proksi yang dinyatakan.

Saringan tersebut perlu diuji: pada Bread Basket, popularitas Coffee membuat sebagian aturan menuju Coffee memiliki lift yang tidak lolos. Itu dapat membuang pasangan yang relevan. Varian tanpa saringan dipakai sebagai **ablasi**, yaitu pemeriksaan perubahan satu komponen, bukan mengganti diam-diam metode aplikasi.

**Sumber lokal:** `skripsi/bab2.tex`, Aturan Asosiasi dan FP-Growth (`subsec:aturan-asosiasi`); `skripsi/bab3.tex`, Pasangan Menu dan Peramalan; `skripsi/bab4.tex`, Hasil Pasangan Menu.

<!-- PAGEBREAK -->

## 09 · Menilai rekomendasi: HR@5, MRR, dan interval kepercayaan

Rekomendasi tidak cukup dinilai dari aturan yang terlihat masuk akal. Penelitian membagi transaksi menurut waktu. Bagian awal digunakan untuk latih dan pemilihan ambang; bagian akhir menjadi uji. Pada keranjang uji dengan minimal dua item berbeda, satu item disembunyikan bergantian. Sistem harus menyarankan item tersebut dari item yang tersisa. Ini disebut **leave-one-out per keranjang**.

### Ilustrasi empat kueri

Misalkan item yang disembunyikan muncul pada peringkat 1, peringkat 2, tidak muncul dalam lima besar, dan peringkat 5.

- **HR@5** = jumlah kueri berhasil / seluruh kueri = 3 / 4 = **0,75**.
- **MRR@5** = rata-rata kebalikan peringkat = (1 + 1/2 + 0 + 1/5) / 4 = **0,425**.
- **Precision@5** = 3 / (4 × 5) = **0,15**, jika setiap kueri memiliki satu item relevan dan lima rekomendasi.

HR menilai apakah item masuk daftar. MRR menilai seberapa tinggi posisi item yang benar. Dalam protokol satu item tersembunyi, Precision@5 paling besar 0,20; angka 0,15 bukan otomatis “buruk” seperti interpretasi akurasi klasifikasi 15%.

**Cakupan katalog** adalah proporsi item katalog yang pernah direkomendasikan. **Cakupan kueri** penelitian adalah proporsi kueri yang memicu minimal satu aturan. Mengisi daftar dengan popularitas dapat meningkatkan keberhasilan, tetapi manfaat aturan dan isian perlu dibedakan.

### Mengapa ada bootstrap?

Selisih kecil dapat berubah jika keranjang yang diuji berbeda. Bootstrap mengambil ulang keranjang dengan pengembalian, lalu menghitung ulang metrik dan selisih pada sampel yang sama untuk kedua metode. Keranjang menjadi unit karena beberapa kueri dari satu struk saling berkaitan.

Untuk H2, selisih **HR@5 FP-Growth − popularitas** harus mempunyai batas bawah interval kepercayaan 95% di atas nol. Jika interval melintasi nol, data belum menunjukkan keunggulan yang meyakinkan. Interval bukan rentang tempat 95% kueri berada dan bukan jaminan pasti pada seluruh kedai.

Bandingkan dengan **popularitas** dan **ko-okurensi**, yaitu pola kemunculan bersama sederhana. Kompleksitas algoritma tidak menjamin hasil lebih baik.

**Sumber lokal:** `skripsi/bab2.tex`, Evaluasi Sistem Rekomendasi (`subsec:evaluasi-rekomendasi`); `skripsi/bab3.tex`, Rancangan Eksperimen; `app/results/external/E1_pairing_breadbasket.json`.

<!-- PAGEBREAK -->

## 10 · Peramalan: memperkirakan kebutuhan berikutnya

**Peramalan** memakai pengamatan masa lalu untuk memperkirakan nilai masa depan. Pada Takar, baris penjualan menjadi deret jumlah unit harian per produk dan outlet. Tanggal yang tidak mempunyai transaksi diberi nol sesuai pemrosesan penelitian.

| Metode | Penjelasan sederhana | Bentuk perkiraan |
|---|---|---|
| Naive | Nilai terbaru diulang | Besok seperti hari terakhir |
| Seasonal naive | Ulang pola hari yang sama | Senin seperti Senin lalu |
| Rata-rata 7 hari | Rerata penjualan terakhir | Nilai datar dari tujuh hari |
| SES / Holt-Winters | Pemulusan data | Level / level, tren dan musim |

Metode keenam adalah **histogram gradient boosting global**. Model mempelajari hubungan fitur dengan penjualan melalui pohon yang memperbaiki kesalahan model sebelumnya secara bertahap. Kata “global” berarti satu model dilatih dari banyak deret menu dan outlet, bukan satu model terpisah untuk setiap menu.

**Lag** adalah nilai sebelumnya, misalnya penjualan tujuh hari lalu. **Fitur** adalah masukan seperti lag, rata-rata masa lalu, hari dalam minggu dan horizon. **Horizon** adalah jarak ramalan, misalnya tujuh hari ke depan. Pada pendekatan langsung, tiap horizon diperkirakan dari informasi yang tersedia pada origin, bukan menganggap angka masa depan sudah diketahui.

### Ilustrasi pola mingguan

Jika Senin terakhir terjual 12 cangkir, seasonal naive memprediksi Senin berikutnya 12. Jika penjualan tujuh hari terakhir totalnya 98, moving average memprediksi 98 / 7 = 14 per hari. Kedua contoh ini hanya menjelaskan cara kerja, bukan hasil dataset Takar.

### Rolling origin mencegah melihat masa depan

Penelitian memakai delapan origin mingguan dan horizon tujuh hari. Pada origin pertama model hanya melihat data sampai titik itu, meramal tujuh hari, lalu origin digeser dan model dilatih kembali. Informasi sesudah origin tidak boleh masuk fitur atau pelatihan. Pelanggaran ini disebut **kebocoran data**.

Model aplikasi dipilih dari WAPE keseluruhan terendah pada Maven. Setelah dipilih, model yang sama diperiksa pada ihelon; memilih ulang setelah melihat hasil uji akan membuat klaim evaluasi terlalu optimistis.

**Sumber lokal:** `skripsi/bab2.tex`, Peramalan Permintaan; `skripsi/bab3.tex`, Pasangan Menu dan Peramalan serta Rancangan Eksperimen; `app/results/forecast_eval.json`, `protocol`.

<!-- PAGEBREAK -->

## 11 · Cara membaca MAE, RMSE, WAPE, MASE, dan bias

Gunakan **y** untuk penjualan aktual dan **y_hat** untuk ramalan. Galat dalam rumus MAE/RMSE adalah aktual dikurangi ramalan. Makin kecil galat absolut umumnya makin baik.

### Ilustrasi tiga hari, bukan hasil penelitian

| Hari | Aktual | Ramalan | Galat absolut |
|---|---|---|---|
| 1 | 10 | 8 | 2 |
| 2 | 20 | 25 | 5 |
| 3 | 0 | 2 | 2 |

**MAE** = rata-rata galat absolut = (2 + 5 + 2) / 3 = **3 cangkir**. Artinya rata-rata meleset tiga cangkir per titik pada ilustrasi.

**RMSE** = akar rata-rata kuadrat galat = akar[(4 + 25 + 4) / 3] = akar 11 ≈ **3,32 cangkir**. Penguadratan memberi penalti lebih besar pada kesalahan besar.

**WAPE** = jumlah galat absolut / jumlah aktual absolut = 9 / 30 = **0,30 atau 30%**. Denominator menjumlahkan volume aktual; tidak membagi satu per satu dengan hari aktual nol. Jika jumlah aktual seluruh bagian yang dinilai nol, WAPE tetap tidak terdefinisi. WAPE 39,64% bukan otomatis “akurasi 60,36%” untuk setiap hari atau menu.

**MASE** = MAE ramalan dibagi skala galat naive musiman pada data latih. Jika skala galat latih ilustratif 4 cangkir, MASE = 3 / 4 = **0,75**. Nilai di bawah satu berarti MAE lebih kecil daripada skala pembanding latih tersebut. Ini bukan selalu sama dengan mengalahkan seasonal naive pada jendela uji. Bila denominator nol, MASE tidak dapat dihitung.

**Bias penelitian** memakai rata-rata (ramalan − aktual). Pada contoh: (−2 + 5 + 2) / 3 = **+1,67 cangkir**. Tanda positif berarti cenderung terlalu tinggi; tanda negatif berarti terlalu rendah. Beberapa sumber memakai tanda kebalikan, sehingga konvensi perlu disebutkan.

Pada WAPE keseluruhan Takar, menu bervolume besar lebih banyak menyumbang denominator dan galat. Nilai agregat dapat menutupi menu tertentu yang kurang akurat. Sebutkan tingkat pelaporan: per produk, keseluruhan, bahan, atau total harian.

**Sumber lokal:** `skripsi/bab2.tex`, persamaan MAE/RMSE, WAPE, MASE dan Bias (`eq:mae-rmse`, `eq:wape`, `eq:mase`, `eq:bias`); `skripsi/bab3.tex`, Rancangan Eksperimen.

<!-- PAGEBREAK -->

## 12 · Restock: dari ramalan minuman ke saran bahan

**Restock** adalah pengisian ulang persediaan. Ramalan 20 latte bukan langsung “beli 20 susu”. Sistem memakai BOM untuk mengubah ramalan produk menjadi kebutuhan setiap bahan, kemudian memperhitungkan pasokan dan posisi stok.

- **Lead time L:** waktu tunggu bahan sejak dipesan sampai datang.
- **Safety stock SS:** cadangan untuk ketidakpastian permintaan.
- **ROP:** batas yang memicu pertimbangan pemesanan.
- **Order-up-to S:** tingkat stok sasaran yang ingin dicapai.
- **Posisi stok:** pada replay, stok tersedia ditambah bahan yang sedang dalam perjalanan. Rekomendasi aplikasi saat ini memakai stok tersedia karena belum mempunyai buku pesanan pembelian; ini keterbatasan penting.

### Rumus rancangan penelitian

`SS = z × sigma × akar(L)`

`ROP = kebutuhan ramalan selama L hari + SS`

`S = kebutuhan ramalan selama L + R hari + SS`

`jumlah saran = maksimum(0, S − posisi stok), dibulatkan ke kemasan`

Sigma adalah simpangan baku galat harian dari kalibrasi. Periode tinjau R = 1 hari dan z = 1,65 adalah parameter contoh. Pemakaian akar L juga pada level sasaran adalah penyederhanaan rancangan, bukan aturan universal seluruh situasi pemasok.

### Ilustrasi numerik, bukan kebutuhan pemasok nyata

Anggap kebutuhan susu 1.000 ml per hari, L = 2 hari, sigma = 100 ml dan z = 1,65. SS = 1,65 × 100 × akar 2 ≈ **233 ml**. ROP = 2.000 + 233 = **2.233 ml**. Dengan R = 1, S = 3.000 + 233 = **3.233 ml**.

Jika posisi stok 1.800 ml, kebutuhan pesan = 3.233 − 1.800 = 1.433 ml. Untuk kemasan 1.000 ml, pembulatan ke atas menghasilkan **2 kemasan atau 2.000 ml**. Hasil model harus dibaca bersama umur simpan, ruang penyimpanan, biaya, dan jadwal pemasok yang nyata.

**Fill rate** = jumlah permintaan yang terpenuhi / jumlah permintaan. Jika kebutuhan ilustratif 10.000 ml dan terpenuhi 9.000 ml, fill rate = 0,90. Hari stockout menghitung hari kekurangan; satu hari kekurangan kecil dan besar sama-sama satu hari, sehingga metriknya saling melengkapi.

**Sumber lokal:** `skripsi/bab3.tex`, Rekomendasi Pengisian Ulang (`eq:restock`); `skripsi/bab2.tex`, Persediaan; `app/backend/app/seed/ASSUMPTIONS.md`, A16 dan A24.

<!-- PAGEBREAK -->

## 13 · Sistem pakar: kuat tidak sama dengan banyak terekstraksi

Sistem pakar memakai **aturan jika–maka** yang disimpan bersama sumber, prioritas dan alasan. Ia menerima metode seduh, dosis, air atau massa minuman, TDS bila ada, waktu, suhu dan deskriptor rasa.

**Forward chaining** dimulai dari fakta masukan. Mesin memilih aturan yang cocok, menambahkan kesimpulan menjadi fakta baru, lalu mengulang hingga tidak ada aturan baru yang bisa dijalankan. Jejak aturan memungkinkan pengguna melihat alasan diagnosis, bukan hanya membaca perintah.

### Dua ukuran yang jangan tertukar

**TDS** menyatakan proporsi padatan kopi terlarut terhadap massa minuman. Ini ukuran kekuatan atau kepekatan. **EY** menyatakan proporsi massa kopi awal yang berpindah ke minuman. Ini ukuran rendemen ekstraksi.

`EY (%) = TDS (%) × massa minuman / dosis kopi`

**Ilustrasi:** dosis 15 g, massa minuman terukur 200 g, dan TDS 1,50%. EY = 1,50 × 200 / 15 = **20%**. Dalam bentuk fraksi, 0,015 × 200 / 15 = 0,20, lalu dikonversi menjadi 20%. Jangan memakai 1,50 sebagai fraksi tanpa konversi.

Air yang dituangkan berbeda dari minuman yang didapat karena sebagian tertahan dalam ampas. Jika memakai 225 g air sebagai massa minuman pada contoh yang sebenarnya menghasilkan 200 g, EY menjadi 22,5% dan dapat menyesatkan. Massa yang diukur harus jelas.

### Ambang teknis bukan jaminan pelanggan suka

Kotak Golden Cup klasik yang dibahas naskah memakai TDS 1,15–1,35% dan EY 18–22%. Bab 2 juga membahas standar dengan rentang TDS berbeda. Resep V60 arahan 1:15 dapat lebih pekat daripada kotak klasik; resep arahan tetap menjadi standar kedai, dan perbedaan dijelaskan.

Validasi eksternal memeriksa rumus EY dan sebagian arah diagnosis. Setelah satu seduhan tidak wajar ditolak, 3.164 penilaian atas 161 seduhan dianalisis. Kesepakatan arah lemah/kuat 76,9% pada penilaian yang memenuhi syarat; hasil ini bukan akurasi seluruh diagnosis rasa. Kesukaan rata-rata dalam kotak 5,812 dan di luar 5,854, dengan interval selisih memuat nol. Kotak teknis tidak terbukti menjamin kesukaan.

**Sumber lokal:** `skripsi/bab2.tex`, Rasio, TDS, EY dan Bagan Kendali; `skripsi/bab3.tex`, Sistem Pakar; `app/results/external/E4_expert_validation.json`; `skripsi/bab4.tex`, Hasil Sistem Pakar.

<!-- PAGEBREAK -->

## 14 · Asisten: BM25, RAG, model lokal, dan alat

**LLM** adalah model bahasa yang menghasilkan teks dari pola yang dipelajari. Takar menjalankan Gemma 4 lokal melalui Ollama. Kata “lokal” menjelaskan tempat inferensi; itu tidak otomatis menjamin seluruh pengelolaan server dan log aman.

**BM25** memberi peringkat dokumen berdasarkan kecocokan istilah, kelangkaan kata, frekuensi dan panjang dokumen. Ia mencari potongan resep/SOP, bukan menghitung takaran baru. **RAG** berarti potongan relevan diberikan sebagai konteks ketika model menyusun jawaban. Setiap potongan mempunyai pengenal dan tautan sumber.

### Alur pipeline yang perlu dipahami

1. Sistem memeriksa cakupan pertanyaan; pertanyaan di luar domain dapat ditolak sebelum model.
2. Bila maksud, menu dan parameter cukup jelas, **router deterministik** memilih alat aplikasi.
3. Alat baca-saja menjalankan kalkulator, diagnosis, stok atau pasangan menu dan mengembalikan hasil.
4. Pertanyaan lain memakai hasil pencarian sebagai konteks bagi model.
5. Jika model tidak tersedia atau penjaga menolak keluaran, sistem menampilkan potongan pencarian dengan penanda mode.

**Ilustrasi:** “Berapa air V60 untuk 20 g?” lebih tepat diarahkan ke layanan kalkulator daripada meminta model mengarang angka. “Bagaimana langkah blooming?” dapat dijawab dari SOP dengan sumber. Jika pertanyaan perhitungan belum menyebut resep atau ukuran yang diperlukan, sistem perlu meminta rincian.

### Empat kondisi evaluasi

**Pencarian saja** menampilkan sumber; **closed-book** memakai model tanpa konteks; **RAG** menambahkan sumber; **RAG + alat** menambahkan layanan aplikasi dan routing. Ada tujuh varian karena tiga kondisi bermodel diuji pada E4B dan E2B, sedangkan BM25 tidak memerlukan model.

**Angka tanpa dasar** berarti angka dalam jawaban tidak didukung pertanyaan, potongan yang benar-benar diberikan, atau keluaran alat menurut penilai. Tingkatnya adalah jumlah angka tanpa dukungan dibagi seluruh angka jawaban. Nol tidak memastikan seluruh kalimat benar: prosedur tetap dapat salah walau angka yang disebut bersumber.

Keberhasilan alat berasal dari fungsi aplikasi, bukan bukti model bahasa berhitung sendiri. Penolakan oleh aturan juga bukan kemampuan penolakan model yang harus diatribusikan kepadanya.

**Sumber lokal:** `skripsi/bab2.tex`, LLM dan RAG; `skripsi/bab3.tex`, Perancangan Asisten; `app/results/assistant_eval.json`, `scoring_note` dan `summary`.

<!-- PAGEBREAK -->

## 15 · Dataset: mana fiktif, mana nyata, dan apa batasnya?

| Sumber | Sifat dan jumlah | Peran |
|---|---|---|
| IBM | Sampel fiktif; 49.894 baris | Mengembangkan pasangan menu |
| Maven | Sampel fiktif; 149.116 baris | Memilih peramal dan simulasi stok |
| Bread Basket | Transaksi nyata; 21.293 baris mentah | E1, pemeriksaan pasangan menu |
| ihelon | Transaksi nyata; 3.636 cangkir | E2–E3, prakiraan dan replay stok |

Sumber lain adalah eksperimen seduh konsumen UC Davis/Cotter dengan 3.186 penilaian awal, tabel 27 resep eksperimen Batali untuk sistem pakar, dan menu Starbucks untuk pola shot. Data menu merupakan catatan komposisi publik, bukan hasil uji rasa atau stok kedai mitra.

**Mengapa data fiktif digunakan?** Katalog dan struknya memungkinkan pengembangan alur aplikasi serta eksperimen yang bisa diulang. Kegunaan itu tidak mengubah sifat fiktifnya. Pemeriksaan eksternal diperlukan agar hasil tidak hanya bergantung pada pola buatan.

Bread Basket berasal dari satu toko roti-kafe Edinburgh dan lisensi unggahan awalnya tidak jelas menurut audit lokal. ihelon berasal dari satu mesin penjual kopi; perilakunya dapat berbeda dari barista dan kedai Indonesia. UC Davis mempunyai konteks peserta dan eksperimennya sendiri. Hasil eksternal memperluas pemeriksaan, tetapi belum mewakili seluruh kedai.

### Pemetaan produk adalah asumsi penting

Nama latte dari dataset dipetakan ke resep aplikasi agar penjualan dapat menjadi kebutuhan susu dan biji. Ini tidak membuktikan resep penerbit dataset persis sama. Produk roti atau kemasan yang tidak mempunyai resep tidak dipaksa menjadi bahan minuman. Produk proksi dan ukuran harus dinyatakan agar pengguna tidak menganggapnya data asli.

### Cara menjelaskan reprodusibilitas

Data mentah dan olahan dipisahkan. DATASHEET mencatat sumber, sifat, lisensi dan batas. Hasil eksperimen menyimpan parameter, waktu, seed bila relevan, dan hash masukan. **Hash** adalah sidik berkas untuk mendeteksi perubahan; **seed** membantu mengulang proses acak. Ini mendukung penelusuran hasil, bukan menghapus semua keterbatasan data.

Untuk Maven, tidak tersedia nomor struk asli; keranjang dari toko, tanggal dan waktu yang sama bersifat heuristik dan hanya analisis sekunder. Jangan menyebutnya struk nyata yang teridentifikasi pasti.

**Sumber lokal:** `skripsi/bab3.tex`, Dataset, tabel `tab:dataset` dan `tab:pemetaan-produk`; `skripsi/bab1.tex`, Ruang Lingkup; `dataset/raw/*/DATASHEET.md`; `dataset/processed/README.md`.

<!-- PAGEBREAK -->

## 16 · Bab 4: hasil H1 dan H2 harus dibaca bersama batasnya

### H1 — takaran berbasis batasan

Grid berisi 525 pesanan efektif pada 12 resep, termasuk tambahan sampai tiga shot. Subset batas awal sampai dua shot berisi 435 pesanan; jangan mencampur denominator keduanya.

| Pemeriksaan, 525 pesanan | Berbasis batasan | Linier dibulatkan | Linier mentah |
|---|---|---|---|
| Shot pecahan | 0 | 0 | 240 |
| Luapan >5% | 0 | 282 | 267 |
| Penyimpangan rasio >0,2 | 0 | 0 | 0 |
| Peringatan kurang isi | 144 | 0 | 0 |

**Keputusan:** H1 didukung pada grid yang diuji. Akan tetapi, rasio nol pada ketiga metode tidak menunjukkan keunggulan khusus metode usulan untuk aspek itu. Shot utuh dan total batch konsisten sebagian dijamin bentuk algoritma, disebut **by construction**. Nilai nol bukan hasil pengukuran rasa atau penerimaan barista.

144 peringatan kurang isi berarti mencegah luapan belum cukup. Kombinasi tertentu dapat menyisakan bahan pengisi terlalu sedikit; keputusan menolak pesanan atau mengubah standar perlu divalidasi operasional.

Pada pemeriksaan Starbucks, aturan diskret menghasilkan shot utuh, tetapi kecocokan tepat dengan menu hanya 58,3%. Pengecualian ukuran mencapai 100% karena diisi dari menu yang sama. Itu kemampuan merepresentasikan tabel, bukan kemampuan memprediksi tabel baru.

### H2 — rekomendasi pasangan menu

Pada **IBM fiktif**, HR@5 FP-Growth 0,4941 dan popularitas 0,1324; selisih 0,3617 dengan IK 95% [0,3402; 0,3839]. H2 didukung di data pengembangan itu, tetapi ko-okurensi lebih tinggi, yaitu 0,5134.

Pada **Bread Basket nyata**, HR@5 FP-Growth 0,5718, popularitas 0,5658 dan ko-okurensi 0,6021. Selisih FP-Growth − popularitas **0,0060**, dengan IK [−0,0028; 0,0147] yang melintasi nol. **H2 tidak didukung pada pemeriksaan nyata.** MRR@5 FP-Growth 0,3768 juga di bawah popularitas 0,3871.

**Jawaban sidang:** “Metode tidak selalu unggul. Data pengembangan menunjukkan manfaat dibanding popularitas, tetapi data nyata belum menunjukkan keunggulan meyakinkan. Saringan lift dan pembanding sederhana perlu diperiksa kembali pada kedai tujuan.”

**Sumber lokal:** `skripsi/bab4.tex`, tabel `tab:hasil-penskalaan` dan `tab:hasil-pasangan`; `app/results/scaling_eval.json`; `app/results/pairing_eval.json`; `app/results/external/E1_pairing_breadbasket.json`; `E5_scaling_starbucks.json`.

<!-- PAGEBREAK -->

## 17 · H3 dan H4: peramal terbaik berbeda dari kebijakan stok yang baik

### H3 — peramalan permintaan

Pada **Maven fiktif**, gradient boosting global mempunyai WAPE terendah **0,3964**, dibanding seasonal naive **0,5381**. Maven membentuk 240 deret produk–outlet; delapan origin × tujuh hari × 240 menghasilkan 13.440 titik per metode. Model tersebut dipilih sebelum pemeriksaan ihelon.

Pada **ihelon nyata per minuman**, WAPE model terpilih **0,6582** dibanding **0,7125**. Estimasi titik lebih kecil, tetapi IK selisih −0,0542 adalah [−0,1145; 0,0159], masih memuat nol. Pada **total harian yang diramal langsung**, model terpilih justru lebih buruk: **0,3862** dibanding **0,2646**, dengan IK selisih seluruhnya di atas nol.

**Keputusan yang dilaporkan:** H3 tidak didukung pada validasi nyata. Hasil eksploratif Holt-Winters tidak mengganti keputusan, karena pemilihannya terjadi setelah jendela uji dilihat. Hasil total dan per minuman berbeda tugas, sehingga jangan hanya memilih angka yang menguntungkan.

### H4 — simulasi restock

Replay ihelon 56 hari diubah menjadi permintaan **tiga bahan demo melalui BOM asumtif**. Rata-rata fill rate per bahan:

| Kebijakan pada ihelon | Fill rate | Hari stockout total |
|---|---|---|
| Sasaran dengan model terpilih | 0,9605 | 17 |
| ROP statis | 0,7900 | 47 |
| Sasaran dengan rata-rata 7 hari | 0,9871 | 9 |
| Sasaran dengan seasonal naive | 0,9671 | 8 |

**H4 didukung untuk pembanding utama**, dengan selisih sekitar 0,1706. Namun, struktur sasaran statis dengan cara pemesanan yang sama sudah mencapai 0,8633. Sebagian manfaat datang dari struktur kebijakan, bukan semata model machine learning. Rata-rata tujuh hari dan seasonal naive bahkan lebih baik dalam replay ini.

Hari stockout dijumlahkan lintas bahan; 47 tidak berarti tepat 47 tanggal berbeda. Fill rate yang dilaporkan adalah rata-rata per bahan, bukan volume semua bahan dengan satuan berbeda yang dijumlahkan. Hasil satu replay belum mempunyai estimasi ketidakpastian H4, dan tidak membuktikan penghematan biaya atau bahan basi.

**Sumber lokal:** `skripsi/bab4.tex`, Hasil Peramalan dan Restock; `app/results/forecast_eval.json`; `app/results/external/E2_forecast_ihelon.json`, `h3`; `E3_restock_ihelon.json`, `h4` dan `summary`.

<!-- PAGEBREAK -->

## 18 · H5: 95% milik pipeline yang diuji, bukan model sendirian

Tolok ukur internal berisi **60 pertanyaan**: 14 fakta resep, 12 prosedur, 10 perhitungan, 8 diagnosis, 6 stok dan 10 di luar cakupan. Tujuh varian menghasilkan 420 jawaban. Empat kondisi berikut memperlihatkan hasil model utama E4B.

| Kondisi E4B | Akurasi isi | Latensi median | Makna |
|---|---|---|---|
| BM25 saja | 55,0% | 0,027 detik | Pencarian dan gerbang cakupan |
| Tanpa konteks | 15,0% | 8,123 detik | Model tanpa sumber aplikasi |
| RAG | 55,0% | 1,721 detik | Sumber ditambahkan |
| RAG + alat | 95,0% | 0,175 detik | Pipeline lengkap |

95,0% berarti **57 dari 60 jawaban** benar menurut penilai internal. Tiga yang salah semuanya terkait prosedur/SOP. Pada E2B, kondisi lengkap mencapai 93,3%, tetapi model utama untuk H5 tetap E4B.

### Dari mana jawaban kondisi lengkap berasal?

- **24 jawaban alat** berasal dari router dan layanan perhitungan, diagnosis atau stok.
- **10 penolakan luar cakupan** berasal dari gerbang aturan sebelum model.
- **26 jawaban model** meliputi fakta dan SOP; 23 benar, yaitu 88,5% pada subset itu.

Median pipeline cepat karena 34 jawaban melewati model. Median **mode model saja 1,679 detik**, sehingga jangan menyebut Gemma selalu menjawab dalam 0,175 detik.

Angka tanpa dasar pada E4B tanpa konteks **466/542 = 85,98%**, sedangkan kondisi lengkap **0/263 = 0%** menurut pemeriksaan versi 2.1. Dua syarat H5 terpenuhi secara deskriptif: akurasi lebih tinggi dan angka tanpa dasar lebih rendah. Metrik tersebut menghitung angka, bukan persentase jawaban yang seluruh isinya mengada-ada.

### Batas terpenting

Pertanyaan disusun dengan bantuan AI dan diperiksa secara mesin, belum ditinjau manual oleh peneliti atau barista praktik. Kegagalan awal pada pertanyaan yang sama dipakai untuk memperbaiki router; kemudian 120 jawaban kondisi lengkap dijalankan ulang dan digabung dengan 300 jawaban kondisi lain, setelah hash diperiksa. Ini **uji regresi internal yang telah memengaruhi pengembangan**, belum himpunan uji independen.

**Kalimat sidang:** “H5 didukung pada pipeline dan benchmark internal ini. Saya belum mengklaim akurasi 95% pada pertanyaan baru atau sebagai kemampuan Gemma sendiri.”

**Sumber lokal:** `skripsi/bab4.tex`, tabel `tab:hasil-asisten`, `tab:hasil-asisten-kategori` dan batas interpretasi; `app/results/assistant_eval.json`.

<!-- PAGEBREAK -->

## 19 · Pengujian, UAT, dan Bab 5: apa yang boleh disimpulkan?

**Black-box** memeriksa masukan dan keluaran tanpa menjadikan struktur kode sebagai jawaban. **Equivalence partitioning** memilih perwakilan kelas masukan, misalnya sah/tidak sah. **Boundary value analysis** memeriksa sekitar batas, misalnya tambahan shot 0 dan 3 serta nilai di luar batas. **E2E** menjalankan alur lengkap melalui antarmuka.

Artefak akhir mencatat **706 pengujian backend dan 29 kasus antarmuka otomatis lulus**. Cakupannya meliputi login, peran, resep, kalkulator, produksi, stok, SOP, timer, AI, asisten, animasi dan tampilan ponsel. Angka tersebut menyatakan hasil suite yang tersimpan, bukan bahwa semua kemungkinan kesalahan sudah hilang.

Pengukuran API menggunakan 20 permintaan pemanasan dan 200 permintaan berurutan per endpoint pada komputer pengembangan. Kalkulator memiliki p50/p95 **7,393/8,669 ms**, sedangkan restock **137,741/159,285 ms**. **p50** adalah median; **p95** berarti sekitar 95% pengamatan berada pada atau di bawah nilai itu. Permintaan tidak dilakukan dengan beban pengguna serentak, sehingga bukan bukti kapasitas produksi kedai.

Audit Lighthouse tiga kali pada halaman masuk mempunyai median kinerja desktop 1,00 dan ponsel 0,97. Audit halaman publik tersebut tidak mewakili semua halaman setelah login.

### UAT dan SUS masih pekerjaan lanjutan

**UAT** memeriksa apakah pengguna yang dituju dapat menerima sistem dalam kegiatan kerja. **SUS** adalah kuesioner kegunaan subjektif 10 butir dengan skor 0–100; skor ini bukan persentase tugas berhasil. Pada rumus SUS, butir positif memakai jawaban dikurangi satu, butir negatif memakai lima dikurangi jawaban, lalu jumlah dikalikan 2,5.

Instrumen telah disiapkan, tetapi belum ada sesi, peserta, skor atau tingkat keberhasilan tugas. Karena itu, RM4 **baru terjawab sebagian** melalui fungsi dan kinerja lokal.

**Bab 5 menyimpulkan sesuai bukti:** integrasi sistem tercapai; H1 didukung pada grid; H2/H3 tidak didukung pada data nyata; H4 didukung pada simulasi terbatas; H5 didukung sebagai regresi internal. Pengurangan variasi rasa, waktu pelatihan, limbah dan peningkatan keuntungan **belum terbukti**.

Saran utamanya: validasi resep dan pasokan kedai, data transaksi baru, benchmark asisten independen, UAT, serta penilaian biaya dan umur simpan stok.

**Sumber lokal:** `skripsi/bab4.tex`, Hasil Fungsional, Kinerja dan UAT; `skripsi/bab5.tex`; `app/results/tests`; `api_latency.json`; `lighthouse/summary.json`.

<!-- PAGEBREAK -->

## 20 · Demo sidang dan rencana belajar

### Alur demo sekitar 4–5 menit

1. **Resep, 30 detik:** masuk menggunakan akun demo; tunjukkan resep dasar, komposisi dan sumber. Jelaskan tiga peran.
2. **V60, 45 detik:** ganti dosis 15 g menjadi 20 g. Tunjukkan air 225 → 300 ml dan target kumulatif 60, 173,3, 300 ml.
3. **Latte, 45 detik:** tambah shot. Tunjukkan shot utuh dan penyesuaian bahan pengisi; lihat perbandingan linier dan peringatan bila muncul.
4. **Produksi dan stok, 45 detik:** lihat pratinjau, catat produksi satu kali, lalu tunjukkan pergerakan bahan. Gunakan basis data demo yang boleh berubah.
5. **Panduan, 30 detik:** buka langkah, timer dan animasi; jelaskan animasi membantu membaca tindakan, manfaat belajar belum diukur.
6. **Asisten dan AI, 60 detik:** tanya air V60 untuk 20 g dan lihat mode alat serta sumber. Buka pasangan dan restock sambil menyebut batas data dan simulasi.

Demo boleh dipersingkat saat waktu terbatas. Prioritaskan alur resep → kalkulator → produksi → stok karena itulah benang merah penelitian.

### Siapkan sebelum masuk ruang sidang

Pastikan aplikasi dan basis data demo sudah berjalan. Siapkan PDF skripsi, panduan ini, dan tangkapan layar hasil utama. Periksa angka yang akan didemokan, sumber jawaban dan peran akun. Layanan model lokal perlu diuji sebelum presentasi. Bila model tidak tersedia, jelaskan mode pencarian dari antarmuka dan gunakan tangkapan layar untuk menunjukkan hasil uji yang tersimpan.

### Rencana belajar tujuh sesi

- **Sesi 1:** halaman 2–4; ceritakan masalah dan RM tanpa melihat catatan.
- **Sesi 2:** halaman 5–7; hitung V60, kapasitas dan BOM dengan tangan.
- **Sesi 3:** halaman 8–11; hitung support, HR, MRR dan WAPE.
- **Sesi 4:** halaman 12–15; jelaskan restock, EY, RAG dan data.
- **Sesi 5:** halaman 16–19; hafalkan hasil bersama batasnya.
- **Sesi 6:** demo dan 30 tanya-jawab; minta teman memberi pertanyaan lanjutan.
- **Sesi 7:** rekam presentasi 7–10 menit, perbaiki bagian yang masih hanya dihafal.

Gunakan pola jawaban **inti → contoh → bukti → batas**. Jika lupa angka rinci, sebutkan arah hasil dengan benar dan buka tabel; jangan membuat angka baru.

**Sumber lokal:** alur `skripsi/bab3.tex` dan implementasi `bab4.tex`; rencana belajar serta durasi demo adalah saran persiapan, bukan hasil penelitian.

<!-- PAGEBREAK -->

## 21 · Latihan sidang 1–10: masalah dan sistem

**1. Apa penelitian Anda dalam satu kalimat?**

Saya membangun Takar untuk menghubungkan resep, takaran variasi pesanan, SOP dan stok, lalu menguji fungsi serta modul keputusan. **Lanjutan:** kalau diminta contoh, ceritakan latte yang dicatat sebagai produksi lalu memotong susu dan biji melalui BOM.

**2. Mengapa masalah ini penting?**

Arahan penelitian menyoroti takaran antarbarista, bantuan latihan staf baru, dan stok yang terpisah. **Lanjutan:** manfaat langsung pada pelanggan belum saya ukur di kedai; implementasi baru mendukung proses standardisasi.

**3. Apa kebaruan penelitian ini?**

Kontribusinya integrasi komponen di sekitar resep standar dan evaluasi dengan pembanding serta pemeriksaan eksternal. **Lanjutan:** saya tidak mengklaim menemukan FP-Growth, gradient boosting atau RAG.

**4. Mengapa FastAPI dan Vue, bukan Laravel/PWA?**

Naskah mendokumentasikan keputusan perubahan 30 September 2026 agar pengolahan data dan AI berada bersama layanan Python. **Lanjutan:** akses responsif tetap tersedia; operasi luring dan PWA tidak termasuk implementasi.

**5. Mengapa memilih SQLite?**

Implementasi dibatasi pada satu outlet dan server lokal dengan basis data satu berkas. **Lanjutan:** hasil ini belum membuktikan kelayakan untuk banyak outlet atau banyak pengguna serentak; kebutuhan tersebut perlu evaluasi lain.

**6. Apakah semua barista bisa mengubah stok dan resep?**

Tidak semua tindakan sama. Barista mencatat produksi; kepala barista/manajer memiliki hak pengelolaan tertentu, dan manajer mengelola pengguna/model. **Lanjutan:** hak diperiksa kembali pada API.

**7. Apa hubungan resep dengan inventaris?**

Resep menjadi BOM; produksi diuraikan menjadi pemakaian bahan dasar. **Lanjutan:** subresep espreso diuraikan lagi menjadi biji sebelum stok dipotong.

**8. Apakah memakai kalkulator langsung mengurangi stok?**

Kalkulator hanya pratinjau. Stok berubah ketika produksi dicatat. **Lanjutan:** pengenal permintaan mencegah pengiriman ulang mengurangi stok dua kali.

**9. Apa arti atomik dan idempoten?**

Atomik menjaga log produksi dan pergerakan stok selesai bersama. Idempoten menjaga permintaan sama tidak berefek berulang. **Lanjutan:** jelaskan contoh klik ulang akibat jaringan lambat.

**10. Mengapa Scrum disebut disesuaikan?**

Penelitian dikerjakan satu mahasiswa, sehingga pekerjaan bertahap mengikuti prinsip backlog, iterasi dan evaluasi tanpa mengklaim seluruh struktur tim Scrum penuh. **Lanjutan:** jelaskan keluaran tiap tahap, jangan mengarang rapat tim yang tidak terjadi.

**Sumber lokal:** `skripsi/bab1.tex`, Latar Belakang, Ruang Lingkup dan Metode; `bab2.tex`, Penelitian Terkait; `bab3.tex`, Kebutuhan dan Perancangan; `bab4.tex`, Implementasi.

<!-- PAGEBREAK -->

## 22 · Latihan sidang 11–20: algoritma dan evaluasi

**11. Mengapa tidak memakai penskalaan linier saja?**

Shot harus utuh, cangkir terbatas, dan air harus mengikuti dosis final. **Lanjutan:** tambahan shot mengambil ruang sehingga susu pengisi perlu berkurang.

**12. Bagaimana V60 15 g diubah menjadi 20 g?**

Faktor 20/15. Air 300 ml dan target kumulatif 60, 173,3 dan 300 ml. **Lanjutan:** target kumulatif tidak dijumlahkan sebagai tiga tambahan air terpisah.

**13. Apa arti by construction pada H1?**

Sebagian sifat, seperti shot utuh, dijamin oleh bentuk algoritma. **Lanjutan:** nilai nol menunjukkan konsistensi aturan pada grid, belum membuktikan rasa atau kelayakan seluruh pesanan.

**14. Mengapa masih ada 144 peringatan kurang isi?**

Pengisian dapat terlalu sedikit setelah ruang diambil komponen lain. Itu di luar tiga kriteria utama H1. **Lanjutan:** aturan menolak atau mengubah pesanan perlu dibahas dan diuji bersama barista.

**15. Apa support, confidence dan lift?**

Support adalah proporsi pasangan; confidence peluang pasangan ketika item awal ada; lift membandingkannya dengan popularitas umum pasangan. **Lanjutan:** pada ilustrasi halaman 8, nilainya 0,20; 0,50; 1,67.

**16. Apakah latte menyebabkan orang membeli croissant?**

Aturan asosiasi hanya menunjukkan kemunculan bersama. **Lanjutan:** sebab-akibat dan dampak penawaran paket memerlukan rancangan evaluasi berbeda.

**17. Apa HR@5 dan MRR@5?**

HR menilai item tersembunyi masuk lima besar; MRR memberi nilai lebih tinggi bila peringkatnya lebih atas. **Lanjutan:** item peringkat dua memberi 1/2 pada MRR, tanpa hit memberi nol.

**18. Mengapa bootstrap berdasarkan keranjang?**

Kueri dalam satu keranjang saling berkaitan, sehingga keranjang diambil ulang sebagai unit. **Lanjutan:** selisih dihitung pada sampel sama untuk setiap metode agar perbandingan berpasangan.

**19. Mengapa model yang rumit kalah dari metode sederhana?**

Pola data, volume, konteks dan saringan dapat berbeda. Pada Bread Basket ko-okurensi lebih tinggi. **Lanjutan:** kompleksitas bukan kriteria menang; nilai uji dan batasnya yang menentukan.

**20. Bagaimana menghindari kebocoran data peramalan?**

Pada rolling origin hanya data sampai origin boleh digunakan. Model dipilih pada Maven sebelum ihelon dinilai. **Lanjutan:** jangan memakai hari masa depan dalam rata-rata fitur atau memilih pemenang setelah melihat uji lalu mengklaim evaluasi independen.

**Sumber lokal:** `skripsi/bab2.tex`, Penskalaan, Aturan Asosiasi, Evaluasi dan Peramalan; `bab3.tex`, Rancangan Eksperimen; `bab4.tex`, Hasil Penskalaan dan Pasangan Menu.

<!-- PAGEBREAK -->

## 23 · Latihan sidang 21–30: hasil dan keterbatasan

**21. Apakah H2 berhasil?**

Didukung pada IBM fiktif; tidak didukung pada Bread Basket nyata karena IK selisih HR@5 melintasi nol. **Lanjutan:** angka 0,5718 versus 0,5658 saja belum cukup menyebut keunggulan meyakinkan.

**22. Mengapa H3 tidak didukung?**

Per minuman ihelon, WAPE lebih kecil tetapi IK memuat nol; total harian model lebih buruk. **Lanjutan:** Holt-Winters yang dipilih sesudah uji hanya eksploratif.

**23. Jika H3 lemah, bagaimana H4 bisa didukung?**

Akurasi ramalan dan struktur keputusan stok adalah tugas berbeda. Sasaran dinamis mengungguli ROP statis pada replay. **Lanjutan:** moving average dengan struktur sama malah lebih baik daripada model terpilih.

**24. Apakah fill rate 0,9605 berarti keuntungan naik?**

Itu pemenuhan permintaan dalam simulasi, bukan keuntungan. **Lanjutan:** biaya, bahan basi, ruang dan pasokan nyata belum dinilai; H4 hanya membandingkan skenario yang ditetapkan.

**25. Bedanya TDS dengan EY apa?**

TDS adalah kepekatan minuman; EY bagian kopi awal yang terekstraksi. **Lanjutan:** TDS 1,5%, minuman 200 g dan dosis 15 g memberi EY 20%.

**26. Apakah Golden Cup menjamin rasa disukai?**

Tidak. Data konsumen tidak menunjukkan kesukaan dalam kotak lebih tinggi secara meyakinkan. **Lanjutan:** aturan merupakan bantuan teknis dengan alasan, bukan penentu tunggal preferensi.

**27. Apakah Gemma sendiri akurat 95%?**

95% adalah pipeline internal: 24 jawaban alat, 10 penolakan aturan, 26 jawaban model. **Lanjutan:** model benar 23/26 pada subset yang diarahkan kepadanya; subset itu tidak setara dengan seluruh 60 pertanyaan.

**28. Apakah nol angka tanpa dasar berarti nol halusinasi?**

Tidak seluruhnya. Penilai hanya memeriksa dukungan angka menurut definisinya. **Lanjutan:** tiga jawaban prosedur E4B tetap salah, dan benchmark belum diaudit barista.

**29. Apa keterbatasan terbesar dan prioritas berikutnya?**

Belum ada UAT, data mitra, dan benchmark independen; BOM/pasokan demo asumtif. **Lanjutan:** mulai dari resep dan pasokan aktual, lalu data transaksi baru, audit asisten dan pengujian tugas pengguna.

**30. Apakah aplikasi terbukti mempersingkat pelatihan dan mengurangi limbah?**

Belum. Fitur mendukung tujuan tersebut tetapi bukti lapangan belum dikumpulkan. **Lanjutan:** ukur waktu dan kesalahan tugas, pemakaian bahan serta penilaian pengguna dengan rancangan yang jelas.

**Sumber lokal:** `skripsi/bab4.tex`, hasil H2–H5, Sistem Pakar dan UAT; `bab5.tex`, Simpulan/Saran; `app/results/external/E1–E4*.json`; `assistant_eval.json`.

<!-- PAGEBREAK -->

## 24 · Naskah presentasi 7–10 menit, bagian pertama

**Petunjuk:** baca dengan tempo wajar, beri jeda pada tabel, dan sisipkan demo singkat. Estimasi total 7–10 menit mencakup kedua halaman, perpindahan slide, dan demo sekitar satu menit. Sesuaikan dengan aturan waktu penguji.

### 0:00–1:15 · Pembukaan dan masalah

“Selamat pagi/siang Bapak dan Ibu penguji. Penelitian saya membahas Takar, aplikasi web manajemen resep dan standardisasi operasional kedai kopi dengan dukungan keputusan berbasis AI.

Masalah yang menjadi titik awal adalah takaran yang bisa berbeda antarbarista, staf baru yang memerlukan panduan, dan catatan bahan yang terpisah dari produksi. Ketika pelanggan mengubah ukuran, tingkat manis atau jumlah shot, takaran perlu dihitung ulang. Jika pencatatan pemakaian bahan juga terpisah, stok dapat tertinggal dari kondisi produksi.

Karena itu, saya memakai resep standar sebagai penghubung. Resep yang sama dipakai untuk membaca komposisi, menghitung variasi pesanan, menampilkan langkah, dan mengurangi bahan ketika produksi dicatat.”

### 1:15–2:15 · Tujuan dan bentuk sistem

“Penelitian memiliki empat rumusan masalah: integrasi resep, SOP dan inventaris; kalkulator yang memenuhi batas praktis; kinerja modul AI dan asisten; serta kelayakan fungsi, kinerja dan penerimaan pengguna.

Saya menggunakan pendekatan rancang bangun dan evaluasi komparatif. Prosesnya dimulai dari analisis kebutuhan, penyusunan basis resep, perancangan data dan API, implementasi bertahap, lalu pengujian dan perbaikan. Unit evaluasi disesuaikan dengan keputusan: satu pesanan untuk kalkulator, satu kueri keranjang untuk pasangan, satu produk dan hari untuk ramalan, serta satu pertanyaan untuk asisten. Pemisahan itu membantu menghindari perbandingan metrik yang sebenarnya berbeda tugas.

Takar memakai Vue.js untuk antarmuka, FastAPI untuk layanan dan SQLite untuk data. Tiga peran adalah barista, kepala barista dan manajer. Peran diperiksa kembali pada server. Cakupan implementasi satu outlet dan server lokal; aplikasi belum terhubung dengan kasir atau menyediakan mode luring.

Kontribusi utama saya adalah integrasi dan evaluasi komponen tersebut. Saya tidak mengklaim menemukan FP-Growth atau metode peramalan yang digunakan.”

### 2:15–3:30 · Kalkulator dan demo singkat

“Penskalaan biasa mengalikan seluruh bahan, tetapi bahan kopi mempunyai sifat berbeda. Shot harus utuh, air mengikuti rasio, dan susu pengisi mengikuti ruang cangkir. Algoritma menghitung komponen dasar dahulu, menyelesaikan rasio, memeriksa kapasitas, kemudian menghitung pengisi dan kebutuhan batch.

Pada V60, resep 15 gram dan 225 mililiter berarti rasio satu banding lima belas. Saat dosis menjadi 20 gram, air menjadi 300 mililiter. Target tuang kumulatif berubah menjadi 60, 173,3 dan 300 mililiter. Setelah produksi dicatat, resep diuraikan lewat BOM menjadi pemakaian bahan.”

**Tindakan demo:** tampilkan perubahan V60 dan, bila waktu cukup, buku besar produksi. Setelah sekitar satu menit, kembali ke tabel hasil.

**Sumber lokal:** `skripsi/bab1.tex`, Rumusan Masalah; `bab3.tex`, Sistem dan Algoritma; `bab4.tex`, Implementasi dan Pengujian Fungsional. Naskah ini adalah latihan penyampaian.

<!-- PAGEBREAK -->

## 25 · Naskah presentasi 7–10 menit, bagian kedua

### 3:30–5:00 · Evaluasi dan hasil utama

“Evaluasi dipisahkan menurut tugas. IBM dan Maven adalah data pengembangan fiktif. Bread Basket dan ihelon memberi pemeriksaan transaksi nyata; data seduhan konsumen dan eksperimen dipakai untuk sistem pakar. Sifat sumber tersebut saya nyatakan agar hasil tidak dianggap berasal dari kedai mitra.

Pada 525 pesanan, kalkulator berbasis batasan tidak menghasilkan shot pecahan, luapan di atas lima persen atau penyimpangan rasio di atas 0,2. Linier mentah menghasilkan 240 shot pecahan dan 267 luapan; linier dibulatkan masih menghasilkan 282 luapan. H1 didukung pada grid. Namun, masih ada 144 peringatan kurang isi, dan sebagian nilai nol dijamin oleh bentuk algoritma.

H2 didukung pada IBM fiktif, tetapi tidak didukung pada Bread Basket nyata karena interval selisih HR@5 melintasi nol. Ko-okurensi sederhana juga lebih tinggi. H3 tidak didukung pada ihelon: selisih per minuman belum meyakinkan, dan pada total harian model terpilih lebih buruk daripada seasonal naive.”

### 5:00–6:30 · Restock, sistem pakar, dan asisten

“Pada simulasi ihelon, H4 didukung untuk kebijakan yang ditetapkan: fill rate 0,9605 dibanding 0,7900 pada ROP statis. Akan tetapi, moving average dengan struktur kebijakan sama mencapai 0,9871. Jadi hasil mendukung kebijakan dinamis pada skenario ini, bukan superioritas model machine learning.

Sistem pakar menghitung TDS dan EY serta menunjukkan jejak aturan. Pemeriksaan mendukung ketepatan perhitungan dan sebagian arah diagnosis, tetapi kotak Golden Cup tidak terbukti menjamin kesukaan konsumen.

Pada asisten E4B, RAG dengan alat mencapai akurasi isi 95 persen dibanding 15 persen tanpa konteks. Angka tanpa dasar turun dari 85,98 persen menjadi nol menurut penilai. Hasil lengkap mencakup 24 jawaban alat, 10 penolakan aturan dan 26 jawaban model. Router diperbaiki memakai benchmark yang sama, sehingga angka tersebut merupakan regresi internal, belum generalisasi pada pertanyaan baru.”

### 6:30–8:00 · Kelayakan, batas, dan penutup

“Suite akhir mencatat 706 tes backend dan 29 kasus antarmuka lulus. Pengukuran API menunjukkan kinerja lokal, tetapi tidak menguji beban serentak. UAT bersama barista dan skor SUS belum tersedia, sehingga penerimaan pengguna serta manfaat pada rasa, waktu pelatihan, limbah dan keuntungan belum dapat disimpulkan.

Keterbatasan lain adalah pemetaan produk dataset ke resep aplikasi, ukuran kemasan, stok awal dan waktu tunggu pemasok yang masih berupa asumsi. Data nyata juga berasal dari konteks tertentu, seperti toko roti-kafe dan mesin penjual kopi. Karena itu, sebelum dipakai untuk keputusan kedai tujuan, resep dan parameter harus diukur kembali. Sistem pakar dan asisten perlu menunjukkan sumber supaya barista dapat memeriksa alasan saran serta mengetahui kapan informasi belum cukup.

Kesimpulan saya adalah integrasi sistem telah terwujud dan modulnya telah dinilai dengan pembanding. Sebagian hipotesis didukung dalam batas tertentu, sedangkan hasil negatif tetap dilaporkan. Langkah berikutnya adalah memvalidasi resep dan pasokan nyata, mengumpulkan transaksi kedai, menguji asisten pada pertanyaan independen, serta melaksanakan UAT. Terima kasih.”

**Sumber lokal:** `skripsi/bab4.tex`, Hasil dan Pembahasan; `bab5.tex`, Simpulan/Saran. Waktu adalah perkiraan latihan, bukan hasil evaluasi penelitian.
