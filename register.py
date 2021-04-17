def register():
    data_user = open("user.csv","r")
    user = data_user.readlines()
    
    data_nama = []
    data_username = []
    data_password = []
    data_alamat = []
    
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
        
        data_nama.append(split_value[1])
        data_username.append(split_value[2])
        data_alamat.append(split_value[4])
        data_password.append(split_value[3])
    
    nama = input("Masukkan nama : ")
    username = input("Masukkan username : ")
    
    isUsernameUsed = False
    for username_test in data_username:
        if username == username_test:
            isUsernameUsed = True
    
    while isUsernameUsed:
        print("Username sudah digunakan, silakan masukan username lain.")
        username = input("Masukkan username : ")
        isUsernameUsed = False
        for username_test in data_username:
            if username == username_test:
                isUsernameUsed = True
    
    password = input("Masukkan password : ")
    alamat = input("Masukkan alamat : ")

    f = open("user.csv","a+")
    f.write(f"\n{len(user)};{nama};{username};{password};{alamat};user")
    f.close()

    print(f"User {username} telah berhasil register ke dalam Kantong Ajaib.")
