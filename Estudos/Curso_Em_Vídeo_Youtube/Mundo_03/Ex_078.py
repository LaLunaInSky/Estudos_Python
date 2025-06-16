#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print(f'\n{'- Me informe 5 números inteiros, e eu te digo suas posições e o maior e o menor entre eles -':^97}\n')

listaDeNúmerosDigitados = []

for contagem in range(0, 5):
    listaDeNúmerosDigitados.append(int(input(f'Digite o número da posição {contagem}: ')))

maiorNúmeroDigitado = max(listaDeNúmerosDigitados)
menorNúmeroDigitado = min(listaDeNúmerosDigitados)
listaDePosiçãoMaior = [] 
listaDePosiçãoMenor = []

print(f'''\nOs números digitados foram os: {listaDeNúmerosDigitados}.
O maior número entre eles foi o ({maiorNúmeroDigitado}), na posição:''', end=' ')

for posição in range(0, listaDeNúmerosDigitados.count(maiorNúmeroDigitado)):
    if posição == 0:
        listaDePosiçãoMaior.append(listaDeNúmerosDigitados.index(maiorNúmeroDigitado))
    else:
        listaDePosiçãoMaior.append(
            listaDeNúmerosDigitados.index(maiorNúmeroDigitado, (listaDePosiçãoMaior[posição - 1] + 1))
        )
    
    print(f'{listaDePosiçãoMaior[posição]}..', end=' ')

print(f'\nO menor número entre eles foi o ({menorNúmeroDigitado}), na posição:', end=' ')

for posição in range(0, listaDeNúmerosDigitados.count(menorNúmeroDigitado)):
    if posição == 0:
        listaDePosiçãoMenor.append(listaDeNúmerosDigitados.index(menorNúmeroDigitado))
    else:
        listaDePosiçãoMenor.append(
            listaDeNúmerosDigitados.index(menorNúmeroDigitado, (listaDePosiçãoMenor[posição - 1] + 1))
        )
    print(f'{listaDePosiçãoMenor[posição]}..', end=' ')

print('\n')