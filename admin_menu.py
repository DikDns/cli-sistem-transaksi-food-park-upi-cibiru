import time
import tpcsv as csv
from utils import print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, normalize_string
from admin_utils import brand, input_konfirmasi_kembali
from admin_kios import KIOS_ACCOUNT_PATH, cari_kios

MENU_PATH = get_absolute_path("data/menu.csv")
PESAN_KONFIRMASI = "\nKembali ke Panel Menu? (Y/N):> "
PESAN_TIDAK_ADA_MENU = "Data menu tidak ditemukan!"


def admin_menu_panel():
    while True:
        brand()

        print_body("Panel Admin > Mengelola Menu", start="\n")

        print_body("Pilih menu sesuai angka:", start="\n")
        print_body("1. Lihat Semua Menu")
        print_body("2. Verifikasi Menu")
        print_body("3. Tambah Menu")
        print_body("4. Ubah Menu")
        print_body("5. Hapus Menu")
        print_body("6. Kembali")

        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            lihat_menu()
        elif pilihan == "2":
            verifikasi_menu()
        elif pilihan == "3":
            tambah_menu()
        elif pilihan == "4":
            ubah_menu()
        elif pilihan == "5":
            hapus_menu()
        elif pilihan == "6":
            clear_screen()
            break
        else:
            print_alert("Pilihan tidak tersedia", start="\n")


def lihat_menu():
    data_menu = csv.get(MENU_PATH)
    while True:
        print_menu(data_menu)

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def verifikasi_menu():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Menu > Verifikasi Menu\n", start="\n")

        id_menu = input("Masukkan ID Menu yang akan diverifikasi:> ")

        data_menu = csv.get(MENU_PATH)
        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert(PESAN_TIDAK_ADA_MENU, start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print_menu([data_menu[index]])

        konfirmasi = input("\nVerifikasi menu tersebut? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu[index]["sudah_terverifikasi"] = True

            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Menu berhasil diverifikasi!", start="\n")
                break

            print_alert("Gagal mengubah data menu", start="\n")

        print_alert("Menu tidak jadi diverifikasi", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def tambah_menu():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Kios > Tambah Menu\n", start="\n")

        judul_menu = input_judul_menu()

        if judul_menu is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        harga_menu = input_harga_menu()

        if harga_menu is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        keyword = input("Masukkan ID Kios/Nama Kios/Nama Pemilik:> ")

        data_kios = csv.get(KIOS_ACCOUNT_PATH)
        index = cari_kios(data_kios, keyword)

        if index == -1:
            print_alert("Kios tidak ditemukan!", start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        data_menu_baru = model_menu(
            judul_menu, harga_menu, data_kios[index]["id"], True)

        print_menu([data_menu_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu = csv.get(MENU_PATH)
            data_menu.append(data_menu_baru)

            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Menu berhasil ditambahkan", start="\n")
                break

            print_alert("Gagal menambahkan menu", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def ubah_menu():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Menu > Ubah Menu", start="\n")

        id_menu = input("\nMasukkan ID Menu yang akan diubah:> ")

        data_menu = csv.get(MENU_PATH)
        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert(PESAN_TIDAK_ADA_MENU, start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print_menu([data_menu[index]])

        print_body("Masukkan data baru:\n", start="\n")

        id_menu = data_menu[index]["id"]
        id_kios = data_menu[index]["id_kios"]
        judul_menu = input_judul_menu()

        if judul_menu is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        harga_menu = input_harga_menu()

        if harga_menu is None:
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        sudah_terverifikasi = input("Verifikasi Menu? (Y/N):> ")

        if sudah_terverifikasi.upper() == "Y":
            sudah_terverifikasi = True
        else:
            sudah_terverifikasi = False

        data_menu_baru = model_menu(
            judul_menu, harga_menu, id_kios, sudah_terverifikasi, id_menu)

        print_menu([data_menu_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu[index] = data_menu_baru
            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Data menu berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data menu", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def hapus_menu():
    while True:
        brand()
        print_body("Panel Admin > Mengelola Menu > Hapus Menu", start="\n")

        id_menu = input("\nMasukkan ID Menu yang akan dihapus:> ")

        data_menu = csv.get(MENU_PATH)
        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert(PESAN_TIDAK_ADA_MENU, start="\n")
            if input_konfirmasi_kembali(PESAN_KONFIRMASI):
                break
            continue

        print_menu([data_menu[index]])

        konfirmasi = input("\nHapus menu tersebut? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu.pop(index)

            # Jika data kosong, tambahkan data kosong agar fungsi csv.put() tidak error
            if len(data_menu) == 0:
                data_menu.append(model_menu(None, None, None))

            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Menu berhasil dihapus!", start="\n")
                break

            print_alert("Gagal menghapus menu", start="\n")

        print_alert("Menu tidak jadi dihapus", start="\n")

        if input_konfirmasi_kembali(PESAN_KONFIRMASI):
            break


def print_menu(list_menu):
    clear_screen()

    if len(list_menu) == 0:
        print_alert("Data menu kosong!", start="\n")
        return

    data_kios = csv.get(KIOS_ACCOUNT_PATH)

    print_border()
    for menu in list_menu:
        index = cari_kios(data_kios, menu["id_kios"])
        nama_kios = data_kios[index]['nama_kios'] if index != -1 else None
        print_body(f"ID: {menu['id']}", is_delayed=False)
        print_body(f"Judul: {menu['judul']}", is_delayed=False)
        print_body(f"Harga: {menu['harga']}", is_delayed=False)
        print_body(
            f"Status: {'Terverifikasi' if menu['sudah_terverifikasi'] else 'Belum Terverifikasi'}", is_delayed=False)
        print_body(f"Kios: {nama_kios}", is_delayed=False)
        print_border()
        time.sleep(0.24)


def input_judul_menu():
    judul_menu = input("Masukkan Judul Menu:> ")

    if judul_menu == "":
        print_alert("Judul menu tidak boleh kosong!", start="\n")
        return

    return judul_menu


def input_harga_menu():
    harga_menu = input("Masukkan Harga Menu:> ")

    if not harga_menu.isdigit():
        print_alert("Harga menu harus angka!", start="\n")
        return

    return harga_menu


def cari_menu(list_menu: list, keyword: str):
    for menu in list_menu:
        if menu["id"] == keyword:
            return list_menu.index(menu)
    return -1


def update_menu(data_menu):
    sorted_data_menu = sort_menu_by_status(data_menu)
    return csv.put(MENU_PATH, sorted_data_menu)


def sort_menu_by_status(data_menu):
    for i in range(len(data_menu) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if data_menu[j]["sudah_terverifikasi"] and not data_menu[pos_max]["sudah_terverifikasi"]:
                pos_max = j
        data_menu[i], data_menu[pos_max] = data_menu[pos_max], data_menu[i]
    return data_menu


def model_menu(judul, harga, id_kios, sudah_terverifikasi=False, id_menu=None):
    if id_menu is None:
        id_menu = generate_id()
    if judul is None:
        return {
            "id": None,
            "judul": None,
            "harga": None,
            "sudah_terverifikasi": None,
            "id_kios": None,
        }
    return {
        "id": id_menu,
        "judul": normalize_string(judul),
        "harga": int(harga),
        "sudah_terverifikasi": sudah_terverifikasi,
        "id_kios": id_kios,
    }
