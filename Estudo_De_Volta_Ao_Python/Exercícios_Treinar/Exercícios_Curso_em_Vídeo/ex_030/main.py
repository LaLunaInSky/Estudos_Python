from os import system

def obterNúmeroInteiroDoUsuário() -> int:
    número_inteiro: int  = int(input("Digite um número inteiro: "))
    return número_inteiro


def analisarSeONúmeroÉParOuÍmpar(número_digitado_pelo_usuário: int) -> None:
    if número_digitado_pelo_usuário % 2 == 0:
        print(f"\nO número {número_digitado_pelo_usuário} é PAR!\n")
    else:
        print(f"\nO número {número_digitado_pelo_usuário} é ÍMPAR!\n")


def main() -> None:
    system("clear")

    número_digitado_pelo_usuário: int = obterNúmeroInteiroDoUsuário()
    
    analisarSeONúmeroÉParOuÍmpar(número_digitado_pelo_usuário)


main()