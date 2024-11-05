from customtkinter import CTkButton

class ButtonCalcular(CTkButton):

    def __init__(self, master):
        super().__init__(master)

        self.__clicado = False

        self.configure(text='Calcular', font=('Arial', 16), width=60, text_color_disabled='#595959',
                        command= lambda: self.__clique_button()
        )

    
    def __clique_button(self):
        self.__clicado = True


    def get_clique(self):
        return self.__clicado
    

    def set_clique_false(self):
        self.__clicado = False