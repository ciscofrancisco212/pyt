import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

#2. Solicitando o ID do usuário a ser excluído
id_exclusao = input("Digite o ID do usuário que deseja excluir: ")

#3. Excluindo o usuário
cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_exclusao,))
conexao.commit()

conexao.close()

if cursor.rowcount == 0:
    print("Usuário não encontrado!")
else:
    print("Usuário excluído com sucesso!")