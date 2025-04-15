from os import system

def obterOPesoPeloUsuário(sequência: int = 0) -> float:
    peso_informado: float = float(input(f"Qual o peso da {sequência}ª Pessoa? "))
    return peso_informado


def mostrarResultado(pesos: list) -> None:
    pesos.sort()

    print(f'''
O menor peso informado foi {pesos[0]}Kg,
e o maior peso informado foi {pesos[4]}Kg. 
''')


def main() -> None:
    system("clear")

    pesos_das_pessoas: list = []

    for count in range(1, 6):
        pesos_das_pessoas.append(obterOPesoPeloUsuário(count))

    mostrarResultado(pesos_das_pessoas)


main()