from customtkinter import CTkButton

class ButtonLimpar(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.__show_resultado = False

        self.configure(text='Limpar', font=('Arial', 17), width=80, text_color_disabled='#4d4d4d',
            command= lambda: self.__esconder_resultado()
        )

    
    def __esconder_resultado(self):
        self.__show_resultado = True


    def set_false_resultado(self):
        self.__show_resultado = False


    def get_show(self):
        return self.__show_resultado