from funcoes import *
from tables import *

create_database()

option = 10000

while (option != 0):

    clear_console()
    
    print("# ----- MAIN MENU ----- #")
    print("1 - Display cars")
    print("2 - Display drivers")
    print("3 - Add car")
    print("4 - Add driver")
    print("5 - Add driver to car")
    print("6 - Remove Car")
    print("7 - Remove Driver")
    print("0 - Leave")

    option = input_int("Insert option (0-7)-> ", 0, 7)
    
    match option:
        case 1:
            clear_console()
            show_cars()
            pass
        case 2:
            clear_console()
            display_drivers()
            pass
        case 3:
            add_cars()
            pass
        case 4:
            add_drivers()
            pass
        case 5:
            add_driver_to_car()
        case 6:
            remove_cars()
            pass
        case 7:
            remove_drivers()
            pass
        case 0:
            clear_console()
            print("Leaving...")
            press_enter()
            clear_console()
            pass
        case _:
            clear_console()
            print("Error! Invalid option!")
            press_enter()
            pass
