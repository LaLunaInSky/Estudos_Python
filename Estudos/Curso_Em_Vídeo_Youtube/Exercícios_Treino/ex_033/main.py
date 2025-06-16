from os import system

def obterNúmeroInteiroDoUsuário(sequência_da_chamada: int = 1) -> int:
    número_digitado_inteiro: int = int(input(f"Digite o {sequência_da_chamada}º Número: "))
    return número_digitado_inteiro


def mostrarResultado(número_menor: int, número_maior: int) -> None:
    print(f'''
O número maior é...{número_maior}
O número menor é...{número_menor}
''')


def main() -> None:
    system("clear")

    números_digitados: list = []

    for x in range(1, 4):
        números_digitados.append(obterNúmeroInteiroDoUsuário(x))

    números_digitados.sort()

    mostrarResultado(números_digitados[0], números_digitados[2])


main()