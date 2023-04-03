from dotenv import load_dotenv

from ui import * # importa todas as funções do arquivo ui.py
from utilidades import * # importa todas as funções do arquivo utilidades.py

load_dotenv()  #carrega as variáveis de ambiente do ficheiro .env para a memória do programa

con = conectar_base_dados() # conecta a base de dados
cur = con.cursor(dictionary=True) # cria um cursor para a base de dados com o dicionário de dados ativado (para que os nomes das colunas sejam os nomes das variáveis)

def main():
    
    #ler_ficheiro_sql(cur,"dados.sql") # lê o ficheiro sql
    
    while True:
        limpar_consola() # limpa a consola
        print_menu_inicial() # imprime o menu inicial
        
        opcao = input_int("Selecione uma opção (0-4)-> ", 0, 4)
        limpar_consola()
        
        match opcao: # switch case
            case 0:
                break
            case 1:
                menu_inserir() # chama a função menu_inserir
                break
            case 2:
                limpar_consola() # limpa a consola
            case 3:
                print_menu_atualizar() # imprime o menu atualizar
            case 4:
                print_menu_remover() # imprime o menu remover
            
    con.close() # fecha a conexão com a base de dados
    
def menu_inserir():
    
    limpar_consola() # limpa a consola
    print_menu_inserir()
    
    opcao = input_int("Selecione uma opção (0-3)-> ", 0, 3)
    limpar_consola()
    
    match opcao: # switch case
        case 0:
            main()
        case 1:
            print_titulo("Inserir Carro")
            
            # -----------------  Caracteristicas do Carro  -----------------
            
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            ano = input_ano("Ano: ")
            cor = input("Cor: ")
            matricula = input("Matricula: ")
            num_portas = input_int("Numero de portas: ", 2, 5)
            num_lugares = input_int("Numero de lugares: ", 2, 9)
            combustivel = input("Combustivel: ")
            cilindrada = input_float("Cilindrada: ")
            potencia = input("Potencia: ")
            dono = input("Dono: ")
            
            # -----------------  Inserir Carro na Base de Dados  -----------------
            
            sql = "INSERT INTO carro (marca, modelo, ano, cor, matricula, num_portas, num_lugares, combustivel, cilindrada, potencia, dono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (marca, modelo, ano, cor, matricula, num_portas, num_lugares, combustivel, cilindrada, potencia, dono) # valores a inserir na base de dados
            
            cur.execute(sql, val) # executa o comando sql
            con.commit() # guarda as alterações na base de dados
            
            print("Carro inserido com sucesso!")
            press_enter()
            
            main()
        case 2:
            limpar_consola()
    

main() # chama a função main para iniciar o programa