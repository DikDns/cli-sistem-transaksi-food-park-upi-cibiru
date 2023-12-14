
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
    elif is_float(string):
        return float(string)
    elif is_bool(string):
        return True if string == "True" else False
    return string


def create_csv(path: str, data: list):
    """
    Menulis data ke file dengan format CSV.

    Args:
        path (str): Alamat absolut file.
        data (list): List Dictionary yang akan ditulis ke file.

    Returns:
        bool: True jika data berhasil ditulis ke file CSV, False jika sebaliknya.
    """
    with open(path, 'w') as f:
        # Mengambil header dari data
        header = list(data[0].keys())

        # Menulis header tabel di csv berdasarkan key dictionary
        for j in range(len(header)):
            f.write(header[j])
            # Jika bukan data terakhir, maka tambahkan koma
            if j != len(data[0]) - 1:
                f.write(",")

        f.write("\n")

        # Menulis data
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][header[j]]))
                # Jika bukan data terakhir, maka tambahkan koma
                if j != len(data[i]) - 1:
                    f.write(",")
            if i != len(data) - 1:
                f.write("\n")

        return True

def read_csv(path: str):
    """
    Membaca data dari file dengan format CSV dan mengubahnya menjadi dictionaries.

    Args:
        path (str): Alamat absolut file.

    Returns:
        list: Daftar dictionaries yang mewakili data dari file dengan format CSV.
    """
    with open(path, 'r') as f:
        # Membaca file txt menjadi string
        string = f.read()
        # Membagi string menjadi list berdasarkan baris
        list_of_string = string.split("\n")

        # Membagi setiap string dalam list berdasarkan koma
        for i in range(len(list_of_string)):
            list_of_string[i] = list_of_string[i].split(",")

        temp = []

        # Mengubah list menjadi dictionary dengan index 0 sebagai key
        for i in range(1, len(list_of_string)):
            temp.append({})
            for j in range(len(list_of_string[i])):
                temp[i-1][list_of_string[0][j]] = transform_data_type(list_of_string[i][j])

        return temp
    

def append_csv(path: str, data: list):
    """
    Menambahkan data ke baris akhir file dengan format CSV.

    Args:
        path (str): Alamat absolut file.
        data (list): List Dictionary yang akan ditambahkan ke file.

    Returns:
        bool: True jika data berhasil ditambahkan ke file CSV, False jika sebaliknya.
    """
    with open(path, 'a') as f:
        # Mengambil header dari data
        header = list(data[0].keys())

        # Menulis data
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][header[j]]))
                # Jika bukan data terakhir, maka tambahkan koma
                if j != len(data[i]) - 1:
                    f.write(",")
            if i != len(data) - 1:
                f.write("\n")

        return True

def update_csv(path: str, data: list):
    """
    Mengubah data dalam file dengan format CSV.

    Args:
        path (str): Alamat absolut file.
        data (list): List Dictionary yang akan mengubah data file.

    Returns:
        bool: True jika file CSV berhasil diubah, False jika sebaliknya.
    """
    headers = list(data[0].keys())

    # Membaca data dari file
    temp = read_csv(path)

    temp_status = False
    # Menambahkan data baru
    for i in range(len(data)):
        for j in range(len(headers)):
            if data[i][headers[j]] != temp[i][headers[j]]:
                temp[i][headers[j]] = data[i][headers[j]]
                temp_status = True

    # Jika data tidak ada yang berubah, tambahkan data baru
    if not temp_status:
        return append_csv(path, data)
    
    return create_csv(path, temp)



# dir_path = __file__.split("\\")[:-1]

# data = update_csv(f"{dir_path}\\..\\data\\data_dummy.txt", [{"id": 1, "username": "admin", "password": "admin"}])



# create_csv("C:\Users\Ardi\Documents\GitHub\cli-sistem-transaksi-food-park-upi-cibiru\data\data_dummy.txt")