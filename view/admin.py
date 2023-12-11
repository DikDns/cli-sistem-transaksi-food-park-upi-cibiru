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

# Komentar tentang fitur menu ke-3 di bawah ini tidak memberikan makna yang jelas!!!
"""fitur menu ke-3"""
# fungsi registrasi akun kasir
data_registrasi = {}


def registrasi(data):
    # nama variabel diharuskan sangat spesifik!
    # username_kasir = input("Username kasir: ")
    username = input("Username kasir: ")
    password = input("Password kasir: ")

    data.update({"username": username, "password": password})
    print("=====akun anda berhasil dibuat=====")

    # menambahkan : di dictionary
    data = {key + ":": value for key, value in data_registrasi.items()}
    for i, j in data.items():
        print(i, j)


registrasi(data_registrasi)


# while True:
#     clear()
#     login()
#     menu()
#     break
