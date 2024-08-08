#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta e:
#A)A soma de todos os valores pares digitados. B)A soma dos valores da terceira coluna. C)O maior valor da segunda linha.

print(f'\n{'- Me informe número para formar uma matriz 3x3, e eu te devolvo algumas informações -':^90}\n')

matriz3x3 = [[], [], []]
contagem = 1
somaDosPares = somaDaTerceiraColuna = 0

while contagem != 3:
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if contagem == 1:
                matriz3x3[linha].append(int(input(f'Qual o número da [{linha} x {coluna}]? ')))

            else:
                print(f'[{matriz3x3[linha][coluna]:^5}]', end='')

                if matriz3x3[linha][coluna] % 2 == 0:
                    somaDosPares += matriz3x3[linha][coluna]

                if coluna == 2:
                    somaDaTerceiraColuna += matriz3x3[linha][2]

        if contagem == 2:
            print()
    
    contagem += 1
    print()

print(f'''A soma de todos os valores pares é de {somaDosPares}.
A soma dos valores da terceira coluna é de {somaDaTerceiraColuna}.
O maior valor da segunda linha é {max(matriz3x3[1])}.
''')