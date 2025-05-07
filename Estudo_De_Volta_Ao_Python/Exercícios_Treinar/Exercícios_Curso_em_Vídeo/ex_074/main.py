from os import system
from random import randint

def obterUmNúmeroInteiroAleatórioEntreUmaDez() -> int:
    número_sorteado: int = randint(1, 10)
    return número_sorteado


def analisarQualÉOMaiorNúmeroSorteado(cinco_números_sorteados: tuple) -> int:
    maior_número_sorteado: int = 0

    for posição, número in enumerate(cinco_números_sorteados):
        if posição == 0:
            maior_número_sorteado = número
        
        if maior_número_sorteado < número:
            maior_número_sorteado = número

    return maior_número_sorteado


def analisarQualÉOMenorNúmeroSorteado(cinco_números_sorteados: tuple) -> int:
    menor_número_sortado: int = 0

    for posição, número in enumerate(cinco_números_sorteados):
        if posição == 0:
            menor_número_sortado = número

        if menor_número_sortado > número:
            menor_número_sortado = número

    return menor_número_sortado


def mostrarInformaçõesSobreOsCincoNúmerosSorteados(cinco_números_sortados: tuple) -> None:
    print("Os números sorteados foram:", end=" ")

    for número in cinco_números_sortados:
        print(f"{número}", end=" ")

    print(f"\n\nO maior número sorteado foi o {analisarQualÉOMaiorNúmeroSorteado(cinco_números_sortados)}.")
    print(f"E O menor número sorteado foi o {analisarQualÉOMenorNúmeroSorteado(cinco_números_sortados)}.\n")


def main() -> None:
    system("clear")

    cinco_números_sorteados: tuple = (
        obterUmNúmeroInteiroAleatórioEntreUmaDez(),
        obterUmNúmeroInteiroAleatórioEntreUmaDez(),
        obterUmNúmeroInteiroAleatórioEntreUmaDez(),
        obterUmNúmeroInteiroAleatórioEntreUmaDez(),
        obterUmNúmeroInteiroAleatórioEntreUmaDez()
    )

    mostrarInformaçõesSobreOsCincoNúmerosSorteados(cinco_números_sorteados)


main()