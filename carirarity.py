from ubahdata import split

def carirarity():
    f = open("gadget.csv", "r")
    lines = f.readlines()
    f.close()
    
    req = input("Masukkan rarity: ")
    
    data_gadget = split(lines)

    state = True
    print("\nHasil pencarian: ")
    for i in range (len(data_gadget)):
        if (data_gadget[i][4] == req):
            state = False
            output(data_gadget, i)
    if state:
        print("\nTidak ditemukan gadget dengan rarity", req)

def output(data, index):
    print("\nNama            :", data[index][1])
    print("Deskripsi       :", data[index][2])
    print("Jumlah          :", data[index][3])
    print("Rarity          :", data[index][4])
    print("Tahun Ditemukan :", data[index][5])
