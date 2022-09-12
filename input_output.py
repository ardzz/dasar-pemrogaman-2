import os


def select_menu():
    menu = ["Penjumlahan", "Pengurangan", "Perkalian"
            "Pembagian", "Modulus", "Exponentiation"
            "Floor division", "Keluar"]
    return input("""
    Program kalkulator sederhana - Challenge 5

    Pilih menu operasi bilangan:

    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Modulus
    6. Exponentation
    7. Floor division
    8. Keluar

    Menu mana yang pengen kamu pilih? [1,2,3,4,5,6,7,8] """)


def input_number(message: str) -> int or float:
    return identify_number(input(message))


def identify_number(number) -> int or float:
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            raise ValueError
        except TypeError:
            raise TypeError


def calculate(calculation_name: str, operation: callable):
    try:
        bilangan_pertama = input_number(
            """
    Inputkan bilangan pertama: """)
        bilangan_kedua = input_number(
            """
    Inputkan bilangan kedua: """)
        kalkulasi = operation(bilangan_pertama, bilangan_kedua)
        print(
            """
    Hasil {} dari bilangan {} dan {} adalah {}""".format(calculation_name, bilangan_pertama, bilangan_kedua, kalkulasi))
    except ValueError or TypeError:
        print("Terjadi error, hanya diperbolehkan menginputkan bilangan bulat dan bilangan pecahan")


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')