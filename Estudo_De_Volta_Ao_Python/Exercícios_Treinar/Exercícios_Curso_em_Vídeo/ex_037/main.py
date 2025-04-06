from os import system

def obterNúmeroInteiroDoUsuário() -> int:
    número_digitado_pelo_usuário: int = int(input("Digite um número inteiro: "))
    return número_digitado_pelo_usuário


def mostrarMenuDeOpçõesDeConversãoDoNúmeroInteiro(número_digitado: int) -> None:
    print(f'''
Escolha uma opção para converter o número {número_digitado}:
    [ 1 ] para a base BINÁRIA
    [ 2 ] para a base OCTAL 
    [ 3 ] para a base HEXADECIMAL''')


def obterNúmeroDaOpçãoDoMenu(número_digitado: int) -> int:
    while True:
        mostrarMenuDeOpçõesDeConversãoDoNúmeroInteiro(número_digitado)

        número_opção_do_menu: int = int(input("Qual opção você escolhe? "))

        if número_opção_do_menu > 0 and número_opção_do_menu <= 3:
            return número_opção_do_menu
        else:
            system("clear")


def mostrarResultado(número_digitado: int, número_opção_conversão: int) -> None:
    base_conversão: str = ''
    número_convertido: str = ''

    if número_opção_conversão == 1:
        base_conversão: str = "BINNÁRIO"
        número_convertido: str = bin(número_digitado)

    elif número_opção_conversão == 2:
        base_conversão: str = "OCTAL"
        número_convertido: str = oct(número_digitado)

    elif número_opção_conversão == 3:
        base_conversão: str = "HEXADECIMAL"
        número_convertido: str = hex(número_digitado)

    print(f"\nO número {número_digitado} convertido na base {base_conversão} é {número_convertido}.\n")


def main() -> None:
    system("clear")

    número_inteiro_digitado_pelo_usuário: int = obterNúmeroInteiroDoUsuário()

    número_da_opção_de_conversão: int = obterNúmeroDaOpçãoDoMenu(número_inteiro_digitado_pelo_usuário)

    mostrarResultado(número_inteiro_digitado_pelo_usuário, número_da_opção_de_conversão)


main()