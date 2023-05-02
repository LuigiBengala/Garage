from classes import *
from tables import *
import sqlite3

criar_base_dados()

opcao = 10000

while (opcao != 0):

    limpar_consola()
    
    print("# ----- Menu Principal ----- #")
    print("1 - Ver carros")
    print("2 - Ver condutores")
    print("3 - Adicionar carro")
    print("4 - Remover carro")
    print("5 - Adicionar condutor")
    print("6 - Remover condutor")
    print("0 - Sair")
    
    opcao = int(input("Opcao: "))
    
    match opcao:
        case 1:
            show_cars()
            pressione_enter()
            pass
        case 2:
            # Ver condutores
            pass
        case 3:
            add_carros()
            pass
        case 4:
            # Remover carro
            pass
        case 5:
            # Adicionar condutor
            pass
        case 6:
            # Remover condutor
            pass