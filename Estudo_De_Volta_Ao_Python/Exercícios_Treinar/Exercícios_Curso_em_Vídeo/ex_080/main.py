from os import system

def obterNúmeroInteiroDigitadoPeloUsuário() -> int: 
    número_inteiro_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))

    return número_inteiro_digitado_pelo_usuário


def retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário: int) -> None:
    print(f"\nO Número {número_inteiro_digitado_pelo_usuário} foi adicionado no final da lista.\n")


def retornoDoPrintDaPosiçãoDoNúmeroNaLista(
        número_inteiro_digitado_pelo_usuário: int,
        posição_do_número: int
    ) -> None:

    print(f"\nO Número {número_inteiro_digitado_pelo_usuário} foi adicionado na posição {posição_do_número}.\n")


def analisarONúmeroEDefinirAPosiçãoAAdicionarOMesmoEmUmaLista(
        número_inteiro_digitado_pelo_usuário: int, 
        números_digitados: list
    ) -> list:

    if len(números_digitados) == 0:
            números_digitados.append(número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário)

    elif len(números_digitados) == 1:
        if números_digitados[0] < número_inteiro_digitado_pelo_usuário:

            números_digitados.append(número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário)
        
        else:
            números_digitados.insert(0, número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 0)

    elif len(números_digitados) == 2:
        if números_digitados[0] < número_inteiro_digitado_pelo_usuário:

            if números_digitados[1] < número_inteiro_digitado_pelo_usuário:

                números_digitados.append(número_inteiro_digitado_pelo_usuário)
                retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário)

            else:
                números_digitados.insert(1, número_inteiro_digitado_pelo_usuário)
                retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 1)
        
        else:
            números_digitados.insert(0, número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 0)

    elif len(números_digitados) == 3:
        if números_digitados[0] < número_inteiro_digitado_pelo_usuário:

            if números_digitados[1] < número_inteiro_digitado_pelo_usuário:

                if números_digitados[2] < número_inteiro_digitado_pelo_usuário:

                    números_digitados.append(número_inteiro_digitado_pelo_usuário)
                    retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário)

                else:
                    números_digitados.insert(2, número_inteiro_digitado_pelo_usuário)
                    retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 2)

            else:
                números_digitados.insert(1, número_inteiro_digitado_pelo_usuário)
                retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 1)
        
        else:
            números_digitados.insert(0, número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 0)

    elif len(números_digitados) == 4:
        if números_digitados[0] < número_inteiro_digitado_pelo_usuário:

            if números_digitados[1] < número_inteiro_digitado_pelo_usuário:

                if números_digitados[2] < número_inteiro_digitado_pelo_usuário:

                    if números_digitados[3] < número_inteiro_digitado_pelo_usuário:

                        números_digitados.append(número_inteiro_digitado_pelo_usuário)
                        retornoDoPrintDaÚltimaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário)

                    else:
                        números_digitados.insert(3, número_inteiro_digitado_pelo_usuário)
                        retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 3)

                else:
                    números_digitados.insert(2, número_inteiro_digitado_pelo_usuário)
                    retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 2)

            else:
                números_digitados.insert(1, número_inteiro_digitado_pelo_usuário)
                retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 1)
        
        else:
            números_digitados.insert(0, número_inteiro_digitado_pelo_usuário)
            retornoDoPrintDaPosiçãoDoNúmeroNaLista(número_inteiro_digitado_pelo_usuário, 0)

    return números_digitados


def armazenarOsNúmerosInteirosDigitadosEmUmaLista() -> list:
    números_digitados: list = []

    while len(números_digitados) < 5:
        número_inteiro_digitado_pelo_usuário: int = obterNúmeroInteiroDigitadoPeloUsuário()
        
        números_digitados = analisarONúmeroEDefinirAPosiçãoAAdicionarOMesmoEmUmaLista(
            número_inteiro_digitado_pelo_usuário,
            números_digitados
        )

    return números_digitados


def mostrarAListaDosNúmerosDigitados(números_digitados: list) -> None:
    print(f'''{"-=" * 25}
Os Números digitados em ordem são {números_digitados}
''')


def main() -> None:
    system("clear")

    números_digitados: list = armazenarOsNúmerosInteirosDigitadosEmUmaLista()

    mostrarAListaDosNúmerosDigitados(números_digitados)


main()