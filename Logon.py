# import tkinter
#
# janela= tkinter.Tk()
# janela.geometry('400x250')
#
# def clique():
#     print('FAZER LOGIN!')
#
# texto= tkinter.Label(text='Fazer Login')
# texto.pack(padx=12, pady=12)
#
# botao= tkinter.Button(janela, text='Login',command=clique)
# botao.pack(padx=12, pady=12)
#
# janela.mainloop()
#
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x350')

def clique():
    print('FAZER LOGIN!')

texto= customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=12, pady=12)
texto= customtkinter.CTkLabel(janela, text='Bem-Vindo Escola PROZ')
texto.pack(padx=12, pady=12)

email= customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail')
email.pack(padx=12, pady=12)

senha= customtkinter.CTkEntry(janela, placeholder_text='Digite sua senha', show='*')
senha.pack(padx=12, pady=12)

checkbox= customtkinter.CTkCheckBox(janela, text='Lembrar senha')
checkbox.pack(padx=12, pady=12)

botao= customtkinter.CTkButton(janela, text='LOGIN', command=clique)
botao.pack(padx=12, pady=12)



janela.mainloop()