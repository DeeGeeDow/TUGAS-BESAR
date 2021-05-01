def riwayatambil():
    f = open("consumable_history.csv", "r")
    his = f.readlines()
    f.close()
    
    f =  open("consumable.csv", "r")
    co = f.readlines()
    f.close()

    f =  open("user.csv", "r")
    user = f.readlines()
    f.close()

    id_user = []
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
        id_user.append(array[0])

    id_co = []
    nama_co = []
    for i in range(1, len(co)):
        new_file = []
        kata = ''
        for j in (co[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        nama_co.append(array[1])
        id_co.append(array[0])

    data = []
    tanggal = []
    for i in range(1, len(his)):
        new_file = []
        kata = ''
        for j in (his[i]):
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
        print("ID Pengambilan       :", data[ind][0])
        print("Nama Pengambil       :", nama[id_user.index(data[ind][1])])
        print("Nama Consumable      :", nama_co[id_co.index(data[ind][2])])
        print("Tanggal Pengambilan  :", data[ind][3])
        print("Jumlah               :", data[ind][4])
        print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        entry = tanggal_baru[6:11]
        for item in entry:
            ind = tanggal_lama.index(item)
            print("ID Pengambilan       :", data[ind][0])
            print("Nama Pengambil       :", nama[id_user.index(data[ind][1])])
            print("Nama Consumable      :", nama_co[id_co.index(data[ind][2])])
            print("Tanggal Pengambilan  :", data[ind][3])
            print("Jumlah               :", data[ind][4])
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

riwayatambil()