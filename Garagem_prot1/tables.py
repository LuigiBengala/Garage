import sqlite3
from funcoes import *

def create_database():
    
    global conn
    conn = sqlite3.connect('garage.db')
    
    sql_cars = '''
        CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand text NOT NULL,
        model text NOT NULL,
        year integer NOT NULL,
        fuel text NOT NULL,
        engine_capacity float NOT NULL,
        engine_power text NOT NULL,
        num_seats integer NOT NULL
        ); 
    '''
    
    sql_drivers = '''
        CREATE TABLE IF NOT EXISTS condutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        drivers_license_type text NOT NULL,
        years_of_license integer NOT NULL                         
        );
    '''
    
    try:
        conn.executescript(sql_cars)
        conn.executescript(sql_drivers)
        conn.commit()
        print('Database created successfully!')
        press_enter()
    except Exception as error:
        print('Error: ', error)
        press_enter()