#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.

print(f'\n{'- Escreva o nome da sua cidade, e eu te digo se começa com Santo -':^71}\n')

nomeDaCidade = input('Qual a sua cidade? ').lower().strip()

print(f'\nA cidade {nomeDaCidade.title()}, deu {nomeDaCidade.startswith('santo')} para começar o nome com SANTO.\n')