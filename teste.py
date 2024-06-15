# import customtkinter as ctk
# from tkinter import messagebox
# from previsao import Previsao
#
#
#
# # font titulos -  kodchasan
# # font textos - Noto Sans Hebrew
#
# class CeuAzulPrevisao():
#     def __init__(self):
#         ctk.set_appearance_mode("Light")
#         ctk.set_default_color_theme("blue")
#         self.janela = ctk.CTk()
#         self.janela.geometry("500x500")
#
#
#         # -- Defindo o fundo do aplicativo
#
#         self.fundo = ctk.CTkFrame(self.janela, width=500, height=500, fg_color="#7A6BFA", corner_radius=0)
#         self.fundo.place(x=0, y=0)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=452, height=467,
#                                   bg_color="#7A6BFA", fg_color="#887CF8", corner_radius=20)
#         self.fundo.place(x=24, y=16)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=440, height=394,
#                                   bg_color="#887CF8", fg_color="#A298FF", corner_radius=20)
#         self.fundo.place(x=30, y=82)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=386, height=50,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=57, y=105)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=214, height=151,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=57, y=169)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=145, height=101,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=298, y=169)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=145, height=101,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=298, y=287)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=214, height=50,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=58, y=338)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=385, height=50,
#                                   bg_color="#A298FF", fg_color="#F4F2FF", corner_radius=10)
#         self.fundo.place(x=58, y=402)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=195, height=103,
#                                   bg_color="#F4F2FF", fg_color="#FFFFFF", corner_radius=10)
#         self.fundo.place(x=66, y=208)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=128, height=49,
#                                   bg_color="#F4F2FF", fg_color="#FFFFFF", corner_radius=10)
#         self.fundo.place(x=306, y=209)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=128, height=49,
#                                   bg_color="#F4F2FF", fg_color="#FFFFFF", corner_radius=10)
#         self.fundo.place(x=306, y=327)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=90, height=35,
#                                   bg_color="#F4F2FF", fg_color="#FFFFFF", corner_radius=10)
#         self.fundo.place(x=165, y=345)
#
#         self.fundo = ctk.CTkFrame(self.janela, width=314, height=30,
#                                   bg_color="#F4F2FF", fg_color="#FFFFFF", corner_radius=10)
#         self.fundo.place(x=75, y=412)
#         # -- Fim dos fundos
#         # -- Entry
#
#         self.cidade = ctk.CTkEntry(self.janela, placeholder_text="Insira uma cidade:",
#                                    font=("Noto Sans Hebrew", 10), width=239, height=20,
#                                    bg_color="#F4F2FF", fg_color="#FFFFFF",
#                                    border_color="#F4F2FF", corner_radius=10)
#         self.cidade.place(x=69, y=120)
#
#         self.dias = ctk.CTkEntry(self.janela, placeholder_text="Dias:",
#                                  font=("Noto Sans Hebrew", 10), width=62, height=20,
#                                  bg_color="#F4F2FF", fg_color="#FFFFFF",
#                                  border_color="#F4F2FF", corner_radius=10)
#         self.dias.place(x=321, y=120)
#
#         # -- Fim dos Entry
#         # -- Labels
#
#         self.texto = ctk.CTkLabel(self.janela, text="CéuAzul", text_color="#FFB800",
#                                   bg_color="#887CF8", font=("kodchasan Bold", 25))
#         self.texto.place(x=197, y=20)
#
#         self.texto = ctk.CTkLabel(self.janela, text="seu aplicativo de previsão do tempo",
#                                   bg_color="#887CF8", font=("Noto Sans Hebrew", 12))
#         self.texto.place(x=148, y=52)
#
#         self.texto = ctk.CTkLabel(self.janela, text="Temperatura", text_color="#7B7878",
#                                   bg_color="#F4F2FF", font=("Noto Sans Hebrew Extrabold", 12))
#         self.texto.place(x=74, y=180)
#
#         self.texto = ctk.CTkLabel(self.janela, text="Máxima", text_color="#7B7878",
#                                   bg_color="#F4F2FF", font=("Noto Sans Hebrew Extrabold", 12))
#         self.texto.place(x=314, y=180)
#
#         self.texto = ctk.CTkLabel(self.janela, text="Mínima", text_color="#7B7878",
#                                   bg_color="#F4F2FF", font=("Noto Sans Hebrew Extrabold", 12))
#         self.texto.place(x=314, y=298)
#
#         self.texto = ctk.CTkLabel(self.janela, text="Sensação:", text_color="#7B7878",
#                                   bg_color="#F4F2FF", font=("Noto Sans Hebrew Extrabold", 12))
#         self.texto.place(x=81, y=350)
#
#         # -- Fim das Labels
#         # -- Buttons
#         self.filtrar = ctk.CTkButton(self.janela, text="", width=20, height=20,
#                                      bg_color="#F4F2FF", fg_color="#FFB800", corner_radius=10,
#                                      command=self.pesquisar)
#         self.filtrar.place(x=396, y=120)
#
#         self.temp = ctk.CTkLabel(self.janela, text="",
#                                  text_color="#FFB800",
#                                  bg_color="#FFFFFF", font=("kodchasan Bold", 40))
#         self.temp.place(x=79, y=222)
#
#         self.max = ctk.CTkLabel(self.janela, text="",
#                                 text_color="#9D91FF",
#                                 bg_color="#FFFFFF", font=("kodchasan Bold", 25))
#         self.max.place(x=318, y=210)
#
#         self.min = ctk.CTkLabel(self.janela, text="",
#                                 text_color="#9D91FF",
#                                 bg_color="#FFFFFF", font=("kodchasan Bold", 25))
#         self.min.place(x=318, y=328)
#
#         self.feels = ctk.CTkLabel(self.janela, text="",
#                                   text_color="#7B7878",
#                                   bg_color="#FFFFFF", font=("kodchasan Bold", 14))
#         self.feels.place(x=176, y=348)
#
#         self.desc = ctk.CTkLabel(self.janela, text="",
#                                  text_color="#7B7878",
#                                  bg_color="#FFFFFF", font=("kodchasan Bold", 12))
#         self.desc.place(x=87, y=412)
#
#         self.data = ctk.CTkLabel(self.janela, text="",
#                                  text_color="#7B7878",
#                                  bg_color="#FFFFFF", font=("kodchasan Bold", 12))
#         self.data.place(x=125, y=280)
#
#         # -- Fim dos Buttons
#
#     def run(self):
#         self.janela.mainloop()
#
#     def pesquisar(self):
#         print("clicado")
#         cidade_inserida = self.cidade.get()
#         dias_selecionados = self.dias.get()
#
#         # Verifica se o campo de dias está vazio ou não é um número
#         if not dias_selecionados.isdigit():
#             messagebox.showerror("Erro", "Por favor, insira um número válido de dias!")
#             return
#
#         dias_selecionados = int(dias_selecionados)
#
#         # Verifica se a cidade foi inserida
#         if not cidade_inserida:
#             messagebox.showerror("Erro", "Por favor, insira o nome da cidade!")
#             return
#
#         # Criar objeto de previsão
#         previsao_obj = Previsao(cidade_inserida, dias_selecionados)
#         resultado = previsao_obj.previsao_tempo()
#
#         if isinstance(resultado, str):
#             messagebox.showerror("Erro", resultado)
#         else:
#             if dias_selecionados == 0:
#                 self.temp.configure(text=f"{resultado['temperatura']}°C")
#                 self.max.configure(text=f"{resultado['temperatura_maxima']}°C")
#                 self.min.configure(text=f"{resultado['temperatura_minima']}°C")
#                 self.feels.configure(text=f"{resultado['sensacao_termica']}°C")
#                 self.desc.configure(text=f"{resultado['descricao']}")
#                 self.data.configure(text="")
#             if 1 <= dias_selecionados <= 5:
#                 self.temp.configure(text=f"{resultado['temperatura']}°C")
#                 self.max.configure(text=f"{resultado['temperatura_maxima']}°C")
#                 self.min.configure(text=f"{resultado['temperatura_minima']}°C")
#                 self.feels.configure(text=f"{resultado['sensacao_termica']}°C")
#                 self.desc.configure(text=f"{resultado['descricao']}")
#                 self.data.configure(tex=f"{resultado['data']}")
#             else:
#                 print("informe um dia válido")
#
#
#
# # Instanciando e executando a aplicação
# if __name__ == "__main__":
#     app = CeuAzulPrevisao()
#     app.run()
