#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print(f'\n{'- Me informe um número, e eu te digo o seu antecessor e sucessor -':^70}\n')

númeroInformado = int(input('Escolha um número: '))

print(f'\nO número escolhido foi o {númeroInformado}, o seu antecessor é o {númeroInformado-1} e o seu sucessor é o {númeroInformado+1}.\n')