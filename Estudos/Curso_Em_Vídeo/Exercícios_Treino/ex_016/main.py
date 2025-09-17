from os import system

def obterUmNúmeroFloatDoUsuário():
    número_float = float(input("Digite um número Real: "))
    return número_float


def mostrarResultado(número_float):
    print(f'''
O número Real {número_float} tem a parte inteira {int(número_float)}.
''')


def main():
    system("clear")

    número_digitado_pelo_usuário = obterUmNúmeroFloatDoUsuário()

    mostrarResultado(número_digitado_pelo_usuário)


main()