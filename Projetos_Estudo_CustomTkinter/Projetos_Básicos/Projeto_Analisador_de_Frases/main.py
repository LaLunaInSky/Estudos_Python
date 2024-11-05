from customtkinter import CTk, CTkButton, CTkLabel, CTkEntry, CTkFrame
from analise_dados import AnalisadorFrase
from retorno_analise import JanelaRetornoAnaliseFrase

ativado = False
show_frame = False
count = 0

def ativação_button():
    global ativado
    global show_frame

    if count == 0:
        show_frame = True

    ativado = True


class ButtonAnalisar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.configure(
            text='Analisar Frase', height=35, corner_radius=18, font=("Arial", 16, 'bold'),
            command= lambda: ativação_button()
        )


class EntryMensagemTexto(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.configure(placeholder_text='Pode conter números, caracteres...', width=400, height=40, font=("Arial", 15))


class LabelMensagemTexto(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='DIGITE O QUE QUISER', font=("Arial", 12, 'bold'))


class Frame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(corner_radius=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.__frase_analisada = []

        self.__label_mensagem_texto = LabelMensagemTexto(self)
        self.__entry_mensagem_texto = EntryMensagemTexto(self)
        self.__button_analisar = ButtonAnalisar(self)

        self.__label_mensagem_texto.grid(row=0, column=0, padx=(0, 250), pady=(10, 0))
        self.__entry_mensagem_texto.grid(row=1, column=0, padx=(25, 25), pady=(0, 15))
        self.__button_analisar.grid(row=2, column=0, pady=(0,15))

        self.__verificação_frame()

    def __verificação_frame(self):
        global ativado
        
        if ativado == True:
            if self.__entry_mensagem_texto.get() != '':
                self.__frase = self.__entry_mensagem_texto.get()
                self.__frase_para_analisar = AnalisadorFrase(self.__frase)
                self.__frase_analisada = self.__frase_para_analisar.get_frase_dict()
            
            ativado = False
        self.after(1, self.__verificação_frame)


    def get_frase_analisada(self):
        return self.__frase_analisada


class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Analisador De Frases')
        self.geometry('+650+250')
        self.resizable(0, 0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.__frame = Frame(self)
        self.__frame_retorno_dados = JanelaRetornoAnaliseFrase(self)
        self.__frame.grid(row=0, column=0)

        self.__verificação_main()


    def __verificação_main(self):
        global count
       
        self.__frase_analisada = self.__frame.get_frase_analisada()
        self.__cópia_frase = ''

        if show_frame == True and count == 0 and self.__frame.get_frase_analisada() != []:
            count += 1
            self.__frame_retorno_dados.grid(row=1, column=0)

        if self.__frame.get_frase_analisada() != []:
            if self.__cópia_frase != self.__frase_analisada:
                self.__cópia_frase = self.__frase_analisada
                self.__frame_retorno_dados.set_frase_analisada(self.__cópia_frase)

        self.after(1, self.__verificação_main)


app = App()
app.mainloop()