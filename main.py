import printdoraemon as pd
from register import register
from login import login
from caritahun import caritahun
from carirarity import carirarity
from ubahjumlah import ubahjumlah
from hapusitem import hapusitem
from tambahitem import tambahitem
from help import help_admin, help_general, help_user


def runCommand(procedure,isUserPermitted):
# I.S. pengguna memasukkan command
# F.S. procedure berjalan jika role-nya memiliki izin untuk menjalankan procedure
# KAMUS LOKAL
# procedure : prosedur
# isUserPerrmitted : boolean (apakah user boleh mengakses atau tidak)
# ALGORITMA PROSEDUR
    if role == 'admin' or (role == 'user' and isUserPermitted):
        procedure()
    elif role == 'user':
        print("Hanya admin yang dapat mengakses command ini.")
    else:
        print("Anda belum login. Gunakan command 'login' untuk login")

role = '' # jika role masih kosong, berarti belum login
pd.print_doraemon()
while True:
    print("Ketik 'help' untuk melihat semua perintah")
    command = input(">>> ")
    if command == 'login':
        if role == '':
            login()
            role = login.role
        else:
            print("Anda sudah login")
    elif command == "register":
        runCommand(register,False) 
    elif command == "caritahun":
        runCommand(caritahun,True)
    elif command == "carirarity":
        runCommand(carirarity,True)
    elif command == "ubahjumlah":
        runCommand(ubahjumlah,False)
    elif command == "hapusitem":
        runCommand(hapusitem,False)
    elif command == "tambahitem":
        runCommand(tambahitem,False)
    elif command == "help":
        if role == "admin":
            help_admin()
        elif role == 'user':
            help_user()
        else:
            help_general()
    elif command == "exit":
        print("Terima kasih")
        break
    else:
        print("Invalid Command")
    
