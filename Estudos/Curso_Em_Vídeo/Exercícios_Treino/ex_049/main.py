from os import system

def obterNúmeroParaATabuada() -> int:
    número_para_tabuada: int = int(input("Digite um número para descobrir sua tabuada: "))
    return número_para_tabuada


def mostrarATabuadaDoNúmeroInformado(número_informado: int) -> None:
    for x in range(1, 11):
        if x == 10:
            print(f"{número_informado} x {x} = {número_informado * x}")
        else:    
            print(f"{número_informado} x {x}  = {número_informado * x}")


def main() -> None:
    system("clear")

    número_para_tabuada: int = obterNúmeroParaATabuada()
    
    mostrarATabuadaDoNúmeroInformado(número_para_tabuada)


main()