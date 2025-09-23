import sqlite3

# Este aquivo contem as funções que sarão importada sno arquivo "main.py"

#Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("biblioteca.db")

#Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Função de Cadastro

def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    disponivel = 'sim'

    cursor.execute("""
        INSERT INTO biblioteca (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, disponivel))

    conexao.commit()


cadastrar_livro()