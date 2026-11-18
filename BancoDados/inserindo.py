import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

nome=input("Digite o nome do usuário: ")
email=input("Digite o email do usuário: ")

comando_sql = f"INSERT INTO usuarios (nome, email) VALUES (?, ?)"

try:
    cursor.execute(comando_sql, (nome, email))
    conexao.commit()
except sqlite3.IntegrityError:
    print("Erro: Email já existe!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
    conexao.close()

print("Registro inserido com sucesso!")

