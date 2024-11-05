from customtkinter import *

class AnalisadorFrase:

    def __init__(self, frase: str):
        self.__frase_analisada = {}
        self.__frase = frase
        self.__frase_sem_espaços = self.__remover_espaços(self.__frase)

        self.__frase_analisada['Foi digitado'] = self.__frase
        self.__frase_analisada['O tipo primitivo é'] = type(self.__frase)
        self.__frase_analisada['Só tem espaços?'] = self.__substituição(self.__frase.isspace())
        self.__frase_analisada['É um número?'] = self.__substituição(self.__frase_sem_espaços.isnumeric())
        self.__frase_analisada['É alfabético?'] = self.__substituição(self.__frase_sem_espaços.isalpha())
        self.__frase_analisada['É alfanúmerico?'] = self.__substituição(self.__frase_sem_espaços.isalnum())
        self.__frase_analisada['Está em maiúscula?'] = self.__substituição(self.__frase.isupper())
        self.__frase_analisada['Está em minúscula?'] = self.__substituição(self.__frase.islower())
        self.__frase_analisada['Está capitalizada?'] = self.__substituição(self.__frase.istitle())


    def __remover_espaços(self, frase: str):
        self.__removido = frase.replace(' ', '')
        return self.__removido


    def __substituição(self, bool: bool):
        self.__substituto = ''

        if bool == True:
            self.__substituto = 'Sim'
        else:
            self.__substituto = 'Não'
        
        return self.__substituto
    

    def get_frase_dict(self):
        return self.__frase_analisada