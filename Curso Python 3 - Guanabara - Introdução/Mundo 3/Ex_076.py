#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços,
#organizando os dados em forma tabular.

print(f'\n{'- Irei te mostrar um lista de produtos -':^50}\n')

listaDeProdutosEPreços = ('lápis', 1.75, 'borracha', 2.0, 'caderno', 15.9, 'estojo', 25.0, 'transferidor', 4.2, 'compasso', 9.99, 
'mochila', 120.32, 'canetas', 22.3, 'livro', 34.9)

print(f'{'=-'*25}\n{' Listagem de Preços ':^50}\n{'=-'*25}')

for posiçãoDoProdutoEPreço, produtoEPreço in enumerate(listaDeProdutosEPreços):
    if posiçãoDoProdutoEPreço % 2 == 0:
        print(f'{produtoEPreço.capitalize():.<40}R$', end=' ')
    else:
        print(f'{produtoEPreço:>7.2f}')

print(f'{'=-'*25}\n')