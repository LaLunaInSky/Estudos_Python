#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fagos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print(f'\n{'- A contagem vai começar -':^31}\n')

sleep(1)

for contagem in range(10, -1, -1):
    print(f'{contagem}...')
    sleep(1)

print('\nBoow! Buum! Powpow!\n')