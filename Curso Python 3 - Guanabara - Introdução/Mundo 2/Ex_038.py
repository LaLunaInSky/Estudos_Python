#Escreva umprograma que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

print(f'\n{'- Me informe 2 números, e eu te digo qual é o maior, ou se são iguais -':^76}\n')

primeiroNúmero = int(input('Qual o 1º Número? '))
segundoNúmero = int(input('Qual o 2º Número? '))

if primeiroNúmero > segundoNúmero:
    print(f'\nO 1º número ({primeiroNúmero}) é MAIOR que o 2º número ({segundoNúmero}).\n')
elif primeiroNúmero < segundoNúmero:
    print(f'\nO 2º número ({segundoNúmero}) é MAIOR que o 1º número ({primeiroNúmero}).\n')
else:
    print(f'\nO 1º número ({primeiroNúmero}) e o 2º número ({segundoNúmero}) SÃO IGUAIS! Não existe valor maior.\n')