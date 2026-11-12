## script.rpy — Struk Terakhir Pukul 02.14
## Ren'Py 8.5.3 — Prolog + Chapter 1 + Chapter 2 + Chapter 3 playable, Chapter 4–5 stub.
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
# CHAPTER 3 — Rabu: Dua Versi Cerita
# Durasi target: ~12 menit
# Beat: 3.1 Versi Mang Ujang
#       3.2 Versi Dimas
#       Pilihan 4 — titik cabang utama
#       3.3 CCTV 22.31
#       Akhir: teguran pertama Bu Ratna
# ============================================================
label chapter3:
    scene bg hitam
    "CHAPTER 3 — Rabu: Dua Versi Cerita"

    # --- Scene 3.1 — Versi Mang Ujang ---
    scene bg interior_siang
    show alya curiga at center
    "Rabu pagi. Alya datang lebih awal dari biasanya — bukan untuk shift, tapi untuk satu pertanyaan yang tidak bisa menunggu sampai sore."
    "Kemarin dia sudah tahu dua hal: Bu Lastri itu istri Pak Wirya, dan Pak Wirya datang jam 21.14 bukan karena kebetulan."
    "Hari ini dia harus tahu satu hal lagi: Pak Wirya itu... siapa, sebenarnya?"

    show ujang serius at center
    ujang "Neng Lya. Pagi-pagi sudah di sini."
    alya "Mang, saya mau tanya. Soal Pak Wirya."
    "Mang Ujang menatap sekeliling toko, memastikan tidak ada yang mendengar. Lalu dia mendekat, suaranya turun setengah."
    ujang "Pak Wirya itu sudah tidak ada, Neng. Yang datang tiap malam itu... ya, yang datang itu. Jangan dipanggil namanya keras-keras."

    show alya kaget at center
    alya "Sudah tidak ada? Maksud Mang, Pak Wirya meninggal?"
    ujang "Tahun sembilan delapan. Sama seperti istrinya. Warung ini digusur, mereka berdua... ya, sudah."
    "Alya menatap Mang Ujang. Ada sesuatu yang tidak cocok."
    "Saat bilang itu, Mang Ujang menghindari kontak mata. Tangannya meremas topi satpamnya. Suaranya datar, tapi terlalu datar — seperti orang yang menghafal kalimat, bukan orang yang mengingat."
    alya "Mang, kalau Pak Wirya sudah tidak ada sejak 1998... siapa yang saya layani tiap malam jam 21.14?"
    ujang "Itu yang saya bilang, Neng. Jangan dicari. Ada pesanan yang memang bukan buat orang hidup."

    # --- Scene 3.2 — Versi Dimas ---
    scene bg jalan_malam
    show dimas serius at center
    "Siang itu, Dimas menunggu di depan toko. Di tangannya ada ponsel, layarnya menampilkan sebuah foto."
    dimas "Mbak, lihat ini. Aku foto dari luar pagar panti Lembang."
    "Foto itu: papan pengumuman panti. Daftar penghuni. Di salah satu baris, ada nama yang dicoret."
    dimas "Wirya Santoso. Ada di daftar penghuni 2015 sampai 2019. Lalu dicoret, ada catatan di sampingnya: pindah ke keluarga."
    alya "Jadi dia pernah di panti Lembang?"
    dimas "Pernah. Tapi sudah pindah. Aku tanya satpam pantinya siang tadi — Pak Wirya pindah ke rumah keponakan di Antapani, awal 2020."
    dimas "Lihat, Mbak. Namanya ada di daftar panti, tapi sudah dicoret. Dia pindah. Bukan orang mati. Mang Ujang itu... dia cuma takut toko ini dibilang angker."

    show alya curiga at center
    alya "Terus arsip koran 1998-nya?"
    dimas "Belum. Aku baru bisa ke perpustakaan daerah besok pagi, Kamis. Arsip koran itu tidak bisa didapat dalam satu sore, Mbak. Sabar."
    "Alya tidak menunjukkan foto KTP — karena Dimas memang tidak punya. Yang dia punya hanya foto papan pengumuman dari luar pagar, dan cerita dari satpam panti."
    "Itu bukti publik. Bukan bukti yang bisa didapat begitu saja, tapi juga bukan bukti yang bisa dipalsukan dengan mudah."
    "Dan sekarang Alya punya dua versi cerita yang saling bertentangan."
    "Versi Mang Ujang: Pak Wirya sudah mati sejak 1998."
    "Versi Dimas: Pak Wirya hidup, pernah di panti Lembang, sekarang tinggal di Antapani."
    "Keduanya tidak bisa benar bersamaan."

    # --- Pilihan 4 — titik cabang utama ---
    scene bg kos_alya
    show alya lelah at center
    "Malam itu, di kos, Alya duduk di depan buku catatannya."
    "Dia harus memilih. Bukan karena dia suka memilih — tapi karena besok, Kamis, dia harus bertindak. Dan dia tidak bisa bertindak dengan dua versi cerita di kepala."

    menu:
        "Percaya Mang Ujang.":
            $ percaya_ujang = True
            $ percaya_dimas = False
            $ kepercayaan += 1
            "Alya memilih percaya pada orang yang paling lama di tanah ini."
            "Mang Ujang tahu sejarah warung ini. Dia ada di sana tahun 1998. Kalau dia bilang Pak Wirya sudah tidak ada, mungkin memang begitu — dan yang datang tiap malam adalah sesuatu yang lain."
            "Tapi di sudut hati Alya, ada yang mengganjal: kenapa Mang Ujang menghindari kontak mata saat bilang itu?"
            jump ch3_cctv

        "Percaya Dimas.":
            $ percaya_dimas = True
            $ percaya_ujang = False
            $ kepercayaan += 1
            "Alya memilih percaya pada bukti yang bisa dilihat."
            "Nama Wirya Santoso ada di papan panti, dicoret dengan catatan pindah ke keluarga. Satpam panti mengatakannya sendiri. Itu lebih kuat daripada cerita yang disampaikan sambil menghindari kontak mata."
            "Besok, Dimas mengajaknya ke rumah keponakan Pak Wirya di Antapani — bukan ke panti Lembang, karena Pak Wirya sekarang tinggal di Antapani."
            jump ch3_cctv

        "Percaya keduanya setengah-setengah, cari bukti sendiri.":
            if bukti_buku_1998 and ketelitian >= 2:
                $ percaya_ujang = True
                $ percaya_dimas = True
                $ ketelitian += 1
                "Alya tidak mau memilih. Dia punya buku 1998 di tangannya — tulisan tangan Bu Lastri, pesanan yang selalu sama, dan nama Wirya Santoso di halaman pertama."
                "Buku itu bilang: Bu Lastri itu nyata, pesanannya nyata, dan suaminya nyata."
                "Foto papan panti bilang: Wirya Santoso itu nyata, pernah di panti, lalu pindah ke keluarga."
                "Dua-duanya bisa benar, kalau dibaca dengan cara yang lain: Pak Wirya hidup, tapi dia datang untuk menuntaskan janji ke istrinya yang sudah meninggal."
                "Ini jalur tersulit — Alya harus memegang dua versi sekaligus, tanpa menolak salah satunya. Tapi ini juga jalur yang paling lengkap untuk True Ending."
                jump ch3_cctv
            else:
                "Alya mencoba memegang dua versi sekaligus — tapi dia sadar, buktinya belum cukup."
                "Dia belum membaca buku 1998 dengan teliti, atau dia belum memperhatikan cukup detail untuk menyambungkan keduanya."
                "Kalau dia memaksakan diri sekarang, dia hanya akan bingung sendiri. Dia harus memilih satu sisi dulu."
                jump ch3_pilih_sisi

