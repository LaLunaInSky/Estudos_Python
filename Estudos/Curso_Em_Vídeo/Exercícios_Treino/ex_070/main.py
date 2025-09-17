from os import system

def mostradorNomeDaLoja() -> None:
    print(f'''{"-"*40}
{"LOJA BARATÃO":^40}
{"-"*40}''')
    

def obterONomeDoProduto() -> str:
    nome_do_produto: str = str(input("Qual o nome? "))
    return nome_do_produto


def obterOPreçoDoProduto() -> float:
    preço_do_produto: float = float(input("Qual o preço? R$"))
    return preço_do_produto


def mostradorDoCadastroDoProdutoX(ordem_do_produto: int = 1) -> tuple:
    print(f"{f"Cadatro do {ordem_do_produto}º Produto":^40}\n{"-"*40}")

    nome_do_produto: str = obterONomeDoProduto()
    preço_do_produto: float = obterOPreçoDoProduto()

    return (nome_do_produto, preço_do_produto)


def perguntarSeQuerAdicionarMaisUmProduto(ordem_do_produto: int, nome_do_produto: str, preço_do_produto: float) -> str:
    while True:
        pergunta_se_quer_adicionar_mais_um_produto: str = str(input("\nQuer adicionar mais um produto [S/N]? ")).lower()

        if pergunta_se_quer_adicionar_mais_um_produto == 's' or pergunta_se_quer_adicionar_mais_um_produto == 'n':
            system("clear")
            return pergunta_se_quer_adicionar_mais_um_produto

        else:
            system("clear")

            mostradorNomeDaLoja()
            print(f"{f"Cadatro do {ordem_do_produto}º Produto":^40}\n{"-"*40}")
            print(f"Qual o nome? {nome_do_produto}\nQual o preço? R${preço_do_produto:.2f}")



def organizadorDoCadastroDeProdutos() -> list:
    produtos_cadastrados: list = []
    
    while True:
        mostradorNomeDaLoja()

        produtos_cadastrados.append(mostradorDoCadastroDoProdutoX(len(produtos_cadastrados) + 1))

        resposta_se_quer_adicionar_mais_um_produto: str = perguntarSeQuerAdicionarMaisUmProduto(len(produtos_cadastrados), produtos_cadastrados[-1][0], produtos_cadastrados[-1][1])

        if resposta_se_quer_adicionar_mais_um_produto == 's':
            system("clear")

        else:
            return produtos_cadastrados
        

def somarOsPreçosDosProdutosCadastrados(produtos_cadastrados: list) -> float:
    valor_total_dos_produtos_cadastrados: float = 0

    for produto in produtos_cadastrados:
        valor_total_dos_produtos_cadastrados += produto[1]

    return valor_total_dos_produtos_cadastrados


def analisarQuantosProdutosSãoSuperioresAMilReais(produtos_cadastrados: list) -> int:
    quantidade_de_produtos_superiores_a_mil_reais: int = 0

    for produto in produtos_cadastrados:
        if produto[1] > 1000:
            quantidade_de_produtos_superiores_a_mil_reais += 1

    return quantidade_de_produtos_superiores_a_mil_reais


def analisarOProdutoCadastradoComMenorPreço(produtos_cadastrados: list) -> tuple:
    produtos_com_menor_preço: tuple = ()
    
    for posição, produto in enumerate(produtos_cadastrados):
        if posição == 0:
            produtos_com_menor_preço = produto

        if produtos_com_menor_preço[1] > produto[1]:
            produtos_com_menor_preço = produto
    
    return produtos_com_menor_preço


def mostrarInformaçõesDosProdutosCadastrados(produtos_cadastrados: list) -> None:
    system("clear")
    
    produto_com_o_menor_preço: tuple = analisarOProdutoCadastradoComMenorPreço(produtos_cadastrados)

    print(f'''
O valor final dos produtos cadastrados é de R${somarOsPreçosDosProdutosCadastrados(produtos_cadastrados):.2f},
ao total possui {analisarQuantosProdutosSãoSuperioresAMilReais(produtos_cadastrados)} produtos com o valor superior a de R$1000.00,
O produto mais barato cadastrado foi o {produto_com_o_menor_preço[0]} com o valor de R${produto_com_o_menor_preço[1]:.2f}.
''')


def main() -> None:
    system("clear")

    produtos_cadastrados: list = organizadorDoCadastroDeProdutos()

    mostrarInformaçõesDosProdutosCadastrados(produtos_cadastrados)


main()