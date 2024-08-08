#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e 
#também indique o menor e o maior valor que estão na tupla.

from random import randint

print(f'\n{'- Irei sortear 5 números, e informar quais foram, depois o maior e  o menor entre eles -':^93}\n')

númerosSorteadosPeloComputador = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os números que o computador sorteou foram os:', end=' ')

for posiçãoDoNúmero, número in enumerate(númerosSorteadosPeloComputador):
    if posiçãoDoNúmero == (len(númerosSorteadosPeloComputador) - 1) :
        print(número)
    else:
        print(número, end=' - ')

print(f'''
O Menor número sorteado foi o {min(númerosSorteadosPeloComputador)}, e o Maior número foi o {max(númerosSorteadosPeloComputador)}.
''')