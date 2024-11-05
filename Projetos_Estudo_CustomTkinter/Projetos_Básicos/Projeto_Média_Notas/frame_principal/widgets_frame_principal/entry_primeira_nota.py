from customtkinter import CTkEntry

class EntryPrimeiraNota(CTkEntry):

    def __init__(self, master):
        super().__init__(master)

        self.__nota = ''
        self.configure(width=80)
        self.__atualização()


    def __atualização(self):
        self.__digitado = self.get()

        try:
            if self.__digitado[0].isnumeric():
                if self.__digitado[0] == '1':
                    if self.__digitado[1] == '.':
                        if self.__digitado[4] != '':
                            self.delete(4, 'end')
                    elif self.__digitado[1] == '0':
                        self.delete(2, 'end')
                    else:
                        self.delete(1, 'end')

                else:
                    if self.__digitado[1] == '.':
                        if self.__digitado[4] != '':
                            self.delete(4, 'end')
                    else:
                        self.delete(1, 'end')                           
            else:
                self.delete(0, 'end')
        except:
            pass
        
        self.__nota = self.__digitado
        self.after(1, self.__atualização)


    def get_nota(self):
        try:
            return float(self.__nota)
        except:
            pass
    

    def set_nota(self):
        self.__nota = ''