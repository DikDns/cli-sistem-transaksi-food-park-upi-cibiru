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
            ubah_kios()
        elif pilihan == "4":
            hapus_kios()
        elif pilihan == "5":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def lihat_kios():
    data_kios = csv.get(kios_account_path)
    while True:
        clear_screen()

        print_data_kios(data_kios)

        konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def registrasi_kios():
    while True:
        data_kios = csv.get(kios_account_path)

        clear_screen()

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Kios > Registrasi Kios", start="\n")

        nama_kios = input("\nMasukkan nama kios:> ")
        nama_pemilik = input("Masukkan nama pemilik:> ")

        if cari_kios(data_kios, nama_kios) != -1:
            print_alert("Nama Kios atau Pemilik sudah terdaftar", start="\n")
            continue

        data_kios_baru = model_kios_account(nama_kios, nama_pemilik)

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


def ubah_kios():
    while True:
        clear_screen()

        data_kios = csv.get(kios_account_path)

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Kios > Ubah Kios", start="\n")

        keyword = input("\nMasukkan ID/Nama Kios/Nama Pemilik:> ")

        index = cari_kios(data_kios, keyword)

        if index == -1:
            print_alert("Data kios tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

        print_data_kios([data_kios[index]])

        print_body("Masukkan data baru:", start="\n")

        id_kios = data_kios[index]["id"]
        password_kios = data_kios[index]["password"]
        nama_kios = input("Masukkan nama kios:> ")
        nama_pemilik = input("Masukkan nama pemilik:> ")

        data_kios_baru = model_kios_account(
            nama_kios, nama_pemilik, id_kios, password_kios)

        clear_screen()

        print_data_kios([data_kios_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios[index] = data_kios_baru
            hasil = csv.put(kios_account_path, data_kios)

            if hasil:
                print_alert("Data kios berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data kios", start="\n")

        konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def hapus_kios():
    while True:
        clear_screen()

        data_kios = csv.get(kios_account_path)

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Kios > Hapus Kios", start="\n")

        keyword = input("\nMasukkan ID/Nama Kios/Nama Pemilik:> ")

        index = cari_kios(data_kios, keyword)

        if index == -1:
            print_alert("Data kios tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")

            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

        print_data_kios([data_kios[index]])

        konfirmasi = input("\nHapus data kios tersebut? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_kios.pop(index)

            # Jika data kosong, tambahkan data kosong agar fungsi csv.put() tidak error
            if len(data_kios) == 0:
                data_kios.append(model_kios_account(None, None))

            hasil = csv.put(kios_account_path, data_kios)

            if hasil:
                print_alert("Data kios berhasil dihapus", start="\n")
                break

            print_alert("Gagal menghapus data kios", start="\n")

        print_alert("Kios tidak jadi dihapus", start="\n")

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


def cari_kios(data, keyword):
    for i in range(len(data)):
        id_kios = data[i]["id"]
        nama_kios = data[i]["nama_kios"].upper()
        nama_pemilik = data[i]["nama_pemilik"].upper()
        if id_kios == keyword or nama_kios == keyword.upper() or nama_pemilik == keyword.upper():
            return i
    return -1


def model_kios_account(nama_kios, nama_pemilik, id_kios=generate_id(), password=generate_password()):
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
