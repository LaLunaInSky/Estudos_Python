from os import system
from math import sin, cos, tan, radians

def obterÂnguloDoUsuário():
    ângulo_usuário = round(float(input("Digite um ângulo: ")), 1)
    return ângulo_usuário


def mostrarResultado(ângulo):
    print()

    categoriasEResultados = [["seno", "cosseno", "cosseno"], [round(sin(radians(ângulo)), 1), round(cos(radians(ângulo)), 1), round(tan(radians(ângulo)), 1)]]


    for x in range(3):
        print(f"O Ângulo {ângulo} tem o {categoriasEResultados[0][x].upper()} de {categoriasEResultados[1][x]}")


def main():
    system("clear")

    ângulo_digitado = obterÂnguloDoUsuário()

    mostrarResultado(ângulo_digitado)


main()