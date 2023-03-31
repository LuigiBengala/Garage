
#Veiculos de 4 rodas

class Carro:
    
    #Atributos
    
    marca = ""
    modelo = ""
    cor = ""
    ano = ""
    combustivel = ""
    cilindrada = ""
    potencia = ""
    num_lugares = ""
    dono = ""
    
    #Metodo construtor

    def __init__(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, num_lugares, dono):
        self.marca = marca #self é o objeto que está a ser criado
        self.modelo = modelo 
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.num_lugares = num_lugares
        self.dono = dono
        pass

    #Metodos

    def registar(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, num_lugares, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.num_lugares = num_lugares
        self.dono = dono
        pass
    
    def listar_informacao(self):
        
        print("-" * 20 + self.dono + "-" * 20)
        print(self.marca)
        print(self.modelo)
        print(self.cor)
        print(self.ano)
        print(self.combustivel)
        print(self.cilindrada)
        print(self.potencia)
        print(self.num_lugares)
        pass
    

class Moto:
    
    #Atributos
    
    marca = ""
    modelo = ""
    cor = ""
    ano = ""
    combustivel = ""
    cilindrada = ""
    potencia = ""
    dono = ""
    
    #Metodo construtor

    def __init__(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.dono = dono
        pass

    #Metodos

    def registar(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.dono = dono
        pass
    
    def listar_informacao(self):
        
        print("-" * 20 + self.dono + "-" * 20)
        print(self.marca)
        print(self.modelo)
        print(self.cor)
        print(self.ano)
        print(self.combustivel)
        print(self.cilindrada)
        print(self.potencia)
        pass
    
class bicicleta:
    
    #Atributos
    
    marca = ""
    modelo = ""
    ano = ""
    sistema_mudancas = ""
    dono = ""
    
    #Metodo construtor

    def __init__(self, marca, modelo, ano, sistema_mudancas, dono):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.sistema_mudancas = sistema_mudancas
        self.dono = dono
        pass

    #Metodos

    def registar(self, marca, modelo, ano, sistema_mudancas, dono):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.sistema_mudancas = sistema_mudancas
        self.dono = dono
        pass
    
    def listar_informacao(self):
        
        print("-" * 20 + self.dono + "-" * 20)
        print(self.marca)
        print(self.modelo)
        print(self.ano)
        print(self.sistema_mudancas)
        print(self.dono)
        pass
    
