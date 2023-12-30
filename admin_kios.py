import time
import tpcsv as csv
from admin_utils import brand, input_konfirmasi_kembali
from utils import print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, generate_password, normalize_string


KIOS_ACCOUNT_PATH = get_absolute_path("data/kios_account.csv")
PESAN_KONFIRMASI = "\nKembali ke Panel Kios? (Y/N):> "


def admin_kios_panel():
    while True:
        brand()

        print_body("Panel Admin > Mengelola Kios", start="\n")

        print_body("Pilih menu sesuai angka:", start="\n")
        print_body("1. Lihat Semua Kios")
        print_body("2. Registrasi Kios")
        print_body("3. Ubah Data Kios")
        print_body("4. Hapus Kios")
        print_body("5. Kembali")

        pilihan = input("\nMasukkan pilihan:> ")

        if pilihan == "1":
            lihat_kios()
        elif pilihan == "2":
            registrasi_kios()
        elif pilihan == "3":
            ubah_kios()
        elif pilihan == "4":
            hapus_kios()
        elif pilihan == "5":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def lihat_kios():
    data_kios = csv.get(KIOS_ACCOUNT_PATH)
    while True:
        print_data_kios(data_kios)

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def registrasi_kios():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Kios > Registrasi Kios\n", start="\n")

        nama_kios = input_nama_kios()

        if nama_kios is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        nama_pemilik = input_nama_pemilik()

        if nama_pemilik is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        data_kios_baru = model_kios_account(nama_kios, nama_pemilik)

        print_data_kios([data_kios_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios = csv.get(KIOS_ACCOUNT_PATH)
            data_kios.append(data_kios_baru)
            hasil = csv.put(KIOS_ACCOUNT_PATH, data_kios)

            if hasil:
                print_alert("Kios berhasil didaftarkan", start="\n")
                break

            print_alert("Gagal mendaftarkan kios", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def ubah_kios():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Kios > Ubah Kios", start="\n")

        keyword = input("\nMasukkan ID/Nama Kios/Nama Pemilik:> ")

        data_kios = csv.get(KIOS_ACCOUNT_PATH)
        index = cari_kios(data_kios, keyword)

        if index == -1:
            print_alert("Data kios tidak ditemukan", start="\n")

            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break

            continue

        print_data_kios([data_kios[index]])
        print_body("Masukkan data baru:\n", start="\n")

        id_kios = data_kios[index]["id"]
        password_kios = data_kios[index]["password"]
        nama_kios = input("Masukkan nama kios:> ")
        nama_pemilik = input("Masukkan nama pemilik:> ")

        data_kios_baru = model_kios_account(
            nama_kios, nama_pemilik, id_kios, password_kios)

        print_data_kios([data_kios_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios[index] = data_kios_baru
            hasil = csv.put(KIOS_ACCOUNT_PATH, data_kios)

            if hasil:
                print_alert("Data kios berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data kios", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def hapus_kios():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Kios > Hapus Kios", start="\n")

        data_kios = csv.get(KIOS_ACCOUNT_PATH)
        keyword = input("\nMasukkan ID/Nama Kios/Nama Pemilik:> ")

        index = cari_kios(data_kios, keyword)

        if index == -1:
            print_alert("Data kios tidak ditemukan", start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print_data_kios([data_kios[index]])

        konfirmasi = input("\nHapus data kios tersebut? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios.pop(index)

            # Jika data kosong, tambahkan data kosong agar fungsi csv.put() tidak error
            if len(data_kios) == 0:
                data_kios.append(model_kios_account(None, None))

            hasil = csv.put(KIOS_ACCOUNT_PATH, data_kios)

            if hasil:
                print_alert("Data kios berhasil dihapus", start="\n")
                break

            print_alert("Gagal menghapus data kios", start="\n")

        print_alert("Kios tidak jadi dihapus", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def print_data_kios(list_kios):
    clear_screen()

    if len(list_kios) == 0:
        print_alert("Data kios kosong!", start="\n")
        return

    print_border()
    for kios in list_kios:
        print_body(f"ID: {kios['id']}", is_delayed=False)
        print_body(f"Nama Kios: {kios['nama_kios']}", is_delayed=False)
        print_body(f"Nama Pemilik: {kios['nama_pemilik']}", is_delayed=False)
        print_body(f"Password: {kios['password']}", is_delayed=False)
        print_border()
        time.sleep(0.24)


def input_nama_kios():
    data_kios = csv.get(KIOS_ACCOUNT_PATH)
    nama_kios = input("Masukkan nama kios:> ")

    if nama_kios == "":
        print_alert("Nama Kios tidak boleh kosong", start="\n")
        return

    if cari_kios(data_kios, nama_kios) != -1:
        print_alert("Nama Kios sudah terdaftar", start="\n")
        return

    return nama_kios


def input_nama_pemilik():
    data_kios = csv.get(KIOS_ACCOUNT_PATH)
    nama_pemilik = input("Masukkan nama pemilik:> ")

    if nama_pemilik == "":
        print_alert("Nama Pemilik tidak boleh kosong", start="\n")
        return

    if cari_kios(data_kios, nama_pemilik) != -1:
        print_alert("Nama Pemilik sudah terdaftar", start="\n")
        return

    return nama_pemilik


def cari_kios(data: list, keyword: str):
    for kios in data:
        id_kios = str(kios["id"])
        nama_kios = str(kios["nama_kios"]).upper()
        nama_pemilik = str(kios["nama_pemilik"]).upper()
        if id_kios == keyword or nama_kios == keyword.upper() or nama_pemilik == keyword.upper():
            return data.index(kios)
    return -1


def model_kios_account(nama_kios, nama_pemilik, id_kios=None, password=None):
    if id_kios is None:
        id_kios = generate_id()
    if password is None:
        password = generate_password()
    if nama_kios is None:
        return {
            "id": None,
            "nama_kios": None,
            "nama_pemilik": None,
            "password": None
        }
    return {
        "id": id_kios,
        "nama_kios": normalize_string(nama_kios),
        "nama_pemilik": normalize_string(nama_pemilik),
        "password": password
    }
