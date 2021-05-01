import ubahdata as ud
from load import load

# Skema pengecekan apakah id gadget atau id consumable bisa dipakai atau belum
def isID_avail(id, data):
    for row in range(len(data)):
            if id == data[row][0]:
                return False
    return True

# Skema validasi rarity
def isRarityValid(rarity):
    if rarity in ["S", "A", "C", "B"]:
        return True
    else: 
        return False

def sortID(data):
    return(data[0])

def tambahitem():    
    # Membaca data dari fungsi load 
    data_gadget = load.data_gadget
    data_consumable = load.data_consumable
    
    # Menerima input ID untuk consumable dan gadget dari user 
    id = input("Masukan ID: ")
    id = id.upper()

    # Melakukan validasi masukan
    if id[0] == 'G':
        if isID_avail(id, data_gadget): 
            G_name = str(input("Masukan Nama: "))
            G_desc = str(input("Masukan Deskripsi: "))
            G_quant = int(input("Masukan Jumlah: "))        
            G_rarity = str(input("Masukan Rarity: "))
            G_rarity = G_rarity.upper()
            if isRarityValid(G_rarity):
                G_year = int(input("Masukan tahun ditemukan: "))
                new_G = [id, G_name, G_desc, G_quant, G_rarity, G_year]
                data_gadget.append(new_G)
                data_gadget.sort(key=sortID)
                # Menulis ulang file gadget dengan entry baru
                gadget = open("gadget.csv", "w")
                gadget.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
                print()
                print("Item berhasil ditambahkan ke database")
            else: 
                print("Input rarity tidak valid")
        else:
            print("Gagal menambahkan item karena ID sudah ada.")
        
    elif id[0] == 'C':
        if isID_avail(id, data_consumable): 
            C_name = str(input("Masukan Nama: "))
            C_desc = str(input("Masukan Deskripsi: "))
            C_quant = int(input("Masukan Jumlah: "))        
            C_rarity = str(input("Masukan Rarity: "))
            C_rarity = C_rarity.upper()
            if isRarityValid(C_rarity):
                new_C = [id, C_name, C_desc, C_quant, C_rarity]
                data_consumable.append(new_C)
                data_consumable.sort(key=sortID)
                # Menulis ulang file gadget dengan entry baru
                consumable = open("consumable.csv", "w")
                consumable.write("id;nama;deskripsi;jumlah;rarity\n")
                print()
                print("Item berhasil ditambahkan ke database")
            else: 
                print("Input rarity tidak valid")
        else:
            print("Gagal menambahkan item karena ID sudah ada.")   
    else: 
        print("Gagal menambah item karena ID tidak valid")