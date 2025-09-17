#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

print(f'\n{'- Me informe os números para completar a matriz 3x3 -':^58}\n')

matriz3x3 = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz3x3[linha].append(int(input(f'Qual o número da [{linha} x {coluna}]? ')))
            
print(f'''
{matriz3x3[0]}
{matriz3x3[1]}
{matriz3x3[2]}
''')