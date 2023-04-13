class carro:
    
    def __init__(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia,  num_lugares, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.num_lugares = num_lugares
        self.dono = dono
    
    def set_carro(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia,  num_lugares, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.num_lugares = num_lugares
        self.dono = dono
        
    def listar_carro(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)
        print("Combustivel: ", self.combustivel)
        print("Cilindrada: ", self.cilindrada)
        print("Potencia: ", self.potencia)
        print("Numero de Lugares: ", self.num_lugares)
        print("Dono: ", self.dono)
        
class moto:
    
    def __init__(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.dono = dono
    
    def set_moto(self, marca, modelo, cor, ano, combustivel, cilindrada, potencia, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel
        self.cilindrada = cilindrada
        self.potencia = potencia
        self.dono = dono
        
    def listar_moto(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)
        print("Combustivel: ", self.combustivel)
        print("Cilindrada: ", self.cilindrada)
        print("Potencia: ", self.potencia)
        print("Dono: ", self.dono)
        
        
class bicicleta:
    
    def __init__(self, marca, modelo, cor, ano, sistema_mudancas, dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.sistema_mudancas = sistema_mudancas
        self.dono = dono
    
    def set_bicicleta(self, marca, modelo, cor, ano, sistema_mudancas,dono):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.sistema_mudancas = sistema_mudancas
        self.dono = dono
        
    def listar_bicicleta(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Ano: ", self.ano)
        print("Sistema de Mudanças: ", self.sistema_mudancas)
        print("Dono: ", self.dono)
        
class dono:
    
    def __init__(self, nome):
        self.nome = nome
        
    def set_dono(self, nome):
        self.nome = nome
        
    def listar_dono(self):
        print("Nome: ", self.nome)