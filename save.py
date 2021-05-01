import os
from load import load
# PROGRAM save.py
# program untuk menyimpan file penyimpanan di suatu folder

# KAMUS
def save():
# I.S. user/admin memanggil command save
# F.S. 
# Folder penyimpanan dibuat jika belum ada,
# File penyimpanan diuat di folder tersebut jika belum ada, jika sudah ada replace file
# penyimpanan sebelumnya dengan file penyimpanan yang baru.

# KAMUS LOKAL
# nama_folder : string
# folder_path : path
# files_path : array

# ALGORITMA PROSEDUR
    nama_folder = input("Masukkan nama folder penyimpanan : ")
    print("Saving...")

    folder_path = os.path.join("folder_penyimpanan", nama_folder)
    files_path = []
    isDirFound = False
    for (root,dirs,files) in os.walk("folder_penyimpanan"):
        if root == folder_path:
            isDirFound = True
            files_path = files
            break
    
    if not isDirFound:
        os.mkdir(folder_path)
    
    user_path = os.path.join(folder_path,"user.csv")
    f_user = open(user_path,'w')
    f_user.write("id;nama;username;password;alamat;role\n")
    savenewdata(load.data_user, f_user)

    gadget_path = os.path.join(folder_path,"gadget.csv")
    f_gadget = open(gadget_path,'w')
    f_gadget.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
    savenewdata(load.data_gadget, f_gadget)

    consumable_path = os.path.join(folder_path, "consumable.csv")
    f_consumable = open(consumable_path, 'w')
    f_consumable.write("id;nama;deskripsi;jumlah;rarity\n")
    savenewdata(load.data_consumable, f_consumable)

    consumable_history_path = os.path.join(folder_path, "consumable_history.csv")
    f_consumable_history = open(consumable_history_path, 'w')
    f_consumable_history.write("id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah\n")
    savenewdata(load.data_consumable_history, f_consumable_history)

    gadget_borrow_history_path = os.path.join(folder_path, "gadget_borrow_history.csv")
    f_gadget_borrow_history = open(gadget_borrow_history_path, 'w')
    f_gadget_borrow_history.write("id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;stok_user\n")
    savenewdata(load.data_gadget_borrow_history, f_gadget_borrow_history)

    gadget_return_history_path = os.path.join(folder_path, "gadget_return_history.csv")
    f_gadget_return_history = open(gadget_return_history_path, 'w')
    f_gadget_return_history.write("id;id_peminjam;id_gadget;tanggal_pengembalian;kembali_berapa\n")
    savenewdata(load.data_gadget_return_history, f_gadget_return_history)

def savenewdata(data_array, line):
# I.S. data pada data_array akan disimpan di file csv_path
# F.S. data pada data_darray telah disimpan di file csv_path
# KAMUS
# line : seqfile of csv_path

# ALGORITMA PROSEDUR
    for data in data_array:
        for i in range(len(data)):
            line.write(str(data[i]))
            if i!=len(data)-1:
                line.write(";")
            else:
                line.write("\n")
    line.close()
    