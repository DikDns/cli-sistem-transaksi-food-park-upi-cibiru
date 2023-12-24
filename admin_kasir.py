import tpcsv as csv
from utils import print_header, print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, generate_password, normalize_string

kasir_account_path = get_absolute_path("data/kasir_account.csv")


def admin_kasir_panel():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Kasir", start="\n")

        print_body("Pilih menu sesuai angka:", start="\n")
        print_body("1. Registrasi Kasir")
        print_body("2. Ubah Data Kasir")
        print_body("3. Hapus Kasir")
        print_body("4. Kembali")

        pilihan = input("\nMasukkan pilihan:> ")

        if pilihan == "1":
            tambah_kasir()
        elif pilihan == "2":
            ubah_kasir()
        elif pilihan == "3":
            hapus_kasir()
        elif pilihan == "4":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def tambah_kasir():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Kasir > Registrasi Kasir", start="\n")

        username = input("Masukkan Username Kasir:> ")

        data_kasir_baru = model_kasir_account(username)

        clear_screen()

        print_data_kasir([data_kasir_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kasir = csv.get(kasir_account_path)
            data_kasir.append(data_kasir_baru)
            hasil = csv.put(kasir_account_path, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil ditambahkan", start="\n")
                break

            print_alert("Gagal menambahkan data kasir", start="\n")

        konfirmasi = input("\nKembali ke Panel Kasir? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def ubah_kasir():
    while True:
        clear_screen()

        data_kasir = csv.get(kasir_account_path)

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Kasir > Ubah kasir", start="\n")

        keyword = input("\nMasukkan ID/Username Kasir:> ")

        index = cari_kasir(data_kasir, keyword)

        if index == -1:
            print_alert("Data kasir tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel kasir? (Y/N):> ")

            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

        print_data_kasir([data_kasir[index]])

        print_body("Masukkan data baru:", start="\n")

        id_kasir = data_kasir[index]["id"]
        nama_kasir = input("Masukkan Username Baru:> ")
        password_kasir = input("Masukan Password Baru:> ")

        data_kasir_baru = model_kasir_account(
            nama_kasir, id_kasir, password_kasir)

        clear_screen()

        print_data_kasir([data_kasir_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kasir[index] = data_kasir_baru
            hasil = csv.put(kasir_account_path, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data Kasir", start="\n")

        konfirmasi = input("\nKembali ke Panel Kasir? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def hapus_kasir():
    while True:
        clear_screen()

        data_kasir = csv.get(kasir_account_path)

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Kasir > Hapus Kasir", start="\n")

        keyword = input("\nMasukkan ID/Username Kasir:> ")

        index = cari_kasir(data_kasir, keyword)

        if index == -1:
            print_alert("Data kasir tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Kasir? (Y/N):> ")

            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

        print(data_kasir[index])

        konfirmasi = input("\nHapus data kasir tersebut? (Y/N):> ")
        if konfirmasi.upper() == "Y":
            data_kasir.pop(index)

            hasil = csv.put(kasir_account_path, data_kasir)

            if hasil:
                print_alert("Data kasir berhasil dihapus", start="\n")
                break

            print_alert("Gagal menghapus data kasir", start="\n")

        konfirmasi = input("\nKembali ke Panel Kasir? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def cari_kasir(data, keyword):
    for i in range(len(data)):
        id_kasir = str(data[i]["id"])
        nama_kasir = data[i]["username"].upper()
        if id_kasir == keyword or nama_kasir == keyword.upper():
            return i
    return -1


def print_data_kasir(list_kasir):
    if len(list_kasir) == 0:
        print_alert("Data kasir kosong!", start="\n")
        return

    print_border()
    for kasir in list_kasir:
        print_body(f"ID: {kasir['id']}")
        print_body(f"Nama Kasir: {kasir['username']}")
        print_body(f"Password: {kasir['password']}")
        print_border()


def model_kasir_account(username, id_kasir=generate_id(), password=generate_password()):
    if username == None:
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
