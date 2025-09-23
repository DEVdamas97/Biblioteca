import sqlite3

# importar arquivo funcoes
import funcoes

#Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("biblioteca.db")

#Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

#Criar tabela (senão existir)
cursor.execute("""
CREATE TABLE IF NOT EXISTS biblioteca(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT
    )
               
""")
print("Tabela criada!")