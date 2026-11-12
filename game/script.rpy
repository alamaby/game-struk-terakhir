## script.rpy — Struk Terakhir Pukul 02.14
## Ren'Py 8.5.3 — Prolog + Chapter 1 + Chapter 2 playable, Chapter 3–5 stub.
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
image dimas serius = Text("DIMAS — serius", size=40, color="#ffffff")

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
# CHAPTER 2 — Selasa: Pelanggan Pukul 21.14
# Durasi target: ~12 menit
# Beat: 2.1 Gudang 15.30 — buku 1998
#       2.2 Menunggu 21.14 — Pilihan 3
#       2.3 Setelah tutup 22.30, warung kopi
# ============================================================
label chapter2:
    scene bg hitam
    "CHAPTER 2 — Selasa: Pelanggan Pukul 21.14"

    # --- Scene 2.1 — Gudang, 15.30, saat toko sepi ---
    scene bg interior_siang
    show alya lelah at center
    "Selasa, 14.00. Shift sore lagi."
    "Semalam Alya hampir tidak tidur. Struk 1998 itu masih di saku seragamnya — atau di tangan Bu Ratna, tergantung apa yang dia lakukan kemarin."
    "Satu hal yang tidak berubah: stok lilin masih kurang satu. Bu Ratna belum menanyakan lagi, tapi Alya tahu pertanyaan itu akan datang."

    if percaya_ujang:
        show ujang serius at center
        ujang "Neng Lya. Toko lagi sepi. Ikut saya ke gudang sebentar."
        alya "Ke gudang, Mang? Ada apa?"
        ujang "Ada yang harus Neng lihat. Soal struk itu."
        "Mang Ujang tidak menunggu jawaban. Dia berjalan ke belakang, dan Alya mengikutinya."
    elif percaya_dimas:
        show dimas serius at center
        dimas "Mbak, aku belum dapat apa-apa. Perpustakaan daerah itu bukanya siang, aku baru bisa ke sana besok. Sabar ya."
        alya "Jadi aku harus nunggu sampai kapan?"
        dimas "Sampai aku dapat kabar. Atau... Mbak coba tanya Mang Ujang. Dia kan sudah lama di sini. Lebih lama dari toko ini."
        "Alya menatap pintu gudang di ujung lorong. Dimas benar. Orang yang paling lama di sini bukan Dimas — Mang Ujang."
        show ujang serius at center
        ujang "Neng mau ke gudang? Saya bukakan. Tapi jangan lama-lama. Bu Ratna bisa nanya."
    else:
        "Alya tidak mengirim foto ke siapa-siapa semalam, dan tidak bertanya ke siapa-siapa pagi ini."
        "Tapi masalah lilin itu tetap ada. Dan struk itu tetap ada."
        "Jam 15.30, saat toko sepi, Alya berjalan sendiri ke pintu gudang."
        show ujang serius at center
        ujang "Neng ngapain di sini?"
        alya "Mang... saya mau lihat gudang. Sebentar saja."
        ujang "Hmm. Ya sudah. Saya temani. Jangan sentuh apa-apa tanpa bilang dulu."

    scene bg gudang
    show alya curiga at center
    "Gudang belakang. Gelap, berdebu, bau kardus basah."
    "Di sudut, di bawah kain, ada bentuk kotak yang Alya kenali samar-samar: mesin kasir tua. Dia belum tahu apa itu — untuk sekarang, dia hanya mencatatnya dalam hati."
    "Mang Ujang menarik sebuah buku catatan dari rak paling bawah. Sampulnya sudah mengelupas, pinggirnya menguning."
    "Tulisan tangan di halaman depannya — Alya membandingkannya dengan struk di sakunya. Sama. Persis sama."

    show ujang serius at center
    ujang "Ini buku almarhumah Bu Lastri. Orang sini memanggilnya Bu Wirya. Dia yang nulis semua pesanan. Roti, susu, lilin. Selalu itu."

    menu:
        "Buka buku itu dan baca halaman pertamanya.":
            $ bukti_buku_1998 = True
            $ ketelitian += 1
            "Alya membuka halaman pertama. Di sana tertulis, dengan tulisan yang sama seperti di struk:"
            "\"Lastri — dipanggil Bu Wirya, mengikuti nama suami saya, Wirya Santoso.\""
            alya "Bu Lastri... istri Pak Wirya?"
            ujang "Iya. Meninggal tahun sembilan delapan. Pas warung ini mau digusur."
            jump ch2_buku_dibaca

        "Jangan sentuh dulu. Tanya Mang Ujang siapa Bu Lastri.":
            $ kepercayaan += 1
            alya "Mang, buku ini punya siapa? Kenapa masih di sini?"
            ujang "Punya Bu Lastri. Istri Pak Wirya. Meninggal tahun sembilan delapan, pas warung ini mau digusur."
            ujang "Halaman pertamanya ada namanya. Baca sendiri, Neng. Saya tidak mau membacakan barang orang mati."
            "Alya membuka halaman pertama. Tertulis: \"Lastri — dipanggil Bu Wirya, mengikuti nama suami saya, Wirya Santoso.\""
            $ bukti_buku_1998 = True
            $ ketelitian += 1
            jump ch2_buku_dibaca

        "Biarkan saja. Jangan sentuh barang orang yang sudah meninggal.":
            "Alya menarik tangannya. Mang Ujang menutup kembali buku itu dan meletakkannya di rak."
            "Bukti itu masih ada di gudang — tapi Alya belum memegangnya. Dia masih bisa kembali di Chapter 4, dengan risiko ketahuan Bu Ratna."
            jump ch2_tanpa_buku

