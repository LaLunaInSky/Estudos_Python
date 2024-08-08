#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print(f'\n{'- Informe um número qualquer, e eu te digo se ele é PAR ou ÍMPAR -':^71}\n')

númeroInformado = int(input('Qual é o número qualquer? '))

print(f'\nO número {númeroInformado}', end=' ')

if (númeroInformado%2) == 0:
    print(f'é PAR. \n')
else:
    print(f'é ÍMPAR. \n')