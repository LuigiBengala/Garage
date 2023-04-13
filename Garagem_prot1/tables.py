import sqlite3
from funcoes import *

def criar_base_dados():
    
    global conn
    conn = sqlite3.connect('garagem.db')
    
    sql_carros = '''
        CREATE TABLE IF NOT EXISTS carros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca text NOT NULL,
        modelo text NOT NULL,
        ano integer NOT NULL,
        combustivel text NOT NULL,
        cilindrada float NOT NULL,
        potencia text NOT NULL,
        num_lugares integer NOT NULL,
        
        ); 
    '''