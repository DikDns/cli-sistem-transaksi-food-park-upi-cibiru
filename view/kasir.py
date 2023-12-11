print("Selamat datang di Menu Kasir")

def loginKasir():
    akses = 3
    username = "KasirUPI"
    password = "FoodCibiru!"

    while akses > 0:
        loginKasir  = input("Masukan Username: ") 
        passKasir   = input("Masukan Password: ")
        
        if loginKasir == username and passKasir == password:
            print("Selamat datang di Kasir")
            break
        akses -=1
        
        if akses == 0:
            print("Anda telah Mencapai Batas, Login Ulang")
            break

        print(f"username atau password anda salah, kesempatan anda {akses}x lagi")

loginKasir()

import os

def hapusTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

hapusTerminal()


riwayat_transaksi = {
    "Kios": "Seblak Meledak",
    "IdTransaksi": "UPI-01",
    "Tanggal": "DD//MM/YY",
    "Table": "01",
    "Barang": [
        {"Nama": "Seblak A", "Jumlah": 2, "Harga": 20000},
        {"Nama": "Seblak B", "Jumlah": 1, "Harga": 10000},
    ],
    "Sub Total": 30000,
    "Metode Pembayaran": "Tunai",
}
print(riwayat_transaksi)

def inputKasir():
    idTransaksi = input("Masukan ID Transaksi: ")
    idTrans = riwayat_transaksi["IdTransaksi"]  
    if idTransaksi == idTrans:
        print(f"Total Harga: {riwayat_transaksi['Sub Total']}")
        return riwayat_transaksi["Sub Total"]
    else:
        return 0

def inputKonsumen():
    total_harga = inputKasir()
    while True:
        bayarKonsumen = int(input("Nominal Pembayaran: "))
        kondisi = input("Apakah Input Pembayaran Sesuai ? (Y/N): ")
        if kondisi == "Y":
            print("Pembayaran dilanjutkan.")
            if bayarKonsumen > total_harga:
                print(f"Uang Kembalian: {bayarKonsumen - total_harga}")
                print("Terima kasih telah memilih UPI Food Park Cibiru sebagai tempat untuk menikmati makanan dan minuman Anda!")
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

inputKonsumen()

