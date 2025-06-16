#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

from time import sleep

print(f'\n{'- Me informe um número, e eu te digo se ele é ou não um número primo -':^75}\n')

númeroInformado = int(input('Qual o número? '))

vezesDividido = 0

sleep(0.5)
print()

for contagem in range(1, númeroInformado+1):
    if númeroInformado % contagem == 0:
        print(f'\033[34m({contagem})\033[m', end=' ')
        vezesDividido += 1

    else:
        print(contagem, end=' ')

    sleep(0.3)

print(f'\n\nO número {númeroInformado} foi {vezesDividido} vezes divido, logo ele', end=' ')

if vezesDividido == 2:
    print('é um número PRIMO!\n')
else:
    print('\033[31mNÃO\033[m é um número PRIMO!\n')