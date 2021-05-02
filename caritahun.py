from carirarity import outputGadget
from load import load

def caritahun():
    data_gadget = load.data_gadget
    print()
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian:")
    print()

    data_kategori = ['<', '>', '>=', '<=', '=']
    data_tahun = []
    for data in data_gadget:
        data_tahun.append(data[5])
    data_tahun = [int(i) for i in data_tahun]

    # Memvalidasi input
    if (tahun > 999) & (kategori in data_kategori):
        if (kategori == '='):
            ind = data_tahun.index(tahun)
            outputGadget(data_gadget,ind)
        elif (kategori == '<'):
            for item in data_tahun:
                if item < tahun:
                    ind = data_tahun.index(item)
                    outputGadget(data_gadget,ind)
                    print()
        elif (kategori == '>'):
            for item in data_tahun:
                if item > tahun:
                    ind = data_tahun.index(item)
                    outputGadget(data_gadget,ind)
                    print()
        elif (kategori == '<='):
            for item in data_tahun:
                if item <= tahun:
                    ind = data_tahun.index(item)
                    outputGadget(data_gadget,ind)
                    print()
        elif (kategori == '>='):
            for item in data_tahun:
                if item >= tahun:
                    ind = data_tahun.index(item)
                    outputGadget(data_gadget,ind)
                    print()
    else:
        print("Tidak ada gadget yang ditemukan")