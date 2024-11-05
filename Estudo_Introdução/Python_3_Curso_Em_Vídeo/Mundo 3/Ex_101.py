#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro um valor literal indicando se uma pessoa tem voto 
#NEGADO, OPCIONAl ou OBRIGATÓRIO nas eleições.

from datetime import date

print(f'\n{'- Me informe sua idade, e eu te digo o estado da obrigatoridade do sue voto -':^82}\n')

def voto(idade):
    if idade < 16:
        return 'não é obrigatório'
    elif 18 > idade >= 16 or idade > 70: 
        return 'é opcional'
    else:
        return 'é obrigatório'

anoDeNascimento = int(input('Qual ano você nasceu? '))
idade = date.today().year - anoDeNascimento

print(f'Você que tem {idade} anos, o seu voto {voto(idade)}!\n')