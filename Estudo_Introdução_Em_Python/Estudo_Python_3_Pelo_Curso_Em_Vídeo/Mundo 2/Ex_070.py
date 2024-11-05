#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final mostre: A)Qual é o tatal gasto na compra; B)Quantos produtos custam mais de R$1000; C)Qual é o nome do produto mais barato e o seu preço.

print(f'\n{'- Me informe o nome e o preço de alguns produtos, e eu te devolvo algumas informações sobre os mesmos -':^108}')

quantidadeDeProdutos = 1
perguntaSobreAdicionarMaisProduto = ''
totalDosPreços = quantidadeDeProdutosMaisDeMil = 0
produtoComMenorPreço = []

while perguntaSobreAdicionarMaisProduto != 'n':
    print(f'\n{f' {quantidadeDeProdutos}º Produto ':=^30}')
    
    nomeDoProduto = input('Nome: ').strip()
    preçoDoProduto = float(input('Preço: R$'))

    totalDosPreços += preçoDoProduto

    if preçoDoProduto > 1000:
        quantidadeDeProdutosMaisDeMil += 1

    if produtoComMenorPreço == []:
        produtoComMenorPreço.append(nomeDoProduto)
        produtoComMenorPreço.append(preçoDoProduto)
    else:
        if preçoDoProduto < produtoComMenorPreço[1]:
            produtoComMenorPreço.clear()
            produtoComMenorPreço.append(nomeDoProduto)
            produtoComMenorPreço.append(preçoDoProduto)

    print()

    while True:
        perguntaSobreAdicionarMaisProduto = input('Quer adicionar mais um produto(S/N)? ').strip().lower()

        if perguntaSobreAdicionarMaisProduto not in ['n', 's']:
            print('\033[31mAPENAS É ACEITO S (sim) OU N (não)\033[m\n')
        else:
            quantidadeDeProdutos += 1
            break

pluralDeCustam = pluralDeProdutos = ''

if quantidadeDeProdutosMaisDeMil != 1:
    pluralDeCustam = 'm'
    pluralDeProdutos = 's'

print(f'\nO total da compra foi de R${totalDosPreços:.2f}, apenas {quantidadeDeProdutosMaisDeMil} produto{pluralDeProdutos} custa{pluralDeCustam} mais de R$1000.00, o produto mais barato foi {produtoComMenorPreço[0]} que custa R${produtoComMenorPreço[1]:.2f}.\n')