from os import system

def obterUmNúmeroInteiroDigitadoPeloUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))
    
    return número_inteiro_digitado_pelo_usuário


def analisarSeJáExisteONúmeroDigitadoNaLista(lista_dos_números_digitados: list, número_digitado: int) -> bool:
    try:
        lista_dos_números_digitados.index(número_digitado)
        return True
    except ValueError:
        return False
    

def obterRespostaSobreAdicionarMaisUmNúmeroALista() -> str:
    while True:
        resposta_sobre_adicionar_mais_um_número_a_lista: str = str(input("Quer adicionar mais um número [S/N]? ")).lower()

        if resposta_sobre_adicionar_mais_um_número_a_lista == 's' or resposta_sobre_adicionar_mais_um_número_a_lista == 'n':
            print()
            return resposta_sobre_adicionar_mais_um_número_a_lista
        else:
            system("clear")


def armazenarNúmerosDigitadosEmUmaLista() -> list:
    números_únicos_digitados: list = []

    while True:
        número_inteiro_digitado_pelo_usuário: int = obterUmNúmeroInteiroDigitadoPeloUsuário()

        if analisarSeJáExisteONúmeroDigitadoNaLista(números_únicos_digitados, número_inteiro_digitado_pelo_usuário) == False:
            números_únicos_digitados.append(número_inteiro_digitado_pelo_usuário)
            print("Valor adicionado com sucesso...\n")
        else:
            print(f"O número {número_inteiro_digitado_pelo_usuário} já foi adicionado!\n")

        resposta_sobre_adicionar_mais_um_número_a_lista: str = obterRespostaSobreAdicionarMaisUmNúmeroALista()

        if resposta_sobre_adicionar_mais_um_número_a_lista == 'n':
            break

    return números_únicos_digitados


def mostrarNúmerosAdicionados(números_únicos_digitados: list) -> None:
    números_únicos_digitados.sort()

    print(f"Foi adicionado os números:", end="")

    for número in números_únicos_digitados:
        print(f" {número}", end=" ")
    
    print("\n")


def main() -> None:
    system("clear")

    números_únicos_digitados: list = armazenarNúmerosDigitadosEmUmaLista()

    mostrarNúmerosAdicionados(números_únicos_digitados)


main()