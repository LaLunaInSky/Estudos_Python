from customtkinter import CTkLabel

class LabelSegundaNota(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Qual a 2ª Nota?', font=('Arial', 15, 'bold'))