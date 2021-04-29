def carirarity():
    f = open("gadget.csv", "r")
    lines = f.readlines()
    f.close()
    
    req = input("Masukkan rarity: ")
    
    data_gadget = data_split(lines)

    state = True
    print("\nHasil pencarian: ")
    for i in range (len(data_gadget)):
        if (data_gadget[i][4] == req):
            state = False
            print("\nNama            :", data_gadget[i][1])
            print("Deskripsi       :", data_gadget[i][2])
            print("Jumlah          :", data_gadget[i][3])
            print("Rarity          :", data_gadget[i][4])
            print("Tahun Ditemukan :", data_gadget[i][5])
    if state:
        print("\nTidak ditemukan gadget dengan rarity", req)

def data_split(line):
    data = []
    for i in range(1, len(lines)):
        new_arr = []
        cc = ''
        for j in (lines[i]):
            if (j == ";"):
                new_arr.append(cc)
                cc = ''
            else:
                cc += j
        if cc:
            new_arr.append(cc)
        arr_data = [data.strip() for data in new_arr]
        data.append(arr_data)
    return data
