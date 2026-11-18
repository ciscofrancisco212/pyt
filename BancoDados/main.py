import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()#2. Criando a tabela "usuarios" se não existir

#3. Comando SQL para criar a tabela
comando_sql = """ 
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""
#4. Executando o comando SQL para criar a tabela
cursor.execute(comando_sql)

#5. Salvando as alterações e fechando a conexão
conexao.commit()

#6. Fechando a conexão com o banco de dados
conexao.close()

print("Banco de Dados e Tabela criados com sucesso!")
