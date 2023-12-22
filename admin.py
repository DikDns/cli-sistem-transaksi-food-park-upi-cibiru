import tpcsv as csv
import uuid

# def create_admin_account():


def combine_path(path: str):
    list_alamat_file_ini = __file__.split("\\")[:-1]
    alamat_file_ini = "\\".join(list_alamat_file_ini)
    return alamat_file_ini + path


admin_account_path = combine_path("\\data\\admin_account.csv")
kios_account_path = combine_path("\\data\\kios_account.csv")
kasir_account_path = combine_path("\\data\\kasir_account.csv")

# data_admin_account = [
#     {
#         "id": 1,
#         "username": "admin",
#         "password": "admin",
#         "email": "",
#     },
#     {
#         "id": 2,
#         "nama": "Owner",
#         "email": "dasd",
#     }
# ]

# print(list(data_admin_account[0].keys()))

# hasil = csv.get(admin_account_path)

# if hasil:
#     print("Berhasil")
# else:
#     print("Gagal")

# print(hasil)

# data_kios = csv.get(kios_account_path)

# print(data_kios)

# id_kios = str(uuid.uuid4())[9:13]
# nama_kios = input("Masukkan nama kios: ")
# alamat_kios = input("Masukkan alamat kios: ")

# data_kios.append({
#     "id": id_kios,
#     "nama": nama_kios,
#     "alamat": alamat_kios,
# })

# print(csv.put(kios_account_path, data_kios))

'''Registrasi akun kasir'''


def registrasi():
    data_kasir = csv.get(kasir_account_path)
    while True:
        # print(data_kasir)
        id_kasir = str(uuid.uuid4())[9:13]
        username = input("masukan username anda: ")
        password = input("masukan password anda: ")
        konfirmasi = input("Apakah anda yakin?(Y/N): ")

        if konfirmasi == "Y":
            data_kasir.append({
                "id": id_kasir,
                "username": username,
                "password": password
            })
            print("Akun berhasil dibuat!")
            break

        else:
            print("Silahkan masukan kembali username dan password anda")

    simpan = csv.put(kasir_account_path, data_kasir)
    return simpan


registrasi()
