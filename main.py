import printdoraemon as pd
from load import load
from save import save
from register import register
from login import login
from pinjam import pinjam
from kembalikan import kembalikan
from minta import minta
from caritahun import caritahun
from carirarity import carirarity
from ubahjumlah import ubahjumlah
from hapusitem import hapusitem
from tambahitem import tambahitem
from riwayatambil import riwayatambil
from riwayatpinjam import riwayatpinjam
from riwayatkembali import riwayatkembali
from help import help_admin, help_general, help_user

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help = "mengakses folder dalam folder_penyimpanan")
args = parser.parse_args()
print("Loading...")
load(args.nama_folder)

def runCommand(procedure,isAdminPermitted, isUserPermitted):
# I.S. pengguna memasukkan command
# F.S. procedure berjalan jika role-nya memiliki izin untuk menjalankan procedure
# KAMUS LOKAL
# procedure : prosedur
# isUserPerrmitted : boolean (apakah user boleh mengakses atau tidak)
# ALGORITMA PROSEDUR
    if (role == 'admin' and isAdminPermitted) or (role == 'user' and isUserPermitted):
        procedure()
    elif role == 'user':
        print("Hanya admin yang dapat mengakses command ini.")
    elif role == 'admin':
        print("Hanya user yang dapat mengakses command ini.")
    else:
        print("Anda belum login. Gunakan command 'login' untuk login")

role = '' # jika role masih kosong, berarti belum login
if not load.loading_failed:
    pd.print_doraemon()
while not load.loading_failed:
    print("Ketik 'help' untuk melihat semua perintah")
    command = input(">>> ")
    if command == 'login':
        if role == '':
            login()
            role = login.role
        else:
            print("Anda sudah login")
    elif command == "register":
        runCommand(register,True,False) 
    elif command == "caritahun":
        runCommand(caritahun,True,True)
    elif command == "carirarity":
        runCommand(carirarity,True,True)
    elif command == "ubahjumlah":
        runCommand(ubahjumlah,True,False)
    elif command == "hapusitem":
        runCommand(hapusitem,True,False)
    elif command == "tambahitem":
        runCommand(tambahitem,True,False)
    elif command == "pinjam":
        runCommand(pinjam,False,True)
    elif command == "minta":
        runCommand(minta,False,True)
    elif command == "kembalikan":
        runCommand(kembalikan,False,True)
    elif command == "riwayatambil":
        runCommand(riwayatambil,True,False)
    elif command == "riwayatkembali":
        runCommand(riwayatkembali,True,False)
    elif command == "riwayatpinjam":
        runCommand(riwayatpinjam,True,False)
    elif command == "help":
        if role == "admin":
            help_admin()
        elif role == 'user':
            help_user()
        else:
            help_general()
    elif command == "save":
        runCommand(save,True,True)
    elif command == "exit":
        print("Terima kasih")
        break
    else:
        print("Invalid Command")
    
