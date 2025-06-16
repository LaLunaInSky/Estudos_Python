from customtkinter import *

show = False
show_frame = False

def mostrar_frame():
    global show
    show = True


def esconder_frame():
    global show
    show = False


def analise_número(número: int):
    analise = {
        'número': número, 'dobro': número * 2, 'triplo': número * 3, 'raiz quadrada': float(f'{número **(1/2):.2f}')
    }
    return analise


class ButtonLimpar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Limpar', font=('Arial', 18, 'bold'), text_color_disabled='#6699cc',
            command= lambda: esconder_frame()
        )


class ButtonAnalisar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Analisar', font=('Arial', 18, 'bold'), text_color_disabled='#6699cc',
            command= lambda: mostrar_frame()
        )


class EntryNúmeroUsuário(CTkEntry):

    def __init__(self, master):
        super().__init__(master)
        
        self.configure(width=180, font=('Arial', 18))
        self.focus()


class LabelInfoNúmero(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Digite um número', font=('Arial', 18, 'bold'))


class ModeloLabel(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.__texto = ''

        self.configure(text=self.__texto, font=('Arial', 16, 'bold'))


    def set_texto(self, key, value):
        self.__texto = f'{key.title()}: {value}'
        self.configure(text=self.__texto)


class FrameResultado(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.__labels = []
        self.__count = self.__count2 = 0
        self.__analise = {}

        self.configure(corner_radius=0)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        for c in range(0, 4):
            self.__labels.append(ModeloLabel(self))

        self.__labels[self.__count].grid(row=self.__count, column=self.__count, columnspan=3)

        for c in range(1, 4):
            if c == 1:
                self.__labels[c].grid(row=1, column=self.__count, padx=(15, 10), pady=(10,20))
            if c == 3:
                self.__labels[c].grid(row=1, column=self.__count, padx=(10, 15), pady=(10,20))

            self.__labels[c].grid(row=1, column=self.__count, pady=(10,20))
            self.__count += 1

        self.__atualização()


    def __atualização(self):
        if self.__analise != {}:
            for key in self.__analise.keys():
                self.__labels[self.__count2].set_texto(key, self.__analise[key])
                self.__count2 +=1

        self.__count2 = 0
        self.after(1, self.__atualização)
    

    def set_analise(self, analise: dict):
        self.__analise = analise


class Frame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.__texto = ''
        self.__analise = {}

        self.configure(corner_radius=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.__label_info_número = LabelInfoNúmero(self)
        self.__entry_número_usuário = EntryNúmeroUsuário(self)
        self.__button_analisar = ButtonAnalisar(self)
        self.__button_limpar = ButtonLimpar(self)

        self.__label_info_número.grid(row=0, column=0, columnspan=2, pady=(15, 2))
        self.__entry_número_usuário.grid(row=1, column=0, columnspan=2, padx=(25, 25))
        self.__button_analisar.grid(row=2, column=0, pady=(10, 15), padx=(20,15))
        self.__button_limpar.grid(row=2, column=1, pady=(10, 15), padx=(15,20))

        self.__atualização()


    def __atualização(self):
        global show
        global show_frame
        
        if self.__entry_número_usuário.get() != '':
            self.__texto = self.__entry_número_usuário.get()

        if self.__texto.isnumeric() and self.__texto != '':
            if show == True:
                self.__entry_número_usuário.configure(state='disabled')
                self.__button_analisar.configure(state='disabled')
                self.__button_limpar.configure(state='normal')
                self.__analise = analise_número(int(self.__texto))
                show_frame = True

        if show == False:
            self.__button_analisar.configure(state='normal')
            self.__button_limpar.configure(state='disabled')
            self.__entry_número_usuário.configure(state='normal')

            try:
                if int(self.__texto) == self.__analise['número']:
                    self.__entry_número_usuário.delete(0, 'end')
                    self.__texto = ''
                    show_frame = False
            except:
                pass

        self.after(1, self.__atualização)

    def get_analise(self):
        return self.__analise


class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Dobro/ Triplo/ Raiz')
        self.resizable(0, 0)

        self.__analise = {}

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.__frame = Frame(self)
        self.__frame_resultado = FrameResultado(self)

        self.__frame.grid(row=0, column=0)

        self.__atualização()


    def __atualização(self):
        global show_frame

        if show_frame == True:
            self.__frame_resultado.grid(row=1, column=0)
            self.__analise = self.__frame.get_analise()
            self.__frame_resultado.set_analise(self.__analise)
        else:
            self.__frame_resultado.grid_forget()

        self.after(1, self.__atualização)


app = App()
app.mainloop()