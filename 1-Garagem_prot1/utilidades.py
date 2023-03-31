import os
from datetime import datetime
from mysql.connector import connect, cursor

#Verificar se é um inteiro

def input_int(mensagem: str, min: int | None = None, max: int | None = None) -> int: 
    while True:
        try:
            valor = int(input(mensagem)) # tenta converter o valor para inteiro
            
            #Se o valor 
            
            if min is not None and valor < min: # se o valor for menor que o minimo 
                print(f"O valor tem de ser maior ou igual a {min}")
                continue
            
            if max is not None and valor > max: # se o valor for maior que o maximo
                print(f"O valor tem de ser menor ou igual a {max}")
                continue
            
            return valor
        
        except ValueError: # se o valor não for um inteiro
            print("O valor tem de ser um inteiro")
             
#None = None, max: int se o valor for maior que o maximo 
#-> int retorna um inteiro

#Verificar se é um float

def input_float(mensagem: str)-> float:
    while True:
        try:
            return float(input(mensagem)) # tenta converter o valor para float
        except ValueError:
            print("O valor tem de ser um float")

#Verificar se o ano é valido

def input_ano(mensagem: str)-> int: 
    while True:
        ano = input_int(mensagem, None, None) # ano inserido pelo utilizador 
        ano_atual = datetime.now().year # ano atual
        if ano > ano_atual:
            print(f"Ano invalido! Não pode inserir um ano superior ao {ano_atual}")
            continue
        return ano
    
#Conectar a base de dados

def conectar_base_dados():
    
    configData = {
        "user": "root",
        "password": "root",
        "host": "127.0.0.1",
        "port": 3306,
        "database": "my_garage"
    }

    conn = connect(**configData)
    return conn

#Ler ficheiro sql

def ler_ficheiro_sql(cursor: cursor.MySQLCursor, ficheiro_sql: str): # recebe o cursor e o ficheiro sql 
    with open(ficheiro_sql, "r") as f: # abre o ficheiro sql para leitura
        sql = f.read() # le o ficheiro sql
        cursor.execute(sql, multi=True) # executa o ficheiro sql
            
def get_carro(cursor: cursor.MySQLCursor, termo: str | int):
    sql = "SELECT * FROM carro WHERE matricula = %s OR dono = %s"
    val = (termo, termo)
