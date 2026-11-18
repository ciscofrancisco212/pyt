import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print("Lista de usuários cadastrados:")
    print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")


conexao.close()