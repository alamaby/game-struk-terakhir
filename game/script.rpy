## script.rpy — Struk Terakhir Pukul 02.14
## Ren'Py 8.5.3 — Prolog + Chapter 1 playable, Chapter 2–5 stub.
## Dialog inti diambil dari outline-naskah.md (revisi audit 2026-11-11).

# --- Placeholder aset (ganti dengan file di game/images/ saat siap) ---
image bg depan_toko = Solid("#5a6a7a")
image bg interior_siang = Solid("#8a7a5a")
image bg meja_kasir = Solid("#3a5a4a")
image bg gudang = Solid("#2a2a2a")
image bg jalan_malam = Solid("#1a2a4a")
image bg kos_alya = Solid("#4a3a5a")
image bg petak_tanah = Solid("#0a1a2a")
image bg hitam = Solid("#000000")

# Sprite placeholder: teks nama karakter di tengah layar.
# Ganti dengan: image alya senyum = "images/sprites/alya_senyum.png", dst.
image alya senyum = Text("ALYA — senyum kerja", size=40, color="#ffffff")
image alya curiga = Text("ALYA — curiga", size=40, color="#ffffff")
image alya lelah = Text("ALYA — lelah", size=40, color="#ffffff")
image alya kaget = Text("ALYA — kaget / haru", size=40, color="#ffffff")
image wirya datar = Text("PAK WIRYA — datar", size=40, color="#ffffff")
image wirya sedih = Text("PAK WIRYA — sedih", size=40, color="#ffffff")
image wirya senyum = Text("PAK WIRYA — senyum tipis", size=40, color="#ffffff")
image ujang serius = Text("MANG UJANG — serius", size=40, color="#ffffff")
image ujang ragu = Text("MANG UJANG — ragu", size=40, color="#ffffff")
image ratna tegas = Text("BU RATNA — tegas", size=40, color="#ffffff")
image dimas antusias = Text("DIMAS — antusias", size=40, color="#ffffff")

# --- Awal game ---
label start:
    scene bg hitam
    "SegarMart Antapani tutup pukul 22.00. Selalu pukul 22.00."
    jump prolog

# ============================================================
# PROLOG — Senin, 13.55 WIB
# ============================================================
label prolog:
    scene bg depan_toko
    show alya lelah at center

    "Senin, 13.55. Gerimis tipis di depan SegarMart Antapani."
    "Alya jalan kaki dari kos, beli gorengan di depan toko, datang untuk shift sore 14.00–22.00."
    "Toko ini tutup jam sepuluh. Selalu jam sepuluh. Bukan karena sepi, tapi karena aturan."

    show alya senyum at center
    sari "Kas pagi cocok. Jangan lupa, pengumuman tutup setengah sepuluh."
    "Mbak Sari serah terima kas, lalu pulang. Dia tidak ada di toko malam hari."

    hide alya
    scene bg meja_kasir
    show alya curiga at center

    "Alya mengecek meja kasir. Ada satu struk terlipat di bawah meja."
    "Header: WARUNG BU WIRYA."
    "Roti tawar Rp2.500, susu kotak Rp1.500, lilin Rp750. Total Rp4.750."
    "Tanggal: 14 Oktober 1998. Jam tercetak: 02.14 WIB."

    alya "Sembilan belas sembilan delapan? Toko ini tutup jam sepuluh malam. Siapa yang belanja jam dua pagi, dua puluh dua tahun lalu — dan kenapa struknya ada di sini hari ini?"

    # Pilihan 1 (Prolog)
    menu:
        "Laporkan ke Bu Ratna sekarang.":
            $ lapor_bu_ratna = True
            $ bukti_struk = True
            $ ketelitian += 1
            "Bu Ratna mencatatnya. Laporan ini nanti akan melindungi Alya."
            jump chapter1

        "Simpan struknya di saku, selidiki sendiri.":
            $ simpan_sendiri = True
            $ bukti_struk = True
            $ keberanian += 1
            $ hide_count += 1
            "Alya melipat struk itu dan memasukkannya ke saku seragam."
            jump chapter1

        "Buang saja, anggap struk lama nyangkut.":
            $ bukti_struk = False
            "Alya membuangnya. Tapi dia masih memikirkannya sepanjang shift."
            "Tanpa struk itu, True Ending sudah tidak mungkin — dia baru akan sadar di Chapter 4."
            jump chapter1

