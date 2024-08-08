#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print(f'\n{'- Informe o salário, e eu te devolvo o mesmo com o aumento -':^65}\n')

salárioInicial = float(input('Qual o valor do salário? R$'))

aumentoDoSalário = salárioInicial * 15 / 100

print(f'\nO salário de R${salárioInicial:.2f} com o aumento de 15%, ficará em R${(salárioInicial + aumentoDoSalário):.2f}\n')