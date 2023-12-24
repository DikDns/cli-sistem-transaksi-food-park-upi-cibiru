import tpcsv as csv
from utils import print_header, print_body, print_border, print_alert, clear_screen, get_absolute_path, generate_id, generate_password, normalize_string
from admin_kios import kios_account_path, cari_kios

menu_path = get_absolute_path("data/menu.csv")


def admin_menu_panel():
    while True:
        clear_screen()

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

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
    data_menu = csv.get(menu_path)
    while True:
        clear_screen()

        print_menu(data_menu)

        konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def verifikasi_menu():
    while True:
        clear_screen()

        data_menu = csv.get(menu_path)

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Menu > Verifikasi Menu", start="\n")

        id_menu = input("\nMasukkan ID Menu yang akan diverifikasi:> ")

        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert("Data menu tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")
            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

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

        konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def tambah_menu():
    while True:
        data_kios = csv.get(kios_account_path)

        clear_screen()

        print_border()
        print_header("Food Park UPI")
        print_border()

        print_body("Panel Admin > Mengelola Kios > Tambah Menu", start="\n")

        judul_menu = input("\nMasukkan Judul Menu:> ")
        harga_menu = input("Masukkan Harga Menu:> ")

        if not harga_menu.isdigit():
            print_alert("Harga menu harus angka!", start="\n")
            continue

        id_kios = input("Masukkan ID Kios:> ")

        if cari_kios(data_kios, id_kios) == -1:
            print_alert("ID Kios tidak ditemukan!", start="\n")
            continue

        data_menu_baru = model_menu(judul_menu, harga_menu, id_kios, True)

        clear_screen()

        print_menu([data_menu_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu = csv.get(menu_path)
            data_menu.append(data_menu_baru)

            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Menu berhasil ditambahkan", start="\n")
                break

            print_alert("Gagal menambahkan menu", start="\n")

        konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def ubah_menu():
    while True:
        clear_screen()

        data_menu = csv.get(menu_path)

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Menu > Ubah Menu", start="\n")

        id_menu = input("\nMasukkan ID Menu yang akan diubah:> ")

        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert("Data menu tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")
            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

        print_menu([data_menu[index]])

        print_body("Masukkan data baru:", start="\n")

        id_menu = data_menu[index]["id"]
        id_kios = data_menu[index]["id_kios"]
        judul_menu = input("Masukkan Judul Menu:> ")
        harga_menu = input("Masukkan Harga Menu:> ")

        if not harga_menu.isdigit():
            print_alert("Harga menu harus angka!", start="\n")
            continue

        sudah_terverifikasi = input("Verifikasi Menu? (Y/N):> ")

        if sudah_terverifikasi.upper() == "Y":
            sudah_terverifikasi = True
        else:
            sudah_terverifikasi = False

        data_menu_baru = model_menu(
            judul_menu, harga_menu, id_kios, sudah_terverifikasi, id_menu)

        clear_screen()

        print_menu([data_menu_baru])

        konfirmasi = input("\nData sudah sesuai? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            data_menu[index] = data_menu_baru
            hasil = update_menu(data_menu)

            if hasil:
                print_alert("Data menu berhasil diubah", start="\n")
                break

            print_alert("Gagal mengubah data menu", start="\n")

        konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def hapus_menu():
    while True:
        clear_screen()

        data_menu = csv.get(menu_path)

        print_border()
        print_header("Food Park UPI", is_delayed=False)
        print_border()

        print_body("Panel Admin > Mengelola Menu > Hapus Menu", start="\n")

        id_menu = input("\nMasukkan ID Menu yang akan dihapus:> ")

        index = cari_menu(data_menu, id_menu)

        if index == -1:
            print_alert("Data menu tidak ditemukan", start="\n")
            konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")
            if konfirmasi.upper() == "Y":
                break
            continue

        clear_screen()

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

        konfirmasi = input("\nKembali ke Panel Menu? (Y/N):> ")

        if konfirmasi.upper() == "Y":
            break


def print_menu(list_menu):
    if len(list_menu) == 0:
        print_alert("Data menu kosong!", start="\n")
        return

    data_kios = csv.get(kios_account_path)

    print_border()
    for menu in list_menu:
        index = cari_kios(data_kios, menu["id_kios"])
        nama_kios = data_kios[index]['nama_kios'] if index != -1 else None
        print_body(f"ID: {menu['id']}")
        print_body(f"Judul: {menu['judul']}")
        print_body(f"Harga: {menu['harga']}")
        print_body(
            f"Status: {'Terverifikasi' if menu['sudah_terverifikasi'] else 'Belum Terverifikasi'}")
        print_body(f"Kios: {nama_kios}")
        print_border()


def cari_menu(list_menu: list, keyword: str):
    for menu in list_menu:
        if menu["id"] == keyword:
            return list_menu.index(menu)
    return -1


def update_menu(data_menu):
    sorted_data_menu = sort_menu_by_status(data_menu)
    return csv.put(menu_path, sorted_data_menu)


def sort_menu_by_status(data_menu):
    for i in range(len(data_menu) - 1, 0, -1):
        pos_max = 0
        for j in range(1, i + 1):
            if data_menu[j]["sudah_terverifikasi"] and not data_menu[pos_max]["sudah_terverifikasi"]:
                pos_max = j
        data_menu[i], data_menu[pos_max] = data_menu[pos_max], data_menu[i]
    return data_menu


def model_menu(judul, harga, id_kios, sudah_terverifikasi=False, id_menu=generate_id()):
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
        "harga": harga,
        "sudah_terverifikasi": sudah_terverifikasi,
        "id_kios": id_kios,
    }
