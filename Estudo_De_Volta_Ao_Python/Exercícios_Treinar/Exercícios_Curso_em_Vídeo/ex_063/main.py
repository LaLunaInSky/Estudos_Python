from os import system

def obterONúmeroInteiroDeQuantosTermosMostrar() -> int:
    while True:
        quantidade_de_termos: int = int(input("Quantos termos você quer ver da Sequência de Fibonacci? "))

        if quantidade_de_termos > 0:
            return quantidade_de_termos
        else:
            system("clear")


def mostrarASequênciaDeFibonacci(quantidade_de_termos: int = 7) -> None:
    penúltima_ocorrênca: int = 0
    última_ocorrência: int = 1
    próxima_ocorrência: int = penúltima_ocorrênca + última_ocorrência

    posição_da_sequência: int = 1

    while posição_da_sequência <= quantidade_de_termos:
        if posição_da_sequência % 3 == 0:
            print(f"{próxima_ocorrência}",end=" ")

            penúltima_ocorrênca = última_ocorrência + próxima_ocorrência
            última_ocorrência = penúltima_ocorrênca + próxima_ocorrência
            próxima_ocorrência = penúltima_ocorrênca + última_ocorrência

        elif posição_da_sequência % 3 == 2:
            print(f"{última_ocorrência}", end=" ")
        elif posição_da_sequência % 3 == 1:
            print(f"{penúltima_ocorrênca}", end=" ")
            

        if posição_da_sequência == quantidade_de_termos:
            print()
        else:
            print("->", end=" ")

        posição_da_sequência += 1


def main() -> None:
    system("clear")

    número_de_quantidade_de_termos_a_mostrar: int = obterONúmeroInteiroDeQuantosTermosMostrar()

    mostrarASequênciaDeFibonacci(número_de_quantidade_de_termos_a_mostrar)


main()