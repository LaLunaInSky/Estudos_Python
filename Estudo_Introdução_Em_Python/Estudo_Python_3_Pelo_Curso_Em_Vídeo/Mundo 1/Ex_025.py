#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

print(f'\n{'- Me informe seu nome completo, e eu te digo se nele tem SILVA -':^69}\n')

nomeCompleto = str(input('Qual o seu nome completo? ')).upper().strip()

print(f'\nO nome {nomeCompleto.title()}, deu {nomeCompleto.find('SILVA') != -1} para SILVA.\n')