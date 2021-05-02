from load import load
from riwayatambil import sort_tanggal

def riwayatkembali():
    data_gadget_return_history = load.data_gadget_return_history
    data_gadget_return_history = sort_tanggal(data_gadget_return_history,2)
    id_user = [data[0] for data in load.data_user]
    id_gadget = [data[0] for data in load.data_gadget]
    id_peminjaman = [data[0] for data in load.data_gadget_borrow_history]
    tanggal = [data[3] for data in load.data_gadget_return_history]

    
    for ind in range(5):
        if ind < len(data_gadget_return_history):
            a = id_peminjaman.index(data_gadget_return_history[ind][1]) 
            print("ID Pengembalian      :", data_gadget_return_history[ind][0])
            print("Nama Pengambil       :", load.data_user[id_user.index(load.data_gadget_borrow_history[a][1])][1])
            print("Nama Gadget          :", load.data_gadget[id_gadget.index(load.data_gadget_borrow_history[a][2])][1])
            print("Tanggal Pengembalian :", data_gadget_return_history[ind][2])
            print()

    req = input("Apakah Anda ingin melihat 5 riwayat lainnya?(Y/N) ")
    print()
    if (req == 'Y' or 'y'):
        if len(data_gadget_return_history) <= 5:
            print("Tidak ada riwayat lain\n")
        else:
            for ind in range(5,10):
                if ind<len(data_gadget_return_history):
                    a = id_peminjaman.index(data_gadget_return_history[ind][1]) #flag
                    print("ID Pengembalian      :", data_gadget_return_history[ind][0])
                    print("Nama Pengambil       :", load.data_user[id_user.index(data_gadget_return_history[a][1])][1])
                    print("Nama Gadget          :", load.data_gadget[id_gadget.index(data_gadget_return_history[a][2])][1])
                    print("Tanggal Pengembalian :", data_gadget_return_history[ind][2])
                    print()
    else:
        print()
