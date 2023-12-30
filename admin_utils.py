from utils import print_border, print_header, clear_screen


def brand():
    clear_screen()
    print_border()
    print_header("Food Park UPI", is_delayed=False)
    print_border()


def input_konfirmasi_kembali():
    konfirmasi = input("\nKembali ke Panel Kios? (Y/N):> ")
    if konfirmasi.upper() == "Y":
        return True
    return False
