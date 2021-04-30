from register import register
from login import login
from caritahun import caritahun
from carirarity import carirarity
from ubahjumlah import ubahjumlah
from hapusitem import hapusitem
from help import help_admin
from help import help_user

login()
role = login.role
while True:
    print("Ketik 'help' untuk melihat semua perintah")
    command = input(">>> ")
    if command == "register" and role == "admin":
        register()
    elif command == "caritahun":
        caritahun()
    elif command == "carirarity":
        carirarity()
    elif command == "ubahjumlah" and role == "admin":
        ubahjumlah()
    elif command == "hapusitem" and role == "admin":
        hapusitem()
    elif command == "help":
        if role == "admin":
            help_admin()
        elif role == "user":
            help_user()
    elif command == "quit":
        print("Terima kasih")
        break
    else:
        print("Invalid Command")
    
