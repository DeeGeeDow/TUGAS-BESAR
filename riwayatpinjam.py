from load import load
from riwayatambil import sort_tanggal

def riwayatpinjam():
    data_gadget_borrow_history = load.data_gadget_borrow_history
    data_gadget_borrow_history = sort_tanggal(data_gadget_borrow_history,3)
    id_user = [data[0] for data in load.data_user]
    id_gadget = [data[0] for data in load.data_gadget]
    tanggal = [data[3] for data in load.data_gadget_borrow_history]


    for ind in range(5):
        if ind < len(data_gadget_borrow_history):
            print("ID Peminjaman        :", data_gadget_borrow_history[ind][0])
            print("Nama Pengambil       :", load.data_user[id_user.index(data_gadget_borrow_history[ind][1])][1])
            print("Nama Gadget          :", load.data_gadget[id_gadget.index(data_gadget_borrow_history[ind][2])][1])
            print("Tanggal Peminjaman   :", data_gadget_borrow_history[ind][3])
            print("Jumlah               :", data_gadget_borrow_history[ind][4])
            print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        if len(data_gadget_borrow_history)<=5:
            print("Tidak ada riwayat lain\n")
        else:
            for ind in range(5,10):
                if ind < len(data_gadget_borrow_history):
                    print("ID Peminjaman        :", data_gadget_borrow_history[ind][0])
                    print("Nama Pengambil       :", load.data_user[id_user.index(data_gadget_borrow_history[ind][1])][1])
                    print("Nama Gadget          :", load.data_gadget[id_gadget.index(data_gadget_borrow_history[ind][2])][1])
                    print("Tanggal Peminjaman   :", data_gadget_borrow_history[ind][3])
                    print("Jumlah               :", data_gadget_borrow_history[ind][4])
                    print()
    else:
        print()

