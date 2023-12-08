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
import csv 
def detail_kios(nama_file):
    with open(nama_file, "r") as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            if row[2] == "Belum Terverifikasi":
                print(row)
            
nama = "data\kios.csv"
detail_kios(nama)

# def edit_verifikasi_kios(nama_file, id_kios):
#     with open(nama_file, "r") as csvfile:
#         reader = csv.reader(csvfile)
#         data_akun_baru = [] 
#         for row in r[4] == id_kios:
#                 row[3] = "Terverifikasi"






'''fitur menu ke-3'''
# fungsi registrasi akun kasir
data_registrasi = {}
def registrasi(data):
    username = input("Username kasir: ")
    password = input("Password kasir: ")
    
    data.update({
        "username" : username,
        "password" : password
    })
    print("=====akun anda berhasil dibuat=====")

    # menambahkan : di dictionary
    data = {key + ':': value for key, value in data_registrasi.items()}
    for i, j in data.items():
        print(i,j)


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



