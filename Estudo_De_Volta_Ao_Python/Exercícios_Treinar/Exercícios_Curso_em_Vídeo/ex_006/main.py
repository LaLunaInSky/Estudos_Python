from os import system
from math import sqrt

def getUserInput():
    input_user = int(input("Digite um número: "))
    return input_user


def obterDobroDoNúmero(number):
    return number * 2


def obterTriploDoNúmero(number):
    return number * 3


def obterRaizQuadradaDoNúmero(number):
    return round(sqrt(number), 2)


def mostrarResultados(number):
    print(f'''
    Analisando o número {number}

O dobro..........: {obterDobroDoNúmero(number)}
O triplo.........: {obterTriploDoNúmero(number)}
A raiz quadrada..: {obterRaizQuadradaDoNúmero(number)}
''')


def main():
    system("clear")

    number_x = getUserInput()
    
    mostrarResultados(number_x)


main()