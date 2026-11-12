## characters.rpy — Struk Terakhir Pukul 02.14
## Definisi karakter, stat tersembunyi, dan flag.
## Stat TIDAK ditampilkan sebagai angka ke pemain (hanya terasa lewat dialog).

# --- Karakter ---
# Warna nama disesuaikan dengan karakter (Alya = teal SegarMart).
define alya = Character("Alya", color="#3a7d7c", what_prefix="\"", what_suffix="\"")
define wirya = Character("Pak Wirya", color="#8a7a5a", what_prefix="\"", what_suffix="\"")
define ujang = Character("Mang Ujang", color="#5a6a8a", what_prefix="\"", what_suffix="\"")
define dimas = Character("Dimas", color="#7a5a8a", what_prefix="\"", what_suffix="\"")
define ratna = Character("Bu Ratna", color="#8a3a3a", what_prefix="\"", what_suffix="\"")
define sari = Character("Mbak Sari", color="#6a8a5a", what_prefix="\"", what_suffix="\"")
define dita = Character("Dita", color="#3a6a7a", what_prefix="\"", what_suffix="\"")
define narator = Character(None)

# --- Stat tersembunyi ---
default ketelitian = 0
default kepercayaan = 0
default keberanian = 0

# --- Flag ---
# Prolog
default lapor_bu_ratna = False
default simpan_sendiri = False
default bukti_struk = False

# Chapter 1 — taruhan pribadi, selalu aktif sejak Scene 1.2
default dituduh_curi_lilin = False

# Chapter 3 — jalur kepercayaan
default percaya_ujang = False
default percaya_dimas = False

# Bukti (True Ending butuh ketiganya, kecuali CCTV yang pendukung)
default bukti_buku_1998 = False
default bukti_cctv_2231 = False
default bukti_mesin_lama = False

# Tanya langsung ke Pak Wirya — bisa didapat Ch.2-A ATAU Ch.4-E
default tanya_pak_wirya = False

# Penghitung: berapa kali menyembunyikan penyelidikan dari Bu Ratna.
# Ending D hanya bisa terjadi kalau hide_count >= 2 DAN tidak pernah lapor.
default hide_count = 0

# --- Placeholder aset ---
# Selama gambar Google Flow belum ada, background/sprite memakai
# warna solid + teks. Ganti dengan file di game/images/ saat aset siap.
# Contoh pengganti:
#   image bg depan_toko = "images/backgrounds/bg_depan_toko.png"
#   image alya senyum = "images/sprites/alya_senyum.png"
