#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

print(f'\n{'- Informe 3 números, e eu te falarei qual é o menor e o maior entre eles -':^79}\n')

primeiroNúmero = int(input('Qual o 1º Número? '))
segundoNúmero = int(input('Qual o 2º Número? '))
terceiroNúmero = int(input('Qual o 3º Número? '))

if primeiroNúmero > segundoNúmero < terceiroNúmero:
   menorNúmero = segundoNúmero
elif primeiroNúmero > terceiroNúmero < segundoNúmero:
    menorNúmero = terceiroNúmero
else:
   menorNúmero = primeiroNúmero

if primeiroNúmero < segundoNúmero > terceiroNúmero:
   maiorNúmero = segundoNúmero
elif primeiroNúmero < terceiroNúmero > segundoNúmero:
   maiorNúmero = terceiroNúmero
else:
   maiorNúmero = primeiroNúmero

print(f'\nO número MENOR é o {menorNúmero} e o MAIOR é o {maiorNúmero}. \n')