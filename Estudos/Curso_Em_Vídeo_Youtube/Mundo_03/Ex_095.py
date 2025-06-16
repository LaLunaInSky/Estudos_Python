#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, dentro de uma lista geral.
#Aprimore o programa para que funcione com vários jogadores, incluindo um sistema de visualização de detalher de aproveitamento de cada jogador.

print(f'\n{'- Me informe as informações de vários jogadores, e eu te devolvo alguns dados sobre os mesmos -':^100}\n')

informaçõesDosJogadores = []
quantidadeDeJogadores = 1

while True:
    if quantidadeDeJogadores > 1:
        print()

    while quantidadeDeJogadores != len(informaçõesDosJogadores):
        dadoDoJogador = {}
        dadoDoJogador['nome'] = input(f'Qual o nome do {quantidadeDeJogadores}º jogador? ').strip().capitalize()
        dadoDoJogador['partidas'] = {}
        dadoDoJogador['total de gols'] = 0

        quantidadeDePartidasJogadas = int(input(f'Quantas partidas {dadoDoJogador["nome"]} jogou? '))
        
        for partida in range(1, (quantidadeDePartidasJogadas + 1)):
            dadoDoJogador['partidas'][f'{partida}ª partida'] = int(input(f'    Quantos gols {dadoDoJogador["nome"]} fez na {partida}ª Partida? '))
            dadoDoJogador['total de gols'] += dadoDoJogador['partidas'][f'{partida}ª partida']

        informaçõesDosJogadores.append(dadoDoJogador.copy())
        dadoDoJogador.clear()

    perguntaSobreContinuar = input('\nQuer adicionar mais um jogador (S/N)? ').strip().upper()

    if perguntaSobreContinuar in ('S', 'N'):
        if perguntaSobreContinuar == 'N':
            print()
            break
        else:
            quantidadeDeJogadores += 1

    else:
        print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m')

print(f'{'=-'*25}\n{' Resultado Dos Jogadores ':^50}\n{'=-'*25}\n{'No.':<6}{'Nome':<11}{'Gols Partidas':<15}{'Total Gols':>16}\n{'-'*50}')

for posição, jogador in enumerate(informaçõesDosJogadores):
    print(f'{f' {posição+1}.':<6}', end='')

    for key, value in jogador.items():
        if key == 'nome':
            print(f'{f'{value}':<11}', end='')
        elif key == 'partidas':
            for gols in value.values():
                print(gols, end=' ')
        else:
            númeroDeEspaços = 26 - (len(jogador["partidas"]) + (len(jogador["partidas"]) - 1))
            for espaço in range(1, númeroDeEspaços):
                print(' ', end='')
            print(f'{value}')

print('=-'*25)

while True:
    perguntarSeQuerMostrar = int(input('\nQuer ver os resulados de qual jogador (999 para nenhum)? '))

    if perguntarSeQuerMostrar == 999:
        print()
        break

    elif 1 <= perguntarSeQuerMostrar <= len(informaçõesDosJogadores):
        print(f'\n{'-'*50}\n-- LEVANTAMENTO DO JOGADOR {informaçõesDosJogadores[perguntarSeQuerMostrar - 1]["nome"].upper()}:')
        for key, value in informaçõesDosJogadores[perguntarSeQuerMostrar - 1]["partidas"].items():
            print(f'    → Na {key.title()} fez {value} gols.')
    
    else:
        print(f'\033[31mAPENAS É ACEITO 1 À {len(informaçõesDosJogadores)}\033[m')