#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-la por extenso. 

print(f'\n{'- Me informe um número entre 0 e 20, e eu te devolvo ele por extenso -':^75}\n')

númerosDe0À20PorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

perguntaSeQuerContinuar = ''

while perguntaSeQuerContinuar != 'N':
    while True:
        númeroInformadoPeloUsuário = int(input('Escreva um número que vai de 0 à 20: '))

        if 0 <= númeroInformadoPeloUsuário <= 20:
            break
        else:
            print('\033[31mAPENAS É ACEITO NÚEMROS DE 0 À 20!\033[m\n')

    print(f'\nO número {númeroInformadoPeloUsuário} por extenso é {númerosDe0À20PorExtenso[númeroInformadoPeloUsuário].capitalize()}.\n')

    while True:
        perguntaSeQuerContinuar = input('Quer continuar(S/N)? ').strip().upper()

        if perguntaSeQuerContinuar in ('S', 'N'):
            break
        else:
            print('\033[31mAPENAS É ACEITO S (sim) OU N (não)!\033[m\n')