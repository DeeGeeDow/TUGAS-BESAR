import ubahdata as ud

# Membaca file gadget dan consumable dan menyimpannya dalam variabel
gadget = open("gadget.csv", "r")
g = gadget.readlines()
gadget.close()

consumable = open("consumable.csv", "r")
c = consumable.readlines()
consumable.close()

# Melakukan parsing csv dengan menggunakan fungsi split buatan 
data_gadget = ud.split(g)
data_consumable = ud.split(c)

# Menerima input ID untuk consumable dan gadget dari user 
id = input("Masukan ID: ")

# Melakukan validasi masukan
if id[0] == 'G':
    for row in range(len(data_gadget)):
        if id == data_gadget[row][0]:
            print("Gagal menambah item karena ID sudah ada")
            break
    
elif id[0] == 'C':
    for row in range(len(data_consumable)):
        if id == data_consumable[row][0]:
            print("Gagal menambah item karena ID sudah ada")
            break
else: 
    print("Gagal menambah item karena ID tidak valid")