#Crie um programa que leia dois valores e mostre um menu com as opções Somar, Multiplicar, Maior, Novos números, Sair do programa.
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print(f'\n{'- Me informe dois valores, e eu irei fazer operações com eles -':^68}')

opçãoDoMenu = 0
númerosInformados = []

while opçãoDoMenu != 5:

    while númerosInformados == []:
        print()
        for contagem in range(1, 3):
            valorInformado = int(input(f'Qual o {contagem}º Valor? '))
            númerosInformados.append(valorInformado)

    opçãoDoMenu = 0

    while opçãoDoMenu > 5 or opçãoDoMenu < 1:
        print('''\n[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior Valor
[ 4 ] Novos Valores
[ 5 ] Sair do Programa''')

        opçãoDoMenu = int(input('Qual Opção do Menu Você Escolhe? '))

        if opçãoDoMenu > 5 or opçãoDoMenu < 1:
            print('\33[31mApenas é aceito do 1 ao 5!\033[m')    
            
        else:
            if opçãoDoMenu == 1:
                print(f'\nA soma dos valores {númerosInformados[0]} + {númerosInformados[1]} = {númerosInformados[0] + númerosInformados[1]}')
                sleep(2)

            elif opçãoDoMenu == 2:
                print(f'\nA multiplicação dos valores {númerosInformados[0]} X {númerosInformados[1]} = {númerosInformados[0] * númerosInformados[1]}')
                sleep(2)

            elif opçãoDoMenu == 3:
                if númerosInformados[0] > númerosInformados[1]:
                    valorMaior = númerosInformados[0]
                else:
                    valorMaior = númerosInformados[1]

                print(f'\nO valor maior digitado foi o {valorMaior}')
                sleep(2)

            elif opçãoDoMenu == 4:
                númerosInformados.clear()

sleep(1)
print('\nFECHANDO O PROGRAMA', end='')

for contagem in range(1, 4):
    sleep(1)
    print('.', end='')

sleep(1)
print('\n')