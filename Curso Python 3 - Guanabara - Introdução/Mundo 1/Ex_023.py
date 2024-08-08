#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separado.
#Ex: 1894 - unidade:4 dezana:3 centena:8 - milhar:1

print(f'\n{'- Me informe um número que vai de 0 a 9999, e eu te devolvo a unidade, dezena, centena e milhar do mesmo -':^111}\n')

númeroInformado =  input('Qual o número? ')

print(f'''
O número informado foi {númeroInformado}:
A unidade é {númeroInformado.zfill(4)[3]}, a dezena é {númeroInformado.zfill(4)[2]}, a centena é {númeroInformado.zfill(4)[1]}, a milhar é {númeroInformado.zfill(4)[0]}.
''')