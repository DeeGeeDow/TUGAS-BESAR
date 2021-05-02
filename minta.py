from load import load
from login import login
import datetime

# Program minta.py
# program untuk meminta consumable

# KAMUS
def minta():
# I.S. command minta dipanggil
# F.S. user/admin berhasil meminta consumable jika masukan valid

# KAMUS LOKAL
    data_id_consumable = [data[0] for data in load.data_consumable]
    # id_item : string = id dari item yg diminta
    # tanggal : string = tanggal hari ini
    # jumlah : int = jumlah item yg diminta
    # index_consumable : int = index dari item yg diminta pada data_consumable

# ALGORITMA PROSEDUR
    # tanggal hari ini
    for data in load.data_consumable:
        data[3] = int(data[3])
    waktu = datetime.date.today()
    tanggal = waktu.strftime("%d/%m/%Y")

    active_user_id = login.id_user
    id_item = input("Masukkan ID item : ")

    index_consumable = -1
    for i in range(len(data_id_consumable)):
        if id_item == data_id_consumable[i]:
            index_consumable = i
    
    if index_consumable != -1:
        jumlah = int(input("Jumlah : "))
        if jumlah > 0:
            if jumlah <= load.data_consumable[index_consumable][3]:
                load.data_consumable[index_consumable][3] -= jumlah
                load.data_consumable_history.append([len(load.data_consumable_history)+1, active_user_id, id_item, tanggal, jumlah])
                print(f"Item {load.data_consumable[index_consumable][1]} (x{jumlah}) berhasil diambil! Stok sekarang : {load.data_consumable[index_consumable][3]}")
            else:
                print("Permintaan terlalu banyak! Stok {load.data_consumable[index_consumable][1]} hanya {load.data_consumable[index_consumable][3]}. ")
        else:
            print("Jumlah harus bilangan bulat positif!")
    else:
        print("ID item tidak ditemukan.")