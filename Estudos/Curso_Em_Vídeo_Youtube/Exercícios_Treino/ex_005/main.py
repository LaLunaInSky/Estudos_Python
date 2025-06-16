from os import system

def getUserInput():
    input_user = int(input("Digite um número: "))
    return input_user


def obterAntecessorDoNúmero(number=0):
    return number - 1


def obterSucessorDoNúmero(number=0):
    return number + 1


def mostrarResultado(number=0):
    print(f"\nO número {number}, tem o antecessor {obterAntecessorDoNúmero(number)} e o sucessor {obterSucessorDoNúmero(number)}.")


def main():
    system("clear")

    number_input = getUserInput()
    
    mostrarResultado(number_input)


main()