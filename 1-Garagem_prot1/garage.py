from dotenv import load_dotenv

from ui import * # importa todas as funções do arquivo ui.py
from utilidades import * # importa todas as funções do arquivo utilidades.py

load_dotenv() # carrega as variáveis de ambiente do ficheiro .env para a memória do programa

con = conectar_base_dados() # conecta a base de dados

cur = con.cursor(dictionary=True) # cria um cursor para a base de dados com o dicionário de dados ativado (para que os nomes das colunas sejam os nomes das variáveis)

def main():
    
    ler_ficheiro_sql(cur,"dados.sql") # lê o ficheiro sql
    
    while True:
        limpar_consola() # limpa a consola
        print_menu_inicial() # imprime o menu inicial
        
        opcao = input_int("Selecione uma opção (0-4)-> ", 0, 4)
        limpar_consola()
        
        match opcao: # switch case
            case 1: 
                print_menu_inserir() # imprime o menu inserir
            case 2:
                #listar_garagem() lista a garagem
                pass
            case 3:
                print_menu_atualizar() # imprime o menu atualizar
            case 4:
                print_menu_remover() # imprime o menu remover
                