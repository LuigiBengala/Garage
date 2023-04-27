import sqlite3
from funcoes import *

def criar_base_dados():
    
    global conn
    conn = sqlite3.connect("garagem.db")
    
    sql_carros = """
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        matricula TEXT NOT NULL,
        cor TEXT NOT NULL,
    );
    """
    
    sql_condutores = """
    CREATE TABLE IF NOT EXISTS condutores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        anos_carta INTEGER NOT NULL,
        prox_renovacao TEXT NOT NULL
    );
    """
    
    