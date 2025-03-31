from os import system

def getUserInput(posição=1):
    number = int(input(f"Digite o {posição}º Número: "))
    return number


def soma(x=0, y=0):
    return x + y


def main():
    system("clear")

    number_1 = getUserInput(1)
    number_2 = getUserInput(2)
    resultadoSoma = soma(number_1, number_2)

    print(f"A soma de {number_1} + {number_2} é igual a: {resultadoSoma}.")

main()