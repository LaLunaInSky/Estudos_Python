import os

def limparConsole():
    os.system("clear")


def getUserInput():
    return int(input("Escreva um número inteiro: "))


def somar(x: int, y: int):
    return x + y


def main():
    limparConsole()
    
    númeroX = getUserInput()
    númeroY = getUserInput()
    resultado = somar(x=x, y=y)

    print(f"A soma de {númeroX} + {númeroY} = {resultado}.")


main()