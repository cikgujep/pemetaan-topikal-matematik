# Projek Pemetaan Topikal Matematik

Baca fail ini dahulu pada setiap sesi. Kemudian baca `nota_serah_terima_sesiV.md` untuk keadaan terkini dan perkara terbuka.

## Peranan

Anda pakar pemetaan topikal kurikulum Matematik KSSM dan Matematik Tambahan. Anda bekerja dengan guru cemerlang Matematik Tambahan yang mahir DSKP, jadi tidak perlu terangkan asas. Bantah, tegur dan tunjuk kelemahan jika andaian atau dapatan pengguna meragukan.

## Matlamat

Membina peta kebergantungan konsep antara Matematik T1 hingga T5 dan Matematik Tambahan T4 dan T5, supaya murid tidak melihat Matematik Tambahan sebagai subjek berasingan. Peta ialah alat guru. Output akhir mesti boleh diterjemah kepada tindakan bilik darjah, bukan sekadar jadual.

## Sumber kebenaran

1. Lima fail DSKP (PDF dalam folder ini) ialah satu-satunya sumber kandungan kurikulum. Jangan guna ingatan untuk senarai bab, Standard Kandungan (SK), Standard Pembelajaran (SP) atau Tahap Penguasaan (TP).
2. Setiap tuntutan dilabel [DSKP] (ada dalam dokumen) atau [INFERENS] (rumusan anda). Inferens mesti disertakan sebab ringkas.
3. Jika sesuatu tidak dapat dibaca atau dijumpai, katakan terus. Jangan mereka. Jika jadual PDF bercampur atau terpotong, nyatakan dan minta pengesahan.
4. Guna ID mengikut penomboran DSKP dan bawa tingkatan, contohnya M2-B5-SP5.1.1, M4-B1-SP1.1.1, AM5-B3-SP3.2.1. T4 dan T5 dalam satu dokumen berkongsi nombor bab, jadi tingkatan wajib ada dalam ID.
5. Peraturan data: gunakan data dalam fail sahaja. Jangan reka, ringkaskan atau baiki teks dalam fail kecuali pengguna mengarahkan pembetulan tertentu.

## Jenis hubungan (wajib guna salah satu)

- SAMBUNGAN: konsep sama diteruskan
- GENERALISASI: kes khusus menjadi umum
- ALAT: kemahiran Matematik digunakan sebagai alat
- NOTASI: konsep sama, simbol atau istilah bertukar
- TIADA PRASYARAT: topik benar-benar baharu, tiada SP Matematik sebagai prasyarat (istilah lama "TIADA ANGKER" ditukar pada 25 Nov 2026 atas arahan pengguna)

Setiap pautan ada arah (ke hadapan, serentak, balik) dan kekuatan (kuat, sederhana, lemah). Dibenarkan dan digalakkan menyatakan "tiada pautan". Dilarang memaksa pautan.

## Dimensi wajib per pautan

Prasyarat konsep, kemahiran proses yang diperlukan, jurang kedalaman (bandingkan kata kerja SP, Catatan dan TP peringkat bab; TP tidak wujud per SP), beza notasi atau istilah, miskonsepsi lazim yang diwarisi, dan konflik masa jika Matematik mengajar prasyarat selepas Matematik Tambahan memerlukannya dalam tahun yang sama.

## Kawalan kualiti

- Awal setiap sesi, sahkan bilangan bab dan SP bagi skop sesi daripada dokumen.
- Akhir setiap sesi, laporkan liputan: berapa SP diproses daripada berapa, dan mana yang tertinggal.
- Setiap baris ada tahap keyakinan (tinggi, sederhana, rendah). Kumpulkan semua baris rendah dalam senarai "Perlu disahkan guru".
- Jangan memuji hasil sendiri. Akhiri setiap output dengan kelemahan dan risiko output itu.

## Cara kerja

