# Nota serah-terima Sesi W (27 Nov 2026)

Skop: kesan DK2027 Matematik T1 pada pautan KSSM ke Matematik Tambahan, berdasarkan tiga fail pemetaan yang ditambah pengguna.

## Fail baharu dan diubah

| Fail | Perubahan |
|---|---|
| `inventori_DK27_M1_catatan.csv` | Fail input pengguna. Tidak diubah. |
| `pemetaan_M1_lama_ke_DK27.csv` | Fail input pengguna. Tidak diubah. 139 SP M1 lama, status dan SP DK27. |
| `pemetaan_M1_DK27_dari_lama.csv` | Fail input pengguna. Tidak diubah. 54 SP DK27 dan sumber lama. |
| `inventori_DK27_M1.csv` | Ditambah lajur `kata_kerja_sp`, `catatan` dan `perlu_semak_visual_catatan` (22 Y) daripada fail catatan. Teks SP, `perlu_semak_visual` (54 N, teks SP) dan nama dokumen tidak diubah. |
| `kelompok_DK27_M1.csv` | `padanan_sk` dan `padanan_kssm` dikira semula daripada pemetaan SP (4 subtajuk berubah: ST1.2, ST7.1, ST7.2, ST7.3). Catatan ST7.2 dibetulkan: akas Teorem Pythagoras digabungkan ke SP7.2.1 dan SP7.2.2. |
| `pautan_warisan_DK27.csv` | Baharu. 69 pautan bersumber SP M1 lama dengan kesan DK27. |
| `halaman/templat.html`, `templat_pembentangan.html`, `templat_hub.html`, `bina.py` | Penanda kesan DK27 dan teks Panduan. |

## Langkah 1: pengesahan

139 `id_lama` sepadan dengan `inventori_M1.csv`; 54 `id_baharu` sepadan dengan `inventori_DK27_M1.csv`; tiada yatim atau pendua; 105 pasangan konsisten dalam kedua-dua arah. Status: GABUNG 48, TIADA DALAM T1 BAHARU 36, UBAH 23, TURUN KE NOTA 17, KEKAL 13, PECAH 2. SP baharu tanpa sumber lama: DK1-B4-SP4.1.4.

## Langkah 3: kesan pada pautan

Liputan: 69 daripada 69 pautan bersumber SP M1 diproses (daripada 356 pautan keseluruhan). Pautan bersumber M2 hingga M5 tidak disentuh kerana DK27 T2 hingga T5 belum ada.

Peraturan kesan [INFERENS]: KEKAL, PECAH, GABUNG = kekal; UBAH = perlu semak; TURUN KE NOTA = dilemahkan; TIADA DALAM T1 BAHARU = terputus (T1 sahaja). Keyakinan = yang lebih rendah antara keyakinan pautan dan keyakinan pemetaan.

Hasil: kekal 30, terputus 23, perlu semak 12, dilemahkan 4. Lajur `sumber_lain_kekal`: 12 daripada 23 pautan terputus masih mempunyai sumber M2 hingga M5 (KSSM semasa) atau sumber M1 lain yang kekal ke sasaran yang sama; 11 tiada sumber lain.

## Langkah 4: jurang dan cadangan [INFERENS]

| Jurang (SP lama tiada dalam DK27 T1) | Bab AM terjejas | Pautan terputus (tanpa sumber lain) | Cadangan bilik darjah | Bergantung pada DK27 T2 hingga T5 |
|---|---|---|---|---|
| Persamaan linear dua pemboleh ubah dan serentak (M1-B6-SK6.2, SK6.3) | AM4-B3 Sistem Persamaan; juga AM4-B5, AM4-B8 | 9 (6) | Sebelum AM4-B3, ajar semula pembentukan dan penyelesaian persamaan linear serentak (penggantian, penghapusan) sebagai prasyarat penuh, bukan imbas kembali ringkas. | Ya. Jika DK27 T2 atau T3 memperkenalkannya, cadangan menjadi imbas kembali sahaja. |
| Peratusan dan perkaitannya dengan nisbah (M1-B4-SK4.5) | AM4-B10 Nombor Indeks | 2 (2) | Sebelum Nombor Indeks, aktiviti penukaran nisbah kepada peratusan dan peratusan suatu kuantiti; tunjukkan indeks sebagai nisbah x 100. | Ya. |
| Set dan tatatanda set (M1-B11) | AM5-B4 Pilih Atur dan Gabungan, AM5-B5 Taburan Kebarangkalian | 2 (2) | Perkenalkan tatatanda set yang diperlukan (unsur, subset, ruang sampel) pada permulaan AM5-B4. KSSM M4-B4 Operasi Set wujud tetapi tiada pautan dipetakan daripadanya ke SP ini. | Ya, terutama sama ada set muncul dalam DK27 T4. |
| Generalisasi pendaraban kuasa dua dan kuasa tiga (M1-B3-SP3.1.8) | AM4-B4 Indeks, Surd dan Logaritma | 1 (1) | Hubungkan dengan hukum indeks M3 KSSM semasa; semak semula apabila DK27 T3 ada. | Ya. |
| Penilaian ungkapan algebra dengan penggantian (M1-B5-SP5.1.3) | AM4-B1 Fungsi | 2 (0) | Latihan penggantian nilai sebagai pengenalan tatatanda f(x). | Separa: sumber lain wujud dalam KSSM M1 dan M2. |
| Perimeter dan luas (M1-B10, sebahagian) | AM4-B7, AM4-B9, AM5-B1, AM5-B3 | 4 (0) | Risiko rendah; semua sasaran ada sumber M2 hingga M4. Semak sama ada SP7.1.3 dan SP7.3.3 DK27 meliputi keperluan rumus luas. | Separa. |
| Operasi integer (M1-B1-SP1.2.1, SP1.2.2) | AM4-B8 Vektor | 2 (0) | Tiada tindakan khusus; fail pemetaan menganggapnya pengetahuan sedia ada. Jangan anggap topik dipindah. | Ya. |
| Sudut dongak dan tunduk (M1-B8-SP8.3.5) | AM4-B9 Penyelesaian Segi Tiga | 1 (0) | Ada sumber M3-B5. Imbas kembali konteks sudut dongak sebelum AM4-B9. | Separa. |

