#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qualserá a base de conversão:
#- 1 para binário
#- 2 para octal
#- 3 para hexadecimal

print(f'\n{'- Me informe um número qualquer, e eu o tranformo em Binário, Octal ou Hexadecimal -':^89}\n')

númeroInformado = int(input('Qual número inteiro? '))

print(f'''Qual base você escolhe para transformar o número {númeroInformado}?
1 - Base Binária
2 - Base Octal
3 - Base Hexadecimal''')

opçãoEscolhida = int(input('Escolha de 1 a 3: '))

if opçãoEscolhida == 1:
    print(f'\nO número {númeroInformado} na Base Binária é igual a {bin(númeroInformado)[2:]}.\n')
elif opçãoEscolhida == 2:
    print(f'\nO número {númeroInformado} na Base Octal é igual a {oct(númeroInformado)[2:]}.\n')
elif opçãoEscolhida == 3:
    print(f'\nO número {númeroInformado} na Base Hexadecial é igual a {hex(númeroInformado)[2:]}.\n')
else:
    print('\nOPÇÃO INVÁLIDA, APENAS 1, 2 e 3\n')