label ch2_buku_dibaca:
    show alya curiga at center
    alya "Mang, dulu Mang kerja apa di warung ini?"
    ujang "Kuli, Neng. Angkut-angkut. Pas jadi minimarket, saya diangkat jadi satpam."
    "Mang Ujang menatap buku itu lama, seperti menatap orang."
    ujang "Jangan dicari, Neng. Ada pesanan yang memang bukan buat orang hidup."
    alya "Tapi Mang, lilin saya kurang satu. Kalau saya tidak bisa menjelaskan, saya yang dicurigai."
    "Mang Ujang tidak menjawab. Dia hanya mengembalikan buku itu ke rak, pelan-pelan, seperti meletakkan sesuatu yang mudah pecah."
    jump ch2_sore

label ch2_tanpa_buku:
    show ujang ragu at center
    ujang "Pintar, Neng. Ada barang yang memang bukan buat dipegang sembarangan."
    "Tapi di wajah Mang Ujang, Alya melihat sesuatu yang lain: lega — dan takut, bersamaan."
    jump ch2_sore

label ch2_sore:
    # --- Scene 2.2 — Menunggu 21.14 ---
    scene bg meja_kasir
    show alya lelah at center
    "20.45. Toko mulai sepi. Alya gelisah sepanjang shift."
    "Setiap kali bel pintu berbunyi, dia menoleh. Bukan. Bukan dia."
    "Jam di dinding kasir bergerak pelan sekali. 20.52. 21.00. 21.07."
    "Alya menghitung dalam hati, tanpa sadar: empat puluh enam menit sebelum tutup. Selalu empat puluh enam menit."
    "21.14."
    "Bel pintu berbunyi."

    show wirya datar at center
    "Pak Wirya masuk, seperti biasa. Roti, susu, lilin."
    "Alya menatap tangannya yang keriput saat dia meletakkan uang pas di meja. Tangan yang sama, yang dulu membawakan roti, susu, dan lilin untuk seseorang yang menunggu jam dua pagi."

    # Pilihan 3 (Chapter 2)
    menu:
        "Tanya langsung: \"Pak, Bapak kenal Bu Lastri?\"":
            $ tanya_pak_wirya = True
            $ keberanian += 1
            alya "Pak... Bapak kenal Bu Lastri?"
            "Pak Wirya terdiam lama. Tangannya berhenti di atas uang kembalian."
            "Lalu, pelan sekali, dia menjawab."
            show wirya sedih at center
            wirya "Dia istri saya."
            "Hanya itu. Tidak ada penjelasan. Tidak ada cerita lanjutan."
            "Tapi bagi Alya, tiga kata itu sudah cukup untuk mengubah segalanya: Pak Wirya bukan orang asing yang kebetulan datang jam segini. Dia datang untuk seseorang."
            jump ch2_malam

        "Ikuti dia pulang setelah toko tutup (22.15, di luar toko).":
            $ keberanian += 2
            "Alya melayani seperti biasa. Senyum kerja. Terima kasih, Pak. Hati-hati di jalan."
            "Tapi begitu rolling door diturunkan, dia tidak langsung pulang."
            scene bg jalan_malam
            show alya curiga at center
            "22.15. Di luar toko, hujan rintik. Alya menjaga jarak, mengikuti dari jauh."
            "Pak Wirya tidak naik angkot. Dia tidak menunggu di halte. Dia berjalan kaki — pelan, tapi pasti — ke arah rumah-rumah di Antapani."
            "Di tengah jalan, dia berhenti. Di petak tanah kosong di belakang toko, di antara gudang dan tembok pembatas. Dia menunduk sebentar, seperti memberi salam kepada seseorang yang tidak terlihat. Lalu lanjut jalan."
            "Alya berdiri di bawah hujan, tidak berani mendekat. Pulang ke kos, bajunya basah, dan dia tahu: besok Bu Ratna bisa saja bertanya kenapa dia pulang telat."
            jump ch2_malam

        "Diam saja, layani seperti biasa.":
            $ ketelitian += 1
            "Alya melayani seperti biasa. Roti, susu, lilin. Rp23.500. Terima kasih, Pak."
            "Tapi kali ini dia memperhatikan — benar-benar memperhatikan."
            "Sebelum keluar, Pak Wirya selalu menatap rak lilin paling bawah. Sekilas saja. Tempat dulu ada foto."
            "Foto siapa? Alya tidak tahu. Tapi dia mencatatnya."
            jump ch2_malam

