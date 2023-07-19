import tkinter as tk
from tkinter import PhotoImage
from tkinter import *
import customtkinter

class ModeloTelaPrincipal:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Login')
        self.janela['bg'] = '#306D92'
        self.janela.geometry('1100x900')
        self.janela.resizable(width=False, height=False)


        self.mainFrame = customtkinter.CTkFrame(self.janela, fg_color='transparent')

        #PAGINA DE BOTOES----------------------------------------------------------------

        self.frame1 = customtkinter.CTkFrame(self.mainFrame,
                                             width=500, height=750,
                                             fg_color='#ffffff',
                                             corner_radius=25)
        self.frame1.pack(pady=70)
        self.frame1.pack_propagate(False)

        self.userIcon = PhotoImage(file='image/user1_dark.png')
        self.imageIcon1 = customtkinter.CTkLabel(self.frame1, image=self.userIcon, text='')
        self.imageIcon1.pack(pady=70)

        self.tittle = customtkinter.CTkLabel(self.frame1,
                                             text='Seja bem-vindo',
                                             font=('Arial', 30, 'bold'), text_color='black', fg_color='white')
        self.tittle.pack()

        self.sub_tittle = customtkinter.CTkLabel(self.frame1,
                                                 text='Por-favor selecione uma opção abaixo para logar',
                                                 font=('Arial', 15), text_color='black', fg_color='white')
        self.sub_tittle.pack()

        self.bttn_adm = customtkinter.CTkButton(self.frame1,
                                                text='Administrador', font=('Arial', 16, 'bold'),corner_radius=10, text_color='#ffffff', bg_color='transparent',
                                                fg_color='#0c4f87', width=250, height=70, command=self.move_next_page)
        self.bttn_adm.pack(pady=40)

        self.bttn_recep = customtkinter.CTkButton(self.frame1,
                                                  text='Recepcionista', font=('Arial', 16, 'bold'),corner_radius=10, text_color='#ffffff', bg_color='transparent',
                                                  fg_color='#0c4f87', width=250, height=70, command=self.move_next_page)
        self.bttn_recep.pack()

        #TELA DE LOGIN-----------------------------------------------------------------------------------------------

        self.frameLogin = customtkinter.CTkFrame(self.mainFrame,
                                                 width=500, height=750,
                                                 fg_color='#ffffff',
                                                 corner_radius=25)
        self.frameLogin.pack(pady=70)
        self.frameLogin.pack_propagate(False)

        self.userIcon = PhotoImage(file='image/user2_dark.png')
        self.imageIcon1 = customtkinter.CTkLabel(self.frameLogin, image=self.userIcon, text='')
        self.imageIcon1.pack(pady=70)

        self.tittle = customtkinter.CTkLabel(self.frameLogin,
                                             text='Login',
                                             font=('Arial', 30, 'bold'), text_color='black', fg_color='white')
        self.tittle.pack()

        self.sub_tittle = customtkinter.CTkLabel(self.frameLogin,
                                                 text='Por-favor insira as informações para logar',
                                                 font=('Arial', 15), text_color='black', fg_color='white')
        self.sub_tittle.pack()


        self.inputUser = customtkinter.CTkEntry(self.frameLogin,
                                                 placeholder_text='Usuário',
                                                 width=250, height=50, border_width=0, corner_radius=12, bg_color='white', text_color='black')
        self.inputUser.pack(pady=30)

        self.inputPass = customtkinter.CTkEntry(self.frameLogin,
                                                placeholder_text='Senha',
                                                width=250, height=50, border_width=0, corner_radius=12, bg_color='white', text_color='black', show='*')
        self.inputPass.pack()
        
        self.bttn_login = customtkinter.CTkButton(self.frameLogin,
                                                  text='Entrar', font=('Arial', 16, 'bold'),corner_radius=10, text_color='#ffffff', bg_color='transparent',
                                                  fg_color='#0c4f87', width=200, height=70)
        self.bttn_login.pack(pady=25)

        self.bttn_back = customtkinter.CTkButton(self.frameLogin,
                                                  text='Voltar', font=('Arial', 16, 'bold'),corner_radius=10, text_color='#ffffff', bg_color='transparent',
                                                  fg_color='#0c4f87', width=100, height=40, command=self.move_back_page)
        self.bttn_back.place(x=40, y=20)



        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        self.pages = [self.frame1, self.frameLogin]
        self.count = 0

    def limpar_dados(self):
        self.inputPass.delete(0, END)
        self.inputUser.delete(0, END)

    def move_next_page(self):
        if not self.count > len(self.pages) - 2:
            for p in self.pages:
                p.pack_forget()
            self.count += 1
            page = self.pages[self.count]
            page.pack(pady=70)

    def move_back_page(self):
        self.limpar_dados()
        if not self.count == 0:
            for p in self.pages:
                p.pack_forget()
            self.count -= 1
            page = self.pages[self.count]
            page.pack(pady=70)

if __name__ == "__main__":
    windows = tk.Tk()
    objeto = ModeloTelaPrincipal(windows)
    windows.mainloop()
