import os 
import classes
import ui
import sqlite3

lista_carros = list()
lista_motos = list()
lista_bicicleta = list()
lista_dono = list()

def limpar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pressione_enter():
    input("Pressione ENTER para continuar...")
    
# ----------- CARROS -----------
