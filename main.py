from register import register
from login import login

login()

while True:
    command = input(">>> ")

    if command == "register":
        register()
    else:
        print("Invalid Command")