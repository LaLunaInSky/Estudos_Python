#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Ex: Apos a sopa, A sacada da casa, A torre da derrota, O lobo ama o bolo, Anotaram a data da maratona.

print(f'\n{'- Escreva uma frase qualquer, e eu te digo se ela é Palíndroma -':^69}\n')

fraseDigitada = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
letrasIguais = 0

print(f'\nA frase {fraseDigitada} ou contrario {fraseDigitada[::-1]}', end=' ')

for contagem in range(0, len(fraseDigitada)):
    if fraseDigitada[contagem] == fraseDigitada[::-1][contagem]:
        letrasIguais += 1

if letrasIguais == len(fraseDigitada):
    print('é \033[32mPALÍNDROMA!\033[m\n')
else:
    print('\033[31mNÃO\033[m é PALÍNDROMA!\n')