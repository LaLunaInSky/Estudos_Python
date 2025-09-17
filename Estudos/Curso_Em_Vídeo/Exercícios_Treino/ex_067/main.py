from os import system

def obterONúmeroInteiroDigitadoPeloUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Qual tabuada você quer ver? "))

    return número_inteiro_digitado_pelo_usuário


def mostrarATabuadaDoNúmeroInformado(número_digitado: int = 2) -> None:
    print()
    for número in range(1, 11):
        if número == 10:
            print(f"{número_digitado} x {número} = {número_digitado * número}")
        else:
            print(f"{número_digitado} x  {número} = {número_digitado * número}")
    print()


def mostrarMaisTabuadaCasoONúmeroNãoSejaNegativo() -> None:
    while True:
        número_digitado_pelo_usuário: int = obterONúmeroInteiroDigitadoPeloUsuário()

        if número_digitado_pelo_usuário >= 0:
            mostrarATabuadaDoNúmeroInformado(número_digitado_pelo_usuário)
        else:
            break


def main() -> None:
    system("clear")

    mostrarMaisTabuadaCasoONúmeroNãoSejaNegativo()


main()