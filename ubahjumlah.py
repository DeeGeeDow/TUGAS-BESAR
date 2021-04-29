# Program ubahjumlah.py
# menambah atau mengurangi gadget/consumable yang terdaftar

# KAMUS 
# variabel
# fungsi dan prosedur
def ubahjumlah():
# I.S. gadget/consumable belum ditambah/dikurangi
# F.S. gadget/consumable sudah ditambah/dikurangi
# KAMUS LOKAL
# gadget : seqfile of gadget.csv
# consumable : seqfile of consumable.csv
# ALGORITMA PROSEDUR
    gadget = open("gadget.csv","r")
    g = gadget.readlines()
    gadget.close()
    
    consumable = open("consumable.csv",'r')
    c = consumable.readlines()
    consumable.close()

    data_gadget = []
    for i in range(1, len(g)):
        new_arr = []
        cc = ''
        for j in (g[i]):
            if (j == ";"):
                new_arr.append(cc)
                cc = ''
            else:
                cc += j
        if cc:
            new_arr.append(cc)
        arr_data = [data.strip() for data in new_arr]
        data_gadget.append(arr_data)

    for data in data_gadget:
        data[3] = int(data[3])

    data_consumable = []
    for i in range(1, len(c)):
        new_arr = []
        cc = ''
        for j in (c[i]):
            if (j == ";"):
                new_arr.append(cc)
                cc = ''
            else:
                cc += j
        if cc:
            new_arr.append(cc)
        arr_data = [data.strip() for data in new_arr]
        data_consumable.append(arr_data)

    for data in data_consumable:
        data[3] = int(data[3])

    id = input("Masukan ID : ")
    jumlah = int(input("Masukkan jumlah : "))

    index = -1
    if id[0] == 'G':
        for i in range(len(data_gadget)):
            if data_gadget[i][0] == id:
                index = i

    elif id[0] == 'C':
        for i in range(len(data_consumable)):
            if data_consumable[i][0] == id:
                index = i


    if index == -1:
        print("Tidak ada item dengan ID tersebut")
    else:
        if id[0] == 'G':
            if data_gadget[index][3] + jumlah < 0:
                print(f"{-1*jumlah} {data_gadget[index][1]} gagal dibuang karena stok kurang. Stok sekarang : {data_gadget[index][3]} (<{-1*jumlah})")
            else:
                data_gadget[index][3] += jumlah
                if jumlah < 0:
                    print(f"{-1*jumlah} {data_gadget[index][1]} berhasil dibuang. Stok sekarang : {data_gadget[index][3]}")
                elif jumlah > 0:
                    print(f"{jumlah} {data_gadget[index][1]} berhasil ditambahkan. Stok sekarang : {data_gadget[index][3]}")
                else:
                    print(f"Tidak terjadi penambahan atau pengurangan {data_gadget[index][1]}. Stok sekarang : {data_gadget[index][3]}") 
        if id[0] == 'C':
            if data_consumable[index][3] + jumlah < 0:
                print(f"{-1*jumlah} {data_consumable[index][1]} gagal dibuang karena stok kurang. Stok sekarang : {data_consumable[index][3]} (<{-1*jumlah})")
            else:
                data_consumable[index][3] += jumlah
                if jumlah < 0:
                    print(f"{-1*jumlah} {data_consumable[index][1]} berhasil dibuang. Stok sekarang : {data_consumable[index][3]}")
                elif jumlah > 0:
                    print(f"{jumlah} {data_consumable[index][1]} berhasil ditambahkan. Stok sekarang : {data_consumable[index][3]}")
                else:
                    print(f"Tidak terjadi penambahan atau pengurangan {data_consumable[index][1]}. Stok sekarang : {data_consumable[index][3]}")

    g = open("gadget.csv",'w')
    g.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
    for data in data_gadget:
        for i in range(len(data)):
            g.write(str(data[i]))
            if i!=len(data)-1:
                g.write(";")
            else:
                g.write("\n")

    c = open("consumable.csv",'w')
    c.write("id;nama;deskripsi;jumlah;rarity\n")
    for data in data_consumable:
        for i in range(len(data)):
            c.write(str(data[i]))
            if i!=len(data)-1:
                c.write(";")
            else:
                c.write("\n")