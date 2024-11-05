#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No finla, coloque esse dicionário em ordem, 
#sabendo que o vencedos tirou o maior número do dado.

from random import randint
from time import sleep

print(f'\n{'- 4 jogadores irão jogar o dado, e irei dolocar na ordem de maiores resultados -':^85}\n')

jogadaDosJogadores = {}

for jogada in range(1, 5):
    jogadaDosJogadores[f'Jogador {jogada}'] = randint(1, 6)

print('=-'*16, f'\n{'JOGANDO OS DADOS':^32}', f'\n{'=-'*16}')

for key, value in jogadaDosJogadores.items():
    sleep(1)
    print(f' → O {key} tirou {value} no dado')

print('=-'*16, f'\n\n{' Ranking Dos Ganhadores ':=^40}')

sleep(1)

contagem = 1

for key, value in sorted(jogadaDosJogadores.items(), key=lambda x: x[1], reverse=True):
    print(f'{f'{contagem}º Lugar → {key} jogou {value} no dado':^40}')
    
    contagem += 1

print()