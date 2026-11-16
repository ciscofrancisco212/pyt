import customtkinter as ctk
from tkinter import messagebox

# Configuração inicial do tema
ctk.set_appearance_mode("System")  # Opções: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"


class AppLogin(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Sistema de Login")
        self.geometry("400x450")
        self.resizable(False, False)

        # Centralizar os elementos
        self.grid_columnconfigure(0, weight=1)

        # Título
        self.titulo = ctk.CTkLabel(self, text="Bem-vindo", font=ctk.CTkFont(size=26, weight="bold"))
        self.titulo.pack(pady=(40, 20))

        # Campo de Usuário
        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="Usuário", width=280, height=40)
        self.entry_usuario.pack(pady=12)

        # Campo de Senha
        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=280, height=40)
        self.entry_senha.pack(pady=12)

        # Botão de Login
        self.btn_login = ctk.CTkButton(self, text="Entrar", command=self.fazer_login, width=280, height=40)
        self.btn_login.pack(pady=20)

        # Switch para alternar o tema (Opcional)
        self.switch_tema = ctk.CTkSwitch(self, text="Modo Escuro", command=self.alternar_tema)
        self.switch_tema.pack(pady=10)

        # Define o estado inicial do switch baseado no tema atual
        if ctk.get_appearance_mode() == "Dark":
            self.switch_tema.select()

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        # Validação simples de exemplo
        if usuario == "admin" and senha == "1234":
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            # Aqui você pode abrir a próxima janela do seu sistema
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def alternar_tema(self):
        if self.switch_tema.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")


if __name__ == "__main__":
    app = AppLogin()
    app.mainloop()