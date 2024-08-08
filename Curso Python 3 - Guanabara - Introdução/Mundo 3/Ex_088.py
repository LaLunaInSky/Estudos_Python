#faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números 
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print(f'\n{'- Me informe quantos jogos da MEGA SENA você quer, e eu te devolvo os números sorteados -':^94}\n')

númeroDeJogos = int(input('Quantos jogos você quer sortear? '))
jogosSorteados = []

print(f'\n{f' Sorteando {númeroDeJogos} Jogos ':=^43}')

for jogo in range(0, númeroDeJogos):
    print(f'{jogo + 1}º Jogo → ', end='')
    
    númerosSorteados = []

    for contagem in range(0, 7):
        númeroSorteado = randint(1, 60)

        if númeroSorteado not in númerosSorteados:
            númerosSorteados.append(númeroSorteado)
    
    jogosSorteados.append(númerosSorteados[:])
    númerosSorteados.clear()

    print(f'{sorted(jogosSorteados[jogo])}')

print('='*43, '\n')