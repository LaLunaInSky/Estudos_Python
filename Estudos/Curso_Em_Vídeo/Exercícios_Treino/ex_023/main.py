from os import system
from time import sleep

def obterNúmeroDoUsuário() -> int:
    número_digitado_usuário = -1

    while True:
        número_digitado_usuário = int(input("Digite um número entre 0 à 9999: "))

        if número_digitado_usuário <= 9999 and número_digitado_usuário >= 0:
            break

        system("clear")
    
    return número_digitado_usuário


def organizarLugaresDoNúmero(número_digitado: int) -> list:
    número_em_string = str(número_digitado)

    lista_de_lugares: list = []

    if len(número_em_string) == 4:
        for número in número_em_string:
            lista_de_lugares.append(int(número))

    elif len(número_em_string) == 3:
        lista_de_lugares.append(0)

        for número in número_em_string:
            lista_de_lugares.append(int(número))
    
    elif len(número_em_string) == 2:

        for x in range(2):
            lista_de_lugares.append(0)

        for número in número_em_string:
            lista_de_lugares.append(int(número))

    else:
        for x in range(3):
            lista_de_lugares.append(0)
        
        lista_de_lugares.append(int(número_em_string))

    return lista_de_lugares


def mostrarResultado(número_digitado: int) -> None:
    lista_de_número_organizada: list = organizarLugaresDoNúmero(número_digitado)
    
    sleep(1)

    print(f'''
unidade.: {lista_de_número_organizada[3]}
dezena..: {lista_de_número_organizada[2]}
centena.: {lista_de_número_organizada[1]}
milhar..: {lista_de_número_organizada[0]}
''')


def main() -> None:
    system("clear")

    número_informado = obterNúmeroDoUsuário()
    
    print(f"Analisando o número {número_informado}...")

    mostrarResultado(número_informado)


main()