from os import system 
from datetime import datetime

def obterAnoDigitadoPeloUsuário() -> int:
    while True:
        ano_digitado: int = int(input("Digite um ano, caso queira o atual digite 0: "))

        if ano_digitado >= 1900 or ano_digitado == 0:
            if ano_digitado == 0:
                return datetime.now().year
            else:
                return ano_digitado
        else:
            system("clear")


def analisarSeOAnoÉBissexto(ano_digitado: int) -> str:
    if ano_digitado % 400 == 0 or (ano_digitado % 4 == 0 and ano_digitado % 100 != 0):
        return "é BISSEXTO"
    else:
        return "NÃO é BISSEXTO"


def mostrarResultado(ano_digitado: int) -> None:
    print(f'''
O ano {ano_digitado} {analisarSeOAnoÉBissexto(ano_digitado)}.
''')


def main() -> None:
    system("clear")

    ano_digitado: int = obterAnoDigitadoPeloUsuário()

    mostrarResultado(ano_digitado)


main()