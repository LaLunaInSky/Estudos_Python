#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo 
#e usa algumas dessas funções. Formate o resultado em um valor monetário utilizando a função moeda().

import moedas

preçoInformado = float(input('\nQual o preço? R$'))

print()

print(f'O preço {moedas.moeda(preçoInformado)} com o aumento de 15% fica {moedas.moeda(moedas.aumentar(preçoInformado, 15))}')
print(f'O preço {moedas.moeda(preçoInformado)} com o desconto de 12% fica {moedas.moeda(moedas.diminuir(preçoInformado, 12))}')
print(f'O dobro de {moedas.moeda(preçoInformado)} é igual à {moedas.moeda(moedas.dobro(preçoInformado))}')
print(f'A metade de {moedas.moeda(preçoInformado)} é igual à {moedas.moeda(moedas.metade(preçoInformado))}')

print()