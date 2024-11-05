from customtkinter import CTkLabel

class LabelResultado(CTkLabel):

    def __init__(self, master):
        super().__init__(master)

        self.__resultado = []

        self.configure(
            text='', font=('Arial', 14, 'bold')
        )

    
    def set_resultado(self, medida: float):
        self.__resultado.clear()

        self.__resultado.append(f'{medida / 1000}km')
        self.__resultado.append(f'{medida / 100}hm')
        self.__resultado.append(f'{medida / 10}dam')
        self.__resultado.append(f'{medida}m')
        self.__resultado.append(f'{medida * 10}dm')
        self.__resultado.append(f'{medida * 100}cm')
        self.__resultado.append(f'{medida * 1000}mm')

        self.configure(text=f'{self.__resultado[0]}  ->  {self.__resultado[1]}  ->  {self.__resultado[2]}  ->  {self.__resultado[3]}  <-  {self.__resultado[4]}  <-  {self.__resultado[5]}  <-  {self.__resultado[6]}')