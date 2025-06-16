from customtkinter import CTk
from frame_principal import FramePrincipal

class App(CTk):

    def __init__(self):
        super().__init__()

        self.title('Conversor de Medida')
        self.resizable(0, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.__frame_principal = FramePrincipal(self)

        self.__frame_principal.grid(row=0, column=0)


app = App()
app.mainloop()