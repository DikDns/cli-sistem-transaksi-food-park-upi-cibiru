import tpcsv as csv
import utils
from utils import print_header, print_body, print_border, print_alert, clear_screen
from admin_kios import admin_kios_panel
from admin_kasir import admin_kasir_panel

admin_account_path = utils.get_absolute_path("data/admin_account.csv")
kios_account_path = utils.get_absolute_path("data/kios_account.csv")
kasir_account_path = utils.get_absolute_path("data/kasir_account.csv")

"""
Pintu Masuk Utama
"""


def admin_panel():
    is_logged_in = login_admin()

    while is_logged_in:
        clear_screen()

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin", start="\n")

        print_body("Pilih menu sesuai angka:", start="\n")
        print_body("1. Mengelola Kios")
        print_body("2. Mengelola Menu")
        print_body("3. Mengelola Kasir")
        print_body("4. Keluar")

        pilihan = input("\nMasukkan pilihan:> ")

        if pilihan == "1":
            admin_kios_panel()
        elif pilihan == "2":
            continue
        elif pilihan == "3":
            admin_kasir_panel()
        elif pilihan == "4":
            clear_screen()
            is_logged_in = False
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def login_admin():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Login Admin", start="\n")

        username = input("\nMasukkan username:> ")
        password = input("Masukkan password:> ")

        data_admin = csv.get(admin_account_path)
        for row in data_admin:
            if row['username'] == username and row['password'] == password:
                return True

        print_body("Username atau password salah", start="\n")

        konfirmasi = input("\nKeluar Aplikasi? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            clear_screen()
            return False


# Buatan Achmad Soe
'''Verifikasi Kios'''


def show_account_kios():
    data = []
    data_kios = csv.get(kios_account_path)
    for row in data_kios:
        if not row['sudah_terverifikasi']:
            data.append(row)
    return data


def search_account_kios(data, target):
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
        search_account = search_account_kios(show_account, username)
        status = input("masukan status: ")
        if search_account != None:
            show_account[search_account] = {
                'id': show_account[search_account]['id'],
                'username': show_account[search_account]['username'],
                'password': show_account[search_account]['password'],
                'sudah_terverifikasi': status
            }
            break
        else:
            print("akun tidak ada silahkan masukan username yang sesuai")

    simpan = csv.put(kios_account_path, show_account)
    return simpan







admin_panel()
