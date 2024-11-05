#Melhore o jogo do Ex_028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print(f'\n{'- Tente adivinhar o número que estou pensando de 0 à 10 -':^62}\n')

querContinuar = ''

while querContinuar != 'n':
    númeroDoComputador = randint(0, 10)
    palpiteDoUsuário = -1
    querContinuar = ''
    palpitesAtéAcertar = 0

    while palpiteDoUsuário != númeroDoComputador:

        while True:   
            palpiteDoUsuário = int(input('Qual o número que estou pensando? '))

            if palpiteDoUsuário > 10 or palpiteDoUsuário < 0:
                print('\033[33mApenas é aceito palpites de 0 à 10!\033[m\n')
            else:
                break

        if palpiteDoUsuário != númeroDoComputador:
            print('\033[31mERROU!\033[m', end=' ')

            if palpiteDoUsuário < númeroDoComputador:
                print('Tente um número maior...\n')
            else:
                print('Tente um número menor...\n')
        
        palpitesAtéAcertar += 1

    print(f'\033[32mEBA! Você Acertou.\033[m Foram {palpitesAtéAcertar} tentativas até acertar.\n')

    while querContinuar not in ['s', 'n']:
        querContinuar = input('Quer jogar novamente(S/N)? ').strip().lower()

        if querContinuar not in ['s', 'n']:
            print('\033[31mApenas é aceito S ou N!\033[m\n')
        
    palpiteDoUsuário = -1
    númeroDoComputador = randint(0, 10)

    print()