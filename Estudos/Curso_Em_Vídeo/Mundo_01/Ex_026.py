#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'.
#Em que posição ela aparece a primeira vez.
#Em que posição ela aprece a última vez.

print(f'\n{'- Escreva uma frase qualquer, e eu te digo informções sobre a letra A nela -':^81}\n')

fraseEscrita = str(input('Escreva uma frase: ')).strip().lower()

print(f'''
Na frase ({fraseEscrita.title()}):
-A letra "A" aparece {fraseEscrita.count('a')} vezes.
-A letra "A" aparece pela primeira vez na posição {fraseEscrita.index('a')+1}.
-A letra "A" aparece pela última vez na posição {fraseEscrita.rindex('a')+1}.
''')