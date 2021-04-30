# Spesifikasi instruction sistem tiap program
F01 = "register - untuk melakukan registrasi user baru"
F02 = "login - untuk melakukan login ke dalam sistem"
F03 = "carirarity - untuk melakukan pencarian gadget dengan rarity tertentu"
F04 = "caritahun - untuk melakukan pencarian gadget berdasarkan tahun ditemukan"
F05 = "tambahitem - untuk melakukan penambahan item ke dalam inventori"
F06 = "hapusitem - untuk melakukan penghapusan item pada inventori gadget atau consumable"
F07 = "ubahjumlah - untuk melakukan perubahan jumlah gadget dan consumable dalam inventori sistem"
F08 = "pinjam - untuk melakukan peminjaman gadget yang terdapat dalam inventori"
F09 = "kembalikan - untuk melakukan pengembalian gadget yang dipinjam secara seutuhnya"
F10 = "minta - untuk melakukan pengambilan consumable yang tersedia"
F11 = "riwayatpinjam - untuk memperlihatkan riwayat peminjaman gadget"
F12 = "riwayatkembali - untuk memperlihatkan riwayat pengembalian gadget"
F14 = "loaddata - untuk melakukan loading data ke dalam sistem"
F13 = "riwayatambil - untuk memperlihatkan riwayat pengambilan consumable"
F15 = "save - untuk melakukan penyimpanan perubahan data ke dalam file"
F16 = "help - untuk memberikan panduan penggunaan sistem"
F17 = "exit - untuk keluar dari sistem/aplikasi"


def help_admin():
    # Sebagai admin
    print("============ HELP ============")
    print(F01,F02,F03,F04,F05,F06,F07,F11,F12,F13,F14,F15,F16,F17, sep="\n")
    print()

def help_user():
    # Sebagai user
    print("============ HELP ============")
    print(F02,F03,F04,F08,F09,F10,F14,F15,F16,F17, sep="\n")
    print()

def help_general():
    # Pengguna menggunakan help tanpa login
    print("============ HELP ============")
    print(F02,F14,F17, sep="\n")
    print()
