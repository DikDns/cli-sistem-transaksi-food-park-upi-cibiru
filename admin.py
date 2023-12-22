from modules import  csv
import os



# Ubah nama fungsi ini menjadi main()
# fungsi main biasa di simpan di atas file sebagai tanda gerbang masuk
# agar memberikan makna bahwa fungsi ini merupakan fungsi yang dipanggil pertama kali!
def menu():

    # panggil fungsi login()

    # if: login() bernilai false
    # return

    # Looping: dimulai
    print("==========Pilih Menu==========")
    print("1. Verifikasi Akun kios")
    print("2. Verivikasi Menu")
    print("3. Registrasi Akun Kasir")
    print("4. Keluar")

    # input: angka pilihan dari user
    # error handling: atasi user yang memasukan input aneh aneh

    # if: pilihan 1
    # panggil fungsi verifikasi_akun_kios()

    # if: pilihan 2
    # panggil fungsi verifikasi_menu()

    # if: pilihan 3
    # panggil fungsi registrasi_akun_kasir()

    # if: pilihan 4
    # keluar dari looping


# menghapus tampilan
def clear():
    if __name__ == "__main__":
        sistem_oprasi = os.name
        match sistem_oprasi:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")


# fungsi login admin
def login():
    clear()
    print("==========", "selamat datang admin!", "==========")

    # panggil fungsi get_admin_data()
    username = "UPI FOOD"
    password = "UPIF2023"
    kesempatan = 3

    # looping: mulai
    while kesempatan > 0:
        input_username = input("masukan username anda : ")
        input_password = input("masukan password anda : ")

        if input_username == username and input_password and password:
            print("Selamat! Anda berhasil Login")
            return True
        kesempatan -= 1

        # input: huruf 'y' untuk mengulang login

        # if: user memasukan bukan huruf 'y' maka keluar dari looping

        # tidak usah kasih batas login
        if kesempatan == 0:
            print("anda telah mencapai batas login, keluar dari program.")

        print(f"Username atau Password salah. kesempatan anda {kesempatan}x lagi")

    # return: false


''''FITUR KE 1'''

# def get_kios(nama_file):
#     with open(nama_file, "r") as csvfile:
#         reader = csv.reader(csvfile,delimiter=',')
#         for row in reader:
#             if row[2] == "Belum Terverifikasi":
#                 return row

# data_kios_belum_verif = "data\kios.csv"
# data_kios = get_kios(data_kios_belum_verif)
# print(data_kios)

# def get_kios(nama_file):
#     with open(nama_file, "r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             print(row)

# CARA PENGGUNAANYA
# data = "data\kios.csv"
# get_kios(data)


# def verifikasi_account(name_file, id_account, new_status):
#     rows = []

#     with open(name_file, "r") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             rows.append(row)

#     found = False

#     for row in rows:
#         if row['id'] == id_account:
#             row['status'] = new_status
#             found = True
#             break

#     if found:
#         with open(name_file, "w", newline='') as csvfile:
#             writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
#             writer.writeheader()  
#             writer.writerows(rows)  

#         print("Data yang sudah diupdate:")
#         print(row)
#     else:
#         print("Akun tidak ditemukan")

# CARA PENGGUNAANNYA
# masukan = input("masukan id: ")
# masukan_satatus = input("masukan status: ")
# verifikasi_account(data,masukan,masukan_satatus)


'''FITUR KE 2'''

path_dir = "\\".join(__file__.split("\\")[:-1])
data = f"{path_dir}\\data\\kios.txt"

print(data)




data_baca = csv.read_csv(data)
for i in data_baca:
    print(f"{i['id']} | {i['nama']} | {i['phone']} | {i['sudah_terverifikasi']}")

def cari(file,target):
# inputannya harus int jika targetnya
    for i in file:
        if i['id'] == target:
            return i


def inputan():
    masukan = int(input("masukan id: "))
    cari_data = cari(data_baca,masukan)
    if cari_data != None:
        print(f"id | nama | phone | Sudah Terverifikasi")
        print(f"...|......|.......|....................")
        print(f"{cari_data['id']} | {cari_data['nama']} | {cari_data['phone']} | {cari_data['sudah_terverifikasi']}")
    else:
        print("Data tidak ditemukan")

masukan = inputan()



# masukan = int(input("masukan id: "))
# cari_data = cari(data_baca,masukan)
# if cari_data != None:
#     print(cari_data)
# else:
#     print("data tidak di temukan")


# masukan = input("masukan id: ")
# cari_data = cari(data_baca,masukan)
# print(cari_data)


# def cari_data(file,id_target):
#     found = False
#     for f in file:
#         if f[0] == id_target:
#             found = True
#     return found

# masukan = input("masukan data: ")
# cari = cari_data(data_baca,masukan)
# print(cari)







'''FITUR KE 3'''
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

# dataRegistrasi = "data\kun_registrasi.csv"
# def registrasi(name_file):
#     name = input("masukan nama anda: ")
#     email = input("masukan email anda: ")
#     password = input("masukan password baru: ")

#     data_pengguna = {'Nama' : name, 'Email' : email, 'Password' : password }

#     with open(name_file, "a", newline="") as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=data_pengguna.keys())
#         if csvfile == 0:
#             writer.writeheader()
#         writer.writerow(data_pengguna)
#         return True

# CARA PENGGUNAANNYA
# data_registrasi = registrasi(dataRegistrasi)
# if data_registrasi == True:
#     print("Akun berhasil di buat")

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
