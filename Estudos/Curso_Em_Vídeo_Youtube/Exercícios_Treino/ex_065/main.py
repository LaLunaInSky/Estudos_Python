from os import system

def obterNúmeroInteiroDigitadoPeloUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))

    return número_inteiro_digitado_pelo_usuário


def perguntarAoUsuárioSeQuerAdiconarMaisUmNúmero() -> str:
    while True:
        pergunta_se_quer_continuar: str = str(input("Quer adicionar mais um número [S/N]: ")).lower()

        if pergunta_se_quer_continuar == 's' or pergunta_se_quer_continuar == 'n':
            break
        else:
            print("\nErro, apenas é aceito S ou N como resposta!\n")

    return pergunta_se_quer_continuar


def analisarQualÉAMédiaDosNúmerosDigitados(números_digitados: list) -> float:
    soma_dos_números: int = 0

    for número in números_digitados:
        soma_dos_números += número

    média_dos_números: float = soma_dos_números / len(números_digitados)

    return média_dos_números


def organizadorDosNúmerosDigitados() -> None:
    números_digitados: list = []
    
    while True:
        número_digitado: int = obterNúmeroInteiroDigitadoPeloUsuário()
        números_digitados.append(número_digitado)

        resposta_da_pergunta: str = perguntarAoUsuárioSeQuerAdiconarMaisUmNúmero()

        if resposta_da_pergunta == 'n':
            break

    números_digitados.sort()

    print(f"\nForam digitados {len(números_digitados)} números, a média dos mesmo é de {analisarQualÉAMédiaDosNúmerosDigitados(números_digitados):.2f}. \nO maior número digitado foi o {números_digitados[-1]} e o menor foi o {números_digitados[0]}.\n")

def main() -> None:
    system("clear")

    organizadorDosNúmerosDigitados()


main()