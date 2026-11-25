# Nota serah-terima Sesi V

Skop: paparan interaktif pemetaan topikal (satu halaman HTML), penambahan dimensi bidang, pembetulan ejaan PENGENALAN, dan pek serah-terima ke Claude Code.

## Apa yang dihasilkan

- `halaman/peta_topikal.html`: halaman tunggal, data dibenamkan (603 SP, 181 SK, 54 rantaian, 15 kelompok, 6 bidang, 356 pautan). Empat paparan:
  1. Lorong topikal: baris rantaian dikumpul mengikut bidang atau kelompok, lajur M1, M2, M3, M4, AM4, M5, AM5. Chip bagi setiap SK. Dua warna sahaja (biru Matematik, jingga Matematik Tambahan), keyakinan rendah ditunjuk dengan sempadan putus-putus dan teks. Penanda Mula baharu dan Jeda dikira daripada data.
  2. Panel butiran (klik chip): SK, semua SP, Catatan, kelompok, kemahiran, peranan, bukti, sumber, keyakinan, pautan masuk dan keluar, lompat ke nod berpaut, dan senarai SK dalam rantaian yang sama.
  3. Rantaian prasyarat: pilih SP Matematik Tambahan, lihat garis masa ke belakang. Nod dilabel PAUTAN atau RANTAIAN.
  4. Mula baharu dan Jeda: senarai rantaian, nod sebelum dan selepas jeda, cadangan [INFERENS].
- Penapis: bidang, kelompok, kemahiran, tingkatan (lajur), jenis hubungan, kekuatan, keyakinan, "Mula baharu dan Jeda sahaja", carian teks.
- Lajur `bidang` ditambah pada `kelompok_topikal.csv` dan `matriks_topikal.csv`.
- Pembetulan PERKENALAN kepada PENGENALAN dalam `kelompok_topikal.csv` (51 baris) dan nota sesi T.

## Pengesahan data

- Inventori 603 SP (139 + 166 + 127 + 171), semua id_nod unik.
- 181 SK dalam inventori sepadan dengan 181 baris kelompok dan 181 id dalam matriks. Tiada pendua atau id yatim.
- 356 pautan (228 AM4 dan 128 AM5). Semua nod_sasaran sah. Semua nod_sumber sah kecuali 15 pautan TIADA PRASYARAT tanpa nod sumber (5 bernilai "-", 10 bernilai "TIADA").

## Perlu disahkan guru

- Daripada sesi T: M5-B5-SK5.4, M5-B8-SK8.1, AM4-B10-SK10.1, AM4-B10-SK10.2, AM5-B3-SK3.4 (SP3.4.1 tiada dalam inventori), dan maksud nilai N, Y, T dalam `perlu_semak_visual`.
- 4 SP M1 bersumber "[DSKP] tidak pasti": M1-B3-SP3.1.3, M1-B4-SP4.1.2, M1-B6-SP6.3.2, M1-B6-SP6.3.3.
- 205 SP bertanda Y belum disemak lawan imej PDF.
- 42 pautan keyakinan rendah.
- Pemetaan bidang (semuanya [INFERENS], pilihan pengguna).

## Perkara terbuka

