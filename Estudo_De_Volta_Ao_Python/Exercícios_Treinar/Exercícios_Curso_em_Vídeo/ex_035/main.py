from os import system

def obterSegmentoDoUsuário(sequência_dos_segmentos: int = 1) -> float:
    segmento_digitado = float(input(f"Digite o {sequência_dos_segmentos}º segmento: "))
    return segmento_digitado


def analisarSeFormaUmTriângulo(a: float, b: float, c: float) -> str:
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        return ''
    else:
        return "NÃO "
    

def mostrarResultado(segmentos: list) -> None:
    print(f'''
Os segmentos {segmentos[0]} x {segmentos[1]} x {segmentos[2]}, {analisarSeFormaUmTriângulo(segmentos[0], segmentos[1], segmentos[2])}FORMAM um triângulo.
''')


def main() -> None:
    system("clear")

    segmentos_digitados: list = []

    for x in range(1, 4):
        segmentos_digitados.append(obterSegmentoDoUsuário(x))

    mostrarResultado(segmentos_digitados)


main()