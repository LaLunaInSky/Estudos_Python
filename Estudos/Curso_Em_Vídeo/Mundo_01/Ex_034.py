#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250.00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.

print(f'\n{'- Me informe o salário do funcionário, e eu te repasso o mesmo com o aumento -':^83}\n')

salárioAtualDoFuncionário = float(input('Qual o salário do funcionário? R$'))

print(f'\nO salário de R${salárioAtualDoFuncionário:.2f}, com o aumento de', end=' ')

if salárioAtualDoFuncionário <= 1250.00:
    print(f'15% fica com o valor de R${salárioAtualDoFuncionário + (salárioAtualDoFuncionário * 15 / 100):.2f}.\n')
else:
    print(f'10% fica com o valor de R${salárioAtualDoFuncionário + (salárioAtualDoFuncionário * 10 / 100):.2f}.\n')