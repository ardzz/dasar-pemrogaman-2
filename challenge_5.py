from all_challenge import *

while True:
    clear_screen()
    option = select_menu()

    match option:
        case "1":
            challenge_1()

        case "2":
            challenge_2()

        case "3":
            challenge_3()

        case "4":
            challenge_4()

        case "5":
            modulus()

        case "6":
            exponentiation()

        case "7":
            floor_division()

        case "8":
            print("Keluar dari program")
            break;

        case _:
            print("""
        Nomer yang anda input tidak ada pada menu""")
