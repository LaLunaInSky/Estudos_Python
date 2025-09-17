from os import system
from time import sleep

def obterNomeCompletoDoUsuário() -> str:
    nome_completo_do_usuário = str(input("Qual o seu nome completo? "))
    return nome_completo_do_usuário.title()


def analisarSeONomePossuiSilva(nome_completo: str) -> str:
    if nome_completo.lower().find("silva") == -1:
        return "não "
    else:
        return ''
    

def mostrarResposta(nome_completo: str) -> None:
    resposta: str = analisarSeONomePossuiSilva(nome_completo)

    sleep(1)

    print(f"O seu nome completo {resposta}possui \'SILVA\'.\n")


def main() -> None:
    system("clear")

    nome_completo_do_usuário = obterNomeCompletoDoUsuário()
    
    print(f"\nAnalisando o seu nome completo {nome_completo_do_usuário}....")

    mostrarResposta(nome_completo_do_usuário)


main()