# ============================================================
# CHAPTER 1 — Senin: Struk yang Mustahil
# ============================================================
label chapter1:
    scene bg interior_siang
    show alya lelah at center

    "Oktober 2020. Bukan panic buying — itu Maret-April. Sekarang AKB, pelanggan beli masker dan kebutuhan harian dalam jumlah wajar, tetap pakai masker dan jaga jarak."

    show dimas antusias at center
    dimas "Mbak Alya, mukanya kenapa? Kayak lihat hantu."
    alya "Bukan hantu. Struk. Tanggalnya sembilan delapan."
    dimas "Wah. Itu sih... menarik."

    # Scene 1.2 — Opname dan lilin yang hilang (21.00)
    scene bg gudang
    show alya curiga at center
    "21.00. Alya dan Dita opname stok gudang. Stok lilin di gudang kurang 1 tanpa transaksi tercatat di POS."

    show ratna tegas at center
    ratna "Lilin kurang satu, Lya. Tidak ada transaksi. Kamu yang pegang gudang sore ini, kan?"

    $ dituduh_curi_lilin = True
    "Kalau saya tidak bisa menjelaskan ini, saya yang dicurigai. Bukan cuma struk aneh — ini soal nama saya."

    # Scene 1.3 — 21.14, dia datang
    scene bg meja_kasir
    show wirya datar at center
    "21.14. Bel pintu berbunyi. Pak Wirya masuk, seperti biasa. Roti, susu, lilin. Rp23.500 pas — dari POS SegarMart, bukan dari mesin lama."

    alya "Pak... Bapak tiap hari jam segini, ya?"
    wirya "Jam segini saya baru selesai makan malam, Neng. Jalan kaki dari rumah keponakan saya, sepuluh menit."
    alya "Bapak sengaja datang jam segini terus?"
    wirya "Saya sengaja datang sebelum pengumuman tutup. Biar Neng tidak terburu-buru hitung kas."

    # Scene 1.4 — Tutup toko
    scene bg jalan_malam
    "Pengumuman 21.30, rolling door diturunkan 22.00. Alya dan Dita tutup kas."
    "Pukul 22.31 lampu toko dan lampu gudang dimatikan — tapi CCTV TIDAK mati. CCTV di sirkuit terpisah dengan UPS, merekam 24 jam dengan mode infrared."
    "Justru ini yang membuat struk 02.14 makin mustahil: CCTV membuktikan tidak ada transaksi di kasir setelah 22.00."
    "Alya pulang jalan kaki, hujan rintik. Di kos dia membuka lagi struk 1998 itu."

    # Pilihan 2 (Chapter 1, di kos 23.00)
    scene bg kos_alya
    show alya curiga at center
    menu:
        "Foto struknya dan kirim ke Dimas.":
            $ percaya_dimas = True
            $ kepercayaan += 1
            "Dimas membalas: dia butuh waktu ke perpustakaan. Kabar baru Rabu/Kamis."
            jump chapter2

        "Tanya Mang Ujang besok pagi sebelum shift.":
            $ percaya_ujang = True
            $ kepercayaan += 1
            "Besok pagi, Mang Ujang akan mengajak Alya ke gudang."
            jump chapter2

        "Tidur saja, besok lupakan.":
            "Alya mencoba tidur. Tapi masalah lilin tetap mengharuskannya kembali menyelidiki besok."
            jump chapter2

