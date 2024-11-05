from customtkinter import *

abrir_fechar = False
verificar = None
números_digitados = ['', '']

def Somar():
    global abrir_fechar
    global verificar
    
    if números_digitados[0] != '' and números_digitados[1] != '':
        abrir_fechar = True
        verificar = abrir_fechar


def Limpar():
    global abrir_fechar
    global números_digitados
    global verificar

    números_digitados[0] = ''
    números_digitados[1] = ''

    abrir_fechar = False
    verificar = abrir_fechar


class LabelResultado(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.resultado = StringVar()
        self.resultado.set('')

        self.configure(textvariable=self.resultado, font=('Arial', 16, 'bold'))


class ButtonLimpar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='LIMPAR', width=60, font=('Arial', 15), command= lambda: Limpar())


class ButtonSomar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='SOMAR', width=60, font=('Arial', 15), command= lambda: Somar())


class EntryNúmero2(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.configure(width=80, font=('Arial', 15))


class EntryNúmero1(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.configure(width=80, font=('Arial', 15))


class LabelNúmero2(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='2° Número', font=('Arial', 15, 'bold'))


class LabelNúmero1(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='1º Número', font=('Arial', 15, 'bold'))


class Frame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.__label_número_1 = LabelNúmero1(self)
        self.__label_número_2 = LabelNúmero2(self)
        self.__entry_número_1 = EntryNúmero1(self)
        self.__entry_número_2 = EntryNúmero2(self)
        self.__button_somar = ButtonSomar(self)
        self.__button_limpar = ButtonLimpar(self)
        self.__label_resultado = LabelResultado(self)

        self.__label_número_1.grid(row=0, column=0, sticky=W, padx=(15,3), pady=(15, 3))
        self.__entry_número_1.grid(row=0, column=1, sticky=W, padx=(3, 30), pady=(15, 3))
        self.__button_somar.grid(row=0, column=2, padx=(0, 15), pady=(10, 2), sticky=E)
        self.__label_número_2.grid(row=1, column=0, sticky=W, padx=(15,3), pady=(2, 10))
        self.__entry_número_2.grid(row=1, column=1, sticky=W, padx=(3, 30), pady=(3, 10))
        self.__button_limpar.grid(row=1, column=2, padx=(0, 15), pady=(3, 10), sticky=E)

        self.__verificação()


    def __verificação(self):
        global números_digitados
        global verificar

        if self.__entry_número_1.get() != '' and self.__entry_número_2.get() != '':
                if self.__entry_número_1.get().isdecimal() and self.__entry_número_2.get().isdecimal():

                    números_digitados[0] = int(self.__entry_número_1.get())
                    números_digitados[1] = int(self.__entry_número_2.get())

        if verificar != None:
            if abrir_fechar == True:
                        self.__entry_número_1.configure(state=DISABLED)
                        self.__entry_número_2.configure(state=DISABLED)

                        self.__label_resultado.resultado.set(
                            f'A soma de {números_digitados[0]} + {números_digitados[1]} é igual a {números_digitados[0] + números_digitados[1]}'
                        )

                        self.__label_resultado.grid(row=2, column=0, columnspan=3, pady=(10,15), sticky='ew')
            else:
                self.__entry_número_1.configure(state=NORMAL)
                self.__entry_número_2.configure(state=NORMAL)

                self.__entry_número_1.delete(0, 'end')
                self.__entry_número_2.delete(0, 'end')

                self.__label_resultado.grid_forget()

        verificar = None        
        self.after(1, self.__verificação)


class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Soma dos Números')
        self.geometry('+750+300')
        self.resizable(0, 0)
        self._set_appearance_mode("system")
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__frame_principal = Frame(self)
        self.__frame_principal.grid(row=0, column=0, sticky='nsew')


app = App()
app.mainloop()