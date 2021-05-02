from load import load
from login import login
import math
import time 
import datetime

waktu = datetime.date.today()
tanggal = waktu.strftime("%d/%m/%Y")


def kembalikan():
    active_user_id = login.id_user
    for data in load.data_gadget:
        data[3] = int(data[3])

    # Mengecek apakah user pernah meminjam barang atau tidak
    for i in range (len(load.data_gadget_borrow_history)):
        if (active_user_id in load.data_gadget_borrow_history[i][1]):
            print("Catatan peminjaman gadget Anda")
            count = 0
            data_id_gadget = [data[0] for data in load.data_gadget]
            for i in range (len(load.data_gadget_borrow_history)):
                if (active_user_id == load.data_gadget_borrow_history[i][1]):
                    count += 1
                    gadget_idx = data_id_gadget.index(load.data_gadget_borrow_history[i][2])
                    print(f"{count}. ({load.data_gadget_borrow_history[i][2]}) {load.data_gadget[gadget_idx][1]} (x{load.data_gadget_borrow_history[gadget_idx][-1]})")  
                    
            # Meminta input barang apa yang ingin dikembalikan        
            id = input("Masukkan ID gadget yang ingin dikembalikan : ")
            
            # Mencari indeks barang yang dituju
            indeks = -1              
            for i in range (len(load.data_gadget)):
                if (id == load.data_gadget[i][0]):
                    indeks = i
                    break
                
            # Mencari indeks untuk mengubah jumlah stok_user di gadget_borrow_history.csv    
            idx = -1          
            for i in range (len(load.data_gadget_borrow_history)):
                if (active_user_id == load.data_gadget_borrow_history[i][1] and id == load.data_gadget_borrow_history[i][2]):
                    idx = i
                    break
            
            if (indeks != -1 and idx != -1):
                # Proses untuk menghitung seberapa banyak barang user telah meminjam sehingga tidak berlebihan ketika ingin mengembalikan
                stok_user = int(load.data_gadget_borrow_history[idx][5])

                print("Stok gadget yang Anda miliki : ", stok_user)
                
                #BONUS 2
                if (stok_user != 0): 
                    kembali_berapa = int(input("Berapa banyak gadget yang ingin dikembalikan : "))
                    
                    if (1 <= kembali_berapa <= stok_user):
                        load.data_gadget[indeks][3] = load.data_gadget[indeks][3] + kembali_berapa
                        print("Gadget", load.data_gadget[indeks][1], "sebanyak", kembali_berapa, "telah dikembalikan.")
                        load.data_gadget_borrow_history[idx][5] = stok_user - kembali_berapa

                        load.data_gadget_return_history.append([len(load.data_gadget_return_history)+1,load.data_gadget_borrow_history[idx][0],tanggal,kembali_berapa])
                        
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