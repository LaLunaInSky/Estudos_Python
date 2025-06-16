from customtkinter import CTkLabel

class LabelMédia(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.__média = 0

        self.configure(text='', font=('Arial', 20, 'bold'))

    
    def set_média(self, primeira_nota: float, segunda_nota: float):
        self.__média = f'Média \n{((primeira_nota + segunda_nota) / 2):.1f}'


    def set_text(self, show_média: bool):
        if show_média == True:
            self.configure(text=self.__média)
        else:
            self.configure(text='')