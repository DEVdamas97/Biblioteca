import sqlite3  # importa o módulo para trabalhar com banco SQLite

# este arquivo contém as funções que serão importadas no arquivo "main.py"
# conecta (ou cria) o banco de dados "biblioteca.db"
conexao = sqlite3.connect("biblioteca.db")
# cria um cursor para executar comandos SQL
cursor = conexao.cursor()

def menu():

    print("\n1 - Cadastrar Livros\n")
    print("\n2 - \n")
    opcao = int(input("Escolha a sua opção: "))


def cadastrar_livro():
    """
    Solicita dados do livro ao usuário e insere no banco de dados.
    """
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano de lançamento do livro: "))
    disponivel = 'sim'  # define o status inicial de disponibilidade

    # executa a query de inserção, passando os valores como parâmetros
    cursor.execute("""
        INSERT INTO biblioteca (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, disponivel))
    # confirma a transação para salvar as alterações
    conexao.commit()

def listar_livros():
    """
    Recupera todos os livros cadastrados e exibe cada um na tela.
    """
    cursor.execute("SELECT * FROM biblioteca")
    livros = cursor.fetchall()  # obtém todos os registros como lista de tuplas

    if not livros:
        # se a lista estiver vazia, informa que não há livros cadastrados
        print("Você não adicionou nenhum livro")
    else:
        # percorre cada tupla de livro e imprime seus campos
        for livro in livros:
            id_livro, titulo, autor, ano, disponivel = livro
            print(
                f"ID: {id_livro} | Título: {titulo} | "
                f"Autor: {autor} | Ano: {ano} | Disponível: {disponivel}"
            )


listar_livros()
