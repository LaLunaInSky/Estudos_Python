from os import system

def obterONúmeroInteiroDigitadoPeloUsuário(mensagem_extra: str = "") -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input(f"Digite um Número Inteiro{mensagem_extra}: "))

    return número_inteiro_digitado_pelo_usuário


def somarNúmerosDigitados(números_digitados: list) -> int:
    soma_dos_números_digitados: int = 0

    for número in números_digitados:
        soma_dos_números_digitados += número

    return soma_dos_números_digitados


def organizadorDosNúmerosDigitados() -> None:
    números_digitados: list = []

    while True:
        número_digitado: int = obterONúmeroInteiroDigitadoPeloUsuário(" [999 para encerrar]")

        if número_digitado != 999:
            números_digitados.append(número_digitado)

        else:
            break

    print(f"\nForam digitados {len(números_digitados)} números, a soma dos mesmos é {somarNúmerosDigitados(números_digitados)}.\n")


def main() -> None:
    system("clear")

    organizadorDosNúmerosDigitados()


main()