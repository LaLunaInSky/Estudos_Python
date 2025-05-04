from os import system

def obterNúmeroDigitadoPeloUsuário(mensagem_extra: str = "") -> int:
    número_digitado_pelo_usuário: int = int(input(f"Digite um número inteiro{mensagem_extra}: "))

    return número_digitado_pelo_usuário


def somaDosNúmeros(números_digitados: list) -> int:
    soma_dos_números: int = 0

    for número in números_digitados:
        soma_dos_números += número

    return soma_dos_números


def repetiçãoDoObterNúmero() -> None:
    números_digitados: list = []

    while True:
        número_digitado: int = obterNúmeroDigitadoPeloUsuário(" [999 para encerrar]")

        if número_digitado != 999:
            números_digitados.append(número_digitado)
        else:
            break

    print(f"\nForam digitados {len(números_digitados)} números, e a soma deles é de {somaDosNúmeros(números_digitados)}.\n")


def main() -> None:
    system("clear")

    repetiçãoDoObterNúmero()


main()