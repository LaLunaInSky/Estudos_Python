from os import system

def obterONúmeroInteiroDigitadoPelousuário() -> int:
    while True:
        try:
            número_inteiro_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))

            return número_inteiro_digitado_pelo_usuário
        except ValueError:
            system("clear")
            print("Apenas é aceito número inteiro!")


def perguntarSeOUsuárioQuerDigitarMaisUmNúmeroInteiro() -> bool:
    while True:
        resposta_se_o_usuário_quer_digitar_mais_um_número_inteiro: str = str(input("Quer digitar mais um número para a lista [S/N]? ")).strip().lower()

        if resposta_se_o_usuário_quer_digitar_mais_um_número_inteiro == 's':
            return True
        
        elif resposta_se_o_usuário_quer_digitar_mais_um_número_inteiro == 'n':
            return False
        
        else:
            system("clear")


def armazenarOsNúmerosInteirosDigitadosEmUmaLista() -> list:
    números_digitados: list = []

    while True:
        número_inteiro_digitado_pelo_usuário: int = obterONúmeroInteiroDigitadoPelousuário()

        números_digitados.append(número_inteiro_digitado_pelo_usuário)

        resposta_se_o_usuário_quer_digitar_mais_um_número_para_a_lista: bool = perguntarSeOUsuárioQuerDigitarMaisUmNúmeroInteiro()

        if resposta_se_o_usuário_quer_digitar_mais_um_número_para_a_lista == False:
            break
        else:
            print()

    return números_digitados


def analisarQuaisSãoOsNúmerosParesDaListaInformada(números_digitados: list) -> list:
    números_pares_encontrados: list = []

    for número in números_digitados:
        if número % 2 == 0:
            números_pares_encontrados.append(número)

    if len(números_pares_encontrados) > 0:
        return números_pares_encontrados
    else:
        return ["Nenhum"]
    

def analisarQuaisSãoOsNúmerosÍmparesDaListaInformada(números_digitados: list) -> list:
    números_ímpares_encontrados: list = []

    for número in números_digitados:
        if número % 2 != 0:
            números_ímpares_encontrados.append(número)

    if len(números_ímpares_encontrados) > 0:
        return números_ímpares_encontrados
    else:
        return ["Nenhum"]


def mostrarInformaçõesFinaisSobreOsNúmerosDigitadosPeloUsuário(números_digitados: list) -> None:
    print(f'''
Os números digitados foram os {números_digitados}.
Os números PARES são {analisarQuaisSãoOsNúmerosParesDaListaInformada(números_digitados)}.
Os números ÍMPARES são {analisarQuaisSãoOsNúmerosÍmparesDaListaInformada(números_digitados)}.
''')


def main() -> None:
    system("clear")

    números_digitados: list = armazenarOsNúmerosInteirosDigitadosEmUmaLista()

    mostrarInformaçõesFinaisSobreOsNúmerosDigitadosPeloUsuário(números_digitados)


main()