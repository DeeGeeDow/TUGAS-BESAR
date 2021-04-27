def find_rarity(): 
    f =  open("gadget.csv", "r")
    gadget = f.readlines()
    f.close()

    rarity = str(input("Masukkan rarity: "))
    count = 0 
    print("Hasil pencarian: \n") 
    for col in gadget: 
        if col[4] == rarity.upper():
            print("Nama           :    {}".format(col[1]))
            print("Deskripsi      :    {}".format(col[2]))
            print("Jumlah         :    {}".format(col[3]))
            print("Rarity         :    {}".format(col[4]))
            print("Tahun ditemukan:    {}\n".format(col[5]))
            count = count + 1
    if count == 0:
        print("Gadget tidak ditemukan\n")