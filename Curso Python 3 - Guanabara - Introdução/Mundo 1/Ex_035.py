#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print(f'\n{'- Me informe 3 comprimentos, e eu te digo se eles podem formar um triângulo -':^82}\n')

primeiroComprimento = float(input('Qual o 1º comprimento? '))
segundoComprimento = float(input('Qual o 2º Comprimento? '))
terceiroComprimento = float(input('Qual o 3º Comprimento? '))

print(f'\nOs comprimentos {primeiroComprimento}, {segundoComprimento} e {terceiroComprimento}', end=' ')

if primeiroComprimento + segundoComprimento > terceiroComprimento and primeiroComprimento + terceiroComprimento > segundoComprimento and segundoComprimento + terceiroComprimento > primeiroComprimento:
    print('podem formar um TRIÂNGULO.\n')
else:
    print('não podem formar um TRIÂNGULO.\n')