#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categria, de acordo com a idade:
#-Até 9 anos: Mirim
#-Até 14 anos: Infantil
#-Até 19 anos: Junior
#-Até 25 anos: Sênior
#-Acima: Master

from datetime import date

print(f'\n{'- Me informe o ano de nascimento, e eu te digo em qual liga a pessoa ficará -':^82}\n')

anoDeNascimentoDoUsuário = int(input('Qual o ano de nascimento? '))
anoAtual = date.today().year
idadeDoUsuário = anoAtual - anoDeNascimentoDoUsuário

print(f'\nA pessoa nascida no ano de {anoDeNascimentoDoUsuário} com {idadeDoUsuário} anos, ficará na Liga', end=' ')

if idadeDoUsuário <= 9:
    print('MIRIM.\n')

elif idadeDoUsuário <= 14:
    print('INFANTIL.\n')

elif idadeDoUsuário <= 19:
    print('JUNIOR.\n')

elif idadeDoUsuário <= 25:
    print('SÊNIOR.\n')

else:
    print('MASTER.\n')