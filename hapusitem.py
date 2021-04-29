from ubahdata import split
from ubahdata import savenewdata

def hapusitem():
    gadget = open("gadget.csv", "r")
    g = gadget.readlines()
    gadget.close()

    consumable = open("consumable.csv", "r")
    c = consumable.readlines()
    consumable.close()

    data_gadget = split(g)
    data_consumable = split(c)

    id = input("Masukkan ID item: ")

    index = 0
    exist = False
    if (id[0] == 'G'):
        for i in range(len(data_gadget)):
            if (data_gadget[i][0] == id):
                index = i
                exist = True
            
        if (exist == True):
            checkhapus(data_gadget, index)

    elif (id[0] == 'C'):
        for i in range(len(data_consumable)):
            if (data_consumable[i][0] == id):
                index = i
                exist = True
            
        if (exist == True):
            checkhapus(data_consumable, index)
    else:
        print("Tidak ada item dengan ID tersebut.")
    
    gadget = open("gadget.csv", "w")
    gadget.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
    savenewdata(data_gadget,gadget)

    consumable = open("consumable.csv", "w")
    consumable.write("id;nama;deskripsi;jumlah;rarity\n")
    savenewdata(data_consumable,consumable)
 
def checkhapus(data, index):
    ans = input("Apakah anda yakin ingin menghapus " + str(data[index][1]) + "(Y/N)? ")
    if (ans == 'Y') or (ans == 'y'):
        data.pop(index)
        print("\nItem telah berhasil dihapus dari database.")
    elif (ans == 'N') or (ans == 'n'):
        print("\nItem gagal dihapus dari database")
    else: #Jika diberi input selain Y dan N
        print("Input invalid")
