from customtkinter import *

def AnalisadorNúmeroDigitado(número: int):
    números = [número - 1, número + 1]
    return números


class LabelSucessor(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='SUCESSOR', font=('Arial', 17, 'bold'))


class LabelAntecessor(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='ANTECESSOR', font=('Arial', 17, 'bold'))


class EntryNúmeroSucessor(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.__número = ''

        self.configure(placeholder_text=self.__número, font=('Arial', 18, 'bold'), placeholder_text_color='black')

        self.__atualição_widget()

    def __atualição_widget(self):
        self.configure(state='normal')

        self.delete(0, 'end')
        self.configure(placeholder_text=self.__número)

        self.configure(state='disabled')
        self.after(1, self.__atualição_widget)


    def set_texto(self, número: int):
        self.__número = número

class EntryNúmeroAntecessor(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.__número = ''

        self.configure(placeholder_text=self.__número, font=('Arial', 18, 'bold'), placeholder_text_color='black')

        self.__atualição_widget()

    def __atualição_widget(self):
        self.configure(state='normal')

        self.delete(0, 'end')
        self.configure(placeholder_text=self.__número)
        
        self.configure(state='disabled')
        self.after(1, self.__atualição_widget)


    def set_texto(self, número: int):
        self.__número = número


class EntryNúmeroUsuário(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.configure(font=('Arial', 16, 'bold'))
        self.focus()


class LabelNúmeroInfo(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Digite um número', font=('Arial', 17, 'bold'))


class Frame(CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.__label_número_info = LabelNúmeroInfo(self)
        self.__entry_número_usuário = EntryNúmeroUsuário(self)
        self.__entry_número_antecessor = EntryNúmeroAntecessor(self)
        self.__entry_número_sucessor = EntryNúmeroSucessor(self)
        self.__label_antecessor = LabelAntecessor(self)
        self.__label_sucessor = LabelSucessor(self)

        self.__label_número_info.grid(row=0, column=0, columnspan=3, pady=(10, 0))
        self.__entry_número_antecessor.grid(row=1, column=0, padx=(20, 0), pady=(5, 0))
        self.__entry_número_usuário.grid(row=1, column=1, padx=(20, 20), pady=(5, 0))
        self.__entry_número_sucessor.grid(row=1, column=2, padx=(0, 20), pady=(5, 0))
        self.__label_antecessor.grid(row=2, column=0, padx=(20, 0), pady=(3, 15))
        self.__label_sucessor.grid(row=2, column=2, padx=(0, 20), pady=(3, 15))

        self.__atualição_widget()

    def __atualição_widget(self):
        self.__número_usuário = ''
        self.__números = []

        if self.__entry_número_usuário.get() != '':
            self.__número_usuário = self.__entry_número_usuário.get()
        
        if self.__número_usuário.isnumeric():
            self.__números = AnalisadorNúmeroDigitado(int(self.__número_usuário))
            
            self.__entry_número_antecessor.set_texto(self.__números[0])
            self.__entry_número_sucessor.set_texto(self.__números[1])

        self.after(1, self.__atualição_widget)


class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Número Antecessor/Sucessor')
        self.resizable(0, 0)

        self._set_appearance_mode('dark')

        self.__frame = Frame(self)
        self.__frame.grid(row=0, column=0, sticky='nsew')


app = App()
app.mainloop()