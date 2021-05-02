from load import load
from login import login

import math
import time 
import datetime

waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")
active_user_id = login.id_user

def pinjam():
    for data in load.data_gadget:
        data[3] = int(data[3])

    id = input("Masukkan ID item : ")
    indeks = -1
    # Mencari Indeks yang dituju
    for i in range(len(load.data_gadget)):
        if (id == load.data_gadget[i][0]):
            indeks = i
            break
        
    if (indeks != -1):
        for i in range (len(load.data_gadget_borrow_history)):
            if (active_user_id == load.data_gadget_borrow_history[i][1] and id == load.data_gadget_borrow_history[i][2]):
                print("Anda sudah pernah meminjam gadget ini")
                break
            
        else:    
            print("Stok yang tersedia :", load.data_gadget[indeks][3])              
            jumlah = int(input("Jumlah peminjaman : "))
            # Pengambilan stok barang setelah tahu indeks gadget yang diinginkan oleh user                    
            if (jumlah <= load.data_gadget[indeks][3]):
                data_gadget[indeks][3] = load.data_gadget[indeks][3] - jumlah
                print("Item", load.data_gadget[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
            else:
                print("Jumlah peminjaman terlalu banyak")
            stok_user = jumlah

            load.data_gadget_borrow_history.append([len(load.data_gadget_borrow_history)+1, active_user_id, id, tanggal, jumlah, stok_user])
    else:
        print("Gadget tidak ditemukan.")
