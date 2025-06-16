from os import system

def obterNúmeroEmMetros():
    input_user = float(input("Digite uma distância em metros: "))
    return input_user


def mostrarResultado(distância_em_metros):
    print(f'''
{distância_em_metros/1000}km
{distância_em_metros/100}hm
{distância_em_metros/10}dam
{distância_em_metros}m
{distância_em_metros*10}dm
{distância_em_metros*100}cm
{distância_em_metros*1000}mm
''')


def main():
    system("clear")

    distância_em_metros = obterNúmeroEmMetros()

    mostrarResultado(distância_em_metros)


main()