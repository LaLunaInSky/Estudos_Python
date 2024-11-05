#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada.

print(f'\n{'- Me informe um número e eu te retorno o seu dobro, triplo e sua raiz quadrada -':^85}\n')

númeroInformado = int(input('Escolha um número: '))

print(f'''\nO número informado foi o {númeroInformado}:
O dobro de {númeroInformado} é igual a {númeroInformado*2};
O triplo de {númeroInformado} é igual a {númeroInformado*3};
A raiz quadrada de {númeroInformado} é igual a {númeroInformado**(1/2):.2f}.
\n''')