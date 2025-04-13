from os import system

def obterNúmerosDeÍmparesDeUmAtéQuinhentos() -> list:
    números_ímpares: list = []

    for x in range(1, 501):
        if x % 2 == 1:
            if x % 3 == 0:
                números_ímpares.append(x)

    return números_ímpares


def somarTodosOsNúmeros(lista_de_números: list) -> int:
    somado: int = 0

    for número in lista_de_números:
        somado += número

    return somado


def mostrarResultado(lista_de_números: list, soma_dos_números: int) -> None:
    print(f"A soma dos {len(lista_de_números)} números ímpares e multiplos por três achados entre os números 1 e 500, é igual à {soma_dos_números}.\n")

def main() -> None:
    system("clear")

    números_ímpares_multiplos_por_três: list = obterNúmerosDeÍmparesDeUmAtéQuinhentos()

    soma_dos_números: int = somarTodosOsNúmeros(números_ímpares_multiplos_por_três)

    mostrarResultado(números_ímpares_multiplos_por_três, soma_dos_números)


main()