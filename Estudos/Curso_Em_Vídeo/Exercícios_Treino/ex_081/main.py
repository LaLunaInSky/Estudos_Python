from os import system

def obterONúmeroInteiroDigitadoPeloUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))
    
    return número_inteiro_digitado_pelo_usuário


def perguntarSeQuerAdicionarMaisUmNúmeroInteiroALista() -> bool:
    while True:
        resposta_se_quer_adicionar_mais_um_número_inteiro_a_lista: str = str(input("\nQuer adicionar mais um número [S/N]? "))

        if resposta_se_quer_adicionar_mais_um_número_inteiro_a_lista == 's':
            return True
        elif resposta_se_quer_adicionar_mais_um_número_inteiro_a_lista == 'n':
            return False
        else:
            system("clear")


def armazenarOsNúmerosInteirosDigitadosEmUmaLista() -> list:
    números_digitados: list = []

    while True:
        número_inteiro_digitado_pelo_usuário: int = obterONúmeroInteiroDigitadoPeloUsuário()

        números_digitados.append(número_inteiro_digitado_pelo_usuário)

        adicionar_novo_número_a_lista: bool = perguntarSeQuerAdicionarMaisUmNúmeroInteiroALista()
        
        print()

        if adicionar_novo_número_a_lista == False:
            break

    return números_digitados


def analisarSeONúmeroCincoEstáNaLista(números_digitados: list) -> str:
    try:
        números_digitados.index(5)
        return "está adicionado na lista"
    except ValueError:
        return "não está na lista"


def mostrarInformaçõesSobreOsNúmerosDigitados(números_digitados: list) -> None:
    números_digitados.sort(reverse=True)

    print(f'''
Foram adicionador {len(números_digitados)} números.
A Lista dos número em ordem decrescente é {números_digitados}.
O número 5 {analisarSeONúmeroCincoEstáNaLista(números_digitados)}.
''')


def main() -> None:
    system("clear")

    números_digitados: list = armazenarOsNúmerosInteirosDigitadosEmUmaLista()

    mostrarInformaçõesSobreOsNúmerosDigitados(números_digitados)


main()