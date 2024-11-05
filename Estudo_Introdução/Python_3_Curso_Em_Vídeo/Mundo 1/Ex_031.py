#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
#cobrando R$0.50 por Km para viagem de até 200Km e R$0.45 para viagens mais longas.

print(f'\n{'- Informe a distância em Km da viagem, e eu te devolvo o valor da passagem -':^81}\n')

distânciaPercorridaDaViagem = float(input('Qual a distância em Km da sua viagem? '))

print(f'\nA sua viagem de {distânciaPercorridaDaViagem:.1f}Km custará o valor de', end=' ')

if distânciaPercorridaDaViagem <= 200:
    print(f'R${distânciaPercorridaDaViagem * 0.50 :.2f}.\n')
else:
    print(f'R${distânciaPercorridaDaViagem * 0.45 :.2f}. \n')