import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

#2. Solicitando o ID do usuário a ser buscado
id_busca = input("Digite o ID do usuário que deseja buscar: ")

#3. Executando a consulta
cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_busca,))

usuario = cursor.fetchone()

#4. Exibindo o resultado
if usuario:
    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
else:
    print("Usuário não encontrado!")

conexao.close()