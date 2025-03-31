from os import system

def obterSalário():
    input_user = round(float(input("Digite o salário do funcionário: R$")), 2)
    return input_user


def obterNovoSalárioComDesconto(salário):
    novo_salário = round(salário + (salário * (15 / 100)), 2)
    return novo_salário


def mostrarResultado(antigo_salário, novo_salário):
    print(f"\nO funcionário com o salário de R${antigo_salário}, com o aumento de 15% fica R${novo_salário}.\n")


def main():
    system("clear")

    salário_do_funcionário = obterSalário()
    novo_salário_do_funcionário = obterNovoSalárioComDesconto(salário_do_funcionário)

    mostrarResultado(salário_do_funcionário, novo_salário_do_funcionário)


main()