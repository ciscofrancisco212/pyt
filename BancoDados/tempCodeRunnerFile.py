import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()