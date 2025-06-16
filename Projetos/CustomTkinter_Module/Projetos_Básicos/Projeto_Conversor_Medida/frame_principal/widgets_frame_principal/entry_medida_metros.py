from customtkinter import CTkEntry

class EntryMedidaMetros(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.__medida = ''

        self.configure(width=80, font=('Arial', 16))

        self.__analise_medida()


    def __analise_medida(self):
        self.__digitado = self.get()

        try:
            for c in range(0, len(self.__digitado)):
                if self.__digitado[c].isnumeric() or self.__digitado[c] == '.':
                    pass
                else:
                    self.delete(c, 'end')

            if self.__digitado[0] != '.':
                if self.__digitado.count('.') <= 1:
                    if self.__digitado[self.__digitado.index('.') + 3] != '':
                        self.delete(self.__digitado.index('.') + 3, 'end')
                else:
                    self.delete(self.__digitado.index('.', self.__digitado.index('.') + 1), 'end')
            else:
                self.delete(0, 'end')

        except:
            pass
        
        self.__medida = self.__digitado
        self.after(1, self.__analise_medida)


    def get_medida(self):
        try:
            return float(self.__medida)
        except:
            return self.__medida