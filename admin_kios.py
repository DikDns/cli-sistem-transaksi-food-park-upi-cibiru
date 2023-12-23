import tpcsv as csv
from utils import print_header, print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, generate_password, normalize_string


kios_account_path = get_absolute_path("data/kios_account.csv")


def admin_kios_panel():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

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
            edit_kios()
        elif pilihan == "4":
            hapus_kios()
        elif pilihan == "5":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def registrasi_kios():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Kios > Registrasi Kios", start="\n")

        nama_kios = input("\nMasukkan nama kios:> ")
        nama_pemilik = input("Masukkan nama pemilik:> ")

        data_kios_baru = {
            "id": generate_id(),
            "nama_kios": normalize_string(nama_kios),
            "nama_pemilik": normalize_string(nama_pemilik),
            "password": generate_password()
        }

        clear_screen()
        print_data_kios([data_kios_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios = csv.get(kios_account_path)
            data_kios.append(data_kios_baru)
            hasil = csv.put(kios_account_path, data_kios)

            if hasil:
                print_alert("Kios berhasil didaftarkan", start="\n")
                break

            print_alert("Gagal mendaftarkan kios", start="\n")

        konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def lihat_kios():
    while True:
        clear_screen()

        data_kios = csv.get(kios_account_path)

        print_data_kios(data_kios)

        konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def print_data_kios(list_kios):
    if len(list_kios) == 0:
        print_alert("Data kios kosong!", start="\n")
        return

    print_border()
    for kios in list_kios:
        print_body(f"ID: {kios['id']}")
        print_body(f"Nama Kios: {kios['nama_kios']}")
        print_body(f"Nama Pemilik: {kios['nama_pemilik']}")
        print_body(f"Password: {kios['password']}")
        print_border()
