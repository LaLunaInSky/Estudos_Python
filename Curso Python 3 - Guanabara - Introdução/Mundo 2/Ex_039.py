#Faça um programa que leia o ano de nascimento de um jovem ,e informe de acordo com sua idade se ele ainda vai se alistar ao serviço militar, 
#se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print(f'\n{'- Me informe seu ano de nascimento, e eu te informo sobre seu alistamento do serviço militar -':^99}\n')

anoDeNascimentoDoUsuário = int(input('Qual seu ano de nascimento? '))
anoAtual = date.today().year
idadeDoUsuário = anoAtual - anoDeNascimentoDoUsuário

print(f'\nVocê tem {idadeDoUsuário} anos,', end=' ')

if idadeDoUsuário < 18:
    print(f'logo faltam {18 - idadeDoUsuário}', end=' ')
    
    if (18 - idadeDoUsuário) > 1:
        print('anos', end=' ')
    else:
        print('ano', end=' ')

    print('para o seu alistamento no serviço militar.\n')

elif idadeDoUsuário == 18:
    print(f'está no ano do seu alistamento no serviço militar.\n')

else:
    print(f'já se passaram {idadeDoUsuário - 18}', end=' ')
    
    if (idadeDoUsuário - 18) > 1:
        print('anos', end=' ')
    else:
        print('ano', end=' ')

    print('do seu prazo do alistamento no serviço militar.\n')