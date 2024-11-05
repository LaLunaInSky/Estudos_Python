from customtkinter import CTkLabel

class LabelPrimeiraNota(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(text='Qual a 1ª Nota?', font=('Arial', 15, 'bold'))