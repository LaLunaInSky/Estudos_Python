#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

print(f'\n{'- Escreva 4 nomes, e eu sorteio entre eles 1 nome -':^56}\n')

primeiroNome = input('Escreva o 1º nome: ')
segundoNome = str(input('Agora o 2º nome: '))
terceiroNome = input('O 3º nome: ')
quartoNome = str(input('E o 4º nome: '))

print(f'\nO nome sorteado foi {choice([primeiroNome, segundoNome, terceiroNome, quartoNome]).upper()}.\n')