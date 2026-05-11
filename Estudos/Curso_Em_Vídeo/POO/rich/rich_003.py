from rich.console import Console
from rich.table import Table
from rich import inspect

console = Console()

def formatarPreco(
    valor = 0.0
) -> str:
    return f"R$ {valor:.2f}".replace(".", ",")

class Produto:
    def __init__(
            self, 
            nome, 
            preco,
            tabela
        ):
        self.nome = nome

        self.preco = formatarPreco(preco)

        tabela.add_row(
            self.nome.title(),
            self.preco
        )

tabela_de_produtos = Table(title="\nTabela de Produtos")

tabela_de_produtos.add_column(
    "Produto",
    justify="left",
    style="red"
)

tabela_de_produtos.add_column(
    "Preço",
    justify="center",
    style="blue"
)

produto_lapis = Produto(
    "lápis",
    1.5,
    tabela_de_produtos
)

produto_borracha = Produto(
    "borracha",
    5,
    tabela_de_produtos
)

# inspect(produto_borracha)

console.print(tabela_de_produtos)