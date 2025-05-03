from os import system

def obterOPrimeiroTermoDaPA() -> int:
    primeiro_termo_da_PA: int = int(input("Qual vai ser o Primeiro Termo da PA? "))

    return primeiro_termo_da_PA


def obterARazãoDaPA() -> int:
    razão_da_PA: int = int(input("Qual vai ser a razão? "))

    return razão_da_PA


def obterQuantidadeAMaisDeTermosDaPA() -> int:
    quantidade_a_mais_de_termos_da_PA: int = int(input("Quantos termos você quer ver a mais desta PA? "))

    return quantidade_a_mais_de_termos_da_PA


def calcularAPA(primeiro_termo: int = 0, razão: int = 1) -> None:
    posição_da_PA: int = 1
    termo_atual_da_PA: int = primeiro_termo
    
    while True:
        if posição_da_PA == 1:
            while posição_da_PA <= 10:
                if posição_da_PA == 10:
                    print(f"{termo_atual_da_PA}\n")
                else:
                    print(f"{termo_atual_da_PA} ->", end=" ")

                termo_atual_da_PA += razão
                posição_da_PA += 1
        else:
            while posição_da_PA <= quantidade_de_termos_a_mais_na_PA:
                if posição_da_PA == quantidade_de_termos_a_mais_na_PA:
                    print(f"{termo_atual_da_PA}\n")
                else:
                    print(f"{termo_atual_da_PA} ->", end=" ")

                termo_atual_da_PA += razão
                posição_da_PA += 1


        quantidade_de_termos_a_mais_na_PA: int = obterQuantidadeAMaisDeTermosDaPA()

        if quantidade_de_termos_a_mais_na_PA <= 0:
            print(f"\nProgressão Finalizada com {posição_da_PA - 1} termos mostrados.\n")
            break

        quantidade_de_termos_a_mais_na_PA += posição_da_PA - 1


def main() -> None:
    system("clear")

    primeiro_termo_da_PA: int = obterOPrimeiroTermoDaPA()
    razão_da_PA: int = obterARazãoDaPA()

    calcularAPA(primeiro_termo_da_PA, razão_da_PA)


main()