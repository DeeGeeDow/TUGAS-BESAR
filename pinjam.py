from ubahdata import split
from ubahdata import savenewdata

import math
import time 
import datetime

waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")
active_user = "Admin"

def pinjam():
    gadget = open("gadget.csv","r")
    g = gadget.readlines()
    gadget.close()
    
    gadget_borrow_history = open("gadget_borrow_history.csv",'r')
    b = gadget_borrow_history.readlines()
    gadget_borrow_history.close()

    data_gadget = split(g)
    for data in data_gadget:
        data[3] = int(data[3])

    data_gadget_borrow_history = split(b)

    id = input("Masukkan ID item : ")
    indeks = -1
    # Mencari Indeks yang dituju
    for i in range(len(data_gadget)):
        if (id == data_gadget[i][0]):
            indeks = i
            break
        
    if (indeks != -1):
        for i in range (len(data_gadget_borrow_history)):
            if (active_user == data_gadget_borrow_history[i][1] and id == data_gadget_borrow_history[i][2]):
                print("Anda sudah pernah meminjam gadget ini")
                break
            
        else:    
            print("Stok yang tersedia :", data_gadget[indeks][3])              
            jumlah = int(input("Jumlah peminjaman : "))
            # Pengambilan stok barang setelah tahu indeks gadget yang diinginkan oleh user                    
            if (jumlah <= data_gadget[indeks][3]):
                data_gadget[indeks][3] = data_gadget[indeks][3] - jumlah
                print("Item", data_gadget[indeks][1], "sebanyak", str(jumlah),"telah dipinjam." )
            else:
                print("Jumlah peminjaman terlalu banyak")
            stok_user = jumlah

            # Data untuk merekam peminjaman barang ke gadget_borrow_history.csv
            b = open("gadget_borrow_history.csv",'a+')
            b.write(f"\n{len(data_gadget_borrow_history)+1};{active_user};{id};{tanggal};{jumlah};{stok_user}")
            b.close()

            g = open("gadget.csv",'w')
            g.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
            savenewdata(data_gadget,g)

    else:
        print("Gadget tidak ditemukan.")

pinjam()
