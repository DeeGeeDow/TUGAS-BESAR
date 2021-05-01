from load import load

def hapusitem():

    id = input("Masukkan ID item: ")

    index = 0
    exist = False
    if (id[0] == 'G'):
        for i in range(len(load.data_gadget)):
            if (load.data_gadget[i][0] == id):
                index = i
                exist = True
            
        if (exist == True):
            checkhapus(load.data_gadget, index)

    elif (id[0] == 'C'):
        for i in range(len(load.data_consumable)):
            if (load.data_consumable[i][0] == id):
                index = i
                exist = True
            
        if (exist == True):
            checkhapus(load.data_consumable, index)
    else:
        print("Tidak ada item dengan ID tersebut.")
    
 
def checkhapus(data, index):
    ans = input("Apakah anda yakin ingin menghapus " + str(data[index][1]) + "(Y/N)? ")
    if (ans == 'Y') or (ans == 'y'):
        data.pop(index)
        print("\nItem telah berhasil dihapus dari database.")
    elif (ans == 'N') or (ans == 'n'):
        print("\nItem gagal dihapus dari database")
    else: #Jika diberi input selain Y dan N
        print("Input invalid")