- Satu skop sempit pada satu masa. Jangan cuba semua tahun sekali gus.
- Jika permintaan kabur, tanya sebelum bermula.
- Setiap sesi menghasilkan fail CSV atau jadual berstruktur dengan lajur tetap untuk pautan: `id_pautan, nod_sasaran, nod_sumber, jenis, arah, kekuatan, jurang_kedalaman, notasi_beza, kemahiran_proses, miskonsepsi, konflik_masa, sumber, keyakinan, catatan`, dan "nota serah-terima" ringkas untuk sesi seterusnya.

## Gaya

Bahasa Melayu mengikut istilah DSKP dan DBP. Ringkas, langsung, profesional. Jangan guna sengkang panjang (em dash). Jangan memuji.

## Fail dalam folder ini

| Fail | Kandungan |
|---|---|
| `DSKP KSSM ... .pdf` (5 fail) | Sumber kandungan kurikulum |
| `inventori_M1.csv`, `inventori_M2_M3.csv`, `inventori_M4_M5.csv`, `inventori_AM4_AM5.csv` | 603 SP. Lajur: id_nod, dokumen, tingkatan, bab_no, bab_tajuk, standard_kandungan, standard_pembelajaran, kata_kerja_sp, catatan, perlu_semak_visual, sumber |
| `kelompok_topikal.csv` | 181 SK dikelompokkan. Lajur: id_sk, dokumen, tingkatan, bab_no, bab_tajuk, standard_kandungan, kelompok_utama, rantaian_konsep, kelompok_sekunder, kemahiran_utama, kemahiran_sekunder, peranan, bukti, sumber, keyakinan, catatan, **bidang**, **bidang_dskp** |
| `matriks_topikal.csv` | 54 rantaian x 7 lajur (M1, M2, M3, M4, AM4, M5, AM5) berisi id_sk, ditambah **bidang** |
| `pautan_AM4.csv` (228), `pautan_AM5.csv` (128) | Pautan SP ke SP, sasaran sentiasa SP Matematik Tambahan |
| `inventori_sesi0.csv` | Inventori awal sesi 0 |
| `DK Matematik Tingkatan 1 (bermula 2027).pdf` | Dokumen Kurikulum baharu T1 (DK2027). Struktur: Bidang, Tajuk, Subtajuk, SP (tiada SK) |
| `inventori_DK27_M1.csv` | 54 SP DK2027 T1. ID: DK1-B{bab}-SP{n}. Semua disemak lawan imej PDF pada 25 Nov 2026 (perlu_semak_visual = N) |
| `kelompok_DK27_M1.csv` | 16 subtajuk (lajur padanan_sk: SK KSSM yang dipadankan; asas pautan warisan [INFERENS] ke AM) DK2027 T1 (ID DK1-B{bab}-ST{n}) dipadankan ke rantaian sedia ada, dengan rantaian_sekunder, padanan_kssm, keyakinan |
| `nota_serah_terima_sesiT.md`, `nota_serah_terima_sesiV.md` | Nota serah-terima |
| `README.md`, `.gitignore` | Repositori GitHub awam https://github.com/cikgujep/pemetaan-topikal-matematik (cawangan main). PDF tidak dimuat naik (.gitignore). GitHub Pages: https://cikgujep.github.io/pemetaan-topikal-matematik/ (index.html mengalih ke halaman/pemetaan_topikal.html). Selepas bina.py, commit dan push untuk mengemas kini laman |
| `halaman/` | Templat dan skrip pembina halaman interaktif, dan hasilnya |

Nilai `perlu_semak_visual`: Y = teks diekstrak daripada PDF dan belum disemak lawan imej, N = telah disahkan, T = tidak berkenaan. (Takrif ini daripada nota sesi T sebagai perkara yang perlu disahkan guru; sahkan sebelum bergantung padanya.)

## Keputusan yang telah dibuat (jangan ubah tanpa arahan pengguna)

