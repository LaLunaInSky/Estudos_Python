from os import system

def obterONúmeroInteiroDigitadoPeloUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Informe um Número Inteiro: "))
    
    return número_inteiro_digitado_pelo_usuário


def calcularOFatorialDoNúmeroInformado(número_informado: int = 5) -> None:
    fatorial_do_número: int = número_informado

    print(f"{número_informado}! = {número_informado} x", end=" ")

    while True:
        número_informado -= 1
        fatorial_do_número *= número_informado


        if número_informado == 1:
            print(f"{número_informado}", end=" ")

            break
        else:
            print(f"{número_informado} x", end=" ")
    
    print(f"= {fatorial_do_número}")




def main() -> None:
    system("clear")

    número_inteiro_digitado_pelo_usuário: int = obterONúmeroInteiroDigitadoPeloUsuário()

    calcularOFatorialDoNúmeroInformado(número_inteiro_digitado_pelo_usuário)


main()