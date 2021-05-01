from load import load

# PROGRAM login.py
# program untuk login ke Kantong Ajaib

# KAMUS
# variabel

# fungsi/prosedur
def login():
# i.s. : user/admin belum login
# f.s. : user/admin sudah login

# KAMUS LOKAL
# user : array of string
# data_username, data_password, data_role : array of string
# username, password : string

# ALGORITMA PROSEDUR
    username = input("Masukkan username : ")

    while username_id(username) == 0:
        print("Username tidak terdaftar")
        username = input("Masukkan username : ")
        
    password = input("Masukkan password : ")
    if password != load.data_user[username_id(username) - 1][3]:
        print("Password salah!")
        login()
    else:
        login.role = load.data_user[username_id(username) - 1][-1]
        print(f"Halo {username}! Selamat datang di Kantong Ajaib.")

def username_id(username):
# menghasilkan id username jika sudah terdaftar, 0 jika belum terdaftar
# KAMUS LOKAL
# username_idx : int
# ALGORITMA FUNGSI
    username_idx = -1
    for i in range(len(load.data_user)):
        if username == load.data_user[i][2]:
            username_idx = i
    
    return username_idx + 1