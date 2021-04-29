def search_rar():
    f = open("gadget.csv", "r")
    lines = f.readlines()
    f.close()
    
    req = input("Masukkan rarity: ")

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

    state = True
    print("\nHasil pencarian: ")
    for i in range (len(data)):
        if (data[i][4] == req):
            state = False
            print("\nNama            :", data[i][1])
            print("Deskripsi       :", data[i][2])
            print("Jumlah          :", data[i][3])
            print("Rarity          :", data[i][4])
            print("Tahun Ditemukan :", data[i][5])
    if state:
        print("\nTidak ditemukan gadget dengan rarity", req)

