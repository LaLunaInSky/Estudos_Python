from os import system
from math import sqrt

def obterOComprimentoDoCateto(str):
    if str == "oposto" or str == "adjacente":
        comprimento_do_cateto = round(float(input(f"Comprimento do cateto {str}: ")), 2)
        return comprimento_do_cateto


def calcularAHipotenusaDoTriânguloRetângulo(cateto_oposto, cateto_adjacente):
    return round(sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2)), 2)


def mostrarResultado(cateto_oposto, cateto_adjacente, hipotenusa):
    print(f'''
O triângulo Retângulo com o cateto oposto de {cateto_oposto} e o cateto adjacente de {cateto_adjacente} possui a hipotenusa de {hipotenusa}
''')


def main():
    system("clear")

    comprimento_do_cateto_oposto = obterOComprimentoDoCateto("oposto")
    comprimento_do_cateto_adjacente = obterOComprimentoDoCateto("adjacente")

    hipotenusa_do_triângulo_retângulo = calcularAHipotenusaDoTriânguloRetângulo(comprimento_do_cateto_oposto, comprimento_do_cateto_adjacente)

    mostrarResultado(comprimento_do_cateto_oposto, comprimento_do_cateto_adjacente, hipotenusa_do_triângulo_retângulo)


main()