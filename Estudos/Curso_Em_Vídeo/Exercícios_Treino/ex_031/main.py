from os import system

def obterKmsDaViagemDoUsuário() -> int:
    kms_da_viagem: int = int(input("Qual é a distância da sua viagem (em Km)? "))
    return kms_da_viagem


def analisarOValorDaViagem(kms_da_viagem: int) -> float:
    valor_até_200Km: float = 0.50
    valor_acima_de_200Km: float = 0.45

    if kms_da_viagem <= 200:
        return (kms_da_viagem * 0.50)
    else: 
        return ( kms_da_viagem * 0.45)


def transformarValorEmMonetário(valor: float) -> str:
    valor_em_monetário: str = f"{valor:.2f}".replace('.', ',')
    return valor_em_monetário


def mostrarResultados(kms_viagem: int, valor_viagem: float) -> None:
    valor_da_viagem_em_monetário: str = transformarValorEmMonetário(valor_viagem)

    print(f"\nA sua viagem de {kms_viagem}Km, vai custar o valor de R${valor_da_viagem_em_monetário}.\n")


def main() -> None:
    system("clear")

    kms_da_viagem_do_usuário: int = obterKmsDaViagemDoUsuário()
    valor_final_da_viagem: float = analisarOValorDaViagem(kms_da_viagem_do_usuário)

    mostrarResultados(kms_da_viagem_do_usuário, valor_final_da_viagem)


main()