from customtkinter import CTkLabel

class LabelInfoNúmero(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.configure(
            text='Informe a medida em Metros', font=('Arial', 16, 'bold')
        )