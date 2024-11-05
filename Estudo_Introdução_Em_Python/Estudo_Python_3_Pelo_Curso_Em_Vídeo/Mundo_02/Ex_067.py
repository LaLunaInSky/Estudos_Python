#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

from time import sleep

print(f'\n{'- Me informe os números que você que ver a tabuada, número negativo encerra o programa -':^93}\n')

while True:
    númeroInformado = int(input('Qual número quer ver a tabuada? '))

    if númeroInformado < 0:
        break

    for contagem in range(1, 11):
        print(f'{númeroInformado} x {contagem:2} = {númeroInformado * contagem}')
    
    sleep(2)
    print()

print()