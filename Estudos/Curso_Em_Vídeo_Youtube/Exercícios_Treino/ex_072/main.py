from os import system

def obterONúmeroInteiroEntreZeroEVinteDoUsuário() -> int:
    while True:
        número_inteiro_entre_zero_e_vinte_digitado_pelo_usuário: int = int(input("Digite um número inteiro [entre 0 e 20]: "))

        if número_inteiro_entre_zero_e_vinte_digitado_pelo_usuário >= 0 and número_inteiro_entre_zero_e_vinte_digitado_pelo_usuário <= 20:
            return número_inteiro_entre_zero_e_vinte_digitado_pelo_usuário
        
        else:
            system("clear")


def retornarPorExtensoONúmeroInteiroInformadoEntreZeroEVinte(número_digitado_pelo_usuário: int) -> None:
    números_por_extenso: tuple = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

    print(f"\nVocê digitou o número {números_por_extenso[número_digitado_pelo_usuário].capitalize()}. \n")


def main() -> None:
    system("clear")

    número_inteiro_digitado_pelo_usuário: int = obterONúmeroInteiroEntreZeroEVinteDoUsuário()

    retornarPorExtensoONúmeroInteiroInformadoEntreZeroEVinte(número_inteiro_digitado_pelo_usuário)


main()