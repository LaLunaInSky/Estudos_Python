from os import system

def obterValorDoImóvel() -> float:
    valor_do_imóvel: float = float(input("Qual o valor do imóvel? R$"))
    return valor_do_imóvel


def obterSalárioDoUsuário() -> float:
    salário_do_usuário: float = float(input("Qual o seu salário? R$"))
    return salário_do_usuário


def obterQuantosAnosQuerPagarOImóvel() -> int:
    quantidade_de_anos_para_pagar_imóvel: int = int(input("Em quantos anos pretende pagar o imóvel? "))
    return quantidade_de_anos_para_pagar_imóvel


def calcularMensalidadesAPagarDoImóvel(valor_do_imóvel: float, quantidade_de_anos_a_pagar: int) -> float:
    quantidades_de_parcelas: int = quantidade_de_anos_a_pagar * 12
    valor_de_cada_parcela: float = valor_do_imóvel / quantidades_de_parcelas
    return round(valor_de_cada_parcela, 2)


def transformarValorEmMonetário(valor: float) -> str:
    return f"{valor:.2f}".replace('.', ',')


def analisarSeOValorDaParcelaÉAté30PorcentoDoSalário(salário_do_usuário: float, valor_de_cada_parcela: float) -> bool:
    trinta_porcento_do_salário_do_usuário: float = (salário_do_usuário * (30 / 100))

    if valor_de_cada_parcela <= trinta_porcento_do_salário_do_usuário:
        return True
    else:
        return False


def mostrarResultado(valor_do_imóvel: float, quantidade_de_anos: int, valor_de_cada_parcela: float, salário_do_usuário: float, empréstimo_liberado: bool) -> None:
    liberado_empréstimo: str = ''

    if empréstimo_liberado:
        liberado_empréstimo = "LIBERADO!"
    else:
        liberado_empréstimo = "NEGADO!"

    print(f'''
O imóvel no valor de R${transformarValorEmMonetário(valor_do_imóvel)}, para ser pago em {quantidade_de_anos} anos, ficará com parcelas de R${transformarValorEmMonetário(valor_de_cada_parcela)}.
Com o seu salário de R${transformarValorEmMonetário(salário_do_usuário)}, o Empréstimo está {liberado_empréstimo}.
''')


def main() -> None:
    system("clear")

    valor_do_imóvel: float = obterValorDoImóvel()

    salário_do_usuário: float = obterSalárioDoUsuário()
    
    quantidade_de_anos_para_pagar_o_imóvel: int = obterQuantosAnosQuerPagarOImóvel()
    
    valor_de_cada_parcela: float = calcularMensalidadesAPagarDoImóvel(valor_do_imóvel, quantidade_de_anos_para_pagar_o_imóvel)
    
    empréstimo_liberado: bool = analisarSeOValorDaParcelaÉAté30PorcentoDoSalário(salário_do_usuário, valor_de_cada_parcela)

    mostrarResultado(valor_do_imóvel, quantidade_de_anos_para_pagar_o_imóvel, valor_de_cada_parcela, salário_do_usuário, empréstimo_liberado)


main()