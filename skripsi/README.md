# Naskah skripsi Takar

Naskah membahas aplikasi web manajemen resep dan standardisasi operasional kedai kopi dengan FastAPI, Vue.js, dan modul rekomendasi. File utama adalah `Skripsi.tex`; hasil kompilasi tersedia di `build/Skripsi.pdf`.

Panduan belajar dari nol dan persiapan sidang tersedia di `../output/pdf/Panduan_Sidang_Takar.pdf`, dengan sumber teks `panduan/README.md`. Untuk membuat ulang panduan dari akar repository:

```powershell
python -m pip install reportlab
python .\skripsi\tools\build_panduan.py
```

Builder panduan memakai Python dan terpisah dari kompilasi LaTeX/Docker di bawah.

## Mulai dari nol

1. Baca PDF untuk melihat susunan lengkap, lalu pelajari `bab1.tex` sampai `bab5.tex` sesuai urutan. `abstrak.tex` merangkum penelitian, sedangkan `lampiran.tex` memuat rincian pengujian.
2. Ubah identitas pada `Awal_konfigurasi.tex` sebelum naskah diserahkan. Nama, NIM, email, pembimbing, dan NIK/NIDN masih berupa placeholder. Tanggal pengesahan masih memakai `\today`.
3. Edit isi bab, kompilasi ulang, lalu periksa gambar, tabel, daftar isi, sitasi, dan nomor halaman pada PDF. Jangan mengisi hasil penelitian tanpa pengujian.

`pic/` memuat gambar yang diperlukan naskah, termasuk salinan gambar hasil dan tangkapan layar dalam `pic/results/`. Kompilasi tidak memerlukan folder aplikasi maupun paper.

## Kompilasi Windows tanpa Docker

Pasang MiKTeX atau TeX Live, lalu jalankan dari akar repository pada PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\skripsi\tools\build.ps1
```

Helper menjalankan pdfLaTeX, BibTeX, dan dua pass tambahan. Perl tidak diperlukan. Jika distribusi TeX meminta paket tambahan, selesaikan instalasi paket tersebut sebelum menjalankan kembali. Alternatif jika `latexmk` beserta Perl tersedia:

```powershell
Set-Location .\skripsi
latexmk -pdf -halt-on-error -file-line-error Skripsi.tex
```

## Kompilasi dengan Docker

Pasang dan jalankan Docker Desktop dengan Linux containers, lalu gunakan PowerShell dari akar repository:

```powershell
powershell -ExecutionPolicy Bypass -File .\skripsi\tools\build.ps1 -Docker
```

Atau jalankan perintah manual:

```powershell
docker build -t barista-skripsi .\skripsi
$outputDir = (Resolve-Path .\skripsi\build).Path
docker run --rm --mount "type=bind,source=$outputDir,target=/output" barista-skripsi
```

Hasil disalin ke `skripsi/build/Skripsi.pdf`; log tersedia di folder yang sama. Hanya folder output yang di-mount, sehingga sumber dalam image tetap tersedia. Build pertama mengunduh paket LaTeX dan memerlukan internet serta ruang disk. Edit sumber harus diikuti `docker build` lagi; lapisan paket akan memakai cache.

Dockerfile mengunci image Debian melalui digest dan paket melalui snapshot Debian 1 September 2025. `SOURCE_DATE_EPOCH=1790899200` dan `FORCE_SOURCE_DATE=1` membekukan tanggal PDF ke 2 Oktober 2026 (UTC); ini juga memengaruhi `\today`. Ganti epoch secara sadar saat tanggal pengesahan perlu berubah. PDF dari MiKTeX/TeX Live yang berbeda dapat memiliki sedikit perbedaan tata letak; periksa hasil engine yang dipakai untuk penyerahan.

## Pemeriksaan sebelum sidang

- Ringkasan dan simpulan menyatakan hasil pengujian aktual. Model ramalan dan kebijakan restock mempunyai hasil negatif yang perlu dijelaskan, sehingga jangan menyebut semua modul AI unggul.
- Pengujian fungsi di naskah bukan bukti penerimaan pengguna. UAT/pengujian pengguna nyata belum dilakukan; jangan mengarang skor kepuasan atau penerimaan.
- Pemeriksa aturan sitasi tersedia: `python .\skripsi\tools\check_citations.py`. Script memeriksa pola sitasi dan daftar lokal; ini tidak memvalidasi kebenaran ilmiah seluruh sumber.
- Sebagian template menghasilkan warning paket lama, bahasa `apacite`, bookmark, dan `Underfull hbox`. Periksa log dan PDF; warning berbeda dari kegagalan kompilasi.

## Peta file

| File/folder | Fungsi |
| --- | --- |
| `Skripsi.tex` | Urutan dan konfigurasi dokumen utama |
| `Awal_konfigurasi.tex` | Judul, identitas, dan nama bab |
| `bab1.tex` - `bab5.tex` | Isi penelitian |
| `ref.bib` | Basis referensi BibTeX |
| `ta.sty`, `*.sty` | Format dan paket template lokal |
| `pic/` | Gambar dan diagram untuk kompilasi mandiri |
| `.latexmkrc` | Output `build/` dan lokasi BibTeX |
| `tools/build.ps1` | Build lokal atau Docker dari Windows |
| `Dockerfile` | Lingkungan kompilasi LaTeX |
