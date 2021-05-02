from load import load
def riwayatambil():
    data_consumable_history = load.data_consumable_history
    data_consumable_history = sort_tanggal(data_consumable_history,3)

    id_user = [data[0] for data in load.data_user]
    id_co = [data[0] for data in load.data_consumable]
    tanggal = [data[3] for data in load.data_consumable_history]

    for ind in range(5):
        if ind < len(data_consumable_history):
            print("ID Pengambilan       :", data_consumable_history[ind][0])
            print("Nama Pengambil       :", load.data_user[id_user.index(data_consumable_history[ind][1])][1])
            print("Nama Consumable      :", load.data_consumable[id_co.index(data_consumable_history[ind][2])][1])
            print("Tanggal Pengambilan  :", data_consumable_history[ind][3])
            print("Jumlah               :", data_consumable_history[ind][4])
            print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        if len(data_consumable_history) <= 5:
            print("Tidak ada riwayat lain\n")
        else:
            for ind in range(5,10):
                if ind < len(data_consumable_history):
                    print("ID Pengambilan       :", data_consumable_history[ind][0])
                    print("Nama Pengambil       :", load.data_user[id_user.index(data_consumable_history[ind][1])][1])
                    print("Nama Consumable      :", load.data_consumable[id_co.index(data_consumable_history[ind][2])][1])
                    print("Tanggal Pengambilan  :", data_consumable_history[ind][3])
                    print("Jumlah               :", data_consumable_history[ind][4])
                    print()
    else:
        print()

def sort_tanggal(raw,index_tanggal):
    for i in range(0, len(raw)):
        for j in range(0, len(raw)-i-1):
            # Urutkan tahun dari yang terbesar
            if (raw[j][index_tanggal][6:] < raw[j + 1][index_tanggal][6:]):
                temp = raw[j]
                raw[j]= raw[j + 1]
                raw[j + 1]= temp
            # Jika tahunnya sama, urutkan bulan dari yang terbesar
            elif (raw[j][index_tanggal][6:] == raw[j + 1][index_tanggal][6:]):
                if (raw[j][index_tanggal][2:5] < raw[j + 1][index_tanggal][2:5]):
                    temp = raw[j]
                    raw[j]= raw[j + 1]
                    raw[j + 1]= temp
                # Jika bulannya sama, urutkan tanggal dari yang terbesar
                elif (raw[j][index_tanggal][2:5] == raw[j + 1][index_tanggal][2:5]):
                    if (raw[j][index_tanggal][:2] < raw[j + 1][index_tanggal][:2]):
                        temp = raw[j]
                        raw[j]= raw[j + 1]
                        raw[j + 1]= temp
    return(raw)
