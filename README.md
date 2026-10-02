# barista

Repositori skripsi **Takar**, aplikasi web manajemen resep dan standardisasi operasional kedai kopi dengan rekomendasi berbasis kecerdasan buatan menggunakan FastAPI dan Vue.js.

## Dockerfile ada di mana?

| Tujuan | Lokasi | Ketersediaan |
| --- | --- | --- |
| Mengompilasi skripsi LaTeX menjadi PDF | [skripsi/Dockerfile](skripsi/Dockerfile) | Ada di GitHub, dapat digunakan setelah clone |
| Menjalankan aplikasi web Takar | `app/backend/Dockerfile` | Ada pada workspace lengkap di `D:\barista\app\backend\Dockerfile` |
| Mengatur container dan data aplikasi | `app/compose.yaml` | Ada pada workspace lengkap |

Untuk menghasilkan PDF dari clone GitHub, ikuti [replikasi skripsi langkah demi langkah](#replikasi-skripsi-dengan-docker-langkah-demi-langkah). Untuk menjalankan aplikasi pada workspace lengkap, ikuti [langkah aplikasi](#replikasi-aplikasi-pada-workspace-lengkap).

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
| `skripsi/Dockerfile` | Lingkungan Linux beserta paket LaTeX untuk menghasilkan PDF |
| `skripsi/tools/build-docker.sh` | Perintah kompilasi yang dijalankan di dalam container |
| `skripsi/tools/build.ps1` | Helper Windows untuk menjalankan kompilasi lokal atau Docker |

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

## Replikasi skripsi dengan Docker: langkah demi langkah

Jalur ini menghasilkan `skripsi/build/Skripsi.pdf`. Docker memasang LaTeX di dalam image, sehingga komputer cukup mempunyai Git dan Docker Desktop. Jalankan seluruh blok berikut di **PowerShell yang sama**.

### 1. Pasang alat dan pastikan Docker siap

Pasang Git for Windows dan [Docker Desktop untuk Windows](https://docs.docker.com/desktop/setup/install/windows-install/). Buka Docker Desktop, ikuti pengaturan WSL 2, dan gunakan **Linux containers**.

```powershell
git --version
docker version
docker info --format '{{.OSType}}'
```

Hasil yang diharapkan: versi Git terlihat, `docker version` mempunyai bagian **Client** dan **Server**, serta perintah terakhir menghasilkan `linux`. Jika bagian Server gagal terhubung, tunggu Docker Desktop siap sebelum melanjutkan.

### 2. Ambil naskah dari GitHub

Untuk komputer baru, simpan proyek di folder `Projects` milik pengguna Windows:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\Projects" | Out-Null
Set-Location "$env:USERPROFILE\Projects"
git clone https://github.com/SeedFlora/barista.git
Set-Location .\barista
Test-Path .\skripsi\Dockerfile
```

Perintah terakhir harus menghasilkan `True`. Folder ini disebut **akar repositori**, yaitu folder yang berisi README ini dan folder `skripsi`.

Jika salinan proyek sudah ada di komputer ini, masuk langsung ke folder tersebut, misalnya `Set-Location D:\barista`. Lanjutkan dari langkah 3; clone cukup dilakukan sekali.

### 3. Bangun image kompilasi

Dari akar repositori:

```powershell
docker build --file .\skripsi\Dockerfile --tag barista-skripsi .\skripsi
```

`--file` menunjukkan lokasi Dockerfile, `--tag` memberi nama image, dan argumen terakhir menentukan folder sumber yang dikirim ke Docker. Folder `skripsi` sudah memuat gambar, template, dan referensi yang diperlukan. Penjelasan konsep folder sumber tersedia pada [dokumentasi build context Docker](https://docs.docker.com/build/concepts/context/).

Build pertama mengunduh image dan paket LaTeX sehingga memerlukan internet dan dapat berlangsung beberapa menit. Tunggu sampai perintah selesai tanpa error. Build berikutnya memakai cache paket.

### 4. Jalankan container dan simpan PDF ke komputer

```powershell
New-Item -ItemType Directory -Force .\skripsi\build | Out-Null
$skripsiOutputDir = (Resolve-Path .\skripsi\build).Path
docker run --rm --mount "type=bind,source=$skripsiOutputDir,target=/output" barista-skripsi
```

Container menjalankan pdfLaTeX dan BibTeX, lalu menyalin hasil ke folder output. Mount menghubungkan `/output` di container dengan `skripsi/build` di komputer; lihat [penjelasan bind mount Docker](https://docs.docker.com/engine/storage/bind-mounts/). Opsi `--rm` membersihkan container setelah selesai; PDF tersimpan di komputer.

Kompilasi memperbarui `skripsi/build/Skripsi.pdf` dan membuat `skripsi/build/compile-docker.log`. Jika gagal, baca pesan error pada terminal sebelum melanjutkan.

### 5. Periksa dan buka hasilnya

Perintah Docker harus selesai tanpa error dan menampilkan informasi PDF. Pada versi naskah yang diuji pada 2 Oktober 2026, hasilnya **148 halaman A4**.

```powershell
Get-Item .\skripsi\build\Skripsi.pdf | Select-Object Name, Length, LastWriteTime
Start-Process .\skripsi\build\Skripsi.pdf
```

Periksa sampul, daftar isi, gambar, tabel, sitasi, daftar pustaka, dan halaman akhir. Jumlah halaman dapat berubah ketika isi naskah diperbarui.

### 6. Melanjutkan penulisan dan kompilasi ulang

Isi identitas pada `skripsi/Awal_konfigurasi.tex`, lalu edit `bab1.tex` sampai `bab5.tex` sesuai kebutuhan. Sesudah menyimpan perubahan, ulangi langkah 3 dan 4. Image berisi salinan sumber pada saat build, sehingga perubahan `.tex` perlu diikuti build lagi.

Sebagai pengganti dua perintah manual tersebut, helper ini membangun image dan menjalankan kompilasi sekaligus dari akar repositori:

```powershell
powershell -ExecutionPolicy Bypass -File .\skripsi\tools\build.ps1 -Docker
```

Rincian toolchain, tanggal PDF yang dibekukan, dan jalur kompilasi Windows tanpa Docker tersedia di [README skripsi](skripsi/README.md).

### 7. Membuat ulang PDF panduan sidang

Panduan sidang dibuat dari `skripsi/panduan/README.md` memakai Python. Pasang Python terlebih dahulu, lalu jalankan dari akar repositori:

```powershell
python -m pip install -r .\skripsi\tools\requirements-panduan.txt
python .\skripsi\tools\build_panduan.py
```

Hasilnya berada di `output/pdf/Panduan_Sidang_Takar.pdf`. Perbarui sumber panduan jika hasil atau kesimpulan penelitian berubah.

### 8. Menyimpan perubahan ke GitHub

Gunakan akun GitHub yang mempunyai akses tulis. Git for Windows menyediakan Git Credential Manager untuk login HTTPS melalui browser dan menyimpan kredensial. Jika login belum tersedia di terminal, ikuti [panduan autentikasi GitHub](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git).

Sesudah memeriksa PDF, tinjau berkas yang akan dipublikasikan:

```powershell
git status --short
git add README.md .gitignore .gitattributes skripsi output/pdf/Panduan_Sidang_Takar.pdf
git diff --cached --stat
git commit -m "Perbarui skripsi dan panduan sidang"
git push origin main
```

### Jika replikasi skripsi mengalami masalah

| Gejala | Langkah perbaikan |
| --- | --- |
| `docker` tidak dikenali | Pasang Docker Desktop, lalu buka PowerShell kembali. |
| Tidak dapat terhubung ke Docker Engine | Buka Docker Desktop dan tunggu sampai Engine siap. |
| Dockerfile tidak ditemukan | Jalankan dari akar repositori dan periksa `Test-Path .\skripsi\Dockerfile`. |
| Build gagal saat mengunduh image atau paket | Periksa koneksi/proxy Docker Desktop, lalu ulangi langkah 3. |
| Sumber mount tidak ditemukan | Jalankan kembali `New-Item` dan `Resolve-Path` pada langkah 4 di PowerShell yang sama. |
| PDF belum berubah setelah mengedit `.tex` | Bangun image lagi pada langkah 3, lalu jalankan langkah 4. |
| Kompilasi gagal karena isi naskah | Baca error pada terminal; perbaiki baris `.tex` yang disebutkan lalu build ulang. |

## Replikasi aplikasi pada workspace lengkap

Dockerfile aplikasi berada di **`D:\barista\app\backend\Dockerfile`** dan Compose berada di **`D:\barista\app\compose.yaml`**. Siapkan salinan workspace yang memuat kode `app/` dan folder data `dataset/`. Publikasi GitHub ini memuat naskah; menjalankan aplikasi memerlukan salinan kode aplikasi tersebut.

Langkah aplikasi pada workspace lengkap:

1. Buka Docker Desktop dalam mode Linux containers.
2. Masuk ke folder `app`. Periksa `backend/Dockerfile`, `compose.yaml`, `../dataset/raw`, dan `results` tersedia.
3. Bangun dan jalankan container, lalu periksa kesehatan API:

```powershell
Set-Location D:\barista\app
Test-Path .\backend\Dockerfile
Test-Path .\compose.yaml
docker compose up --build -d --wait --wait-timeout 180
docker compose ps
Invoke-RestMethod http://127.0.0.1:8080/api/health
```

4. Jika API menampilkan `status: ok` dan `app: Takar`, buka **http://127.0.0.1:8080**. Akun demo manajer: `manager@takar.local`, kata sandi `takar123`.
5. Untuk melatih pasangan menu, prakiraan, dan restock, siapkan data IBM dan Maven sesuai `app/README.md`, lalu jalankan:

```powershell
docker compose exec -T backend python scripts/train_models.py
```

6. Untuk berhenti, jalankan `docker compose stop`. Untuk melanjutkan, jalankan `docker compose up -d --wait`. Setelah mengedit kode, jalankan `docker compose up --build -d --wait`.

README aplikasi pada **`D:\barista\app\README.md`** memuat langkah lengkap, nama berkas dataset, akun/peran, dan Ollama opsional. `app/DOCKER.md` memuat rincian backup, penyimpanan data, dan troubleshooting. Docker aplikasi memakai volume tersendiri untuk database dan mempertahankannya ketika container dibuat ulang.

## Sebelum penyerahan resmi

- Lengkapi identitas mahasiswa dan pembimbing di `skripsi/Awal_konfigurasi.tex`.
- Tinjau sumber, istilah, rumus, dan hasil pengujian bersama pembimbing.
- Nyatakan hasil negatif, asumsi simulasi, dan status UAT secara konsisten.
- Perjelas kriteria interval kepercayaan H3 pada Bab 1 dan Bab 3 agar sesuai dengan keputusan evaluasi di Bab 4.
- Periksa kembali format kampus, nomor halaman, dan kualitas cetak PDF.
