#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print(f'\n{'- Informe o preço do produto, e eu te devolvo o novo preço com o desconto -':^80}\n')

preçoInicialDoProduto = float(input('Qual o preço do produto? R$'))

descontoDoPreçoInicial = (5*preçoInicialDoProduto)/100

print(f'\nO produto com valor de R${preçoInicialDoProduto:.2f} com o desconto de 5%, ficará pelo preço de R${(preçoInicialDoProduto-descontoDoPreçoInicial):.2f}\n')