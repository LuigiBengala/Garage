

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; 
START TRANSACTION;
SET time_zone = "+00:00"; 


-- Estrutura da tabela carro

CREATE TABLE 'carro'(

    'id' int(11) PRIMARY KEY NOT NULL ,
    'matricula' varchar(10) NOT NULL,
    'marca' varchar(20) NOT NULL,
    'modelo' varchar(20) NOT NULL,
    'cor' varchar(20) NOT NULL,
    'ano' int(4) NOT NULL,
    'combustivel' varchar(20) NOT NULL,
    'cilindrada' varchar(10) NOT NULL,
    'potencia' varchar(10) NOT NULL,
    'nportas' int(10) NOT NULL,
    'nlugares' int(10) NOT NULL,
    'dono' varchar(20) NOT NULL,
)


-- Estrutura da tabela Moto

CREATE TABLE 'moto'(

    'id' int(11) PRIMARY KEY NOT NULL ,
    'matricula' varchar(10) NOT NULL,
    'marca' varchar(20) NOT NULL,
    'modelo' varchar(20) NOT NULL,
    'cor' varchar(20) NOT NULL,
    'ano' int(4) NOT NULL,
    'combustivel' varchar(20) NOT NULL,
    'cilindrada' varchar(10) NOT NULL,
    'potencia' varchar(10) NOT NULL,
    'dono' varchar(20) NOT NULL,
)

-- Estrutura da tabela bicicleta

CREATE TABLE 'bicicleta'(

    'id' int(11) PRIMARY KEY NOT NULL ,
    'marca' varchar(30) NOT NULL,
    'modelo' varchar(30) NOT NULL,
    'sistema_mudancas' varchar(50) NOT NULL,
    'dono' varchar(20) NOT NULL,
)