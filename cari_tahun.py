import carirarity

def caritahun():
    f =  open("gadget.csv", "r")
    gadget = f.readlines()
    f.close()

    print()
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian:")
    print()

    # Mengubah tanda petik dan enter pada list
    old_lines = [raw_line.replace('"', "") for raw_line in gadget]
    lines = [raw_line.replace("\n", "") for raw_line in old_lines]

    # Mengkonversi baris pada list menjadi array
    data = carirarity.split(lines)
    data_kategori = ['<', '>', '>=', '<=', '=']
    data_tahun = data[5]

    # Memvalidasi input
    if (tahun > 999) & (kategori in data_kategori):
        if (kategori == '='):
            ind = data_tahun.index(tahun)
            print("Nama: ",data[ind][1])
            print("Deskripsi: ",data[ind][2])
            print("Jumlah: ",data[ind][3])
            print("Rarity: ",data[ind][4])
            print("Tahun Ditemukan: ",data[ind][5])
        elif (kategori == '<'):
            for item in data_tahun:
                if item < tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '>'):
            for item in data_tahun:
                if item > tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '<='):
            for item in data_tahun:
                if item <= tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '>='):
            for item in data_tahun:
                if item >= tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
    else:
        print("Tidak ada gadget yang ditemukan")

# Fungsi untuk mengkonversi array menjadi value sebenarnya
def convertArray(array):
    arr = array[:]
    for i in range(6):
        # Untuk kolom indeks ke-5 value sebenarnya adalah integer
        if(i == 5):
            arr[i] = int(arr[i])
    return(arr)
