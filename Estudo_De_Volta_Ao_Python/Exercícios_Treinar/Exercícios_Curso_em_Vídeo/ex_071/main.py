from os import system

def mostrarLogoDoBanco() -> None:
    print(f'''{"-" * 46}
{"BANCO CEV":^46}
{"-" * 46}''')
    

def mostrarMensagemDeDespedida() -> None:
    print(f"\n{"-" * 46}\n{"Volte sempre ao BANCO CEV! Tenha um Bom Dia!":^46}\n")
    

def obterNúmeroInteiroDoUsuário() -> int:
    número_inteiro_digitado_pelo_usuário: int = int(input("Qual valor você quer sacar?  R$"))

    return número_inteiro_digitado_pelo_usuário


def analisarQuantidadeDeNotasPrecisaEntregarAoUsuário(valor_a_sacar: int) -> None:
    print()

    while valor_a_sacar != 0:
        if valor_a_sacar // 50 != 0:
            quantidade_a_dividir: int = valor_a_sacar // 50
            print(f"Total de {quantidade_a_dividir} cédulas de R$50")

            valor_a_sacar -= (50  * quantidade_a_dividir)
        else:
            if valor_a_sacar // 20 != 0:
                quantidade_a_dividir: int = valor_a_sacar // 20
                print(f"Total de {quantidade_a_dividir} cédulas de R$20")

                valor_a_sacar -= (20  * quantidade_a_dividir)
            else:
                if valor_a_sacar // 10 != 0:
                    quantidade_a_dividir: int = valor_a_sacar // 10
                    print(f"Total de {quantidade_a_dividir} cédulas de R$10")
                
                    valor_a_sacar -= (10  * quantidade_a_dividir)
                else:
                    quantidade_a_dividir: int = valor_a_sacar // 1
                    print(f"Total de {quantidade_a_dividir} cédulas de R$1")
                    
                    valor_a_sacar -= (1  * quantidade_a_dividir)

    mostrarMensagemDeDespedida()


def main() -> None:
    system("clear")

    mostrarLogoDoBanco()
    
    valor_que_o_usuário_quer_sacar: int = obterNúmeroInteiroDoUsuário()

    analisarQuantidadeDeNotasPrecisaEntregarAoUsuário(valor_que_o_usuário_quer_sacar)


main()