from os import system

def obterVelocidadeDoCarroDoUsuário() -> int:
    velocidade_do_carro: int = int(input("Qual a velocidade do seu carro? "))
    return velocidade_do_carro


def analisarSeLevouMulta(velocidade_do_carro: int) -> None:
    limite_de_velocidade = 80
    
    print(f"\nO LIMITE DE VELOCIDADE DA VIA É DE {limite_de_velocidade}Km/h")

    if velocidade_do_carro < limite_de_velocidade:
        print("Você está no abaixo do limite, siga com cuidado e use sempre sinto de segurança!\n")
    elif velocidade_do_carro == limite_de_velocidade:
        print("Você está no limite, siga com cuidado e use sempre sinto de segurança!\n")
    else:
        valor_a_ser_pago: float = ((velocidade_do_carro - limite_de_velocidade) * 7.00)
        valor_formatado: str = f"{valor_a_ser_pago:.2f}".replace('.', ',')

        print(f"VOCÊ FOI MULTADO, o valor a ser pago é de R${valor_formatado}.\n")


def main() -> None:
    system("clear")

    velocidade_do_carro_do_usuário: int = obterVelocidadeDoCarroDoUsuário()

    analisarSeLevouMulta(velocidade_do_carro_do_usuário)


main()