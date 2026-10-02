# barista

Repositori skripsi **Takar**, aplikasi web manajemen resep dan standardisasi operasional kedai kopi dengan rekomendasi berbasis kecerdasan buatan menggunakan FastAPI dan Vue.js.

## Mulai belajar dari nol

1. Baca [Panduan Sidang Takar](output/pdf/Panduan_Sidang_Takar.pdf). Satu PDF ini menjelaskan masalah penelitian, istilah penting, cara kerja sistem, contoh perhitungan, hasil, batasan, pertanyaan sidang, dan naskah presentasi.
2. Baca [skripsi lengkap](skripsi/build/Skripsi.pdf). Gunakan panduan untuk memahami, lalu cocokkan penjelasan dengan Bab 1 sampai Bab 5.
3. Pelajari Bab 1 untuk menjawab **mengapa penelitian diperlukan**, Bab 3 untuk **bagaimana penelitian dilakukan**, dan Bab 4 sampai Bab 5 untuk **apa hasilnya dan apa batasannya**.

Panduan merupakan bahan belajar berdasarkan skripsi yang ada. Contoh buatan diberi label ilustrasi. Identitas mahasiswa, NIM, dan pembimbing pada skripsi masih berupa placeholder; isi sebelum penyerahan resmi.

## Isi repositori

| Lokasi | Kegunaan |
| --- | --- |
| `skripsi/Skripsi.tex` | Berkas utama yang menggabungkan seluruh bagian skripsi |
| `skripsi/bab1.tex` sampai `bab5.tex` | Isi tiap bab |
| `skripsi/Awal_konfigurasi.tex` | Judul dan identitas penulis/pembimbing |
| `skripsi/ref.bib` | Daftar pustaka |
| `skripsi/pic/` | Gambar, diagram, dan hasil pengujian yang dipakai naskah |
| `skripsi/build/Skripsi.pdf` | PDF skripsi hasil kompilasi |
| `output/pdf/Panduan_Sidang_Takar.pdf` | PDF belajar dan persiapan sidang |
| `skripsi/panduan/` | Sumber panduan yang dapat diperbarui |
| `skripsi/README.md` | Petunjuk kompilasi LaTeX dan Docker |

Publikasi ini berisi sumber skripsi, PDF, gambar pendukung, dan dokumentasi pembuatannya. Folder `paper/`, kode aplikasi `app/`, dataset mentah, model, cache, dan backup tetap berada di workspace lokal. Aturan `.gitignore` membatasi berkas yang masuk GitHub.

Naskah dapat dikompilasi dari repositori ini. Untuk mengulang eksperimen aplikasi, diperlukan workspace penelitian lengkap beserta kode, data, dan konfigurasi pengujiannya.

## Memahami hasil sebelum sidang

| Bagian | Hasil yang perlu dijelaskan |
| --- | --- |
| Penskalaan resep (H1) | Pada 525 pesanan uji, metode berbasis batasan tidak menghasilkan shot pecahan, luapan di atas 5%, atau penyimpangan rasio di atas 0,2. Metode linier mentah menghasilkan 240 shot pecahan dan 267 luapan. |
| Pasangan menu (H2) | FP-Growth belum mengungguli popularitas secara meyakinkan pada Bread Basket nyata. |
| Peramalan (H3) | Keunggulan model terpilih atas seasonal naive belum didukung pada data minuman ihelon nyata. |
| Restock (H4) | Dalam simulasi, fill rate berbasis prakiraan 0,9605, dibandingkan 0,7900 untuk titik pesan ulang statis. Hasil ini berasal dari simulasi. |
| Asisten (H5) | Akurasi tolok ukur internal 95,0% untuk sistem lengkap, dibandingkan 15,0% tanpa konteks. Tolok ukur yang sama dipakai memperbaiki router, sehingga diperlukan uji independen. |
| Penerimaan pengguna | UAT belum dilakukan. Pengujian otomatis tidak menggantikan penerimaan pengguna nyata. |

IBM dan Maven adalah data sampel fiktif untuk pengembangan. Data eksternal nyata dipakai sebagai pemeriksaan tambahan sesuai protokol pada naskah. Baca rincian dan batas generalisasi di Bab 3, Bab 4, Bab 5, dan panduan sidang.

## Mengambil dan melanjutkan skripsi

Pasang Git, lalu jalankan di PowerShell:

```powershell
git clone https://github.com/SeedFlora/barista.git
Set-Location barista
```

Untuk kompilasi, ikuti [petunjuk LaTeX dan Docker](skripsi/README.md). Docker menyediakan lingkungan kompilasi; editor seperti VS Code tetap dapat dipakai untuk mengubah `.tex`.

Urutan kerja setelah mengubah naskah:

1. Ubah bagian yang sesuai pada `skripsi/`, lalu kompilasi ulang.
2. Buka PDF untuk memeriksa tata letak, gambar, tabel, rujukan, dan daftar pustaka.
3. Jika hasil atau kesimpulan berubah, perbarui panduan sidang agar angkanya tetap sesuai.
4. Periksa berkas yang akan dipublikasikan sebelum commit.

Sumber panduan ada di `skripsi/panduan/README.md`. Untuk membuat PDF panduan kembali dengan Python:

```powershell
python -m pip install -r .\skripsi\tools\requirements-panduan.txt
python .\skripsi\tools\build_panduan.py
```

```powershell
git status --short
git add README.md .gitignore .gitattributes skripsi output/pdf/Panduan_Sidang_Takar.pdf
git diff --cached --stat
git commit -m "Perbarui skripsi dan panduan sidang"
git push origin main
```

## Docker aplikasi pada workspace lengkap

Docker aplikasi dan petunjuk menjalankan dari nol disiapkan pada workspace lokal di `app/DOCKER.md`. Bagian aplikasi membutuhkan folder `app/` dan data lokal yang sesuai. Untuk melanjutkan aplikasi, buka workspace lengkap tersebut dan ikuti dokumentasinya.

## Sebelum penyerahan resmi

- Lengkapi identitas mahasiswa dan pembimbing di `skripsi/Awal_konfigurasi.tex`.
- Tinjau sumber, istilah, rumus, dan hasil pengujian bersama pembimbing.
- Nyatakan hasil negatif, asumsi simulasi, dan status UAT secara konsisten.
- Perjelas kriteria interval kepercayaan H3 pada Bab 1 dan Bab 3 agar sesuai dengan keputusan evaluasi di Bab 4.
- Periksa kembali format kampus, nomor halaman, dan kualitas cetak PDF.
