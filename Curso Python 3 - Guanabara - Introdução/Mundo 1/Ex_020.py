#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro aluno e mostre a ordem sorteada.

from random import sample

print(f'\n{'- Informe os 4 nomes, e eu sorteio uma ordem de apresentação -':^67}\n')

primeiroNome = input('Qual o 1º nome? ')
segundoNome= str(input('Qual o 2º nome? '))
terceiroNome = input('Qual o 3º nome? ')
quartoNome = str(input('Qual o 4º nome? '))

print(f'\nA ordem de apresentação ficou {sample([primeiroNome.capitalize(), segundoNome.capitalize(), terceiroNome.capitalize(), quartoNome.capitalize()], k=4)}. \n')