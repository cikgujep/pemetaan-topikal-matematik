# Pemetaan Topikal Matematik dan Matematik Tambahan

Peta kebergantungan konsep antara Matematik KSSM Tingkatan 1 hingga 5 dan Matematik Tambahan Tingkatan 4 dan 5, dengan lapisan pilihan Dokumen Kurikulum Matematik Tingkatan 1 (bermula 2027). Peta ini alat guru.

## Buka

Buka `halaman/pemetaan_topikal.html` dalam pelayar. Fail tunggal, tidak memerlukan internet. Tiga tab:

- **Panduan**: cara membaca ID, rantaian konsep, kelompok, bidang, pautan, penanda Mula baharu dan Jeda, had dan risiko.
- **Peta Topikal**: lorong rantaian konsep mengikut tingkatan, prasyarat SP, senarai Mula baharu dan Jeda.
- **Pembentangan**: satu rantaian konsep setiap slaid, T1 hingga T5.

## Data

| Fail | Kandungan |
|---|---|
| `inventori_*.csv` | Standard Pembelajaran (SP) daripada DSKP dan DK2027 |
| `kelompok_topikal.csv` | Standard Kandungan (SK) dengan kelompok, rantaian konsep dan bidang |
| `matriks_topikal.csv` | Rantaian konsep x tingkatan |
| `pautan_AM4.csv`, `pautan_AM5.csv` | Pautan SP Matematik ke SP Matematik Tambahan |
| `kelompok_DK27_M1.csv` | Subtajuk DK2027 T1 dipadankan ke rantaian konsep |

Fail PDF DSKP dan DK2027 tidak disertakan. Dokumen tersebut milik Kementerian Pendidikan Malaysia.

## Bina semula halaman

```
cd halaman
py bina.py
```

## Status

Draf kerja. Data belum diaudit sepenuhnya: sebahagian SP belum disemak lawan imej PDF, dan sebahagian pautan berkeyakinan rendah. Tuntutan dilabel [DSKP] atau [INFERENS]; kelompok, rantaian konsep dan nama bidang projek ialah [INFERENS], bukan istilah rasmi.
