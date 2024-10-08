#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro),
#e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$ 1.

print(f'\n{'- Me informe o valor a ser sacado, e eu te devolvo a quantidade de cédulas -':^81}\n')

valorASerSacado = int(input(f'{' Caixa Eletrônico ':=^50}\nQual o valor que você quer sacar? R$'))

quantidadeDe50 = quantidadeDe20 = quantidadeDe10 = quantidadeDe1 = 0

print('='*50)
print()

while True:
    pluralCédulas = ''

    if valorASerSacado // 50 != 0:
        quantidadeDe50 = valorASerSacado // 50
        valorASerSacado %= 50

        if quantidadeDe50 != 1:
            pluralCédulas = 's'

        print(f'→ {quantidadeDe50} cédula{pluralCédulas} de R$50')

    elif valorASerSacado // 20 != 0:
        quantidadeDe20 = valorASerSacado // 20
        valorASerSacado %= 20

        if quantidadeDe20 != 1:
            pluralCédulas = 's'

        print(f'→ {quantidadeDe20} cédula{pluralCédulas} de R$20')

    elif valorASerSacado // 10 != 0:
        quantidadeDe10 =  valorASerSacado // 10
        valorASerSacado %= 10

        if quantidadeDe10 != 1:
            pluralCédulas = 's'

        print(f'→ {quantidadeDe10} cédula{pluralCédulas} de R$10')

    elif valorASerSacado // 1 != 0:
        quantidadeDe1 = valorASerSacado // 1
        valorASerSacado %= 1
        
        if quantidadeDe1 != 1:
            pluralCédulas = 's'

        print(f'→ {quantidadeDe1} cédula{pluralCédulas} de R$1')

    else:
        break

print()