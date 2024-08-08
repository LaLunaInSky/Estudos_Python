#Faça um programa que tenha uma lista chamada númmeros e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro 
#da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

print(f'\n{'- Irei sortear 5 números, e somar os que forem PARES -':^59}\n')

def sorteia():
    número = randint(0, 10)
    return número

def somarPar(lista):
    soma = 0
    for número in lista:
        if número % 2 == 0:
            soma += número
    return soma


números = []

print('Sorteando 5 números:', end=' ')

for contagem in range(1, 6):
    sleep(1)
    while True:
        número  = sorteia()

        if número not in números:
            números.append(número)
            print(número, end=' ')
            break
        
print(f'\nA soma dos números PARES na lista {números} é igual à {somarPar(números)}.\n')