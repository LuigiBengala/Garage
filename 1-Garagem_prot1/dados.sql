
-- Criação tabela de carro

CREATE TABLE IF NOT EXISTS 'carro'(

    id int AUTO_INCREMENT PRIMARY KEY,
    marca varchar(50) NOT NULL,
    modelo varchar(50) NOT NULL,
    ano int NOT NULL,
    cor varchar(50) NOT NULL,
    matricula varchar(50) NOT NULL,
    num_portas int NOT NULL,
    num_lugares int NOT NULL,
    combustivel varchar(50) NOT NULL,
    cilindrada int NOT NULL,
    potencia int NOT NULL,
);

CREATE INDEX IF NOT EXISTS index_carro_marca ON carro(marca); -- Index para marca do carro (para pesquisa) 

-- Criação tabela mota

CREATE TABLE IF NOT EXISTS 'mota'(
    
    id int AUTO_INCREMENT PRIMARY KEY,
    marca varchar(50) NOT NULL,
    modelo varchar(50) NOT NULL,
    ano int NOT NULL,
    cor varchar(50) NOT NULL,
    matricula varchar(50) NOT NULL,
    cilindrada int NOT NULL,
    potencia int NOT NULL,
);

CREATE INDEX IF NOT EXISTS index_mota_marca ON mota(marca); -- Index para marca da mota (para pesquisa)

-- Criação tabela bicletas

CREATE TABLE IF NOT EXISTS 'bicicleta'(

    id int AUTO_INCREMENT PRIMARY KEY,
    marca varchar(50) NOT NULL,
    modelo varchar(50) NOT NULL,
    ano int NOT NULL,
    cor varchar(50) NOT NULL,
    sistema_AS0mudanças varchar(50) NOT NULL,
);