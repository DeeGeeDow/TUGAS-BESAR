from load import load
# Menerima input ID untuk consumable dan gadget dari user 
id = input("Masukan ID: ")

# Melakukan validasi masukan
if id[0] == 'G':
    for row in range(len(load.data_gadget)):
        if id == load.data_gadget[row][0]:
            print("Gagal menambah item karena ID sudah ada")
            break
    
elif id[0] == 'C':
    for row in range(len(load.data_consumable)):
        if id == load.data_consumable[row][0]:
            print("Gagal menambah item karena ID sudah ada")
            break
else: 
    print("Gagal menambah item karena ID tidak valid")