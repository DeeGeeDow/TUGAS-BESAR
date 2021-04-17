f = open("user.csv","r")
user = f.readlines()
f.close()

data_username = []
data_password = []
data_role = []

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

username_idx = 0
 
def login():
    username = input("Masukkan username : ")
    isUsernameFound = False
    for i in range(len(data_username)):
        if username == data_username[i]:
            isUsernameFound = True
            username_idx = i
    
    while not isUsernameFound:
        print("Username tidak terdaftar")
        username = input("Masukkan username : ")
        isUsernameFound = False
        for i in range(len(data_username)):
            if username == data_username[i]:
                isUsernameFound = True
                username_idx = i
    

    password = input("Masukkan password : ")
    if password != data_password[username_idx]:
        print("Password salah!")
        login()
    else:
        print(f"Halo {username}! Selamat datang di Kantong Ajaib.")