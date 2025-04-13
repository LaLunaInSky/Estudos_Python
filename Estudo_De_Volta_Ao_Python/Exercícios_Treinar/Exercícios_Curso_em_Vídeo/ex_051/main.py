from os import system

def obterOPrimeiroTermoDaPA() -> int:
    primeiro_termo: int = int(input("Primeiro Termo: "))
    return primeiro_termo


def obterARazãoDaPA() -> int:
    razão: int = int(input("A Razão: "))
    return razão


def mostrarAPA(primeiro_termo: int, razão: int) -> None:
    if razão <= 0:
        razão = 1
    
    ultimo_termo_da_PA: int = primeiro_termo

    for x in range(10):
        ultimo_termo_da_PA += razão

    for x in range(primeiro_termo, ultimo_termo_da_PA, razão):
        if x == (ultimo_termo_da_PA - razão):
            print(f"{x}.\n")
        elif x == primeiro_termo:
            print(f"\n{x} ->", end=' ')
        else:
            print(f"{x} ->", end=' ')


def main() -> None:
    system("clear")

    print(f"{"=" * 35}\n{"10 Primeiros termos da PA":^35}\n{"=" * 35}")

    primeiro_termo_da_PA: int = obterOPrimeiroTermoDaPA()

    razão_da_PA: int = obterARazãoDaPA()

    mostrarAPA(primeiro_termo_da_PA, razão_da_PA)


main()