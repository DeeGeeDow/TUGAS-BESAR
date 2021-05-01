def riwayatkembali():
    f = open("gadget_return_history.csv", "r")
    re = f.readlines()
    f.close()

    f = open("gadget_borrow_history.csv", "r")
    bo = f.readlines()
    f.close()

    f =  open("gadget.csv", "r")
    gadget = f.readlines()
    f.close()

    f =  open("user.csv", "r")
    user = f.readlines()
    f.close()

    id_nama = []
    nama = []
    for i in range(1, len(user)):
        new_file = []
        kata = ''
        for j in (user[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        nama.append(array[1])
        id_nama.append(array[0])

    id_gadget = []
    nama_gadget = []
    for i in range(1, len(gadget)):
        new_file = []
        kata = ''
        for j in (gadget[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        nama_gadget.append(array[1])
        id_gadget.append(array[0])
    
    id_peminjaman = []
    id_peminjam = []
    id_gad = []
    for i in range(1, len(bo)):
        new_file = []
        kata = ''
        for j in (bo[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        id_peminjaman.append(array[0])
        id_peminjam.append(array[1])
        id_gad.append(array[2])
    
    data = []
    tanggal = []
    for i in range(1, len(re)):
        new_file = []
        kata = ''
        for j in (re[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        data.append(array)
        tanggal.append(array[2])

    tanggal_baru = sort_tanggal(tanggal)

    tanggal_lama = []
    for i in data:
        tanggal_lama.append(i[2])

    entry = tanggal_baru[0:6]
    
    for item in entry:
        ind = tanggal_lama.index(item)
        a = id_peminjaman.index(data[ind][1])
        print("ID Pengembalian      :", data[ind][0])
        print("Nama Pengambil       :", nama[id_nama.index(id_peminjam[a])])
        print("Nama Gadget          :", nama_gadget[id_gadget.index(id_gad[a])])
        print("Tanggal Pengembalian :", data[ind][2])
        print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        entry = tanggal_baru[6:11]
        for item in entry:
            ind = tanggal_lama.index(item)
            a = id_peminjaman.index(data[ind][1])
            print("ID Pengembalian      :", data[ind][0])
            print("Nama Pengambil       :", nama[id_nama.index(id_peminjam[a])])
            print("Nama Gadget          :", nama_gadget[id_gadget.index(id_gad[a])])
            print("Tanggal Pengembalian :", data[ind][2])
            print()
    else:
        print()

def sort_tanggal(raw):
    for i in range(0, len(raw)):
        for j in range(0, len(raw)-i-1):
            # Urutkan tahun dari yang terbesar
            if (raw[j][6:] < raw[j + 1][6:]):
                temp = raw[j]
                raw[j]= raw[j + 1]
                raw[j + 1]= temp
            # Jika tahunnya sama, urutkan bulan dari yang terbesar
            elif (raw[j][6:] == raw[j + 1][6:]):
                if (raw[j][2:5] < raw[j + 1][2:5]):
                    temp = raw[j]
                    raw[j]= raw[j + 1]
                    raw[j + 1]= temp
                # Jika bulannya sama, urutkan tanggal dari yang terbesar
                elif (raw[j][2:5] == raw[j + 1][2:5]):
                    if (raw[j][:2] < raw[j + 1][:2]):
                        temp = raw[j]
                        raw[j]= raw[j + 1]
                        raw[j + 1]= temp
    return(raw)