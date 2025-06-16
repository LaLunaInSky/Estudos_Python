from os import system

def obterNúmeroDigitadoPeloUsuário(sequência: int = 1) -> None:
    número_digitado_pelo_usuário: int = int(input(f"Digite o {sequência}º Número: "))
    return número_digitado_pelo_usuário


def mostrarResultado(lista_de_números: list) -> None:
    print(f"\nOs números ímpares digitados foram:", end=' ')

    for número in lista_de_números:
        if número % 2 == 1:
            print(f"{número}, ", end=' ')

    print(f"\nOs número pares digitados foram:", end=' ')

    soma_dos_pares: int = 0

    for número in lista_de_números:
        if número % 2 == 0:
            soma_dos_pares += número
            print(f"{número}, ", end=' ')

    print(f"\nA soma dos pares é igual à {soma_dos_pares}.")


def main() -> None:
    system("clear")

    números_digitado_pelo_usuário: list = []

    for x in range(1, 7):
        números_digitado_pelo_usuário.append(obterNúmeroDigitadoPeloUsuário(x))

    mostrarResultado(números_digitado_pelo_usuário)


main()