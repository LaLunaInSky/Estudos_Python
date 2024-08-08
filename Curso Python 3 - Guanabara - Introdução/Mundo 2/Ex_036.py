#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print(f'\n{'- Para liberar o empréstimo me informe o valor da casa, o seu salário e em quantos anos vai pagar tudo -':^109}\n')

valorDaCasa = float(input('Qual o valor da Casa? R$'))
salárioDoComprador = float(input('Qual o seu salário? R$'))
quantidadeDeAnosParaPagar = int(input('Em quantos anos quer pagar? '))

valorDaPrestaçãoMensal = 80000 / (7 * 12)

print(f'''\nA casa no valor de R${valorDaCasa:.2f} com a inteção de pagar em {quantidadeDeAnosParaPagar} anos, com base no seu salário de R${salárioDoComprador:.2f},
Terá a Prestação mensal no valor de R${valorDaPrestaçãoMensal:.2f}, logo o Empréstimo está''', end=' ')

if valorDaPrestaçãoMensal <= (salárioDoComprador * 30 / 100):
    print('APROVADO!\n')
else:
    print('NEGADO!\n')