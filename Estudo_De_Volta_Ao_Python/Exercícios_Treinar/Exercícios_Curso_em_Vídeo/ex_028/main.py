from os import system
from random import randint

def obterNúmeroDoUsuário() -> int:
    while True:
        print("Tente adivinhar o número que estou pensando, só vale 0 à 5...")

        número_do_usuário = int(input("Qual número você acha que escolhi? "))

        if 5 >= número_do_usuário >= 0:
            return número_do_usuário
        else:
            system("clear")


def obterNúmeroDoComputador() -> int:
    número_do_computador = randint(0, 5)
    return número_do_computador


def mostrarResultado(número_do_usuário: int) -> None:    
    número_do_computador = obterNúmeroDoComputador()
    
    if número_do_computador == número_do_usuário:
        print("\nVocê GANHOU!")
    else:
        print("\nVocê PERDEU!")
    
    print(f"Eu pensei no número {número_do_computador} e você escolheu o número {número_do_usuário}.\n")


def main() -> None:
    system("clear")

    número_do_usuário = obterNúmeroDoUsuário()

    mostrarResultado(número_do_usuário)


main()