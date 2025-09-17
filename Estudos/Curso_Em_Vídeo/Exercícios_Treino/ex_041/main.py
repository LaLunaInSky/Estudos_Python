from os import system
from datetime import datetime

ano_atual: int = datetime.now().year

def obterAnoDeNascimentoDoUsuário() -> int:
    while True:
        ano_de_nascimento: int = int(input("Em que ano você nasceu? "))

        if ano_de_nascimento >= (ano_atual - 100) and ano_de_nascimento <= ano_atual:
            return ano_de_nascimento
        else:
            system("clear")


def calcularIdadeDoUsuário(ano_de_nascimento: int) -> int:
    return (ano_atual - ano_de_nascimento)


def definirACategoriaDoUsuário(idade: int) -> str:
    if idade <= 9:
        return "MIRIM"
    elif idade <= 14:
        return "INFANTIL"
    elif idade <= 19:
        return "JUNIOR"
    elif idade <= 25:
        return "SÊNIOR"
    else:
        return "MASTER"


def mostrarResultado(dados_do_usuário: dict) -> None:

    print(f'''
A pessoa que nasceu em {dados_do_usuário["ano_de_nascimento"]} e tem {dados_do_usuário["idade"]} anos,
está ma categoria {dados_do_usuário["categoria"]}.
''')


def main() -> None:
    system("clear")

    dados_do_usuário: dict = {
        "ano_de_nascimento": 0,
        "idade": 0,
        "categoria": ''
    }

    dados_do_usuário["ano_de_nascimento"] = obterAnoDeNascimentoDoUsuário()

    dados_do_usuário['idade'] = calcularIdadeDoUsuário(dados_do_usuário["ano_de_nascimento"])

    dados_do_usuário["categoria"] = definirACategoriaDoUsuário(dados_do_usuário["idade"])

    mostrarResultado(dados_do_usuário)


main()