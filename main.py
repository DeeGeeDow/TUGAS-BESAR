from register import register
from login import login
from cari_tahun import cari_tahun
from carirarity import search_rar

login()
role = login.role
while True:
    command = input(">>> ")
    if command == "register" and role == "admin":
        register()
    elif command == "caritahun" and (role == "admin" or role == "user"):
        cari_tahun()
    elif command == "carirarity" and (role == "admin" or role == "user"):
        search_rar()
    else:
        print("Invalid Command")