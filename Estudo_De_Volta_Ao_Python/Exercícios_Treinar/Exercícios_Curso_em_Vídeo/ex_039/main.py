from os import system
from datetime import datetime

ano_atual: int = datetime.now().year

def obterAnoDeNascimentoDoUsuário() -> int:
    while True:
        ano_de_nascimento: int = int(input("Qual o seu ano de nascimento? "))

        if ano_de_nascimento > (ano_atual - 100) and ano_de_nascimento <= ano_atual:
            return ano_de_nascimento
        else:
            system("clear")


def calcularIdadeDoUsuário(ano_de_nascimento: int) -> int:
    return (ano_atual - ano_de_nascimento)


def analisarBaseadoNaIdadeORecutramentoMilitarDoUsuário(idade: int) -> str:
    if idade == 18:
        return f"Seu alistamento é obrigatório agora em {ano_atual}.\n"
    elif idade > 18:
        return f"já Passou o seu alistamento, há {idade - 18} anos,\nseu alistamento foi em {ano_atual - (idade - 18)}.\n"
    elif idade < 18:
        return f"não Precisa se alistar, ainda falta {18 - idade} anos.\nSeu alistamento será em {ano_atual + (18 - idade)}.\n"


def mostrarResultado(ano_de_nascimento: int, idade: int) -> int:
    print(f"\nVocê que nasceu em {ano_de_nascimento} e tem {idade} anos,\n{analisarBaseadoNaIdadeORecutramentoMilitarDoUsuário(idade)}")


def main() -> None:
    system("clear")

    ano_de_nascimento_do_usuário: int = obterAnoDeNascimentoDoUsuário()

    idade_do_usuário: int = calcularIdadeDoUsuário(ano_de_nascimento_do_usuário)

    mostrarResultado(ano_de_nascimento_do_usuário, idade_do_usuário)


main()