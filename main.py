from register import register
from login import login

login()
role = login.role
while True:
    command = input(">>> ")

    if command == "register" and role == "admin":
        register()
    else:
        print("Invalid Command")