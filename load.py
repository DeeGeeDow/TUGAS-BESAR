import os
# PROGRAM load.py
# program untuk membuka file-file penyimpanan

# KAMUS

def load(nama_folder):
# I.S. program baru dinyalakan dengan input suatu folder penyimpanan
# F.S. program dapat digunakan, file-file penyimpanan telah disimpan di array-array
# KAMUS
# loading_failed : bool = true jika loading gagal
# isDirFound : bool = True jika folder ditemukan
# data_user, data_gadget, data_consumable, data_consumable_history,
# data_gadget_borrow_history, data_gadget_return_history : array
# ALGORITMA PROSEDUR
    load.loading_failed = False
    load.folder_path = os.path.join("folder_penyimpanan", nama_folder)
    load.files_name = []
    isDirFound = False
    for (root,dirs,files) in os.walk("folder_penyimpanan"):
        if root == load.folder_path:
            isDirFound = True
            load.files_name = files
            break
    
    if not isDirFound:
        print("Folder tidak ditemukan")
        load.loading_failed = True
    else:
        load.data_user = []
        load.data_gadget = []
        load.data_consumable = []
        load.data_consumable_history = []
        load.data_gadget_borrow_history = []
        load.data_gadget_return_history = []

        load_file("user.csv", load.data_user)
        load_file("gadget.csv", load.data_gadget)
        load_file("consumable.csv", load.data_consumable)
        load_file("consumable_history.csv", load.data_consumable)
        load_file("gadget_borrow_history.csv", load.data_gadget_borrow_history)
        load_file("gadget_return_history.csv", load.data_gadget_return_history)

def load_file(file_csv,data_arr):
# I.S. file_csv belum diload
# F.S. file_csv sudah diload ke data_arr jika file_csv ada
# KAMUS LOKAL
# isFileFound : bool = true jika file_csv ada
# f : seqfile of file_csv
# ALGORITMA PROSEDUR
    isFileFound = False
    for file in load.files_name:
        if file == file_csv:
            file_path = os.path.join(load.folder_path, file_csv)
            f = open(file_path,"r")
            line = f.readlines()
            data_arr = split(line)
            print(file_csv + " loaded")
            isFileFound = True
    if not isFileFound:
        print("Failed to load " + file_csv)
        load.loading_failed = True

def split(line):
# mengembalikan data dalam line yang awalnya array of string dengan ';' sebagai pembatas
# menjadi array of array of string dengan array of string
# KAMUS LOKAL
# data : array of array of string
# arr_data = array of string
# ALGORITMA FUNGSI
    data = []
    for i in range(1, len(line)):
        new_arr = []
        cc = ''
        for j in (line[i]):
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