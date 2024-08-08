#Elabore um programa que calcule o valor a ser poago por um produto, considerando o seu preço normal e condição de pagamento:
#-À vista dinheiro/cheque: 10% de desconto
#-À vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros

from time import sleep

print(f'\n{'- Me informe o valor do produto e a forma de pagamento, e eu te devolvo o valor final -':^92}\n')

valorDoProduto = float(input('Qaul o preço do produto? R$'))

formaDePagamento = 0

while formaDePagamento not in [1,2,3,4]:

    print('''
Qual será a forma de pagamento?
[ 1 ] À vista no Dinheiro ou Cheque
[ 2 ] À vista o Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')

    formaDePagamento = int(input('Informe o número: '))

    if formaDePagamento not in [1,2,3,4]:
        print('\nApenas as opções 1, 2, 3 ou 4 são aceitas! Tente de novo!')

        sleep(2)

    if formaDePagamento == 1:
        print(f'\nO produto que custa R${valorDoProduto:.2f}, com o pagamento à vista no dinheiro ou cheque terá 10% de desconto, custando agora R${valorDoProduto - ((valorDoProduto * 10) / 100):.2f}.\n')

    elif formaDePagamento == 2:
        print(f'\nO produto que custa R${valorDoProduto:.2f}, com o pagamento à vista no cartão terá 5% de desconto, custando agora R${valorDoProduto - ((valorDoProduto * 5) / 100):.2f}.\n')

    elif formaDePagamento == 3:
        print(f'\nO produto que custa R${valorDoProduto:.2f}, com o pagamento em 2x no cartão não terá desconto, ficando 2 parcelas de R${valorDoProduto / 2:.2f}.\n')

    elif formaDePagamento == 4:
        
        quantidadeDeParcelas = 0
        while quantidadeDeParcelas < 3:
            quantidadeDeParcelas = int(input('\nQuantas parcelas no cartão? '))

            if quantidadeDeParcelas < 3:
                print('Apenas aceitamos 3 parcelas ou mais! Tente de novo!')

        print(f'\nO produro que custa R${valorDoProduto:.2f}, com o pagamento em {quantidadeDeParcelas}x no cartão terá 20% de juros, ficando {quantidadeDeParcelas} parcelas de R${(valorDoProduto + ((valorDoProduto * 20) / 100)) / quantidadeDeParcelas:.2f}.\nCustando R${valorDoProduto + ((valorDoProduto * 20) / 100):.2f}.\n')