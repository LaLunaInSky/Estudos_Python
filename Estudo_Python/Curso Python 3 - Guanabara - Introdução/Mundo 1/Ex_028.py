#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o npumero escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print(f'\n{'- Vou pensar em um número de 0 á 5 e desafio você a acertar qual número pensei -':^85}\n')

númeroDoComputador = randint(0, 5)

númeroDoUsuário = int(input('Escolha um número(0 á 5): '))

if númeroDoComputador == númeroDoUsuário:
    print('\nParabéns! Você acertou o número que pensei', end=', ')
else:
    print('\nErrou! Que pena você não acertou o número que pensei', end=(', '))

print(f'é o {númeroDoComputador}.\n')