# ============================================================
# CHAPTER 2 — Selasa: Pelanggan Pukul 21.14 (STUB)
# Naskah penuh: tulis di label ini, mengikuti outline Ch.2.
# Beat yang harus ada:
#   2.1 Gudang 15.30 — buku 1998 (bukti_buku_1998 = True jika masuk gudang)
#   2.2 Pilihan 3 di 21.14 — A: tanya_pak_wirya = True
#       B: ikuti pulang (Keberanian +2), C: diam (Ketelitian +1)
#   2.3 Setelah tutup 22.30, warung kopi
# ============================================================
label chapter2:
    scene bg gudang
    show ujang serius at center
    "[Chapter 2 — STUB: naskah penuh belum ditulis. Beat: gudang 15.30, buku 1998, pilihan 21.14.]"
    "Placeholder logika: pemain yang masuk gudang mendapat bukti buku 1998."
    $ bukti_buku_1998 = True

    menu:
        "Tanya langsung: \"Pak, Bapak kenal Bu Lastri?\"":
            $ tanya_pak_wirya = True
            wirya "Dia istri saya."
            jump chapter3

        "Ikuti dia pulang setelah toko tutup (22.15, di luar toko).":
            $ keberanian += 2
            "Alya melihat Pak Wirya berjalan kaki ke arah rumah keponakannya di Antapani, bukan naik angkot. Dia berhenti sebentar di petak tanah kosong di belakang toko, menunduk sebentar, lalu lanjut jalan."
            jump chapter3

        "Diam saja, layani seperti biasa.":
            $ ketelitian += 1
            "Alya memperhatikan: Pak Wirya selalu menatap rak lilin paling bawah, tempat dulu ada foto."
            jump chapter3

# ============================================================
# CHAPTER 3 — Rabu: Dua Versi Cerita (STUB)
# Beat: 3.1 versi Mang Ujang (bohong, takut toko dibilang angker)
#   3.2 versi Dimas (papan panti Lembang, satpam panti)
#   Pilihan 4: percaya_ujang / percaya_dimas / keduanya
#   3.3 CCTV 22.31 — bukti_cctv_2231 = True (jalur Dimas / mandiri)
#   Akhir: teguran pertama Bu Ratna
# ============================================================
label chapter3:
    scene bg interior_siang
    "[Chapter 3 — STUB: naskah penuh belum ditulis. Beat: dua versi cerita, CCTV 22.31, teguran Bu Ratna.]"
    $ bukti_cctv_2231 = True
    jump chapter4

# ============================================================
# CHAPTER 4 — Kamis: Pesanan Terakhir (STUB)
# Beat: 4.1 rumah keponakan / gudang, 4.2 mesin kasir lama
#   (bukti_mesin_lama = True), Mang Ujang mengaku soal lilin
#   Peringatan kalau bukti belum lengkap
#   4.3 21.14 — Rp50.000, \"besok saya tidak datang lagi\"
#   Pilihan 5: A janji 02.14, B tolak, C lapor Bu Ratna,
#   D tuduh (Ending C), E tanya langsung (kesempatan kedua tanya_pak_wirya)
# ============================================================
label chapter4:
    scene bg gudang
    "[Chapter 4 — STUB: naskah penuh belum ditulis. Beat: mesin kasir lama, Rp50.000, pilihan akhir sebelum Jumat.]"

    if not (bukti_buku_1998 and bukti_mesin_lama and tanya_pak_wirya):
        "Alya merasa masih ada yang kurang. Ada bukti yang belum dia pegang."
        "Kalau dia lanjut tanpa bukti lengkap, dia akan jatuh ke Ending B."

    $ bukti_mesin_lama = True

    menu:
        "Janji akan melakukannya pukul 02.14 di luar toko.":
            jump chapter5

        "Tolak karena takut, sarankan Pak Wirya melakukannya sendiri.":
            jump ending_b

        "Laporkan semuanya ke Bu Ratna dan minta izin resmi.":
            $ lapor_bu_ratna = True
            "Bu Ratna melarang. Alya harus memilih melanggar atau nurut."
            jump chapter5

        "Tuduh Mang Ujang atau Dimas sebagai pelaku yang mencetak struk.":
            jump ending_c

        "Tanya langsung ke Pak Wirya sekarang: \"Pak, kenapa Bapak tidak melakukannya sendiri malam ini?\"":
            $ tanya_pak_wirya = True
            wirya "Saya sudah terlalu lemah untuk keluar jam 2 pagi, Neng. Saya percaya Neng yang masih muda bisa melakukannya."
            jump chapter5

