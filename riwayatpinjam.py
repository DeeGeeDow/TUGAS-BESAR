from load import load
def riwayatpinjam():
    id_user = [data[0] for data in load.data_user]
    id_gadget = [data[0] for data in load.data_gadget]
    tanggal = [data[3] for data in load.data_gadget_borrow_history]

    tanggal_baru = sort_tanggal(tanggal)
    
    entry = tanggal_baru[0:6]

    for item in entry:
        ind = tanggal.index(item)
        print("ID Peminjaman        :", load.data_gadget_borrow_history[ind][0])
        print("Nama Pengambil       :", load.data_user[id_user.index(load.data_gadget_borrow_history[ind][1])][1])
        print("Nama Gadget          :", load.data_gadget[id_gadget.index(load.data_gadget_borrow_history[ind][2])][1])
        print("Tanggal Peminjaman   :", load.data_gadget_borrow_history[ind][3])
        print("Jumlah               :", load.data_gadget_borrow_history[ind][4])
        print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        entry = tanggal_baru[6:11]
        for item in entry:
            ind = tanggal.index(item)
            print("ID Peminjaman        :", load.data_gadget_borrow_history[ind][0])
            print("Nama Pengambil       :", load.data_user[id_user.index(load.data_gadget_borrow_history[ind][1])][1])
            print("Nama Gadget          :", load.data_gadget[id_gadget.index(load.data_gadget_borrow_history[ind][2])][1])
            print("Tanggal Peminjaman   :", load.data_gadget_borrow_history[ind][3])
            print("Jumlah               :", load.data_gadget_borrow_history[ind][4])
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
