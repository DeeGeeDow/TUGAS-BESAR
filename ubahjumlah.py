from load import load

# Program ubahjumlah.py
# menambah atau mengurangi gadget/consumable yang terdaftar

# KAMUS 
# variabel
# fungsi dan prosedur
def ubahjumlah():
# I.S. gadget/consumable belum ditambah/dikurangi
# F.S. gadget/consumable sudah ditambah/dikurangi
# KAMUS LOKAL
# index : int = index barang yg ingin diubah pada file csv (-1 jika tidak ada pada file csv)
# ALGORITMA PROSEDUR
    for data in load.data_gadget:
        data[3] = int(data[3])

    for data in load.data_consumable:
        data[3] = int(data[3])

    id = input("Masukan ID : ")
    jumlah = int(input("Masukkan jumlah : "))

    index = -1
    if id[0] == 'G':
        for i in range(len(load.data_gadget)):
            if load.data_gadget[i][0] == id:
                index = i

    elif id[0] == 'C':
        for i in range(len(load.data_consumable)):
            if load.data_consumable[i][0] == id:
                index = i


    if index == -1:
        print("Tidak ada item dengan ID tersebut")
    else:
        if id[0] == 'G':
            if load.data_gadget[index][3] + jumlah < 0:
                print(f"{-1*jumlah} {load.data_gadget[index][1]} gagal dibuang karena stok kurang. Stok sekarang : {load.data_gadget[index][3]} (<{-1*jumlah})")
            else:
                load.data_gadget[index][3] += jumlah
                if jumlah < 0:
                    print(f"{-1*jumlah} {load.data_gadget[index][1]} berhasil dibuang. Stok sekarang : {load.data_gadget[index][3]}")
                elif jumlah > 0:
                    print(f"{jumlah} {load.data_gadget[index][1]} berhasil ditambahkan. Stok sekarang : {load.data_gadget[index][3]}")
                else:
                    print(f"Tidak terjadi penambahan atau pengurangan {load.data_gadget[index][1]}. Stok sekarang : {load.data_gadget[index][3]}") 
        if id[0] == 'C':
            if load.data_consumable[index][3] + jumlah < 0:
                print(f"{-1*jumlah} {load.data_consumable[index][1]} gagal dibuang karena stok kurang. Stok sekarang : {load.data_consumable[index][3]} (<{-1*jumlah})")
            else:
                load.data_consumable[index][3] += jumlah
                if jumlah < 0:
                    print(f"{-1*jumlah} {load.data_consumable[index][1]} berhasil dibuang. Stok sekarang : {load.data_consumable[index][3]}")
                elif jumlah > 0:
                    print(f"{jumlah} {load.data_consumable[index][1]} berhasil ditambahkan. Stok sekarang : {load.data_consumable[index][3]}")
                else:
                    print(f"Tidak terjadi penambahan atau pengurangan {load.data_consumable[index][1]}. Stok sekarang : {load.data_consumable[index][3]}")
