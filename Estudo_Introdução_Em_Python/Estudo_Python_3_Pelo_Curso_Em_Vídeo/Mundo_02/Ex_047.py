#Crie um programa que mostre na tela todos os número pares que estão no intervalo entr 1 e 50.

from time import sleep

print(f'\n{'- Irei te mostrar uma sequência par que vai do 1 até o 50 -':^64}\n')
sleep(0.5)

for númeroPar in range(2, 51, 2):
    print(númeroPar, end=' ')
    sleep(0.3)

print('- Fim da Sequência -\n')
sleep(0.5)