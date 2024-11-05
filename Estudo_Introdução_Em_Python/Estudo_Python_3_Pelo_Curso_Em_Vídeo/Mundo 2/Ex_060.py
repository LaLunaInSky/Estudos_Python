#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120

print(f'\n{'- Me informe um número inteiro, e eu te devolvo o seu fatorial -':^69}\n')

númeroInformado = int(input('Qual número você escolhe? '))
resultadoDoFatorial = númeroInformado

print(f'\nO Fatorial de {númeroInformado}:\n{númeroInformado}! =', end=' ')

while númeroInformado != 0:

    if númeroInformado == 1:
        print(f'{númeroInformado} =', end=' ')
    else:
        print(f'{númeroInformado}x', end='')
    
    númeroInformado -= 1
    
    if númeroInformado != 0:
        resultadoDoFatorial *= númeroInformado  

print(f'{resultadoDoFatorial}\n')