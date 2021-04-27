from register import register
from login import login
from cari_tahun import cari_tahun
from carirarity import find_rarity 

login()
role = login.role
while True:
    command = input(">>> ")
    if command == "register" and role == "admin":
        register()
    if command == "caritahun" and role == "admin" or role == "user":
        cari_tahun()
    if command == "carirarity" and role == "admin" or role == "user":
        find_rarity()
    else:
        print("Invalid Command")