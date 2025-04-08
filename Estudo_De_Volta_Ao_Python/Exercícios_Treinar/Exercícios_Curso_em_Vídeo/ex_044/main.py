from os import system

def obterPreçoDasComprasDoUsuário() -> float:
    valor_total_das_compras: float = float(input("Qual o valor total das suas compras? R$"))
    return valor_total_das_compras


def tranformarValorEmMonetário(valor: float) -> str:
    return f"R${valor:.2f}".replace('.', ',')


def mostrarOValorÀVistaNoDinheiroOuCheque(valor_dos_produtos: float) -> None:
    valor_com_10_porcento_de_desconto: float = valor_dos_produtos - (valor_dos_produtos * (10 / 100))

    print(f"A compra de {tranformarValorEmMonetário(valor_dos_produtos)}, à vista no dinheiro ou cheque fica {tranformarValorEmMonetário(valor_com_10_porcento_de_desconto)}.\n")


def mostrarOValorÀVistaNoCartão(valor_do_produto: float) -> None:
    valor_com_5_porcento_de_desconto: float = valor_do_produto - (valor_do_produto * (5 / 100))

    print(f"A compra de {tranformarValorEmMonetário(valor_do_produto)}, à vista no cartão fica {tranformarValorEmMonetário(valor_com_5_porcento_de_desconto)}.\n")


def mostrarOValor2VezesNoCartão(valor_do_produto: float) -> None:
    valor_de_cada_parcela: float = valor_do_produto / 2

    print(f"O valor de {tranformarValorEmMonetário(valor_do_produto)}, em 2x no cartão fica com parcelas de {tranformarValorEmMonetário(valor_de_cada_parcela)}.\n")


def mostrarOValor3VezesOuMaisNoCartão(valor_do_produto: float) -> None:
    quantidade_de_parcelas: int = 3
    
    while True:
        quantidade_de_parcelas: int = int(input(f"Quantas parcelas será o pagamento da compra {tranformarValorEmMonetário(valor_do_produto)}? "))

        if quantidade_de_parcelas >= 3:
            break
        else:
            system("clear")

    valor_de_cada_parcela: float = valor_do_produto / quantidade_de_parcelas

    valor_de_cada_parcela_com_20_porcento_de_acrescimo: float = valor_de_cada_parcela + (valor_de_cada_parcela * (20 / 100))

    valor_total_da_compra: float = valor_de_cada_parcela_com_20_porcento_de_acrescimo * quantidade_de_parcelas

    print(f"O valor de {tranformarValorEmMonetário(valor_do_produto)}, em {quantidade_de_parcelas}x no cartão fica com parcelas de {tranformarValorEmMonetário(valor_de_cada_parcela_com_20_porcento_de_acrescimo)} com juros.\nO valor final da compra é de {tranformarValorEmMonetário(valor_total_da_compra)}.\n")


def menuDeOpçõesDeFormaDePagamento(valor_dos_produtos: float) -> None:
    while True:
        print(f'''
Escolha um forma de Pagamento para a compra de {tranformarValorEmMonetário(valor_dos_produtos)}:
[ 1 ] À vista no dinheiro ou cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
        
        opção_escolhida: int = int(input("Qual a opção escolhida? "))

        if opção_escolhida >= 1 and opção_escolhida <= 4:
            if opção_escolhida == 1:
                mostrarOValorÀVistaNoDinheiroOuCheque(valor_dos_produtos)
            elif opção_escolhida == 2:
                mostrarOValorÀVistaNoCartão(valor_dos_produtos)
            elif opção_escolhida == 3:
                mostrarOValor2VezesNoCartão(valor_dos_produtos)
            elif opção_escolhida == 4:
                mostrarOValor3VezesOuMaisNoCartão(valor_dos_produtos)
            break
        else:
            system("clear")


def main() -> None:
    system("clear")

    preço_das_compras_do_usuário: float = obterPreçoDasComprasDoUsuário()

    menuDeOpçõesDeFormaDePagamento(preço_das_compras_do_usuário)


main()