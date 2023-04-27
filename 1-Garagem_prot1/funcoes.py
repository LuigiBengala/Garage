import os
import sqlite3

def limpar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pressione_enter():
    input("Pressione Enter para continuar...")
    
#
# 
#   CARROS
# 
# 
    
def Inserir_veiculo():
    
    global conn
    conn = sqlite3.connect("garagem.db")
    
    marca = input("Marca-> ")
    modelo = input("Modelo-> ")
    cor = input("Cor-> ")
    dono = input("Dono-> ")
    
    sql = """
        INSERT INTO carros (marca, modelo, cor, dono) VALUES (?, ?, ?, ?);
    """
    
    c = conn.cursor()
    
    try:
        c.execute(sql, (marca, modelo, cor, dono))
        conn.commit()
        print("Carro inserido com sucesso!")
        pressione_enter()
    except Exception as error:
        print(f"Ocorreu um erro ao inserir o carro: {error}")
        pressione_enter()
    
    limpar_consola()
    
    pass

def ver_carros():
    
    limpar_consola()
    
    global conn
    conn = sqlite3.connect("garagem.db")
    
    sql = """
        SELECT * FROM carros;
    """
    
    c = conn.cursor(sql)
    
    for dados in c:
        print("----------- CARROS -----------")
        print("")
        print(f"Marca: {dados[1]}")
        print(f"Modelo: {dados[2]}")
        print(f"Cor: {dados[3]}")
        print(f"Dono: {dados[4]}")
        print("")
        print("-------------------------------")
    
    pass

def remover_carro():
    
    ver_carros()
    
    global conn
    conn = sqlite3.connect("garagem.db")
    
    id = int(input("ID do carro a remover-> "))
    
    sql = """
        DELETE FROM carros WHERE id = ?;
    """
    
    try:
        conn.execute(sql, (id,))
        conn.commit()
        print("O carro ", id, " foi removido com sucesso!")
        pressione_enter()
    except Exception as error:
        print(f"Ocorreu um erro ao remover o carro: {error}")
        pressione_enter()
        
#
# 
#   CONDUTORES
# 
# 

def inserir_condutor():
    global conn
    pass
