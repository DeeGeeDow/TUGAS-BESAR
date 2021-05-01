from load import load
# PROGRAM register.py
# program untuk mendaftar user

# KAMUS
# variabel

# fungsi/prosedur
def register():
# i.s. : akun dengan username tertentu belum terdaftar
# f.s. : akun sudah terdaftar

# KAMUS LOKAL
# new_user : array of string
# nama, username, password, alamat : string

# ALGORITMA PROSEDUR
    new_user = []
    nama = input("Masukkan nama : ")
    username = input("Masukkan username : ")
    
    while not isUsernameValid(username):
        print("Username sudah digunakan, silakan masukan username lain.")
        username = input("Masukkan username : ")
    
    password = input("Masukkan password : ")
    alamat = input("Masukkan alamat : ")

    new_user = [len(load.data_user)+1,nama,username,password,alamat]
    load.data_user.append(new_user)

    print(f"User {username} telah berhasil register ke dalam Kantong Ajaib.")


def isUsernameValid(username): 
# menghasilkan true jika username belum pernah digunakan

# KAMUS LOKAL
    isUsernameUsed = False 
# ALGORITMA FUNGSI
    for user in load.data_user:
        if username == user[2]:
            isUsernameUsed = True
    return not isUsernameUsed