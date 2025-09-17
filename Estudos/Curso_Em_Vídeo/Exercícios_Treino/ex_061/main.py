from os import system

def obterOPrimeiroTermoDaPA() -> int:
    primeiro_termo_da_PA: int = int(input("Qual vai ser o Primeiro Termo da PA? "))

    return primeiro_termo_da_PA


def obterARazãoDaPA() -> int:
    razão_da_PA: int = int(input("Qual vai ser a Razão? "))

    return razão_da_PA


def calcularAPADosDezPrimeirosTermos(primeiro_termo: int = 1, razão: int = 2) -> None:
    termo_da_PA: int = 1
    termo_atual_da_PA: int = primeiro_termo

    while termo_da_PA <= 10:

        if termo_da_PA == 10:
            print(f"{termo_atual_da_PA}\n")
        else:
            print(f"{termo_atual_da_PA} ->", end=" ")

        termo_atual_da_PA += razão
        termo_da_PA += 1


def main() -> None:
    system("clear")

    primeiro_termo_da_PA: int = obterOPrimeiroTermoDaPA()
    razão_da_PA: int = obterARazãoDaPA() 

    calcularAPADosDezPrimeirosTermos(primeiro_termo_da_PA, razão_da_PA)


main()