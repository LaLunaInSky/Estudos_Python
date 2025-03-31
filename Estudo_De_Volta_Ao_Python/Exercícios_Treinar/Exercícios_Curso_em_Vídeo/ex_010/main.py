from os import system

def obterQuantidadeDeDinheiro():
    input_user = round(float(input("Digite quanto de dinheiro tem na sua carteira: R$")), 2)
    return input_user


def mostrarResultado(dinheiro_na_carteira):
    dolar = 3.27

    print(f"\nCom R${dinheiro_na_carteira} na sua carteira, você pode comprar US${round((dinheiro_na_carteira / dolar), 2)}.\n")


def main():
    system("clear")

    dinheiro_na_carteira = obterQuantidadeDeDinheiro()

    mostrarResultado(dinheiro_na_carteira)


main()