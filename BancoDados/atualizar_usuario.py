import sqlite3
#1. Conectando ao banco de dados (ou criando se não existir)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

#2. Solicitando o ID do usuário a ser atualizado
id_atualizacao = input("Digite o ID do usuário que deseja atualizar: ")

#3. Solicitando os novos dados do usuário
novo_nome = input("Digite o novo nome do usuário: ")
novo_email = input("Digite o novo email do usuário: ")

#4. Atualizando os dados do usuário
cursor.execute("UPDATE usuarios SET nome = ?, email = ? WHERE id = ?", (novo_nome, novo_email, id_atualizacao))
conexao.commit()


conexao.close()
print("Usuário atualizado com sucesso!")