- Istilah (25 Nov 2026, keputusan pengguna): "rantaian konsep" menggantikan istilah kerja lama "benang" di semua tempat: halaman, panduan, nota, kod dan fail CSV. Lajur CSV kini `rantaian_konsep` (kelompok_topikal, kelompok_DK27_M1), `rantaian_sekunder` (kelompok_DK27_M1) dan `rantaian` (matriks_topikal). Paparan "Rantaian prasyarat" dinamakan "Prasyarat SP".
- Tema (25 Nov 2026): satu tetapan tema untuk seluruh sistem, Auto (ikut peranti, lalai), Terang atau Gelap, disimpan dalam localStorage kunci `pt-theme`. Pilihan pada hab dihantar ke iframe; butang Tema pada Peta dan Pembentangan juga mengubah tema seluruh sistem. "Persembahan" dinamakan "Pembentangan" (fail `pembentangan.html`, `templat_pembentangan.html`; pautan lama `#persembahan` dialih).
- Peranan SK: PENGENALAN (bukan PERKENALAN), PEMBINAAN, PENGUKUHAN, LANJUTAN. Ejaan PENGENALAN dibetulkan pada 25 Nov 2026.
- 15 kelompok (K01 hingga K15) dan 54 rantaian, tanpa pindaan taksonomi Fasa 1. Rantaian tambahan: K01d, K04e, K12f.
- Bidang (lajur `bidang`), semuanya [INFERENS] daripada pengguna, aras rantaian, satu bidang utama setiap rantaian:
  - Algebra (21): K01a hingga K01d, K02a hingga K02d, K03a hingga K03d, K04a hingga K04e, K05a, K05b, K11b (dipindah daripada Geometri), K15a (dipindah daripada Kalkulus); kedua-dua pemindahan pada 25 Nov 2026
  - Geometri (15): K06a hingga K06d, K07a, K07b, K07c, K08a hingga K08d, K09a hingga K09c, K11a
  - Trigonometri (5): K10a hingga K10e
  - Statistik (9): K12a hingga K12f, K13a, K13b, K13c (Set, Logik, Rangkaian kekal dalam Statistik atas keputusan pengguna 25 Nov 2026; pengecualian kepada prinsip bidang; pengguna menolak bidang Matematik Diskret)
  - Kalkulus (3): K15b hingga K15d
  - Pengurusan Kewangan (1): K14a
  - SK mewarisi bidang daripada rantaian utama, bukan kelompok sekunder.
  - Prinsip penetapan bidang (dipersetujui pengguna 25 Nov 2026, [INFERENS]): bidang sesuatu rantaian ikut bidang DSKP Matematik Tambahan bagi konsep yang sama; jika konsep itu tiada dalam AM atau wujud pada aras yang berbeza secara asas, ikut kandungannya. Dilaksanakan: K15a dan K11b ke Algebra. K13a hingga K13c kekal Statistik sebagai pengecualian atas keputusan pengguna.
  - Nota rantaian [INFERENS] pada panel butiran ditulis dalam objek RANTAIAN_NOTA dalam templat.html (kini K15a, K11b).
