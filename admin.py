import tpcsv as csv
import utils
from utils import print_header, print_body, print_border, print_alert, clear_screen
from admin_kios import admin_kios_panel
from admin_menu import admin_menu_panel
from admin_kasir import admin_kasir_panel

admin_account_path = utils.get_absolute_path("data/admin_account.csv")


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
            admin_menu_panel()
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


admin_panel()