# ============================================================
# CHAPTER 5 — Jumat: 21.14 Terakhir (STUB)
# Beat: 5.1 pintu tidak berbunyi 21.14, 5.2 beli 1 set Rp23.500
#   dari Rp50.000 (kembalian Rp26.500 untuk ojek), 5.3 Pilihan 6
# ============================================================
label chapter5:
    scene bg meja_kasir
    "[Chapter 5 — STUB: naskah penuh belum ditulis.]"
    "21.14. Pintu toko tidak berbunyi. Pak Wirya tidak datang, sesuai janjinya Kamis."
    "Sebelum tutup, Alya membeli satu set roti, susu, lilin Rp23.500 dari uang Rp50.000 Pak Wirya. Kembaliannya Rp26.500 dia simpan untuk ongkos ojek pulang pukul 02.14."

    menu:
        "Pergi pukul 02.14, setelah membersihkan jejak di gudang.":
            if bukti_buku_1998 and bukti_mesin_lama and tanya_pak_wirya:
                jump ending_a
            else:
                jump ending_b

        "Pergi pukul 02.14, tapi tanpa semua bukti.":
            jump ending_b

        "Tidak pergi, tetap di kos.":
            jump ending_b

        "Pergi pukul 02.14 tanpa membersihkan jejak di gudang.":
            if hide_count >= 2 and not lapor_bu_ratna:
                jump ending_d
            else:
                "Alya pernah melapor ke Bu Ratna — dia dilindungi. Pilihan ceroboh ini tidak berujung pemindahan."
                jump ending_b

# ============================================================
# ENDING
# ============================================================
label ending_a:
    scene bg petak_tanah
    "Pukul 02.14. Bukan di dalam toko — toko sudah tutup sejak jam sepuluh, seperti seharusnya."
    "Di luar, di petak tanah kosong di belakang toko, di tempat seorang istri pernah menunggu suaminya pulang dari pasar."
    "Alya tidak melihat apa-apa. Tidak ada hantu. Hanya lilin yang menyala sebentar, lalu padam ditiup angin."
    "Esok paginya, tidak ada lagi struk aneh di meja kasir. Dan pukul 21.14, pintu toko tidak lagi berbunyi untuk Pak Wirya."
    "Tapi Alya tetap menoleh setiap jam itu. Bukan karena takut. Karena rindu pada seseorang yang bahkan bukan miliknya."
    "— Ending A: Pesanan Dituntaskan (True Ending) —"
    "SegarMart Antapani tutup pukul 22.00. Selalu. Dan pukul 21.14, Alya masih selalu menyiapkan satu roti, satu susu, satu lilin — untuk berjaga-jaga."
    return

label ending_b:
    scene bg hitam
    "— Ending B: Tenang — Berhenti Menyelidiki —"
    "SegarMart Antapani tutup pukul 22.00. Selalu. Dan pukul 21.14, Alya masih selalu menyiapkan satu roti, satu susu, satu lilin — untuk berjaga-jaga."
    return

label ending_c:
    scene bg hitam
    "— Ending C: Salah Tuduh —"
    "Tuduhan tanpa bukti lengkap merusak hubungan Alya dengan orang yang sebenarnya membantunya. Misteri tidak terjawab."
    "SegarMart Antapani tutup pukul 22.00. Selalu."
    return

label ending_d:
    scene bg hitam
    "— Ending D: Dipindah Cabang —"
    "Alya pergi tanpa membersihkan jejak. Buku 1998 terbuka, mesin lama menyala. Bu Ratna melaporkannya ke area manager."
    "Misteri tak terjawab."
    return
