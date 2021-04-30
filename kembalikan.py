from ubahdata import split
from ubahdata import savenewdata

import math
import time 
import datetime

waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")
active_user = "Admin"


def kembalikan():
    gadget = open("gadget.csv","r")
    g = gadget.readlines()
    gadget.close()

    gadget_borrow_history = open("gadget_borrow_history.csv",'r')
    b = gadget_borrow_history.readlines()
    gadget_borrow_history.close()
    
    gadget_return_history = open("gadget_return_history.csv",'r')
    r = gadget_return_history.readlines()
    gadget_return_history.close()

    data_gadget = split(g)
    for data in data_gadget:
        data[3] = int(data[3])

    data_gadget_borrow_history = split(b)
    data_gadget_return_history = split(r)

    # Mengecek apakah user pernah meminjam barang atau tidak
    for i in range (len(data_gadget_borrow_history)):
        if (active_user in data_gadget_borrow_history[i][1]):
            print("Catatan peminjaman gadget Anda")
            for i in range (len(data_gadget_borrow_history)):
                if (active_user == data_gadget_borrow_history[i][1]):
                    print(data_gadget_borrow_history[i][0:4])  
                    
            # Meminta input barang apa yang ingin dikembalikan        
            id = input("Masukkan ID gadget yang ingin dikembalikan : ")
            
            # Mencari indeks barang yang dituju
            indeks = -1              
            for i in range (len(data_gadget)):
                if (id == data_gadget[i][0]):
                    indeks = i
                    break
                
            # Mencari indeks untuk mengubah jumlah stok_user di gadget_borrow_history_matrix_history.csv    
            idx = -1          
            for i in range (len(data_gadget_borrow_history)):
                if (active_user == data_gadget_borrow_history[i][1] and id == data_gadget_borrow_history[i][2]):
                    idx = i
                    break
            
            if (indeks != -1 and idx != -1):
                # Proses untuk menghitung seberapa banyak barang user telah meminjam sehingga tidak berlebihan ketika ingin mengembalikan
                stok_user = int(data_gadget_borrow_history[idx][5])

                print("Stok gadget yang Anda miliki : ", stok_user)
                
                #BONUS 2
                if (stok_user != 0): 
                    kembali_berapa = int(input("Berapa banyak gadget yang ingin dikembalikan : "))
                    
                    if (1 <= kembali_berapa <= stok_user):
                        data_gadget[indeks][3] = data_gadget[indeks][3] + kembali_berapa
                        print("Gadget", data_gadget[indeks][1], "sebanyak", kembali_berapa, "telah dikembalikan.")
                        data_gadget_borrow_history[idx][5] = stok_user - kembali_berapa

                        g = open("gadget.csv",'w')
                        g.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan\n")
                        savenewdata(data_gadget,g)

                        b = open("gadget_borrow_history.csv",'w')
                        b.write("id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;stok_user\n")
                        savenewdata(data_gadget_borrow_history,b)

                        r = open("gadget_return_history.csv",'a+')
                        r.write(f"\n{len(data_gadget_return_history)+1};{active_user};{id};{tanggal};{kembali_berapa}")
                        r.close()
                        
                    elif (kembali_berapa >= stok_user):
                        print("Input berlebih.")
                        
                    else:
                        print("Input harus >0.")
                    break
                else:
                    print("Anda sudah tidak memiliki gadget ini.")
                break
            else:
                print("Anda tidak memiliki Gadget ini.")
    else:
        print("Anda tidak pernah meminjam gadget!")