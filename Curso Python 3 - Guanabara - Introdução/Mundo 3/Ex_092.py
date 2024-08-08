#Crie um programa que leia nome, ano de nascimeno e carteira de trabalho e cadastre-os(com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO, 
#o dicionário receberá também o ano de cotratação e o salário. Calcule e acrescente a idade que a pessoa vai se aposentar.

from datetime import date

print(f'\n{'- Me informe o nome, o ano de nascimento e a carteira de trabalho de uma pessoa -':^86}\n')

dadosDaPessoa = {}

dadosDaPessoa['nome'] = input('Nome da pessoa: ').strip().capitalize()
dadosDaPessoa['ano de nascimento'] = int(input(f'Ano de nascimento de {dadosDaPessoa["nome"]}: '))
dadosDaPessoa['idade'] = date.today().year - dadosDaPessoa['ano de nascimento']
dadosDaPessoa['CTPS'] = {}

dadosDaPessoa['CTPS']['número do CTPS'] =  int(input('Qual o número da CTPS (0 não tem)? '))

if dadosDaPessoa['CTPS']['número do CTPS'] > 0:
    dadosDaPessoa['CTPS']['ano de contratação'] = int(input('Qual o ano de contratação? '))
    dadosDaPessoa['CTPS']['salário'] = float(input('Qual o salário? R$'))
    dadosDaPessoa['CTPS']['idade da aposentadoria'] = 60

print('\n'+'=-'*22)

for key, values in dadosDaPessoa.items():
    if key == 'CTPS':
        print(f' → {key} é igual a', end=' ')
    else:
        print(f' → {key.title()} é igual a', end=' ')

    if key == 'CTPS' and values['número do CTPS'] >= 0:
        print(f'{values['número do CTPS']}.')

        if values['número do CTPS'] > 0:
            for key2, values2 in dadosDaPessoa['CTPS'].items():
                if key2 == 'salário':
                    print(f' → {key2.title()} é igual a R${values2:.2f}.')
                elif key2 != 'número do CTPS':
                    print(f' → {key2.title()} é igual a {values2}.')   

    else:
        print(f'{values}.')

print('=-'*22+'\n')