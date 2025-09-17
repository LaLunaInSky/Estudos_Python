from os import system

def obterPreçoDoProduto():
    input_user = round(float(input("Qual o preço do produto? R$")), 2)
    return input_user


def obterNovoPreçoComDesconto(preço_produto):
    novo_preço = round((preço_produto - (preço_produto * (5 / 100))), 2)
    return novo_preço


def mostrarResultado(preço_produto, preço_produto_com_desconto):
    print(f"\nO produto com o valor de R${preço_produto}, com 5% fica R${preço_produto_com_desconto}.\n")


def main():
    system("clear")

    preço_do_produto = obterPreçoDoProduto()
    novo_preço_do_produto = obterNovoPreçoComDesconto(preço_do_produto)

    mostrarResultado(preço_do_produto, novo_preço_do_produto)


main()