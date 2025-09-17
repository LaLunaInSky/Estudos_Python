#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fiboncacci.
#Ex: 0→1→1→2→3→5→8

print(f'\n{'- Me informe um número qualquer, e eu te devolvo esse número de primeiros elementos da Sequência de Fibonacci -':^116}\n')

númeroInformado = int(input('Qual número você quer? '))
contador = 1
primeiroTermoDaSequência = 0
segundoTermoDaSequência = 1

print()

while True:
    if contador == 1:
        penúltimoTermoDaSequência = primeiroTermoDaSequência
        próximoTermoDaSequência = penúltimoTermoDaSequência
    elif contador == 2:
        próximoTermoDaSequência = segundoTermoDaSequência
    else:
        penúltimoTermoDaSequência = próximoTermoDaSequência
        próximoTermoDaSequência = primeiroTermoDaSequência + segundoTermoDaSequência
        primeiroTermoDaSequência = penúltimoTermoDaSequência
        segundoTermoDaSequência = próximoTermoDaSequência

    if contador == númeroInformado:
        print(f'{próximoTermoDaSequência}\n')
        break
    else:
        print(f'{próximoTermoDaSequência} → ', end='')
    
    contador += 1    
    