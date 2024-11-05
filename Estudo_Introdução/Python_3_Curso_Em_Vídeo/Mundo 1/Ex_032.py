#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from calendar import isleap
from datetime import date

print(f'\n{'- Me informe um ano qualquer, e eu te digo se ele é BISSEXTO -':^67}\n')

anoInformado = int(input('Qual o ano(0 para o ano atual)? '))

if anoInformado == 0:
    anoInformado = date.today().year

print(f'\nO ano de {anoInformado}', end=' ')

if isleap(anoInformado) == True:
    print('é BISSEXTO.\n')
else:
    print('não é BISSEXTO.\n')