label ch2_malam:
    # --- Scene 2.3 — Setelah tutup, 22.30, warung kopi ---
    scene bg jalan_malam
    show alya lelah at center
    "22.30. Warung kopi di depan toko. Lampu kuning, bau kopi dan gorengan."
    "Alya duduk, memesan teh hangat. Dia butuh seseorang untuk bicara — atau setidaknya, seseorang yang mau mendengar."

    if percaya_dimas:
        show dimas serius at center
        dimas "Mbak, aku sudah tanya-tanya. Besok aku coba ke perpustakaan daerah, cari arsip koran 1998. Tapi aku tidak janji bisa dapat hari itu juga. Arsip koran itu... ya, Mbak tahu sendiri. Lama."
        alya "Jadi besok pun belum tentu ada jawaban?"
        dimas "Belum tentu. Tapi Mbak, ini penting: kalau memang ada koran 1998 soal warung itu, kita jadi tahu warungnya tutup kenapa. Bukan cuma soal struk."
        "Dimas menyeruput kopinya, lalu menatap Alya serius."
        dimas "Mbak, satu hal. Kalau Mang Ujang bilang yang datang itu bukan orang hidup... jangan langsung percaya. Cari buktinya dulu."
    elif percaya_ujang:
        show ujang ragu at center
        ujang "Neng, saya sudah bilang. Jangan dicari."
        alya "Tapi Mang, saya sudah baca bukunya. Bu Lastri itu istri Pak Wirya, kan?"
        "Mang Ujang menghindari kontak mata. Dia menatap gelas kopinya lama."
        ujang "Neng... ada hal yang lebih baik tidak ditanya. Saya cuma tidak mau toko ini dibilang angker. Saya cuma mau kerja tenang sampai tua."
        "Itu bukan jawaban. Tapi Alya mencatat nada suaranya: bukan takut pada hantu. Takut pada sesuatu yang lain."
    else:
        show dimas antusias at center
        dimas "Mbak Alya! Kok di sini? Aku kira Mbak langsung pulang."
        alya "Aku... butuh udara. Kamu ngapain di sini jam segini?"
        dimas "Nongkrong. Biasa. Eh, Mbak, soal struk itu — aku besok coba ke perpustakaan daerah. Cari arsip koran 1998. Tidak janji dapat, tapi dicoba dulu."
        "Alya mengangguk. Dia tidak bercerita soal buku di gudang. Belum. Dia masih memilih siapa yang bisa dia percaya."

    "Malam itu, di kos, Alya menulis di buku catatannya sendiri — tiga hal yang dia tahu pasti:"
    "Satu: struk itu nyata, tanggal 1998, jam 02.14."
    "Dua: Bu Lastri itu istri Pak Wirya, dan pesanannya selalu roti, susu, lilin."
    "Tiga: Pak Wirya datang jam 21.14, dan dia tidak pernah naik angkot."
    "Besok, Rabu, dia harus memilih: percaya pada siapa?"
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
