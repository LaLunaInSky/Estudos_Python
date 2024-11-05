#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia, e R$0.15 por Km rodado.

print(f'\n{'- Me informe a quantidade de dias e de quilometros rodados com o carro alugado, e eu te devolvo o preço final a pagar -':^124}\n')

diasComOCarro = int(input('Quantos dias você ficou com o carro? '))

kmRodadoComOCarro = float(input('Quantos quilometros rodado? '))

preçoFinalAPagar = (kmRodadoComOCarro * 0.15) + (diasComOCarro * 60)

print(f'\nO carro alugado percorreu {kmRodadoComOCarro}km em {diasComOCarro} dias, o preço final a pagar fica em R${preçoFinalAPagar:.2f}\n')