from customtkinter import CTk
from frame_principal import FramePrincipal

class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Média Notas')
        self.resizable(0, 0)

        self.__frame_principal = FramePrincipal(self)

        self.__frame_principal.grid(row=0, column=0)


app = App()
app.mainloop()