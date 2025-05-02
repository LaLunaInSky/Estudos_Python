from os import system
from random import randint

def obterNúmeroDoComputadorEntreZeroEDez() -> int:
    número_sorteado: int = randint(0, 10)
    return número_sorteado


def obterPalpitesDoUsuário(número_do_computador: int) -> None:
    quantidade_de_tentativas: int = 0

    while True:
        palpite: int = int(input("Qual número você acha que é? "))

        if palpite > 10 or palpite < 0:
            system("clear")

            print("Só vale 0 até 10!")

        else:
            if palpite == número_do_computador:
                print(f"\nPARABÉNS! Você Acertou em {quantidade_de_tentativas} tentativas o número {número_do_computador}.\n")
                break
            elif palpite > número_do_computador:
                print(f"O número que pensei é menor que {palpite}... Tente de novo!")
                quantidade_de_tentativas += 1
            elif palpite < número_do_computador:
                print(f"O número que pensei é maior que {palpite}... Tente de novo!")
                quantidade_de_tentativas += 1


def main() -> None:
    system("clear")

    número_do_computador: int = obterNúmeroDoComputadorEntreZeroEDez()

    print("Pensei em um número de 0 a 10, será que você consegue acertar?")

    obterPalpitesDoUsuário(número_do_computador)


main()