Dilemahkan (kandungan dalam Nota sahaja): M1-B4-SP4.4.2 (nisbah apabila diberi nisbah lain) ke AM4-B7 dan AM4-B10, dan M1-B1-SP1.2.5 (hukum operasi) ke AM4-B5.

## Langkah 5: paparan

- Suis DK2027 (Lorong): chip Matematik Tambahan memaparkan lencana "DK27: n terputus / dilemahkan / perlu semak" (21 SK AM terjejas). Kad pautan dalam panel butiran dan Prasyarat SP memaparkan kesan serta butiran (status, SP DK27, sumber lain, keyakinan).
- Chip subtajuk DK27 dan laci DK27 dalam Pembentangan kini memakai warisan aras SP daripada `pautan_warisan_DK27.csv`, menggantikan warisan aras SK.
- Mod KSSM (suis mati): tiada penanda; diuji dalam pelayar terbina (pelayan tempatan), tiada ralat konsol.
- Panduan bahagian 9 dikemas kini dengan angka dan jurang utama.

## Perlu disahkan guru

- 15 pautan warisan berkeyakinan rendah: P-AM4-B1-008, P-AM4-B2-013, P-AM4-B3-012, P-AM4-B4-016, P-AM4-B6-010, P-AM4-B7-002, P-AM4-B7-004, P-AM4-B7-021, P-AM4-B8-024, P-AM4-B9-020, P-AM4-B9-022, P-AM4-B10-004, P-AM4-B10-009, P-AM5-B1-014, P-AM5-B2-030.
- 16 SP lama berkeyakinan rendah dalam pemetaan: M1-B3-SP3.1.7, SP3.2.7, M1-B4-SP4.4.2, SP4.4.3, M1-B8-SP8.1.2, SP8.1.5, SP8.2.1, SP8.3.3, M1-B9-SP9.2.3, SP9.3.3, SP9.3.4, M1-B10-SP10.1.3, SP10.2.3, SP10.3.1, SP10.3.2, M1-B12-SP12.1.6.
- 22 Nota DK27 bertanda Y (`perlu_semak_visual_catatan`), termasuk Nota 1.3.1 dan 1.3.2. Semakan kasar teks juga menunjukkan beberapa Nota bertanda N tidak sepadan dengan teks ekstrak PDF (mungkin kesan susun atur dua lajur).
- Penyerapan perimeter dan luas ke SP7.1.3 dan SP7.3.3 (inferens).
- DK1-B4-SP4.1.4 ditanda BAHARU tanpa sumber lama.
- Peraturan GABUNG = kekal dan UBAH = perlu semak ialah penyederhanaan; sesetengah GABUNG mungkin mengubah kedalaman.

## Perkara terbuka

1. Dokumen DK27 T2 hingga T5: apabila ada, ulang langkah 3 untuk pautan bersumber M2 hingga M5 dan nilai semula semua status "terputus".
2. Audit 12 pautan "perlu semak" satu demi satu.
3. Semak Nota DK27 lawan imej PDF.

## Kelemahan dan risiko

- "Terputus" diukur pada aras SP T1 sahaja; ia tidak bermaksud murid tidak akan belajar kandungan itu dalam DK27.
- Sumber lain "M2 hingga M5" ialah KSSM semasa; dalam DK27 sumber itu sendiri mungkin berubah.
- Pautan asal belum diaudit; kesan mewarisi kelemahan pautan itu.
- Pembentangan tidak memaparkan lencana kesan pada kad AM; hanya laci subtajuk DK27.
