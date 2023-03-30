import os
from utilidades import *

# Limpar a consola

def limpar_consola():
    os.system("cls" if os.name == "nt" else "clear")
    
# Pressione Enter para continuar
    
def press_enter():
    input("Pressione Enter para continuar...") 
    
# Titulo

def print_titulo(titulo:str):
    print(f"<----- {titulo} ----->")
    
# Menu principal

def print_menu_inicial():
    
    print_titulo("Menu Principal")
    print("1 - Inserir...")
    print("2 - Listar Garagem")
    print("3 - Atualizar...")
    print("4 - Remover...")
    print("0 - Sair")
    
# Menu Inserir

def print_menu_inserir():
    
    print_titulo("Inserir Veiculo")
    print("1 - Inserir Carro")
    print("2 - Inserir Moto")
    print("3 - Inserir Bicicleta")