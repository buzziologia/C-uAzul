import customtkinter as ctk
from tkinter import messagebox

import os

from janela_previsao import CeuAzulPrevisao


class AppCeuAzul:
    def __init__(self):
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")
        self.janela = ctk.CTk()
        self.janela.title("CéuAzul")
        self.janela.geometry("500x500")

        # Definindo o fundo do aplicativo
        self.fundo = ctk.CTkFrame(self.janela, width=500, height=500, fg_color="#7A6BFA", corner_radius=0)
        self.fundo.place(x=0, y=0)

        self.fundo1 = ctk.CTkFrame(self.janela, width=452, height=467,
                                   bg_color="#7A6BFA", fg_color="#887CF8", corner_radius=20)
        self.fundo1.place(x=24, y=16)

        self.fundo2 = ctk.CTkFrame(self.janela, width=440, height=394,
                                   bg_color="#887CF8", fg_color="#A298FF", corner_radius=20)
        self.fundo2.place(x=30, y=82)

        self.fundo3 = ctk.CTkFrame(self.janela, width=174, height=300,
                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
        self.fundo3.place(x=59, y=145)

        self.fundo4 = ctk.CTkFrame(self.janela, width=174, height=300,
                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
        self.fundo4.place(x=265, y=145)

        # Entry
        self.email = ctk.CTkEntry(self.janela, placeholder_text="Email:",
                                  font=("Noto Sans Hebrew", 10), width=146, height=20,
                                  bg_color="#F4F2FF", fg_color="#FFFFFF",
                                  border_color="#F4F2FF", corner_radius=10)
        self.email.place(x=75, y=222)

        self.senha = ctk.CTkEntry(self.janela, placeholder_text="Senha:", show="*",
                                  font=("Noto Sans Hebrew", 10), width=146, height=20,
                                  bg_color="#F4F2FF", fg_color="#FFFFFF",
                                  border_color="#F4F2FF", corner_radius=10)
        self.senha.place(x=75, y=257)

        self.email1 = ctk.CTkEntry(self.janela, placeholder_text="Email:",
                                   font=("Noto Sans Hebrew", 10), width=146, height=20,
                                   bg_color="#F4F2FF", fg_color="#FFFFFF",
                                   border_color="#F4F2FF", corner_radius=10)
        self.email1.place(x=280, y=222)

        self.senha1 = ctk.CTkEntry(self.janela, placeholder_text="Senha:", show="*",
                                   font=("Noto Sans Hebrew", 10), width=146, height=20,
                                   bg_color="#F4F2FF", fg_color="#FFFFFF",
                                   border_color="#F4F2FF", corner_radius=10)
        self.senha1.place(x=280, y=257)

        self.senha2 = ctk.CTkEntry(self.janela, placeholder_text="Confirmar senha:", show="*",
                                   font=("Noto Sans Hebrew", 10), width=146, height=20,
                                   bg_color="#F4F2FF", fg_color="#FFFFFF",
                                   border_color="#F4F2FF", corner_radius=10)
        self.senha2.place(x=280, y=292)

        # Labels
        self.texto = ctk.CTkLabel(self.janela, text="CéuAzul", text_color="#FFB800",
                                  bg_color="#887CF8", font=("kodchasan Bold", 25))
        self.texto.place(x=197, y=20)

        self.texto = ctk.CTkLabel(self.janela, text="seu aplicativo de previsão do tempo",
                                  bg_color="#887CF8", font=("Noto Sans Hebrew", 12))
        self.texto.place(x=148, y=52)

        self.texto = ctk.CTkLabel(self.janela, text="Bem-Vindo",
                                  bg_color="#A298FF", font=("kodchasan", 20))
        self.texto.place(x=182, y=94)

        self.texto = ctk.CTkLabel(self.janela, text="Login",
                                  bg_color="#F4F2FF", font=("kodchasan", 20))
        self.texto.place(x=118, y=160)

        self.texto = ctk.CTkLabel(self.janela, text="Cadastrar",
                                  bg_color="#F4F2FF", font=("kodchasan", 20))
        self.texto.place(x=304, y=160)

        # Buttons
        self.logar = ctk.CTkButton(self.janela, text="", width=20, height=20,
                                   bg_color="#F4F2FF", fg_color="#FFB800", corner_radius=10,
                                   command=self.logar)
        self.logar.place(x=138, y=372)

        self.cad = ctk.CTkButton(self.janela, text="", width=20, height=20,
                                 bg_color="#F4F2FF", fg_color="#FFB800", corner_radius=10,
                                 command=self.cadastrar)
        self.cad.place(x=343, y=372)
        # -- End of Buttons

    def run(self):
        self.janela.mainloop()

    def cadastrar(self):
        # Obter o e-mail e as senhas inseridos pelo usuário
        email_cadastro = self.email1.get()
        senha_cadastro = self.senha1.get()
        confirmar_senha = self.senha2.get()

        # Verificar se os campos não estão vazios e se as senhas coincidem
        if email_cadastro and senha_cadastro and senha_cadastro == confirmar_senha:
            # Verificar se o e-mail já foi cadastrado
            if os.path.exists('users.txt'):
                with open('users.txt', 'r') as file:
                    users = file.readlines()
                    for user in users:
                        self.email, _ = user.strip().split(',')
                        if email_cadastro == self.email:
                            messagebox.showerror("Erro", "Este e-mail já foi cadastrado!")
                            return

            # Adicionar o novo usuário ao arquivo
            with open('users.txt', 'a') as file:
                file.write(f"{email_cadastro},{senha_cadastro}\n")

            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Aviso: as duas senhas precisam ser iguais. Tente Novamente.")

    def abrir_janela_previsao(self):
        print("abrindo")
        self.janela.destroy()  # Destroi a janela de login
        janela_previsao = CeuAzulPrevisao()  # Cria uma instância da classe CeuAzulPrevisao
        janela_previsao.run()

    def logar(self):
        global email
        email_inserido = self.email.get()
        global senhaf
        senha_inserida = self.senha.get()

        # Verificar se o e-mail e a senha estão corretos
        if os.path.exists('users.txt'):
            with open('users.txt', 'r') as file:
                users = file.readlines()
                for user in users:
                    self.email, senha = user.strip().split(',')
                    if email_inserido == self.email and senha_inserida == senha:
                        # Se o login for bem-sucedido, abrir uma nova janela
                        self.abrir_janela_previsao()
                        return


# Instanciando e executando a aplicação
if __name__ == "__main__":
    app = AppCeuAzul()
    app.run()
