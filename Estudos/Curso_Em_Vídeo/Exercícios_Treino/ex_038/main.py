from os import system

def obterNúmeroInteiroDoUsuário(sequência: int = 1) -> int:
    número_digitado: int = int(input(f"Digite o {sequência}º Número: "))
    return número_digitado


def analisarONúmeroMaior(números: list) -> str:
    if números[0] > números[1]:
        return f"{números[0]}"
    elif números[1] > números[0]:
        return f"{números[1]}"
    elif números[0] == números[1]:
        return "São Iguais!"


def mostrarResultado(números: list) -> None:
    print("\nAnalisando os números:", end=' ')

    analise_números: str = analisarONúmeroMaior(números)

    if analise_números.isnumeric():
        print(f"O número maior é o {analise_números}.\n")
    else:
        print(f"Os números {analise_números}\n")


def main() -> None:
    system("clear")

    números_digitados: list = []

    for x in range(1, 3):
        números_digitados.append(obterNúmeroInteiroDoUsuário(x))

    mostrarResultado(números_digitados)


main()