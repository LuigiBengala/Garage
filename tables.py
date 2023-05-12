import sqlite3
from funcoes import *

def create_database():
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    sql_cars = '''
        CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        fuel TEXT NOT NULL,
        engine_capacity FLOAT NOT NULL,
        engine_power TEXT NOT NULL,
        num_seats INTEGER NOT NULL
        ); 
    '''
    
    sql_drivers = '''
        CREATE TABLE IF NOT EXISTS drivers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        drivers_license_type TEXT NOT NULL,
        years_of_license INTEGER NOT NULL                         
        );
    '''
    
    sql_drivers_car = '''
        CREATE TABLE IF NOT EXISTS drivers_cars (  
        driver_id INTEGER REFERENCES drivers(id),
        car_id INTEGER REFERENCES cars(id)
        );
    '''
    
    try:
        conn.executescript(sql_cars)
        conn.executescript(sql_drivers)
        conn.executescript(sql_drivers_car)
        conn.commit()
    except Exception as error:
        print('Error: ', error)
        press_enter()