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
    
# --------------------------------------------  Submenus  --------------------------------------------
    
# Menu Inserir

def print_menu_inserir():
    
    print_titulo("Inserir Veiculo")
    print("1 - Inserir Carro")
    print("2 - Inserir Moto")
    print("3 - Inserir Bicicleta")
    
# Menu Atualizar

def print_menu_atualizar():
    
    print("1 - Atualizar carros")
    print("2 - Atualizar moto")
    print("3 - Atualizar bicicletas")
    
# Menu Remover

def print_menu_remover():
    
    print("1 - Remover carros")
    print("2 - Remover moto")
    print("3 - Remover bicicletas")
    
# --------------------------------------------  SubSubMenus  --------------------------------------------

def print_menu_atualizarCarro():
    
    print("1 - Atualizar marca")
    print("2 - Atualizar modelo")
    print("3 - Atualizar cor")
    print("4 - Atualizar ano")
    print("5 - Atualizar combustivel")
    print("6 - Atualizar cilindrada")
    print("7 - Atualizar potencia")
    print("8 - Atualizar numero de lugares")
    print("9 - Atualizar dono")
    
def print_menu_atualizarMoto():
    
    print("1 - Atualizar marca")
    print("2 - Atualizar modelo")
    print("3 - Atualizar cor")
    print("4 - Atualizar ano")
    print("5 - Atualizar combustivel")
    print("6 - Atualizar cilindrada")
    print("7 - Atualizar potencia")
    print("8 - Atualizar dono")
    
def print_menu_atualizarBicicleta():
    
    print("1 - Atualizar marca")
    print("2 - Atualizar modelo")
    print("3 - Atualizar sistema de mudanças")
    print("4 - Atualizar ano")
    print("5 - Atualizar dono")
    