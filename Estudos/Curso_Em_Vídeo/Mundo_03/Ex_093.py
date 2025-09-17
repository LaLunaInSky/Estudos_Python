#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print(f'\n{'- Me informe o nome de um jogador, quantas partidas ele jogou, e quantos gols fez em cada partida -':^104}\n')

informaçõesDoJogador = {}

informaçõesDoJogador['nome'] = input('Qual o nome do jogador? ').strip().capitalize()

quantidadeDePartidasJogadas = int(input(f'Quantas partidas {informaçõesDoJogador["nome"]} jogou? '))

informaçõesDoJogador['partidas'] = {}
informaçõesDoJogador['total de gols'] = 0

print(f'\n{'-'*50}')

for partida in range(1, quantidadeDePartidasJogadas + 1):
    informaçõesDoJogador['partidas'][f'{partida}ª partida'] = int(input(f'  Quantos gols {informaçõesDoJogador["nome"]} fez na {partida}ª Partida? '))
    
    informaçõesDoJogador['total de gols'] += informaçõesDoJogador['partidas'][f'{partida}ª partida']

print(f'{'-'*50}\n\n{'-'*50}\n{informaçõesDoJogador}\n{'-'*50}')

for key, value in informaçõesDoJogador.items():
    print(f'O campo {key.title()} tem valor {value}')

print(f'{'-'*50}\nO jogador {informaçõesDoJogador["nome"]} jogou {quantidadeDePartidasJogadas} partidas:')

for key, value in informaçõesDoJogador['partidas'].items():
    print(f'    → Na {key.title()} fez {value} gols.')

print(f'No total fez {informaçõesDoJogador["total de gols"]} gols.\n{'-'*50}\n')