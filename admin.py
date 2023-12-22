import tpcsv as csv
import uuid


def combine_path(path: str):
    list_alamat_file_ini = __file__.split("\\")[:-1]
    alamat_file_ini = "\\".join(list_alamat_file_ini)
    return alamat_file_ini + path


admin_account_path = combine_path("\\data\\admin_account.csv")
kios_account_path = combine_path("\\data\\kios_account.csv")
kasir_account_path = combine_path("\\data\\kasir_account.csv")


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
                "id" : id_kasir,
                "username" : username,
                "password" : password}})
            print("Akun berhasil dibuat!")
            break

        else:
            print("Silahkan masukan kembali username dan password anda")

    simpan = csv.put(kasir_account_path,data_kasir)
    return simpan

'''Verifikasi Kios'''
def  show_account_kios():
    data = []
    data_kios = csv.get(kios_account_path)
    for row in data_kios:
        if not row['sudah_terverifikasi']:
            data.append(row)
    return data

def search_account_kios(data,target):
    for i in range(len(data)):
        if data[i]['username'] == target:
            return i
    return None


def verifikasi_account_kios():
    show_account = csv.get(kios_account_path)
    for row in show_account:
        print(row)
    

    while True:
        username = input("masukan username: ")
        search_account = search_account_kios(show_account,username)
        status = input("masukan status: ")
        if search_account != None:
            show_account[search_account] = {
                'id': show_account[search_account]['id'],
                'username': show_account[search_account]['username'],
                'password': show_account[search_account]['password'],
                'sudah_terverifikasi' : status
            }
            break
        else:
            print("akun tidak ada silahkan masukan username yang sesuai")
            continue

    simpan = csv.put(kios_account_path,show_account)
    return simpan

verifikasi = verifikasi_account_kios()

data = csv.get(kios_account_path)
for row in data:
    print(row)

