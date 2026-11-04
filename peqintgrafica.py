import tkinter as tk

def mostrar_mensagem():
    nome = entrada_nome.get()
    if nome.strip():
        rotulo_resultado.config(text=f"Olá, {nome}! Bem-vindo(a) à interface gráfica.")
    else:
        rotulo_resultado.config(text="Por favor, digite seu nome.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Meu Primeiro App GUI")
janela.geometry("450x250")
janela.config(bg="#808080")

# Título / Instrução
rotulo_instrucao = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), bg="#f0f0f0")
rotulo_instrucao.pack(pady=15)

# Campo de entrada de texto
entrada_nome = tk.Entry(janela, font=("Arial", 12), width=25)
entrada_nome.pack(pady=5)

# Botão de ação
botao_enviar = tk.Button(janela, text="Enviar", command=mostrar_mensagem, font=("Arial", 10, "bold"),
                         bg="#800080", fg="white", padx=10, pady=5)
botao_enviar.pack(pady=10)

# Rótulo para exibir o resultado
rotulo_resultado = tk.Label(janela, text="", font=("Arial", 11, "bold"), bg="#f0f0f0", fg="#333333")
rotulo_resultado.pack(pady=15)

# Iniciar o loop principal da aplicação
janela.mainloop()


