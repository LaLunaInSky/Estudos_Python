#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27

print(f'\n{'- Me informe quantos Reais você tem, e te digo quantos Dólares você consegue comprar -':^91}\n')

quantidadeDeReais = float(input('Quantos (Reais) R$: '))

quantidadeDeDólar = quantidadeDeReais / 3.27

print(f'\nVocê possui R${quantidadeDeReais:.2f}, covertendo em Dólares é igual a US${quantidadeDeDólar:.2f}\n')