from load import load

def carirarity():
    req = input("Masukkan rarity: ")

    state = True
    print("\nHasil pencarian: ")
    for i in range (len(load.data_gadget)):
        if (load.data_gadget[i][4] == req):
            state = False
            outputGadget(load.data_gadget, i)
    if state:
        print("\nTidak ditemukan gadget dengan rarity", req)

def outputGadget(data, index):
    print("\nNama            :", data[index][1])
    print("Deskripsi       :", data[index][2])
    print("Jumlah          :", data[index][3])
    print("Rarity          :", data[index][4])
    print("Tahun Ditemukan :", data[index][5])
