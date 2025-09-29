import sqlite3  # importa o módulo para trabalhar com banco SQLite

# este arquivo contém as funções que serão importadas no arquivo "main.py"
# conecta (ou cria) o banco de dados "biblioteca.db"
conexao = sqlite3.connect("biblioteca.db")
# cria um cursor para executar comandos SQL
cursor = conexao.cursor()

def menu():
    # Mostra as opções disponiveis do CRUD
    print("\n1 - Cadastrar Livros")
    print("\n2 - Listar Livro")
    print("\n3 - Livro Disponivel")
    print("\n3 - Remover Livro")
    opcao = int(input("Escolha a sua opção: "))


def cadastrar_livro():
    """
    Solicita dados do livro ao usuário e insere no banco de dados.
    """
    # Pede ao usuário o título do livro
    titulo = input("Digite o título do livro: ")

    # Pede ao usuário o autor do livro
    autor = input("Digite o autor do livro: ")

    # Pede o ano de lançamento e converte para inteiro
    ano = int(input("Digite o ano de lançamento do livro: "))

    # Define o status inicial de disponibilidade como "sim"
    disponivel = 'sim'  

    # Executa a query de inserção na tabela "biblioteca"
    # Os valores são passados como parâmetros (uso de ?), o que evita SQL Injection
    cursor.execute("""
        INSERT INTO biblioteca (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, disponivel))

    # Exibe mensagem de confirmação para o usuário
    print(f"Livro: {titulo}\nCadastrado com sucesso! ✔")

    # Confirma a transação no banco de dados, salvando a inserção
    conexao.commit()



def listar_livros():
    """
    Recupera todos os livros cadastrados e exibe cada um na tela.
    """
    # Executa uma consulta SQL para selecionar todos os registros da tabela "biblioteca"
    cursor.execute("SELECT * FROM biblioteca")

    # fetchall() retorna todos os resultados da consulta como uma lista de tuplas
    # Cada tupla representa um livro (linha da tabela)
    livros = cursor.fetchall()  

    # Verifica se a lista está vazia (ou seja, não há livros cadastrados)
    if not livros:
        # Caso não haja registros, informa ao usuário
        print("Você não adicionou nenhum livro")
        # commit() aqui não é necessário, pois não houve alteração no banco
        conexao.commit()
    else:
        # Se houver registros, percorre a lista de tuplas
        for livro in livros:
            # Desempacota os valores da tupla em variáveis individuais
            id_livro, titulo, autor, ano, disponivel = livro

            # Exibe os dados formatados de cada livro
            print(
                f"ID: {id_livro} | Título: {titulo} | "
                f"Autor: {autor} | Ano: {ano} | Disponível: {disponivel}"
            )
        # commit() também não é necessário aqui, já que SELECT não altera dados
        conexao.commit()

        

def atualizar_disponibilidade():
    # Pede ao usuário o ID do livro que deseja atualizar e converte para inteiro
    id_atualizar = int(input("Deseja atualizar qual livro? (Digite pelo id) "))

    # Pergunta se o usuário quer deixar o livro disponível ou indisponível
    disponibilidade = input("Deseja deixa-lo como disponivel ou indisponivel ?: ").lower()

    # Se a resposta for "sim" ou "disponivel", atualiza o campo para "sim"
    if disponibilidade == 'sim' or disponibilidade == 'disponivel':
        cursor.execute("""
        UPDATE biblioteca
        SET disponivel = ? WHERE id = ? 
        """, ("sim", id_atualizar)  # passa os parâmetros de forma segura
        )
        print(f"ID: {id_atualizar} | Agora está disponível")
        conexao.commit()  # salva a alteração no banco

    # Se a resposta for "nao", "não" ou "indisponivel", atualiza para "não"
    elif disponibilidade == "nao" or disponibilidade == 'não' or disponibilidade == 'indisponivel':
        cursor.execute("""
        UPDATE biblioteca
        SET disponivel = ? WHERE id = ?
        """, ("não", id_atualizar)
        )
        print(f"ID: {id_atualizar} | Agora está indisponivel")
        conexao.commit()  # salva a alteração no banco



def remover_livros():
    try:
        # Conectando ao banco de dados (ou cria se não existir)
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        # Solicita ao usuário o ID do livro a ser removido
        # OBS: input() retorna string, então é bom converter para int
        id_removido = int(input("Digite o id do livro que deseja excluir: "))

        # Executa o comando DELETE usando parâmetro para evitar SQL Injection
        # IMPORTANTE: o parâmetro precisa ser passado como tupla (id_removido,)
        cursor.execute("DELETE FROM biblioteca WHERE id = ?", (id_removido,))
       
        # Confirma a alteração no banco
        conexao.commit()

        # Verifica se algum registro foi realmente deletado
        if cursor.rowcount > 0:
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")

    except Exception as erro:
        # Captura qualquer erro (ex: conexão, sintaxe SQL, etc.)
        print(f"Erro ao tentar excluir Livro: {erro}")

    finally:
        # Fecha a conexão mesmo em caso de erro
        if conexao:
            conexao.close()



