from os import system

def obterLarguraOuAlturaDaParede(str):
    if str == "largura" or str == "altura":
        input_user = float(input(f"Qual a {str} da parede em metros? "))
        return input_user


def obterAÁreaDaParede(largura, altura):
    return round((largura * altura), 2)


def mostrarResultado(largura, altura, área):
    print(f'''
A parede com {largura}m e altura {altura}m, tem a área de {área}m².
A quantidade de tinta necessária para pintar essa parede é de {round((área / 2), 2)}l.
''')


def main():
    system("clear")

    largura_da_parede = obterLarguraOuAlturaDaParede("largura")
    altura_da_parede = obterLarguraOuAlturaDaParede("altura")
    área_da_parede = obterAÁreaDaParede(largura_da_parede, altura_da_parede)

    mostrarResultado(largura_da_parede, altura_da_parede, área_da_parede)


main()