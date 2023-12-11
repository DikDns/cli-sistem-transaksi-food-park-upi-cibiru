
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
        return bool(string)
    return string