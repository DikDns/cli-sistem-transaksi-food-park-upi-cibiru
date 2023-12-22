import tpcsv as csv
import pandas as pd
import uuid
import os


def hapus_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def combine_path(path: str):
    list_alamat_file_ini = __file__.split("\\")[:-1]
    alamat_file_ini = "\\".join(list_alamat_file_ini)
    return alamat_file_ini + path


kasir_account_path = combine_path("\\data\\kasir.csv")

print("Selamat datang di Menu Kasir")

riwayat_transaksi = {
    "Kios": "Seblak Meledak",
    "IdTransaksi": "UPI-01",
    "Tanggal": "DD//MM/YY",
    "Table": "01",
    "Menu": [
        {"Nama": "Seblak A", "Jumlah": 2, "Harga": 20000},
        {"Nama": "Seblak B", "Jumlah": 1, "Harga": 10000},
    ],
    "Sub Total": 30000,
    "Metode Pembayaran": "Tunai",
}


def login_kasir():
    akses = 3
    username = "KasirUPI"
    password = "FoodCibiru!"

    while akses > 0:
        login_kasir = input("Masukan Username: ")
        pass_kasir = input("Masukan Password: ")

        if login_kasir == username and pass_kasir == password:
            print("Selamat datang di Kasir")
            return True
        akses -= 1

        if akses == 0:
            print("Anda telah Mencapai Batas, Login Ulang")
            return False

        print(
            f"username atau password anda salah, kesempatan anda {akses}x lagi")


def input_konsumen():
    total_harga = input_kasir()
    while True:
        bayarKonsumen = int(input("Nominal Pembayaran: "))
        kondisi = input("Apakah Input Pembayaran Sesuai ? (Y/N): ")
        if kondisi == "Y":
            print("Pembayaran dilanjutkan")
            if bayarKonsumen > total_harga:
                print(f"Uang Kembalian: {bayarKonsumen - total_harga}")
                print(
                    "Terima kasih telah memilih UPI Food Park Cibiru sebagai tempat untuk menikmati makanan dan minuman Anda!")
                break
            elif bayarKonsumen == total_harga:
                print("Terima kasih banyak telah memilih UPI Food Park Cibiru sebagai tempat untuk menikmati makanan dan minuman Anda!")
                break
            else:
                print("Pembayaran kurang. Silakan masukkan nominal yang mencukupi.")
        elif kondisi == "N":
            print("Pembayaran dibatalkan. Silakan masukkan ulang.")
        else:
            print("Input tidak valid. Masukkan Y untuk lanjut atau N untuk batalkan.")


def input_kasir():

    while True:
        idTransaksi = input("Masukan ID Transaksi: ")
        idTrans = riwayat_transaksi["IdTransaksi"]
        if idTransaksi == idTrans:
            print(f"Total Harga: {riwayat_transaksi['Sub Total']}")
            return riwayat_transaksi["Sub Total"]
        else:
            print("Input Id tidak Valid, Mohon cek kembali.")


akses_kasir = login_kasir()


if akses_kasir == True:
    hapus_terminal()
    print(riwayat_transaksi)
    input_konsumen()
