import sqlite3
from funcoes import *

def criar_base_dados():
    
    global conn
    conn = sqlite3.connect('garagem.db')
    
    sql_carros = '''
        CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca text NOT NULL,
        modelo text NOT NULL,
        ano integer NOT NULL,
        combustivel text NOT NULL,
        cilindrada float NOT NULL,
        potencia text NOT NULL,
        num_lugares integer NOT NULL
        ); 
    '''
    
    sql_condutores = '''
        CREATE TABLE IF NOT EXISTS condutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome text NOT NULL,
        tipo_de_carta text NOT NULL,
        anos_de_carta integer NOT NULL                         
        );
    '''
    
    try:
        conn.executescript(sql_carros)
        conn.executescript(sql_condutores)
        conn.commit()
        print('Base de dados criada com sucesso!')
        pressione_enter()
    except Exception as e:
        print('Erro: ', e)
        pressione_enter()