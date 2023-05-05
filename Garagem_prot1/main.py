from funcoes import *
from tables import *
import sqlite3

create_database()

option = 10000

while (option != 0):

    clear_console()
    
    print("# ----- MAIN MENU ----- #")
    print("1 - Display cars")
    print("2 - Display drivers")
    print("3 - Add car")
    print("4 - Add driver")
    print("5 - Remove Car")
    print("6 - Remove Driver")
    print("0 - Leave")
    
    option = int(input("Insert option (0-6)-> "))
    
    match option:
        case 1:
            show_cars()
            clear_console()
            pass
        case 2:
            display_drivers()
            pass
        case 3:
            add_carros()
            pass
        case 4:
            add_drivers()
            pass
        case 5:
            remove_cars()
            pass
        case 6:
            remove_drivers()
            pass
        case 0:
            clear_console()
            print("Leaving...")
            press_enter()
            clear_console()
            pass