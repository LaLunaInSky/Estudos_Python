#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print(f'\n{'- Vamos jogar Par ou Ímpar? -':^34}\n')

quantidadeDeVitóriasDoJogador = 0

while True:
    númeroDoComputador = randint(1,10)
    resultadoDaJogada = ganhadorDaPartida = parOuÍmparDoJogador = parOuÍmparDoComputador = ''
    númeroDoJogador = 0

    while númeroDoJogador ==  0 and parOuÍmparDoJogador == '':
        while True:
            númeroDoJogador = int(input('Jogue um número de 1 à 10: '))

            if 1 > númeroDoJogador or 10 < númeroDoJogador:
                print('\033[31mAPENAS NÚMEROS DE 1 À 10!\033[m\n')
            else:
                break

        while True:
            parOuÍmparDoJogador = input('Você quer Par ou Ímpar? ').strip().lower()[0]

            if parOuÍmparDoJogador == 'i':
                parOuÍmparDoJogador = 'í'

            if parOuÍmparDoJogador not in ['p', 'í']:
                print('\033[31mAPENAS PAR OU ÍMPAR\033[m\n')
            else:
                break

    if parOuÍmparDoJogador == 'í':
        parOuÍmparDoComputador = 'p'
    else:
        parOuÍmparDoComputador = 'í'

    somaDosNúmerosJogados = númeroDoJogador + númeroDoComputador
    
    if somaDosNúmerosJogados % 2 == 0:
        resultadoDaJogada = 'par'
    else:
        resultadoDaJogada = 'ímpar'

    if parOuÍmparDoComputador == resultadoDaJogada[0]:
        ganhadorDaPartida = 'computador'
    elif parOuÍmparDoJogador == resultadoDaJogada[0]:
        ganhadorDaPartida = 'jogador'
        quantidadeDeVitóriasDoJogador += 1

    print(f'A soma dos números é ({somaDosNúmerosJogados}), logo o resultado é \033[34m{resultadoDaJogada.capitalize()}\033[m, o ganhador foi o \033[35m{ganhadorDaPartida.upper()}\033[m.\n')

    pluralVitórias = ''

    if quantidadeDeVitóriasDoJogador != 1:
        pluralVitórias = 's'

    if ganhadorDaPartida == 'computador':
        print(f'\033[37mO jogador ganhou {quantidadeDeVitóriasDoJogador} vitória{pluralVitórias} consecutiva{pluralVitórias}!\033[m\n')
        break