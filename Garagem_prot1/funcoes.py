import os 
import classes
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

def add_carros():
    
    limpar_consola()
    
    global conn
    conn = sqlite3.connect('garagem.db')
    
    print("Insira os dados do carro: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    combustivel = input("Combustivel: ")
    cilindrada = float(input("Cilindrada: "))
    potencia = input("Potencia: ")
    num_lugares = int(input("Numero de lugares: "))
    
    sql = '''
        INSERT INTO carros(marca, modelo, ano, combustivel, cilindrada, potencia, num_lugares) VALUES(?,?,?,?,?,?,?);
    '''
    
    c = conn.cursor()
    
    try:
        c.execute(sql, (marca, modelo, ano, combustivel, cilindrada, potencia, num_lugares,))
        conn.commit()
        print("Carro adicionado com sucesso!")
        pressione_enter()
    except Exception as e:
        print("Erro: ", e)
        pressione_enter()
        
    limpar_consola()

def show_cars():
    
    limpar_consola()
    
    global conn
    conn = sqlite3.connect('garagem.db')
    
    sql = '''
        SELECT id, marca, modelo, ano, combustivel, cilindrada, potencia, num_lugares FROM carros;
    '''
    
    c = conn.execute(sql)
    
    print("# ----- CARROS ----- #")
    print(" ")
    
    for dados in c:
        print("ID: ", dados[0])
        print("Marca: ", dados[1])
        print("Modelo: ", dados[2])
        print("Ano: ", dados[3])
        print("Combustivel: ", dados[4])
        print("Cilindrada: ", dados[5])
        print("Potencia: ", dados[6])
        print("Numero de lugares: ", dados[7])
        print(" ")
        print("-------------------------------")
        print(" ")
