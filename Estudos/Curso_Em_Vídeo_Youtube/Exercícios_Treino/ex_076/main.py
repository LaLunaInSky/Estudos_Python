from os import system

def obterListagemDeProdutos() -> tuple:
    produtos: tuple = (
        ("lápis", 1.75),
        ("borracha", 2.0),
        ("caderno", 15.9),
        ("estojo", 25.0),
        ("transferidor", 4.2),
        ("compasso", 9.99),
        ("mochila", 120.32),
        ("canetas", 22.3),
        ("livro", 34.9)
    )

    return produtos


def mostrarTabulaçãoDosProdutos(produtos: tuple) -> None:
    print(f"{"-" * 50}\n{"Listagem de Produtos".upper():^50}\n{"-" * 50}")

    for produto in produtos:
        print(f" {produto[0].title():.<38}R$ {f"{produto[1]:.2f}".replace(".", ","):>7}")

    print("-" * 50)


def main() -> None:
    system("clear")

    lista_de_produtos: tuple = obterListagemDeProdutos()
    
    mostrarTabulaçãoDosProdutos(lista_de_produtos)


main()