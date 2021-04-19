# PROGRAM login.py
# program untuk login ke Kantong Ajaib

# KAMUS
# variabel

# fungsi/prosedur
def login():
# i.s. : user/admin belum login
# f.s. : user/admin sudah login
# KAMUS LOKAL
# ALGORITMA PROSEDUR
    f = open("user.csv","r")
    user = f.readlines()
    f.close()

    data_username = []
    data_password = []
    data_role = []

    # csv parser
    for i in range(1,len(user)):
        split_value = []
        tmp = ''
        for c in user[i]:
            if c == ";":
                split_value.append(tmp)
                tmp = ''
            else:
                tmp += c
        if tmp:
            split_value.append(tmp)

        data_username.append(split_value[2])
        data_password.append(split_value[3])
        data_role.append(split_value[-1])

    username = input("Masukkan username : ")

    while username_id(username,data_username) == 0:
        print("Username tidak terdaftar")
        username = input("Masukkan username : ")
        
    password = input("Masukkan password : ")
    if password != data_password[username_id(username, data_username) - 1]:
        print("Password salah!")
        login()
    else:
        print(f"Halo {username}! Selamat datang di Kantong Ajaib.")

def username_id(username, data_username):
# menghasilkan id username jika sudah terdaftar, 0 jika belum terdaftar
# KAMUS LOKAL
# ALGORITMA FUNGSI
    username_idx = -1
    for i in range(len(data_username)):
        if username == data_username[i]:
            isUsernameFound = True
            username_idx = i
    
    return username_idx + 1