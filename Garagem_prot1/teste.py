from dotenv import load_dotenv

from ui import * # importa todas as funções do arquivo ui.py
from utilidades import * # importa todas as funções do arquivo utilidades.py

load_dotenv()  #carrega as variáveis de ambiente do ficheiro .env para a memória do programa

con = conectar_base_dados() # conecta a base de dados

cur = con.cursor(dictionary=True) # cria um cursor para a base de dados com o dicionário de dados ativado (para que os nomes das colunas sejam os nomes das variáveis)

