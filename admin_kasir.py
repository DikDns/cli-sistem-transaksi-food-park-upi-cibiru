import time
import tpcsv as csv
from admin_utils import brand, input_konfirmasi_kembali
from utils import print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, generate_password, normalize_string

KASIR_ACCOUNT_PATH = get_absolute_path("data/kasir_account.csv")
PESAN_KONFIRMASI = "\nKembali ke Panel Kasir? (Y/N):> "


def admin_kasir_panel():
    while True:
        brand()

        print_body("Panel Admin > Mengelola Kasir", start="\n")

        print_body("Pilih menu sesuai angka:", start="\n")
        print_body("1. Lihat Akun Kasir")
        print_body("2. Registrasi Kasir")
        print_body("3. Ubah Data Kasir")
        print_body("4. Hapus Kasir")
        print_body("5. Kembali")

        pilihan = input("\nMasukkan pilihan:> ")

        if pilihan == "1":
            lihat_kasir()
        elif pilihan == "2":
            tambah_kasir()
        elif pilihan == "3":
            ubah_kasir()
        elif pilihan == "4":
            hapus_kasir()
        elif pilihan == "5":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def lihat_kasir():
    data_kasir = csv.get(KASIR_ACCOUNT_PATH)
    while True:
        print_data_kasir(data_kasir)

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def tambah_kasir():
    while True:
        brand()

        print_body(
            "Panel Admin > Mengelola Kasir > Registrasi Kasir\n", start="\n")

        username = input_username_kasir()

        if username is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        data_kasir_baru = model_kasir_account(username)

        print_data_kasir([data_kasir_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kasir = csv.get(KASIR_ACCOUNT_PATH)
            data_kasir.append(data_kasir_baru)
            hasil = csv.put(KASIR_ACCOUNT_PATH, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil ditambahkan", start="\n")
                break

            print_alert("Gagal menambahkan data kasir", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def ubah_kasir():
    while True:
        brand()

        print_body("Panel Admin > Mengelola Kasir > Ubah kasir\n", start="\n")

        data_kasir = csv.get(KASIR_ACCOUNT_PATH)
        keyword = input("Masukkan ID/Username Kasir:> ")

        index = cari_kasir(data_kasir, keyword)

        if index == -1:
            print_alert("Data kasir tidak ditemukan", start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print_data_kasir([data_kasir[index]])

        print_body("Masukkan data baru:\n", start="\n")

        id_kasir = data_kasir[index]["id"]
        username_kasir = input_username_kasir()

        if username_kasir is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        password_kasir = input_password_kasir()

        if password_kasir is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        data_kasir_baru = model_kasir_account(
            username_kasir, id_kasir, password_kasir)

        print_data_kasir([data_kasir_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kasir[index] = data_kasir_baru
            hasil = csv.put(KASIR_ACCOUNT_PATH, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data Kasir", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def hapus_kasir():
    while True:
        brand()

        data_kasir = csv.get(KASIR_ACCOUNT_PATH)

        print_body("Panel Admin > Mengelola Kasir > Hapus Kasir\n", start="\n")

        keyword = input("Masukkan ID/Username Kasir:> ")

        index = cari_kasir(data_kasir, keyword)

        if index == -1:
            print_alert("Data kasir tidak ditemukan", start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print(data_kasir[index])

        konfirmasi = input("\nHapus data kasir tersebut? (Y/N):> ")
        if konfirmasi.upper() == "Y":
            data_kasir.pop(index)

            # Jika data kosong, tambahkan data kosong agar fungsi csv.put() tidak error
            if len(data_kasir) == 0:
                data_kasir.append(model_kasir_account(None))

            hasil = csv.put(KASIR_ACCOUNT_PATH, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil dihapus", start="\n")
                break

            print_alert("Gagal menghapus data kasir", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def cari_kasir(data: list, keyword):
    for kasir in data:
        id_kasir = str(kasir["id"])
        username_kasir = str(kasir["username"]).upper()
        if id_kasir == keyword or username_kasir == keyword.upper():
            return data.index(kasir)
    return -1


def print_data_kasir(list_kasir: list):
    clear_screen()

    if len(list_kasir) == 0:
        print_alert("Data kasir kosong!", start="\n")
        return

    print_border()
    for kasir in list_kasir:
        print_body(f"ID: {kasir['id']}", is_delayed=False)
        print_body(f"Username: {kasir['username']}", is_delayed=False)
        print_body(f"Password: {kasir['password']}", is_delayed=False)
        print_border()
        time.sleep(0.24)


def input_username_kasir():
    data_kasir = csv.get(KASIR_ACCOUNT_PATH)
    nama_kasir = input("Masukkan nama kasir:> ")

    if nama_kasir == "":
        print_alert("Nama Kasir tidak boleh kosong", start="\n")
        return

    if cari_kasir(data_kasir, nama_kasir) != -1:
        print_alert("Nama Kasir sudah terdaftar", start="\n")
        return

    return nama_kasir


def input_password_kasir():
    password = input("\nMasukkan password kasir:> ")

    if password == "":
        print_alert("Password Kasir tidak boleh kosong", start="\n")
        return

    return password


def model_kasir_account(username, id_kasir=None, password=None):
    if id_kasir is None:
        id_kasir = generate_id()
    if password is None:
        password = generate_password()
    if username is None:
        return {
            "id": None,
            "username": None,
            "password": None
        }
    return {
        "id": id_kasir,
        "username": normalize_string(username),
        "password": password
    }
