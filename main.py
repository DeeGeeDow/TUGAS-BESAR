from register import register
from login import login
from cari_tahun import cari_tahun
from carirarity import search_rar
from ubahjumlah import ubahjumlah
from help import help_admin
from help import help_user

login()
role = login.role
while True:
    print("Ketik help untuk melihat semua perintah")
    command = input(">>> ")
    if command == "register" and role == "admin":
        register()
    elif command == "caritahun":
        cari_tahun()
    elif command == "carirarity":
        search_rar()
    elif command == "ubahjumlah" and role == "admin":
        ubahjumlah()
    elif command == "help" and role == "admin":
        help_admin()
    elif command == "help" and role == "user":
        help_user()
    elif command == "quit":
        print("Terima kasih")
        break
    else:
        print("Invalid Command")
    