#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.

from math import trunc

print(f'\n{'- Me informe um número Real, e eu te devolvo a parte Inteira do mesmo -':^76}\n')

númeroEscolhido = float(input('Qual o número escolhido? '))

print(f'\nO número que você escolheu foi o {númeroEscolhido}, a parte Inteira é igual a {trunc(númeroEscolhido)}.\n')