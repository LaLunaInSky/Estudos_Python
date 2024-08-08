#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

print(f'\n{'- Me informe 7 datas de nascimento, e eu te digo quantos são maiores e menores de idade -':^94}\n')

anoAtual = date.today().year
menorDeIdade = 0
maiorDeIdade = 0

for contagem in range(1, 8):
    dataDeNascimento = int(input(f'Qual a {contagem}ª Data? '))
    
    if (anoAtual - dataDeNascimento) < 18:
        menorDeIdade += 1
    else:
        maiorDeIdade += 1

print(f'\nDe Todas as datas de nascimentos tivemos {menorDeIdade} menores de idade, e {maiorDeIdade} maiores de idade ao todo.\n')