# Struk Terakhir Pukul 02.14

Visual novel misteri ringan / supernatural, Bahasa Indonesia.
Heroine: **Alya Ayu Baskara (AAB), 24 tahun**, kasir shift sore di SegarMart fiktif, Antapani, Bandung, Oktober 2020.

> Toko tutup pukul 22.00. Selalu pukul 22.00.
> Lalu kenapa ada struk bertanggal 14 Oktober 1998, jam 02.14, di meja kasir?

- **Engine:** Ren'Py 8.5.3 (open source, MIT, gratis untuk komersial)
- **Target durasi:** 45–60 menit / playthrough, 22.000–26.000 kata
- **Struktur:** Prolog + 5 chapter (Senin–Jumat), 4 ending
- **Resolusi:** 1280×720 (16:9)

Naskah lengkap / outline: `docs/outline.md` (ringkasan) dan
`~/workspace/visual-novel/struk-terakhir-0214/outline-naskah.md` (versi penuh, di luar repo ini).

## Cara menjalankan

1. Instal **Ren'Py 8.5.3** dari https://www.renpy.org/ (versi yang dipakai saat scaffold ini dibuat, 15 Mei 2026).
2. Buka Ren'Py Launcher → **Open Project** / salin folder ini ke folder proyek Ren'Py kamu.
3. Pilih proyek `struk-terakhir` → **Launch Project**.
4. Untuk build: di Launcher → **Build Distributions** → pilih Windows / macOS / Linux / Android / iOS / Web (Web masih beta di Ren'Py 8).

> Catatan: `game/gui.rpy` dan `game/screens.rpy` di repo ini adalah versi minimal yang sudah disesuaikan untuk proyek ini. Kalau Ren'Py Launcher mengeluh saat pertama kali dibuka, biarkan Launcher membuat proyek baru dengan nama yang sama, lalu timpa file `game/script.rpy`, `game/characters.rpy`, dan `game/options.rpy` dengan file dari repo ini — `gui.rpy` / `screens.rpy` bawaan Launcher tetap bisa dipakai.

## Struktur proyek

```
game-struk-terakhir/
├── README.md
├── .gitignore
├── docs/
│   └── outline.md            # Ringkasan outline + peta ending
└── game/
    ├── options.rpy           # Nama game, resolusi, build
    ├── characters.rpy        # Definisi karakter, stat, flag
    ├── script.rpy            # Prolog + Chapter 1 (playable),
    │                         # Chapter 2–5 + ending sebagai label stub
    ├── gui.rpy               # GUI minimal (font, warna, ukuran teks)
    ├── screens.rpy           # Layar minimal (say, choice, menu, save/load)
    ├── images/
    │   ├── backgrounds/      # 7 background — lihat docs/outline.md
    │   ├── sprites/          # Sprite Alya, Pak Wirya, Mang Ujang, Dimas, Bu Ratna
    │   └── cg/               # CG1 struk 1998, CG2 buku 1998, CG3 lilin 02.14
    └── audio/
        └── README.md         # Daftar kebutuhan audio (belum ada file)
```

## Sistem pilihan (sesuai outline)

Tiga stat tersembunyi, tidak ditampilkan sebagai angka ke pemain:

- `ketelitian` — memeriksa struk, stok, CCTV, buku gudang
- `kepercayaan` — percaya Mang Ujang atau Dimas
- `keberanian` — tanya langsung ke Pak Wirya, langgar perintah Bu Ratna

Flag penting (di `game/characters.rpy`):

- `lapor_bu_ratna` / `simpan_sendiri` (Prolog)
- `dituduh_curi_lilin` = True sejak Scene 1.2
- `percaya_ujang` / `percaya_dimas` (Chapter 3)
- `bukti_buku_1998`, `bukti_cctv_2231`, `bukti_mesin_lama`
- `tanya_pak_wirya` (Chapter 2-A ATAU Chapter 4-E — ada kesempatan kedua)

**True Ending (A — Pesanan Dituntaskan):**
`bukti_buku_1998` + `bukti_mesin_lama` + `tanya_pak_wirya`, pilih A di Chapter 4 dan A di Chapter 5.

Ending lain: B Tenang, C Salah Tuduh (tuduh di Ch.4-D), D Dipindah Cabang (Ch.5-D + 2× menyembunyikan penyelidikan dari Bu Ratna; tidak bisa terjadi kalau pernah `lapor_bu_ratna`).

## Aset artwork

Artwork digenerate di Google Flow (di luar repo ini).
Daftar lengkap ada di `docs/outline.md` bagian 6 dan di
`character-sheet-alya.md` / `concept-art-alya-prompts.md`.

Nama file yang diharapkan di `game/images/`:

- Background: `bg_depan_toko.png`, `bg_interior_siang.png`, `bg_meja_kasir.png`, `bg_gudang.png`, `bg_jalan_malam.png`, `bg_kos_alya.png`, `bg_petak_tanah.png`
- Sprite Alya: `alya_senyum.png`, `alya_curiga.png`, `alya_lelah.png`, `alya_kaget.png`
- Sprite lain: `wirya_datar.png`, `wirya_sedih.png`, `wirya_senyum.png`, `ujang_serius.png`, `ujang_ragu.png`, `ujang_pasrah.png`, `dimas_antusias.png`, `dimas_serius.png`, `dimas_kecewa.png`, `ratna_tegas.png`, `ratna_lelah.png`
- CG: `cg_struk_1998.png`, `cg_buku_1998.png`, `cg_lilin_0214.png`

Selama aset belum ada, game memakai placeholder warna solid yang didefinisikan di `game/script.rpy` (image `bg … = Solid(...)`, sprite `= Text(...)`). Jadi proyek tetap bisa dijalankan dan dites logika branching-nya tanpa menunggu gambar selesai.

## Status

- [x] Scaffold Ren'Py 8.5.3
- [x] Prolog + Chapter 1 playable (dengan dialog inti dari outline)
- [x] Chapter 2 playable (gudang 15.30 + buku 1998, pilihan 21.14, warung kopi 22.30)
- [ ] Chapter 3–5 — naskah penuh (saat ini label stub + beat utama)
- [ ] Aset background / sprite / CG dari Google Flow
- [ ] Audio / musik
- [ ] Playtest HP + build Android

## Lisensi

Kode game di repo ini (file `.rpy`, `.md`) bebas dipakai untuk proyek ini.
Ren'Py sendiri berlisensi MIT (sebagian LGPL) — lihat https://www.renpy.org/.
Artwork karakter/latar adalah karya dari Google Flow untuk proyek ini, bukan aset open source.
