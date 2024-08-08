#Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import choice

print(f'\n{'- Vamos jogar Jokenpô? -':^29}\n')

escolhaDoUsuário = 0
escolhaDoComputador = choice(['pedra', 'papel', 'tesoura'])

while escolhaDoUsuário not in [1,2,3]:
    print('''Qual você vai escolher?
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')

    escolhaDoUsuário = int(input('Eu escolho: '))

    if escolhaDoUsuário not in [1,2,3]:
        print('Apenas as opções 1, 2 e 3! Tente Novamente!\n')
        sleep(2)

if escolhaDoUsuário == 1:
    escolhaDoUsuário = 'pedra'

    if escolhaDoUsuário == escolhaDoComputador:
        vitória = 1
    elif escolhaDoComputador == 'tesoura':
        vitória = 2
    elif escolhaDoComputador == 'papel':
        vitória = 3

elif escolhaDoUsuário == 2:
    escolhaDoUsuário = 'papel'

    if escolhaDoComputador == escolhaDoUsuário:
        vitória = 1
    elif escolhaDoComputador == 'pedra':
        vitória = 2
    elif escolhaDoComputador == 'tesoura':
        vitória = 3

elif escolhaDoUsuário == 3:
    escolhaDoUsuário = 'tesoura'
    
    if escolhaDoComputador == escolhaDoUsuário:
        vitória = 1
    elif escolhaDoComputador == 'papel':
        vitória = 2
    elif escolhaDoComputador == 'pedra':
        vitória = 3

sleep(0.5)
print('\nJO', end='')
sleep(0.5)
print('KEN', end='')
sleep(0.5)
print('PÔ\n')
sleep(0.5)

print(f'Você escolheu {escolhaDoUsuário.upper()} e o Computador escolheu {escolhaDoComputador.upper()}')

if vitória == 1:
    print('FOI EMPATE!\n')

elif vitória == 2:
    print('VOCÊ GANHOU!\n')

elif vitória == 3:
    print('O COMPUTADOR GANHOU!\n')