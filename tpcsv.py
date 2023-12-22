import os


def put(path: str, data: list):
    """
    Menulis data ke file dengan format CSV.

    Args:
        path (str): Alamat absolut file.
        data (list): List Dictionary yang akan ditulis ke file.

    Returns:
        bool: True jika data berhasil ditulis ke file CSV, False sebaliknya.
    """
    if data is None or len(data) == 0:
        return False

    with open(path, 'w') as f:
        # Mengambil header dari data
        row_headers = list(data[0].keys())

        # Menulis header tabel di csv berdasarkan key dictionary
        for row_header in row_headers:
            f.write(row_header.strip())
            # Jika bukan data terakhir, maka tambahkan koma
            if row_header != row_headers[-1]:
                f.write(",")

        f.write("\n")

        # Menulis data
        for data_row in data:
            for row_header in row_headers:
                f.write(str(data_row[row_header]).strip())
                # Jika bukan data terakhir, maka tambahkan koma
                if row_header != row_headers[-1]:
                    f.write(",")
            if data_row != data[-1]:
                f.write("\n")

        return True


def get(path: str):
    """
    Membaca data dari file CSV dan mengubahnya menjadi dictionaries.

    Args:
        path (str): Alamat absolut file.

    Returns:
        list: Daftar dictionaries yang mewakili data dari file CSV.
    """
    if not os.path.exists(path):
        return None

    with open(path, 'r') as f:
        # Membagi string menjadi list berdasarkan baris
        rows_str = f.read().strip().split("\n")

        # Membagi setiap string dalam list berdasarkan koma
        rows = []
        for row_str in rows_str:
            rows.append(row_str.split(","))

        # Mengubah list menjadi dictionary dengan index 0 sebagai key
        result = []
        for row_index in range(1, len(rows)):
            row_dict = {}
            for col_index in range(len(rows[row_index])):
                key = rows[0][col_index].strip()
                value = transform_data_type(rows[row_index][col_index])
                row_dict[key] = value
            result.append(row_dict)

        return result


def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_bool(string):
    if string == "True" or string == "False":
        return True
    else:
        return False


def transform_data_type(string):
    if is_int(string):
        return int(string)
    if is_float(string):
        return float(string)
    if is_bool(string):
        return bool(string)
    return string
