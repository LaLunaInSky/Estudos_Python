from os import system 

def obterSalárioDoUsuário() -> float:
    salário_digitado: float = float(input("Digite o seu salário: R$"))
    return salário_digitado


def analisarSalárioEDarAumento(salário_digitado: float) -> float:
    if salário_digitado <= 1250:
        return salário_digitado + (salário_digitado * (15 / 100))
    else:
        return salário_digitado + (salário_digitado * (10 / 100))


def formatarSalárioComMonetário(salário_digitado: float) -> str:
    return f"{salário_digitado:.2f}".replace('.', ',')


def mostrarResultado(salário_sem_aumento: float, salário_com_aumento: float) -> None:
    print(f'''
O salário de R${formatarSalárioComMonetário(salário_sem_aumento)} com o aumento ficará R${formatarSalárioComMonetário(salário_com_aumento)}.
''')


def main() -> None:
    system("clear")

    salário_do_usuário: float = obterSalárioDoUsuário()
    salário_do_usuário_com_aumento = analisarSalárioEDarAumento(salário_do_usuário)

    mostrarResultado(salário_do_usuário, salário_do_usuário_com_aumento)


main()