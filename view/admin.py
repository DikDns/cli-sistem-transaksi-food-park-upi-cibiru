import os
import csv


# menghapus tampilan
def clear():
    if __name__ == "__main__":
        sistem_oprasi = os.name
        match sistem_oprasi:
            case "posix": os.system("clear")
            case "nt" : os.system("cls")


# fungsi login admin
def login():
    clear()
    print("==========","selamat datang admin!", "==========")
    username = "UPI FOOD"
    password = "UPIF2023"
    kesempatan = 3

    while kesempatan > 0:
        
        input_username = input("masukan username anda : ")
        input_password = input("masukan password anda : ")

        if input_username == username and input_password and password:
            print("Selamat! Anda berhasil Login")
            return True
        kesempatan -= 1

        if kesempatan == 0:
            print("anda telah mencapai batas login, keluar dari program.")
        

        print(f"Username atau Password salah. kesempatan anda {kesempatan}x lagi")


''''fitur menu ke-1'''

# def get_kios(nama_file):
#     with open(nama_file, "r") as csvfile:
#         reader = csv.reader(csvfile,delimiter=',')
#         for row in reader:
#             if row[2] == "Belum Terverifikasi":
#                 return row

# data_kios_belum_verif = "data\kios.csv"
# data_kios = get_kios(data_kios_belum_verif)
# print(data_kios)

def get_kios(nama_file):
    with open(nama_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
        
# data = "data\kios.csv"
# get_kios(data)


def verifikasi_account(name_file, id_account, new_status):
    rows = []

    with open(name_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)

    found = False

    for row in rows:
        if row['id'] == id_account:
            row['status'] = new_status
            found = True
            break

    if found:
        with open(name_file, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
            writer.writeheader()  
            writer.writerows(rows)  

        print("Data yang sudah diupdate:")
        print(row)
    else:
        print("Akun tidak ditemukan")


# masukan = input("masukan id: ")
# masukan_satatus = input("masukan status: ")
# verifikasi_account(data,masukan,masukan_satatus)



'''fitur menu ke-3'''
# fungsi registrasi akun kasir
# data_registrasi = {}
# def registrasi(data):
#     username = input("Username kasir: ")
#     password = input("Password kasir: ")
    
#     data.update({
#         "username" : username,
#         "password" : password
#     })
#     print("=====akun anda berhasil dibuat=====")

#     # menambahkan : di dictionary
#     data = {key + ':': value for key, value in data_registrasi.items()}
#     for i, j in data.items():
#         print(i,j)

# data_registrasi = "data/registrasi.csv"
# def registrasi(name_file,nama,nama_tenant,phone):
#     with open(name_file, "a",newline="") as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=" ")

dataRegistrasi = "data\kun_registrasi.csv"
def registrasi(name_file):
    name = input("masukan nama anda: ")
    email = input("masukan email anda: ")
    password = input("masukan password baru: ")

    data_pengguna = {'Nama' : name, 'Email' : email, 'Password' : password }

    with open(name_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_pengguna.keys())
        if csvfile == 0:
            writer.writeheader()
        writer.writerow(data_pengguna)
        return True

data_registrasi = registrasi(dataRegistrasi)
if data_registrasi == True:
    print("Akun berhasil di buat")

# fungsi menu
def menu():
    print("==========Pilih Menu==========")
    print("1. Verifikasi Akun kios")
    print("2. Verivikasi Menu")
    print("3. Registrasi Akun Kasir")
    print("4. Keluar")




# registrasi(data_registrasi)






# while True:
#     clear()
#     login()
#     menu()
#     break



