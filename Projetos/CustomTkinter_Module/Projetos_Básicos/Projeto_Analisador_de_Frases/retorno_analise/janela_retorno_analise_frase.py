from customtkinter import *

frase_analisada = []

class ModeloLabel(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='', font=('Arial', 18))

    
    def set_texto(self, texto: str):
        self.configure(text=texto)


class JanelaRetornoAnaliseFrase(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(corner_radius=0, width=450, height=250)
        self.grid_propagate(0)

        self.__labels = []
        
        self.grid_columnconfigure(0, weight=1)
        
        for c in range(0, 9):
            self.grid_rowconfigure(c, weight=1)
            self.__labels.append(ModeloLabel(self))

            if c < 8:
                self.__labels[c].grid(row=c , column=0)
            else:
                self.__labels[c].grid(row=c , column=0, pady=(0, 15))

        self.__atualização_frame()

    def set_frase_analisada(self, frase: dict):
        global frase_analisada
        frase_analisada = frase

    
    def __atualização_frame(self):
        self.__count = 0

        if frase_analisada != []:
            for key in frase_analisada.keys():
                self.__labels[self.__count].set_texto(f'{key}   {frase_analisada[key]}')
                self.__count += 1

        self.__count = 0
        self.after(1, self.__atualização_frame)