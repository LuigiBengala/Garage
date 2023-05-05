import os
import sqlite3


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter():
    input("Press ENTER to continue...")

# ----------- CARS -----------


def add_carros():

    clear_console()

    global conn
    conn = sqlite3.connect('garage.db')

    print("# ----- ADD CAR ----- #")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Year: "))
    fuel = input("Fuel: ")
    engine_capacity = float(input("Engine Capacity: "))
    engine_power = input("Engine Power (Horse Power): ")
    num_seats = int(input("Number of Seats: "))

    sql = '''
        INSERT INTO carros(brand, model, year, fuel, engine_capacity, engine_power, num_seats) VALUES(?,?,?,?,?,?,?);
    '''

    c = conn.cursor()

    try:
        c.execute(sql, (brand, model, year, fuel,
                  engine_capacity, engine_power, num_seats,))
        conn.commit()
        print("The car was added successfully!")
        press_enter()
    except Exception as error:
        print("Error: ", error)
        press_enter()

    clear_console()

def show_cars():

    clear_console()

    global conn
    conn = sqlite3.connect('garage.db')

    sql = '''
        SELECT id, brand, model, year, fuel, engine_capacity, engine_power, num_seats FROM carros;
    '''

    c = conn.execute(sql)

    print("# ----- CARS ----- #")
    print(" ")
    print("-------------------------------")

    for data in c:
        print("ID: ", data[0])
        print("Brand: ", data[1])
        print("Model: ", data[2])
        print("Year: ", data[3])
        print("Fuel: ", data[4])
        print("Engine Capacity: ", data[5])
        print("Engine Power(Horse Power): ", data[6])
        print("Number of Seats: ", data[7])
        print("-------------------------------")
        print(" ")
    press_enter()

def remove_cars():
    
        clear_console()
    
        global conn
        conn = sqlite3.connect('garage.db')
        
        show_cars()
    
        print("# ----- REMOVE CAR ----- #")
        id = int(input("Insert the ID of the car you want to remove: "))
    
        sql = '''
            DELETE FROM carros WHERE id = ?;
        '''
    
        c = conn.cursor()
    
        try:
            c.execute(sql, (id,))
            conn.commit()
            print("The car was removed successfully!")
            press_enter()
        except Exception as error:
            print("Error: ", error)
            press_enter()
    
        clear_console()


# ----------- DRIVERS -----------


def add_drivers():
    clear_console()
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    print("# ----- ADD DRIVER ----- #")
    name = input("Name: ")
    drivers_license_type = input("Drivers License Type: ")
    years_of_license = int(input("Years of License: "))
    
    sql = '''
        INSERT INTO condutores(name, drivers_license_type, years_of_license) VALUES(?,?,?);
    '''
    
    c = conn.cursor()
    
    try:
        c.execute(sql, (name, drivers_license_type, years_of_license,))
        conn.commit()
        print("The driver was added successfully!")
        press_enter()
    except Exception as error:
        print("Error: ", error)
        press_enter()

def display_drivers():
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    sql = '''
        SELECT id, name, drivers_license_type, years_of_license FROM condutores;
    '''
    
    c = conn.execute(sql)
    
    print("")
    print("# ----- DRIVERS ----- #")
    print(" ")
    print("-------------------------------")
    
    for data in c:
        print("ID: ", data[0])
        print("Name: ", data[1])
        print("Drivers License Type: ", data[2])
        print("Years of License: ", data[3])
        print("-------------------------------")
        print(" ")
    press_enter()

def remove_drivers():
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    display_drivers()
    
    print("# ----- REMOVE DRIVER ----- #")
    id = int(input("Insert the ID of the driver you want to remove: "))
    
    sql = '''
        DELETE FROM condutores WHERE id = ?;
    '''
    
    c = conn.cursor()
    
    try:
        c.execute(sql, (id,))
        conn.commit()
        print("The driver was removed successfully!")
        press_enter()
    except Exception as error:
        print("Error: ", error)
        press_enter()
    
    clear_console()
