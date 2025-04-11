from os import system 
from random import choice
from time import sleep

opções: list = ["Pedra", "Papel", "Tesoura"]

def obterEscolhaDoUsuário() -> str:

    while True:
        print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
    
        escolha_do_usuário: int = int(input("Qual você escolhe? "))

        if escolha_do_usuário > 0 and escolha_do_usuário < 4:
            return opções[escolha_do_usuário - 1]
        else:
            system("clear")


def obterEscolhaDoComputador() -> str:
    escolha_do_computador: str = choice(opções)
    return escolha_do_computador


def analisarQuemGanhou(escolha_do_usuário: str, escolha_do_computador: str) -> str:
    if escolha_do_usuário == opções[0]:
        if escolha_do_computador == opções[0]:
            return "Ouve EMPATE!"
        elif escolha_do_computador == opções[1]:
            return  "Você PERDEU!"
        elif escolha_do_computador == opções[2]:
            return "Você GANHOU!"
        
    elif escolha_do_usuário == opções[1]:
        if escolha_do_computador == opções[0]:
            return "Você GANHOU!"
        elif escolha_do_computador == opções[1]:
            return  "Ouve EMPATE!"
        elif escolha_do_computador == opções[2]:
            return "Você PERDEU!"
        
    elif escolha_do_usuário == opções[2]:
        if escolha_do_computador == opções[0]:
            return "Você PERDEU!"
        elif escolha_do_computador == opções[1]:
            return  "Você GANHOU!"
        elif escolha_do_computador == opções[2]:
            return "Ouve EMPATE!"


def mostrarResultado(escolha_do_usuário: str, escolha_do_computador: str) -> None:
    print("\nJO", end='')
    sleep(0.5)
    print("KEN", end='')
    sleep(0.5)
    print("PÔ\n")

    print(f"Você escolheu {escolha_do_usuário},\ne o Computador escolheu {escolha_do_computador}...")

    print(f"\n{analisarQuemGanhou(escolha_do_usuário, escolha_do_computador)}\n")


def main() -> None:
    system("clear")

    escolha_do_usuário: str = obterEscolhaDoUsuário()
    escolha_do_computador: str = obterEscolhaDoComputador()

    mostrarResultado(escolha_do_usuário, escolha_do_computador)


main()