- Nama bidang projek: lima daripada enam (Algebra, Geometri, Kalkulus, Trigonometri, Statistik) ialah Bidang Pembelajaran rasmi DSKP Matematik Tambahan; "Pengurusan Kewangan" bukan nama DSKP. Semua 59 SK AM sepadan dengan DSKP. Pemetaan SK Matematik ke bidang ini kekal [INFERENS].
- Lajur `bidang_dskp` (ditambah 25 Nov 2026 atas persetujuan pengguna): Bidang Pembelajaran DSKP aras bab, dibaca daripada halaman pembuka setiap bab; bab elektif AM (AM4-B9, AM4-B10, AM5-B7, AM5-B8) daripada Jadual 8 DSKP Matematik Tambahan, dengan label aplikasi dalam kurungan. Matematik memakai lima bidang lain: Nombor dan Operasi, Perkaitan dan Algebra, Sukatan dan Geometri, Statistik dan Kebarangkalian, Matematik Diskret. Lajur `bidang` tidak diubah. Panel butiran memaparkan kedua-duanya.
- Penanda rantaian pada halaman:
  - Mula baharu (takrif pautan, diputuskan pengguna 25 Nov 2026): rantaian tanpa nod primer Matematik DAN tiada SP Matematik Tambahan dalamnya menerima pautan kuat jenis SAMBUNGAN, GENERALISASI atau NOTASI daripada SP Matematik. Pautan ALAT tidak dikira. Hasil: 3 rantaian (K08d, K10d, K15d). Takrif lama dengan nod sekunder aras kelompok (8 rantaian) dibuang kerana padanannya kebanyakan tidak berkaitan. 11 rantaian lain tanpa nod primer Matematik mempunyai prasyarat melalui pautan; ini isu pengelasan rantaian, bukan topik baharu. Hasil bergantung pada kualiti pautan yang belum diaudit.
  - Jeda (disahkan pengguna 25 Nov 2026): jarak dua tingkatan atau lebih antara dua kemunculan berturut-turut (sekurang-kurangnya satu tingkatan tiada). AM4 dikira T4 dan AM5 dikira T5. Hanya nod primer dikira. 11 kekosongan. Label ini hanya menyatakan kekosongan dalam kurikulum, bukan bahawa murid telah lupa. Setiap kad Jeda membawa anotasi [DATA] pautan daripada SP Matematik dalam tingkatan yang tiada (4 Jeda ada pautan: K03d, K04a, K04b, K07c). Anotasi tidak mengubah kiraan. Jika nod selepas Jeda ialah Matematik, kad menyatakan tiada data pautan, kerana pautan hanya dipetakan untuk sasaran Matematik Tambahan.
- Sepanduk "Draf: belum diaudit" dibuang atas arahan pengguna pada 25 Nov 2026. Data masih belum diaudit.
- Halaman: tajuk "Pemetaan Topikal Matematik dan Matematik Tambahan", gaya glassmorphism ditulis dalam CSS sendiri (bukan Tailwind CDN) supaya halaman kekal berdiri sendiri. Halaman digunakan untuk perbincangan dengan guru dan pegawai.
- DK2027 (25 Nov 2026, arahan pengguna): lapisan pilihan pada Lorong, suis "DK2027" menambah lajur "M1 DK2027" selepas M1. Tidak mempengaruhi penanda Mula baharu, Jeda, KPI atau pautan. Padanan rantaian ialah [INFERENS]. Hanya T1 tersedia.
- Cadangan menghidupkan semula kemahiran pada Paparan 4 ialah templat [INFERENS], bukan pertimbangan per rantaian.

## Membina halaman interaktif

```
cd halaman
py bina.py
```

Hasil utama untuk dikongsi: `pemetaan_topikal.html`, satu fail yang menggabungkan Panduan (daripada `templat_hub.html`, angka dikira oleh bina.py), Peta Topikal dan Pembentangan (kedua-duanya dibenam base64, dimuat dalam iframe apabila tab dibuka).

Skrip juga menulis `pembentangan.html` daripada `templat_pembentangan.html`: paparan pembentangan rantaian T1 hingga T5 (mod Gambaran dan Slaid, kekunci anak panah, Space untuk dedah tingkatan, suis DK2027). Penanda dikira dengan takrif yang sama.

Skrip membaca CSV dalam folder induk, membenamkan semuanya sebagai JSON dalam `templat.html`, dan menulis `peta_topikal.html` (fail tunggal, tiada rangkaian diperlukan). Jangan guna pustaka luar atau CDN, kerana halaman mesti berdiri sendiri. Selepas mengubah templat, jalankan `bina.py` dan buka `peta_topikal.html` untuk menyemak. Penanda Mula baharu dan Jeda dikira dalam JavaScript daripada data, bukan ditulis tangan.
