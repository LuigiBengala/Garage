import os
from datetime import datetime
import sqlite3


# ----------- Functions  -----------


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("Press ENTER to continue...")

def input_int(message: str, min: int | None = None, max: int | None = None) -> int:
    while True:
        try:
            value = int(input(message))
            
            if min is not None and value < min:
                print("Invalid value! Introduce an enteger, higher or equal to", min)
                continue
            if max is not None and value > max:
                print("Invalid value! Introduce an enteger, lower or equal to", max)
                continue
            return value
        except ValueError:
            print("Invalid value! Introduce an enteger!")

def input_float(message: str) -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid value! Introduce a float!")
        
def input_year(message: str) -> int:
    while True:
        year = int(input(message))
        actual_year = datetime.now().year
        if year > actual_year:
            print("Invalid value! Introduce a year lower or equal to", actual_year)
            continue
        return year


# ----------- CARS ----------------


def add_cars():

    clear_console()

    global conn
    conn = sqlite3.connect('garage.db')

    print("# ----- ADD CAR ----- #")
    brand = input("Brand: ")
    model = input("Model: ")
    plate = input("Plate: ")
    year = input_year("Year: ")
    fuel = input("Fuel: ")
    engine_capacity = input_float("Engine Capacity: ")
    engine_power = input("Engine Power (Horse Power): ")
    num_seats = input_int("Number of Seats: ", 1, 9)

    sql = '''
        INSERT INTO cars(brand, model, plate, year, fuel, engine_capacity, engine_power, num_seats) VALUES(?,?,?,?,?,?,?,?);
    '''

    c = conn.cursor()

    try:
        c.execute(sql, (brand, model, plate, year, fuel,
                  engine_capacity, engine_power, num_seats,))
        conn.commit()
        print("The car was added successfully!")
        press_enter()
    except Exception as error:
        print("Error: ", error)
        press_enter()

    clear_console()

def show_cars():

    global conn
    conn = sqlite3.connect('garage.db')

    sql = '''
        SELECT * FROM cars;
    '''

    c = conn.execute(sql)

    print("# ----- CARS ----- #")
    print(" ")
    print("-------------------------------")

    for data in c:
        
        sql_drivers = '''
            SELECT name FROM drivers WHERE id IN (SELECT driver_id FROM drivers_cars WHERE car_id = ?);
        '''
        
        drivers = conn.execute(sql_drivers, (data[0],))
        
        drivers_str = ""
        
        for driver in drivers:
            drivers_str += driver[0] + ", "
        
        print("ID: ", data[0])
        print("Drivers: ", drivers_str)
        print("Brand: ", data[1])
        print("Model: ", data[2])
        print("Plate: ", data[3])
        print("Year: ", data[4])
        print("Fuel: ", data[5])
        print("Engine Capacity: ", data[6])
        print("Engine Power(Horse Power): ", data[7])
        print("Number of Seats: ", data[8])
        print("-------------------------------")
        print(" ")
    press_enter()

def remove_cars():
    
        clear_console()
    
        global conn
        conn = sqlite3.connect('garage.db')
        
        show_cars()
    
        print("# ----- REMOVE CAR ----- #")
        id = input_int("Insert the ID of the car you want to remove: ")
    
        sql = '''
            DELETE FROM cars WHERE id = ?;
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
    years_of_license = input_year("Year you get your licence: ")
    
    sql = '''
        INSERT INTO drivers(name, drivers_license_type, years_of_license) VALUES(?,?,?);
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
        SELECT id, name, drivers_license_type, years_of_license FROM drivers;
    '''
    
    c = conn.execute(sql)
    
    print("")
    print("# ----- DRIVERS ----- #")
    print(" ")
    print("-------------------------------")
    
    for data in c:
        
        sql_cars = '''
            SELECT brand, model, plate FROM cars WHERE id IN (SELECT car_id FROM drivers_cars WHERE driver_id = ?);
        '''
        
        cars = conn.execute(sql_cars, (data[0],))
        
        cars_str = ""
        
        for car in cars:
            cars_str += car[0] + " " + car[1] + " / Plate -> " + car[2] + ", "
        
        print("ID: ", data[0])
        print("Name: ", data[1])
        print("Cars: ", cars_str)
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
    id = input_int("Insert the ID of the driver you want to remove: ")
    
    sql = '''
        DELETE FROM drivers WHERE id = ?;
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


# ----------- DRIVERS TO CARS -----------


def add_driver_to_car():
    
    clear_console()
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    show_cars()
    
    display_drivers()
    
    print("# ----- ADD DRIVER TO CAR ----- #")
    driver_id = input_int("Insert the ID of the driver: ")
    car_id = input_int("Insert the ID of the car: ")
    
    sql = '''
        INSERT INTO drivers_cars(driver_id, car_id) VALUES(?,?);
    '''
    
    c = conn.cursor()
    
    try:
        c.execute(sql, (driver_id, car_id,))
        conn.commit()
        print("The driver was added to the car successfully!")
        press_enter()
    except Exception as error:
        print("Error: ", error)
        press_enter()
    
    clear_console()