1. [DIPUTUSKAN 25 Nov 2026] Pengurusan Kewangan kekal satu rantaian (K14a). Pecahan mengikut konteks ditolak kerana menghasilkan lorong 1 hingga 2 SK tanpa kesinambungan. Catatan M3-B3-SK3.1 dalam kelompok_topikal.csv ditambah [INFERENS] tentang faedah kompaun sebagai jambatan ke AM4-B4 dan AM4-B5 (5 pautan). kelompok_sekunder tidak diubah.
2. [DIPUTUSKAN 25 Nov 2026] Takrif Mula baharu: takrif pautan dipilih (lihat CLAUDE.md). 3 rantaian: K08d, K10d, K15d. Kotak pilihan nod sekunder dibuang daripada halaman.
3. [DIPUTUSKAN 25 Nov 2026] Takrif Jeda: kekal (sekurang-kurangnya satu tingkatan tiada, 11 Jeda). Anotasi pautan daripada tingkatan yang tiada ditambah pada kad Jeda (lihat CLAUDE.md).
4. [DIPUTUSKAN 25 Nov 2026] Bidang lawan DSKP: lima nama bidang projek ialah bidang rasmi DSKP AM (59/59 SK AM sepadan). Lajur bidang_dskp ditambah pada kelompok_topikal.csv dan dipaparkan dalam panel. Percanggahan utama (Matriks berkait perkara 6): Matematik Diskret (M1-B11, M4-B3 hingga B5, 8 SK) diletak dalam Statistik, dan M5-B2 Matriks (Perkaitan dan Algebra dalam DSKP) diletak dalam Geometri.
5. [DIPUTUSKAN 25 Nov 2026] K15a dipindah ke bidang Algebra (matriks_topikal.csv 1 baris, kelompok_topikal.csv 4 SK). Sebab: DSKP meletakkan M2-B9 dan M4-B7 dalam Perkaitan dan Algebra, dan tiada konsep had, terbitan atau kamiran. Nota [INFERENS] pada panel: asas kinematik dan pengamiran dalam konteks fizikal. Prinsip penetapan bidang direkod dalam CLAUDE.md. Halaman ini akan digunakan untuk perbincangan dengan guru dan pegawai.
6. [DIPUTUSKAN 25 Nov 2026] K11b Matriks dipindah ke bidang Algebra (matriks_topikal.csv 1 baris, kelompok_topikal.csv 2 SK). Sebab: DSKP meletakkan M5-B2 dalam Perkaitan dan Algebra, matriks tiada dalam DSKP AM, tiada pautan ke AM, dan semua SP ialah operasi. Nota panel menyebut kaitan tatatanda dengan vektor lajur AM4-B8 (murid AM melihat vektor sebelum matriks). Pautan arah balik ini tidak boleh direkod dalam fail pautan sekarang.
7. Cadangan sesi T yang belum dibuat: pecahkan M4-B1-SK1.1 (fungsi dan persamaan kuadratik) dan AM5-B2-SK2.4 (Aplikasi Pembezaan, 9 SP).
8. [DIPUTUSKAN 25 Nov 2026] Sepanduk draf dibuang atas arahan pengguna. UI diberi gaya glassmorphism (CSS sendiri). Belum disemak dalam pelayar.

9. [DIPUTUSKAN 25 Nov 2026] K13a hingga K13c kekal Statistik. Pengguna menolak bidang Matematik Diskret. Bidang kekal 6. Perkara 7 dan 8 belum dibincang.

10. DK2027 T1 dipetakan (16 subtajuk, 54 SP) dan dipaparkan melalui suis. Perkara terbuka: Set (K13a), persamaan linear dua pemboleh ubah dan serentak (M1-B6-SK6.2, SK6.3), akas Pythagoras dan bab Perimeter dan Luas tidak dijumpai dalam DK2027 T1; surd muncul dalam T1 (K02c). Teks SP7.3.3 dibetulkan; 54 SP disemak lawan imej. Pautan warisan [INFERENS] DK2027 ke AM melalui padanan_sk. Halaman pembentangan.html ditambah. Dokumen DK2027 T2 hingga T5 belum ada.

11. Istilah "rantaian" ditukar kepada "rantaian konsep" pada halaman (CSV tidak diubah). Fail utama untuk dikongsi: halaman/pemetaan_topikal.html (Panduan, Peta Topikal, Pembentangan).

## Kelemahan dan risiko paparan

- Pautan wujud hanya dengan sasaran Matematik Tambahan. Rantai Matematik ke Matematik pada Paparan 3 datang daripada keahlian rantaian (matriks), bukan pautan SP ke SP yang dipetakan. Garis penyambung tidak dilukis.
- Nod sekunder (53 SK) dipaparkan sebagai baris berasingan aras kelompok, jadi chip yang sama muncul dua kali dalam mod kelompok.
- Penapis jenis, kekuatan dan keyakinan bermakna berbeza antara Lorong (menapis SK) dengan Rantaian (menapis pautan).
- Chip memotong tajuk SK kepada dua baris pada skrin. Teks penuh ada pada tooltip, panel dan paparan cetak.
- Rendering visual, skrin kecil dan cetakan diuji dalam jsdom sahaja, belum disemak dalam pelayar.
- Cadangan menghidupkan semula kemahiran ialah templat [INFERENS], bukan pertimbangan per rantaian.

## Langkah seterusnya (cadangan)

1. Putuskan perkara terbuka 1 hingga 3.
2. Buka `halaman/peta_topikal.html` dalam pelayar dan semak susun atur, skrin kecil dan cetakan.
3. Audit sampel pautan berkeyakinan rendah dan baris Perlu disahkan guru, kemudian pindahkan sepanduk draf apabila pengguna mengarahkan.
4. Pertimbangkan pautan Matematik ke Matematik jika rantaian penuh T1 hingga T5 diperlukan.

## Liputan sesi

603 daripada 603 SP dan 181 daripada 181 SK dimuatkan pada halaman. Tiada yang tertinggal.
