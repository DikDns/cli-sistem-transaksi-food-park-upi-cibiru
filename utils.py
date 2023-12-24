import os
import time
import uuid
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_id():
    return str(uuid.uuid4())[9:13]


def generate_password():
    return random.randint(100000, 999999)


def normalize_string(string: str):
    result = []
    for each_string in string.strip().split(" "):
        result.append(each_string.capitalize())
    return " ".join(result)


def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)


def print_header(string: str, start="", end="\n", is_delayed=True):
    content = f"{start}[]====|{string:^32}|====[]"
    if is_delayed:
        print_delay(content, end=end)
    else:
        print(content, end=end)

 
def print_body(string: str, start="", end="\n", is_delayed=True):
    content = f"{start}[]=| {string}"
    if is_delayed:
        print_delay(content, end=end)
    else:
        print(content, end=end)


def print_border():
    print(f"[]{42*'='}[]")


def print_alert(string: str, start="", end="\n", is_delayed=False):
    print_body(string, start=start, end=end, is_delayed=is_delayed)
    input("Tekan enter untuk melanjutkan...")


def print_delay(string: str, delay=0.01, end="\n"):
    for char in string:
        print(char, end="", flush=True)
        time.sleep(delay)
    print(end=end)