label ch3_pilih_sisi:
    menu:
        "Percaya Mang Ujang.":
            $ percaya_ujang = True
            $ percaya_dimas = False
            $ kepercayaan += 1
            jump ch3_cctv

        "Percaya Dimas.":
            $ percaya_dimas = True
            $ percaya_ujang = False
            $ kepercayaan += 1
            jump ch3_cctv

label ch3_cctv:
    # --- Scene 3.3 — CCTV 22.31 ---
    scene bg gudang
    show alya curiga at center
    "Rabu siang. Bu Ratna sedang keluar toko."
    "Mang Ujang membuka pintu ruang DVR dengan kuncinya sendiri — diam-diam."
    show ujang ragu at center
    ujang "Jangan bilang-bilang, Neng. Ini bisa jadi masalah buat saya juga. Saya cuma buka sebentar."
    "Alya mengangguk. Dia tahu: kasir tidak boleh mengakses DVR sendiri. Akses hanya lewat kepala toko, atau lewat Mang Ujang yang memegang kunci ruang DVR."
    "Rekaman pertama: CCTV toko SegarMart sendiri. Retensi 14–30 hari, bisa dicek mundur."
    "Setelah 22.00, toko kosong. Tidak ada orang masuk lewat pintu depan. Tidak ada transaksi di kasir."
    "Lampu boleh mati pukul 22.31 — tapi CCTV tidak mati. CCTV di sirkuit terpisah dengan UPS, merekam 24 jam dengan mode infrared. Yang gelap hanya lampunya."
    "Jadi struk 02.14 itu makin mustahil: tidak ada transaksi di kasir setelah 22.00, tapi ada struk yang tercetak jam 02.14."

    if percaya_dimas:
        scene bg jalan_malam
        show dimas serius at center
        "Rekaman kedua: CCTV warung sebelah."
        "Dimas meminta izin ke pemilik warung sebelah Rabu siang. Pemiliknya hanya mengizinkan melihat satu jam rekaman, pukul 22.00–23.00, di tempat, tidak boleh difoto sembarangan."
        "Di rekaman itu, pukul 22.31 — setelah toko tutup — terlihat sosok Pak Wirya berjalan melewati toko, menuju petak tanah kosong di belakang toko, lalu menghilang dari frame."
        "Dia tidak masuk toko. Dia ke tanah bekas warung di belakang."
        $ bukti_cctv_2231 = True
        $ ketelitian += 1
        "Alya mencatat: gudang belakang adalah blind spot. Tidak ada kamera di dalam gudang, hanya 1 kamera lorong yang rusak sejak 2019 dan belum diganti. Di situlah mesin kasir lama berada."
    else:
        "Alya hanya sempat melihat rekaman toko sendiri. Rekaman warung sebelah belum sempat dia lihat — pemiliknya hanya mengizinkan kalau ada yang meminta dengan sopan, dan Alya belum sempat ke sana."
        "Tapi satu hal sudah jelas: tidak ada orang masuk toko setelah 22.00. Kalau ada yang berjalan pukul 22.31, dia berjalan di luar toko — bukan di dalam."

    # --- Akhir Chapter 3 — Teguran pertama Bu Ratna ---
    scene bg interior_siang
    show ratna tegas at center
    "Sore itu, Bu Ratna memanggil Alya ke ruang kepala toko."
    ratna "Saya dengar kamu utak-atik gudang. Saya tegur sekali ini. Sekali lagi, saya laporkan ke area manager."
    "Ini teguran pertama, bukan ancaman pindah langsung. Tapi tekanan naik."
    "Alya harus menjawab — sekarang, di depan Bu Ratna."

    menu:
        "Jujur: saya sedang mencari tahu soal struk dan lilin yang hilang.":
            $ lapor_bu_ratna = True
            $ ketelitian += 1
            ratna "Hmm. Saya catat. Tapi jangan utak-atik gudang tanpa izin lagi. Kalau ada apa-apa, lapor saya dulu."
            "Bu Ratna tidak senang — tapi dia mencatat. Dan laporan itu melindungi Alya: kalau dia pernah melapor, Ending D tidak bisa terjadi padanya."
            jump chapter4

        "Bohong: saya cuma merapikan stok, Bu.":
            $ hide_count += 1
            $ keberanian += 1
            "Alya berbohong. Bu Ratna menatapnya lama, lalu mengangguk pelan — tidak percaya sepenuhnya, tapi tidak mengejar."
            "Alya menyembunyikan penyelidikannya. Sekali lagi. Dan dia tahu, kalau ini terjadi sekali lagi, dia tidak akan punya pelindung."
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
