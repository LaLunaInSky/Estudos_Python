#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão.

from time import sleep

print(f'\n{'- Me informe o 1º termo e a razão da PA, e eu te devolvo os 10 primeiros termos da mesma -':^95}\n')

primeiroTermo = int(input('Qual o 1º termo da PA? '))
razão = int(input('Qual a razão da PA? '))
pA = primeiroTermo

print()
sleep(0.5)

for contagem in range(1, 11):
    print(pA, end=' -> ')
    pA += razão
    sleep(0.3)

print('Fim Da PA.\n')